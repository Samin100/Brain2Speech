$(document).ready(function(){
  //refreshes 10x a second
    setInterval(refresh, 100);
})

function refresh(){

  var curr_col = '-10';
  var curr_row = '-10';

    //string refresh
      $.get("/string", function(string){
        if ($( ".output" ).text() != string) {
          $(".output").html(string);
        }
  });

  $.get("/next", function(next){
    if (next == 'True') {
      $(".hash").css("background-color","green");
    }else if(next == 'False'){
      $(".hash").css("background-color","#1E445D");
    }
});


   $.get("/col", function(col){

     if(col == '0'){  //white and empty
       $(".col1").css("background-color","white");
       $(".col2").css("background-color","white");
       $(".col3").css("background-color","white");
       $(".col4").css("background-color","white");
       $(".col5").css("background-color","white");
       $(".col6").css("background-color","white");

     }
     if(col != curr_col){
       curr_col = col;
     if (col == '1') {
      $(".col1").css("background-color","deepskyblue");

    }else if(col == '2'){
      $(".col1").css("background-color","white");
      $(".col2").css("background-color","deepskyblue");
    }else if(col == '3'){
      $(".col2").css("background-color","white");
      $(".col3").css("background-color","deepskyblue");
    }else if(col == '4'){
      $(".col3").css("background-color","white");
      $(".col4").css("background-color","deepskyblue");
    }else if(col == '5'){
      $(".col4").css("background-color","white");
      $(".col5").css("background-color","deepskyblue");
    }else if(col == '6'){
      $(".col5").css("background-color","white");
      $(".col6").css("background-color","deepskyblue");
    }
  }
});

$.get("/row", function(row){

  if(row != curr_row){
    curr_row = row;

  if (row == '1') {
   $(".row1").css("background-color","deepskyblue");

 }else if(row == '2'){
   $(".row1").css("background-color","white");
   $(".row2").css("background-color","deepskyblue");
 }else if(row == '3'){
   $(".row2").css("background-color","white");
   $(".row3").css("background-color","deepskyblue");
 }else if(row == '4'){
   $(".row3").css("background-color","white");
   $(".row4").css("background-color","deepskyblue");
 }else if(row == '5'){
   $(".row4").css("background-color","white");
   $(".row5").css("background-color","deepskyblue");
 }
 }
});



}
