<html>
<body>

<?php $quick = $_GET["quick"]; ?>
<?php $tv = $_GET["tv"]; ?>
<?php $up = $_GET["up"]; ?>
<?php $down = $_GET["down"]; ?>
<?php $mute = $_GET["mute"]; ?>

Quick Select is <?php echo $quick; ?><br>
TV is <?php echo $tv; ?><br>
Up is <?php echo $up; ?><br>
Down is <?php echo $down; ?><br>
Mute is <?php echo $mute; ?><br>

<?php

if ($quick) {
  exec("denon -q" . escapeshellarg($quick));
}

?>

<?php

if ($tv) {
  exec("denon -t" . escapeshellarg($tv));
}

?>


<?php

if ($up) {
  exec("denon -u" . escapeshellarg($up));
}

?>

<?php

if ($down) {
  exec("denon -d" . escapeshellarg($down));
}

?>

<?php

if ($mute) {
  exec("denon -m" . escapeshellarg($mute));
}

?>


</body>
</html>
