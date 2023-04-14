from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Command line tool for downloading music from youtube videos \
      and converting them to mp3 format using ffmpeg.'
  
setup(
        name ='ytmd',
        version ='1.0.0',
        author ='Peter Posfay',
        author_email ='posfay.peter@wigner.hu',
        url ='https://github.com/saturfy/YTMD',
        description ='youtube music downloader CLI tool',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'ytmd = ytmd.cli:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='youtube music downloader ffmpeg mp3',
        install_requires = requirements,
        zip_safe = False
)