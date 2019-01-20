#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
A basic REST skeleton from https://www.youtube.com/watch?v=BHAUJUuhiDw
'''
from bottle import run, get, post, request, delete

animals = [
        {'name' : 'Ellie', 'type' : 'Elphant'},
        {'name' : 'Python', 'type' : 'Snake'},
        {'name' : 'Zed', 'type' : 'Zebra'}
        ]

@get('/animal')
def getAll():
    return {'animals' : animals}

@get('/animal/<name>')
def getOne(name):
    theAnimal = [animal for animal in animals if animal['name'] == name]
    return {'animal' : theAnimal[0]}

@post('/animal')
def addOne():
    newAnimal = {'name' : request.json.get('name'), 'type' : request.json.get('type')}
    animals.append(newAnimal)
    return {'animals' : animals}

@delete('/animal/<name>')
def deleteOne(name):
    theAnimal = [animal for animal in animals if animal['name'] == name]
    animals.remove(theAnimal[0])
    return {'animals' : animals}

run(reloader=True, debug=True)
