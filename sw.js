// Guarda Moli en el celular: abre rápido y también sin internet.
// Solo la página principal sale de la caja guardada; el laboratorio y las guías siempre vienen de internet.
const V="moli-6395a4e79c-w",APPJS="app.js?v=db75100b2f",CDN="moli-cdn";
self.addEventListener("install",e=>{self.skipWaiting(),e.waitUntil(caches.open(V).then(c=>c.addAll(["./",APPJS])).catch(()=>{}))});
self.addEventListener("activate",e=>e.waitUntil((async()=>{for(const k of await caches.keys())k!==V&&k!==CDN&&await caches.delete(k);await self.clients.claim()})()));
const put=async(n,r,s)=>{try{await(await caches.open(n)).put(r,s)}catch(e){}};
self.addEventListener("fetch",e=>{const r=e.request;if("GET"!==r.method)return;const u=new URL(r.url);
if(u.origin===location.origin){
if("navigate"===r.mode){const h=new URL("./",self.registration.scope).pathname;if(u.pathname!==h&&u.pathname!==h+"index.html")return}
if("navigate"===r.mode)return void e.respondWith((async()=>{const o=await caches.match("./",{cacheName:V}),n=fetch(r).then(s=>(s.ok&&put(V,"./",s.clone()),s));return o?Promise.race([n.catch(()=>o),new Promise(t=>setTimeout(()=>t(o),2500))]):n})());
/\/(app\.js|img\/(moli\/[\w-]+\.webp|fonts\/[\w-]+\.woff2))$/.test(u.pathname)&&e.respondWith((async()=>await caches.match(r)||fetch(r).then(s=>(s.ok&&put(V,r,s.clone()),s)))());return}
(/^(cdn\.jsdelivr\.net|cdnjs\.cloudflare\.com|fonts\.gstatic\.com|fonts\.googleapis\.com)$/.test(u.host)||"www.gstatic.com"===u.host&&/^\/firebasejs\//.test(u.pathname))&&e.respondWith((async()=>await caches.match(r)||fetch(r).then(s=>((s.ok||"opaque"===s.type)&&put(CDN,r,s.clone()),s)))())});
