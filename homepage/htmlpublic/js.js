async function logJSONData(link) {
    const response = await fetch(link);
    const jsonData = await response.json();
    document.getElementsByClassName("context")[0].innerHTML = JSON.stringify(jsonData);
}


document.getElementById("submit11").onclick = ()=>{
    string = document.getElementById("inputlink").value
    logJSONData(string)
}

