<!DOCTYPE html> 
<html>

	<!-- Vorlage für die mobile App für den Conrad Raspberry Pi Adventskalender -->

<head>
	
	<?php
		if ($_POST["servoCCW"]) {
			echo exec('python /var/www/html/day20/pyramidServoCCW.py');
		} elseif ($_POST["servoCW"]) {
			echo exec('python /var/www/html/day20/pyramidServoCW.py');			
		} elseif ($_POST["running"]) {
			echo exec('python /var/www/html/day20/pyramidLedRunning.py');			
		} elseif ($_POST["blinking"]) {
			echo exec('python /var/www/html/day20/pyramidLedBlinking.py');			
		}	
	?>	
	
	<title>Conrad Raspberry Pi Adventskalender</title>
	
	<!-- CSS-Dateien für die Formatierung -->
	
	<link rel="stylesheet" type="text/css" href="css/general-styles.css">
	<link rel="stylesheet" media="screen and (max-width: 1200px) and (min-width: 601px)" href="css/styles_1200px.css" />
	<link rel="stylesheet" media="screen and (max-width: 600px) and (min-width: 351px)" href="css/styles_600px.css" />
	<link rel="stylesheet" media="screen and (max-width: 350px)" href="css/styles_350px.css" />
	

</head>
<body>
<div id="envelope">
<header>
    <h2>Conrad Raspberry Pi Adventskalender</h2>
</header>
<hr>

<form action="index.php" method="post">  
	<input name="servoCCW" id="servoCCW" type="submit" value="Pyramide links" style="background-color: #4180C5">		
	<input name="servoCW" id="servoCW" type="submit" value="Pyramide rechts" style="background-color: #4180C5">		
	<input name="running" id="running" type="submit" value="Lauflicht" style="background-color: #4180C5">
	<input name="blinking" id="blinking" type="submit" value="Blinken" style="background-color: #4180C5">
</form>
</div>
</body>
</html>
