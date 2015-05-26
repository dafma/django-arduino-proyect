function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var token = getCookie('csrftoken');



$(document).ready(function() {
    $(".dispositivos").bootstrapSwitch({
        size: "large",
        onText: "Encendido",
        offText: "Apagado"

    });

    $(".dispositivos").on('switchChange.bootstrapSwitch', function(event, state) {
        
        $.ajax({
            type: 'POST',
            url: '/dispositivos/update/',
            data: {
                id: event.target.name,
                is_on: state,
                csrfmiddlewaretoken: token                            
            },
            dateType: 'json',
            success: function (resp) {
                //calendar.fullCalendar('refetchEvents');
            }
        });


    });

});