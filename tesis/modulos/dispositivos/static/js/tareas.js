    

    
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

    function deleteEvent(eventId) {

        $.ajax({
            type: 'POST',
            url: '/tareas/delete/',
            data: {
                //opcion: "borrar",
                id: eventId,
                csrfmiddlewaretoken: token                            
            },
            dateType: 'json',
            success: function (resp) {
                $('#calendar').fullCalendar('refetchEvents');
            }
        });
    }

    $(document).ready(function() {
        var calendar = $('#calendar').fullCalendar({
            //theme: true,
            
            defaultView: 'agendaWeek',
            //weekends: false,
            //firstHour: 7,
            //maxTime: 19,
            //minTime: 7,
            editable: true,
            selectable: true,
            selectHelper: true,
            droppable: true, 
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay'
            },
             buttonText: {
                prev:     'Anterior', // <
                next:     'Siguiente', // >
                prevYear: '&laquo;',  // <<
                nextYear: '&raquo;',  // >>
                today:    'hoy',
                month:    'mes',
                week:     'semana',
                day:      'dia'
            },
            //allDayDefault: false, 
            //allDaySlot: false,
            dayNames:['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sabado'],
            dayNamesShort:['Dom','Lun','Mar','Mier','Jue','Vie','Sab'],
            monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            monthNamesShort: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            
            /*columnFormat:{
                month: 'ddd',    // Mon
                week: 'ddd ', // Mon 9/7
                day: 'dddd '  // Monday 9/7
            },*/
            
            eventMouseover: function(calEvent, domEvent) {
                var layer = "<div id='events-layer' class='fc-transparent' style='position:absolute; width:100%; height:100%; top:-1px; text-align:right; z-index:100'> <a> <img width='22px' height='18px' border='0' style='padding-right:5px;' src='/media/x.png' onClick='deleteEvent("+calEvent.id+");'></a></div>";
                $(this).append(layer);
            },

            eventMouseout: function(calEvent, domEvent) {
                 $("#events-layer").remove();
            }, 

            select: function (startDate, endDate, allDay, jsEvent) {
               
                /*
                calendar.fullCalendar('renderEvent', {
                    title: "asdasd",
                    start: startDate,
                    end: endDate,
                    allDay: allDay,
                }, false // make the event "unstick"
                );*/
                //YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
                var inicio = $.fullCalendar.formatDate(startDate, 'yyyy-MM-dd HH:mm:ss[Z]');
                var fin = $.fullCalendar.formatDate(endDate, 'yyyy-MM-dd HH:mm:ss[Z]');

                $.ajax({
                    type: 'POST',
                    url: '/tareas/create/',
                    data: {
                        inicio: inicio,
                        fin: fin,
                        title: 'Tarea',
                        csrfmiddlewaretoken: token                            
                    },
                    dateType: 'json',
                    success: function (resp) {
                        calendar.fullCalendar('refetchEvents');
                    }
                });
                calendar.fullCalendar('unselect');
            },

            
            eventResize: function(event, dayDelta, minuteDelta, revertFunc) {
                var id = event.id;
                var startDate=event.start;
                var endDate=event.end;
                var inicio = $.fullCalendar.formatDate(startDate, 'yyyy-MM-dd HH:mm:ss[Z]');
                var fin = $.fullCalendar.formatDate(endDate, 'yyyy-MM-dd HH:mm:ss[Z]');
                $.ajax({
                    type: 'POST',
                    url: '/tareas/update/',
                    data: {
                        //opcion: "actualizar",
                        id: id,
                        inicio: inicio,
                        fin: fin,
                        title: 'Tarea',
                        csrfmiddlewaretoken: token                            
                    },
                    dateType: 'json',
                    success: function (resp) {
                        calendar.fullCalendar('refetchEvents');
                    }
                });
                calendar.fullCalendar('unselect');

            },

            
            eventDrop: function(event, dayDelta, minuteDelta, allDay, revertFunc) {
                var id=event.id;
                var startDate=event.start;
                var endDate=event.end;
                var inicio = $.fullCalendar.formatDate(startDate, 'yyyy-MM-dd HH:mm:ss[Z]');
                var fin = $.fullCalendar.formatDate(endDate, 'yyyy-MM-dd HH:mm:ss[Z]');
                $.ajax({
                    type: 'POST',
                    url: '/tareas/update/',
                    data: {
                        //opcion: "actualizar",
                        id: id,
                        inicio: inicio,
                        fin: fin,
                        title: 'Tarea',
                        csrfmiddlewaretoken: token                            
                    },
                    dateType: 'json',
                    success: function (resp) {
                        calendar.fullCalendar('refetchEvents');
                    }
                });
                calendar.fullCalendar('unselect');
            },

            events: '/tareas/list/',
            eventRender: function (event, element) {
                element.find('.fc-event-title').html("<b>"+event.title+": </b>"+event.dispositivo__nombre+ "<br><b>Status: </b>"+event.status);
            }
        });    
    });