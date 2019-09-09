<?php
require_once('../Connection.php');

$db = Db::getConnect();

$listRespuesta = array();

$code = $_REQUEST['code'];
$status = $_REQUEST['status'];

$select = $db->prepare('SELECT idAssistance, Employee, DateTime, Status FROM Assistance WHERE Employee = :code AND DateTime like CONCAT(CURDATE(), "%") ORDER BY DateTime DESC LIMIT 1;');

$select->bindValue('code', $code, PDO::PARAM_STR);

$select->execute();

foreach($select->fetchAll() as $DBSelect) {
  $listRespuesta[] = $DBSelect;
}

$resultado = array('resultado' => 0);

if (empty($listRespuesta)){
  $insert = $db->prepare('INSERT INTO Assistance(Employee, DateTime, Status) VALUES(:code, NOW(), :status);');

  $insert->bindValue('code', $code, PDO::PARAM_STR);
  $insert->bindValue('status', $status, PDO::PARAM_STR);

  if ($insert->execute()) {
      $resultado = array('resultado' => 1);
  }
} else {
  if($listRespuesta[0][3] != $status){
    $insert = $db->prepare('INSERT INTO Assistance(Employee, DateTime, Status) VALUES(:code, NOW(), :status);');

    $insert->bindValue('code', $code, PDO::PARAM_STR);
    $insert->bindValue('status', $status, PDO::PARAM_STR);

    if ($insert->execute()) {
        $resultado = array('resultado' => 1);
    }
  }
}

echo json_encode($resultado);
?>