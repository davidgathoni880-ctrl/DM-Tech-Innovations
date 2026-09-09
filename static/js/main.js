/* 
   DM TECH INNOVATIONS
   MAIN JAVASCRIPT
   */

document.addEventListener("DOMContentLoaded", function () {

    "use strict";


    /* 
       1. NAVIGATION
     */

    const navbar =
        document.querySelector(".navbar");

    const navbarCollapse =
        document.querySelector(".navbar-collapse");

    const navigationLinks =
        document.querySelectorAll(
            ".navbar .nav-link, .navbar .btn"
        );


    navigationLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                if (
                    navbarCollapse &&
                    navbarCollapse.classList.contains("show") &&
                    window.innerWidth < 992 &&
                    window.bootstrap
                ) {

                    const collapse =
                        bootstrap.Collapse.getInstance(
                            navbarCollapse
                        ) ||
                        new bootstrap.Collapse(
                            navbarCollapse,
                            {
                                toggle: false
                            }
                        );

                    collapse.hide();

                }

            }
        );

    });


    /* =========================================================
   ACTIVE NAVIGATION LINK
   ========================================================= */

const sections = document.querySelectorAll(
    "section[id]"
);

const sectionLinks = document.querySelectorAll(
    '.navbar .nav-link[href^="#"]'
);

function updateActiveNavigation() {

    let currentSection = "";

    sections.forEach(function (section) {

        const sectionTop =
            section.offsetTop - 120;

        if (
            window.scrollY >= sectionTop
        ) {
            currentSection =
                section.getAttribute("id");
        }

    });

    sectionLinks.forEach(function (link) {

        link.classList.remove("active");

        if (
            link.getAttribute("href") ===
            "#" + currentSection
        ) {
            link.classList.add("active");
        }

    });

    /* Highlight Home when at the top */
    if (window.scrollY < 100) {

        sectionLinks.forEach(function (link) {
            link.classList.remove("active");
        });

        const homeLink =
            document.querySelector(
                '.navbar .nav-link[href="/"]'
            );

        if (homeLink) {
            homeLink.classList.add("active");
        }

    }

}

window.addEventListener(
    "scroll",
    updateActiveNavigation
);

updateActiveNavigation();
    /* 
       2. NAVBAR SCROLL EFFECT
         */

    function navbarScrollEffect() {

        if (!navbar) {
            return;
        }

        if (window.scrollY > 50) {

            navbar.classList.add(
                "navbar-scrolled"
            );

        } else {

            navbar.classList.remove(
                "navbar-scrolled"
            );

        }

    }


    window.addEventListener(
        "scroll",
        navbarScrollEffect,
        {
            passive: true
        }
    );

    navbarScrollEffect();


    /* 
       3. SMOOTH SCROLLING
        */

    const anchorLinks =
        document.querySelectorAll(
            'a[href^="#"]'
        );


    anchorLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function (event) {

                const targetID =
                    link.getAttribute("href");


                if (
                    !targetID ||
                    targetID === "#"
                ) {
                    return;
                }


                const targetElement =
                    document.querySelector(
                        targetID
                    );


                if (targetElement) {

                    event.preventDefault();


                    const navbarHeight =
                        navbar
                            ? navbar.offsetHeight
                            : 0;


                    const targetPosition =
                        targetElement
                            .getBoundingClientRect()
                            .top +
                        window.scrollY -
                        navbarHeight;


                    window.scrollTo({

                        top: targetPosition,

                        behavior: "smooth"

                    });


                    history.pushState(
                        null,
                        "",
                        targetID
                    );

                }

            }
        );

    });


      /* 
   4. SCROLL REVEAL
*/

const revealElements =
    document.querySelectorAll(
        ".reveal"
    );


if (
    "IntersectionObserver" in window
) {

    const revealObserver =
        new IntersectionObserver(
            function (
                entries,
                observer
            ) {

                entries.forEach(
                    function (entry) {

                        if (
                            !entry.isIntersecting
                        ) {
                            return;
                        }

                        entry.target.classList.add(
                            "revealed"
                        );

                        observer.unobserve(
                            entry.target
                        );

                    }
                );

            },
            {
                threshold: 0.12
            }
        );


    revealElements.forEach(
        function (element) {

            revealObserver.observe(
                element
            );

        }
    );

} else {

    revealElements.forEach(
        function (element) {

            element.classList.add(
                "revealed"
            );

        }
    );

}


/* 
   4B. ABOUT SECTION REVEAL
*/

const aboutSection =
    document.querySelector(
        ".about-section"
    );


if (
    aboutSection &&
    "IntersectionObserver" in window
) {

    const aboutObserver =
        new IntersectionObserver(
            function (entries, observer) {

                entries.forEach(
                    function (entry) {

                        if (
                            !entry.isIntersecting
                        ) {
                            return;
                        }

                        aboutSection.classList.add(
                            "about-visible"
                        );

                        observer.unobserve(
                            aboutSection
                        );

                    }
                );

            },
            {
                threshold: 0.15
            }
        );


    aboutObserver.observe(
        aboutSection
    );

} else if (aboutSection) {

    aboutSection.classList.add(
        "about-visible"
    );

}
    /* 
       5. SERVICE CARD EFFECT
        */

    const cards =
        document.querySelectorAll(
            ".card"
        );


    cards.forEach(function (card) {

        card.addEventListener(
            "mouseenter",
            function () {

                card.classList.add(
                    "card-hover"
                );

            }
        );


        card.addEventListener(
            "mouseleave",
            function () {

                card.classList.remove(
                    "card-hover"
                );

            }
        );

    });


    /* 
       6. BACK TO TOP BUTTON
         */

    let backToTop =
        document.getElementById(
            "backToTop"
        );


    if (!backToTop) {

        backToTop =
            document.createElement(
                "button"
            );

        backToTop.id =
            "backToTop";

        backToTop.type =
            "button";

        backToTop.setAttribute(
            "aria-label",
            "Back to top"
        );

        backToTop.innerHTML =
            '<i class="bi bi-arrow-up"></i>';

        document.body.appendChild(
            backToTop
        );

    }


    function updateBackToTop() {

        if (
            window.scrollY > 500
        ) {

            backToTop.classList.add(
                "show"
            );

        } else {

            backToTop.classList.remove(
                "show"
            );

        }

    }


    window.addEventListener(
        "scroll",
        updateBackToTop,
        {
            passive: true
        }
    );


    backToTop.addEventListener(
        "click",
        function () {

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        }
    );


    updateBackToTop();


    /*
       7. DISABLE EMPTY # LINKS
        */

    const emptyLinks =
        document.querySelectorAll(
            'a[href="#"]'
        );


    emptyLinks.forEach(
        function (link) {

            link.addEventListener(
                "click",
                function (event) {

                    event.preventDefault();

                }
            );

        }
    );


    /*
       8. PAGE LOADED
       */

    window.addEventListener(
        "load",
        function () {

            document.body.classList.add(
                "page-loaded"
            );

        }
    );


    /* 
       9. REDUCED MOTION
       */

    const reducedMotion =
        window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches;


    if (reducedMotion) {

        document.documentElement.classList.add(
            "reduce-motion"
        );

    }


    /*
       10. CONSOLE TEST
       */

    console.log(
        "DM Tech Innovations JavaScript loaded successfully."
    );

});

