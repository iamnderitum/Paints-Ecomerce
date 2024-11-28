import { Carousel, initMDB } from "mdb-ui-kit";

initMDB({ Carousel });

$(document).ready(function(){
    $(".intro-slider").owlCarousel({
        items: 1,               // One item visible at a time
        loop: true,             // Loop through slides continuously
        autoplay: true,         // Enable autoplay
        autoplayTimeout: 5000,  // Slide duration in milliseconds
        autoplayHoverPause: true, // Pause on hover
        dots: true,             // Enable dots for navigation
        nav: true,              // Enable navigation arrows
        navText: ["<", ">"],    // Custom navigation arrows
        responsive: {
            0: {
                nav: false       // Hide navigation on small screens
            },
            992: {
                nav: true        // Show navigation on larger screens
            }
        }
    });
});

// Adding Touch Support for Mobile

document.querySelectorAll('.product').forEach(product => {
    product.addEventListener('touchstart', () => {
        product.classList.add('hover');
    });
    product.addEventListener('touchend', () => {
        product.classList.remove('hover');
    });
});

document.querySelector('.mobile-menu-toggle').addEventListener('click', function () {
    document.querySelector('.top-menu-right').classList.toggle('active');
});
