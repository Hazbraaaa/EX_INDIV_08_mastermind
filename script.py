import random

# init variables

colors = ["Red", "Blue", "Yellow", "Green"]
codeToBreak = random.choices(colors, k = 2)


# init functions

def isAttemptCorrect(codeToBreak, codeAttempt):
    if len(codeToBreak) != len(codeAttempt):
        return False
    return all(codeAttempt[i] == codeToBreak[i] for i in range(len(codeToBreak)))

def checkAnswer(codeAttempt, feedback):
    secret = codeToBreak.copy()
    attempt = codeAttempt.copy()

    for i in range(len(attempt)):
        if attempt[i] == secret[i]:
            feedback[0] += 1
            secret[i] = "checked"
            attempt[i] = "checked"
    for i in range(len(attempt)):
        if attempt[i] != "checked" and attempt[i] in secret:
            feedback[1] += 1
            secret[i] = "checked"
    return feedback

def mastermind(codeToBreak):
    for x in range(2):
        codeAttempt = []
        for x in range(len(codeToBreak)):
            codeAttempt.append(input(f"Couleur {x+1} : "))
        if isAttemptCorrect(codeToBreak, codeAttempt):
            print(f"Gagné\nCode: {codeToBreak}")
            return
        else:
            result = checkAnswer(codeAttempt, feedback = [0, 0])
            print(f"Resultat: {result}\n")
            print(f"Choix: {colors}")
    print(f"Perdu\nCode: {codeToBreak}")
    return


# execute code

print(f"Choix: {colors}")
mastermind(codeToBreak)