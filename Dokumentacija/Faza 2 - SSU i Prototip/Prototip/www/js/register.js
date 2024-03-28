// Teodor Djelic
var attempted = false;

var username_field = document.getElementById("username");
var email_field = document.getElementById("email");
var password_field = document.getElementById("password");
var password_confirmed_field = document.getElementById("password_confirmed");

var error_box = document.getElementById("errorMsg");

const regex = new RegExp("[a-zA-Z].*@[a-zA-Z]+");

function onClick()
{
    updateColors();

    if(!username_field.value.localeCompare("")
        || !password_field.value.localeCompare("")
        || !email_field.value.localeCompare("")
        || !password_confirmed_field.value.localeCompare(""))
    {
        return;
    }

    if(!regex.test(email_field.value)){
        error_box.style.display = "inline";
        error_box.innerHTML = "Incorrect email!";
        return;
    }

    if(password_field.value.localeCompare(password_confirmed_field.value)){
        error_box.style.display = "inline";
        error_box.innerHTML = "Passwords do not match!";
        return;
    }

    if(!attempted){
        attempted = true;
        error_box.style.display = "inline";
        error_box.innerHTML = "Username already exists!";
    }
    else{
        window.location.href = "HomeLoggedIn.html";
    }

}

function updateColors()
{
    updatePCColors();
    updatePColors();
    updateEColors();
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

function updateEColors()
{
    if(!email_field.value.localeCompare("") || !regex.test(email_field.value))
    {
        email_field.style.borderColor = "red";
    }
    else{
        email_field.style.borderColor = "var(--button-border-color)";
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

function updatePCColors()
{
    if(!password_confirmed_field.value.localeCompare("")
        || password_field.value.localeCompare(password_confirmed_field.value))
    {
        password_confirmed_field.style.borderColor = "red";
    }
    else{
        password_confirmed_field.style.borderColor = "var(--button-border-color)";
    }
}