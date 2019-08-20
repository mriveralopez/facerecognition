<?php
require_once('Connection.php');

$db = Db::getConnect();

$resultado = array('resultado' => 0);

$codmateria = $_GET['codmateria']; 
$carnet = $_GET['carnet']; 
$ciclo = $_GET['ciclo']; 
$notafinal = $_GET['notafinal'];

$update = $db->prepare('UPDATE NOTA SET notafinal = :notafinal WHERE carnet = :carnet AND codmateria = :codmateria AND ciclo = :$ciclo;');

$update->bindValue('codmateria', $codmateria, PDO::PARAM_STR);
$update->bindValue('carnet', $carnet, PDO::PARAM_STR);
$update->bindValue('ciclo', $ciclo, PDO::PARAM_STR);
$update->bindValue('notafinal', $notafinal, PDO::PARAM_STR);

if($update->execute()) {
    $resultado = array('resultado' => 1);
}

echo json_encode($resultado);
?>