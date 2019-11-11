from question import Question
import random

path = 'questions_1.1.txt'

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

random.shuffle(question_list)

print(unit)
for question in question_list:
    question.ask()
