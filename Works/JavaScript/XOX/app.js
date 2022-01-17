var number = 3;
document.getElementById("box").addEventListener("click", function() {
    console.log('mouseClick = ' + number);
    number++;
})
document.getElementById("alt").addEventListener("click", function() {

    if (number % 2 == 1) {
        document.querySelector("#sa").style.display = "flex"



    } else if (number % 2 == 0) {
        document.querySelector("#se").style.display = "flex"
    }
})

document.getElementById("alt1").addEventListener("click", function() {

    if (number % 2 == 1) {
        document.querySelector("#sa1").style.display = "flex"



    } else if (number % 2 == 0) {
        document.querySelector("#se1").style.display = "flex"
    }
})
document.getElementById("alt2").addEventListener("click", function() {


    if (number % 2 == 1) {
        document.querySelector("#sa2").style.display = "flex"


    } else if (number % 2 == 0) {
        document.querySelector("#se2").style.display = "flex"
    }
})

document.getElementById("alt3").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa3").style.display = "flex"
    } else if (number % 2 == 0) {
        document.querySelector("#se3").style.display = "flex"
    }
})
document.getElementById("alt4").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa4").style.display = "flex"
    } else if (number % 2 == 0) {
        document.querySelector("#se4").style.display = "flex"
    }
})
document.getElementById("alt5").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa5").style.display = "flex"
    } else if (number % 2 == 0) {
        document.querySelector("#se5").style.display = "flex"
    }
})
document.getElementById("alt6").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa6").style.display = "flex"
    } else if (number % 2 == 0) {
        document.querySelector("#se6").style.display = "flex"
    }
})
document.getElementById("alt7").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa7").style.display = "flex"
    } else if (number % 2 == 0) {
        document.querySelector("#se7").style.display = "flex"
    }
})
document.getElementById("alt8").addEventListener("click", function() {
    if (number % 2 == 1) {
        document.querySelector("#sa8").style.display = "flex"

    } else if (number % 2 == 0) {
        document.querySelector("#se8").style.display = "flex"


    }
}) 
 