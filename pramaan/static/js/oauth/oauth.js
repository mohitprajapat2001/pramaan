$(document).ready(() => {
    /* If user changes any form field then enable submit button */
    $('form').on('change', 'input, select, textarea', function () {
        $('button[type="submit"]').prop('disabled', false);
    });
})
