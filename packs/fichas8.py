import json,html,re
OUT='/home/user/christian/packs/u8/'
import os;os.makedirs(OUT,exist_ok=True)
def e(x):return html.escape(x)
def lines(n=2):return '<div class="ln"></div>'*n
def table(head,rows,n=None,cls=""):
    h=''.join(f'<th>{e(x)}</th>' for x in head)
    body=''
    for r in rows:
        body+='<tr>'+''.join(f'<td>{c}</td>' for c in (r+['']*(len(head)-len(r))))+'</tr>'
    if n:
        for _ in range(n):body+='<tr class="bk">'+'<td>&nbsp;</td>'*len(head)+'</tr>'
    if len(head)==2 and not cls:cls="kv"
    if len(head)>=5 and cls!="chk":cls+=" wide"
    elif len(head) in (3,4) and not cls:cls="mid"
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'
def check(title,items,cols=("Sí","Debo mejorar")):
    return table([title]+list(cols),[[e(i)]+['☐']*len(cols) for i in items],cls="chk")
def scaf(t):return f'<div class="scaf"><b>Andamio:</b> {t}</div>'
def tip(t):return f'<div class="tip"><b>Recuerda:</b> {t}</div>'
def dua():return '<div class="dua"><b>🎨 ¿Cómo lo presentamos?</b> Elijan el formato que más les guste: afiche · cómic · organizador visual · maqueta · dramatización · audio o video corto · canción o rima · exposición con objetos · ¡otra idea!</div>'
def informe(part,body):return f'<div class="inf"><b>Para mi póster · {e(part)}</b>{body}</div>'
def act(n,mode,title,body):
    lab={"i":"👤 Individual","g":"👥 En grupo"}[mode]
    return f'<section class="act {mode}"><div class="ah"><span class="an">Actividad {n}</span><span class="am">{lab}</span></div><h2>{title}</h2>{body}</section>'
def feedback(kind):
    if kind=="estrella":return table(["⭐ Una estrella: algo que logramos","🪜 Una escalera: algo que podemos mejorar"],[],1)
    if kind=="vps":return table(["👀 Veo","❓ Pregunto","💡 Sugiero"],[],1)
    if kind=="semaforo":return table(["Criterio","Verde","Amarillo","Rojo"],[],0)
def page(num,title,meta,crit,acts,extra=""):
    cr=''.join(f'<li>☐ {e(c)}</li>' for c in crit)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:12mm 12mm 14mm}}
*{{box-sizing:border-box}}body{{font-family:"DejaVu Sans",Arial,sans-serif;font-size:10.5pt;color:#000;margin:0;background:#fff}}
.hd{{display:flex;align-items:center;gap:12px;border-bottom:1px solid #000;padding:0 0 8px}}
.hd .n{{border:1px solid #000;border-radius:10px;padding:5px 11px;font-weight:600;font-size:18pt;text-align:center;line-height:1}}
.hd .n small{{display:block;font-size:7pt;letter-spacing:.08em}}
.hd h1{{margin:0;font-size:15pt;font-weight:700}}.hd p{{margin:2px 0 0;font-size:8.5pt}}
.xname{{display:flex;gap:10px;margin:8px 0;font-size:9pt}}.name span{{flex:1;border-bottom:1.3px solid #000;padding-bottom:2px}}
.xmeta{{border:1.5px solid #000;border-radius:12px;padding:7px 12px;margin:6px 0}}
.meta ul{{list-style:none;padding:0;margin:4px 0 0;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:9pt}}
.act{{border:1px solid #000;border-radius:14px;padding:8px 12px 10px;margin:10px 0;break-inside:auto}}

.ah{{display:flex;gap:8px;align-items:center}}.an{{font-weight:400;font-size:8pt;letter-spacing:.08em;text-transform:uppercase}}
.am{{font-size:8pt;font-weight:400}}
h2{{margin:3px 0 6px;font-size:12.5pt;font-weight:600}}h3{{font-size:10.5pt;margin:8px 0 4px;font-weight:600}}b{{font-weight:400}}
p{{margin:4px 0}}.ln{{border-bottom:.8px dotted #000;height:34px}}
table{{width:100%;border-collapse:collapse;margin:5px 0;font-size:9.2pt;break-inside:auto}}tr{{break-inside:avoid;page-break-inside:avoid}}thead{{display:table-header-group}}h2,.ah{{break-after:avoid}}th{{text-align:left;padding:4px 6px;border:.7px solid #000;font-weight:400;background:#fff}}td{{border:.7px solid #000;padding:5px 6px;height:44px;vertical-align:top}}
table.kv td:first-child,table.kv th:first-child{{width:42%}}
table.chk td{{height:30px}}table.wide{{table-layout:fixed}}table tr.bk td{{height:70px}}table.mid{{table-layout:fixed}}table.mid td{{height:56px}}table.wide td{{height:70px}}table.wide td:first-child{{height:auto}}
table.chk td:not(:first-child),table.chk th:not(:first-child){{width:62px;text-align:center}}
.scaf{{margin:5px 0;font-size:9.4pt}}
.tip{{margin:5px 0;font-size:9.2pt}}
.dua{{margin:6px 0;font-size:9.2pt}}
.inf{{margin:8px 0 6px}}.inf>b{{display:block;margin-bottom:3px}}
.read{{font-size:9.4pt;margin:5px 0;font-style:italic}}
.fill{{display:inline-block;min-width:120px;border-bottom:.8px solid #000}}
.grid{{height:230px;border:1px solid #000;background-image:linear-gradient(#bbb 1px,transparent 1px),linear-gradient(90deg,#bbb 1px,transparent 1px);background-size:14px 14px;margin:6px 0}}
.lg{{margin-left:auto;display:flex;align-items:center;gap:5px;font-size:10pt}}.lg b.i{{font-weight:700}}.lg span{{letter-spacing:.02em}}
.bank{{border:1px solid #000;border-radius:8px;padding:6px 10px;text-align:center}}.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:6px 0;break-inside:avoid}}.cards b{{grid-column:1/-1;font-weight:700}}.card{{border:1.2px dashed #000;border-radius:6px;padding:8px 6px;min-height:52px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:9pt}}.fig{{text-align:center;margin:4px 0}}.strip{{width:7cm;height:1.2cm;border:1.2px dashed #000;display:flex;align-items:center;justify-content:center;margin:6px 0}}
.foot{{margin-top:8px;font-size:8pt;text-align:center}}
</style></head><body>
<div class="hd"><div class="n"><small>SESIÓN</small>{num}</div><div><h1>{e(title)}</h1><p>Ciencia y Tecnología · 6.° grado · Unidad 8: El sistema reproductor humano</p></div><div class="lg"><svg viewBox="22 14 68 92" width="22" height="30" fill="none" stroke="#000" stroke-width="3"><path d="M27 20 Q36 19 44 21 Q49 29 53 38 Q42 34 30 34 Q28 27 27 20 Z"/><path d="M28 40 Q42 38 54 44 Q57 70 56 98 Q38 86 32 66 Q28 54 28 40 Z"/><path d="M58 26 Q74 32 84 46 Q82 76 58 100 Q62 64 58 26 Z"/></svg><span><b class="i">innova</b> schools</span></div></div>
{''.join(acts)}{extra}
<div class="foot">Producto de la unidad: Dos pósters científicos · Sistemas reproductores y ciclo ovárico · Tecnologías del embarazo y el parto</div>
</body></html>'''

ORG=["Características","Funciones","Dato interesante"]
def organ(orgs):return table(["Órgano"]+orgs,[[x] for x in ORG])
P=[]
CARD=lambda t:f'<div class="card">{t}</div>'
P.append(dict(t="Conocemos el sistema reproductor",acts=[
act(1,"i","¿Qué sé del sistema reproductor?",'<p>Lee el banco de palabras y escribe cada órgano en la columna que crees que corresponde.</p><p class="bank">testículos · ovarios · útero · pene · trompas de Falopio · vagina · escroto · conductos deferentes</p>'+
 table(["Sistema reproductor masculino","Sistema reproductor femenino"],[],3)+'<p>Elige dos órganos y escribe qué crees que hace cada uno.</p>'+
 scaf("«Creo que el/la ________ sirve para ________ porque ________.»")+lines(2)),
act(2,"g","Parejas de tarjetas",'<p>Recorten las tarjetas y formen parejas: cada órgano con su función. Luego comparen sus parejas con el video.</p><div class="cards"><b>Órganos</b>'+''.join(CARD(x) for x in ["Testículos","Ovarios","Útero","Escroto","Trompas de Falopio","Conductos deferentes","Vagina","Pene"])+'</div><div class="cards"><b>Funciones</b>'+''.join(CARD(x) for x in ["Es el lugar donde se desarrolla el bebé durante el embarazo","Producen los espermatozoides","Llevan los espermatozoides desde los testículos","Producen los óvulos","Protege a los testículos y regula su temperatura","Conducto que comunica el útero con el exterior; es el canal del parto","Conducen el óvulo hacia el útero; allí ocurre la fecundación","Órgano externo por donde salen la orina y el semen"])+'</div>'+
 '<p>¿Qué pareja les costó más? ¿Qué órganos no mencionó el video?</p>'+lines(2)+dua()),
act(3,"i","Mi glosario científico",informe("Glosario",table(["Palabra nueva","¿Qué significa?"],[],5))+
 scaf("«El sistema reproductor sirve para ________. Está formado por ________.»")+lines(2))]))
P.append(dict(t="El sistema reproductor masculino",acts=[
act(1,"i","Tomo apuntes del video",'<p>Mira el video dos veces. La segunda vez, completa la tabla con tus palabras.</p>'+
 table(["Órganos internos","Testículos","Conductos deferentes","Uretra"],[["Características"],["Funciones"],["Dato interesante"]],cls="wide")+table(["","Vesícula seminal","Pene (externo)","Escroto (externo)"],[["Características"],["Funciones"],["Dato interesante"]],cls="wide")+
 tip("Sintetizar es escribir las ideas principales con tus palabras, no copiar todo lo que dice el video.")),
act(2,"g","Tres estrellas y un deseo",'<p>En dúo, intercambien sus apuntes y revísenlos.</p>'+
 table(["Criterio","Estrella"],[["Identifica los órganos del sistema reproductor masculino","☐"],["Detalla la función de cada órgano","☐"],["Las ideas son claras y la letra es legible","☐"]])+
 table(["Mi deseo para mejorar tu trabajo"],[],1)+dua()),
act(3,"i","Para mi póster: sistema masculino",informe("Póster 1",scaf("«El/la ________ se encarga de ________.»")+lines(4)))]))
P.append(dict(t="El sistema reproductor femenino y el ciclo ovárico",acts=[
act(1,"i","Leo sobre el ciclo ovárico",'<p>¿Es lo mismo menstruación que ciclo ovárico? Escribe lo que piensas antes de leer.</p>'+lines(1)+
 '<div class="read">El ciclo ovárico o ciclo menstrual dura de 21 a 40 días y tiene tres fases. En la <b>fase folicular</b>, la hormona FSH hace madurar un óvulo dentro de un folículo del ovario y el recubrimiento del útero se engrosa. En la <b>ovulación</b>, la hormona LH hace que el óvulo maduro sea liberado; suele ocurrir cerca del día 14. En la <b>fase lútea</b>, el óvulo viaja por la trompa de Falopio y la progesterona prepara el útero. Si el óvulo no es fecundado, el recubrimiento del útero se desprende: es la <b>menstruación</b>, que dura de 3 a 7 días.<br>Fuente: adaptado de Sanitas, Biblioteca de salud.</div>'+
 '<p>Marca con una X las hormonas que participan en el ciclo:</p><p>FSH ( ) LH ( ) TSH ( ) Progesterona ( ) Testosterona ( ) Hormona de crecimiento ( )</p>'),
act(2,"g","El ciclo en pareja",'<p>En pareja, organicen las fases del ciclo ovárico.</p>'+
 table(["Fase","¿Qué ocurre?","Hormona que participa"],[["Folicular"],["Ovulación"],["Lútea"]])+
 organ(["Ovarios","Trompas de Falopio","Útero","Vagina"])+dua()),
act(3,"i","Para mi póster: sistema femenino",informe("Póster 1",scaf("«Primero ________. Luego ________. Finalmente ________.»")+lines(4)))]))
P.append(dict(t="La fecundación y el primer trimestre",acts=[
act(1,"i","Veo, pienso, me pregunto",'<p>Observa la imagen.</p><div class="fig"><svg viewBox="0 0 300 150" width="300" height="150" fill="none" stroke="#000" stroke-width="1.4"><circle cx="210" cy="75" r="52"/><circle cx="210" cy="75" r="58" stroke-dasharray="3 3"/><circle cx="222" cy="66" r="10"/><ellipse cx="140" cy="40" rx="6" ry="4"/><path d="M134 40 q-10 -6 -20 0 t-20 0"/><ellipse cx="125" cy="75" rx="6" ry="4"/><path d="M119 75 q-10 -6 -20 0 t-20 0"/><ellipse cx="145" cy="110" rx="6" ry="4"/><path d="M139 110 q-10 -6 -20 0 t-20 0"/><ellipse cx="100" cy="55" rx="6" ry="4"/><path d="M94 55 q-10 -6 -20 0 t-20 0"/><ellipse cx="95" cy="100" rx="6" ry="4"/><path d="M89 100 q-10 -6 -20 0 t-20 0"/></svg></div>'+table(["Veo","Pienso","Me pregunto"],[],1)+
 '<p>Palabras nuevas del video:</p>'+lines(1)),
act(2,"g","La fecundación paso a paso",table(["","La fecundación"],[["¿Qué células sexuales están involucradas?"],["¿Por qué las células sexuales se tienen que unir?"],["¿Qué sucede luego de que se unen?"]])+
 '<p>Ordenen los pasos del 1 al 4:</p>'+table(["N.°","Paso"],[["___","El cigoto se divide muchas veces"],["___","El espermatozoide se une al óvulo"],["___","El embrión se implanta en el útero"],["___","Se forma el cigoto"]])+dua()),
act(3,"i","Para mi póster: fecundación y primer trimestre",informe("Línea de tiempo",table(["Semanas","Cambio importante"],[["1 a 4"],["5 a 8"],["9 a 12"]]))+
 scaf("«En la semana ___ el embrión ________.»"))]))
P.append(dict(t="El desarrollo del bebé: segundo y tercer trimestre",acts=[
act(1,"i","La tirita de 7 cm",'<p>Recorta la tirita. Mide 7 cm.</p><div class="strip">7 cm</div><p>¿Qué crees que representa?</p>'+lines(1)+'<p>Mira el video del segundo trimestre y completa.</p>'+
 table(["Semana 14","Semana 16","Semana 20","Semana 24","Semana 28"],[],2)+'<p>¿Qué síntomas podría experimentar la mamá?</p>'+lines(1)),
act(2,"g","El viaje de 9 meses",'<p>Completen la información del tercer trimestre.</p>'+table(["Semana 28 (7.° mes)","Semana 32 (8.° mes)","Semana 36 (9.° mes)"],[],2)+
 '<p>¿Qué cambios presenta la mamá?</p>'+lines(1)+dua()),
act(3,"i","Para mi póster: segundo y tercer trimestre",informe("Datos sorprendentes",scaf("«En la semana ___ el bebé ________.»")+lines(3)))]))
P.append(dict(t="Opinamos sobre las tecnologías del embarazo y el parto",acts=[
act(1,"i","¿Cómo funciona una ecografía?",'<p>Mira el video y responde.</p>'+table(["Pregunta","Respuesta"],[["¿Cómo funciona una ecografía?"],["¿Qué utilidad tiene en el primer trimestre?"],["¿Y en el segundo trimestre?"],["¿Y en el tercer trimestre?"]])+
 '<div class="read"><b>El Minsa implementa monitores fetales.</b> Los Centros de Salud Materno Infantil de Lima cuentan con monitores fetales gemelares. Estos equipos miden la frecuencia cardíaca del bebé (latidos por minuto) y las contracciones del útero. Si el monitor muestra una frecuencia baja, los médicos pueden acelerar el parto o derivar a la gestante a un hospital. Además, el equipo puede leer los latidos de mellizos o trillizos.<br>Fuente: adaptado de Minsa, nota de prensa.</div>'),
act(2,"g","Opinamos en dúo",'<p>Compartan su opinión con su compañero y revísenla.</p>'+
 table(["Criterio","Sí","Debo mejorar"],[["Explica cómo funciona la tecnología","☐","☐"],["Da razones para su opinión","☐","☐"],["Usa información de fuentes confiables","☐","☐"]],cls="chk")+
 table(["Sugerencia de mejora para mi compañero"],[],1)+dua()),
act(3,"i","Para mi póster: mi opinión",informe("Póster 2",table(["Parte de mi opinión","Lo que escribo"],[["Introducción"],["¿Cómo funciona el monitor fetal?"],["Razón 1 para usar la tecnología"],["Razón 2 para usar la tecnología"],["Una precaución o razón en contra"],["Conclusión"]]))+
 scaf("«Opino que ________ porque ________. Según ________, ________.»"))]))
P.append(dict(t="Nuestros pósters científicos",acts=[
act(1,"i","Mi boceto",'<p>Planifica lo que aportarás al póster.</p>'+table(["Título","Dibujo o esquema","3 ideas clave con palabras científicas"],[],3)),
act(2,"g","Nuestros pósters científicos",table(["Póster","Contenido","Imágenes que usaremos","Responsable"],[["1. Sistemas reproductores y ciclo ovárico"],["2. Tecnologías del embarazo y el parto"]])+
 table(["Revisamos el póster","Sí","Debemos mejorar"],[["Tiene título e imágenes relacionadas","☐","☐"],["Explica con lenguaje científico","☐","☐"],["Explica cómo interviene la tecnología","☐","☐"],["Se lee con claridad","☐","☐"]],cls="chk")+dua()),
act(3,"i","Me evalúo",'<p>Marca tu nivel en cada criterio de la rúbrica.</p>'+
 table(["Criterio","C","B","A","AD"],[["Explica el saber científico","☐","☐","☐","☐"],["Explica las consecuencias de la tecnología","☐","☐","☐","☐"],["Opina sobre la tecnología con razones y fuentes","☐","☐","☐","☐"]])+
 '<p>¿Qué conocimientos son nuevos para ti en esta unidad?</p>'+lines(1)+'<p>¿Qué te gustaría investigar?</p>'+lines(1))]))
pk=json.load(open('/home/user/christian/packs/unidad8.json'))
for i,(p,s) in enumerate(zip(P,pk["sessions"]),1):
    h=page(i,p["t"],s["meta"],s["criteria"],p["acts"]).replace("⭐","★")
    h=re.sub(r'[\U0001F000-\U0001FAFF⌀-⏿☀-☄☆-☏☑-✓✕-➿️‍]\s?','',h)
    open(f'{OUT}s{i}.html','w').write(h)
print('ok',len(P))
