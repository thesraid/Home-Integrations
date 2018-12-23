#!/usr/bin/env python

'''from plexapi.myplex import MyPlexAccount
account = MyPlexAccount('thesraid', 'ry2HYp@PBpd4')
plex = account.resource('thesraid').connect()  # returns a PlexServer instance
'''

from plexapi.server import PlexServer
baseurl = 'http://192.168.0.14:32400'
token = 'DXzLXpZV1uNRrcCPkAzZ'
plex = PlexServer(baseurl, token)


'''# Example 1: List all unwatched movies.
movies = plex.library.section('Movies')
for video in movies.search(unwatched=True):
        print(video.title)
'''

video = plex.library.section('Movies').get('Unbreakable')
print('Run running the following command to play in Chromecast:')
print('catt -d Projector cast "%s"' % video.getStreamURL())

# Better to use pyChromecast maybe? 
