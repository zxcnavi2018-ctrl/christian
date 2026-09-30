import json,html,re
OUT='/home/user/christian/packs/u7/'
import os;os.makedirs(OUT,exist_ok=True)
def e(x):return html.escape(x)
def lines(n=2):return '<div class="ln"></div>'*n
def table(head,rows,n=None,cls=""):
    h=''.join(f'<th>{e(x)}</th>' for x in head)
    body=''
    for r in rows:
        body+='<tr>'+''.join(f'<td>{c}</td>' for c in (r+['']*(len(head)-len(r))))+'</tr>'
    if n:
        for _ in range(n):body+='<tr>'+'<td>&nbsp;</td>'*len(head)+'</tr>'
    if len(head)==2 and not cls:cls="kv"
    return f'<table class="{cls}"><tr>{h}</tr>{body}</table>'
def check(title,items,cols=("Sí","Debo mejorar")):
    return table([title]+list(cols),[[e(i)]+['☐']*len(cols) for i in items],cls="chk")
def scaf(t):return f'<div class="scaf"><b>🪜 Andamio</b> {t}</div>'
def tip(t):return f'<div class="tip"><b>💡 Recuerda</b> {t}</div>'
def dua():return '<div class="dua"><b>🎨 ¿Cómo lo presentamos?</b> Elijan el formato que más les guste: afiche · cómic · organizador visual · maqueta · dramatización · audio o video corto · canción o rima · exposición con objetos · ¡otra idea!</div>'
def informe(part,body):return f'<div class="inf"><b>📘 Para mi informe · {e(part)}</b>{body}</div>'
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
.hd{{display:flex;align-items:center;gap:12px;border:2px solid #000;border-radius:14px;padding:8px 14px}}
.hd .n{{border:2px solid #000;border-radius:12px;padding:6px 12px;font-weight:900;font-size:18pt;text-align:center;line-height:1}}
.hd .n small{{display:block;font-size:7pt;letter-spacing:.08em}}
.hd h1{{margin:0;font-size:15pt}}.hd p{{margin:2px 0 0;font-size:8.5pt}}
.name{{display:flex;gap:10px;margin:8px 0;font-size:9pt}}.name span{{flex:1;border-bottom:1.3px solid #000;padding-bottom:2px}}
.meta{{border:1.5px solid #000;border-radius:12px;padding:7px 12px;margin:6px 0}}
.meta ul{{list-style:none;padding:0;margin:4px 0 0;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:9pt}}
.act{{border:1.5px solid #000;border-radius:14px;padding:8px 12px 10px;margin:10px 0;break-inside:auto}}
.act.g{{border-style:double;border-width:4px}}
.ah{{display:flex;gap:8px;align-items:center}}.an{{font-weight:900;font-size:8pt;letter-spacing:.08em;text-transform:uppercase}}
.am{{font-size:8pt;font-weight:800;border-radius:999px;padding:1px 9px;border:1.3px solid #000}}
h2{{margin:3px 0 6px;font-size:12.5pt}}h3{{font-size:10.5pt;margin:8px 0 4px}}
p{{margin:4px 0}}.ln{{border-bottom:1.2px dotted #000;height:27px}}
table{{width:100%;border-collapse:collapse;margin:5px 0;font-size:9.2pt;break-inside:avoid}}th{{text-align:left;padding:4px 6px;border:1px solid #000;font-weight:800}}td{{border:1px solid #000;padding:5px 6px;height:28px;vertical-align:top}}
table.kv td:first-child,table.kv th:first-child{{width:42%}}
table.chk td:not(:first-child),table.chk th:not(:first-child){{width:62px;text-align:center}}
.scaf{{border:1.3px dashed #000;border-radius:10px;padding:5px 9px;margin:5px 0;font-size:9.4pt}}
.tip{{border-left:4px solid #000;padding:4px 9px;margin:5px 0;font-size:9.2pt}}
.dua{{border:1.3px dotted #000;border-radius:10px;padding:5px 9px;margin:6px 0;font-size:9.2pt}}
.inf{{border:2px solid #000;border-radius:12px;padding:6px 10px;margin:6px 0}}.inf>b{{display:block;margin-bottom:3px}}
.read{{border:1.2px solid #000;border-radius:10px;padding:6px 10px;font-size:9.4pt;margin:5px 0}}
.fill{{display:inline-block;min-width:120px;border-bottom:1.2px solid #000}}
.grid{{height:230px;border:1px solid #000;background-image:linear-gradient(#bbb 1px,transparent 1px),linear-gradient(90deg,#bbb 1px,transparent 1px);background-size:14px 14px;margin:6px 0}}
.foot{{margin-top:8px;font-size:8pt;text-align:center}}
</style></head><body>
<div class="hd"><div class="n"><small>SESIÓN</small>{num}</div><div><h1>{e(title)}</h1><p>Ciencia y Tecnología · 6.° grado · Unidad 7: Microorganismos en acción</p></div></div>
{''.join(acts)}{extra}
<div class="foot">Producto de la unidad: Informe de indagación · ¿Cómo influye la temperatura del agua en la actividad de la levadura?</div>
</body></html>'''

P=[]
# ---------- S1
P.append(dict(t="¿Por qué nos enfermamos?",acts=[
act(1,"i","🤒 ¿Por qué me enfermé?",'<p>Lee cada caso.</p><div class="read"><b>Caso 1 · Lucía:</b> tiene fiebre, tos y dolor de garganta. El médico explica que tiene <b>influenza</b>, causada por un virus.<br><b>Caso 2 · Mariana:</b> tiene fiebre alta y dolor muscular. Tiene <b>dengue</b>, causado por un virus que llega por la picadura de un mosquito infectado.<br><b>Caso 3 · Carlos:</b> controla la glucosa de su sangre porque tiene <b>diabetes</b>. No la causa ningún virus, bacteria, hongo ni parásito.<br><b>Caso 4 · Pedro:</b> se cansa con frecuencia. Tiene <b>anemia</b> por falta de hierro en su organismo.</div>'+
 table(["Caso","¿Qué enfermedad tiene?","¿Qué la causa?","¿Interviene un microorganismo?","¿Infecciosa o no infecciosa?","¿Qué dato te ayudó a decidir?"],[["Lucía"],["Mariana"],["Carlos"],["Pedro"]])+
 scaf("Pregúntate: ¿se puede pasar de una persona a otra? ¿La causa un virus, una bacteria, un hongo o un parásito?")),
act(2,"g","🦠 Microorganismos: ¿amigos o enemigos?",'<p>En grupo, usen lo que investigaron antes de clase (levadura, bacterias del yogur, <i>Salmonella</i> y moho del pan).</p>'+
 table(["Microorganismo","Grupo (bacteria, hongo…)","¿Qué hace?","¿Nos ayuda o nos daña? ¿En qué contexto?"],[["Levadura de pan"],["Bacterias del yogur"],["Salmonella"],["Moho del pan"]])+
 '<p><b>Pregunta del grupo:</b> ¿Todos los microorganismos del mismo grupo producen el mismo efecto? ¿Por qué?</p>'+lines(2)+dua()+
 tip("<i>Salmonella</i> y los mohos no se cultivan ni se manipulan en el aula.")),
act(3,"i","🍞 Mi microorganismo útil",'<p>Completa:</p>'+table(["Una enfermedad es…","Una enfermedad infecciosa se caracteriza por…","Una enfermedad no infecciosa se caracteriza por…"],[],1)+
 informe("Introducción (parte 1)",'<p>Escribe 3 o 4 líneas sobre la levadura: qué es y cómo nos ayuda.</p>'+scaf("«La levadura es un ________ formado por ________. Nos ayuda a ________ porque ________.»")+lines(3)))]))
# ---------- S2
P.append(dict(t="La levadura despierta",acts=[
act(1,"i","👀 Predigo y observo",'<p>Antes de comenzar, responde:</p><p>¿Qué cambio crees que observarás en la mezcla de agua, azúcar y levadura?</p>'+lines(2)+'<p>¿Qué cambio podrías medir con una regla?</p>'+lines(1)+
 scaf("Usa tus sentidos: 👁️ ¿qué cambia de tamaño o de color? 👃 ¿a qué huele? 👂 ¿se escucha algo?")),
act(2,"g","🧪 Registramos los cambios",'<p>Observen la mezcla cada 5 minutos y completen la tabla.</p>'+
 table(["Tiempo","Altura de la espuma","Burbujas observadas","Descripción del cambio"],[["0 min","____ cm"],["5 min","____ cm"],["10 min","____ cm"],["15 min","____ cm"],["20 min","____ cm"]])+
 tip("<b>Medir</b> es usar un instrumento y escribir la cantidad con su unidad. <b>Describir</b> es contar lo que observas sin explicar todavía por qué ocurre.")+
 '<p>¿Cuánto cambió la altura entre el inicio y los 20 minutos? Cálculo: <span class="fill"></span> Diferencia: <span class="fill" style="min-width:60px"></span> cm</p>'+dua()),
act(3,"i","📝 Explico el fenómeno",'<div class="read">La levadura es un microorganismo formado por una sola célula. Con agua, azúcar y una temperatura adecuada realiza <b>fermentación</b>: usa el azúcar y produce un gas llamado <b>dióxido de carbono</b>. Sus burbujas forman la espuma. La levadura de pan trabaja mejor cerca de los 30 °C; con frío actúa más lento y con calor excesivo se daña.<br><small>Fuente: adaptado de Khan Academy y Salvadó et al. (2011).</small></div>'+
 scaf("«La altura de la espuma cambió de ___ cm a ___ cm. Este cambio ocurrió porque la levadura utilizó el azúcar y liberó ________. Las burbujas de este gas ________.»")+lines(2)+
 table(["Factor que podría cambiarse","Efecto que podría medirse","Instrumento para medirlo"],[],1)+
 informe("Introducción (parte 2)",'<p>Describe lo que ocurrió con tus datos y completa: «Posible relación entre la ________ del agua y la ________ de la espuma».</p>'+lines(2)))]))
# ---------- S3
P.append(dict(t="Formulamos nuestra pregunta de indagación",acts=[
act(1,"i","❓ ¿Se puede investigar?",'<p>Marca ✔ las preguntas que se pueden responder con un experimento.</p>'+
 table(["Pregunta","¿Se puede investigar?","¿Por qué?"],[["¿Te gusta el pan con levadura?","☐ Sí ☐ No"],["¿Cómo influye la temperatura del agua en la altura de la espuma?","☐ Sí ☐ No"],["¿La levadura es bonita?","☐ Sí ☐ No"],["¿Cómo influye la cantidad de azúcar en la altura de la espuma?","☐ Sí ☐ No"]])+
 scaf("¿Hay algo que puedo <b>cambiar</b>? ¿Hay algo que puedo <b>medir</b> con un instrumento? Si las dos respuestas son «sí», ¡se puede investigar!")+
 '<p><b>Nuestra experiencia:</b> agua a 15 °C, 25 °C y 35 °C · termómetro · regla · cronómetro · la misma cantidad de agua, azúcar y levadura en cada recipiente.</p>'+
 table(["Elemento","Respuesta"],[["Factor que se modificará"],["Valores que se probarán"],["Efecto que se medirá"],["Instrumento y unidad"],["Tiempo para comparar"]])),
act(2,"g","🃏 Fábrica de preguntas",'<p>Comparen sus preguntas individuales y construyan la pregunta del equipo.</p>'+
 table(["Pregunta inicial del equipo"],[],1)+'<p>Otro equipo les da retroalimentación:</p>'+feedback("estrella")+table(["Pregunta mejorada del equipo"],[],1)+dua()),
act(3,"i","✏️ Mi pregunta científica",scaf("«¿Cómo influye ________ (🔵 causa) en ________ (🔴 efecto) después de ________?»")+
 informe("Pregunta de indagación",'<p>Escribe tu pregunta. Subraya la causa en azul y el efecto en rojo.</p>'+lines(2))+
 check("Reviso mi pregunta",["Seleccioné un factor que puede modificarse","Seleccioné un efecto que puede medirse","Relacioné lo que se modificará con lo que se medirá"])+
 '<p>⭐ <b>Reto:</b> escribe otra pregunta sobre un factor distinto que también se pueda experimentar.</p>'+lines(1))]))
# ---------- S4
P.append(dict(t="Elaboramos nuestra hipótesis",acts=[
act(1,"i","📖 La levadura y la temperatura",'<p>Copia la pregunta acordada:</p>'+lines(1)+'<div class="read">La levadura es un microorganismo de una sola célula. Con agua y azúcar realiza <b>fermentación</b>: usa el azúcar y libera <b>dióxido de carbono</b>, cuyas burbujas forman la espuma. La temperatura modifica su actividad: dentro de un intervalo adecuado, una temperatura más cálida favorece la fermentación; con frío actúa más lento; una temperatura demasiado alta puede dañar sus células.</div>'+
 scaf("Mientras lees, pregúntate: ¿qué le pasa a la levadura con el frío? ¿Y con lo tibio? ¿Y con el calor excesivo?")+
 table(["Idea científica que me ayuda a predecir","¿Por qué la elegí?"],[["Idea 1:"],["Idea 2:"]])),
act(2,"g","🎲 La apuesta científica",'<p>¿Con qué temperatura habrá más espuma? Ordénenlas de mayor a menor y defiendan su apuesta.</p>'+
 table(["1.° lugar (más espuma)","2.° lugar","3.° lugar (menos espuma)"],[["____ °C","____ °C","____ °C"]])+
 scaf("«Creemos que con agua a ___ °C habrá más espuma porque en el texto dice que ________.»")+
 table(["Hipótesis inicial del equipo"],[],1)+feedback("estrella")+table(["Hipótesis mejorada del equipo"],[],1)+dua()),
act(3,"i","💡 Mi hipótesis",table(["Componente","Respuesta"],[["Factor que se modificará"],["Efecto que se medirá"],["Temperaturas que se probarán"],["Temperatura con la que espero más espuma"],["Información científica que explica mi predicción"]])+
 scaf("«<b>Si</b> la temperatura inicial del agua ________, <b>entonces</b> la mezcla con agua a ___ °C producirá ________, <b>porque</b> ________.»")+
 informe("Hipótesis",lines(3))+
 check("Reviso mi hipótesis",["Seleccioné información científica relacionada con la pregunta","Relacioné la temperatura con la altura de la espuma","Predije con qué temperatura habrá más espuma","Expliqué científicamente mi predicción"]))]))
# ---------- S5
P.append(dict(t="Determinamos nuestras variables",acts=[
act(1,"i","🔎 ¿Es una prueba justa?",'<p>Un equipo preparó estas mezclas:</p>'+
 table(["Mezcla","Temperatura","Agua","Azúcar","Levadura"],[["A","15 °C","50 mL","5 g","2 g"],["B","35 °C","60 mL","10 g","3 g"]])+
 '<p>¿Qué factores cambió el equipo?</p>'+lines(1)+'<p>¿Podrían saber si la diferencia en la espuma se debió solo a la temperatura? ¿Por qué?</p>'+lines(2)+
 scaf("Tres preguntas clave: ¿Qué cambio a propósito? ¿Qué mido? ¿Qué debe quedar igual para que la prueba sea justa?")),
act(2,"g","🔧 Las reglas de nuestro experimento",table(["Componente","Decisión del grupo"],[["Variable que modificaremos (independiente)"],["Valores que probaremos"],["Instrumento y unidad"],["Variable que mediremos (dependiente)"],["¿Cómo la mediremos? Instrumento y unidad"]])+
 table(["Factor que mantendremos igual","Valor o forma que usaremos"],[["Cantidad de agua"],["Cantidad de azúcar"],["Cantidad de levadura"],["Tipo y tamaño del recipiente"],["Forma de mezclar"],["Tiempo total y momentos de medición"],["Forma de medir la espuma"]])+
 tip("La variable que <b>modificamos</b> es la <b>independiente</b>. La variable que <b>medimos</b> es la <b>dependiente</b>.")+dua()),
act(3,"i","📋 Mis variables",informe("Variables",table(["Cambiaremos","Mediremos","Mantendremos igual"],[],1)+'<p>Explica con tus palabras por qué algunas cosas deben quedar igual:</p>'+lines(2))+
 '<h3>🚦 Semáforo de criterios</h3>'+table(["Criterio","Verde","Amarillo","Rojo"],[["Identifico la variable que se modificará y la que se medirá","☐","☐","☐"],["Indico los instrumentos y las unidades","☐","☐","☐"],["Establezco los factores que se mantendrán iguales","☐","☐","☐"]])+'<p>Mejora que realizaré:</p>'+lines(1))]))
# ---------- S6
P.append(dict(t="Diseñamos nuestro experimento",acts=[
act(1,"i","🧩 Pasos en orden",'<p>Ordena los pasos para preparar un vaso de refresco con los números 1 a 5.</p>'+
 table(["N.°","Paso"],[["___","Mezclar hasta disolver el azúcar"],["___","Lavar el vaso y la cuchara"],["___","Echar 200 mL de agua al vaso"],["___","Servir y beber"],["___","Agregar dos cucharadas de azúcar y el jugo"]])+
 scaf("Usa conectores: <b>primero</b>, <b>luego</b>, <b>después</b>, <b>finalmente</b>.")),
act(2,"g","🗺️ Nuestro plan de experimento",table(["Material o instrumento","Cantidad","¿Para qué lo usaremos?"],[],4)+
 table(["Medidas de seguridad"],[["💧 Agua a una temperatura máxima de 35 °C"],["🚫 No consumir ni acercar el rostro a las mezclas"],[""]])+
 table(["Paso","Acción (en orden)"],[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"]])+
 '<p>Revisen el diseño de otro grupo:</p>'+feedback("vps")+dua()),
act(3,"i","📊 Mi tabla de registro",informe("Diseño",'<p>Diseña tu tabla con temperaturas, repeticiones y tiempos.</p>'+
 table(["Temperatura","Repetición","0 min","5 min","10 min","15 min","20 min"],[["15 °C","1"],["15 °C","2"],["15 °C","3"],["25 °C","1"],["…",""]])+'<p>Unidad para la altura de la espuma: <span class="fill"></span></p>')+
 check("Comprobamos el diseño",["Indicamos materiales, instrumentos y su función","Incluimos medidas de seguridad","Organizamos las acciones en secuencia lógica","La tabla incluye temperaturas, tiempos y repeticiones"],("Sí","Debemos mejorar")))]))
# ---------- S7
P.append(dict(t="¡Manos a la ciencia!",acts=[
act(1,"i","🦺 Listos y seguros",'<p>Mi rol en el grupo: ☐ Medidor ☐ Cronometrista ☐ Anotador ☐ Vigía de seguridad</p>'+
 table(["Medida de seguridad","Sí"],[["Usamos agua a una temperatura máxima de 35 °C","☐"],["Los recipientes están sobre una superficie estable","☐"],["No consumimos ni acercamos el rostro a las mezclas","☐"],["Tenemos papel para limpiar derrames","☐"],["Nos lavaremos las manos al finalizar","☐"]])+
 table(["Recipiente","Agua","Azúcar","Levadura","Etiqueta"],[["15 °C","___ mL","___ g","___ g","☐"],["25 °C","___ mL","___ g","___ g","☐"],["35 °C","___ mL","___ g","___ g","☐"]])),
act(2,"g","⏱️ Realizamos el experimento",'<p>Hagan el experimento con las 3 temperaturas, 3 veces cada una. Midan la espuma a los 20 minutos y tomen fotos como evidencia.</p>'+
 table(["Temperatura","Repetición 1","Repetición 2","Repetición 3","Total"],[["15 °C"],["25 °C"],["35 °C"]])+'<p>Unidad de medida: <span class="fill"></span></p>'+
 table(["Incidencia observada","¿En qué recipiente?","¿Cómo podría afectar el dato?"],[],2)+
 tip("Si no hubo incidencias, escriban: «No se observaron incidencias que afectaran el registro».")),
act(3,"i","📓 Mi diario del experimento",informe("Registro de datos",scaf("«Observé que ________ (burbujas, olor, color). Lo más difícil fue ________.»")+lines(3))+
 table(["¿Qué observación recibimos?","¿Qué ajuste realizamos?"],[],1))]))
# ---------- S8
P.append(dict(t="Procesamos nuestros datos",acts=[
act(1,"i","🧮 Verifico y saco el promedio",check("Verifico mis registros",["Tengo datos de 15 °C, 25 °C y 35 °C","Tengo las tres repeticiones","Las medidas están en centímetros","Registré las incidencias"],("Sí","Debo revisar"))+
 scaf("Promedio: 1) Suma las 3 repeticiones. 2) Divide el total entre 3. 3) Escribe la unidad. Ejemplo: 4 + 5 + 6 = 15 → 15 ÷ 3 = <b>5 cm</b>.")+
 table(["Temperatura","Rep. 1","Rep. 2","Rep. 3","Total","Promedio (cm)"],[["15 °C"],["25 °C"],["35 °C"]])),
act(2,"g","📈 Nuestros datos hablan",'<p>Construyan un gráfico de barras con los promedios.</p><div class="grid"></div>'+
 '<p>Título: <span class="fill" style="min-width:300px"></span></p><p>Eje horizontal: <span class="fill"></span> Eje vertical: <span class="fill"></span></p>'+
 '<p>¿Por qué eligieron este gráfico?</p>'+lines(1)+dua()),
act(3,"i","📊 Mi tabla y mi gráfico",informe("Resultados",'<p>Pasa tu tabla de promedios y tu gráfico al informe.</p>')+
 check("Compruebo mi gráfico",["Tiene un título relacionado con los datos","Los ejes tienen nombres y unidades","La escala aumenta de manera uniforme","Representa las tres temperaturas","Coincide con la tabla","Incluye una leyenda"],("Sí","Debo revisar"))+
 '<p>⭐ <b>Reto:</b> explica por qué el tipo de gráfico que elegiste es el adecuado.</p>'+lines(1))]))
# ---------- S9
P.append(dict(t="Interpretamos nuestros resultados",acts=[
act(1,"i","🔍 Leo mis resultados",table(["Temperatura","Altura promedio a los 20 min"],[["15 °C","____ cm"],["25 °C","____ cm"],["35 °C","____ cm"]])+
 '<p>Temperatura con más espuma: <span class="fill"></span> Con menos espuma: <span class="fill"></span></p><p>Diferencia entre el mayor y el menor: <span class="fill" style="min-width:200px"></span></p>'+
 scaf("Mira tu gráfico: ¿cuál es la barra más alta? ¿Cuál la más baja? ¿Hay algún dato muy distinto?")),
act(2,"g","🖼️ Galería científica",'<p>Visiten los gráficos de los demás grupos.</p>'+
 table(["¿Qué se repite en todos? (patrón)","¿Qué fue diferente? (dato inusual)","¿Por qué pudo pasar?"],[],1)+
 '<p>¿Alguna incidencia registrada podría explicar el dato inusual?</p>'+lines(1)+dua()),
act(3,"i","🗣️ Lo que muestran mis datos",table(["Componente","Respuesta"],[["Resultado principal"],["Comparación entre temperaturas"],["Evidencia 1 (dato)"],["Evidencia 2 (dato)"],["Patrón identificado"],["Límite de mis resultados"]])+
 scaf("«Cuando la temperatura fue ___ °C, la espuma llegó a ___ cm. <b>Esto muestra que</b> ________.»")+
 informe("Interpretación",lines(3)))]))
# ---------- S10
P.append(dict(t="Argumentamos nuestra conclusión",acts=[
act(1,"i","📚 Lo que dice la ciencia",'<div class="read">Con agua y azúcar, la levadura realiza fermentación para obtener energía y libera <b>dióxido de carbono</b>; sus burbujas forman la espuma. La temperatura influye en la actividad de sus células: dentro de un intervalo adecuado, más calor favorece la fermentación; con frío es más lenta; el calor excesivo daña sus células. En nuestra indagación solo probamos 15 °C, 25 °C y 35 °C.</div>'+
 table(["Información científica","Dato de mi experimento","¿Cómo ayuda a explicar el resultado?"],[],2)+
 scaf("Pregúntate: ¿qué parte del texto explica lo que pasó en <b>mi</b> experimento?")),
act(2,"g","⚖️ Juicio a la hipótesis",table(["Nuestra hipótesis predijo","Los resultados mostraron"],[],1)+
 '<p>Veredicto: ☐ Respaldada ☐ Parcialmente respaldada ☐ No respaldada</p><p>Datos que sustentan la decisión:</p>'+lines(2)+
 scaf("«Nuestra hipótesis fue ________ porque los datos muestran que ________.»")+dua()),
act(3,"i","🏁 Mi conclusión",table(["Componente","Respuesta"],[["Respuesta a la pregunta"],["Decisión sobre la hipótesis"],["Evidencia 1"],["Evidencia 2"],["Explicación científica"],["Dificultades y mejoras"]])+
 informe("Conclusión",scaf("1) Descubrí que… 2) Esto coincide con… 3) Tuve dificultad con… 4) Lo mejoraría…")+lines(4)))]))
# ---------- S11
P.append(dict(t="Científicos ante un nuevo reto",acts=[
act(1,"i","🆕 Un nuevo misterio",'<div class="read">Un grupo de 6.° quiere saber si la <b>cantidad de azúcar</b> cambia la actividad de la levadura. Usaron agua a 25 °C en todos los vasos y probaron 0 g, 5 g y 10 g de azúcar. Midieron la espuma a los 20 minutos, 3 veces cada una.</div>'+
 table(["Elemento","Respuesta"],[["Pregunta de indagación"],["Hipótesis posible"],["Variable independiente"],["Variable dependiente"],["Factores que quedan igual"]])),
act(2,"g","🕵️ Científicos en acción",'<p>Analicen los resultados del grupo:</p>'+table(["Azúcar","Rep. 1","Rep. 2","Rep. 3","Promedio"],[["0 g","0,2 cm","0,1 cm","0,3 cm",""],["5 g","2,8 cm","3,1 cm","3,0 cm",""],["10 g","4,2 cm","4,5 cm","1,0 cm",""]])+
 '<p>¿Qué conclusión se puede sacar? ¿Hay un dato inusual?</p>'+lines(2)+table(["Mejora 1 al procedimiento","Mejora 2 al procedimiento"],[],1)+dua()),
act(3,"i","🪞 Me evalúo",'<p>Revisa tu informe y marca tu nivel en cada criterio de la rúbrica.</p>'+
 table(["Criterio","C","B","A","AD"],[["Describe hechos y fenómenos (introducción)","☐","☐","☐","☐"],["Formula pregunta de indagación","☐","☐","☐","☐"],["Elabora hipótesis","☐","☐","☐","☐"],["Diseña y ejecuta su indagación","☐","☐","☐","☐"],["Organiza y procesa datos","☐","☐","☐","☐"],["Elabora y comunica conclusiones","☐","☐","☐","☐"]])+
 '<p>🎯 Mi meta para mejorar:</p>'+lines(2))]))
pk=json.load(open('/home/user/christian/packs/unidad7.json'))
for i,(p,s) in enumerate(zip(P,pk["sessions"]),1):
    h=page(i,p["t"],s["meta"],s["criteria"],p["acts"]).replace("⭐","★")
    h=re.sub(r'[\U0001F000-\U0001FAFF\u2300-\u23FF\u2600-\u2604\u2606-\u260F\u2611-\u2713\u2715-\u27BF\uFE0F\u200D]\s?','',h)
    open(f'{OUT}s{i}.html','w').write(h)
    s["fichaTitle"]=f'Ficha · Sesión {i} · {p["t"]}'
json.dump(pk,open('/home/user/christian/packs/unidad7.json','w'),ensure_ascii=False,indent=1)
print('ok',len(P))
