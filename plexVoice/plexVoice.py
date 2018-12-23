#!/usr/bin/env python

from plexapi.server import PlexServer
import argparse
import time
import pychromecast

###########################################################################################
"""
Get command line args from the user.
"""
def get_args():
    parser = argparse.ArgumentParser(
        description='Video type, name name and Chromecast')

      
    parser.add_argument('-t', '--type',
        required=True,
        action='store',
        help='TV or Movie')
    
    parser.add_argument('-v', '--video',
        required=True,
        action='store',
        help='Video')

    parser.add_argument('-c', '--chromecast',
        required=False,
        default="Projector",
        action='store',
        help='Chromecast')

    args = parser.parse_args()

    return args

###########################################################################################
def playOnChromecast( URL, ccName ):
    print URL
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == ccName)
    cast.wait()
    #print(cast.device)
    mc = cast.media_controller
    # Plex gives us a m2u8 URL which chromecast can't play natively. GAME OVER MAN, GAME OVER
    mc.play_media(URL, 'video/mp4')
    mc.block_until_active()
    print(mc.status)
###########################################################################################

'''
Main Module
'''

def main():

    args = get_args()
    mediaType  = args.type
    videoName = args.video
    ccName = args.chromecast

    baseurl = 'http://192.168.0.14:32400'
    token = 'hdHPsyJ8ingKxpzmLcPn'
    plex = PlexServer(baseurl, token)

    video = plex.library.section(mediaType).get(videoName)
    playOnChromecast(video.getStreamURL(), ccName)

###########################################################################################

""" Start program """
if __name__ == "__main__":
    main()
