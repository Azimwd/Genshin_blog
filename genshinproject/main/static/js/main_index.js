const exit_btn = document.querySelector('.exit');
const container_mobile = document.querySelector('.container_mobile');
const menu__btn = document.querySelector('.menu__btn');

exit_btn.addEventListener('click',()=>{
    container_mobile.style.display = 'none';
    menu__btn.style.display = 'block';
})

menu__btn.addEventListener('click',()=>{
    container_mobile.style.display = 'block';
    menu__btn.style.display = 'none';
})
