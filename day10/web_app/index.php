<!DOCTYPE html>
<html>
<head>
	<title>Conrad Raspberry Pi Advent calendar</title>

	<link rel="stylesheet" type="text/css" href="css/general-styles.css">
	<link rel="stylesheet" media="screen and (max-width: 1200px) and (min-width: 601px)" href="css/styles_1200px.css" />
	<link rel="stylesheet" media="screen and (max-width: 600px) and (min-width: 351px)" href="css/styles_600px.css" />
	<link rel="stylesheet" media="screen and (max-width: 350px)" href="css/styles_350px.css" />

	<?php
		if ($_POST['up']) {
			echo exec('python /var/www/html/day10/pwm_up.py');
		}
		elseif ($_POST['down']) {
			echo exec('python /var/www/html/day10/pwm_down.py');
		}
	?>

</head>
<body>
        <div id="envelope">
                <header>
                    <h2>Conrad Raspberry Pi Advent calendar</h2>
                </header>
                <hr>

                <form action="index.php" method="post">
					<input type="submit" name="up" value="Brighten" id="up">
					<input type="submit" name="down" value="Dim" id="down">
                </form>
        </div>
</body>
</html>
