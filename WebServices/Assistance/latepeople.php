<?php
require_once('../Connection.php');

$db = Db::getConnect();

$listRespuesta = array();
$listRespuesta2 = array();
$listRespuesta3 = array();
$listRespuesta4 = array();

$date = $_GET['date'];
$timein = $_GET['timein'];
$timeout = $_GET['timeout'];

if($date == ""){
    $date = "2019-09-02";
}

if($timein == "") {
    $timein = "09:00:00";
}

if($timeout == "") {
    $timeout = "17:00:00";
}

$select = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime LIKE :date AND DateTime < :datetime AND Status = "IN";');

$select->bindValue('date', $date."%", PDO::PARAM_STR);
$select->bindValue('datetime', $date." ".$timein, PDO::PARAM_STR);

$select->execute();

foreach($select->fetchAll() as $DBSelect) {
    $listRespuesta[] = $DBSelect;
}

$select2 = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime LIKE :date AND DateTime > :datetime AND Status = "IN";');

$select2->bindValue('date', $date."%", PDO::PARAM_STR);
$select2->bindValue('datetime', $date." ".$timein, PDO::PARAM_STR);

$select2->execute();

foreach($select2->fetchAll() as $DBSelect) {
    $listRespuesta2[] = $DBSelect;
}

$select3 = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime LIKE :date AND DateTime < :datetime AND Status = "OUT";');

$select3->bindValue('date', $date."%", PDO::PARAM_STR);
$select3->bindValue('datetime', $date." ".$timeout, PDO::PARAM_STR);

$select3->execute();

foreach($select3->fetchAll() as $DBSelect) {
    $listRespuesta3[] = $DBSelect;
}

$select4 = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime LIKE :date AND DateTime > :datetime AND Status = "OUT";');

$select4->bindValue('date', $date."%", PDO::PARAM_STR);
$select4->bindValue('datetime', $date." ".$timeout, PDO::PARAM_STR);

$select4->execute();

foreach($select4->fetchAll() as $DBSelect) {
    $listRespuesta4[] = $DBSelect;
}

$select5 = $db->prepare('SELECT Status, COUNT(*) FROM Assistance WHERE DateTime LIKE :date GROUP BY Status;');

$select5->bindValue('date', $date."%", PDO::PARAM_STR);

$select5->execute();

foreach($select5->fetchAll() as $DBSelect) {
    $listRespuesta5[] = $DBSelect;
    if($DBSelect[0] = 'IN') {
        $countin = $DBSelect[1];
    }
    if($DBSelect[0] = 'OUT') {
        $countout = $DBSelect[1];
    }
}

// echo json_encode($listRespuesta);
// echo json_encode($listRespuesta2);
// echo json_encode($listRespuesta3);
// echo json_encode($listRespuesta4);
// echo json_encode($listRespuesta5);
// echo "<BR>";

// print($date);
// print($timein);
// print($timeout);
?>