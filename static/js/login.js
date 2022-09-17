var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});


$('#br_block').bootstrapBirthday({
    widget: {
        wrapper: {
            tag: 'div',
            class: 'row'
        },
        wrapperYear: {
            use: true,
            tag: 'div',
            class: 'col-sm-4'
        },
        wrapperMonth: {
            use: true,
            tag: 'div',
            class: 'col-sm-4'
        },
        wrapperDay: {
            use: true,
            tag: 'div',
            class: 'col-sm-4'
        },
        selectYear: {
            name: 'birthday[year]',
            class: 'form-control'
        },
        selectMonth: {
            name: 'birthday[month]',
            class: 'form-control'
        },
        selectDay: {
            name: 'birthday[day]',
            class: 'form-control'
        }
    }

});

// Bindings
$("#sign_up_form").submit(function(e) {
    e.preventDefault();
    var api_endpoint = $(this).attr('action');
    var formData = new FormData(this);
    sendForm(api_endpoint, formData).then(function(resp){
        if (resp["status"]){
            window.location.replace("/feed");
        }else{
            $("#email_already_used").css("display", "block");
        }
    });
});

$("#login_form").submit(function(e) {
    e.preventDefault();
    var api_endpoint = $(this).attr('action');
    var formData = new FormData(this);
    sendForm(api_endpoint, formData).then(function(resp){
        if (resp["status"]){
            window.location.replace("/feed");
        }else{
            $("#invalid_auth").css("display", "block");
        }
    });
});