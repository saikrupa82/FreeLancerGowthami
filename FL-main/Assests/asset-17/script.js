<<<<<<< HEAD
notis={"army":[["anotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["alnotification-1","23-08-2022","25-08-2022"],
],
"navy":[["nnotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["nlnotification-1","23-08-2022","25-08-2022"],
],
"airforce":[["arnotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["arlnotification-1","23-08-2022","25-08-2022"],
]}
let category = "army";
let activepg = 0;

setcat("army");

function show(index){
    let pgold = document.getElementById(`pg${activepg}`);
    let pgnew = document.getElementById(`pg${index}`);
    pgold.classList.remove("active");
    pgnew.classList.add("active");
    activepg = index;
    let notifications = notis[category];
    let noti_html = `<div class="box head">
    <p style="flex-grow: 8;">Notification</p>
    <p style="flex-grow: 1;">Start date</p>
    <p style="flex-grow: 1;">End date</p>
  </div>`;
    for(let i=(index*10); i<(index*10)+9;i++){
      try{
        noti_html += `<div class="box">
        <p style="flex-grow: 8;">${notifications[i][0]}</p>
        <p style="flex-grow: 1;">${notifications[i][1]}</p>
        <p style="flex-grow: 1;">${notifications[i][2]}</p>
      </div>`
      }
      catch{break;}
    }
    document.getElementById("notifications").innerHTML=noti_html;
}
function setcat(cat){
    category = cat;
    setpages(cat);
    show(0);
}

function setpages(cat){
  pages = Math.ceil( notis[cat].length/10);
  let pages_html = `<a onclick="show(${0})" id="pg${0}" class="active" href="#">1</a>`
  for(let i=2;i<=pages;i++){
      pages_html += `<a onclick="show(${i-1})" id="pg${i-1}" href="#">${i}</a>`;
  }
  document.getElementById("pagination").innerHTML = pages_html;
}

=======
notis={"army":[["anotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["alnotification-1","23-08-2022","25-08-2022"],
],
"navy":[["nnotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["nlnotification-1","23-08-2022","25-08-2022"],
],
"airforce":[["arnotification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["notification-1","23-08-2022","25-08-2022"],
["arlnotification-1","23-08-2022","25-08-2022"],
]}
let category = "army";
let activepg = 0;

setcat("army");

function show(index){
    let pgold = document.getElementById(`pg${activepg}`);
    let pgnew = document.getElementById(`pg${index}`);
    pgold.classList.remove("active");
    pgnew.classList.add("active");
    activepg = index;
    let notifications = notis[category];
    let noti_html = `<div class="box head">
    <p style="flex-grow: 8;">Notification</p>
    <p style="flex-grow: 1;">Start date</p>
    <p style="flex-grow: 1;">End date</p>
  </div>`;
    for(let i=(index*10); i<(index*10)+9;i++){
      try{
        noti_html += `<div class="box">
        <p style="flex-grow: 8;">${notifications[i][0]}</p>
        <p style="flex-grow: 1;">${notifications[i][1]}</p>
        <p style="flex-grow: 1;">${notifications[i][2]}</p>
      </div>`
      }
      catch{break;}
    }
    document.getElementById("notifications").innerHTML=noti_html;
}
function setcat(cat){
    category = cat;
    setpages(cat);
    show(0);
}

function setpages(cat){
  pages = Math.ceil( notis[cat].length/10);
  let pages_html = `<a onclick="show(${0})" id="pg${0}" class="active" href="#">1</a>`
  for(let i=2;i<=pages;i++){
      pages_html += `<a onclick="show(${i-1})" id="pg${i-1}" href="#">${i}</a>`;
  }
  document.getElementById("pagination").innerHTML = pages_html;
}

>>>>>>> a8b8591f24ac99c12ac59b07afd0af39833fc4f9
