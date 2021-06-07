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

function withdraw() 
{
    $('#withdrawTxt').text("Kindly wait for 24 hours we are checking your details.");
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



function change_pass() 
{
    var userid = $('#username').val();
    var current = $('#current_pass').val();
    var new_pass = $('#new_pass').val();
    var confirm = $('#confirm_pass').val();
    $('#msg1').hide();
    $('#msg1').hide();

    if (new_pass!=confirm)
    {
        $('#msg2').text("Password did not match!");
        $('#msg2').show();
    }
    else
    {
        $.ajax({
            type: 'POST',
            url: "change_password",
            data: {
            user: userid,
            password:current,
            new_password:new_pass,
            csrfmiddlewaretoken: $('meta[name="_token"]').attr('content')
            },
            success: function (data) {
                if(data==0)
                {
                    $('#msg1').text('Incorrect password!');
                    $('#msg1').show();
                }
                else
                {
                    $('#msg2').text("Password Changed Successfully ");
                    $('#msg2').show();
                }
            },
        });
    }
    
}
