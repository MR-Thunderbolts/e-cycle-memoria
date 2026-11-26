<!--CH resumen|00|Resumen|Abstract e introducción-->

## Resumen {#resumen}

En Chile, los residuos electrónicos de los hogares casi no llegan al circuito formal. En 2017, el canal doméstico aportó solo el 5,5 % de lo recolectado (313 de 5.677 toneladas) y apenas el 3,4 % de los RAEE generados se trató formalmente ([MMA, Fundación Chile y E2BIZ, 2019](#ref-mma2)). Además, el 94 % de la población se declara poco o nada informada sobre la Ley REP ([IPP UNAB, 2024](#ref-unab)).

e-cycle es una plataforma web que conecta a los hogares con los operadores que recolectan y valorizan residuos de aparatos eléctricos y electrónicos (RAEE). Su promesa combina clasificación, trazabilidad y educación. El proyecto se desarrolló con el Doble Diamante y un enfoque sistémico.

Hoy existe un MVP de la capa ciudadana publicado en Vercel: es solo frontend, muestra 12 puntos reales de recolección en cinco comunas del sur de la Región Metropolitana y mantiene de ejemplo solo los comercios del canje. Se evaluó con usuarios en dos ciclos —un focus group presencial con cerca de 15 estudiantes de INACAP y un test no moderado en Maze con 12 personas— y con una revisión experta de diseño de producto. Las capas de Gestión y Conductor existen como diseño en Figma y quedan como proyección: no hubo conversación con un operador, por lo que la tesis B2B se declara no validada.

<p class="todo">Pendiente: reescribir el resumen con la voz del autor al cerrar el capítulo 6.</p>

## Abstract {#abstract}

In Chile, household e-waste rarely reaches the formal system. In 2017 the residential channel accounted for only 5.5% of the e-waste collected (313 of 5,677 tonnes), and just 3.4% of the e-waste generated was formally treated (MMA, Fundación Chile & E2BIZ, 2019). In addition, 94% of the population reports knowing little or nothing about Chile's Extended Producer Responsibility law (IPP UNAB, 2024). e-cycle is a web platform that connects households with the operators that collect and recover waste electrical and electronic equipment (WEEE), built around classification, traceability and education. The citizen layer exists as a frontend-only MVP with sample data, tested with users in two cycles (an in-person focus group with about 15 students and an unmoderated Maze study with 12 participants) and reviewed by a senior product designer. The Management and Driver layers remain Figma designs; with no operator conversation, the B2B thesis is declared unvalidated.

## Introducción {#introduccion}

Esta Memoria documenta el desarrollo de e-cycle, Proyecto de Título del autor en la carrera de Diseño Digital Profesional de INACAP. El proyecto aborda un problema concreto: los aparatos eléctricos y electrónicos en desuso se quedan guardados en los hogares y casi no llegan al circuito formal de reciclaje y reutilización, justo cuando el DS 22/2025 fija metas de recolección que se exigirán desde mayo de 2028.

La idea nació en 2025 y se retomó en 2026. En el camino pasó de ser una aplicación pensada solo para el ciudadano a una plataforma para los operadores que recolectan y valorizan residuos electrónicos, con una capa ciudadana que es hoy la única construida en código.

El documento se organiza en ocho capítulos. El primero delimita el tema, el caso, el problema, los objetivos y la metodología. El segundo reúne los antecedentes normativos, el ecosistema de actores y el estado del arte, y el diagnóstico general resume las necesidades del ciudadano y los análisis FODA y PESTEL. El tercero presenta el marco teórico y el cuarto, los instrumentos de investigación y su análisis. El quinto desarrolla la propuesta de diseño, desde los objetivos hasta la evaluación con usuarios, el presupuesto y la gestión del proyecto. Los capítulos 6 a 8 recogen las conclusiones, la bibliografía y los anexos.

<!--CH c1|01|Delimitación de la investigación|Qué problema se estudia, dónde, con qué pregunta y con qué método.-->

## 1.1 Tema {#s1-1}

Gestión de los residuos de aparatos eléctricos y electrónicos (RAEE) de origen doméstico en la Región Metropolitana, en el marco de la [Ley 20.920](#ref-ley) (Ley REP) y del [Decreto Supremo N.º 22 de 2025](#ref-ds22).

La solución es una plataforma web de clasificación, trazabilidad y educación. Quien paga es la empresa operadora que recolecta y valoriza RAEE; quien usa la capa ciudadana es el hogar que tiene aparatos en desuso.

## 1.2 Caso de investigación {#s1-2}

**Caso (11/10/2026):** Pañiwe, un operador que recolecta y valoriza RAEE, en comunas del sur de Santiago. **Acotación (21/10/2026):** el caso se acota a **La Florida**, más la comunidad de **INACAP** como segundo grupo de usuarios, porque el autor no tenía contactos suficientes para trabajar en tres comunas.

**Por qué La Florida.** En la visita a terreno del 20/10/2026 se constató que el punto limpio cercano al domicilio del autor ya no estaba; según los vecinos, lo retiraron unas dos semanas antes y sin aviso. En la junta de vecinos se informó que los contenedores de RAEE reciben cualquier tipo de residuo. <span class="chip c-int">Relato de vecinos</span>

El 17/11/2026, Valeria Gutiérrez, de la Dirección de Medio Ambiente, Aseo, Ornato y Operaciones de la Municipalidad, confirmó ese problema: en los puntos fijos llegan otros desechos porque los vecinos ven un contenedor y creen que es para basura. La Municipalidad trabaja solo con Pañiwe para retirar RAEE. <span class="chip c-ver">Entrevista aplicada</span>

## 1.3 Problema de investigación {#s1-3}

<!--LADDER-->

**Pregunta de investigación.** ¿Cómo puede una plataforma web de clasificación y trazabilidad facilitar que los RAEE de los hogares del sur de la Región Metropolitana ingresen al circuito formal de gestión y contribuyan al cumplimiento de las metas del DS 22?


## 1.4 Fundamentación de la oportunidad {#s1-4}

**Motivación.** El proyecto nace en 2025 como una idea del autor y se retoma en 2026 como Proyecto de Título. La motivación es también personal: la convicción de que la gestión responsable de los dispositivos electrónicos impacta en la relación entre las personas, la economía y el medioambiente.

<!--GAP-->

<!--FIGS-->

**Innovación.** Se revisaron siete casos (Reciclapp, Vínculo Verde, ReSimple, RLG/Reconomy, Karo Sambhav, Muta y Back Market). Ninguno cubre a la vez la clasificación por categoría legal del DS 22, la trazabilidad por aparato y una capa ciudadana.

**Viabilidad.** *Legal:* e-cycle no puede ser Sistema de Gestión, porque el Art. 10 de la Ley REP lo reserva a los productores; se posiciona como proveedor de software para los operadores. *Técnica:* existe un MVP de la capa ciudadana publicado y probado con usuarios. *Económica:* depende de validar la tarifa con un operador (ver 5.9).

## 1.5 Objetivo general {#s1-5}

Diseñar una plataforma web de clasificación y trazabilidad de aparatos eléctricos y electrónicos en desuso que conecte a los hogares del sur de la Región Metropolitana con un operador de gestión de RAEE, para que esos aparatos dejen de hibernar en las casas y entren al circuito formal de reutilización y reciclaje.

## 1.6 Objetivos específicos {#s1-6}

1. **Identificar** las barreras y necesidades de los hogares del sur de la RM y del operador de gestión, mediante encuesta, entrevistas y análisis de antecedentes.
2. **Diseñar** el sistema en tres interfaces (ciudadano, conductor y panel del operador), con sus flujos de clasificación, retiro y trazabilidad por aparato.
3. **Evaluar** los prototipos con usuarios y con expertos, para verificar que el recorrido ciudadano se completa sin ayuda.

**Resultado del corte del 2 de noviembre (H1).** No hubo conversación con un operador: el correo exploratorio a Pañiwe (29/09) y el contacto directo obtenido por la Municipalidad (17/11) siguen sin respuesta. Según el criterio fijado de antemano, la tesis B2B se declara **no validada**. Como este es un proyecto académico, el alcance no cambia: la capa ciudadana es la que se construye y evalúa, y Gestión y Conductor se mantienen como **proyección diseñada** en Figma. <span class="chip c-pro">Proyección</span>

## 1.7 Metodología de diseño {#s1-7}

El proyecto sigue el **Doble Diamante** con **enfoque sistémico**. El enfoque sistémico explica por qué el problema no se resuelve tocando un solo eslabón: hogares, operadores, sistema de gestión y productores dependen unos de otros.

<!--DIAMOND-->

<!--CH c2|02|Antecedentes generales|El marco legal que fija fechas, los actores del sistema y lo que ya existe.-->

## 2.1 Marco normativo chileno {#s2-1}

La [Ley 20.920](#ref-ley) obliga a los productores de productos prioritarios, entre ellos los aparatos eléctricos y electrónicos, a financiar y organizar la gestión de sus residuos. El [DS 22/2025](#ref-ds22) fija las metas de recolección y valorización: se publicó en el Diario Oficial el 07/05/2026 y sus metas se exigen desde el **07/05/2028**. La meta general sube del 3 % en el primer año al 45 % desde el décimo.

<!--TIMELINE-->

- **Art. 10.** El Sistema de Gestión lo constituyen los productores obligados: e-cycle no puede ser uno.
- **Art. 29.** Retiro en retail de más de 400 m², hoy a través de TRAEE.
- **Art. 32.** Recolección domiciliaria coordinada por un GRANSIC: el horizonte hacia 2028.
- **Art. 36.** Gestor registrado: posible evolución futura.

**Posición del proyecto.** e-cycle es un "sistema operativo de operadores": software de gestión y trazabilidad para quienes recolectan y valorizan RAEE. La ventana 2026–2028 permite madurar el producto antes de que el cumplimiento del canal doméstico sea exigible. Según la Municipalidad de La Florida, Pañiwe participa en la mesa de trabajo del decreto y el orden entre actores llegará con el DS 22, porque hoy "no hay incentivo". <span class="chip c-int">Según la entrevistada</span>

<p class="todo">Pendiente: tabla de metas por categoría desde el texto oficial del DS 22.</p>

## 2.2 Ecosistema y mapa de actores {#s2-2}

<!--ACTORS-->

Pañiwe es el único operador con que trabaja la Municipalidad de La Florida y la alianza ancla del proyecto, pero no ha respondido. Midas Chile (valorizador catalogado por el MMA, certificado R2v3) y Chilenter (reacondicionamiento) están aguas abajo. TRAEE es el sistema de gestión de referencia y un posible financiador futuro. Reciclapp y Redciclach son competencia y referencia en el espacio ciudadano; ReSimple gestiona envases y sirve solo como modelo de negocio.


## 2.3 Estado del arte {#s2-3}

Se revisaron siete casos en septiembre de 2026 ([Anexo A](#anexos)). Dejan dos lecciones:

1. **El modelo solo ciudadano no se sostiene en Chile.** El hogar no paga por reciclar; el ingreso tiene que venir del operador o del productor obligado.
2. **Escala lo que se vuelve obligatorio.** ReSimple cobra una licencia de software más un fee por tonelada validada ante la autoridad.

En el espacio ciudadano, Reciclapp retira RAEE a domicilio y Redciclach opera contenedores inteligentes. Ambos resuelven la entrega; ninguno conecta lo que entrega el ciudadano con la información que el operador necesita para cumplir la REP. <span class="chip c-int">Interpretación del autor</span>

**Tendencias.** Cuatro tendencias empujan hacia un software de trazabilidad pagado por el operador: la obligación legal con fecha (DS 22, 2028), el canal domiciliario vacío (5,5 %), el software cobrado al obligado (ReSimple) y la trazabilidad e incentivos digitales ([Mugerwa et al., 2025](#ref-mugerwa)).

<!--CH dg|DG|Diagnóstico general|Necesidades del ciudadano y el estado del proyecto frente a su entorno.-->

## Necesidades del ciudadano {#dg-1}

| Necesidad | Prioridad | Cómo responde el MVP | Estado |
|---|---|---|---|
| Saber dónde llevar el aparato | Crítica | Mapa y lista de puntos, con la ficha de cada punto | Resuelta: 12 puntos reales en 5 comunas del sur |
| Un esfuerzo proporcional al objeto | Alta | Retiro a domicilio desde 5 kg | Probada: 91,7 % de éxito <span class="chip c-sup">Quién retira: supuesto</span> |
| Recibir algo a cambio | Alta | Beneficios y canje en comercios | Probada: 75 % de éxito, la tarea más débil |
| Ver que la acción tuvo efecto | Alta | Dato educativo al terminar el escaneo | Parcial: no hay seguimiento tras la entrega |
| No exponer datos personales | Crítica | Sin flujo de borrado seguro | Requerimiento futuro ([NIST SP 800-88](#ref-nist)) |

## FODA {#dg-2}

<!--FODA-->

## PESTEL {#dg-3}

| Dimensión | Análisis |
|---|---|
| Político-legal | Ley 20.920 y DS 22/2025, con metas exigibles desde el 07/05/2028 |
| Económico | Los modelos B2C puros no se sostienen; los SaaS cobrados a obligados sí escalan |
| Social | El 94 % se declara poco o nada informado sobre la Ley REP |
| Tecnológico | Trazabilidad con blockchain (Wee Chile) y sensores de llenado ya existen en el ecosistema |
| Ecológico | Solo el 3,4 % de los RAEE se trató formalmente en 2017 |
| Legal | e-cycle no puede ser Sistema de Gestión (Art. 10) |

<!--CH c3|03|Marco teórico|Las fuentes que explican el problema y respaldan las decisiones de diseño.-->

## 3.1 Magnitud del problema {#s3-1}

En 2022 el mundo generó 62 millones de toneladas de RAEE y solo el 22 % se recolectó y recicló formalmente ([ITU y UNITAR, 2024](#ref-gem)). En Chile, la generación se estimó en 9,6 kg por habitante en 2017, con una proyección de 13,9 kg en 2027 ([MMA, FCh y E2BIZ, 2019](#ref-mma1), p. 8).

## 3.2 El canal doméstico chileno {#s3-2}

En 2017, de las 5.677 toneladas recolectadas, 5.364 (94 %) provinieron de empresas e instituciones y solo 313 (5,5 %) fueron de origen residencial. Apenas el 3,4 % de los RAEE generados recibió tratamiento formal ([MMA, FCh y E2BIZ, 2019](#ref-mma2), pp. 9–10).

## 3.3 Responsabilidad Extendida del Productor {#s3-3}

La REP nace como un principio de política ambiental: extender la responsabilidad del fabricante a todo el ciclo de vida del producto, y en especial a su recuperación, reciclaje y disposición final después del consumo ([Lindhqvist, 2000](#ref-lindhqvist)). Chile la adopta con la [Ley 20.920](#ref-ley): los productores de aparatos eléctricos y electrónicos deben organizar y financiar la recolección y valorización por medio de sistemas de gestión, con metas que el [DS 22](#ref-ds22) hace exigibles desde 2028.

**Qué implica para el diseño.** Si la obligación y el costo recaen en el productor y en quien gestiona por él, el que paga no es el hogar. Por eso e-cycle se plantea como software para el operador y no cobra al ciudadano. Además, como la ley reserva el rol de sistema de gestión a los productores organizados (art. 10), e-cycle solo puede ser proveedor tecnológico. <span class="chip c-int">Lectura del autor</span>

## 3.4 Comportamiento: por qué no se recicla {#s3-4}

La teoría del comportamiento planificado explica la intención de actuar a partir de tres factores: la actitud hacia la conducta, la presión social percibida y el control que la persona cree tener para realizarla ([Ajzen, 1991](#ref-ajzen)). Un metaanálisis de 37 muestras (18.410 personas) sobre reciclaje de RAEE encontró que la actitud, la efectividad percibida de las políticas y la comodidad se asocian con la intención de reciclar con efectos muy grandes, y que la intención se traduce en conducta ([Puzzo y Prati, 2024](#ref-puzzo1)). Un estudio posterior de los mismos autores midió la comodidad de los centros de acopio (cercanía, disponibilidad y experiencia de uso) y encontró que influye directamente en la conducta de reciclaje ([Puzzo y Prati, 2025](#ref-puzzo2)).

La evidencia propia apunta en la misma dirección: el competidor real de e-cycle no es otro punto de reciclaje, sino la inercia de acumular. El 58,3 % guarda el aparato en un cajón y el 62,5 % de quienes no reciclaron no supo dónde llevarlo (encuesta exploratoria, n = 12, 2025). En Maze, 10 de 12 personas dejan de usar un aparato cada 2 o 3 años o casi nunca.

**Qué implica para el diseño.** La barrera no parece ser la actitud, sino el control percibido: no saber dónde ni cómo. Por eso e-cycle invierte en encontrar el punto, saber qué recibe y pedir retiro, más que en convencer. <span class="chip c-int">Lectura del autor</span>

## 3.5 Incentivos {#s3-5}

[Mugerwa, Chen, Kachule y Nakanwagi (2025)](#ref-mugerwa) encontraron que la motivación del usuario y la comodidad tecnológica determinan la adopción de una app de recompensas por reciclaje, y que los incentivos personalizados se asocian a mayor participación. e-cycle mantiene beneficios y canje, pero eliminó la gamificación: la motivación medida está dividida (41,7 % ambiental, 33,3 % por recompensa) y en Maze el beneficio concreto fue el segundo motivo de uso.

## 3.6 Economía circular: reparar antes de reciclar {#s3-6}

[Potting, Hekkert, Worrell y Hanemaaijer (2017)](#ref-potting) ordenan las estrategias de circularidad en una escalera de diez niveles, de R0 a R9: mientras más arriba, más se conserva el valor del producto y menor es el impacto ambiental. Reciclar (R8) y recuperar energía (R9) están abajo; reutilizar, reparar y restaurar están por encima.

<!--NINER-->

**Qué implica para el diseño.** La recolección de e-cycle opera en R8, pero los beneficios se orientan a reparar (descuentos en servicio técnico, cables y cargadores) y el destino aguas abajo incluye la reutilización (Chilenter). Así, el producto empuja hacia los niveles altos sin dejar de cumplir la meta de recolección. <span class="chip c-sup">Hipótesis · comercios de ejemplo</span>

## 3.7 Confianza y trazabilidad {#s3-7}

En un análisis conjunto con 184 residentes en China, la confianza en el reciclador fue el atributo más importante para decidir reciclar residuos electrónicos (27,8 % de importancia), por sobre la forma de compensación y el precio; la certificación y supervisión del gobierno fue el nivel preferido, por temor a la filtración de datos personales ([Wang, Wang y Chen, 2023](#ref-wang)). El contexto es distinto al chileno y la muestra es joven, pero coincide con lo observado aquí: en Maze, ver el impacto quedó último como motivo de uso, y aun así 6 de 10 respuestas abiertas piden saber qué pasó con el aparato después de entregarlo.

**Qué implica para el diseño.** La trazabilidad no se ofrece como un panel de impacto, sino como respuesta a una pregunta concreta: «¿qué pasó con mi aparato?». Es también el dato que el operador necesita para reportar sus metas. <span class="chip c-int">Lectura del autor</span>

## 3.8 Síntesis del marco teórico {#s3-8}

| Concepto | Fuente | Decisión de diseño |
|---|---|---|
| REP | Lindhqvist (2000); Ley 20.920 | Cobrar al operador, no al hogar; ser proveedor tecnológico, no sistema de gestión |
| Comportamiento planificado y comodidad | Ajzen (1991); Puzzo y Prati (2024, 2025) | Encontrar el punto, saber qué recibe y pedir retiro, antes que persuadir |
| Incentivos | Mugerwa et al. (2025) | Beneficio directo y canje; sin gamificación |
| Escalera de circularidad | Potting et al. (2017) | Beneficios orientados a reparar; reutilización aguas abajo |
| Confianza | Wang et al. (2023) | Trazabilidad como respuesta a «¿qué pasó con mi aparato?» |

<!--CH c4|04|Marco metodológico|Qué instrumentos se aplicaron, a quién, y qué dijeron.-->

## 4.1 Instrumentos aplicados {#s4-1}

| Instrumento | Fecha | Participantes | Qué aportó |
|---|---|---|---|
| Encuesta exploratoria a ciudadanos | 21/09/2025 | 12 | Barreras y motivaciones del hogar |
| Investigación documental y benchmark | Ago–sep 2026 | 7 casos | Antecedentes y estado del arte |
| Entrevista técnica a Daniel Muñoz | 15/09/2026 | Consultor técnico | Operación de retiro y trazabilidad |
| Visita a terreno en La Florida | 20/10/2026 | Vecinos y junta de vecinos | Puntos retirados y contenedores mal usados |
| Reunión con la Municipalidad de La Florida | 17/11/2026 | Valeria Gutiérrez | Cómo opera la recolección y contacto de Pañiwe |
| Sesión presencial de navegación con Daniel Muñoz | Nov. 2026 | Consultor técnico | Observación del uso del MVP (sin registro escrito) |
| Focus group sobre el MVP (ciclo 1) | 12/11/2026 | ~15 estudiantes INACAP | Fricciones del recorrido |
| Revisión experta (Diego Guajardo) | Nov. 2026 | Aliado del proyecto | Ajustes de retiro y beneficios |
| Test no moderado en Maze (ciclo 2) | 23–24/11/2026 | 12 | Éxito, abandono y motivos de uso |

Los guiones de entrevista para operadores (Pañiwe, Midas, TRAEE y Re-Use) se diseñaron pero no se aplicaron: el correo a Pañiwe del 29/09 y el contacto directo obtenido el 17/11 no tuvieron respuesta. Van en el [Anexo C](#anexos).

## 4.2 Análisis de datos {#s4-2}

**Encuesta exploratoria (2025, n = 12).** 7 de 12 guardan su último aparato en un cajón; 5 de 8 que no reciclaron no supieron dónde llevarlo; 4 de 8 mencionan distancia u horarios.

**Terreno y Municipalidad.** El problema del ciudadano es de acceso e información, y los puntos cambian sin aviso. La Municipalidad lo confirma: la difusión funciona en los eventos ("Recicla en tu sede", ferias), pero no en los puntos fijos, donde llegan otros desechos. Lo que Pañiwe no recibe, como los refrigeradores, queda sin derivación. Valeria no pidió ni sugirió una capa tecnológica: su criterio para elegir operador es la confiabilidad logística. <span class="chip c-int">Lectura del autor</span>

**Ciclos de testeo.** Ver resultados en [5.8](#s5-8).

**Limitaciones.** Muestras pequeñas y por conveniencia; ninguna entrevista aplicada a un operador; el MVP no tiene datos de uso real.

<!--CH c5|05|Propuesta de diseño|Del objetivo de diseño al prototipo: qué se construyó, cómo se probó y qué cambió.-->

## 5.1 Objetivos de diseño {#s5-1}

| Interfaz | Requerimiento | Objetivo de diseño |
|---|---|---|
| Ciudadano | Búsqueda de puntos | Encontrar un punto que reciba su aparato sin ayuda |
| Ciudadano | Clasificación funcional | Declarar el aparato en la categoría correcta |
| Ciudadano | Retiro a domicilio | Pedir un retiro sabiendo antes de avanzar si alcanza el mínimo |
| Ciudadano | Trazabilidad visible | Entender qué pasa con el aparato después de entregarlo |
| Conductor | Ruta y agendamiento por sector | <span class="chip c-pro">Proyección</span> |
| Operador | Segunda clasificación y reportes REP | <span class="chip c-pro">Proyección</span> |

## 5.2 Referentes de diseño {#s5-2}

Los referentes de diseño no vienen del reciclaje, sino de productos que ya resolvieron bien las mismas tareas:

<!--REFS-->


## 5.3 Propuesta de valor {#s5-3}

<div class="vp">
<div><span class="eyebrow">Clasificar</span><p>Que cada aparato llegue al destino correcto.</p><small>Hoy: pre-clasificación por categoría al declarar.</small></div>
<div><span class="eyebrow">Trazar</span><p>Que la persona sepa qué pasó con lo que entregó.</p><small>Hoy: no existe después de la entrega. Ciclo 3.</small></div>
<div><span class="eyebrow">Educar</span><p>Que entienda qué se puede reciclar y por qué.</p><small>Hoy: un dato educativo al terminar el escaneo.</small></div>
</div>

| Segmento | Propuesta | Evidencia |
|---|---|---|
| Operador de gestión (paga) | Información por aparato y categoría para operar y cumplir metas, rutas por sector y más volumen domiciliario | <span class="chip c-sup">Supuesto</span> sin conversación con un operador |
| Ciudadano (usa) | Saber dónde y qué entregar, pedir retiro y recibir un beneficio | Dos ciclos de testeo |

**Pertinencia.** Responde al problema real (el aparato se guarda por inercia y el retiro a domicilio fue el motivo de uso n.º 1); llena un vacío del estado del arte (nadie devuelve información sobre el destino, y 6 de 10 lo piden); y va con la tendencia que paga (la REP exige metas desde 2028 y el modelo que escala cobra software al obligado, no al hogar).

## 5.4 Escalabilidad y sostenibilidad {#s5-4}

<div class="cards4">
<div><h4>Retiro colectivo por sector</h4><p>El camión sale cuando el sector completa el peso mínimo (5 kg por solicitud): menos viajes por kilo recolectado.</p><span class="chip c-sup">Por validar con el operador</span></div>
<div><h4>Web app sin tienda de apps</h4><p>Un aparato se descarta cada 2 o 3 años: no se justifica una app instalada todo el año.</p><span class="chip c-ver">10 de 12 en Maze</span></div>
<div><h4>Reparar antes de reciclar</h4><p>Los beneficios son descuentos en reparación de celulares, cables o cargadores: alargan la vida útil antes del reciclaje. Servicios técnicos y tiendas podrían ser además puntos de recolección: los «embajadores e-cycle».</p><span class="chip c-sup">Hipótesis · comercios de ejemplo</span></div>
<div><h4>Que llegue al destino correcto</h4><p>La pre-clasificación por categoría evita mezclar residuos, el problema que la Municipalidad describe en los puntos fijos.</p><span class="chip c-ver">Terreno y Municipalidad</span></div>
</div>

**Escalabilidad.** El modelo escala por operador, no por usuario: cada operador que adopta el software suma sus puntos, campañas y comunas, y la capa ciudadana se replica sin costo marginal relevante. El horizonte es la recolección domiciliaria del Art. 32 hacia 2028. <span class="chip c-pro">Proyección</span>

<!--SIM-->

## 5.5 Conceptualización {#s5-5}

**Tres canales, un mismo recorrido.** El hogar busca y pide retiro en la web app; en el punto físico escanea el QR del contenedor y entrega; en el comercio adherido muestra su código y canjea. La cuenta se crea al final, con teléfono y SMS.

<!--USERFLOW-->

**Mapa de navegación.** Cuatro destinos en la barra inferior, cada uno con una sola tarea; la cuenta no es un destino, aparece cuando hace falta.

<!--NAVMAP-->

## 5.6 Desarrollo formal {#s5-6}

**Versión previa (septiembre de 2026, descartada).** Apostaba por la gamificación: niveles, multiplicadores, misiones e insignias. En la evaluación 2 de Diseño de Experiencia la recompensa del escaneo no se entendía; se simplificó a un beneficio directo y un dato educativo. En Maze, 1 de 12 pidió misiones y ligas: no se aplica, con fundamento.

**Sistema visual compartido.** Un paso, una decisión: cada pantalla pide una sola decisión con su dato clave a la vista. Plus Jakarta Sans e íconos Material Symbols Rounded; modos claro, oscuro y alto contraste; áreas táctiles de 44 × 44.

<p class="todo">Pendiente: capturas de la versión previa junto a la actual.</p>

## 5.7 Prototipo y ficha técnica {#s5-7}

<!--PROTO-->

| Ficha técnica | |
|---|---|
| Plataforma | Web app progresiva (PWA), sin tienda de apps; móvil primero y adaptada a escritorio |
| Stack | React 19 · TypeScript · Vite · Framer Motion 11 |
| Despliegue | Vercel · [e-cycle-tau.vercel.app](https://e-cycle-tau.vercel.app) |
| Destinos | Explorar (mapa y lista de puntos) · Retiro (4 pasos, gratis desde 5 kg) · Escanear (QR simulado) · Beneficios (saldo, canje e historial) |
| Cuenta | Opcional, con teléfono y código SMS; sin cuenta, los puntos se guardan 30 días en el navegador |
| Datos | 12 puntos reales de recolección en La Florida, Puente Alto, La Cisterna, El Bosque y San Bernardo. Los comercios del canje siguen siendo de ejemplo |
| Accesibilidad | Áreas táctiles de 44 × 44, respeta "reducir movimiento", textos en español de Chile |
| Diseño | Figma «E-Cycle V2.1» · Design System v2 |

## 5.8 Evaluación del proyecto {#s5-8}

La capa ciudadana se evaluó en dos ciclos con método y muestra distintos, con una revisión experta entre ellos.

<!--CYCLES-->

**Revisión experta.** Diego Guajardo (Senior Product Designer, LATAM Airlines; líder de Friends of Figma Chile) sugirió mostrar el peso estimado siempre, los beneficios desde el inicio, guardar la dirección y sopesar el impacto frente a la baja frecuencia de uso. Tres de sus cuatro sugerencias se aplicaron y se midieron en el ciclo 2.

<!--RESULTS-->

[Ver el reporte completo en Maze ↗](https://app.maze.co/report/e-cycle-Retiro-y-beneficios/xX_q6E2r_UXWw9OS7qy0dwz89ydK1-zR/intro){target=_blank}

### Iteración entre ciclos

<!--ITER-->

## 5.9 Presupuesto {#s5-9}

Etapa académica, precios de octubre de 2026 ([Vercel, 2026](#ref-vercel)). Dólares a $940 más 19 % de IVA.

| Partida | Monto mensual (CLP) |
|---|---|
| Claude Pro | $22.372 |
| Figma Professional | $22.372 |
| Vercel Pro | $22.372 |
| Alimentación, transporte y gastos comunes del autor | $145.000 |
| **Total directo** | **$212.116** |
| Horas del autor (16 h/semana a $5.307) | $367.658 |
| **Costo mensual total** | **$579.774** |

**Modelo de ingresos (proyección).** Licencia de software más un fee por tonelada certificada, como ReSimple. <span class="chip c-sup">Validar con un operador</span>

<!--BMC-->

## 5.10 Gestión del proyecto {#s5-10}

El plan de implementación (Unidad 2) organizó seis actividades y cuatro hitos. Así se cumplió:

<!--HITOS-->

**H1 · Corte B2B.** Sin conversación con un operador, la tesis B2B se declara no validada; el alcance académico no cambia. **H2.** El MVP y el test estuvieron listos para el focus group del 12/11; desde el 24/11 el MVP muestra puntos reales. **H3.** En vez de 5 sesiones individuales hubo dos ciclos: un focus group (12/11, ~15 personas) y Maze (23–24/11, n = 12), difundido con QR. **H4 · Marcha blanca.** Con vecinos y en INACAP sigue pendiente. <span class="chip c-pro">Pendiente</span>

<!--CH c6|06|Conclusiones|Lo que el proyecto demuestra, lo que no, y hacia dónde sigue.-->

## Conclusiones {#s6}

<p class="todo">Se redactan al cierre del ciclo 3, con la voz del autor.</p>

- La capa ciudadana tiene evidencia de dos ciclos de testeo: el retiro se completa (91,7 %) y el canje es el punto débil (75 %).
- El diferenciador de clasificación, trazabilidad y educación es defendible, pero hoy existe en una versión simple.
- La pertinencia para el operador sigue siendo un supuesto: no hubo conversación con Pañiwe.
- Proyecciones: recolección domiciliaria (Art. 32) hacia 2028, otros operadores de la RM y borrado seguro de datos.

<!--CH c7|07|Bibliografía|Solo fuentes verificadas, en formato APA.-->

## Referencias {#s7}

<ol class="refs">
<li id="ref-ajzen">Ajzen, I. (1991). The theory of planned behavior. <em>Organizational Behavior and Human Decision Processes, 50</em>(2), 179–211. <a href="https://doi.org/10.1016/0749-5978(91)90020-T">doi.org/10.1016/0749-5978(91)90020-T</a></li>
<li id="ref-coder">Coderhouse. (2026). <em>Sueldo de diseñador UX/UI en Chile</em>. <a href="https://www.coderhouse.com/cl/sueldos/sueldo-disenador-ux-ui-chile-2025">coderhouse.com</a></li>
<li id="ref-chilenter">Fundación Chilenter. (2023). <em>En Chile aún no hay conciencia de que los residuos electrónicos son contaminantes</em>. <a href="https://www.hn.cl/blog/en-chile-no-hay-conciencia-de-que-los-residuos-electronicos-son-contaminantes/">hn.cl</a></li>
<li id="ref-unab">Instituto de Políticas Públicas UNAB. (2024). <em>Sondeo sobre conocimiento ciudadano de la Ley REP</em>. Citado en Diario Sustentable. <a href="https://www.diariosustentable.com/2024/04/94-de-la-poblacion-reconoce-estar-poco-o-nada-informada-sobre-la-ley-rep-segun-sondeo-ipp-unab/">diariosustentable.com</a></li>
<li id="ref-gem">International Telecommunication Union & United Nations Institute for Training and Research. (2024). <em>The Global E-waste Monitor 2024</em>. ITU/UNITAR.</li>
<li id="ref-ley">Ley N.º 20.920. (2016). <em>Establece marco para la gestión de residuos, la responsabilidad extendida del productor y fomento al reciclaje</em>. Ministerio del Medio Ambiente.</li>
<li id="ref-lindhqvist">Lindhqvist, T. (2000). <em>Extended producer responsibility in cleaner production: Policy principle to promote environmental improvements of product systems</em> [Tesis doctoral, IIIEE, Lund University]. <a href="https://lup.lub.lu.se/record/19692">lup.lub.lu.se</a></li>
<li id="ref-mma1">Ministerio del Medio Ambiente, Fundación Chile & E2BIZ. (2019). <em>Informe N.º 1: Antecedentes para la elaboración de análisis económico de metas de recolección y valorización de RAEE</em>. <a href="https://rechile.mma.gob.cl/wp-content/uploads/2021/06/Informe-No1-RAEE-FINAL-2019-03-29.pdf">rechile.mma.gob.cl</a></li>
<li id="ref-mma2">Ministerio del Medio Ambiente, Fundación Chile & E2BIZ. (2019). <em>Informe N.º 2: Análisis económico de metas de recolección y valorización de RAEE</em>. <a href="https://rechile.mma.gob.cl/wp-content/uploads/2021/06/INFORME-No2-FINAL-RAEE-2019-07-04.pdf">rechile.mma.gob.cl</a></li>
<li id="ref-ds22">Ministerio del Medio Ambiente. (2026, 7 de mayo). Decreto Supremo N.º 22 de 2025. <em>Diario Oficial de la República de Chile</em>. <a href="https://www.diariooficial.interior.gob.cl/publicaciones/2026/05/07/44443/01/2805526.pdf">diariooficial.interior.gob.cl</a></li>
<li id="ref-mugerwa">Mugerwa, I., Chen, J., Kachule, E. P., & Nakanwagi, O. (2025). Incentivizing recycling in developing urban cities. <em>Journal of Material Cycles and Waste Management</em>. <a href="https://doi.org/10.1007/s10163-025-02239-y">doi.org/10.1007/s10163-025-02239-y</a></li>
<li id="ref-muni">Municipalidad de La Florida. (s. f.). <em>Dirección de Medio Ambiente, Aseo, Ornato y Operaciones</em>. <a href="https://www.laflorida.cl/sitio/servicios/aseo-y-ornato/">laflorida.cl</a></li>
<li id="ref-nist">National Institute of Standards and Technology. (2025). <em>NIST SP 800-88 Rev. 2: Guidelines for media sanitization</em>.</li>
<li id="ref-potting">Potting, J., Hekkert, M., Worrell, E., & Hanemaaijer, A. (2017). <em>Circular economy: Measuring innovation in the product chain</em>. PBL Netherlands Environmental Assessment Agency. <a href="https://www.pbl.nl/en/publications/circular-economy-measuring-innovation-in-product-chains">pbl.nl</a></li>
<li id="ref-puzzo1">Puzzo, G., & Prati, G. (2024). Psychological correlates of e-waste recycling intentions and behaviors: A meta-analysis. <em>Resources, Conservation and Recycling, 204</em>, 107462. <a href="https://doi.org/10.1016/j.resconrec.2024.107462">doi.org/10.1016/j.resconrec.2024.107462</a></li>
<li id="ref-puzzo2">Puzzo, G., & Prati, G. (2025). Unraveling the influence of convenience situational factors on e-waste recycling behaviors: A goal-framing theory approach. <em>Sustainable Development, 33</em>(1), 1174–1191. <a href="https://ideas.repec.org/a/wly/sustdv/v33y2025i1p1174-1191.html">ideas.repec.org</a></li>
<li id="ref-vercel">Vercel. (2026). <em>Pricing</em>. <a href="https://vercel.com/pricing">vercel.com/pricing</a></li>
<li id="ref-wang">Wang, J., Wang, C., & Chen, Y. (2023). Promoting residents’ willingness to recycle electronic ICT waste in China: An empirical study using conjoint analysis. <em>Sustainability, 15</em>(16), 12258. <a href="https://doi.org/10.3390/su151612258">doi.org/10.3390/su151612258</a></li>
</ol>


<!--CH anexos|08|Anexos|Las entregas del proceso que respaldan esta memoria.-->

## Anexos {#anexos}

<!--ANNEX-->

## Anexo L · Testeo y validación {#ax-test}

Registro de las instancias con personas reales que respaldan el capítulo 5. Los resultados cuantitativos del ciclo 2 están en [5.8](#s5-8).

<!--ANNEXTEST-->

## Declaración de uso de IA {#ia}

| Herramienta | Para qué se usó | Qué no hizo |
|---|---|---|
| Claude (Anthropic) | Ordenar contenido, verificar fuentes y cifras, configurar el test en Maze, organizar sus resultados, diagramar láminas y esta memoria | No tomó decisiones de diseño, no generó datos de terreno ni de testeo |
| Claude Code | Programar el MVP en Vercel a partir del diseño en Figma | No definió flujos ni arquitectura de información |
| Figma y Maze | Diseño del prototipo y test no moderado | — |

Las decisiones, los datos de terreno y testeo, y la autoría del proyecto son de Amaro Latoja. El uso de IA respeta el límite declarado por cada ramo.
