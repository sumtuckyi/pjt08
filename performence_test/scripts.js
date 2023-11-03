const carousel = document.querySelector('.carousel');
const carouselItems = document.querySelectorAll('.carousel-item');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

let currentIndex = 0;

function rotateCarousel() {
    const angle = (currentIndex * 72) % 360;
    carousel.style.transform = `rotateY(${angle}deg)`;
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % carouselItems.length;
    rotateCarousel();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
    rotateCarousel();
}

nextButton.addEventListener('click', nextSlide);
prevButton.addEventListener('click', prevSlide);

setInterval(nextSlide, 3000); // Auto-rotate every 3 seconds
