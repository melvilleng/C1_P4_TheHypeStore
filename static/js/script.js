let bumpToTopBtn = document.querySelector("#bringmetotop");


bumpToTopBtn.addEventListener("click", function(){
    window.scrollTo(1,1);
});

window.addEventListener("scroll", function(){
    if(window.pageYOffset > 100){
        bumpToTopBtn.style.display = "block";
    }

    else{
        bumpToTopBtn.style.display = 'none';

    }
})

 
$('#thesizechart').click(function(){
  $('#myModal').show();
});
 
let close = $('#closeM')[0];
close.onclick = function(){
  $('#myModal').hide();
}
