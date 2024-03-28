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
var colors = ['black', 
'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red',
'white', 'white', 'white', 'white', 'white', 'white', 'white'];

var id_color = {};
var box_selected = "0";
// Shuffle the colors array
colors = shuffle(colors);

// Assign colors to boxes
document.addEventListener('DOMContentLoaded', function() {
  let boxes = document.querySelectorAll('.box');
  console.log(boxes)
  boxes.forEach(function(box, index) {
    // box.classList.add(colors[index]);
    id_color[box.id] = colors[index];
  });  
  boxes.forEach(function(box) {
    box.addEventListener('click', function() {
        // This function will be executed when a box is clicked
        if(box_selected != 0) {
          document.getElementById(box_selected).classList.remove("selected");
        }
        box_selected = box.id;
        box.classList.add("selected");

        // You can perform any actions you want here
    });
  });

});

function checkColor() {
  let box = document.getElementById(box_selected);
  box.classList.remove("selected");
  box.classList.add(id_color[box.id]);
}
    
