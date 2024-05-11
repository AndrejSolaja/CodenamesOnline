// Teodor Djelic
var attempted = false;

var username_email_field = document.getElementById("username_email");
var password_field = document.getElementById("password");

var error_box = document.getElementById("errorMsg");

function onClick()
{
    updateColors();

    if(!username_email_field.value.localeCompare("admin") && !password_field.value.localeCompare("admin")){
        window.location.href = 'administrator';
    }

    if(!username_email_field.value.localeCompare("")
        || !password_field.value.localeCompare(""))
    {
        return;
    }

    if(!attempted){
        attempted = true;
        error_box.style.display = "inline";
        error_box.innerHTML = "Incorrect password!";
    }
    else{
        window.location.href = 'home';
    }

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