from app import app
from flask import render_template, request,url_for,jsonify

# @app.route('/')
# def home():
# 	return render_template('crossword.html')

@app.route('/')
def next_step():
	questions=[]
	f = list(open("app/static/text_files/ques.txt", "r",encoding="UTF-8"))
	for x in range(20):
		question={}
		question["id"]=x
		question["statement"]=f[(x*2+0)]
		questions.append(question)
	return render_template('home.html',questions=questions)