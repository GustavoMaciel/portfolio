$(document).ready(function(){
	AOS.init({ disable: 'mobile' });
    
    //Getting the Header height
    var navbarHeight = $('#navbar-topo').outerHeight();
    $('.scroll-suave').click( function(event) {
        var linkHref = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(linkHref).offset().top - navbarHeight
        }, 755);

        event.preventDefault();
    });
});