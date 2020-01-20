import random

chapters = ['VI : Big O', 'VII : Technical Questions', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
questions = {'VI : Big O': 12, 'VII : Technical Questions': 4, '1': 9, '2': 8, '3': 6, '4': 12, '5': 8, '6': 10,
             '7': 10, '8': 14, '9': 8, '10': 11, '11': 6, '12': 11, '13': 8, '14': 7, '15': 7, '16': 26, '17': 26}

while True:
    chapter = random.choice(chapters)
    question = round(random.randint(1, questions[chapter]))
    print('Chapter: ', chapter)
    print('Question: ', question)
    print('\nNext Question? (Press "n" to exit)')


    if input() is 'n':
        exit()
    else:
        print("\033c", end="")
