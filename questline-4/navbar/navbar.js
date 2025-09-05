(function(){
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.navbar a');


function onScroll(){
let current = '';
sections.forEach(section => {
const top = window.scrollY;
const offset = section.offsetTop - 80;
const height = section.offsetHeight;
if(top >= offset && top < offset + height){
current = section.getAttribute('id');
}
});


navLinks.forEach(link => {
link.classList.remove('active');
if(link.getAttribute('href') === '#' + current){
link.classList.add('active');
}
});
}


window.addEventListener('scroll', onScroll);
})();