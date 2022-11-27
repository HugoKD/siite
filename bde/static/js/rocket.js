var lastScrollTop = 0;
$(window).scroll(function(event){
   var st = $(this).scrollTop();
   if (st > lastScrollTop){
       $('#rocket').hide();
       $('#rocket_bottom').show();
   } else {
      $('#rocket_bottom').hide();
       $('#rocket').show();
   }
   lastScrollTop = st;
});