function change(){
    var ret_val = confirm("Are you sure that you want to make changes to the words in this set?")
    if(ret_val == true){
        alert("You successfully changed the words in the selected set.")
    }
}

function unsaved_change(){
    confirm("Changes to the set haven't been made. Are you sure you want to continue?")
}

function remove_set(){
    var ret_val = confirm("Are you sure that you want to remove this set?")
    if (ret_val == true){
        alert("You successfully removed the set.")
    } else{ 
        alert("Unsuccessful removal.")
    }
    
}

function activate_set(){
    var ret_val = confirm("Are you sure that you want to activate this set?")
    if (ret_val == true){
        alert("You successfully activated the set.")
    }
    
}