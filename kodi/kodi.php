<html>
<body>

<?php $pause = $_GET["pause"]; ?>
<?php $stop = $_GET["stop"]; ?>
<?php $channel = $_GET["channel"]; ?>

Pause is <?php echo $pause; ?><br>
Stop is <?php echo $stop; ?><br>
Channel is <?php echo $channel; ?><br>

<?php

if ($pause) {
  exec("kodi -p " . escapeshellarg($pause));
}

?>

<?php

if ($stop) {
  exec("kodi -s " . escapeshellarg($stop));
}

?>

<?php

if ($channel) {
  exec("kodi -c " . escapeshellarg($channel));
}

?>


</body>
</html>
