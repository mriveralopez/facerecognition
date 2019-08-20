<?php
require_once('Connection.php');

$db = Db::getConnect();

$listRespuesta = array();

$codmateria = $_GET['codmateria'];
$carnet = $_GET['carnet'];
$ciclo = $_GET['ciclo'];

$select = $db->prepare('SELECT * FROM employee');

$select->bindValue('code', $codmateria, PDO::PARAM_STR);
$select->bindValue('carnet', $carnet, PDO::PARAM_STR);
$select->bindValue('ciclo', $ciclo, PDO::PARAM_STR);

$select->execute();

foreach($select->fetchAll() as $DBSelect) {
  $listRespuesta[] = $DBSelect;
}

echo json_encode($listRespuesta);
?>