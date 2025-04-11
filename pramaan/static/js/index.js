$(document).ready(() => {
    /**
     * Default Commons jQuery Utility
     */
    setTimeout(() => {
        $(".alert-message") && $(".alert-message").fadeOut("slow");
    }, 5000);

    $(".alert-dismiss").on("click", () => {
        $(".alert-message") && $(".alert-message").fadeOut("slow");

    });
});
