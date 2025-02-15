"use strict";var menuBtn=document.querySelector(".menu-btn"),
menu=document.querySelector(".menu"),
menuNav=document.querySelector(".menu-nav"),
navItems=document.querySelectorAll(".nav-item"),
md_trigger=document.querySelectorAll(".md__trigger")
,md_modal=document.querySelector(".md__modal"),
md_close=document.querySelector(".md__close"),
navLinks=document.querySelectorAll(".nav-link"),
// days=document.querySelector(".days"),
hours=document.querySelector(".hours"),
minutes=document.querySelector(".minutes"),
seconds=document.querySelector(".seconds"),
counter=document.querySelector(".counter__container"),
showMenu=!1;
function toggleMenu()
{showMenu=showMenu?(menuBtn.classList.remove("close"),
menu.classList.remove("show"),
menuNav.classList.remove("show"),
navItems.forEach(function(e){return e.classList.remove("show")}),!1):(menuBtn.classList.add("close"),menu.classList.add("show"),menuNav.classList.add("show"),navItems.forEach(function(e){return e.classList.add("show")}),!0)}function closeMenu(){showMenu=showMenu?(menuBtn.classList.remove("close"),menu.classList.remove("show"),menuNav.classList.remove("show"),navItems.forEach(function(e){return e.classList.remove("show")}),!1):(menuBtn.classList.add("close"),menu.classList.add("show"),menuNav.classList.add("show"),navItems.forEach(function(e){return e.classList.add("show")}),!0)}menuBtn.addEventListener("click",toggleMenu),navLinks.forEach(function(e){return e.addEventListener("click",closeMenu)});
// var html,body,countDownDate=new Date("Apr 22, 2019 00:00:00").getTime(),countDownFunction=setInterval(function(){var e=(new Date).getTime(),n=countDownDate-e;days.innerHTML=Math.floor(n/864e5),hours.innerHTML=Math.floor(n%864e5/36e5),minutes.innerHTML=Math.floor(n%36e5/6e4),seconds.innerHTML=Math.floor(n%6e4/1e3),n<0&&(clearInterval(countDownFunction),counter.style.display="none")},1e3);function scroll(n,o,t){var s,c=n<o?10:-10,r=setInterval(function(){var e=Math.round(body.scrollTop||html.scrollTop);s==e||n<o&&o<=e||o<n&&e<=o?(clearInterval(r),window.location.hash=t):(body.scrollTop+=c,html.scrollTop+=c,s=e)},1)}window.onload=function(){var e=document.links;html=document.documentElement,body=document.body;for(var n=0;n<e.length;n++)e[n].onclick=function(){var e=Math.round(body.scrollTop||html.scrollTop);if(""!==this.hash){event.preventDefault();for(var n=0,o=document.getElementById(this.hash.substring(1));o.offsetParent;)n+=o.offsetTop,o=o.offsetParent;scroll(e,n=Math.round(n),this.hash)}}},md_trigger.forEach(function(e){return e.addEventListener("click",function(){md_modal.classList.add("md__show")})}),md_close.addEventListener("click",function(){md_modal.classList.remove("md__show")});