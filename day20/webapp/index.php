<!DOCTYPE html> 
<html>

	<!-- Vorlage für die mobile App für den Conrad Raspberry Pi Adventskalender -->

<head>
	
	<?php
		if ($_POST["servo_links"]) {
			echo exec('python /var/www/html/tag20/20servo_li.py');
		} elseif ($_POST["servo_rechts"]) {
			echo exec('python /var/www/html/tag20/20servo_re.py');			
		} elseif ($_POST["lauflicht"]) {
			echo exec('python /var/www/html/tag20/20pyramide_lauflicht.py');			
		} elseif ($_POST["blinken"]) {
			echo exec('python /var/www/html/tag20/20pyramide_blink.py');			
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
	<input name="servo_links" id="servo_links" type="submit" value="Pyramide links" style="background-color: #4180C5">		
	<input name="servo_rechts" id="servo_rechts" type="submit" value="Pyramide rechts" style="background-color: #4180C5">		
	<input name="lauflicht" id="lauflicht" type="submit" value="Lauflicht" style="background-color: #4180C5">
	<input name="blinken" id="blinken" type="submit" value="Blinken" style="background-color: #4180C5">
</form>
</div>
</body>
</html>
