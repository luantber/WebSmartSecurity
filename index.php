<?php 

function explorar($dir){
	$fotos = scandir($dir,1);
	array_pop($fotos);
	array_pop($fotos);
	return $fotos;
}

$cfotos = explorar("fotos");

$respuesta = array();

foreach ( $cfotos as $carpeta) {
	$cactual = explorar("fotos/".$carpeta);
	$tmp = array($carpeta);
	foreach ($cactual as $foto) {
		array_push($tmp, "fotos/".$carpeta."/".$foto);
	}
	array_push($respuesta,$tmp);
}

echo "<script> var data = ";
print_r(json_encode($respuesta));
echo ";</script>";

include_once("fotos.html");
?>