![](https://raw.githubusercontent.com/saturfy/YTMD/main/YTMD.png)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytube?color=brightgreen)
![](https://img.shields.io/badge/python-pytube-orange) 
![](https://img.shields.io/badge/ffmpeg-version:%202023--03--27--git--f7abe92bd7-brightgreen)

# Description
YouTube Music Downloader (YTMD) is a python and ffmpeg baed console application for downloading audiostreams from youtube URLs to your computer and converting them to mp3 format for offline use. 

----

# Prerequisites
You need to have ffmpeg and python installed. The software was tested with ffmpeg version: 2023--03--27--git--f7abe92bd7 and python 3.9.7. The python code interacts with ffmpg via console commands so the only requirement for it to work is that you can call ffmpeg from the same console as python. Most of the time this is automatic but in certain cases like conda command promt you have to make sure that both of them work. 

You can download ffmpeg from [here](https://ffmpeg.org/download.html) and [here](https://phoenixnap.com/kb/ffmpeg-windows) you can find an installation guide for windows where it is explained how to set the PATH environmental variables to make ffmpeg commands avalilable in command line. 

# Installation
1. ___OFFLINE___: Download the dist/ytmd-1.0.0-py3-none-any.whl file from the release folder and install it using pip:

        python -m pip install ytmd-1.0.0-py3-none-any.whl
        
2. ___ONLINE___
        
        python -m pip install git+https://github.com/saturfy/YTMD
    

# Usage

