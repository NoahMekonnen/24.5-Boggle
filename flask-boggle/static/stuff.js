const form = $("form")


async function getRequest(e){
    guess = $('#guess')[0].value
    response = await axios.post('/guesses',{params:{guess: guess}});
    console.log(response)
}

form.on('submit', function buttonRequest(e){
    e.preventDefault();
    getRequest();
})

