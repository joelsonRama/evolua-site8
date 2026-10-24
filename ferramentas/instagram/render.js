const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1080,height:1350}});
 for (let i=1;i<=30;i++){ const n=String(i).padStart(2,'0'); await p.goto('file://'+process.argv[2]+'/p'+n+'.html'); await p.waitForTimeout(i==1?1500:500); await p.screenshot({path:process.argv[2]+'/out/post-'+n+'.png'}); }
 await b.close(); })();
