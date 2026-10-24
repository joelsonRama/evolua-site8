const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1080,height:1920}});
 const fs=require('fs'); const d=process.argv[2]; let first=true;
 for (const f of fs.readdirSync(d).filter(f=>/^(s\d-\d|capa\d)\.html$/.test(f)).sort()) {
   await p.goto('file://'+d+'/'+f); await p.waitForTimeout(first?1500:450); first=false;
   await p.screenshot({path:d+'/sout/'+f.replace('.html','.png')}); }
 await b.close(); })();
