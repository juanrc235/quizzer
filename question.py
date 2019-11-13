import random

class Question:

    def __init__(self, num, question, correct_answer, incorrect_answers):

        self.number = num
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.your_answer = None

    def print(self):
        str = '{}\n{}\n{}'.format(self.question, self.correct_answer, self.incorrect_answers)
        print(str)

    def ask(self):

        pos_answers = []
        pos_answers.append(self.correct_answer)
        for i in self.incorrect_answers:
            pos_answers.append(i)
        random.shuffle(pos_answers)
        i = 1
        txt = '\n' + self.question + '\n'
        for ans in pos_answers:
            txt += '({}) {}\n'.format(i, ans)
            i += 1
        print(txt, end='')
        answer = ''
        while answer not in ('1', '2', '3', '4'):
            answer = input('Please, type the answer number [1-4]: ')

        if pos_answers[int(answer)-1] == self.correct_answer:
            print('\n|========= CORRECT =========|')
            self.your_answer = 'CORRECT'
        else:
            print('\n|========= INCORRECT =========|')
            self.your_answer = 'INCORRECT'
            while answer not in ('y', 'n', 'Y', 'N'):
                answer = input('\nDo you want to see the correct one?[y/n]: ')
            if answer in  ('y', 'Y'):
                print(self.correct_answer)
