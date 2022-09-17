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