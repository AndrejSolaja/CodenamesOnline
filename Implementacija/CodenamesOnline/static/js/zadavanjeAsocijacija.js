document.addEventListener('DOMContentLoaded', function() {
    let boxes = document.querySelectorAll('.box');
    console.log(boxes)
    boxes.forEach(function (box, index) {
        // box.classList.add(colors[index]);
        if (word_dict[box.innerHTML][1] == 1) {
            for (var i = 0; i < box.classList.length; i++) {
                if (box.classList[i].includes("blue") || box.classList[i].includes("red") ||
                    box.classList[i].includes("black") || box.classList[i].includes("white")) {

                    var color = box.classList[i];

                    box.classList.remove(box.classList[i]);
                    box.classList.add(color + "Selected");

                    break;
                }
            }
        }


    });
});