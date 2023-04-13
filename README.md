![](https://raw.githubusercontent.com/saturfy/YTMD/main/YTMD.png)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytube?color=brightgreen)
![](https://img.shields.io/badge/python-pytube-orange) 
![](https://img.shields.io/badge/ffmpeg-version:%202023--03--27--git--f7abe92bd7-brightgreen)

# Description
YouTube Music Downloader (YTMD) is a python and ffmpeg based console application for downloading audiostreams from youtube URLs to your computer and converting them to mp3 format for offline use. 

----

# Prerequisites
You need to have ffmpeg and python installed. The software was tested with ffmpeg version: 2023--03--27--git--f7abe92bd7 and python 3.9.7. The python code interacts with ffmpg via console commands so the only requirement for it to work is that you can call ffmpeg from the same console as python. Most of the time this is automatic but in certain cases like conda command promt you have to make sure that both of them work. 

You can download ffmpeg from [here](https://ffmpeg.org/download.html) and [here](https://phoenixnap.com/kb/ffmpeg-windows) you can find an installation guide for windows where it is explained how to set the PATH environmental variables to make ffmpeg commands avalilable in command line. 

# Installation
1. ___OFFLINE___: Download the dist/ytmd-1.0.0-py3-none-any.whl file from the release folder and install it using pip:

        python -m pip install ytmd-1.0.0-py3-none-any.whl
        
2. ___ONLINE___
        
        python -m pip install git+https://github.com/saturfy/YTMD

## Test the installation
A test.txt file is provided in the repository to test the installation. Download this file into an empty folder and run:
        
        ytmd -f test.txt

The text file containts 5 URLs. The command will try to download these from youtube but the last two are bad URLs which are skipped. At the end you will have 3 mp3 files. 
    
# Usage
The program can be run from console using the __ytmd__ command. You must provide a youtube URL to download music. There are two ways to do it:
- ___Direct___:
        
        ytmd -u <youtube-url-of-a video>
 
You can download one url this way. For multiple urls at once use the file method below.
        
- ___FILE___: in this case you can list the urls in a txt file. The program will go through them one by one and downloads the music from each. The txt file should contian only one url per line. An example is given in the repo files: _test.txt_. To download urls from a file use the following command: 

        ytmd -f <path-to-the-txt-file>
        
The default behaviour is that ytmd downloads files into the folder it was called from. However You can specify a dwonload folder if you want using -d 

        ytdm -d <path-to-download-directory> -u <youtube-url>
        
## Example
Download youtube videos from the urls in the test.txt file into a download folder: Call the command from the folder where the file is located

        ytmd -d download -f test.txt
        
# Notes
- The program always downloads the best available audio stream using the mp4 files from the video.

