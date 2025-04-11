$(document).ready(() => {
    $(".toggle-password").on("click", () => {
        togglePasswordField(event.target.getAttribute("data-target"))
    })
})

/**
 * Toggle Password Text <--> Password
 */
function togglePasswordField(id) {
    const passwordField = document.getElementById(id);
    const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);
}
