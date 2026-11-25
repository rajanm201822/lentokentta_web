

function tallenna(arvo) {
    const nimi = localStorage.getItem("screen_name");
    fetch("http://127.0.0.1:3000/ticket/" + nimi + "/" + arvo);
}



function intro() {
    document.getElementById("vastaus").textContent = "Sinulla on lippu! Pääset jatkamaan peliä.";
}

function eiLippua() {
    document.getElementById("vastaus").textContent = "Ei ole lippua! Et voi jatkaa peliä.";
}