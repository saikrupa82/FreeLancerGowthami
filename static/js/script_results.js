let def_imgs = [["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-2","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-3","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"]];

let inter_imgs = [["https://st2.depositphotos.com/1104517/11965/v/950/depositphotos_119659092-stock-illustration-male-avatar-profile-picture-vector.jpg","name-1","JD-1","2022"],
["https://st2.depositphotos.com/1104517/11965/v/950/depositphotos_119659092-stock-illustration-male-avatar-profile-picture-vector.jpg","name-2","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-3","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"],
["https://www.w3schools.com/howto/img_avatar.png","name-1","JD-1","2022"]];

let category="defence";

function setcat(cat){
    category = cat;
    show(0);
    let all_html = ``;
    if(category == "defence"){
        for(let i=0; i<def_imgs.length; i++){
            all_html += `<button onclick="show(${i})"><img src=${def_imgs[i][0]} width="130px" height="150px"></button>`
        }
        document.getElementById("all_imgs").innerHTML=all_html;
    }
    else{
        for(let i=0; i<inter_imgs.length; i++){
            all_html += `<button onclick="show(${i})"><img src=${inter_imgs[i][0]} width="130px" height="150px"></button>`
        }
        document.getElementById("all_imgs").innerHTML=all_html;
    }
}

function show(index){
    if(category == "defence"){info=def_imgs[index];}
    else{info=inter_imgs[index];}
    let img_html = `<img src=${info[0]} width="180px" height="200px" style="margin-right: 50px;"></img>
    <div class="details" id="details">
        <p>Name : ${info[1]}</p>
        <p>Job pos : ${info[2]}</p>
        <p>Batch : ${info[3]}</p>
      </div>`;
    document.getElementById("main_img").innerHTML = img_html;  
}

setcat("defence");
