/*!
* Start Bootstrap - Blog Post v5.0.8 (https://startbootstrap.com/template/blog-post)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-post/blob/master/LICENSE)
*/
// Smooth reveal on scroll
document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('[data-animate]');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });
    elements.forEach(el => observer.observe(el));
});
