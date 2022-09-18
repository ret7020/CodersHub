

// Bindings
$("#new_post_form").submit(function(e) {
    e.preventDefault();
    var api_endpoint = $(this).attr('action');
    var formData = new FormData(this);
    sendForm(api_endpoint, formData).then(function(resp){
        if (resp["status"]){
            var myModal = $("#createModal");
            var modal = bootstrap.Modal.getOrCreateInstance(myModal);
            modal.hide();
            $("#post_text_area").val('');
            $(resp["data"]).hide().prependTo(".posts_area").fadeIn();
        }else{
            $("#publication_error").css("display", "block");
        }
    });
});

$(document).ready(function() {
    getReqApi('/api/load_posts_for_user').then(function(resp){
        if (resp["status"]){
            $(".posts_area").html(resp["data"]);
        }else{

        }
        
    });
});
