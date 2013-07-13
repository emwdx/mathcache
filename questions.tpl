<!DOCTYPE html>
<html lang="en">

<head>
<title>Math Cache</title>
<link rel="stylesheet" type="text/css" href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css">

</head>

<body>
<div class = "container">

%for question in questions:

%if(question[1]==''):

	<div class = "row-fluid">
		
			<h2>
			
			{{!question[0]}}
			
			</h2>
	
	</div>
%else:

	<div class = "row-fluid">
	<div class = "span4">
		<img src = "/static/{{question[1]}}">
	</div>
	<div class = "span8">
		<h2>
			
			{{!question[0]}}
			
		</h2>
	</div>
	</div>
	
%end

%end
	<hr>
	
	<div class = "row-fluid">
		<form action = "/" method = "GET">
		<p class = "text-info text-center">Multiply your answers to the three questions together and round to the nearest integer.
		<input type = "text" name = "newlocation" >
		<button class = "btn">Go to Location</button>
		</p>
	
	</div>
</div>
</body>
</html>
