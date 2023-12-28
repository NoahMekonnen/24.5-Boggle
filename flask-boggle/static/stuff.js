const form = $("form")
const button = $("button")
console.log(form.children(), Math.random())


button.on('click', function buttonRequest(e){
    e.preventDefault();
    console.log(Math.random())
    postRequest()
})

async function postRequest(e){
    await axios.post('/guesses',{guess: form.children[1].value });
}
