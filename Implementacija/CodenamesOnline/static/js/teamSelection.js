function seek(){
    fetch('/game/players', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        for(let i = 0; i < 4; i++)
        {
            if(response[i]){
                document.getElementById(String(i)).classList = "disabledButton";
                document.getElementById(String(i)).disabled = true;
            }
        }
    }
    )
}

seek()
setInterval(seek, 500)