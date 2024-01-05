"use strict";

const form = $("form")
const button = $("button")
const input = $("input")
const label = $("label")
const body = $("body")
const result = $("<h3></h3>")

class Boggle_stuff{
    constructor(listOfWords,score){
        this.listOfWords = listOfWords
        this.score = score
    }

    async postRequest(){
        const guess = $('#guess')[0].value
        // handles duplicate words
        if (!(this.listOfWords.includes(guess))){
            const response = await axios.get("/check-word",{params:{guess: guess}},);
            // making response based on validity of word
            if (response.data.result == "ok"){
                result.text("This is a valid word")
                this.score += guess.length
                console.log($("#score"))
                $("#score").text(this.score)
            }
            else if (response.data.result == "not-a-word"){
                result.text("This is not a word")
            }
            else{
                result.text("This is not on the board")
            }
            body.append(result)
            this.listOfWords.push(guess)
        }
        else{
            alert("Type in a distinct word")
        }
    }

    async gameOver(){
        form.hide();
        button.hide();
        label.hide();
        input.hide();
        await axios.post("/update-num-of-games",{params:{score: score}});
    }
}



document.addEventListener('DOMContentLoaded',function(e){
    const newBoggleStuff = new Boggle_stuff([],0);

    form.on('submit', function buttonRequest(e){
        e.preventDefault();
        newBoggleStuff.postRequest();
        form[0].reset();
    })

    setTimeout(newBoggleStuff.gameOver, 60000)
})