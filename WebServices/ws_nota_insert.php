<?php
require_once('Connection.php');

$db = Db::getConnect();

$listHorario = array();

$resultado = array('resultado' => 0);

$codmateria = $_GET['codmateria'];
$carnet = $_GET['carnet'];
$ciclo = $_GET['ciclo'];
$notafinal = $_GET['notafinal'];

$insert = $db->prepare('INSERT INTO NOTA VALUES(:codmateria, :carnet, :ciclo, :notafinal);');

$insert->bindValue('codmateria', $codmateria, PDO::PARAM_STR);
$insert->bindValue('carnet', $carnet, PDO::PARAM_STR);
$insert->bindValue('ciclo', $ciclo, PDO::PARAM_STR);
$insert->bindValue('notafinal', $notafinal, PDO::PARAM_STR);

if ($insert->execute()) {
    $resultado = array('resultado' => 1);
}

echo json_encode($resultado);
?>