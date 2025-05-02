// init variables

const colors = ["Red", "Blue", "Yellow", "Green"];
const codeToBreak = ["Greeeen", "Blue"];
let feedback = [0, 0];


// init functions

function isCodeAllowed(codeToBreak) {
    return codeToBreak.every((element) => colors.includes(element));
}

function isAttemptCorrect(codeToBreak, codeAttempt) {


    return codeAttempt.every((element) => codeAttempt[element] === codeToBreak[element]);


}

function mastermind(codeToBreak) {
    if (!isCodeAllowed(codeToBreak)) {
        console.log("Code à déchiffrer incorrect. Recommencer.")
        return;
    }
    return console.log("gagné");
}


// execute code

mastermind(codeToBreak);
