$(document).ready(function(){

    //Getting the Header height
    var navbarHeight = $('#navbar-topo').outerHeight();
    $('.smooth-scroll').click(function(event){
        var linkHref = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(linkHref).offset().top - headerHeight
        }, 755);

        event.preventDefault();
    });
});