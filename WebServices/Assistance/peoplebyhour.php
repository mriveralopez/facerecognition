<?php
require_once('../Connection.php');

$db = Db::getConnect();

$listRespuesta = array();
$time = array();

$date = $_GET['date'];

if($date == ""){
    $date = "2019-09-02";
}

for ($i = 0; $i < 24; $i++) {
    $select = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime BETWEEN :init AND :end AND Status = "IN";');
    $select2 = $db->prepare('SELECT COUNT(*) FROM Assistance WHERE DateTime BETWEEN :init AND :end AND Status = "OUT";');

    if(strlen($i) == 1){
        $init = " 0$i:00:00";
    } else {
        $init = " $i:00:00";
    }
    $e = $i + 1;
    if(strlen($e) == 1){
        $end = " 0$e:00:00";
    } else {
        $end = " $e:00:00";
    }
    $select->bindValue('init', $date.$init, PDO::PARAM_STR);
    $select->bindValue('end', $date.$end, PDO::PARAM_STR);

    $select2->bindValue('init', $date.$init, PDO::PARAM_STR);
    $select2->bindValue('end', $date.$end, PDO::PARAM_STR);

    // echo $date.$init."<BR>";
    // echo $date.$end."<BR>";

    $select->execute();

    foreach($select->fetchAll() as $DBSelect) {
        $listRespuesta[] = $DBSelect;
    }
    
    $select2->execute();

    foreach($select2->fetchAll() as $DBSelect) {
        $listRespuesta2[] = $DBSelect;
    }
    $time[] = $date.$init;
}

// echo json_encode($listRespuesta);
// echo "<BR>";
// echo json_encode($time);
?>