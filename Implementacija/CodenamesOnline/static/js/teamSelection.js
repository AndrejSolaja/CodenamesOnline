function seek(){
    fetch('/game/players', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        console.log(response)
        for(let i = 0; i < 4; i++)
        {
            if(response[i] != null){
                document.getElementById(String(i)).classList = "disabledButton";
                document.getElementById(String(i)).disabled = true;
            }
        }
        redTeam = "Leader: "
        blueTeam = "Leader: "
        if(response[0] != null){
            redTeam += response[0]
        }
        redTeam += "&#13;&#10;Player: "
        if(response[1] != null){
            redTeam += response[1]
        }

        if(response[2] != null){
            blueTeam += response[2]
        }
        blueTeam += "&#13;&#10;Player: "
        if(response[3] != null){
            blueTeam += response[3]
        }

        if(document.getElementById("igraci1").innerHTML != redTeam)
            document.getElementById("igraci1").innerHTML = redTeam

        if(document.getElementById("igraci2").innerHTML != blueTeam)
            document.getElementById("igraci2").innerHTML = blueTeam
    }
    )

    fetch('/game/activeSet', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(response => {
        document.getElementById("setRed").innerHTML = response;
        document.getElementById("setBlue").innerHTML = response;
    }
    )
}

seek()
setInterval(seek, 500)