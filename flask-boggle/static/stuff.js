"use strict";

const form = $("form")
const button = $("button")
const input = $("input")
const label = $("label")
const body = $("body")
const result = $("<h3></h3>")
// const startButton = $("<button></button>").text("Start Game")

// body.append(startButton)
// startButton.hide()

let score = 0

let listOfWords = []

// post request for button
async function postRequest(){
    const guess = $('#guess')[0].value
    // 
    if (!(listOfWords.includes(guess))){
        const response = await axios.post("/check-word",{params:{guess: guess}},);
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
        listOfWords.push(guess)
        console.log(guess in listOfWords)
    }
    else{
        alert("Type in a distinct word")
    }
    console.log(listOfWords)
}

// form functionality
form.on('submit', function buttonRequest(e){
    e.preventDefault();
    console.log("online!")
    postRequest();
    form[0].reset()
})

// // start button functionality
// startButton.on("click", function startGame(e){
//     // e.preventDefault()
//     score = 0
//     form.show()
//     button.show()
//     label.show()
//     input.show()
//     startButton.hide()
//     setTimeout(gameOver, 60000)
// })

// ending the game
async function gameOver(){
    form.hide()
    button.hide()
    label.hide()
    input.hide()
    await axios.post("/update-num-of-games",{params:{score: score}})
    // startButton.show()
}

// stop guessing after 60 seconds
setTimeout(gameOver, 60000)

