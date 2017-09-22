from collections import namedtuple
import csv
import time

class Q():
    def __init__(self, question, answer, rating, age, flags, note):
        self.question=question;self.answer=answer;self.rating=rating;self.age=age;self.flags=flags;self.note=note;

    def __repr__(self):
        '''Returns representation of the object'''
        return("{}('{} {} {}')".format(self.__class__.__name__, self.question, self.rating, self.age))

def mylog(s1, s2='', s3=''):
    print(s1, s2, s3);

def conout(s1, s2='', s3=''):
    print(s1, s2, s3);


def show_questions(questions, log_message):
    mylog(log_message)
    for q in questions:
        mylog(q.question, q.rating, q.age)
    mylog('')

def quiz():
    Question = namedtuple('Question', 'question, answer, rating, age, flags, note')
    f = open("fiveq.qz")
    qs = map(Question._make, csv.reader(f, delimiter='\t'))
    
    mylog('Making questions.\n')
    qx = [Question(q.question, q.answer, int(q.rating), int(q.age), q.flags, q.note) for q in qs]
    
    questions = [Q(q.question, q.answer, q.rating, q.age, q.flags, q.note) for q in qx]
    
    f.close()
    
    show_questions(questions, 'here they are')

    mylog('Starting quiz.')
    for q in questions:
        response = input('[%d]%s:' % (1, q.question))
        now = int(time.time())
        if (response.lower() == q.answer.lower()):
            conout('correct')
            conout(q)
            new_rating = int((1 + 2 * q.rating) / 3)
            
            #q = q._replace(rating=new_rating, age=now)
            q.rating = new_rating
            q.age = now
            conout(q)
        else:
            conout('wrong')
            new_rating = 100
            #q = q._replace(rating=new_rating, age=now)
            q.rating = new_rating
            q.age = now

    mylog('')
    
    show_questions(questions, 'Showing updated questions.')
    
quiz()  


