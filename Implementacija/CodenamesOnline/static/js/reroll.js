// Andrej Solaja


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

const rezervneReci = remaining_words;
var selectedBoxes = [];
var oldWords = [];
var newWords = [];

document.addEventListener('DOMContentLoaded', function() {
  let boxes = document.querySelectorAll('.box');

  boxes.forEach(function(box) {
    box.addEventListener('click', function() {
        
        if(selectedBoxes.includes(box)) {
          selectedBoxes.pop(box);
          box.classList.remove("selected");
        }else if (selectedBoxes.length < 3){
          selectedBoxes.push(box);
          box.classList.add("selected");
        }
        console.log(selectedBoxes);
        

    });
  });

});

function reRoll() {
  
  selectedBoxes.forEach(function(box) {
    box.classList.remove("selected");
    oldWords.push(box.innerHTML);
    let newWord = rezervneReci.pop();
    box.innerHTML = newWord
    newWords.push(newWord)
  })

  console.log("reroll POST sent")
    fetch(window.location.href,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({'old_words': oldWords, 'new_words': newWords})
        }
    )

  selectedBoxes = [];
  newWords = [];
  oldWords = [];

}


    
