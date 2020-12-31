def part_one():
    with open("input.txt") as f:
        inputfile = f.read().splitlines()
        yes_questions = {}
        questions_answered = 0
        for line in inputfile:
            if len(line) == 0:
                questions_answered += len(yes_questions.keys())
                yes_questions = {}
            else:
                for c in line:
                    yes_questions[c] = True
        return questions_answered


def part_two():
    with open("input.txt") as f:
        inputfile = f.read().splitlines()
        yes_questions = {}
        questions_answered = 0
        people = 0
        for line in inputfile:
            if len(line) == 0:
                all_answered = list(yes_questions[0].keys())
                for i in range(1, people):
                    all_answered = list(
                        set(all_answered).intersection(yes_questions[i].keys())
                    )
                questions_answered += len(all_answered)
                yes_questions = {}
                people = 0
            else:
                person_questions = {}
                for c in line:
                    person_questions[c] = True
                yes_questions[people] = person_questions
                people += 1
        return questions_answered


# Code to run
print("Part one answer: " + str(part_one()))
print("Part two answer: " + str(part_two()))
