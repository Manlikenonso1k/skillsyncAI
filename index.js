// script.js
document.addEventListener('DOMContentLoaded', () => {
  const hamburgerMenu = document.querySelector('.hamburger-menu');
  const mobileNavMenu = document.querySelector('.mobile-nav-menu');

  hamburgerMenu.addEventListener('click', () => {
    mobileNavMenu.classList.toggle('show');
  });
});
