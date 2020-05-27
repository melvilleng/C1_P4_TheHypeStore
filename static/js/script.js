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

