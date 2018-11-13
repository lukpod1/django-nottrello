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

    

var ctx = document.getElementsByClassName("bar");
var qtProjetoPendente = document.getElementById('pendente');
var qtProjetoEmAndamento = document.getElementById('andamento');
var qtProjetoConcluido = document.getElementById('concluido');

var bar = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Pendente', 'Em Andamento', 'Concluído'],
        datasets: [{
            label: 'Quantidade de Projetos',
            data: [qtProjetoPendente.value, qtProjetoEmAndamento.value, qtProjetoConcluido.value],
            backgroundColor: ["#fdcb6e", "#e17055", "#00b894"],
        }]
    },
    options: {
        legend: { display: true},
        title: {
          display: true,
          text: 'Quantidade de Projetos'
        }
      }
   
});
