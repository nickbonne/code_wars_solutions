
# https://www.codewars.com/kata/dubstep/train/python

import re

def song_decoder(song):

    return re.sub('(WUB)+', ' ', song).strip()