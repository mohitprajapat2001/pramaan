let options = null
$(document).ready(() => {
    $("#id_city").selectize({
        'placeholder': "Please Choose City"
    })
    $(".selectize-control").addClass("border border-primary rounded-sm")
    // getRequest("/api/v1/city/", getCitiesSuccess);
    // $("#id_city-selectized").on("keyup", () => {
    //     getRequest(`/api/v1/city/?q=${event.target.value}`, getCitiesSuccess);
    // })
})

// /**
//  * callback function to update the options
//  */
// function getCitiesSuccess(response) {
//     if (response.count) {
//         options = response.results;
//         const dropdownContent = document.querySelector(".selectize-dropdown-content")
//         dropdownContent.innerHTML = ""
//         options.forEach((item) => {
//             dropdownContent.innerHTML += `
//             <div class="option" data-selectable="" data-value="${item.id}">${item.display_name}</div>`
//         })
//     }

// }
