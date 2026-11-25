'use strict'

document.getElementById("button").addEventListener("click", async() => {
const  username=document.getElementById("username").value;
const viesti = document.getElementById("viesti")

if (!username){
    viesti.textContent= "syötä matkustaja"

}

    const response = await fetch("http://127.0.0.1:3000/register", {
        method: "POST",
        headers:{'content-type':'application/json'},
        body: JSON.stringify({username:  username})

    })
    const data = await response.json()

    viesti.textContent=data.error||data.message
});