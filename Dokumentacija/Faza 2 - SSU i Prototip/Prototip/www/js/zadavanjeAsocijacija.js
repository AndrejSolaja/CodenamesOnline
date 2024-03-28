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

// Shuffle the colors array
colors = shuffle(colors);

// Assign colors to boxes
document.addEventListener('DOMContentLoaded', function() {
  var boxes = document.querySelectorAll('.box');
  boxes.forEach(function(box, index) {
    box.classList.add(colors[index]);
  });
});


// JavaScript for handling box clicks
document.querySelectorAll('.box').forEach(box => {
box.addEventListener('click', () => {
    // Example: show color on click
    // alert(box.classList);
    });
});

function skoci(){
  window.location.href = "pogadjanjePojma.html";
}