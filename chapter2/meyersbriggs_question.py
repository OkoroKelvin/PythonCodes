questions = ["expend energy", "enjoy groups", "conserve energy", "enjoy one-on-one", "interpret literally",
             "look for meaning and possibilities", "logical, thinking,questioning",
             "empathetic, feeling, accommodating",
             "organized, orderly", "flexible, adaptable", "more outgoing, think out loud",
             "more reserved, think to yourself", "practical, realistic, experiential",
             "imaginative, innovative, theoretical", "candid, straight forward, frank", "tactful, kind, encouraging",
             "plan, schedule", "unplanned, spontaneous", "seek many tasks, public activities, interaction with others",
             "seek private, solitary activities with quiet to concentrate", "standard, usual, conventional",
             "different, novel, unique", "firm, tend to criticize, hold the line",
             "gentle, tend to appreciate, conciliate", "regulated, structured", "easygoing, live and let live",
             "external, communicative, express yourself",
             "internal, reticent, keep to yourself", "focus on here-and-now",
             "look to the future, global perspective,big picture",
             "tough-minded, just", "tender-hearted, merciful", "preparation, plan ahead",
             "go with the flow, adapt as you go",
             "active, initiate", "reflective, deliberate", "facts, things,what is",
             "ideas, dreams, what could be,philosophical",
             "matter of fact, issue-oriented", "sensitive, people-oriented, compassionate", "control, govern",
             "latitude, freedom"]

countOfA = 0
countOfB = 0
count = 0
personality = ''
for question in questions:
    userInput = input(question)
    userInput.upper()
    if userInput == 'A':
        countOfA = countOfA + 1
    if userInput == 'B':
        countOfB = countOfB + 1
    count = count + 1

    if count == 5:
        if countOfA > countOfB:
            personality = personality + "E"
        else:
            personality = personality + "I"
   