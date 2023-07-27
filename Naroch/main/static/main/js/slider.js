const images = document.querySelectorAll('#slider_line img');
const sliderLine = document.querySelector('#slider_line');
let count = 0;
let width;
let timer;

function slider() {
    width = document.querySelector('#slider').offsetWidth;
    sliderLine.style.width = width*images.length + 'px';
    images.forEach(item =>{
        item.style.width = width + 'px';
        item.style.height = 'auto';
    });
    rollSlider();
}

//! Сдвигание
//!_________________________________________________________________

function rollSlider(){
    sliderLine.style.transform = "translate(-" + count * width + 'px)';
}

//! Вперёд
//!_________________________________________________________________

document.querySelector("#slider_next").addEventListener('click', next);
function next() {
    count++;
    if (count >= images.length) {
        count = 0;
    }
    rollSlider();
}

//! Назад
//!_________________________________________________________________

document.querySelector("#slider_prev").addEventListener('click', prev);
function prev() {
    count--
    if (count <0) {
        count = images.length -1;
    }
    rollSlider();
}

//! Авто прокрутка
//!_________________________________________________________________

function autoSlider() {
    timer = setInterval(next, 7000);
}

//! Пересчёт при изменении размера страницы
//!_________________________________________________________________

window.addEventListener('resize', slider);

//! Свайпы
//!_________________________________________________________________
document.addEventListener('touchstart', handleTouchStart, false);
document.addEventListener('touchmove', handleTouchSMove, false);

const x1 = null;
const y1 = null;

function handleTouchStart(event){ //? Ищем координаты
    const firstTouch = event.touches[0];
    x1 = firstTouch.clientX;
    y1 = firstTouch.clientY;
};
function handleTouchSMove(event){
    if(!x1 || !y1){
    return false;
    };
    let x2 =  event.touches[0].clientX;
    let y2 =  event.touches[0].clientY;

    let xDiff = x2 - x1;
    let yDiff = y2 - y1;

    if(Math.abs(xDiff) > Math.abs(yDiff)){
        if(xDiff > 0 ) prev();
        else next();
    }
    // else{ //? Вниз, вверх не нужно
    //     if(yDiff > 0 ) console.log("bottom"); //? Вниз
    //     else console.log("top"); //? Вверх
    // }
    x1 = null;
    y1 = null;
};

//! Запуск слайдера
//!_________________________________________________________________
slider();
autoSlider();
