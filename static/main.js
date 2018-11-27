// JavaScript Document
  $(function(){
			var wid=$("body").width();
			if(wid<600){
				$(".container").width(wid);
				$("#form").css("width","90%");
			}
			else{
				$(".container").width(600);
				$("#form").width(450);
			}
		});

	$(window).resize(function(){
			var wid=$("body").width();
			if(wid<600){
				$(".container").width(wid);
				$("#form").css("width","90%");
			}
			else{
				$(".container").width(600);
				$("#form").width(450);
			}
	});
	

function setTime(ele){
	var time=$(ele).prop("id");
	$("#time").val(time);
	$("#subtime").text($(ele).text());
	$("#timevalue").removeAttr("disabled");
	$("#timevalue").attr("placeholder","时限");
	if(time=='p'){
		$("#timevalue").attr("disabled","disabled");
		$("#timevalue").attr("placeholder","");
		$("#timevalue").val("");
	}
}
 function checkform(){
	 var title=$("#title").val()!="";
	 var content=$("#content").val()!="";
	 var time=$("#timevalue").val()!="";
	 if(title&&content&&time){
		 var str="";
		 if($("#title").val().length<6){
			 str+="标题不少于6个字\n";
		 }
	 	if($("#content").val().length<20){
			 str+="内容不少于20个字\n";
		 }
	 	 if($("#timevalue").val()>59){
			 str+="时限不大于59\n";
		 }
		 if(str!=""){
			 $("#mes").text(str);
			 return false;
		 }else return true;
	 }else{
		 $("#mes").text("请填完必填项");
		 return false;
	 } 
 }

