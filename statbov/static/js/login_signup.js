// Lógica para mostrar a senha ao clicar no ícone
const button_show_password = document.querySelector(".fa-eye");
const show_icon = document.getElementsByClassName("fa-eye")[0];
button_show_password.addEventListener("click", function () {
    const password = document.querySelector("#floatingPassword");
    if (password.type === "password") {
        password.type = "text";
        show_icon.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        password.type = "password";
        show_icon.classList.replace("fa-eye-slash", "fa-eye");
    }
});