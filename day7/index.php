<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <?php
            if ($_POST['light_on']) {
                echo shell_exec('sudo $(PWD)/webLedSwitch.py');
            }
         ?>
        <title>Conrad Raspberry Pi Advent calendar</title>
        <link rel="stylesheet" href="/css/general_styles.css">
        <link rel="stylesheet" media="screen and (max-width: 1200px) and (min-width: 601px)" href="/css/styles_1200px.css">
        <link rel="stylesheet" media="screen and (max-width: 600px) and (min-width: 351px)" href="/css/styles_600px.css">
        <link rel="stylesheet" media="screen and (max-width: 350px)" href="/css/styles_350px.css">
    </head>
<body>
<div id="envelope">
    <header>
        <h2>Conrad Raspberry Pi Adventskalender</h2>
    </header>
    <hr>
    <form action="index.php" method="post">
    </form>
</div>
</body>
</html>
