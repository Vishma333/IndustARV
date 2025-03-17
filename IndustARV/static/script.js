document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a");

    links.forEach(link => {
        link.addEventListener("mouseover", () => {
            link.style.transform = "scale(1.1)";
        });

        link.addEventListener("mouseleave", () => {
            link.style.transform = "scale(1)";
        });
    });
});
