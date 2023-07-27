const imgs = document.querySelectorAll('.np_image');
const modalMain = document.querySelector('.modal--main');
const modalSideLeft = document.querySelector('.modal--side--left');
const modalSideRight = document.querySelector('.modal--side--right');
const activeImage = document.querySelector('#active--image');
const overlay = document.querySelector('.overlay');
const closeIcon = document.querySelector('.close_btn');

//! Вставляем картинку в молальное окно
//!_________________________________________________________________

imgs.forEach(img => img.addEventListener('click', displayImage));

function displayImage(e) {
    
    activeImage.src = e.target.src;
    // console.log(e.target.src)
    modalMain.style.display = 'block'
    overlay.style.display = 'block'
    modalSideLeft.style.display = 'flex'
    modalSideRight.style.display = 'flex'
}

//! Закрытие модального окна
//!_________________________________________________________________

if(closeIcon){
closeIcon.addEventListener('click', closeImage);
}
overlay.addEventListener('click', closeImage);

function closeImage() {
    modalMain.style.display = 'none'
    overlay.style.display = 'none'
    modalSideLeft.style.display = 'none'
    modalSideRight.style.display = 'none'
}

//! Вперёд
//!_________________________________________________________________

const next = document.querySelector("#modal--side--right").addEventListener('click', nextImage);

function nextImage() {
    for(var i = 0; i < imgs.length; i++){
        if (activeImage.src === imgs[i].src) {
        var nextImageVar = imgs[i].nextElementSibling;
        }
    }
    if (nextImageVar === null) {
        activeImage.src = imgs[0].src;
    }
    else{
        activeImage.src = nextImageVar.src;
    }
}

//! Назад
//!_________________________________________________________________

const previous = document.querySelector('#modal--side--left').addEventListener('click', previousImage);

function previousImage() {
    for(var i = 0; i < imgs.length; i++){
        if (activeImage.src === imgs[i].src) {
            var nextImageVar = imgs[i].previousElementSibling;
        }
    }
    if (nextImageVar === null) {
        activeImage.src = imgs[imgs.length -1 ].src;
    }
    else{
    activeImage.src = nextImageVar.src;
    }
}

//! Свайпы
//!_________________________________________________________________

document.addEventListener('touchstart', handleTouchStart, false);
document.addEventListener('touchmove', handleTouchSMove, false);

const x1 = null;
const y1 = null;

function handleTouchStart(event){
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
    console.log(x2, y2);

    if(Math.abs(xDiff) > Math.abs(yDiff)){
        if(xDiff > 0 ) previousImage();
        else nextImage();
    }
    x1= null;
};
