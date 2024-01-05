"use strict";

const form = $("form")
const button = $("button")
const input = $("input")
const label = $("label")
const body = $("body")
const result = $("<h3></h3>")
const startButton = $("<button></button>").text("Start Game")

body.append(startButton)
startButton.hide()

let score = 0

let listOfWords = []

// post request for button
async function postRequest(){
    const guess = $('#guess')[0].value
    
    if (!(guess in listOfWords)){
        const response = await axios.post("/check-word",{params:{guess: guess}},{headers: {'Content-Type': 'application/json'}});
        // making response based on validity of word
        if (response.data.result == "ok"){
            result.text("This is a valid word")
            score += guess.length
            $("#score").text(score)
        }
        else if (response.data.result == "not-a-word"){
            result.text("This is not a word")
        }
        else{
            result.text("This is not on the board")
        }
        body.append(result)
    }
    listOfWords.push(guess)
}

// form functionality
form.on('submit', function buttonRequest(e){
    e.preventDefault();
    console.log("online!")
    postRequest();
    form[0].reset()
})

// start button functionality
startButton.on("click", function startGame(e){
    e.preventDefault()
    form.show()
    button.show()
    label.show()
    input.show()
    startButton.hide()
    setTimeout(gameOver, 5000)
})

// ending the game
async function gameOver(){
    form.hide()
    button.hide()
    label.hide()
    input.hide()
    await axios.post("/",{params:{score: score}})
    startButton.show()
}

// stop guessing after 60 seconds
setTimeout(gameOver, 5000)

