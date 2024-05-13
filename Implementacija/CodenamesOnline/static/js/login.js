// Teodor Djelic
var attempted = false;

var username_email_field = document.getElementById("username_email");
var password_field = document.getElementById("password");

var error_box = document.getElementById("errorMsg");

if(error_box.innerHTML === "")
{
    error_box.style.display = "None"    
}

function onClick()
{
    updateColors();
}

function updateColors()
{
    updatePColors();
    updateUColors();
}

function updateUColors()
{
    if(!username_email_field.value.localeCompare(""))
    {
        username_email_field.style.borderColor = "red";
    }
    else{
        username_email_field.style.borderColor = "var(--button-border-color)";
    }
}

function updatePColors()
{
    if(!password_field.value.localeCompare(""))
    {
        password_field.style.borderColor = "red";
    }
    else{
        password_field.style.borderColor = "var(--button-border-color)";
    }
}