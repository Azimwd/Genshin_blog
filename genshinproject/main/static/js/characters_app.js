"use strict";
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = document.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
let timeDom = document.querySelector('.carousel .time');
let charapers_item = document.querySelector('.carousel .list .item');

let search_title = document.querySelectorAll('.search_container .serach_list .charapter_list li');
let SliderItemsDom = document.querySelectorAll('.carousel .list .item');

let timeRunning = 500;

search_title.forEach((e,i)=>{
    e.addEventListener('click',()=>{
        SliderItemsDom.forEach((e1,i)=>{
            console.log(((SliderItemsDom[i].innerText).toLowerCase()));
            if((SliderItemsDom[i].innerText).toLowerCase().includes((e.innerText).toLowerCase())){
                SliderDom.prepend(e1);
                thumbnailBorderDom.appendChild(thumbnailItemsDom[i]);
                carouselDom.classList.add('next');
            }  
            clearTimeout(runTimeOut);
            runTimeOut = setTimeout(() => {
                carouselDom.classList.remove('next');
                carouselDom.classList.remove('prev');
            }, timeRunning);
        });
    });
});


document.querySelector('#serach_list_id').oninput = function(){
    let val = (this.value.trim()).toLowerCase();
    let elasticItems = document.querySelectorAll('.charapter_list li');
    if (val != ''){
        elasticItems.forEach((e)=>{
            if((e.innerText).toLowerCase().search(val) == -1){
                e.style.display = 'none';    
            }
            else{
                e.style.display = 'block'; 
            }
        });
    }
    else{
        elasticItems.forEach((e)=>{
            e.style.display = 'none';    
        });
    }
}

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);


nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;

function showSlider(type){
    let  SliderItemsDom = document.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);
}