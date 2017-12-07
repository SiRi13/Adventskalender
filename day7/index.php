<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Conrad Raspberry Pi Advent calendar</title>

    <link rel="stylesheet" type="text/css" href="css/general_styles.css">
    <link rel="stylesheet" media="screen and (max-width: 1200px) and (min-width: 601px)" type="text/css" href="css/general-styles.css">
    <link rel="stylesheet" media="screen and (max-width: 600px) and (min-width: 351px)" type="text/css" href="css/styles_600px.css">
    <link rel="stylesheet" media="screen and (max-width: 350px)" type="text/css" href="css/styles_350px.css">

    <?php
        if ($_POST['light_on']) {
            echo shell_exec('sudo /var/www/html/day7/webLedSwitch.py');
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
            <input type="submit" name="light_on" value="Light On" id="light_on">
        </form>
    </div>
</body>
</html>
