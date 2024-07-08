var typed = new Typed(".text",{
    strings:["Backend Developer", "Python Developer", "Web Developer"],
    typeSpeed : 10,
    backSpeed : 100,
    backDelay : 1000,
    loop : true
});
document.addEventListener("DOMContentLoaded", function() {
    const confirmationMessage = "Thank you for contacting us! We will be in touch with you shortly.";
    if (confirmationMessage) {
        alert(confirmationMessage);
    }
});
