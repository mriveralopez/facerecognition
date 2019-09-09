<?php
class Db
{
	private static $instance = NULL;

	function __construct() {}

	public static function getConnect() {
		// try{
		if (!isset(self::$instance)) {
			$pdo_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;
			self::$instance = new PDO('mysql:host=localhost:3306;dbname=face_recognition', 'face_recognition', 'face_recognition', $pdo_options);
		}
		return self::$instance;
		// } catch (){
			
		// }
	}
}

// $db = Db::getConnect();
?>
