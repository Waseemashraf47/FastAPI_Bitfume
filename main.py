from fastapi import FastAPI

app = FastAPI()
#
@app.get('/')
def index():
    return {'data': 'blog List'}

@app.get('/about') #adding about button
def about():
    return {'about': 'about page'}

@app.get('/blog')
def index(limit=10, published:bool=True):
        #return 'Hello Dear'
    #return {'data': 'blog list'}
    #return published
    if published:
        return {'data', f'{limit} published blogs from db'}
    else :
        return {'data', f'{limit} blogs from db'} 

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished Blogs'}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}

@app.get('/blog/{sd}/comments')
def comments(sd: int):
    return { f'data {sd}' : {'comment1','comment2'}}
