import os
import shutil


def transcode_command(path, filetype='mkv', log=False, speed='normal'):
    vidformat = f"--{filetype}"
    if log == False:
        whetherlog = " --no-log"
    else:
        whetherlog = ""
    if filetype == "mkv":
        vidformat = ""
    elif filetype == "m4v":
        vidformat = " --"+filetype
    elif filetype == "mp4":
        vidformat = " --"+filetype
    else:
        print("Output file type must be either mp4, m4v, or left empty for mkv.")
        return
    if speed == "normal":
        speed = ""
    elif speed == "quick":
        speed = " --"+speed
    elif speed == "veryquick":
        speed = " --"+speed
    else:
        print("Transcode speed must be either quick, veryquick, or left empty for normal.")
        return
    command = f"transcode-video{vidformat}{whetherlog}{speed} \"{path}\""
    return command


ripped_dir = "/Users/hunterholland/Ripped Media"
iTunes_dir = "/Users/hunterholland/Music/iTunes/iTunes Media"
media_type = "TV Shows"
media_name = "Merlin"

for directory, subdirs, files in os.walk(f"{ripped_dir}/{media_type}/{media_name}", topdown=False):
    dirs = os.listdir(directory)
    count = 0
    for item in dirs:
        if item.endswith(".mkv"):
            count += 1
    if count == 0:
        shutil.rmtree(directory)
        continue
    rel = os.path.relpath(directory, start=ripped_dir)
    new_dir = os.path.join(iTunes_dir, rel)
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)
    for file in files:
        filepath = os.path.join(directory, file)
        if file.endswith(".mkv"):
            command = transcode_command(
                filepath, filetype="m4v", speed="veryquick")
            os.system(f"cd \"{new_dir}\"; {command}")
        elif file.startswith("."):
            pass
        os.remove(filepath)
print("All files successfully transcoded and moved to their new locations. Original files have been deleted.")
