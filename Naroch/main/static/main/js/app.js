$(document).ready(function() {
    setInterval(window.onload = function(){


//! Fixed Hider - закрепление меню
//!_______________________________________________________
$(function() { 

    let header = $("#header");

    let intro = $("#intro");
    let introH = intro.innerHeight();
    let scrollPos = $(window).scrollTop();
    
    $(window).on("scroll load resize", function(){
        introH = intro.innerHeight();
        scrollPos = $(this).scrollTop();
        if (scrollPos > introH) {
            header.addClass("fixed");
        } else {
            header.removeClass("fixed");
        }
    });


//! Nav Toggle - бургер меню
//!_______________________________________________________

let nav = $("#nav")
let navToggle = $("#navToggle")

navToggle.on("click", function(event) {
    event.preventDefault();
    nav.toggleClass("show");

});

//! Fixed Hider - закрепление меню в photo и layout 2
//!_______________________________________________________

let header_l2 = $('#header_l2');
let heighit_l2 = $('#heighit_l2');

let heighit_l2H = heighit_l2.innerHeight();
let scrollPos_l2 = $(window).scrollTop();

$(window).on("scroll", function(){
    scrollPos_l2 = $(this).scrollTop();

    if (scrollPos_l2 > heighit_l2H) {
        header_l2.addClass("fixed");
    } else {
        header_l2.removeClass("fixed");
    }
})
});
});
});
