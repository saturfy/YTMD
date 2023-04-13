import argparse
import os
from pytube import YouTube
import subprocess
import requests


def parse_arguments():
    """
    Creates an argument parser for the CLI tool.

    Parameters
    ----------

    Returns
    -------
    argparse.Namespace object
        The parsed arguments.

    """
    # parser object
    parser = argparse.ArgumentParser(
        prog='ytmd',
        description='Downloads music from youtube urls.'
        )

    # determine the working directory
    parser.add_argument('-d', '--dir', help='target dir path')

    # choose how to suppy the urls
    # directly by -u
    # from a file using -f
    # f is used for batch works
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='download url')
    group.add_argument('-f', '--file', help='path to the file which contains the urls')

    return parser.parse_args()


def get_variables(args):
    """
    Parses the arguemnts from the command line.

    Parameters
    ----------
    args : argparse.Namespace object
        The parsed arguments

    Returns
    -------
    touple
        (List_of_URLS, target_dir_path)
        List_of_URLS: list of strings, the url address for the downloads
        target_dir_path: os.path for the download directory
    """

    # --- Create URL list ---
    URLS = []

    # read from console
    if args.url is not None:
        URLS.append(args.url)

    # read from file
    if args.file is not None:
        with open(args.file) as listfile:
            for line in listfile:
                URLS.append(line.rstrip())

    # --- Set target dir ---
    if args.dir is not None:
        # Select specified
        TARGET_DIR = os.path.normpath(args.dir)
    else:
        # default is the working directory
        TARGET_DIR = os.getcwd()

    return URLS, TARGET_DIR


def grab_files(URLS, TARGET_DIR):
    """
    Downloads the files from youtube using the pytube package.

    Parameters
    ----------
    URLS : list
        List of strings which are the URLS of the files to be downloaded

    TARGET_DIR : os.path object
        The path to the download dir

    Retruns
    -------
    FILE_NAMES : list
        List of os.path to the downloaded files.

    """

    FILE_NAMES = []

    for url in URLS:
        # --- Select the stream ---

        # --- Check URL validity ---
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            print(url + ' is not a valid url. Skipping...')
            continue

        # check for valid response
        if r.status_code != 200:
            print(url + ' is not giving a correct response. Skipping...')
            continue

        # check for available video
        if '"status":"ERROR"' in r.text:

            print('The video at the url' + url + ' is unavailable. Skipping...')
            continue

        # Get the available mp4 audio streams
        yt = YouTube(url)
        streams = yt.streams.filter(only_audio=True, file_extension='mp4')

        # check for stream existence
        if len(streams) == 0:
            print(f"There was no mp4 stream for file {url}. Skipping...")
            continue

        # select highest bitrate stream
        stream = streams[-1]

        # --- Download the selected stream ---

        # rename the file so it does not contain spaces
        name = stream.default_filename.replace(' ', '_')

        # download
        print(f"Started downloading {name} ")

        filename = stream.download(output_path=TARGET_DIR, filename=name)
        print(f"Downloaded {stream.filesize_mb} mb")

        # save file name
        FILE_NAMES.append(filename)

    return FILE_NAMES


def convert_audio(FILE_NAMES, delete=True):
    """
    Converts the provided mp4 audio files to mp3.
    The original files can be kept or deleted.

    Parameters
    ----------
    FILE_NAMES : list
        list of os.path to the files which have to be converted.

    Returns
    -------
    """

    for filename in FILE_NAMES:

        # check for mp4 files
        if filename[-3:] != 'mp4':
            print(filename + ' is not an mp4 file. Skipping...')
            continue

        # new name for the converted file
        outname = filename[:-4]+'.mp3'

        # prepare ffmpeg command
        cmd = f"ffmpeg -i {filename} -vn {outname}"

        # converting files
        print(f"Converting {filename} to mp3")

        subprocess.run(cmd)

        # remove original file
        if delete:
            os.remove(filename)


def main():

    # get the command line arguments
    args = parse_arguments()

    # deterimine the variables from the arguments
    URLS, TARGET_DIR = get_variables(args)

    # download the mp4 audio streams
    FILE_NAMES = grab_files(URLS, TARGET_DIR)

    # convert the mp4 audio to mp3 using ffmpeg
    convert_audio(FILE_NAMES)

    print(f"Successfully grabbed {len(FILE_NAMES)} files from youtube.")
