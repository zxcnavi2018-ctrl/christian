import json
DUA=" Preséntenlo como más les guste: afiche, cómic, organizador, maqueta, dramatización, audio o video corto."
def Q(q,o,a,w):return{"q":q,"options":o,"answer":a,"why":w}
def A(m,t,d):return{"mode":m,"title":t,"desc":d,"ficha":"","file":""}
S=[]
S.append(dict(meta="Describe las principales características del sistema reproductor humano.",
 criteria=["Identifica las funciones generales del sistema reproductor","Diferencia órganos del sistema masculino y femenino","Usa vocabulario científico"],
 activities=[A("individual","🧩 ¿Qué sé del sistema reproductor?","Lee el banco de palabras (testículos, ovarios, útero, pene, trompas de Falopio, vagina, escroto, conductos deferentes) y escribe cada órgano en el sistema que crees que corresponde. Luego elige dos y escribe qué crees que hace cada uno."),
  A("group","👥 Parejas de tarjetas","En grupo, recorten las tarjetas de la ficha y formen parejas de cada órgano con su función. Luego compárenlas con el video: ¿qué pareja les costó más? ¿Qué órganos no mencionó el video?"+DUA),
  A("individual","📘 Mi glosario científico","Empieza tu glosario: escribe 5 palabras nuevas con su significado. Completa: «El sistema reproductor sirve para ___». Será la base de tu póster.")],
 qs=[Q("¿Cuál es la función principal del sistema reproductor?",["Permitir la reproducción, es decir, originar nuevos seres humanos","Digerir los alimentos","Bombear la sangre"],0,"El sistema reproductor permite la formación de nuevos seres humanos."),
  Q("¿Qué órgano pertenece al sistema reproductor femenino?",["Los testículos","El útero","La próstata"],1,"El útero es parte del sistema reproductor femenino."),
  Q("¿Qué órgano pertenece al sistema reproductor masculino?",["El ovario","La vagina","Los testículos"],2,"Los testículos producen los espermatozoides."),
  Q("¿Cómo se llaman las células sexuales femeninas?",["Óvulos","Espermatozoides","Neuronas"],0,"Los óvulos se forman en los ovarios."),
  Q("¿Para qué sirve un glosario científico?",["Para dibujar","Para registrar palabras nuevas y su significado","Para copiar tareas"],1,"El glosario ayuda a usar un lenguaje científico correcto.")]))
S.append(dict(meta="Describe las partes y funciones del sistema reproductor masculino.",
 criteria=["Identifica los órganos del sistema masculino","Detalla la función de cada órgano","Usa vocabulario científico"],
 activities=[A("individual","🎬 Tomo apuntes del video","Mira el video y completa la tabla con las características, funciones y un dato interesante de cada órgano: testículos, conductos deferentes, uretra, vesícula seminal, pene y escroto. Resume con tus palabras, no copies todo."),
  A("group","⭐ Tres estrellas y un deseo","En dúo, intercambien sus apuntes. Denle a su compañero una estrella por cada criterio cumplido (identifica órganos, detalla funciones, ideas claras) y un deseo para mejorar."+DUA),
  A("individual","📝 Para mi póster: sistema masculino","Elige 3 órganos y explica su función en una oración cada uno: «El/la ___ se encarga de ___».")],
 qs=[Q("¿Qué órgano produce los espermatozoides?",["Los testículos","La uretra","El escroto"],0,"Los testículos producen los espermatozoides y la hormona testosterona."),
  Q("¿Cuál es la función del escroto?",["Producir orina","Proteger los testículos y regular su temperatura","Formar el óvulo"],1,"El escroto es la bolsa de piel que protege a los testículos."),
  Q("¿Por dónde viajan los espermatozoides desde los testículos?",["Por el útero","Por las trompas de Falopio","Por los conductos deferentes"],2,"Los conductos deferentes transportan los espermatozoides."),
  Q("¿Qué órganos del sistema masculino son externos?",["El pene y el escroto","La vesícula seminal y la uretra","Los conductos deferentes"],0,"El pene y el escroto se ven por fuera del cuerpo."),
  Q("¿Qué significa «sintetizar» información de un video?",["Copiar todo lo que dice","Escribir las ideas principales con tus palabras","No tomar apuntes"],1,"Sintetizar es resumir lo importante.")]))
S.append(dict(meta="Explica las partes del sistema reproductor femenino y el ciclo ovárico.",
 criteria=["Identifica órganos y funciones del sistema femenino","Describe las fases del ciclo ovárico y sus hormonas","Usa vocabulario científico"],
 activities=[A("individual","📖 Leo sobre el ciclo ovárico","Antes de leer, escribe si crees que menstruación y ciclo ovárico son lo mismo. Lee sobre las tres fases del ciclo y marca con una X las hormonas que participan."),
  A("group","🔄 El ciclo en pareja","En pareja, completen la tabla de las tres fases del ciclo ovárico (qué ocurre y qué hormona participa) y la tabla de ovarios, trompas de Falopio, útero y vagina."+DUA),
  A("individual","📝 Para mi póster: sistema femenino","Resume el ciclo ovárico en 3 oraciones para tu póster: «Primero ___. Luego ___. Finalmente ___».")],
 qs=[Q("¿Qué órgano produce los óvulos?",["Los ovarios","El útero","La vagina"],0,"Los óvulos maduran dentro de los ovarios."),
  Q("¿Cuántas fases tiene el ciclo ovárico?",["Dos","Tres: folicular, ovulación y lútea","Cinco"],1,"Tiene tres fases: folicular, ovulatoria y lútea."),
  Q("¿Qué es la ovulación?",["El inicio de la menstruación","El crecimiento del útero","La liberación de un óvulo maduro desde el ovario"],2,"En la ovulación el ovario libera un óvulo maduro."),
  Q("¿Qué hormona prepara el útero para recibir un óvulo fecundado?",["La progesterona","La insulina","La adrenalina"],0,"La progesterona mantiene el recubrimiento del útero."),
  Q("¿Qué ocurre si el óvulo no es fecundado?",["Se forma un bebé","El recubrimiento del útero se desprende: es la menstruación","El ovario deja de funcionar"],1,"Sin fecundación, el recubrimiento se expulsa como menstruación.")]))
S.append(dict(meta="Explica el proceso de fecundación y los cambios en el primer trimestre del embarazo.",
 criteria=["Describe paso a paso la fecundación","Describe los eventos del primer trimestre","Presenta información sintetizada con lenguaje científico"],
 activities=[A("individual","👀 Veo, pienso, me pregunto","Observa el dibujo de la ficha y escribe: ¿qué veo?, ¿qué pienso?, ¿qué me pregunto? Luego mira el video y anota las palabras nuevas."),
  A("group","🧬 La fecundación paso a paso","En grupo, respondan qué células se unen, por qué se unen y qué pasa después, y ordenen del 1 al 4 los pasos de la fecundación."+DUA),
  A("individual","📝 Para mi póster: fecundación y primer trimestre","Completa una línea de tiempo del primer trimestre (semanas 1 a 12) con 3 cambios importantes del bebé en formación.")],
 qs=[Q("¿Qué células se unen en la fecundación?",["El espermatozoide y el óvulo","Dos óvulos","Dos neuronas"],0,"La fecundación es la unión de un espermatozoide con un óvulo."),
  Q("¿Cómo se llama la primera célula que se forma tras la fecundación?",["Feto","Cigoto","Óvulo"],1,"La célula resultante se llama cigoto."),
  Q("¿Dónde se implanta el embrión?",["En el ovario","En la vagina","En el útero"],2,"El embrión se implanta en la pared del útero."),
  Q("¿Por qué el espermatozoide y el óvulo aportan cada uno la mitad del material genético?",["Para formar un ser con información de ambos padres","Porque son pequeños","Para producir hormonas"],0,"Cada célula sexual aporta la mitad de la información genética."),
  Q("¿Cuánto dura aproximadamente el primer trimestre?",["1 mes","Las primeras 12 semanas","9 meses"],1,"El primer trimestre abarca aproximadamente las semanas 1 a 12.")]))
S.append(dict(meta="Explica el desarrollo fetal en el segundo y tercer trimestre del embarazo.",
 criteria=["Reconoce las características del segundo trimestre","Describe las características del tercer trimestre","Presenta información sintetizada con lenguaje científico"],
 activities=[A("individual","📏 La tirita de 7 cm","Recorta la tirita de 7 cm de tu ficha: ¿qué crees que representa? Mira el video y completa la tabla del segundo trimestre (semanas 14, 16, 20, 24 y 28) y los síntomas que podría tener la mamá."),
  A("group","🤰 El viaje de 9 meses","En grupo, completen los cambios del bebé en las semanas 28, 32 y 36, y los cambios que presenta la mamá en el tercer trimestre."+DUA),
  A("individual","📝 Para mi póster: segundo y tercer trimestre","Escribe 3 datos que te sorprendieron del desarrollo del bebé, usando números: «En la semana ___ el bebé ___».")],
 qs=[Q("¿Qué representa la tirita de 7 cm?",["El tamaño del feto al inicio del segundo trimestre","El tamaño del óvulo","La duración del embarazo"],0,"Al inicio del segundo trimestre el feto mide unos 7 cm."),
  Q("¿En qué trimestre el bebé empieza a moverse y oír?",["Primer trimestre","Segundo trimestre","Después del parto"],1,"Durante el segundo trimestre el bebé se mueve y puede oír."),
  Q("Cerca de la semana 36, ¿cómo suele ubicarse el bebé?",["Sentado","De costado sin moverse","Con la cabeza hacia abajo"],2,"Se ubica con la cabeza hacia abajo, preparándose para el parto."),
  Q("¿Cuánto pesa aproximadamente el bebé al final del embarazo?",["Cerca de 3 kilos","Cerca de 30 kilos","Cerca de 300 gramos"],0,"Al final del tercer trimestre pesa alrededor de 3 kg."),
  Q("¿Qué cambio puede presentar la mamá durante el embarazo?",["Deja de respirar","Sube de peso y puede tener hinchazón en las piernas","Crece de estatura"],1,"El cuerpo de la madre cambia para sostener al bebé.")]))
S.append(dict(meta="Elabora conclusiones sobre el uso de la tecnología asociada con el embarazo y el parto.",
 criteria=["Selecciona y contrasta información de fuentes confiables","Expresa opiniones fundamentadas en evidencia científica","Redacta conclusiones claras sobre el embarazo y el parto"],
 activities=[A("individual","🩺 ¿Cómo funciona una ecografía?","Mira el video de las ecografías y responde: ¿cómo funciona? ¿Para qué sirve en el primer, segundo y tercer trimestre? Luego lee la noticia del monitor fetal."),
  A("group","💬 Opinamos en dúo","En dúo, compartan su opinión sobre las tecnologías del embarazo y el parto. Revisen si usaron razones y fuentes, y denle a su compañero una sugerencia de mejora."+DUA),
  A("individual","📝 Para mi póster: mi opinión","Escribe tu opinión con el organizador: introducción, cómo funciona el monitor fetal, 2 razones para usarlo, 1 razón en contra o una precaución, y tu conclusión.")],
 qs=[Q("¿Qué usa la ecografía para formar imágenes del bebé?",["Ondas de ultrasonido","Rayos del sol","Electricidad fuerte"],0,"La ecografía usa ultrasonido, que no daña al bebé."),
  Q("¿Qué mide el monitor fetal?",["El peso de la mamá","Los latidos del bebé y las contracciones","La estatura del bebé"],1,"Mide la frecuencia cardíaca del bebé y las contracciones del útero."),
  Q("¿Qué es opinar con fundamento?",["Decir lo primero que pienso","Copiar la opinión de otro","Dar mi idea con razones y fuentes confiables"],2,"Una opinión fundamentada usa razones y evidencias."),
  Q("¿Para qué sirve una ecografía en el primer trimestre?",["Para identificar posibles riesgos en el bebé","Para saber su comida favorita","Para cambiar su tamaño"],0,"En el primer trimestre ayuda a detectar riesgos tempranos."),
  Q("¿Cuál es una fuente confiable?",["Un rumor en redes sociales","Un artículo del Ministerio de Salud","Lo que dijo un desconocido"],1,"Las instituciones de salud son fuentes confiables.")]))
S.append(dict(meta="Elabora un póster en equipo reflexionando sobre lo aprendido en la unidad.",
 criteria=["Explica el saber científico de los sistemas reproductores y la fecundación","Explica cómo la tecnología interviene en el embarazo y el parto","Comunica con claridad, recursos visuales y lenguaje científico"],
 activities=[A("individual","✏️ Mi boceto","Revisa tus apuntes y glosario. Haz un boceto de lo que aportarás al póster: un título, un dibujo o esquema y 3 ideas clave con palabras científicas."),
  A("group","🖼️ Nuestros pósters científicos","En equipo, organicen el contenido, las imágenes y los responsables de los dos pósters: 1) sistemas reproductores y ciclo ovárico; 2) tecnologías del embarazo y el parto. Revísenlos con la lista de cotejo y preséntenlos en modo feria."+DUA),
  A("individual","🪞 Me evalúo","Revisa tu trabajo con la rúbrica: marca tu nivel (C, B, A o AD) y responde: ¿qué conocimiento es nuevo para ti? ¿Qué te gustaría investigar?")],
 qs=[Q("¿Qué debe tener un póster científico?",["Título, imágenes y textos breves con lenguaje científico","Solo dibujos sin texto","Textos muy largos sin imágenes"],0,"Un póster combina títulos, imágenes y textos cortos y claros."),
  Q("¿Qué tema va en el primer póster?",["Recetas de cocina","Los sistemas reproductores y el ciclo ovárico","Los planetas"],1,"El primer póster describe los sistemas reproductores y el ciclo ovárico."),
  Q("¿Qué tema va en el segundo póster?",["Deportes","Animales marinos","Tecnologías asociadas a la fecundación, el embarazo o el parto"],2,"El segundo póster trata sobre las tecnologías, como la ecografía."),
  Q("¿Para qué sirve hacer un boceto antes del póster?",["Para planificar el contenido y la distribución","Para gastar papel","Para no trabajar en equipo"],0,"El boceto ayuda a organizar las ideas antes de hacer la versión final."),
  Q("¿Qué significa «explicar» en la rúbrica?",["Nombrar sin dar razones","Dar razones y detallar cómo ocurre un proceso","Copiar un texto"],1,"Explicar es dar razones y detallar pasos o procesos.")]))
for s,rb in zip(S,["Explica el saber científico"]*5+["Explica las consecuencias y opina sobre la tecnología","Todos los criterios (póster final)"]):
  s["rubric"]=rb
  assert len(s["qs"])==5 and len(s["activities"])==3
  s["ticket"]={"questions":s.pop("qs")};s.setdefault("flipped",{"enabled":False,"title":"","desc":"","file":""});s.setdefault("flipped2",{"enabled":False,"title":"","desc":"","file":""});s["title"]=""
S[1]["flipped"]={"enabled":True,"title":"Para la siguiente sesión: sistema reproductor femenino","desc":"Mira el video del sistema reproductor femenino y completa en tu cuaderno el cuadro de ovario, trompas de Falopio, útero y vagina: características, funciones y un dato interesante.","file":""}
S[2]["flipped2"]={"enabled":True,"title":"Para hoy: sistema reproductor femenino","desc":"Trae tu cuadro del sistema reproductor femenino completado con el video (ovario, trompas de Falopio, útero y vagina).","file":""}
S[5]["flipped"]={"enabled":True,"title":"Para la siguiente sesión: materiales del póster","desc":"Por equipo traigan imágenes del sistema reproductor masculino y femenino, de la fecundación y las etapas del embarazo, y de tecnologías como la ecografía o el monitor fetal. También papelógrafo, plumones, tijeras y goma.","file":""}
S[6]["flipped2"]={"enabled":True,"title":"Para hoy: imágenes y materiales","desc":"Trae las imágenes y los materiales acordados con tu equipo para armar los pósters.","file":""}
json.dump({"unit":"unit8","title":"El sistema reproductor humano","product":"Dos pósters científicos: 1) los sistemas reproductores y el ciclo ovárico; 2) tecnologías asociadas a la fecundación, el embarazo y el parto","sessions":S},open('/home/user/christian/packs/unidad8.json','w'),ensure_ascii=False,indent=1)
print('ok',len(S))
