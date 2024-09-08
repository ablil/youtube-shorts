#!/usr/bin/env python

import yt_dlp

yt_opts = {
  'format': 'best',  # Download the best available quality
  'outtmpl': '%(title)s.%(ext)s',  # Save with the video's title and correct extension
  'force_generic_extractor': True,
  'postprocessors': [{
      'key': 'FFmpegVideoConvertor',
      'preferedformat': 'mp4',  # Convert to mp4 format
  }],
}

def extract_info(url):
  with yt_dlp.YoutubeDL(yt_opts) as yt:
    return yt.extract_info(url, download=False)
