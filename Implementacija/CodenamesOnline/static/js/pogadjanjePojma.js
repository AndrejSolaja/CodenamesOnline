// Andrej Solaja
// Function to shuffle array


var id_color = {};
var box_selected = "0";

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
        if(box_selected != 0) {
            console.log(box_selected)
          document.getElementById(box_selected).classList.remove("selected");
        }
        box_selected = box.id;
        box.classList.add("selected");

    });
  });

});

function checkColor() {
  let box = document.getElementById(box_selected);
  box.classList.remove("selected");
  box.classList.add(id_color[box.id]);
  word_dict[box.innerHTML][1] = 1
}
    
