const exit_btn = document.querySelector('.exit');
const container_mobile = document.querySelector('.container_mobile');
const navbar_mobile = document.querySelector('.navbar_mobile');
let background_image = document.querySelector('body');


window.addEventListener('scroll', function() {
    console.log(pageYOffset)
    if(pageYOffset >= 0 && pageYOffset <=100) {
        background_image.className = 'background_image ' 
    }
    else{
        background_image.className = 'background_image active';
    }
});
