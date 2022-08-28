let drop1 = document.querySelector(".profile_displayname_abbr");
let drop2 = document.querySelector(".profile_icon");
let menu = document.querySelector(".nav_icon");
let close = document.querySelector(".close");
const mainNav = document.querySelector(".wat");
let circle_cancel = document.querySelector(".circle_closed");
const dropdown = document.querySelector(".profile_dropdown_container");
menu.addEventListener('click',showmenu);
close.addEventListener('click',showmenu);
drop1.addEventListener("click", showdropdown);
drop2.addEventListener("click", showdropdown);
circle_cancel.addEventListener("click", showdropdown);

function showmenu(){
    if (mainNav.style.display == "none"){
        mainNav.style.display = "block"
    }
    else{
        mainNav.style.display = "none"
    }

}

function showdropdown(){
     if (dropdown.style.display == "none"){
        dropdown.style.display = "block"
    }
    else{
        dropdown.style.display = "none"
    }
}




