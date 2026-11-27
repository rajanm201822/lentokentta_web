'use strict'
document.getElementById("button").addEventListener('click',async()  => {
    const username =document.getElementById("screen_name").value
    const viesti =document.getElementById("viesti1")

    if (!username){
    viesti.textContent= "syötä matkustaja"

}

    const response = await fetch("http://127.0.0.1:3000/login", {
        method: "POST",
        headers:{'content-type':'application/json'},
        body: JSON.stringify({username:  username})

    })
    const data = await response.json()
    if(data.error){
        viesti.textContent=data.error||data.message
    }
    else{
        viesti.textContent=data.message
        localStorage.setItem("matkustaja",username)

            location.href = "/lentokentta_web/frontend/intro_fe/intro.html";

    }
});