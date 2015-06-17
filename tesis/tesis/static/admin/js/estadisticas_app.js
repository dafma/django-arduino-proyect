$(document).ready(function(){


    $.getJSON("dispositivos/update/", function(data){

        $('#chart1').highcharts({
            chart: {
                type: 'pie',
                options3d: {
                    enabled: true,
                    alpha: 45,
                    beta: 0
                }
            },
            title: {
                text: 'Dispositivo cantidad usado'
            },
            tooltip: {
                pointFormat: '{dispositivos.id}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    depth: 35,
                    dataLabels: {
                        enabled: true,
                                           }
                }
            },
            series: [{
                type: 'pie',
                name: 'Porcentaje',
                data: data 
            }]
        });

    });


    $.getJSON("dispositivos/update/", function(data){

        // Build the chart
        $('#chart2').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: 'Dispositivo mas Demandado'
            },
            tooltip: {
                pointFormat: '{dispositivos.nombre}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    }
                }
            },
            series: [{
                type: 'pie',
                name: 'Browser share',
                data: data
            }]
        });

    });
});
