// 第一題
const welcome_message_block = document.querySelector(".welcome");
welcome_message_block.addEventListener('click',()=>{
    const message_text = document.querySelector(".welcome-paragraph");
    message_text.textContent = "Have a Good Time!"
});

//第二題
// 一開始設定 display 是 none
const hidden_boxes = document.querySelector(".hidden-boxes");
hidden_boxes.style.display = 'none';

const button_click_to_show = document.querySelector("button");
button_click_to_show.addEventListener('click', ()=>{
    
    if(hidden_boxes.style.display === 'none'){
        hidden_boxes.style.display = 'block';
        button_click_to_show.textContent = "click to hide";
    }else{
        hidden_boxes.style.display = 'none';
        button_click_to_show.textContent = "click to show";
    }
    
});

