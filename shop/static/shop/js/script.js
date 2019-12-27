var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 5,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 2000,
    autoplayHoverPause: false,
    slideTransition: 'linear',
    autoplaySpeed: 500,
    animateOut: 'fadeOut',
    nav: false,
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
});
$('.prev').on('click', function () {
    owl.trigger('prev.owl.carousel');
    owl.trigger('play.owl.autoplay',[3000])
})
$('.next').on('click', function () {
    owl.trigger('next.owl.carousel');
})