from bottle import *

HOST = '192.168.199.106'

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = '/Users/weinbergmath/Sites/mathcache/')

@route('/')
def main():

    location = request.query.newlocation

    if(location == ''):

        question1 =[ "Question 1: What is the sum of the first five positive whole numbers?",'']
        question2 =["Question 2: How many sides are in the polygon at left?",'polygon.png']
        question3 =["Question 3: How many prime numbers are between 1 and 20?",'']

        questions = [question1, question2, question3]
    
        return template('questions.tpl', questions = questions)
    #15*6*8 = 720
    elif(location == '720'):
        
        question1 = ["Question 1: What is 2*2?",'']
        question2 =["Question 2: What is 7 - 3?",'']
        question3 = ["Question 3: What is 1 - 1?",'']
 

        questions = [question1, question2,question3]
        return template('questions.tpl', questions = questions)

    elif(location == '0'):

        return template('success.tpl')

    else:
        return template('lost.tpl',location=location)

@route('/page2/')
def main():

    question1 = ["Question 1: What is 2*2?",'']
    question2 =["Question 2: What is 7 - 3?",'']
    question3 = ["Question 3: What is 1 - 1?",'']
 

    questions = [question1, question2,question3]
    return template('questions.tpl',questions = questions)


@route('/test/')
def main2():

    return "This is test #2"

    


run(host = HOST, port = 8080, debug = True)
