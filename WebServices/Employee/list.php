<?php
require_once('../Connection.php');

$db = Db::getConnect();

$listRespuesta = array();

$name = $_GET['name'];
$lastname = $_GET['lastname'];
$code = $_GET['code'];

$select = $db->prepare('SELECT name, lastname, code FROM employee');

$select->execute();

foreach($select->fetchAll() as $DBSelect) {
  $listRespuesta[] = $DBSelect;
}

echo json_encode($listRespuesta);
?>