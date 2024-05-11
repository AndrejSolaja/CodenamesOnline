// Andrej Solaja
// Function to shuffle array
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}


// Array to store colors
var rezervneReci = ["Porcelan", "Jakna", "Kosovo", "Sistem", "Pistolj", "Pas"];
shuffle(rezervneReci);
var selectedBoxes = [];

// Shuffle the colors array

// Assign colors to boxes
document.addEventListener('DOMContentLoaded', function() {
  let boxes = document.querySelectorAll('.box');

  boxes.forEach(function(box, index) {
    box.classList.add("blue");
  });  
  boxes.forEach(function(box) {
    box.addEventListener('click', function() {
        // This function will be executed when a box is clicked
        
        if(selectedBoxes.includes(box)) {
          selectedBoxes.pop(box);
          box.classList.remove("selected");
        }else if (selectedBoxes.length < 3){
          selectedBoxes.push(box);
          box.classList.add("selected");
        }
        console.log(selectedBoxes);
        

        // You can perform any actions you want here
    });
  });

});

var i = 0;

function reRoll() {
  
  selectedBoxes.forEach(function(box) {
    box.classList.remove("selected");
    box.innerHTML = rezervneReci.pop();
  })
  selectedBoxes = [];

  i++;

  if(i == 1){
    document.getElementById("re-roll-submit-button").disabled = true;
    setTimeout(() => {
      window.location.href = "zadavanjeAsocijacija.html";
    }, 3000);
    
  }

}
    
