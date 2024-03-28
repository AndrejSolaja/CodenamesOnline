// Teodor Djelic
var attempted = false;

var username_field = document.getElementById("username");

var error_box = document.getElementById("errorMsg");

const regex = new RegExp("[a-zA-Z].*@[a-zA-Z]+");

function onClick()
{
    updateColors();

    if(!username_field.value.localeCompare(""))
    {
        return;
    }

    if(!attempted){
        attempted = true;
        error_box.style.display = "inline";
        error_box.innerHTML = "User with the given username does not exist!";
    }
    else{
        attempted = true;
        error_box.style.display = "inline";
        error_box.innerHTML = "The password recovery email has been sent!";
        setTimeout(() => {
            window.location.href = "Home.html";
        }, 2000);
    }

}

function updateColors()
{
    updateUColors();
}

function updateUColors()
{
    if(!username_field.value.localeCompare(""))
    {
        username_field.style.borderColor = "red";
    }
    else{
        username_field.style.borderColor = "var(--button-border-color)";
    }
}