// Moli guarda su mensaje: al llegar uno nuevo muestra 💬 y al tocar a Moli se abre o se cierra.
(()=>{const box=document.querySelector('.moli-say');if(!box)return;const p=box.querySelector('p'),img=box.querySelector('img');let t=0,last='';
const open=v=>{box.classList.toggle('open',v);box.classList.remove('new');clearTimeout(t);if(v)t=setTimeout(()=>box.classList.remove('open'),9000)};
img.setAttribute('role','button');img.setAttribute('tabindex','0');img.setAttribute('aria-label','Ver lo que dice Moli');
img.addEventListener('click',()=>open(!box.classList.contains('open')));img.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' ')open(!box.classList.contains('open'))});
p.addEventListener('click',e=>{if(!e.target.closest('button'))open(false)});
new MutationObserver(()=>{const s=p.textContent.trim();if(!s||s===last)return;last=s;if(box.classList.contains('open'))open(true);else box.classList.add('new')}).observe(p,{childList:true,subtree:true,characterData:true});
if(p.textContent.trim()){last=p.textContent.trim();box.classList.add('new')}})();
