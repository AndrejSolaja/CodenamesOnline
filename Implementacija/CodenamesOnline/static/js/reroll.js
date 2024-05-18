// Andrej Solaja


const rezervneReci = remaining_words;
var selectedBoxes = [];

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
    box.innerHTML = rezervneReci.pop();
  })
  selectedBoxes = [];

}


    
