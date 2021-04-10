 /* Code For JavaScript(Website) (Contributed By : Pruthvik Sheth)  */


const header = document.querySelector('header');



var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    header.style.top = "0px";
  } else {
    header.style.top = "-120px";
  }
  prevScrollpos = currentScrollPos;
}

document.addEventListener('scroll',function(){
    if(document.documentElement.scrollTop > 100 || document.body.scrollTop > 100)
    {
      document.getElementById("upButton").style.display = "block";
    }
    else
    {
      document.getElementById("upButton").style.display = "none";
    }
  });
