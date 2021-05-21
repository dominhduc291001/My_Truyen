$("#sizeBox").change(function (){
    let mySize = $("#sizeBox").val() + "px";
   $("#reading-book").css("font-size",mySize);
})
$("#lineBox").change(function (){
    $("#reading-book").css("line-height",$("#lineBox").val());
})
$("#colorBox").change(function (){
    $("#reading-book").css("color",$("#colorBox").val());
})
$("#fontBox").change(function (){
    $("#reading-book").css("font-family",$("#fontBox").val());
})