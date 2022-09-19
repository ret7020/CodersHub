var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});


function reactPost(post_id, reaction_type){
    postReqApi('/api/react_post', {"post_id": post_id, "reaction_type": reaction_type}).then(function(resp){
        let reacted = $(`#post-${post_id}-card`).data("reacted");
        if (reacted == -1){
            if (reaction_type == 1){
                $(`#like-post-${post_id}-title`).addClass("text-primary");
                $(`#like-post-${post_id}-icon`).addClass("text-primary");
                $(`#post-${post_id}-card`).data("reacted", 1);
            }else if (reaction_type == 0){
                $(`#dislike-post-${post_id}-title`).addClass("text-danger");
                $(`#dislike-post-${post_id}-icon`).addClass("text-danger");
                $(`#post-${post_id}-card`).data("reacted", 0);
            }
        }else if (reacted == 1){
            
            $(`#like-post-${post_id}-title`).removeClass("text-primary");
            $(`#like-post-${post_id}-icon`).removeClass("text-primary");
            $(`#post-${post_id}-card`).data("reacted", -1);

            if (reaction_type == 0){
                $(`#dislike-post-${post_id}-title`).addClass("text-danger");
                $(`#dislike-post-${post_id}-icon`).addClass("text-danger");
                $(`#post-${post_id}-card`).data("reacted", 0);
            }
            

        }else if (reacted == 0){
            $(`#dislike-post-${post_id}-title`).removeClass("text-danger");
            $(`#dislike-post-${post_id}-icon`).removeClass("text-danger");
            $(`#post-${post_id}-card`).data("reacted", -1);

            if (reaction_type == 1){
                $(`#like-post-${post_id}-title`).addClass("text-primary");
                $(`#like-post-${post_id}-icon`).addClass("text-primary");
                $(`#post-${post_id}-card`).data("reacted", 1);
            }

            
        }
    });
}

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
            hljs.highlightAll();
        }else{
            $("#publication_error").css("display", "block");
        }
    });
});

$(document).ready(function() {
    getReqApi('/api/load_posts_for_user').then(function(resp){
        if (resp["status"]){
            $(".posts_area").html("");
            $(".posts_area").html(resp["data"]);
        }else{

        }
        
    });
});

