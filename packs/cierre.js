// Genera la hoja de cierre (flipped para la siguiente sesión + Exit ticket con su tarjeta)
// de cada sesión de las Unidades 7 y 8 con la misma función de la app.
// Uso: servir la carpeta del repo en http://localhost:8765 y luego: node packs/cierre.js <carpeta-salida>
const {chromium}=require('playwright');const fs=require('fs');const OUT=process.argv[2];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage();p.on('dialog',d=>d.accept());
await p.addInitScript(()=>{localStorage.setItem('ciencia4b:me:1ba4092d0e',JSON.stringify({key:'k0aaaaaaaaaaaaaaaaaaa',dni:'11111111',name:'Docente',section:'DOC',rid:'x',teacher:true,createdAt:1}));localStorage.setItem('ciencia4b:auth:1ba4092d0e',JSON.stringify({email:'t@x.com',idToken:'x',refreshToken:'x',exp:Date.now()+36e5}))});
await p.route('**/firestore.googleapis.com/**',r=>r.fulfill({status:404,json:{}}));
await p.route('**/cdn.jsdelivr.net/**',r=>{const u=r.request().url();if(u.includes('pdf-lib.min.js')&&process.env.PDFLIB)return r.fulfill({body:fs.readFileSync(process.env.PDFLIB),contentType:'application/javascript'});return r.continue()});
await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(1800);
await p.evaluate(()=>[...document.querySelectorAll('button')].find(b=>b.textContent.trim()==='Panel')?.click());await p.waitForTimeout(600);
for(const n of [7,8]){await p.evaluate(n=>document.querySelector(`[data-tk="h-uimp"][data-n="${n}"]`).click(),n);await p.waitForTimeout(2500);
 const N=await p.evaluate(n=>APP.units.find(u=>u.key==='unit'+n).sessions.length,n);
 for(let i=1;i<=N;i++){const b64=await p.evaluate(([n,i])=>window.__moli.closePDF('unit'+n,i),[n,i]);fs.writeFileSync(`${OUT}/cierre-u${n}-s${i}.pdf`,Buffer.from(b64,'base64'))}
 console.log('Unidad',n,':',N,'hojas de cierre')}
await b.close()})();
