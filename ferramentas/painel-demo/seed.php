<?php
mt_srand(42);
$d=new PDO('mysql:host=127.0.0.1;dbname=evolua_demo;charset=utf8mb4','demo','demo',[PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION]);
foreach(["ALTER TABLE sales ADD COLUMN waiter_fee DECIMAL(12,2) NOT NULL DEFAULT 0","ALTER TABLE devices ADD COLUMN battery_charging TINYINT NULL",
 "CREATE TABLE IF NOT EXISTS cash_withdrawals (id VARCHAR(64) PRIMARY KEY,cash_id VARCHAR(64) NOT NULL,amount DECIMAL(12,2) NOT NULL DEFAULT 0,note VARCHAR(255) NULL,created_at BIGINT NOT NULL)"] as $q){try{$d->exec($q);}catch(Throwable $e){}}
foreach(['sale_items','sales','cash_sessions','devices','products','product_categories','product_images','cash_withdrawals'] as $t)$d->exec("DELETE FROM $t");
$ev='EV-FESTA';$cli='CLI-DEMO';$now=time();
$photos=$argv[1];
$cats=[['CAT-BEB','Bebidas','#2b8cff'],['CAT-LAN','Lanches','#f59e0b'],['CAT-DOC','Doces','#ec4899']];
foreach($cats as $i=>[$id,$n,$c])$d->prepare('INSERT INTO product_categories(id,event_id,name,color,sort_order,active,created_at) VALUES(?,?,?,?,?,1,?)')->execute([$id,$ev,$n,$c,$i,$now]);
$prods=[ // id, nome, preço, categoria, foto, peso de venda
['P-AGUA','Água',5,'CAT-BEB','agua-crystal',14],['P-SKOL','Cerveja Skol',8,'CAT-BEB','cerveja-skol',30],['P-BRAH','Cerveja Brahma',8,'CAT-BEB','cerveja-brahma',22],
['P-HEIN','Cerveja Heineken',12,'CAT-BEB','cerveja-heineken',18],['P-GUAR','Guaraná lata',6,'CAT-BEB','lata-guarana',12],['P-PEPS','Pepsi lata',6,'CAT-BEB','lata-pepsi',8],
['P-BALD','Balde 5 cervejas',55,'CAT-BEB','balde-cerveja',4],['P-VODK','Dose de vodka',15,'CAT-BEB','vodka-smirnoff',5],
['P-XSAL','X-Salada',24,'CAT-LAN','hamburguer-salada',9],['P-XBAC','X-Bacon BBQ',28,'CAT-LAN','hamburguer-bacon-barbecue',7],['P-DUPL','Duplo Bacon',34,'CAT-LAN','hamburguer-duplo-bacon',4],
['P-HOTD','Cachorro-quente',12,'CAT-LAN','cachorro-quente',13],['P-FRIT','Batata frita',15,'CAT-LAN','batata-frita',10],['P-PIPO','Pipoca',8,'CAT-LAN','pipoca',7],
['P-CHUR','Churros',10,'CAT-DOC','churros-chocolate',8],['P-CREP','Crepe',14,'CAT-DOC','crepe',5],['P-MACA','Maçã do amor',8,'CAT-DOC','maca-do-amor',4],['P-MORA','Morango no palito',9,'CAT-DOC','morango-chocolate',4]];
foreach($prods as [$id,$n,$p,$c,$f,$w]){
 $d->prepare('INSERT INTO products(id,event_id,name,price,stock,track_stock,active,updated_at,category_id) VALUES(?,?,?,?,0,0,1,?,?)')->execute([$id,$ev,$n,$p,$now,$c]);
 $file="$photos/$f.jpg"; if(is_file($file))$d->prepare('INSERT INTO product_images(product_id,mime,data,updated_at) VALUES(?,?,?,?)')->execute([$id,'image/jpeg',file_get_contents($file),$now]);
}
$devs=[ // nome, serial, bateria, carregando, online?, operador
['Bar Central 01','MS2-4471',86,0,1,'Carla'],['Bar Central 02','MS2-4472',64,0,1,'Diego'],['Lanchonete','STN-2210',41,1,1,'Marcos'],
['Doces e Churros','LIO-8831',18,0,1,'Patrícia'],['Entrada / Bilheteria','MS2-4475',92,1,1,'Juliana'],['Barraca 2','AND-1190',57,0,0,'Rafael']];
$weights=[];foreach($prods as $i=>$p)for($k=0;$k<$p[5];$k++)$weights[]=$i;
$pays=array_merge(array_fill(0,46,'PIX'),array_fill(0,24,'CREDITO'),array_fill(0,18,'DEBITO'),array_fill(0,12,'DINHEIRO'));
$order=1000;
foreach($devs as $i=>[$name,$serial,$bat,$chg,$on,$op]){
 $did='DEV-'.($i+1);$seen=$on?$now-mt_rand(5,60):$now-3600;
 $d->prepare('INSERT INTO devices(id,client_id,license_id,device_key,serial_number,device_name,current_event_id,token,active,first_seen_at,last_seen_at,battery,battery_charging) VALUES(?,?,?,?,?,?,?,?,1,?,?,?,?)')
   ->execute([$did,$cli,'LIC-1','key-'.$did,$serial,$name,$ev,bin2hex(random_bytes(16)),$now-86400,$seen,$bat,$chg]);
 $sid='CASH-'.($i+1);$opened=$now-mt_rand(4*3600,5*3600);
 $d->prepare('INSERT INTO cash_sessions(id,event_id,user_id,cashier_id,opening,opened_at,status,device_id,client_id,operator_name) VALUES(?,?,?,?,?,?,?,?,?,?)')->execute([$sid,$ev,'',"",100,$opened,'OPEN',$did,$cli,$op]);
 $n=mt_rand(70,140);
 for($s=0;$s<$n;$s++){
  $t=$opened+(int)(($now-$opened)*($s+mt_rand(0,90)/100)/$n);
  $lines=[];$tot=0;$k=mt_rand(1,3);
  for($j=0;$j<$k;$j++){$pi=$weights[mt_rand(0,count($weights)-1)];$q=mt_rand(1,3)==1?2:1;$lines[$pi]=($lines[$pi]??0)+$q;}
  $saleId='S-'.$did.'-'.$s;$items=[];
  foreach($lines as $pi=>$q){$p=$prods[$pi];$tot+=$p[2]*$q;$items[]=['product_id'=>$p[0],'name'=>$p[1],'qty'=>$q,'unit_price'=>$p[2]];}
  $pay=$pays[mt_rand(0,count($pays)-1)];
  $d->prepare('INSERT INTO sales(id,event_id,order_no,user_id,cashier_id,session_id,payment,total,items_json,created_at,synced_at,device_id,client_id,waiter_fee) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,0)')
    ->execute([$saleId,$ev,++$order,'','',$sid,$pay,$tot,json_encode($items,JSON_UNESCAPED_UNICODE),$t,$t+3,$did,$cli]);
  foreach($items as $it)$d->prepare('INSERT INTO sale_items(sale_id,product_id,name,qty,unit_price,addons_json) VALUES(?,?,?,?,?,?)')->execute([$saleId,$it['product_id'],$it['name'],$it['qty'],$it['unit_price'],'[]']);
 }
}
$d->prepare("REPLACE INTO event_settings(event_id,config_json,updated_at) VALUES(?,?,?)")->execute([$ev,json_encode(['sangria'=>['enabled'=>true,'required_amount'=>800]]),$now]);
echo "ok ".$d->query('SELECT COUNT(*) FROM sales')->fetchColumn()." vendas, R$ ".$d->query('SELECT SUM(total) FROM sales')->fetchColumn()."\n";
