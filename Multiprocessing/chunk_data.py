import os
import multiprocessing as mp
from collections import Counter
from astropy.io import fits
import numpy as np


def chunk(coords):
    """Takes a (n,2) ndarray of coordinates as input.
    Returns chunks of x and y coordinates, the number of which being determined by your machine's core count.
    """

    NCHUNKS = os.cpu_count()

    chunks = np.array_split(coords, NCHUNKS)

    x_chunks = []
    y_chunks = []
    for c in chunks:
        xandy = np.hsplit(c, 2)
        xs, ys = xandy[0].flatten(), xandy[1].flatten()
        x_chunks.append(xs)
        y_chunks.append(ys)
    return x_chunks, y_chunks, NCHUNKS


def cell(x, y, xedges, yedges):
    """
    """

    # iterate through the bins on each axis
    image_maxes = []
    for j in range(len(yedges)-1):
        for i in range(len(xedges)-1):
            cell_xmin, cell_xmax = xedges[i], xedges[i+1]
            cell_ymin, cell_ymax = yedges[j], yedges[j+1]

            # isolate the events within each cell
            cell_constraints = np.where((x < cell_xmax) & (
                x >= cell_xmin) & (y < cell_ymax) & (y >= cell_ymin))

            cell_x = x[cell_constraints]
            cell_y = y[cell_constraints]
            coord_pairs = list(zip(cell_x, cell_y))

            # find the maximum point in the cell
            coord_counts = Counter(coord_pairs).most_common()
            for result in coord_counts:
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

        # determine x and y bins
        xbinedges = np.histogram_bin_edges(MASTER_XS, bins='fd')
        ybinedges = np.histogram_bin_edges(MASTER_YS, bins='fd')

        event_pairs = np.column_stack((MASTER_XS, MASTER_YS))

        xs, ys, NCHUNKS = chunk(event_pairs)

        xbiniter = [xbinedges for i in range(NCHUNKS)]
        ybiniter = [ybinedges for i in range(NCHUNKS)]

        args = list(zip(xs, ys, xbiniter, ybiniter))

        p = mp.Pool()
        chunk_maxes = p.starmap(cell, args)

        image_maxes = [item for sublist in chunk_maxes for item in sublist]

        maxes_compressed = {}
        for loc, count in image_maxes:
            if not loc in maxes_compressed.keys():
                maxes_compressed[loc] = count
            else:
                maxes_compressed[loc] += count

        # sort the identified maxima by count and return their x(RA) and y(Dec) coordinates
        maxes_compressed = sorted(
            maxes_compressed.items(), key=lambda x: x[1], reverse=True)
        print(maxes_compressed)
        centroid_xs = np.array([item[0][0] for item in maxes_compressed])
        centroid_ys = np.array([item[0][1] for item in image_maxes])
        return centroid_xs, centroid_ys


find_centroids(
    "/Users/hunterholland/Documents/Research/Laidlaw/Data/Modified/L1517/Chandra/primary/acisf03755N004_evt2.fits.gz")
