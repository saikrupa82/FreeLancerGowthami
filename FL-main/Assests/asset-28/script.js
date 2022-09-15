<<<<<<< HEAD
careers=[["anotification-1","23-08-2022"],
["notification-2","23-08-2022"],
["anotification-3","23-08-2022"],
["notification-4","23-08-2022"],
["anotification-5","23-08-2022"],
["notification-6","23-08-2022"],
["anotification-7","23-08-2022"],
["notification-8","23-08-2022"],
["anotification-9","23-08-2022"],
["notification-10","23-08-2022"],
["anotification-11","23-08-2022"],
["notification-12","23-08-2022"],
["anotification-13","23-08-2022"],
["notification-14","23-08-2022"],
["anotification-15","23-08-2022"],
["notification-16","23-08-2022"],
["anotification-17","23-08-2022"],
["notification-18","23-08-2022"],
["anotification-19","23-08-2022"],
["adsadnotification-20","23-08-2022"],
["adsadnotification-21","23-08-2022"]
];
console.log(careers);

let activepg = 0;

setcat();
function show(index){
    let pgold = document.getElementById(`pg${activepg}`);
    let pgnew = document.getElementById(`pg${index}`);
    pgold.classList.remove("active");
    pgnew.classList.add("active");
    activepg = index;
    let notifications = careers;
    let noti_html = ``;
    for(let i=(index*10); i<(index*10)+10;i++){
      try{
        noti_html += `<div class="box">
        <p style="flex-grow: 8;">${notifications[i][0]}</p>
        <p style="flex-grow: 2;">${notifications[i][1]}</p>
      </div>`
      }
      catch{break;}
    }
    document.getElementById("notifications").innerHTML=noti_html;
}
function setcat(){
    setpages();
    show(0);
}

function setpages(){
  pages = Math.ceil((careers.length)/10);
  let pages_html = `<a onclick="show(${0})" id="pg${0}" class="active" href="#">1</a>`
  for(let i=2;i<=pages;i++){
      pages_html += `<a onclick="show(${i-1})" id="pg${i-1}" href="#">${i}</a>`;
  }
  document.getElementById("pagination").innerHTML = pages_html;
}

=======
careers=[["anotification-1","23-08-2022"],
["notification-2","23-08-2022"],
["anotification-3","23-08-2022"],
["notification-4","23-08-2022"],
["anotification-5","23-08-2022"],
["notification-6","23-08-2022"],
["anotification-7","23-08-2022"],
["notification-8","23-08-2022"],
["anotification-9","23-08-2022"],
["notification-10","23-08-2022"],
["anotification-11","23-08-2022"],
["notification-12","23-08-2022"],
["anotification-13","23-08-2022"],
["notification-14","23-08-2022"],
["anotification-15","23-08-2022"],
["notification-16","23-08-2022"],
["anotification-17","23-08-2022"],
["notification-18","23-08-2022"],
["anotification-19","23-08-2022"],
["adsadnotification-20","23-08-2022"],
["adsadnotification-21","23-08-2022"]
];
console.log(careers);

let activepg = 0;

setcat();
function show(index){
    let pgold = document.getElementById(`pg${activepg}`);
    let pgnew = document.getElementById(`pg${index}`);
    pgold.classList.remove("active");
    pgnew.classList.add("active");
    activepg = index;
    let notifications = careers;
    let noti_html = ``;
    for(let i=(index*10); i<(index*10)+10;i++){
      try{
        noti_html += `<div class="box">
        <p style="flex-grow: 8;">${notifications[i][0]}</p>
        <p style="flex-grow: 2;">${notifications[i][1]}</p>
      </div>`
      }
      catch{break;}
    }
    document.getElementById("notifications").innerHTML=noti_html;
}
function setcat(){
    setpages();
    show(0);
}

function setpages(){
  pages = Math.ceil((careers.length)/10);
  let pages_html = `<a onclick="show(${0})" id="pg${0}" class="active" href="#">1</a>`
  for(let i=2;i<=pages;i++){
      pages_html += `<a onclick="show(${i-1})" id="pg${i-1}" href="#">${i}</a>`;
  }
  document.getElementById("pagination").innerHTML = pages_html;
}

>>>>>>> a8b8591f24ac99c12ac59b07afd0af39833fc4f9
