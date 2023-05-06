from project_questions import Question


question_prompts = [
    'What number is first?\n(a) 2 \n(b) 3 \n(c) 4\n\n',
    'What number is second?\n(a) 1 \n(b) 2 \n(c) 3\n\n',
    'What number is third?\n(a) 3 \n(b) 4 \n(c) 5\n\n'
]


questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + ' answers correct.')


run_test(questions)
