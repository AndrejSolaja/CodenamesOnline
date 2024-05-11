// Teodor Djelic
const imena = ["Marko", "Ivan", "Petar", "Zika"];

var lider1imena = ""
var igraci1imena = ""

var lider2imena = ""
var igraci2imena = ""

var i1 = 0;
var i2 = 0;

function igrac1(){
    if(i1 != 1){
        if(igraci1imena.localeCompare("")){
            igraci1imena += ",";
        }

        igraci1imena += " " +  imena.pop();
        updateIgraci1();

        i1++;
        if(i1 == 1){
            document.getElementById("b2").disabled = true;
            document.getElementById("b2").classList += "disabledButton";
        }
    }
}

function igrac2(){
    if(i2 != 1){
        if(igraci2imena.localeCompare("")){
            igraci2imena += ",";
        }

        igraci2imena += " " + imena.pop();
        updateIgraci2();

        i2++;
        if(i2 == 1){
            document.getElementById("b4").disabled = true;
            document.getElementById("b4").classList += "disabledButton";
        }
    }
}


function lider1(){
    if(!lider1imena.localeCompare("")){
        lider1imena = imena.pop();
        updateIgraci1();
        document.getElementById("b1").disabled = true;
        document.getElementById("b1").classList += "disabledButton";
    }
}

function updateIgraci1(){
    var string = "Leader: " + lider1imena + "\nPlayers:" + igraci1imena;
    document.getElementById("igraci1").innerHTML = string;

    if(imena.length == 0){
        window.location.href = "reroll.html";
    }
}

function lider2(){
    if(!lider2imena.localeCompare("")){
        lider2imena = imena.pop();
        updateIgraci2();
        document.getElementById("b3").disabled = true;
        document.getElementById("b3").classList += "disabledButton";
    }
}

function updateIgraci2(){
    var string = "Leader: " + lider2imena + "\nPlayers:" + igraci2imena;
    document.getElementById("igraci2").innerHTML = string;

    if(imena.length == 0){
        window.location.href = "reroll.html";
    }
}

updateIgraci1();
updateIgraci2();