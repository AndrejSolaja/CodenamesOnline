// Djordje Vukovic
let circularProgress1 = document.querySelector("#profile-circ1"),
progressValue1 = document.querySelector("#profile-c-val1");

let progressStartValue1 = 0,
progressEndValue1 = 20,
speed = 25;

let progress1 = setInterval(() => {
    progressStartValue1++;
    
    progressValue1.textContent = `${progressStartValue1}%`;
    circularProgress1.style.background = `conic-gradient(#d1002a ${progressStartValue1 * 3.6}deg, #ededed  0deg)`;

    if(progressStartValue1 == progressEndValue1){
        clearInterval(progress1);
    }

}, speed);  



let circularProgress2 = document.querySelector("#profile-circ2"),
progressValue2 = document.querySelector("#profile-c-val2");

let progressStartValue2 = 0,
progressEndValue2 = 70;

let progress2 = setInterval(() => {
    progressStartValue2++;
    
    progressValue2.textContent = `${progressStartValue2}%`;
    circularProgress2.style.background = `conic-gradient(#0023e8 ${progressStartValue2 * 3.6}deg, #ededed  0deg)`;

    if(progressStartValue2 == progressEndValue2){
        clearInterval(progress2);
    }

}, speed);  