<?php
require_once('../Connection.php');

$db = Db::getConnect();

$listRespuesta = array();
$listRespuesta2 = array();
$listRespuesta3 = array();
$listRespuesta4 = array();

$date = $_GET['datein'];
$dateout = $_GET['dateout'];

if($datein == ""){
    $datein = "2019-09-02";
}

if($dateout == ""){
    $dateout = "2019-09-02";
}

$select = $db->prepare('SELECT e.LastName, e.Name, a.DateTime, a.Status FROM Assistance a INNER JOIN Employee e ON a.Employee = e.Code WHERE a.DateTime BETWEEN :datein AND :dateout;');

$select->bindValue('datein', $datein." 00:00:00", PDO::PARAM_STR);
$select->bindValue('dateout', $dateout." 23:59:59".$timein, PDO::PARAM_STR);

$select->execute();

foreach($select->fetchAll() as $DBSelect) {
    $listRespuesta[] = $DBSelect;
}

// echo json_encode($listRespuesta);
// print($datein);
// print($dateout);
?>