document.addEventListener('DOMContentLoaded', function () {
    new Swiper('.swiper', {
        direction: 'horizontal',
        loop: true,
        speed: 1000,
        autoplay: true
    });
})

const container = document.querySelector('.scroll-container');
const sections = document.querySelectorAll('.scroll-section');
const dots = document.querySelectorAll('.fixed.right-8 button');
let isScrolling = false;

function scrollToSection(index) {
    if (!isScrolling) {
        isScrolling = true;
        sections[index].scrollIntoView({ behavior: 'smooth' });
        updateDots(index);
        setTimeout(() => {
            isScrolling = false;
        }, 1000);
    }
}

function updateDots(index) {
    dots.forEach((dot, i) => {
        dot.className = `w-3 h-3 rounded-full transition-all duration-300 ${i === index ? 'bg-white scale-150' : 'bg-white/20 hover:bg-white hover:scale-150'
            }`;
    });
}

// Update dots on scroll
container.addEventListener('scroll', () => {
    const index = Math.round(container.scrollTop / window.innerHeight);
    updateDots(index);
});

// Initialize first dot
updateDots(0);
