'''
Created on Sep 19, 2017

@author: louie
'''

import random

def show_quiz(questions_dict, quiz_number=1):
    '''Generate a set of n questions equal to length of question_dict
    The order of the questions is random.'''

    # questions must be asked in a random order,
    # we can't shuffle the dictionary (since a dictionary is unordered),
    # so we create a list of keys, and shuffle that
    questions_keys = list(questions_dict.keys())
    random.shuffle(questions_keys)

    # no particular order needed
    # this serves as a master list to generate 4 possible answers to each question
    all_answers_list = list(questions_dict.values())

    quiz_page_header = '''Name:\n\nDate:\n\nPeriod:\n
                    State Capitals Quiz (Form %d)\n\n''' % quiz_number

    # do 50 questions, one for each state
    quiz_body = ''

    question_number = 1
    for state_name in questions_keys:
        answer = questions_dict[state_name]

        #insert_index = random.randint(0, nchoices_per_question)

        quiz_body += show_question(all_answers_list, question_number, state_name, answer)

        question_number += 1

    return quiz_page_header + quiz_body


def potential_answers_list(all_answers_master_list, answer, nchoices, insert_index):
    '''Generate a 4 item list of A, B, C, D choices for this question.

    Generates a list of answers.
    The list is of length nchoices, and includes 3 invalid answers plus
    a real answer, where the real answer appears in a random location

    :param all_answers_master_list: the master list of all possible answers
    from which to make this list
    :param answer: the question's answer
    :nchoices: generate this many potential answers and include the real answer
    :returns: list
    '''
    # Start with all the capitals in a list by making a copy of the master list of answers
    all_answers_copy = all_answers_master_list[:]

    # remove the real answer's capital from the master list
    all_answers_copy.remove(answer)
    # generate a 3 item list choosing randomly from previous list
    choices = random.sample(all_answers_copy, nchoices - 1)
    # insert the real answer into this list in a random location
    choices.insert(insert_index, answer)
    return choices


def show_question(all_answers_master_list, number, state, answer):
    '''Show a single question with multiple choices picked from
    the list all_answers_master_list'''

    nchoices = 4
    insert_index = 3
    question_text = '%d. What is the capital of %s?\n' % (number, state)

    choices = potential_answers_list(all_answers_master_list, answer, nchoices, insert_index)

    question_choices_text = ''
    for i in range(4):
        question_choices_text += '     %s. %s\n' % ('ABCD'[i], choices[i])
    question_choices_text += '\n'
    return question_text + question_choices_text


if __name__ == '__main__':
    QUESTIONS_DICTIONARY = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }
print(show_quiz(QUESTIONS_DICTIONARY))
