<?php
	$output = shell_exec('python deploy.py');
	echo "<pre>$output</pre>";
?>