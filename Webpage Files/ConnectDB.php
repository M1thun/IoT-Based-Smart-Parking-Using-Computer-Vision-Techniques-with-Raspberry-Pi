<html>
<body>

<?php
	$MyUsername = "mithun";  // enter your username for mysql
	$MyPassword = "mithun";  // enter your password for mysql
	$MyHostname = "localhost";      // this is usually "localhost" unless your database resides on a different server

	$dbh = mysqli_connect($MyHostname , $MyUsername, $MyPassword);
	$selected = mysqli_select_db($dbh,"slots"); //Enter your database name here 

	$sql = "INSERT INTO slots.slots (slot1) VALUES ('".$_GET["temp"]."')";
    mysqli_query($dbh, $sql)
    


?>
</body>
</html>