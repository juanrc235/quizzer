from question import Question
import random
import sys

path = sys.argv[1]

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

print('\nWELCOME TO QUIZZER. YOUR PLACE IF YOU LOVE ISO\nPress [Ctrl + c] to exit\n')
print(unit)
for question in question_list:
    try:
        question.ask()
    except KeyboardInterrupt:
        break
print('\n| ================= RESULTs =================| ')
for question in question_list:
    if question.your_answer is not None:
        print('{} / {}'.format(question.your_answer, question.question))
