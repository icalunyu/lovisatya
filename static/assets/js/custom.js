$(document).ready(function(){

  $('#id_attending').change(function() {
    if ($('#id_attending option[value="reception"]').is(':selected') || $('#id_attending option[value=""]').is(':selected')) {
      $('#id_keypass').val('');
      $('.thecode').hide();
      $('#id_keypass').prop('required',false);
    } else {
      $('#id_keypass').val('');
      $('.thecode').show();
      $('#id_keypass').prop('required',true);
    }
  })

  $('#id_keypass').focus(function() {
    $('.error-form').hide();
  })

  $('#id_keypass').change(function() {
    var code = $(this).val();

    $.ajax({
      url: '/ajax/validate_code/',
      data: {
        'keypass': code
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_true) {
          $('.error-form').hide();
          $('.rsvp-form-submit').prop('disabled', false);
        } else {
          $('.error-form').show();
          $('.rsvp-form-submit').prop('disabled', true);
        }
      }
    });
  });

  $(".scrolldown").on('click', function(event) {
    $('html, body').animate({
        scrollTop: $('#story').offset().top
      }, 300, function(){
    });
  });

});
