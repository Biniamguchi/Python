$(document).ready(function(){
    $('ul li').click(function(e){
        var ind = $(this).attr('ind')

        $.get('/turtles/'+ind,function(data){
            data = data.split(' ');
            $('h1').html("You chose "+data[0]+"!");
            $('img').attr('src',"static/"+data[2])
        })
    })
})