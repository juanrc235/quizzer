from question import Question
import random
import sys

u = {'1.1' : 0, '1.2' : 1, '2.1' : 2, '2.2' : 3, '3.1' : 4}
paths = ['questions/1.1.txt',
         'questions/1.2.txt',
         'questions/2.1.txt',
         'questions/2.2.txt',
         'questions/3.1.txt']

def usage():
  print('Usage: main.py: Use preload questions\n       main.py <-f> <file>: Use the questions of the file')

def parse_argv(argv):

    if len(argv) == 1:
        selection = 1
    elif len(argv) == 3 and argv[1] == '-f':
        selection = 2
    else:
        selection = 3

    return selection


def create_unit(path):
    with open(path, 'r', encoding='utf-8') as fd:
        content = fd.read()

    content = content.split('\n')
    content = [item for item in content if item != '']

    unit = content.pop(0)
    print(unit)
    n = 5
    final = [content[i * n:(i + 1) * n] for i in range((len(content) + n - 1) // n )]

    question_list = []
    i = 1
    for item in final:
        try:
            question_list.append( Question( i, item[0], item[1], (item[2], item[3], item[4])) )
        except Exception:
            print('[ERROR] File: {} Question: {}'.format(path, i, item[0]))
            sys,exit()
        i+=1

    random.shuffle(question_list)

    return (unit, question_list)

def ask(unit, question_list):
    print('\n| ================= {}  =================|'.format(unit))
    for question in question_list:
        try:
            question.ask()
        except KeyboardInterrupt:
            break
    print('\n| ================= RESULTS =================| ')
    for question in question_list:
        if question.your_answer is not None:
            print('{} / {}'.format(question.your_answer, question.question))

def preload_questions():
    units = []
    for path in paths:
        units.append(create_unit(path))

    print('\nWELCOME TO QUIZZER. YOUR PLACE IF YOU LOVE ISO\nPress [Ctrl + c] to exit\n')

    str_units = [unit[0].split(' ')[1] for unit in units]
    str = ', '.join(str_units)
    selection = ''
    while selection not in str_units:
        try:
            selection = input('Select the Unit [' + str  + ']: ')
        except KeyboardInterrupt:
            print('\nBye, Bye')
            sys.exit(0)

    ask(units[u[selection]][0], units[u[selection]][1])

def load_file(path):
    unit = create_unit(path)
    ask(unit[0], unit[1])

def main(argv):

    selection = parse_argv(argv)

    if selection == 1:
        preload_questions()
    elif selection == 2:
        load_file(argv[2])
    else:
        usage()

if __name__ =='__main__':
    main(sys.argv)
