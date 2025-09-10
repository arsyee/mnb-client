<?php
$client = new SoapClient("http://www.mnb.hu/arfolyamok.asmx?wsdl");
// ***************************************************************
// Az összes elérhető fv lekrérdezése.
//var_dump($client >__getFunctions());
// ***************************************************************
// Pénznemek lekérdezése
print($client->GetCurrencies()->GetCurrenciesResult . "\n");
// ***************************************************************
// Aktuális árfolyamok lekérdezése.
print($client->GetCurrentExchangeRates()->GetCurrentExchangeRatesResult . "\n");
?>
