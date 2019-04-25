# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for
app = Flask(__name__) #name of the module. special variable

#dictionary
posts = [
    {
        'author': 'Juan Suman',
        'title': 'Primeiro post',
        'content': 'Conteudo do primeiro post.',
        'date_posted': '17 de Abril, 2019.'
    },
    {
        'author': 'Laura Kook',
        'title': 'Segundo post',
        'content': 'Conteudo do segundo post.',
        'date_posted': '18 de Abril, 2019.'
    }
]

@app.route("/") #route to homepage("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") #route to aboutpage("/")
def about():
    return render_template('about.html', title='About')