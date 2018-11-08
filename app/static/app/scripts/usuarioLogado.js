jQuery(document).ready(function ($) {

    /* ======= Scrollspy ======= */
    $('body').scrollspy({ target: '#header', offset: 400 });

    /* ======= Fixed header when scrolled ======= */

    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > 50) {
            $('#header').addClass('navbar-fixed-top');
        }
        else {
            $('#header').removeClass('navbar-fixed-top');
        }
    });

    /* ======= ScrollTo ======= */
    $('a.scrollto').on('click', function (e) {

        //store hash
        var target = this.hash;

        e.preventDefault();

        $('body').scrollTo(target, 800, { offset: -70, 'axis': 'y', easing: 'easeOutQuad' });
        //Collapse mobile menu after clicking
        if ($('.navbar-collapse').hasClass('show')) {
            $('.navbar-collapse').removeClass('show');
        }

    })})

    
// var ctx = document.getElementsByClassName("line-graph");


// var graph = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"],
//         datasets: [{
//             label: "Projetos Concluídos",
//             data: [5,10,5,14,20,15,9,10,5,0,10,1],
//             borderWidth: 6,
//             borderColor: 'rgba(77,166,253,0.85)',
//             background: 'transparent',
//         },
//         {
//             label: "Tarefas Concluídos",
//             data: [7,15,4,12,12,8,9,5,4,0,3,7],
//             borderWidth: 6,
//             borderColor: 'green',
//             background: 'transparent',
//         }]
//     }
// });

var ctx = document.getElementsByClassName("bar");
var qtProjetoPendente = document.getElementById('pendente');
var qtProjetoEmAndamento = document.getElementById('andamento');
var qtProjetoConcluido = document.getElementById('concluido');

var bar = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ['Pendente', 'Em Andamento', 'Concluído'],
        datasets: [{
            label: 'Quantidade de Projetos',
            data: [qtProjetoPendente.value, qtProjetoEmAndamento.value, qtProjetoConcluido.value],
            backgroundColor: ["#fdcb6e", "#e17055", "#00b894"],
        }]
    },
    options: {
        legend: { display: false },
        title: {
          display: true,
          text: 'Quantidade de Projetos'
        }
      }
   
});
