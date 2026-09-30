import json,html,re,pymupdf
E=html.escape
EM=re.compile(r'[\U0001F000-\U0001FAFF⌀-⏿☀-➿⭐️‍]\s?')
def c(x):return E(EM.sub('',x).strip())
RUB={7:("INDAGA · Indaga mediante métodos científicos",[
 ("Describe hechos y fenómenos","Describe los hechos o fenómenos relacionados con lo investigado usando datos cualitativos y cuantitativos (va en la introducción del informe)."),
 ("Formula pregunta de indagación","Formula una pregunta que establece relaciones de causa y efecto sobre la situación indagada."),
 ("Elabora hipótesis","Elabora una hipótesis que responde a la pregunta y relaciona la causa y el efecto."),
 ("Verificación mediante el diseño","Propone un diseño que permite comprobar o refutar la hipótesis, con repeticiones, forma de medir y medidas de seguridad, y lo pone en práctica."),
 ("Organiza y procesa datos","Organiza y procesa los datos con repeticiones y unidades en tablas de doble entrada y gráficos."),
 ("Elabora y comunica conclusiones","Elabora conclusiones de causa y efecto, las contrasta con otras fuentes, y describe dificultades y mejoras.")],
 ["Describe hechos y fenómenos","Describe hechos y fenómenos","Formula pregunta de indagación","Elabora hipótesis","Verificación mediante el diseño","Verificación mediante el diseño","Verificación mediante el diseño (puesta en práctica)","Organiza y procesa datos","Organiza y procesa datos","Elabora y comunica conclusiones","Todos los criterios (evaluación final)"]),
 8:("EXPLICA · Explica el mundo físico basándose en conocimientos científicos",[
 ("Explica el saber científico","Explica el saber científico relacionado con los sistemas fisiológicos de las funciones de los humanos."),
 ("Explica las consecuencias de las aplicaciones científicas y tecnológicas","Explica las consecuencias de las aplicaciones científicas y tecnológicas."),
 ("Opina sobre las consecuencias de las aplicaciones científicas y tecnológicas","Opina sobre las consecuencias (positivas y/o negativas) en su vida cotidiana, la de su familia o del entorno, sustentando sus ideas en razones y usando diversas fuentes.")],
 ["Explica el saber científico","Explica el saber científico","Explica el saber científico","Explica el saber científico","Explica el saber científico","Explica las consecuencias y Opina sobre la tecnología","Todos los criterios (póster final)"])}
CSS='''@page{size:A4;margin:14mm 14mm 14mm}body{font-family:"DejaVu Sans",Arial,sans-serif;font-size:10pt;color:#000}
h1{font-size:20pt;margin:0 0 4px}h2{font-size:14pt;margin:0 0 6px}h3{font-size:11pt;margin:10px 0 4px}
.k{font-size:8pt;letter-spacing:.1em;text-transform:uppercase}.box{border:1px solid #000;border-radius:10px;padding:8px 12px;margin:8px 0}
table{width:100%;border-collapse:collapse;margin:4px 0;font-size:9pt}th,td{border:.7px solid #000;padding:4px 6px;text-align:left;vertical-align:top}th{font-weight:600}
ol{margin:4px 0 0 18px;padding:0}li{margin:2px 0}.ok{text-decoration:underline}.pb{page-break-after:always}p{margin:4px 0}'''
def cover(n,pk,sess):
    name,crit,_=RUB[n]
    rows=''.join(f'<tr><td>{i}</td><td>{c(s["meta"])}</td><td>{E(RUB[n][2][i-1])}</td></tr>' for i,s in enumerate(sess,1))
    rb=''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td></tr>' for a,b in crit)
    return f'<div class="k">Guía docente · Ciencia y Tecnología · 6.° grado</div><h1>Unidad {n}: {E(pk["title"])}</h1><div class="box"><b>Producto:</b> {E(pk["product"])}</div><h3>Rúbrica {E(name)} (nivel A)</h3><table><tr><th style="width:32%">Criterio</th><th>Descripción</th></tr>{rb}</table><h3>Sesiones</h3><table><tr><th style="width:6%">N.°</th><th>Meta</th><th style="width:30%">Criterio de la rúbrica</th></tr>{rows}</table>'
def sess(n,i,s):
    cr=''.join(f'<li>{c(x)}</li>' for x in s["criteria"])
    ac=''.join(f'<tr><td>{k}</td><td>{"En grupo" if a["mode"]=="group" else "Individual"}</td><td><b>{c(a["title"])}</b><br>{c(a["desc"])}</td></tr>' for k,a in enumerate(s["activities"],1))
    fl=f'<div class="box"><b>Flipped:</b> {c(s["flipped"]["title"])}. {c(s["flipped"]["desc"])}</div>' if s.get("flipped",{}).get("enabled") else ''
    qs=''.join(f'<li>{c(q["q"])}<br>'+' · '.join((f'<span class="ok">{"abc"[j]}) {c(o)} ✔</span>' if j==q["answer"] else f'{"abc"[j]}) {c(o)}') for j,o in enumerate(q["options"]))+'</li>' for q in s["ticket"]["questions"])
    return f'<div class="k">Unidad {n} · Guía docente</div><h2>Sesión {i}</h2><div class="box"><b>Meta:</b> {c(s["meta"])}<br><b>Criterio de la rúbrica:</b> {E(RUB[n][2][i-1])}</div><h3>Criterios de éxito</h3><ol>{cr}</ol>{fl}<h3>Actividades</h3><table><tr><th style="width:8%">N.°</th><th style="width:14%">Modalidad</th><th>Actividad</th></tr>{ac}</table><h3>Exit ticket (respuesta correcta subrayada)</h3><ol>{qs}</ol><p style="margin-top:8px">A continuación: ficha del estudiante de la sesión {i}.</p>'
pages=[]
for n in (7,8):
    pk=json.load(open(f'unidad{n}.json'));S=pk["sessions"]
    pages.append(('html',cover(n,pk,S)))
    for i,s in enumerate(S,1):
        pages.append(('html',sess(n,i,s)));pages.append(('pdf',f'u{n}/sesion-{i}.pdf'))
k=0
for t,v in pages:
    if t=='html':open(f'_d{k}.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{v}');k+=1
json.dump([p if p[0]=='pdf' else ('html',None) for p in pages],open('_plan.json','w'))
print(k)
