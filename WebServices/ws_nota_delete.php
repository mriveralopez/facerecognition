<?php
require_once('Connection.php');

$db = Db::getConnect();

$listHorario = array();

$codmateria=$_REQUEST['codmateria']; 
$carnet=$_REQUEST['carnet']; 
$ciclo=$_REQUEST['ciclo'];

$resultado = array('resultado' => 0);

$select = $db->prepare('DELETE FROM NOTA WHERE carnet = :carnet AND codmateria = :codmateria AND ciclo = :ciclo;');

$select->bindValue('codmateria', $codmateria, PDO::PARAM_STR);
$select->bindValue('carnet', $carnet, PDO::PARAM_STR);
$select->bindValue('ciclo', $ciclo, PDO::PARAM_STR);

if($select->execute()) {
    $resultado = array('resultado' => 1);
}

echo json_encode($resultado);
?>