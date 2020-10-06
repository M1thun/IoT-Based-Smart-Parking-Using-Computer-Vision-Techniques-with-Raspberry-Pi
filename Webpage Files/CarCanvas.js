var car=new Image();
car.src="redcar.png";
var park;
var ctx;
var canvas;
window.onload = function() {

   canvas = document.getElementById("myCanvas");
   ctx = canvas.getContext("2d");
};
function canvas(){

   ctx.fillStyle ="rgb(230,230,230)";
   ctx.fillRect(0, 0, canvas.width, canvas.height);
   
   //VARIABLES
   var num_cars=10;
   var car_width=120;
   var car_height=220;
   var car_bias=20;

   var space=canvas.width/6;   
   var stepCount =6 ;
   $("#myCanvas").load("load.php");

   $.ajax({
     url: 'ret.php',
     success: function (response) {
	   if(!response.includes("Notice")){
      park=response;
	  }
   }
    });
	

 
   //ROAD
   ctx.fillStyle="rgb(60,60,60)";
   ctx.fillRect(0,0,canvas.width,200);

   
   //WHITE STRIPE
   ctx.lineCap="butt";
   ctx.setLineDash([80,40]); 
   ctx.lineWidth=8;
   ctx.beginPath();
   ctx.moveTo(0,canvas.height/4.5);
   ctx.lineTo(canvas.width, canvas.height/4.5);
   ctx.strokeStyle = 'white';
   ctx.stroke();
 
   //PLACING CARS ACCORDING TO INFO
   var axis=car_bias;
   ctx.font = " 30pt Arial";
   ctx.textAlign = "center";
   ctx.strokeStyle = 'black';
   ctx.lineWidth=1.5;
   ctx.fillStyle="white";
   ctx.setLineDash([]);
   
   

   for (var j = 0; j <= stepCount; j++)
   {
	   if (park[j]=='1')
	   {
		  ctx.beginPath();
   		   ctx.rect(j*space, 205, space, canvas.height);

           ctx.fill();
           ctx.lineWidth = 2;
           ctx.strokeStyle = '#ffff00';
           ctx.stroke();
		   ctx.drawImage(car, axis+6, canvas.height-100-140,car_width,car_height);
		   ctx.fillStyle="white";
		   ctx.fillText(j+1, axis+65, canvas.height-100,30);
	   }
	   else
	   {
		 ctx.beginPath();
		   ctx.rect(j*space, 205, space, canvas.height);
           ctx.fillStyle = '#7dff7d';
           ctx.fill();
           ctx.lineWidth = 2;
           ctx.strokeStyle = '#ffff00';
           ctx.stroke();
		   ctx.fillStyle="white";
		   ctx.fillText(j+1, axis+65, canvas.height-100,30);
	   }
	   axis=axis+car_width+2*car_bias+5;
		   
   }
   	  ctx.font="30px Arial";
      ctx.fillText("Way to L H C",650,60);
	  ctx.beginPath();
      canvas_arrow(ctx, 500, 78, 800, 78);
      ctx.lineWidth = "3";
      ctx.lineCap = "round";
      ctx.fillStyle="White";
      ctx.stroke();
	  function canvas_arrow(context, fromx, fromy, tox, toy) {
	  var headlen = 20; // length of head in pixels
	  var dx = tox - fromx;
	  var dy = toy - fromy;
	  var angle = Math.atan2(dy, dx);
	  context.moveTo(fromx, fromy);
	  context.lineTo(tox, toy);
	  context.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
	  context.moveTo(tox, toy);
	  context.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
}

 
};
    setInterval(canvas,1000);