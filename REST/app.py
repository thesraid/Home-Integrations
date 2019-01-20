#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
A basic bottle app skeleton
'''

import bottle
from bottle import template

app = application = bottle.Bottle()

@app.route('/static/<filename:path>')
def static(filename):
    '''
    Serve static files
    '''
    return bottle.static_file(filename, root='./static')

@app.route('/')
def show_index():
    '''
    The front "index" page
    '''
    return 'Hello'

@app.route('/page/<page_name>')
def show_page(page_name):
    '''
    Return a page that has been rendered using a template
    '''
    return template('page', page_name=page_name)

class StripPathMiddleware(object):
    '''
    Get that slash out of the request
    '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=8080)
