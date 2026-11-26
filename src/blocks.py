# Bloques HTML que se insertan en los marcadores <!--X--> del contenido.
BLOCKS = {}

BLOCKS['FIGS'] = '''
<div class="stats">
  <div class="stat"><b>5,5 %</b><span>del RAEE recolectado en 2017 vino de hogares (313 de 5.677 t)</span><small><a href="#ref-mma2">MMA, FCh y E2BIZ, 2019</a></small></div>
  <div class="stat"><b>3,4 %</b><span>de los RAEE generados recibió tratamiento formal</span><small><a href="#ref-mma2">MMA, FCh y E2BIZ, 2019</a></small></div>
  <div class="stat"><b>94 %</b><span>se declara poco o nada informado sobre la Ley REP</span><small><a href="#ref-unab">IPP UNAB, 2024</a></small></div>
  <div class="stat"><b>3 → 45 %</b><span>meta de recolección del DS 22, del primer al décimo año</span><small><a href="#ref-ds22">DS 22, 2026</a></small></div>
</div>
<p class="cap">Fig. 1.2 · La brecha, en cifras. Se eliminaron de versiones anteriores las cifras sin fuente primaria localizada.</p>
'''

BLOCKS['SIM'] = '''
<figure class="sim" aria-labelledby="sim-t">
  <div class="sim-head"><span class="eyebrow">Interactivo · lógica del MVP</span><h4 id="sim-t">¿Alcanza el mínimo para un retiro gratis?</h4><p>Suma aparatos como en el paso 1 del retiro. Los pesos son los estimados que usa el prototipo; el mínimo por solicitud es 5 kg.</p></div>
  <div class="sim-body">
    <ul class="sim-list" id="simList"></ul>
    <div class="sim-out"><div class="meter"><div id="simBar"></div><i style="left:calc(5/12*100%)"></i></div><p id="simTxt" aria-live="polite"></p></div>
  </div>
  <figcaption class="cap">Pesos estimados de <code>src/constants/ciudadano.ts</code> (repositorio e-cycle). Simulación del flujo, no dato de uso.</figcaption>
</figure>
'''

BLOCKS['FLOW'] = '''
<ol class="flow">
  <li><span class="n">1</span><b>Descubre</b><span>Encuentra un punto o pide el retiro</span></li>
  <li><span class="n">2</span><b>Entrega</b><span>Escanea el QR y declara el aparato</span></li>
  <li><span class="n">3</span><b>Valida y suma</b><span>El contenedor confirma y suma puntos</span></li>
  <li><span class="n">4</span><b>Canjea</b><span>Muestra el código en el comercio</span></li>
  <li class="proj"><span class="n">5</span><b>Seguimiento</b><span>Recibido, clasificado, valorizado</span><em class="chip c-pro">Proyección</em></li>
</ol>
'''

BLOCKS['PROTO'] = '''
<div class="proto">
  <div class="phone"><iframe src="https://e-cycle-tau.vercel.app" title="MVP de e-cycle en Vercel" loading="lazy"></iframe></div>
  <div class="proto-txt">
    <span class="eyebrow">Pruébalo aquí</span>
    <h4>El MVP, funcionando</h4>
    <p>Es la versión de mayor fidelidad del producto, con todos los ajustes del prototipo de Figma aplicados. Navega Explorar, Retiro y Beneficios dentro del marco, o ábrelo en tu celular.</p>
    <p class="btns"><a class="btn" href="https://e-cycle-tau.vercel.app" target="_blank" rel="noopener">Abrir e-cycle-tau.vercel.app ↗</a><a class="btn ghost" href="https://www.figma.com/proto/jV6NVg7yiB1AiKIu9M7VG6" target="_blank" rel="noopener">Prototipo en Figma ↗</a></p>
    <p class="cap">Solo frontend, sin backend ni datos de uso real. Los 12 puntos son reales; los comercios del canje, de ejemplo.</p>
  </div>
</div>
'''

BLOCKS['CYCLES'] = '''
<div class="cycles">
  <div class="cycle"><span class="eyebrow">Ciclo 1</span><h4>Focus group presencial</h4><dl><dt>Formato</dt><dd>Moderado, en sala, con tareas guiadas</dd><dt>Participantes</dt><dd>Cerca de 15 estudiantes de INACAP · 12 de noviembre de 2026</dd><dt>Prototipo</dt><dd>MVP en Vercel</dd><dt>Tareas</dt><dd>Encontrar y filtrar un punto · declarar un aparato · canjear · pedir retiro</dd><dt>Registro</dt><dd>Audio transcrito; hallazgos cualitativos, sin conteos</dd></dl></div>
  <div class="cycle"><span class="eyebrow">Ciclo 2</span><h4>Test no moderado en Maze</h4><dl><dt>Formato</dt><dd>Remoto, sin moderador</dd><dt>Participantes</dt><dd>12 personas · 23 y 24 de noviembre de 2026</dd><dt>Prototipo</dt><dd>Figma «E-Cycle V2.1», con los ajustes del ciclo 1</dd><dt>Tareas</dt><dd>Pedir un retiro · encontrar dónde canjear · escalas, ranking y pregunta abierta</dd><dt>Métricas</dt><dd>Éxito, abandono, clics fallidos y tiempo</dd></dl></div>
</div>
<p class="cap"><span class="chip c-sup">Límite</span> Muestras pequeñas y por conveniencia: orientan el diseño, no representan a la población.</p>
'''

BLOCKS['RESULTS'] = '''
<div class="dark-block">
  <span class="eyebrow">Ciclo 2 · resultados</span>
  <h3>El retiro se completa; el canje sigue siendo el punto débil</h3>
  <div class="kpis">
    <div class="kpi"><span class="eyebrow">Tarea · pedir un retiro</span><b class="big" data-count="91.7">91,7 %</b><span class="cap2">completó la tarea (11 de 12)</span>
      <dl><dt>8,3 %</dt><dd>abandono</dd><dt class="w">40,1 %</dt><dd>clics fallidos</dd><dt>55,5 s</dt><dd>tiempo promedio</dd><dt>4,2 / 5</dt><dd>claridad del peso y de que es gratis</dd></dl></div>
    <div class="kpi weak"><span class="eyebrow">Tarea · encontrar dónde canjear</span><b class="big" data-count="75">75 %</b><span class="cap2">completó la tarea (9 de 12)</span>
      <dl><dt class="w">25 %</dt><dd>abandono</dd><dt>14,8 %</dt><dd>clics fallidos</dd><dt>3,5 / 5</dt><dd>facilidad para encontrar dónde canjear</dd></dl></div>
  </div>
  <div class="rank">
    <span class="eyebrow">¿Qué te haría usar e-cycle? · posición promedio (1 = más importante)</span>
    <ol>
      <li><span>Que lo retiren en mi casa</span><i style="--w:100%"></i><b>2,0</b></li>
      <li><span>Recibir un beneficio concreto</span><i style="--w:84%"></i><b>2,6</b></li>
      <li><span>Saber dónde llevar mi aparato</span><i style="--w:71%"></i><b>3,1</b></li>
      <li><span>Aprender qué se puede reciclar</span><i style="--w:64%"></i><b>3,4</b></li>
      <li><span>Ver qué pasó con mi aparato</span><i style="--w:52%"></i><b>3,9</b></li>
    </ol>
  </div>
  <div class="split">
    <div class="band"><b>10 de 12</b><p>deja de usar un aparato cada 2 o 3 años o casi nunca. La baja frecuencia confirma una web app sin tienda de apps.</p></div>
    <div class="band alt"><b>6 de 10</b><p>respuestas abiertas piden saber qué pasó con su aparato. La trazabilidad no atrae: retiene. Va al cierre del flujo.</p></div>
  </div>
  <p class="cap">Fuente: Maze «e-cycle · Retiro y beneficios», n = 12, 23 y 24 de noviembre de 2026; pregunta abierta, 10 respuestas al cierre. Barra más larga = más importante.</p>
</div>
'''

BLOCKS['BMC'] = '''
<div class="bmc">
  <div class="b1"><span class="eyebrow">Socios clave</span><p>Pañiwe, alianza ancla por confirmar. Municipalidad de La Florida, puente local. Comercios y servicios técnicos para el canje. TRAEE, posible financiador futuro.</p></div>
  <div class="b2"><span class="eyebrow">Actividades clave</span><p>Desarrollar el software de gestión y la web ciudadana. Mantener vigentes los datos de puntos.</p></div>
  <div class="b3"><span class="eyebrow">Recursos clave</span><p>MVP publicado, sistema de diseño y alianza técnica de backend y logística.</p></div>
  <div class="b4"><span class="eyebrow">Propuesta de valor</span><div class="vp2"><span class="tag pay">Operador · paga</span><p>Gestión y trazabilidad por aparato y categoría, rutas por sector y reportes para la Ley REP, más volumen domiciliario.</p><span class="tag use">Ciudadano · usa</span><p>Saber dónde y qué entregar, pedir retiro y recibir un beneficio.</p></div></div>
  <div class="b5"><span class="eyebrow">Relación</span><p>Piloto acompañado con el operador y soporte continuo.</p></div>
  <div class="b6"><span class="eyebrow">Canales</span><p>Web app para el ciudadano. Venta directa al operador. Municipio como puente.</p></div>
  <div class="b7"><span class="eyebrow">Segmentos</span><span class="tag pay">Paga</span><p>Operadores de gestión de RAEE con puntos y campañas.</p><span class="tag use">Usa</span><p>Ciudadanos del sur de Santiago; piloto en La Florida.</p></div>
  <div class="b8"><span class="eyebrow">Costos</span><p>Desarrollo y hosting; incorporación de comercios. La logística del retiro la asume el operador. Montos por estimar.</p></div>
  <div class="b9"><span class="eyebrow">Ingresos</span><p>Licencia de software más fee por tonelada certificada. e-cycle no puede ser Sistema de Gestión (Art. 10).</p></div>
</div>
<p class="cap"><span class="chip c-sup">Supuesto</span> Primer borrador del modelo de negocio (I+E III, evaluación 3). Se valida con un operador.</p>
'''

A = [
 ("A","Benchmark de 7 casos","Tabla completa de modelos de negocio revisados (sept. 2026)","2.3","Por adjuntar",None),
 ("B","Estudio de 6 dimensiones (Diseño de Experiencia, EV1)","Análisis de la experiencia de depósito, antes del pivote","5.6","PDF entregado",None),
 ("C","Entrevista técnica a Daniel Muñoz (Taller, EV1)","Mirada técnica del consultor del proyecto","4.1","PDF entregado",None),
 ("D","Memoria de Título, EV1","Primera versión de la memoria. Versión histórica: algunas cifras se corrigieron en el cap. 1","—","PDF entregado",None),
 ("E","Pitch animado (I+E III, EV2)","Primera propuesta de valor","5.3","Ver presentación","https://claude.ai/artifact/VVRkmsgTZyh977rAF94Mku"),
 ("F","Tablero de control (Gestión de Diseño, EV2)","Madurez, Gantt, indicadores y roles al 15/10","5.10","Ver tablero","https://claude.ai/artifact/3fPXZMvm7egQkLwkGQkrsn"),
 ("G","Lámina de testeo (Taller)","Brecha entre el diseño declarado y el MVP, y ruta de testeo","5.7","PDF entregado",None),
 ("H","Rediseño de un punto de contacto (Diseño de Experiencia, EV2)","Salida de la gamificación y rediseño de la recompensa","5.6","PDF entregado",None),
 ("I","Plan de implementación (Proyecto de Título, U2)","Actividades, socios, Gantt e instrumentos","5.10","PDF entregado",None),
 ("J","Prototipo, testeo e iteración (I+E III, EV3)","Dos ciclos de testeo, matrices de ajuste y modelo de negocio","5.8","Ver en Figma","https://www.figma.com/deck/G5Z5WwihG99KlNSLITtRVX"),
 ("K","Del punto de contacto al sistema (Diseño de Experiencia, EV3)","Sistema de canales, sistema visual y diseño por componente","5.5","Ver en Figma","https://www.figma.com/deck/fdSYqRnw5QEQwNAmwIYFDX"),
 ("L","Testeo y validación","Focus group, revisión experta, Maze, sesión técnica y reunión municipal","5.8","Ver abajo","#ax-test"),
]
rows=''.join(f'<li><span class="al">{a}</span><div><b>{t}</b><span>{d}</span></div><span class="sec">{s}</span>'+(f'<a href="{u}"'+('' if u.startswith('#') else ' target="_blank" rel="noopener"')+f'>{l} '+('↓' if u.startswith('#') else '↗')+'</a>' if u else f'<span class="pdf">{l}</span>')+'</li>' for a,t,d,s,l,u in A)
BLOCKS['ANNEX'] = f'<ol class="annex">{rows}</ol><p class="cap">Los anexos en PDF se adjuntan a la versión impresa. Faltan Gestión de Diseño EV1 y las entregas finales de Taller y Proyecto de Título.</p>'

BLOCKS['REFS'] = """
<div class="refpairs">
 <article class="rpair"><header><span class="eyebrow">Referente · Google Maps</span><h4>Buscar sobre el mapa</h4><p>La barra de búsqueda flota sobre el mapa y lleva el acceso a la cuenta dentro, a la derecha: buscar es la primera acción y nunca tapa el mapa.</p><span class="dec"><b>Decisión del 25/11:</b> siguiendo este referente, los filtros pasan bajo el buscador y se elimina el cajón de la lista: los puntos cercanos aparecen al abrir el buscador y el detalle solo al tocar un punto. Aplicado en Figma V2.1; el MVP aún no cambia.</span></header>
  <div class="rp-row">
   <div class="mk ref"><div class="mk-map"><span class="pin" style="left:30%;top:58%"></span><span class="pin" style="left:62%;top:40%"></span><span class="pin" style="left:72%;top:70%"></span></div><div class="mk-search"><span class="ms">search</span><i>Buscar aquí</i><span class="av"></span></div><div class="mk-chips"><span>Restaurantes</span><span>Gasolina</span><span>Hoteles</span></div><small class="mk-tag">Patrón recreado</small></div>
   <span class="rp-arr ms">arrow_forward</span>
   <div class="mk ec"><div class="mk-map d"><span class="pin" style="left:34%;top:56%"></span><span class="pin" style="left:60%;top:56%"></span><span class="pin" style="left:70%;top:72%"></span></div><div class="mk-search d"><span class="ms">search</span><i>Busca un punto o aparato</i><span class="av d"><span class="ms">person</span></span></div><div class="mk-chips d"><span>Todos</span><span class="on">Con beneficios</span><span>Celulares</span></div><small class="mk-tag d">e-cycle · Explorar</small></div>
  </div></article>
 <article class="rpair"><header><span class="eyebrow">Referente · Mercado Libre</span><h4>Cuánto falta para el envío gratis</h4><p>Una barra de progreso dice cuánto falta para el beneficio antes de pagar: la meta se ve y se puede alcanzar sumando productos.</p></header>
  <div class="rp-row">
   <div class="mk ml"><div class="ml-top">Carrito (3)</div><div class="ml-card"><div class="mk-line"><b>Envío</b><span>$3.990</span></div><div class="mk-bar"><div style="width:72%"></div></div><p class="mk-p">Agrega <b>$5.600</b> y obtén <b>envío gratis</b></p></div><div class="mk-btn">Continuar compra</div><small class="mk-tag">Patrón recreado</small></div>
   <span class="rp-arr ms">arrow_forward</span>
   <div class="mk ec"><div class="mk-line d"><b>Peso estimado</b><span>3,2 kg</span></div><div class="mk-bar d"><div style="width:64%"></div></div><p class="mk-p d">Te faltan <b>1,8 kg</b> para que tu retiro sea gratis</p><div class="mk-btn d off">Continuar</div><small class="mk-tag d">e-cycle · Retiro, paso 1</small></div>
  </div></article>
 <article class="rpair"><header><span class="eyebrow">Referente · Uber</span><h4>Resumen antes de confirmar y estado después</h4><p>Antes de pedir se ve el resumen completo; después, el estado del pedido avanza por pasos y la persona sabe qué viene.</p></header>
  <div class="rp-row">
   <div class="mk ub"><div class="mk-line"><b>Llega en 4 min</b><span>Económico</span></div><ol class="mk-steps"><li class="ok">Conductor asignado</li><li class="ok">En camino a tu ubicación</li><li>Llegó</li></ol><div class="mk-btn">Confirmar</div><small class="mk-tag">Patrón recreado</small></div>
   <span class="rp-arr ms">arrow_forward</span>
   <div class="mk ec"><div class="mk-line d"><b>Solicitud recibida</b><span class="ms ok">check_circle</span></div><ol class="mk-steps d"><li class="ok">Tu sector junta e-waste</li><li>Ruta programada</li><li>Te avisamos con 24 horas</li><li>Sumamos tus puntos</li></ol><small class="mk-tag d">e-cycle · Retiro, seguimiento</small></div>
  </div></article>
 <article class="rpair solo"><header><span class="eyebrow">Referente · Material Design 3</span><h4>La base de los componentes</h4><p>Sistema de diseño de Google, probado en uso: barra de navegación inferior, tarjetas, hojas inferiores y estados de botones. e-cycle lo adapta con sus tokens: tema oscuro, menta y la grilla de píxeles.</p></header></article>
</div>
<p class="cap">Patrones de referencia recreados de forma esquemática (sin marcas) junto a su versión en e-cycle, reconstruida a partir del MVP publicado.</p>
"""
