document.addEventListener("DOMContentLoaded", function () {

    const sidebar = document.getElementById("sidebar");
    const toggle = document.getElementById("sidebarToggle");

    /* =================================
       MAIN SIDEBAR OPEN / CLOSE
    ================================= */

    toggle.addEventListener("click", function () {

        sidebar.classList.toggle("expanded");

    });

    /* =================================
       SUBMENU OPEN / CLOSE
    ================================= */

    const submenuToggles =
        document.querySelectorAll(".submenu-toggle");

    submenuToggles.forEach(function (menu) {

        menu.addEventListener("click", function () {

            const parent =
                menu.closest(".has-submenu");


            parent.classList.toggle("open");
            
            /* Plus → Minus */
            const icon =
                menu.querySelector(".submenu-icon");

            if (parent.classList.contains("open")) {
                icon.classList.remove("fa-plus");
                icon.classList.add("fa-minus");

            } else {
                icon.classList.remove("fa-minus");
                icon.classList.add("fa-plus");
            }

        });

    });

});