const form = $("form")


async function postRequest(e){
    // await axios.post('/guesses',{guess: ('#guess').val });
    await axios.post('/guesses',{guess: ('#guess').val });
}

form.on('submit', function buttonRequest(e){
    e.preventDefault();
    console.log(form)
    postRequest();
})

