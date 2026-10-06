// ======================================================
// STUDENT ATTENDANCE EXPERT SYSTEM
// JavaScript
// ======================================================

document.addEventListener("DOMContentLoaded", function () {

    // ==================================================
    // AUTO HIDE FLASH MESSAGES
    // ==================================================

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.opacity = "0";
            alert.style.transition = "opacity 0.5s ease";

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 4000);

    });


    // ==================================================
    // FORM VALIDATION
    // ==================================================

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const requiredFields =
                form.querySelectorAll("[required]");

            let valid = true;

            requiredFields.forEach(function (field) {

                if (field.value.trim() === "") {

                    valid = false;

                    field.style.border =
                        "2px solid #dc2626";

                } else {

                    field.style.border =
                        "1px solid #e2e8f0";
                }

            });

            if (!valid) {

                event.preventDefault();

                alert(
                    "Please fill in all required fields."
                );
            }

        });

    });


    // ==================================================
    // ATTENDANCE STATUS COLOR
    // ==================================================

    const statusElement =
        document.querySelector(".status");

    if (statusElement) {

        const status =
            statusElement.textContent
            .trim()
            .toLowerCase();

        if (status === "eligible") {

            statusElement.style.backgroundColor =
                "#dcfce7";

            statusElement.style.color =
                "#166534";

        }

        else if (
            status === "short attendance"
        ) {

            statusElement.style.backgroundColor =
                "#fef3c7";

            statusElement.style.color =
                "#92400e";

        }

        else if (
            status === "critical attendance"
        ) {

            statusElement.style.backgroundColor =
                "#fee2e2";

            statusElement.style.color =
                "#991b1b";
        }

    }


    // ==================================================
    // SET TODAY'S DATE
    // ==================================================

    const dateInput =
        document.querySelector(
            'input[type="date"]'
        );

    if (dateInput && !dateInput.value) {

        const today = new Date();

        const year =
            today.getFullYear();

        const month =
            String(
                today.getMonth() + 1
            ).padStart(2, "0");

        const day =
            String(
                today.getDate()
            ).padStart(2, "0");

        dateInput.value =
            `${year}-${month}-${day}`;
    }


    // ==================================================
    // TABLE ROW HOVER EFFECT
    // ==================================================

    const rows =
        document.querySelectorAll("tbody tr");

    rows.forEach(function (row) {

        row.addEventListener(
            "mouseenter",
            function () {

                row.style.transition =
                    "background-color 0.2s";

            }
        );

    });

});


// ======================================================
// DELETE CONFIRMATION
// ======================================================

function confirmDelete(studentName) {

    return confirm(
        "Are you sure you want to delete " +
        studentName +
        "?"
    );

}


// ======================================================
// SEARCH STUDENTS
// ======================================================

function searchStudents() {

    const input =
        document.getElementById(
            "studentSearch"
        );

    const table =
        document.getElementById(
            "studentTable"
        );

    if (!input || !table) {
        return;
    }

    const search =
        input.value.toLowerCase();

    const rows =
        table.querySelectorAll(
            "tbody tr"
        );

    rows.forEach(function (row) {

        const text =
            row.textContent.toLowerCase();

        if (text.includes(search)) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}


// ======================================================
// ATTENDANCE PERCENTAGE COLOR
// ======================================================

function getAttendanceColor(percentage) {

    if (percentage >= 75) {

        return "#16a34a";

    }

    if (percentage >= 60) {

        return "#d97706";

    }

    return "#dc2626";
}


// ======================================================
// ANIMATE ATTENDANCE NUMBER
// ======================================================

function animatePercentage(element) {

    if (!element) {
        return;
    }

    const target =
        parseFloat(
            element.textContent
        );

    if (isNaN(target)) {
        return;
    }

    let current = 0;

    const interval =
        setInterval(function () {

            current += 1;

            element.textContent =
                current.toFixed(0) + "%";

            if (current >= target) {

                clearInterval(interval);

                element.textContent =
                    target.toFixed(2) + "%";
            }

        }, 15);

}


// ======================================================
// PAGE LOAD ANIMATION
// ======================================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const cards =
            document.querySelectorAll(
                ".card"
            );

        cards.forEach(
            function (card, index) {

                card.style.opacity = "0";

                card.style.transform =
                    "translateY(15px)";

                setTimeout(
                    function () {

                        card.style.transition =
                            "all 0.4s ease";

                        card.style.opacity =
                            "1";

                        card.style.transform =
                            "translateY(0)";

                    },
                    index * 100
                );

            }
        );

    }
);
