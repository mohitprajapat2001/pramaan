/*Ajax Requests */
function getRequest(url, callback) {
  ajaxCall("GET", url, null, callback);
}

function postRequest(url, data, callback) {
  ajaxCall("POST", url, data, callback);
}

function putRequest(url, data, callback) {
  ajaxCall("PUT", url, data, callback);
}

function deleteRequest(url, callback) {
  ajaxCall("DELETE", url, null, callback);
}

function ajaxCall(method, url, data, callback) {
  const ajaxToken = document.querySelector("[name=csrfmiddlewaretoken]");
  $.ajax({
    url: url,
    type: method,
    data: data,
    headers: {
      "X-CSRFToken": ajaxToken.value,
    },
    success: function (content, status, xhr) {
      if (xhr.status == 201) {
        triggerAlert("Successfully Created");
      }
      callback && callback(content)
    },
    error: function (xhr, error, status) {
      if (xhr.status == 400) {
        const errors = JSON.parse(xhr.responseText);
        Object.values(errors).forEach((error) => {
          triggerAlert(error)
        });
      }
      console.error(`An Error Occured with Status ${status} ${xhr.status}`);
    },
  });
}
