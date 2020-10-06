<?php
   
	$MyUsername = "mithun";  // enter your username for mysql
	$MyPassword = "mithun";  // enter your password for mysql
	$MyHostname = "localhost";      // this is usually "localhost" unless your database resides on a different server

	$dbh = mysqli_connect($MyHostname , $MyUsername, $MyPassword);
	$selected = mysqli_select_db($dbh,"slots"); //Enter your database name here 


    $data = mysqli_query($dbh, "SELECT slot1 FROM slots  ORDER BY Date DESC LIMIT 1");
	$sql2 = "DELETE FROM slots;";
	mysqli_query($dbh,$sql2);
	
	
	// output data of each row
	$row = mysqli_fetch_array($data);	
	mysqli_close($dbh);
	echo $row["slot1"];
	
?>
