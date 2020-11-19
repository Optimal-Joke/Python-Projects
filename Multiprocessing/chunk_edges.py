import os
import multiprocessing as mp
from collections import Counter
from astropy.io import fits
import numpy as np


def chunk(x, y):
    """Takes
    """
    NCHUNKS = os.cpu_count()

    # determine x and y bins
    xbins = np.histogram_bin_edges(x, bins='fd')
    ybins = np.histogram_bin_edges(y, bins='fd')

    # split ybins up into NCHUNKS chunks
    ybinchunks = np.array_split(ybins, NCHUNKS)

    for i in range(NCHUNKS):
        if i < (NCHUNKS-1):
            # append the first edge of the next bin to the current one to ensure coverage
            ybinchunks[i] = np.append(ybinchunks[i], ybinchunks[i+1][0])
        yield x, y, xbins, ybinchunks[i]


def cell(x, y, xedges, yedges):
    """Takes in x and y data as input, along with the preferred bins, and returns the local maximum of each cell.
    """

    # iterate through the bins on each axis
    image_maxes = []
    for j in range(len(yedges)-1):
        for i in range(len(xedges)-1):
            cell_xmin, cell_xmax = xedges[i], xedges[i+1]
            cell_ymin, cell_ymax = yedges[j], yedges[j+1]

            # isolate events within each cell
            cell_constraints = np.where((x < cell_xmax) & (
                x >= cell_xmin) & (y < cell_ymax) & (y >= cell_ymin))

            cell_x = x[cell_constraints]
            cell_y = y[cell_constraints]
            coord_pairs = list(zip(cell_x, cell_y))

            # find maximum point in cell
            max_coord_counts = Counter(coord_pairs).most_common(1)
            for result in max_coord_counts:
                image_maxes.append(result)
    return image_maxes


def find_centroids(file_path):
    """This (crude) algorithm iterates through the pixels of an image and returns the
    RA and Dec coordinates of the maxima of the image as two 1D numpy arrays.
    """

    with fits.open(f"{file_path}") as file:
        # load in RA/Dec coordinates
        MASTER_XS = np.array(file[1].data["X"])
        MASTER_YS = np.array(file[1].data["Y"])

        # create arguments for starmap function
        args = chunk(MASTER_XS, MASTER_YS)

        # run cell function with input chunks
        p = mp.Pool()
        chunk_maxes = p.starmap(cell, args)

        # unpack list of lists into single list
        image_maxes = [item for sublist in chunk_maxes for item in sublist]

        # combine event counts for locations that appeared in more than one chunk
        maxes = {}
        for loc, count in image_maxes:
            if not loc in maxes.keys():
                maxes[loc] = count
            else:
                maxes[loc] += count

        # sort the identified maxima by count and return their x(RA) and y(Dec) coordinates
        maxes = sorted(maxes.items(), key=lambda x: x[1], reverse=True)
        centroid_xs = np.array([item[0][0] for item in maxes])
        centroid_ys = np.array([item[0][1] for item in maxes])
        return centroid_xs, centroid_ys


find_centroids(
    "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified/L1517/Swift/xrt/event/sw00034249004xpcw3po_cl.evt.gz")
