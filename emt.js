document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("enrollmentForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); 

    
        const fullName = document.getElementById("fullName").value.trim();
        const studentID = document.getElementById("studentID").value.trim();
        const email = document.getElementById("email").value.trim();
        const dob = document.getElementById("dob").value.trim();
        const gradeLevel = document.getElementById("gradeLevel").value;
        const guardianName = document.getElementById("guardianName").value.trim();
        const guardianContact = document.getElementById("guardianContact").value.trim();
        const address = document.getElementById("address").value.trim();
        const fileInput = document.getElementById("documents").files[0];

        
        if (!fullName || !studentID || !email || !dob || !gradeLevel || !guardianName || !guardianContact || !address) {
            alert("Please fill in all required fields.");
            return;
        }

        
        if (fileInput) {
            const fileSize = fileInput.size / 1024 / 1024; 
            if (fileSize > 5) {
                alert("File size must not exceed 5MB.");
                return;
            }
        }

        alert("Enrollment Submitted Successfully!");
        form.reset();
    });
});