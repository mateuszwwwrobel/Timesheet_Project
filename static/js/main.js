const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links li');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    links.forEach(link =>{
        link.classList.toggle('fade');
    });
}); 


function clicked() {
    return confirm('Another week down? Are you sure you want to reset your timesheet?');
}