from question import Question
import random
import sys
import os

def explore_dir():
    print('Exploring DIR questions/')
    return os.listdir('questions/')

def usage():
  print('Usage: main.py: Use preload questions\n       main.py <-f> <file>: Use the questions of the file')

def parse(argv):

    if len(argv) == 1:
        selection = 1
    elif len(argv) == 3 and argv[1] == '-f':
        selection = 2
    else:
        selection = 3

    return selection

def create_unit(path):
    with open('questions/'+path, 'r', encoding='utf-8') as fd:
        try:
            content = fd.read()
        except UnicodeDecodeError:
            print('Error parsing file: {}. Please remove all non UTF-8 characters'.format(path))
            sys.exit(1)

    content = content.split('\n')
    content = [item for item in content if item != '']

    unit = content.pop(0)
    n = 5
    final = [content[i * n:(i + 1) * n] for i in range((len(content) + n - 1) // n )]

    question_list = []
    i = 1
    for item in final:
        try:
            question_list.append( Question( i, item[0], item[1], (item[2], item[3], item[4])) )
        except Exception:
            print('[ERROR] File: {} Question: {}. Be sure all questions follow the format'.format(path, i, item[0]))
            sys,exit()
        i+=1

    random.shuffle(question_list)
    print('File <{}> finish'.format(path))
    return (unit, question_list)

def ask(unit):
    question_list = unit[1]
    i = 1
    total = len(question_list)
    print('\n| ================= {}  =================|'.format(unit[0]))
    for question in question_list:
        try:
            print('\n[{}/{}] '.format(i, total), end='')
            question.ask()
            i+=1
        except KeyboardInterrupt:
            break
    print('\n| ================= RESULTS =================| ')

    correct = 0
    for question in question_list:
        if question.your_answer is not None:
            print('{} / {}'.format(question.your_answer, question.question))
            if question.your_answer is 'CORRECT':
                correct+=1
    print('##### CORRECT: {} INCORRECT: {} #####'.format(correct, total-correct))


def valid(s, i):
    valid = False
    try:
        value = int(s)
        if value >= 0 and value <= i:
            valid = True
    except ValueError:
        pass
    return valid

def preload_questions_option():
    units = []
    paths = explore_dir()
    for path in paths:
        units.append(create_unit(path))

    print('\nWELCOME TO QUIZZER. YOUR PLACE IF YOU LOVE ISO\nPress [Ctrl + c] to exit\n')

    selection = ''
    str = []
    i = 0
    for unit, question_list in units:
        print('({}) {}'.format(i, unit))
        i+=1
    while not valid(selection, i):
        try:
            selection = input('Select the question set: ')
        except KeyboardInterrupt:
            print('\nBye, Bye')
            sys.exit(0)

    ask(units[int(selection)])

def load_file_option(path):
    if not os.path.isfile('questions/'+path):
        print('Please, write only the file name. Not the path')
        sys.exit()
    unit = create_unit(path)
    ask(unit)

def main(argv):

    selection = parse(argv)

    if selection == 1:
        preload_questions_option()
    elif selection == 2:
        load_file_option(argv[2])
    else:
        usage()

if __name__ =='__main__':
    main(sys.argv)
