import json
DUA=" Preséntenlo como más les guste: afiche, cómic, organizador, maqueta, dramatización, audio o video corto."
def Q(q,o,a,w):return{"q":q,"options":o,"answer":a,"why":w}
def A(m,t,d,f="",fi=""):return{"mode":m,"title":t,"desc":d,"ficha":fi,"file":f}
S=[]
S.append(dict(meta="Explicar qué es una enfermedad y diferenciar sus tipos a partir de una situación.",
 criteria=["Reconoce el concepto de enfermedad","Describe los tipos de enfermedades","Diferencia infecciosas y no infecciosas"],
 flipped2={"enabled":True,"title":"Para hoy: Microorganismos","desc":"Trae investigada la información sobre la levadura, las bacterias del yogur, la Salmonella y el moho del pan, con la ficha completa.","file":"f1"},
 flipped={"enabled":True,"title":"Para la siguiente sesión: materiales","desc":"Por grupo traigan: un vaso o frasco transparente, una regla y una cucharita. El profesor llevará la levadura y el azúcar.","file":""},
 activities=[A("individual","🤒 ¿Por qué me enfermé?","Lee los casos de niños que se enfermaron. Decide si cada enfermedad es infecciosa (se contagia) o no infecciosa y explica por qué. Pista: ¿se pasa de una persona a otra? ¿La causa un microorganismo?","f2","Ficha · Actividad 01"),
  A("group","🦠 Microorganismos: ¿amigos o enemigos?","En grupo, usen lo que investigaron antes de clase: completen la tabla de la levadura, las bacterias del yogur, la Salmonella y el moho del pan (grupo, qué hace y si nos ayuda o nos daña). Luego respondan: ¿todos los microorganismos del mismo grupo producen el mismo efecto?"+DUA,"f3","Ficha · Actividad 02"),
  A("individual","🍞 Mi microorganismo útil","Completa qué es una enfermedad, una enfermedad infecciosa y una no infecciosa. Luego escribe 3 o 4 líneas sobre la levadura: qué es y cómo nos ayuda. ¡Es el inicio de tu informe!")],
 qs=[Q("¿Qué es una enfermedad infecciosa?",["Una enfermedad causada por un microorganismo que puede contagiarse","Una enfermedad causada solo por dormir poco","Una enfermedad que solo tienen los adultos"],0,"Las enfermedades infecciosas las causan virus, bacterias, hongos o parásitos y pueden contagiarse."),
  Q("¿Cuál de estas enfermedades NO es infecciosa?",["La gripe","La diabetes","La varicela"],1,"La diabetes no se contagia: se relaciona con cómo el cuerpo usa el azúcar."),
  Q("El dengue se transmite por la picadura de un mosquito. ¿Qué tipo de enfermedad es?",["No infecciosa","Hereditaria","Infecciosa"],2,"El dengue lo causa un virus que el mosquito transmite, por eso es infecciosa."),
  Q("¿Qué microorganismo nos ayuda a preparar el pan?",["La levadura","La Salmonella","El virus de la gripe"],0,"La levadura es un hongo útil que hace crecer la masa del pan."),
  Q("¿Todos los microorganismos causan enfermedades?",["Sí, todos son dañinos","No, algunos son útiles, como los del yogur","Solo los que viven en el agua"],1,"Muchos microorganismos son útiles: nos ayudan a hacer yogur, pan y queso.")]))
S.append(dict(meta="Explica el fenómeno de la actividad de la levadura para delimitar una relación investigable.",
 criteria=["Observa los cambios","Registra medidas y descripciones","Describe factores que lo modifican"],
 activities=[A("individual","👀 Predigo y observo","Antes de empezar, predice qué cambio verás en la mezcla de agua, azúcar y levadura, y qué podrías medir con una regla. Usa tus sentidos: ¿qué ves, qué hueles, qué escuchas?"),
  A("group","🧪 Registramos los cambios","En grupo, observen la mezcla de levadura cada 5 minutos, desde 0 hasta 20 minutos. Midan la espuma con la regla, describan las burbujas y calculen cuánto cambió."+DUA),
  A("individual","📝 Explico el fenómeno","Lee sobre la fermentación y explica con tus datos: «La espuma cambió de ___ cm a ___ cm porque la levadura liberó ___». Luego escribe qué factor podrías cambiar y qué medirías.")],
 qs=[Q("¿Qué es la levadura?",["Un microorganismo formado por una sola célula","Una planta con hojas y raíces","Un tipo de azúcar"],0,"La levadura es un ser vivo microscópico: un hongo de una sola célula."),
  Q("¿Qué gas libera la levadura cuando se alimenta del azúcar?",["Oxígeno","Dióxido de carbono","Vapor de agua"],1,"Durante la fermentación la levadura produce dióxido de carbono."),
  Q("¿Por qué se formó espuma en la mezcla?",["Porque el agua se congeló","Porque el azúcar desapareció","Por las burbujas del gas que liberó la levadura"],2,"Las burbujas de dióxido de carbono forman la espuma."),
  Q("¿Con qué instrumento medimos la altura de la espuma?",["Con una regla","Con un termómetro","Con una balanza"],0,"La altura se mide con una regla, en centímetros."),
  Q("¿Qué factor podría cambiar la cantidad de espuma?",["El color del vaso","La temperatura del agua","El nombre del grupo"],1,"La temperatura del agua puede hacer que la levadura trabaje más o menos.")]))
S.append(dict(meta="Formula una pregunta que pueda responderse mediante una indagación experimental.",
 criteria=["Selecciona un factor","Selecciona un efecto","Relaciona causa y efecto"],
 activities=[A("individual","❓ ¿Se puede investigar?","Lee varias preguntas y marca cuáles se pueden responder con un experimento. Pista: ¿hay algo que puedo cambiar? ¿Hay algo que puedo medir? Si las dos respuestas son «sí», ¡se puede investigar!","",""),
  A("group","🃏 Fábrica de preguntas","En grupo, comparen sus preguntas individuales y escriban la pregunta inicial del equipo. Otro equipo les da una estrella (algo logrado) y una escalera (algo por mejorar), y con eso escriben la pregunta mejorada."+DUA,"",""),
  A("individual","✏️ Mi pregunta científica","Escribe tu pregunta de indagación. Subraya en azul lo que vas a cambiar (causa) y en rojo lo que vas a medir (efecto). ⭐ Reto: inventa otra pregunta sobre algo más que se pueda probar.")],
 qs=[Q("En nuestra indagación, ¿qué vamos a cambiar a propósito?",["La temperatura del agua","El color del recipiente","La marca del azúcar"],0,"Probaremos agua a 15 °C, 25 °C y 35 °C."),
  Q("¿Qué efecto vamos a medir?",["El sabor de la mezcla","La altura de la espuma","El olor de la levadura"],1,"El efecto es lo que observamos y medimos con un instrumento."),
  Q("¿Cuál es una pregunta que SÍ se puede investigar con un experimento?",["¿Te gusta el pan?","¿La levadura es bonita?","¿Cómo influye la temperatura del agua en la altura de la espuma?"],2,"Tiene una causa que podemos cambiar y un efecto que podemos medir."),
  Q("En «¿Cómo influye la temperatura en la espuma?», ¿cuál es la causa?",["La temperatura","La espuma","El vaso"],0,"La causa es lo que cambiamos: la temperatura."),
  Q("¿Qué palabras ayudan a escribir una pregunta de causa y efecto?",["«¿Te gusta…?»","«¿Cómo influye… en…?»","«¿Qué color…?»"],1,"«¿Cómo influye ___ en ___?» une la causa con el efecto.")]))
S.append(dict(meta="Elabora una hipótesis causal y fundamentada para la indagación.",
 criteria=["Selecciona información científica","Relaciona causa y efecto","Predice el resultado"],
 activities=[A("individual","📖 La levadura y la temperatura","Copia la pregunta de tu equipo y lee cómo reacciona la levadura al frío, a lo tibio y al calor. Elige 2 ideas científicas que te ayuden a predecir y explica por qué las elegiste."),
  A("group","🎲 La apuesta científica","En grupo, ordenen las temperaturas de mayor a menor espuma y defiendan su apuesta con lo que leyeron. Escriban la hipótesis inicial del equipo, reciban una estrella y una escalera de otro equipo y escriban la hipótesis mejorada."+DUA),
  A("individual","💡 Mi hipótesis","Escribe tu hipótesis: «Si el agua está a ___ (causa), entonces la espuma ___ (efecto), porque la levadura ___ (razón científica)». Usa palabras como fermentación y dióxido de carbono.")],
 qs=[Q("¿Qué es una hipótesis?",["Una respuesta posible a la pregunta, que luego comprobamos","Un dibujo del experimento","La lista de materiales"],0,"La hipótesis es nuestra predicción fundamentada, que el experimento confirma o no."),
  Q("¿Cuál está escrita como hipótesis?",["Me gusta la levadura","Si el agua está tibia, entonces habrá más espuma, porque la levadura se activa","La espuma es blanca"],1,"Tiene la estructura «Si… entonces… porque…»."),
  Q("¿Qué le pasa a la levadura con el agua muy fría?",["Trabaja más rápido","Se muere al instante","Trabaja más lento"],2,"Con el frío la levadura se vuelve lenta y produce menos gas."),
  Q("En una hipótesis, la parte «porque…» sirve para…",["Dar la razón científica","Decir el color de la espuma","Nombrar a los integrantes"],0,"El «porque» fundamenta la predicción con información científica."),
  Q("¿Qué produce la levadura que hace subir la espuma?",["Agua","Dióxido de carbono","Sal"],1,"El dióxido de carbono forma burbujas y la espuma sube.")]))
S.append(dict(meta="Determina las variables necesarias para comprobar la hipótesis.",
 criteria=["Identifica qué cambia y qué mide","Define cómo medirá y en qué unidades","Establece lo que queda igual"],
 activities=[A("individual","🔎 ¿Es una prueba justa?","Un equipo preparó dos mezclas cambiando la temperatura, el agua, el azúcar y la levadura a la vez. ¿Podrían saber si la espuma cambió solo por la temperatura? Explica por qué."),
  A("group","🔧 Las reglas de nuestro experimento","En grupo, completen qué variable modificarán y qué variable medirán (con instrumento y unidad), y la tabla de factores que mantendrán iguales: agua, azúcar, levadura, recipiente, forma de mezclar, tiempo y forma de medir."+DUA),
  A("individual","📋 Mis variables","Completa tus variables: qué cambiaremos, qué mediremos y qué mantendremos igual. Explica por qué algunas cosas deben quedar igual y revisa tu trabajo con el semáforo de criterios.")],
 qs=[Q("¿Cuál es la variable que cambiamos a propósito?",["La temperatura del agua","La altura de la espuma","La cantidad de levadura"],0,"Es la variable independiente: 15 °C, 25 °C y 35 °C."),
  Q("¿Cuál es la variable que medimos?",["El tipo de vaso","La altura de la espuma","La hora del día"],1,"Es la variable dependiente: la medimos en centímetros."),
  Q("¿Por qué usamos la misma cantidad de azúcar en todos los vasos?",["Porque sobra azúcar","Para que el vaso pese igual","Para que solo la temperatura sea la diferencia"],2,"Si todo lo demás queda igual, la prueba es justa."),
  Q("¿En qué unidad medimos la temperatura?",["Grados Celsius (°C)","Centímetros (cm)","Gramos (g)"],0,"La temperatura se mide en °C con un termómetro."),
  Q("¿Cuál de estas es una variable que debe quedar igual?",["La temperatura","La cantidad de agua","La altura de la espuma"],1,"La cantidad de agua se controla: es igual en todos los vasos.")]))
S.append(dict(meta="Diseña una estrategia experimental válida y segura para comprobar la hipótesis.",
 criteria=["Describe materiales y seguridad","Organiza acciones en secuencia","Diseña su tabla de registro"],
 activities=[A("individual","🧩 Pasos en orden","Ordena los pasos para preparar un refresco usando «primero, luego, después, finalmente». Así practicas cómo escribir un procedimiento."),
  A("group","🗺️ Nuestro plan de experimento","En grupo, completen la tabla de materiales (cantidad y para qué sirven), las medidas de seguridad y los pasos en orden, y presenten su diseño de indagación en un papelote. Luego revisen el diseño de otro grupo con «Veo, pregunto, sugiero»."+DUA),
  A("individual","📊 Mi tabla de registro","Diseña tu tabla de registro con las temperaturas (15, 25 y 35 °C), las 3 repeticiones y los tiempos (0 a 20 minutos). Luego comprueba tu diseño con la lista de cotejo.")],
 qs=[Q("¿Por qué repetimos 3 veces cada temperatura?",["Para que los resultados sean más confiables","Para gastar más levadura","Porque es divertido"],0,"Repetir ayuda a detectar errores y confiar en los datos."),
  Q("¿Cuál es una medida de seguridad de nuestro experimento?",["Probar la mezcla para ver su sabor","Usar agua a 35 °C como máximo y no consumir las mezclas","Usar agua hirviendo"],1,"Usamos agua hasta 35 °C y nunca probamos las mezclas."),
  Q("¿Para qué sirve el termómetro en nuestro experimento?",["Para medir la espuma","Para contar el tiempo","Para medir la temperatura del agua"],2,"El termómetro nos dice si el agua está a 15, 25 o 35 °C."),
  Q("¿Qué palabra usamos para el primer paso de un procedimiento?",["Primero","Finalmente","Además"],0,"Los conectores ayudan a ordenar los pasos."),
  Q("¿Qué debe tener nuestra tabla de registro?",["Solo dibujos","Temperaturas, repeticiones y altura de la espuma","Los nombres de las mascotas"],1,"La tabla organiza todos los datos que vamos a medir.")]))
S.append(dict(meta="Ejecuta el procedimiento experimental controlando las condiciones establecidas.",
 criteria=["Sigue el procedimiento con seguridad","Controla las condiciones","Registra los datos de todas las repeticiones"],
 activities=[A("individual","🦺 Listos y seguros","Elige tu rol en el grupo (medidor, cronometrista, anotador o vigía de seguridad), revisa la lista de seguridad y comprueba las cantidades de agua, azúcar y levadura de cada recipiente."),
  A("group","⏱️ Realizamos el experimento","En grupo, realicen el experimento con las 3 temperaturas, 3 veces cada una. Midan la espuma a los 20 minutos, anoten las incidencias y tomen fotos como evidencia."),
  A("individual","📓 Mi diario del experimento","Anota algo que observaste (burbujas, olor, color) y una dificultad que tuviste: «Observé que ___. Lo más difícil fue ___». Luego escribe la observación que recibió tu grupo y el ajuste que hicieron.")],
 qs=[Q("¿Qué hace el cronometrista del grupo?",["Controla el tiempo","Mide la temperatura","Lava los vasos"],0,"El cronometrista avisa cuándo medir, por ejemplo a los 20 minutos."),
  Q("Si a un vaso le echamos más levadura por error, ¿qué pasa?",["No importa","La prueba ya no es justa","La espuma será azul"],1,"Cambió una variable que debía quedar igual."),
  Q("¿Por qué anotamos los datos apenas medimos?",["Para terminar rápido","Para decorar la tabla","Para no olvidar ni confundir las medidas"],2,"Registrar al momento evita errores."),
  Q("¿Qué es una observación cualitativa?",["Describir burbujas, olor o color","Medir en centímetros","Contar los minutos"],0,"Lo cualitativo se describe con palabras; lo cuantitativo, con números."),
  Q("¿Para qué anotamos las dificultades?",["Para quejarnos","Para proponer mejoras en la conclusión","Para no hacer el informe"],1,"Las dificultades nos ayudan a mejorar el experimento.")]))
S.append(dict(meta="Procesa los datos experimentales para facilitar su comparación.",
 criteria=["Verifica registros completos","Calcula el promedio","Organiza en tabla y gráfico"],
 activities=[A("individual","🧮 Verifico y saco el promedio","Revisa con la lista de cotejo que tus registros estén completos. Calcula el promedio de cada temperatura: 1) suma las 3 medidas, 2) divide entre 3, 3) escribe la unidad (cm)."),
  A("group","📈 Nuestros datos hablan","En grupo, construyan un gráfico de barras con los promedios: escriban el título y el nombre de los ejes, y expliquen por qué eligieron ese gráfico."+DUA),
  A("individual","📊 Mi tabla y mi gráfico","Pasa tu tabla y tu gráfico al informe, con título, nombre de los ejes y unidades (cm, °C). ⭐ Reto: explica por qué elegiste ese tipo de gráfico.")],
 qs=[Q("Las medidas fueron 4 cm, 5 cm y 6 cm. ¿Cuál es el promedio?",["5 cm","15 cm","6 cm"],0,"4 + 5 + 6 = 15, y 15 ÷ 3 = 5 cm."),
  Q("¿Qué gráfico sirve mejor para comparar la espuma en 3 temperaturas?",["Un gráfico de líneas del clima","Un gráfico de barras","Un dibujo libre"],1,"Las barras permiten comparar cantidades entre grupos."),
  Q("¿Qué debe tener siempre un gráfico?",["Muchos colores","Stickers","Título, ejes y unidades"],2,"Sin título ni unidades no se entiende qué muestra."),
  Q("¿Para qué calculamos el promedio?",["Para tener un solo valor representativo de las repeticiones","Para borrar datos","Para que la tabla sea más larga"],0,"El promedio resume las 3 repeticiones en un valor."),
  Q("¿Qué es una tabla de doble entrada?",["Una tabla con una sola columna","Una tabla que cruza filas y columnas, como temperatura y repetición","Una lista de materiales"],1,"Cruza dos datos a la vez: filas y columnas.")]))
S.append(dict(meta="Interpreta los datos para establecer la relación entre la temperatura y la actividad de la levadura.",
 criteria=["Compara los resultados","Identifica patrones y datos inusuales","Explica qué muestran tabla y gráfico"],
 activities=[A("individual","🔍 Leo mis resultados","Anota la altura promedio de cada temperatura y responde: ¿con cuál hubo más espuma? ¿Con cuál menos? ¿Cuánta diferencia hay entre ellas?"),
  A("group","🖼️ Galería científica","En grupo, visiten los gráficos de los demás. Busquen qué se repite en todos y qué fue diferente: «En todos se repite ___. Lo diferente fue ___». Comenten por qué pudo pasar."+DUA),
  A("individual","🗣️ Lo que muestran mis datos","Completa la tabla: resultado principal, comparación entre temperaturas, dos evidencias, el patrón y el límite de tus resultados. Luego escribe tu interpretación: «Cuando la temperatura fue ___, la espuma llegó a ___ cm. Esto muestra que ___».")],
 qs=[Q("Si la barra de 35 °C es la más alta, ¿qué significa?",["A 35 °C hubo más espuma","A 35 °C hubo menos espuma","La temperatura no importa"],0,"La barra más alta representa la mayor altura de espuma."),
  Q("¿Qué es un patrón en los datos?",["Un error","Algo que se repite en los resultados","Un dibujo bonito"],1,"Un patrón es una tendencia que se repite."),
  Q("Un grupo obtuvo un dato muy distinto a los demás. ¿Qué hacemos?",["Lo borramos sin decir nada","Lo copiamos de otro grupo","Lo revisamos y pensamos por qué pasó"],2,"Los datos inusuales se analizan; pueden indicar un error en el procedimiento."),
  Q("Si a más temperatura hay más espuma, ¿cuál es la relación?",["De causa y efecto","De colores","De tamaño del vaso"],0,"La temperatura (causa) influye en la espuma (efecto)."),
  Q("¿Qué debemos usar para explicar lo que muestra el gráfico?",["Solo opiniones","Los números y datos obtenidos","Lo que dijo un amigo"],1,"Las explicaciones científicas se apoyan en datos.")]))
S.append(dict(meta="Argumenta una conclusión mediante evidencias experimentales y conocimientos científicos.",
 criteria=["Selecciona información científica","Relaciona levadura, gas y espuma","Contrasta resultados con la hipótesis"],
 activities=[A("individual","📚 Lo que dice la ciencia","Lee sobre cómo la levadura produce gas al alimentarse del azúcar y completa la tabla: información científica, dato de tu experimento y cómo ayuda a explicar el resultado."),
  A("group","⚖️ Juicio a la hipótesis","En grupo, escriban qué predijo su hipótesis y qué mostraron los resultados. Decidan si fue respaldada, parcialmente respaldada o no respaldada, y escriban los datos que lo sustentan."+DUA),
  A("individual","🏁 Mi conclusión","Completa la tabla de tu conclusión (respuesta a la pregunta, decisión sobre la hipótesis, dos evidencias, explicación científica, dificultades y mejoras) y escríbela en tu informe.")],
 qs=[Q("¿Qué es una conclusión?",["La respuesta a la pregunta, apoyada en los datos","El título del informe","La lista de materiales"],0,"La conclusión responde la pregunta de indagación con evidencias."),
  Q("Si los datos NO coinciden con la hipótesis, entonces la hipótesis…",["Se cambia a escondidas","No es respaldada, y lo explicamos con los datos","Se borra del informe"],1,"Una hipótesis no respaldada también es un resultado científico valioso."),
  Q("¿Por qué la levadura produce más espuma con temperatura adecuada?",["Porque el agua se evapora","Porque el azúcar se vuelve sal","Porque se activa y libera más dióxido de carbono"],2,"Con una temperatura adecuada la fermentación es más rápida."),
  Q("¿Qué es una evidencia?",["Un dato u observación que apoya lo que decimos","Una opinión personal","Un adorno del informe"],0,"Las evidencias son datos medidos u observados."),
  Q("En la conclusión también escribimos…",["Nuestro juego favorito","Las dificultades y cómo mejorar el experimento","El precio de la levadura"],1,"Mencionar dificultades y mejoras es parte de una buena conclusión.")]))
S.append(dict(meta="Sustenta decisiones de indagación y conclusiones ante una nueva situación experimental.",
 criteria=["Organiza pregunta, hipótesis y variables","Analiza datos en tabla o gráfico","Sustenta conclusiones y propone mejoras"],
 activities=[A("individual","🆕 Un nuevo misterio","Lee una situación nueva: la levadura con distintas cantidades de azúcar. Identifica la pregunta, la hipótesis, qué se cambia, qué se mide y qué queda igual."),
  A("group","🕵️ Científicos en acción","En grupo, calculen los promedios de la tabla del nuevo misterio, busquen el dato inusual, escriban una conclusión y propongan 2 mejoras al procedimiento."+DUA),
  A("individual","🪞 Me evalúo","Revisa tu informe con la rúbrica. Marca tu nivel en cada criterio (C, B, A o AD) y escribe una meta para mejorar.")],
 qs=[Q("Si ahora cambiamos la cantidad de azúcar, ¿cuál es la causa?",["La cantidad de azúcar","La altura de la espuma","El termómetro"],0,"Lo que cambiamos a propósito es la causa."),
  Q("En ese nuevo experimento, ¿qué debe quedar igual?",["La cantidad de azúcar","La temperatura del agua","La altura de la espuma"],1,"Si probamos el azúcar, la temperatura debe ser igual en todos los vasos."),
  Q("¿Cuál es una buena mejora para un experimento?",["Hacer una sola medición","No anotar los datos","Aumentar las repeticiones y medir con cuidado"],2,"Más repeticiones y mediciones cuidadosas dan datos más confiables."),
  Q("¿Qué parte del informe responde la pregunta de indagación?",["La conclusión","La lista de materiales","El título"],0,"La conclusión responde la pregunta usando los datos."),
  Q("¿Para qué sirve la rúbrica?",["Para copiar respuestas","Para saber qué logré y qué puedo mejorar","Para decorar el informe"],1,"La rúbrica muestra los niveles de logro de cada criterio.")]))
S[5]["flipped"]={"enabled":True,"title":"Para la siguiente sesión: materiales del experimento","desc":"Por grupo traigan: 3 vasos o frascos transparentes iguales, una regla, una cucharita, etiquetas o cinta para rotular y papel toalla. El profesor llevará la levadura, el azúcar, el termómetro y el agua a 15, 25 y 35 °C.","file":""}
S[6]["flipped2"]={"enabled":True,"title":"Para hoy: repasa tu diseño","desc":"Trae tu ficha de la sesión anterior con el procedimiento, la tabla de registro y las medidas de seguridad.","file":""}
for s,rb in zip(S,["Describe hechos y fenómenos","Describe hechos y fenómenos","Formula pregunta de indagación","Elabora hipótesis","Verificación mediante el diseño","Verificación mediante el diseño","Verificación mediante el diseño (puesta en práctica)","Organiza y procesa datos","Organiza y procesa datos","Elabora y comunica conclusiones","Todos los criterios (evaluación final)"]):
  s["rubric"]=rb
  assert len(s["qs"])==5 and len(s["activities"])==3
  s["ticket"]={"questions":s.pop("qs")}
  s.setdefault("flipped",{"enabled":False,"title":"","desc":"","file":""});s.setdefault("flipped2",{"enabled":False,"title":"","desc":"","file":""})
  s["title"]=""
json.dump({"unit":"unit7","title":"Microorganismos en acción","product":"Informe de indagación: ¿Cómo influye la temperatura del agua en la actividad de la levadura?","sessions":S},open('/home/user/christian/packs/unidad7.json','w'),ensure_ascii=False,indent=1)
print("ok",len(S))
