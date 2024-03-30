let times_clicked = 0;

function send_set(){
    times_clicked++;
    console.log(times_clicked)
    if(times_clicked == 1){
        // Greska ime vec postoji
        document.getElementById("name_error").innerHTML = "There already exists a set with that name.";
    } else if (times_clicked == 2){
        // Greska nedovoljno reci
        document.getElementById("name_error").innerHTML = "";
        document.getElementById("word_error").innerHTML = "Not enough words! The minimum is 31.";
    } else if( times_clicked == 3){
        // Greska nije navedeno ime seta
        document.getElementById("name_error").innerHTML = "There is no set name. Please enter a name for you word set.";
        document.getElementById("word_error").innerHTML = "";
    } else{
        document.getElementById("name_error").innerHTML = "";
        document.getElementById("word_error").innerHTML = "";
        alert("You successfully created a set!")
    }
    
    
}