document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("transactionForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent actual form submission
        alert("Your transaction request has been submitted successfully!");
        form.reset();
    });
});