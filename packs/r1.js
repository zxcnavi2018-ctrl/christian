const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();
const jobs=JSON.parse(process.argv[2]);for(const [i,o] of jobs){await p.goto('file://'+i);await p.pdf({path:o,format:'A4',printBackground:true,preferCSSPageSize:true});}await b.close()})();
