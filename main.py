from question import Question
import random
import sys

u = {'1.1' : 0, '1.2' : 1, '2.1' : 2, '2.2' : 3}
paths = ['questions/1.1.txt',
         'questions/1.2.txt',
         'questions/2.1.txt',
         'questions/2.2.txt']

def create_unit(path):
    with open(path, 'r') as fd:
        content = fd.read()

    content = content.split('\n')
    content = [item for item in content if item != '']

    unit = content.pop(0)

    n = 5
    final = [content[i * n:(i + 1) * n] for i in range((len(content) + n - 1) // n )]

    question_list = []
    i = 1
    for item in final:
        question_list.append( Question( i, item[0], item[1], (item[2], item[3], item[4])) )
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
    print('\n| ================= RESULTs =================| ')
    for question in question_list:
        if question.your_answer is not None:
            print('{} / {}'.format(question.your_answer, question.question))

units = []
for path in paths:
    units.append(create_unit(path))

print('\nWELCOME TO QUIZZER. YOUR PLACE IF YOU LOVE ISO\nPress [Ctrl + c] to exit\n')

selection = ''
while selection not in ('1.1', '1.2', '2.1', '2.2'):
    try:
        selection = input('Select the Unit [1.1, 1.2, 2.1, 2.1]: ')
    except KeyboardInterrupt:
        print('\nBye, Bye')
        sys.exit(0)

ask(units[u[selection]][0], units[u[selection]][1])
