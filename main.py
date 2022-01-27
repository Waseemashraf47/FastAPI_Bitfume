from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():

    return 'Hello'

@app.get('/about') #adding about button
def about():
    return {'about': 'about page'}
