// Andrej Solaja
// Function to shuffle array
function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;}

var id_color = {};
var box_selected = "0";
var guessed_words = []

document.addEventListener('DOMContentLoaded', function() {
  let boxes = document.querySelectorAll('.box');
  console.log(boxes)
  boxes.forEach(function(box, index) {
      // box.classList.add(colors[index]);
    for (var i = 0; i < box.classList.length; i++) {
        if (box.classList[i].includes("blue") || box.classList[i].includes("red") ||
            box.classList[i].includes("black") || box.classList[i].includes("white")) {

            id_color[box.id] = box.classList[i];
            if(word_dict[box.innerHTML][1] == 0){
                box.classList.remove(box.classList[i]);
            }

            break;
        }
    }

  });
  boxes.forEach(function(box) {
    box.addEventListener('click', function() {
        // This function will be executed when a box is clicked
        if (word_dict[box.innerHTML][1] == 1) {
            return;
        }
        if(box_selected != 0) {
            console.log(box_selected)
          document.getElementById(box_selected).classList.remove("selected");
        }
        box_selected = box.id;
        box.classList.add("selected");

    });
  });

});

async function guess() {
    console.log(box_selected)
  let box = document.getElementById(box_selected);
  box.classList.remove("selected");
  box.classList.add(id_color[box.id]);
  word_dict[box.innerHTML][1] = 1;
  guessed_words.push(box.innerHTML)

  // TODO LOGIC for checking is he guessing correctly
    try{
       const fetchResponse = await fetch(window.location.href,
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({'tileIndex': box_selected, 'guessed_word': box.innerHTML, 'action': "guess"})
    }).then(function(response) {
        return response.json(); // Parse the JSON response
    })
    .then(function(data) {
        // Ako je receno da je kraj poteza, treba da reloaduje?
        if (data.done === true){
            location.reload();
       }
    })
    // .then(function(res){ console.log(res) })
    .catch(function(res){ console.log(res) })
    } catch (e) {
      console.log(e)
    }

}

async function end_guess(){
    console.log("end guess")
    fetch(window.location.href,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({'action': "end_guess"})
        }
    )
}