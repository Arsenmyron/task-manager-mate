document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll(".index-card");
    const activeColor = "#333";
    let currentIndex = -1;

    cards.forEach((card, index) => {
        card.addEventListener("click", () => {
            if (currentIndex !== -1) {
                const prevCard = cards[currentIndex];
                prevCard.classList.remove("active");
                prevCard.style.backgroundColor = "";
                prevCard.style.color = "";
                const prevArrow = prevCard.querySelector(".index-arrow");
                if (prevArrow) prevArrow.style.display = "none";

                const prevCardBody = prevCard.querySelector(".index-card-body");
                if (prevCardBody) {
                    prevCardBody.style.fontSize = "20px";
                    prevCardBody.classList.remove("active");
                }
            }

            card.classList.add("active");
            card.style.backgroundColor = activeColor;
            card.style.color = "white";

            const cardBody = card.querySelector(".index-card-body");
            if (cardBody) {
                cardBody.style.fontSize = "24px";
                cardBody.classList.add("active");
            }

            const arrow = card.querySelector(".index-arrow");
            if (arrow) arrow.style.display = "block";

            currentIndex = index;
        });
    });
});
