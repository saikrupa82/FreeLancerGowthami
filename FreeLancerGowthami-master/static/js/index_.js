let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  slides[slideIndex-1].style.display = "block";
}

function show_close(id) {
  ans=document.getElementById(id);
  sym=document.getElementById('s'+id);
  if(ans.style.display == "block"){
    ans.style.display = "none";
    sym.innerHTML="▼"
  }
  else{
    ans.style.display = "block";
    sym.innerHTML="▲"
  }

}