document.addEventListener('DOMContentLoaded', function () {
    new Swiper('.swiper-container', {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 8,
        autoplay: {
            delay: 8000,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        breakpoints: {
            640: {
                slidesPerView: 1.5,
            },
            1024: {
                slidesPerView: 1,
            },
        },
    })
})
