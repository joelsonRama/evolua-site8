<?php
mt_srand(7);
$d=new PDO('mysql:host=127.0.0.1;dbname=evolua_demo;charset=utf8mb4','demo','demo',[PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION]);
date_default_timezone_set('America/Sao_Paulo');
$d->exec("DELETE FROM sales WHERE id LIKE 'H-%'"); $d->exec("DELETE FROM events WHERE id LIKE 'EV-H%'"); $d->exec("DELETE FROM client_events WHERE event_id LIKE 'EV-H%'");
$evs=[['EV-H1','Carnaval de Rua 2026','2026-02-14',14200],['EV-H2','Festa de Páscoa','2026-04-04',6100],['EV-H3','Arraiá São João','2026-06-20',16800],
      ['EV-H4','Rodeio da Cidade','2026-08-15',21400],['EV-H5','Festa da Primavera','2026-09-19',9300],['EV-H6','Show de Verão','2026-01-24',7800],
      ['EV-H7','Feira Gastronômica','2026-05-16',8900],['EV-H8','Festival de Inverno','2026-07-11',11200]];
foreach($evs as [$id,$n,$day,$tot]){
 $t=strtotime($day.' 20:00');
 $d->prepare('INSERT INTO events(id,name,start_at,end_at,status,active,created_at) VALUES(?,?,?,?,?,1,?)')->execute([$id,$n,$t,$t+6*3600,'CLOSED',$t]);
 $d->prepare('INSERT INTO client_events(client_id,event_id,active) VALUES(?,?,1)')->execute(['CLI-DEMO',$id]);
 $left=$tot;$k=0;
 while($left>0){$v=min($left,mt_rand(20,60));$left-=$v;$k++;
  $d->prepare("INSERT INTO sales(id,event_id,order_no,user_id,cashier_id,session_id,payment,total,items_json,created_at,synced_at,device_id,client_id,waiter_fee) VALUES(?,?,?,'','','',?,?,'[]',?,?,'DEV-1','CLI-DEMO',0)")
   ->execute(["H-$id-$k",$id,$k,['PIX','CREDITO','DEBITO','DINHEIRO'][mt_rand(0,3)],$v,$t+mt_rand(0,6*3600),$t]);}
}
echo "ok\n";
