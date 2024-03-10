let setimg = document.querySelectorAll('.setimg');
    weppon = document.querySelectorAll('.description.weppon'),
    watch = document.querySelectorAll('.description.watch'),
    flower = document.querySelectorAll('.description.flower'),
    cup = document.querySelectorAll('.description.cup'),
    feather = document.querySelectorAll('.description.feather'),
    cap = document.querySelectorAll('.description.cap')
    
    constimg = document.querySelectorAll('.constimg');
    const1 = document.querySelectorAll('.description.const1'),
    const2 = document.querySelectorAll('.description.const2'),
    const3 = document.querySelectorAll('.description.const3'),
    const4 = document.querySelectorAll('.description.const4'),
    const5 = document.querySelectorAll('.description.const5'),
    const6 = document.querySelectorAll('.description.const6'),

    list = document.querySelector('.main_slaider .list'),
    slaid = document.querySelectorAll('.slaid'),
    menu = document.querySelector('.menu'),
    assembly = document.querySelector('.assembly'),
    assembly_li = document.querySelectorAll('.assembly ul li'),
    assembly_exit = document.querySelector('.assembly .exit')
    slaid1 = document.querySelector('.slaid.first'),
    slaid2 = document.querySelector('.slaid.second'),
    slaid3 = document.querySelector('.slaid.third'),
    slaid4 = document.querySelector('.slaid.fourth'),
    slaid5 = document.querySelector('.slaid.fifth');

change_slaid();
open_cose_menu();
show_artefacts_const();

function change_slaid(){
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        assembly_li.forEach((e)=>{
            e.addEventListener('click',()=>{
                assembly.style.display = 'none';
            })
        })
      } else {
        assembly_li.forEach((e)=>{
            e.addEventListener('click',()=>{
                slaid.forEach((e2)=>{
                    e2.style.display = 'none';
                    if (e.classList == e2.classList[1]){
                        e2.style.display = 'block';
                        list.prepend(e2);
                    };
                })
            })
        })
    }       
}

function open_cose_menu(){
    assembly_exit.addEventListener('click', ()=>{
        assembly.style.display = 'none';
    })
    
    menu.addEventListener('click', ()=>{
        assembly.style.display = 'block';
    })
}

function show_artefacts_const(){
    weppon.forEach((e)=>{
        e.style.display = 'block';
    })
    const artefacts = [weppon,watch,flower,cup,feather,cap] 
    const constellation = [const1,const2,const3,const4,const5,const6]
    
    setimg.forEach((e)=>{ // перебор артефактов
        e.addEventListener('click',()=>{
            artefacts.forEach((e2)=>{ // Перебор описания артефакта 
                e2.forEach((e3)=>{ // Перебор каждого описания артефакта по очереди их несколько например описание оружия и надо перебирать каждый
                    e3.style.display = 'none'; // Скрываем описание артов
                    if (e3.classList[1] == e.classList[1]) { // Если нажатый класс арта равно описанию арта то делаем его видимым
                        e3.style.display = 'block';
                    }
                })
                constellation.forEach((e2)=>{ // перебор созвездия
                    e2.forEach((e3)=>{ // Перебор каждого описания созвездия по очереди их несколько например 1 созвездия и надо перебирать каждый**
                        e3.style.display = 'none';
                    })   
                })
            })
    
        })
    });
    
    
    constimg.forEach((e)=>{ // перебор констов
        e.addEventListener('click',()=>{
            weppon.forEach((e)=>{
                e.style.display = 'none';
            })
            constellation.forEach((e2)=>{ // Перебор описания созвездия 
                e2.forEach((e3)=>{ // Перебор каждого описания созвездия по очереди их несколько например описание 1 созвездия и надо перебирать каждый
                    e3.style.display = 'none';
                    if (e3.classList[1] == e.classList[1]) {
                        e3.style.display = 'block';
                    }
                })
            })
            artefacts.forEach((e2)=>{
                e2.forEach((e3)=>{
                    e3.style.display = 'none';
                }) 
                
            })
        })
    });
    
}




