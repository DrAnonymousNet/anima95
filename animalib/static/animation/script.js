// const { ClickAwayListener } = require("@mui/material");

let option1 = document.querySelector(".anime-option1");
let option2 = document.querySelector(".anime-option2");
let option3 = document.querySelector(".anime-option3");
let menu = document.querySelector(".menu_bars");
let closed = document.querySelector(".close");
var y = document.querySelector('.etext');
 var z = document.querySelector('.circle');
 var w = document.querySelector('.square');
 let mainMenu = document.querySelector(".menu_ol");
 let mainM = document.querySelector(".unauth_tab .menu");


menu.addEventListener("click",showmenu)
closed.addEventListener("click",showmenu)
option1.addEventListener("click",changeOption)
option2.addEventListener("click",changeOption)
option3.addEventListener("click",changeOption)


function showmenu(){
    if (mainMenu.style.display == "none"){
        mainMenu.style.display = "block"
    }
    else{
        mainMenu.style.display = "none"
    }

     if (mainM.style.display == "none"){
        mainM.style.display = "block"
    }

}


function changeOption(){
    if (this==option1){
        y.style.display="block";
        z.style.display="none";
        w.style.display="none";
        this.setAttribute("class","fa-solid fa-font selected anime-option1");
        option2.setAttribute("class","fa-solid fa-circle anime-option2");
        option3.setAttribute("class","fa-solid fa-square anime-option3");
    }
    else if(this==option2){
        z.style.display="block";
        y.style.display="none";
        w.style.display="none";
         this.setAttribute("class","fa-solid fa-circle selected anime-option2");
        option1.setAttribute("class","fa-solid fa-font anime-option1");
        option3.setAttribute("class","fa-solid fa-square anime-option3");
    }
     if (this==option3){
        w.style.display="block";
        y.style.display="none";
        z.style.display="none";
         this.setAttribute("class","fa-solid fa-square selected anime-option3");
        option1.setAttribute("class","fa-solid fa-font anime-option1");
        option2.setAttribute("class","fa-solid fa-circle   anime-option2");
    }
}


function editText() {
    var element = document.getElementById("editNoteOverlay");
    element.classList.toggle("show")
}
//function favouritesTab() {
//    var element = document.getElementById("favouriteOverlay");
//    element.classList.toggle("favouriteShow")
//}



function viewCode() {
    var element = document.getElementById("");
    element.classList.toggle("show")
}


document.querySelector('.menu_bars').addEventListener
('click', () => document.querySelector('.menu_ol').classList.toggle('show'));

document.querySelector('.fav1').addEventListener
('click', () => document.querySelector(".favouriteOverlay").classList.toggle('favouriteShow'));

// document.querySelector('.profile_icon').addEventListener
// ('click', () => document.querySelector('.profileOverlay').classList.toggle('profileShow'));

function moveDown() {
    var element = document.getElementById("element");
    element.classList.toggle("move_down")
}

function moveUp() {
    var element = document.getElementById("element");
    element.classList.toggle("move_up")
}

function moveLeft() {
    var element = document.getElementById("element");
    element.classList.toggle("move_left")
}

function moveRight() {
    var element = document.getElementById("element");
    element.classList.toggle("appear-from-right")
}

function bounce() {
    var element = document.getElementById("element");
    element.classList.toggle("bounce")
}

function fade() {
    var element = document.getElementById("element");
    element.classList.toggle("fade")
}

function blink() {
    var element = document.getElementById("element");
    element.classList.toggle("blink")
}

function tremble() {
    var element = document.getElementById("element");
    element.classList.toggle("tremble")
}

function rotate() {
    var element = document.getElementById("element");
    element.classList.toggle("rotate")
}






function colorbg(event){
    var color = event.value;
    document.getElementsByTagName('textarea')[0].style.backgroundColor=color;
    document.getElementsByClassName('change')[0].style.backgroundColor=color;
}

//USerNote OverLay JS
function toggleText(){
    var x = document.getElementById('notes');
    if (x.style.display === 'none'){
        x.style.display = 'block'
    } else{
        x.style.display = 'none'
    };
};
// document.getElementById('notes').style.display = 'none';



//Element options experiment


