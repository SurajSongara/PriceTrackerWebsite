function show_wallet() {
    $('#cart').hide();
    $('#password_change').hide();
    $('#wallet').show();
}

function show_cart() {
    $('#wallet').hide();
    $('#password_change').hide();
    $('#cart').show();
}

function password_change() {
    $('#wallet').hide();
    $('#cart').hide();
    $('#password_change').show();
}

function withdraw() {
    $('#withdrawTxt').text("Your withdrawl request has been sent successfully, kindly wait for 24 hours.");
}

function remove(id) {
    $.ajax({
        type: 'POST',
        url: "/cartremove",
        data: {
            product_id: id,
            user:  $('meta[name="_userid"]').attr('content') ,
            csrfmiddlewaretoken: $('meta[name="_token"]').attr('content')
        },
        success: function (data) {
            id = '#card-' + id;
            $(id).remove();
        },
    });
}