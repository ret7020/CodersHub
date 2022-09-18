

// Bindings
$("#new_post_form").submit(function(e) {
    e.preventDefault();
    var api_endpoint = $(this).attr('action');
    var formData = new FormData(this);
    sendForm(api_endpoint, formData).then(function(resp){
        if (resp["status"]){
            var myModal = $("#createModal");
            var modal = bootstrap.Modal.getOrCreateInstance(myModal)
            modal.hide()
        }else{
            $("#publication_error").css("display", "block");
        }
    });
});