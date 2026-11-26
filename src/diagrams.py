# Diagramas visuales que reemplazan tablas y cards.
D = {}

# ---------- 1.3 Cadena de porqués ----------
rungs = [
 ("Problema","Los RAEE de los hogares casi no llegan al circuito formal: el canal doméstico fue el 5,5 % de lo recolectado en 2017.","ver","MMA, FCh y E2BIZ, 2019"),
 ("¿Por qué? 1","Los hogares guardan los aparatos en vez de entregarlos: 7 de 12 los dejan en un cajón.","ver","Encuesta propia, n = 12"),
 ("¿Por qué? 2","No saben dónde llevarlos (62,5 %) y el esfuerzo es desproporcionado al objeto (50 % menciona distancia u horarios).","ver","Encuesta propia, n = 12"),
 ("¿Por qué? 3","La recolección formal está pensada para el canal empresa (94 % de lo recolectado); el hogar no tiene un canal propio.","int","Dato verificado · lectura del autor"),
 ("¿Por qué? 4","Para el sistema, el canal doméstico es caro y disperso, y no hay cómo trazar cada aparato para las metas del DS 22.","sup","Sin entrevista a un operador"),
 ("Causa raíz","Falta una capa que clasifique, trace y reporte el aparato doméstico de punta a punta.","sup","Conclusión de la cadena"),
]
lab = {"ver":"Verificado","int":"Interpretación","sup":"Supuesto"}
D['LADDER'] = '<figure class="ladder">' + ''.join(
  f'<div class="rung {k}{" root" if i==len(rungs)-1 else ""}"><span class="lvl">{l}</span><p>{t}</p><span class="chip c-{k}">{lab[k]}</span><small>{s}</small></div>'
  for i,(l,t,k,s) in enumerate(rungs)) + '<figcaption class="cap">Fig. 1.1 · Cadena de los 5 porqués. Cada eslabón indica qué tan respaldado está.</figcaption></figure>'

# ---------- 1.4 Barra de la brecha ----------
D['GAP'] = '''
<figure class="gapbar">
  <div class="gb-head"><span class="eyebrow">RAEE recolectado en Chile, 2017 · 5.677 t</span></div>
  <div class="gb-bar"><div class="gb-e" style="--w:94.5%"><span>Empresas e instituciones · 5.364 t · 94 %</span></div><div class="gb-h" style="--w:5.5%"></div></div>
  <div class="gb-lab"><b>313 t · 5,5 %</b> vino de hogares</div>
  <figcaption class="cap">Fuente: <a href="#ref-mma2">MMA, FCh y E2BIZ (2019)</a>, Informe N.º 2, Cuadro 1.</figcaption>
</figure>'''

# ---------- 1.7 Doble diamante ----------
D['DIAMOND'] = '''
<figure class="diamond">
<svg viewBox="0 0 960 250" role="img" aria-label="Doble Diamante: descubrir, definir, desarrollar y entregar">
  <defs><linearGradient id="dd1" x1="0" x2="1"><stop offset="0" stop-color="#004D40"/><stop offset="1" stop-color="#0E6B58"/></linearGradient>
  <linearGradient id="dd2" x1="0" x2="1"><stop offset="0" stop-color="#0E6B58"/><stop offset="1" stop-color="#19B99A"/></linearGradient></defs>
  <polygon points="20,125 240,20 460,125 240,230" fill="url(#dd1)"/>
  <polygon points="500,125 720,20 940,125 720,230" fill="url(#dd2)"/>
  <line x1="240" y1="20" x2="240" y2="230" stroke="#121212" stroke-opacity=".35" stroke-dasharray="4 5"/>
  <line x1="720" y1="20" x2="720" y2="230" stroke="#121212" stroke-opacity=".35" stroke-dasharray="4 5"/>
  <circle cx="480" cy="125" r="18" fill="#121212"/><text x="480" y="130" text-anchor="middle" font-size="13" font-weight="800" fill="#1DE9B6">?</text>
  <g font-family="Plus Jakarta Sans, sans-serif" font-weight="700" fill="#F5F4EB" font-size="22" text-anchor="middle">
    <text x="135" y="131">Descubrir</text><text x="350" y="131">Definir</text><text x="615" y="131">Desarrollar</text><text x="830" y="131" fill="#0B2E28">Entregar</text>
  </g>
  <g font-family="JetBrains Mono, monospace" font-size="11" fill="#8E9492" text-anchor="middle"><text x="240" y="248">Problema definido</text><text x="720" y="248">Solución evaluada</text></g>
</svg>
<div class="dd-cols">
  <div><b>Descubrir</b><span>Investigación documental · encuesta exploratoria 2025 · benchmark de 7 casos · mapa de actores · visita a terreno</span></div>
  <div><b>Definir</b><span>5 porqués · FODA y PESTEL · pregunta y objetivos · requerimientos</span></div>
  <div><b>Desarrollar</b><span>Flujos en FigJam · sistema de diseño · prototipo Figma V2.1 · MVP en Vercel</span></div>
  <div><b>Entregar</b><span>Entrevista técnica · reunión municipal · focus group · Maze · revisión experta · iteración</span></div>
</div>
<figcaption class="cap">Fig. 1.3 · Doble Diamante con enfoque sistémico: cómo se recorrió en este proyecto.</figcaption>
</figure>'''

# ---------- 2.1 Línea de tiempo normativa ----------
tl = [("2016","Ley 20.920 (Ley REP)","Productores financian la gestión de sus residuos",""),
      ("17/07/2025","DS 22 fechado","Metas para pilas y AEE",""),
      ("07/05/2026","DS 22 publicado","Diario Oficial",""),
      ("2026","e-cycle","MVP, testeo y memoria","now"),
      ("07/05/2028","Metas exigibles","Año 1: meta general del 3 %","key"),
      ("Año 10","Meta general 45 %","Exigencia máxima del decreto","")]
D['TIMELINE'] = '<figure class="tline"><ol>' + ''.join(f'<li class="{c}"><span class="d">{d}</span><b>{t}</b><span class="s">{s}</span></li>' for d,t,s,c in tl) + '</ol><figcaption class="cap">Fig. 2.1 · La ventana 2026–2028 permite madurar el producto antes de que la meta doméstica sea exigible. Fuente: <a href="#ref-ds22">DS 22</a>.</figcaption></figure>'

# ---------- 2.2 Mapa de actores ----------
import math
cx, cy = 400, 290
rings = [(85,"Contacto directo"),(170,"Cadena de valorización"),(250,"Sistema y norma")]
nodes = [
 ("Hogar · vecinos",0,250,"ok"),("Pañiwe",0,330,"warn"),("Municipalidad\nLa Florida",0,50,"ok"),("Comercios del canje",0,172,"proj"),
 ("Midas Chile",1,290,"ref"),("Chilenter",1,20,"ref"),("Reciclapp",1,235,"ref"),("Redciclach",1,195,"ref"),
 ("TRAEE",2,320,"ref"),("Productores\nobligados",2,30,"ref"),("MMA · SMA",2,255,"ref"),("ReSimple\n(modelo)",2,135,"ref"),
]
col = {"ok":"#1DE9B6","warn":"#F29B38","ref":"#6C7270","proj":"#6C7270"}
svg = f'<svg viewBox="0 0 800 590" role="img" aria-label="Mapa de actores por proximidad al aparato en desuso">'
for r,(rad,name) in enumerate(rings):
    da = 'stroke-dasharray="3 5"' if r==2 else ''
    svg += f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="#2C2C2C" stroke-width="1.2" {da}/>'
    la = math.radians(100)
    svg += f'<text x="{cx+rad*math.cos(la):.0f}" y="{cy-rad*math.sin(la)+14:.0f}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#6C7270" letter-spacing="1">{name.upper()}</text>'
svg += f'<circle cx="{cx}" cy="{cy}" r="44" fill="#004D40"/><text x="{cx}" y="{cy-3}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-weight="700" font-size="12" fill="#F5F4EB">Aparato</text><text x="{cx}" y="{cy+12}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-weight="700" font-size="12" fill="#F5F4EB">en desuso</text>'
for lab_,ri,ang,st in nodes:
    rad = rings[ri][0]; a = math.radians(ang)
    x, y = cx + rad*math.cos(a), cy - rad*math.sin(a)
    dash = ' stroke-dasharray="3 3"' if st=="proj" else ''
    fill = "#121212" if st in ("ref","proj") else ("#0F3D35" if st=="ok" else "#3A2A14")
    svg += '<g class="an">'
    svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{col[st]}" stroke="#121212" stroke-width="3"/>'
    lines = lab_.split("\n"); w = max(len(s) for s in lines)*6.6+18; h = 16*len(lines)+10
    ty = y + (14 if y>cy else -14-h)
    svg += f'<rect x="{x-w/2:.1f}" y="{ty:.1f}" width="{w:.1f}" height="{h}" rx="6" fill="{fill}" stroke="{col[st]}" stroke-opacity=".6"{dash}/>'
    for k,s in enumerate(lines):
        svg += f'<text x="{x:.1f}" y="{ty+18+k*16:.1f}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="12" font-weight="600" fill="#E2E2E2">{s}</text>'
    svg += '</g>'
svg += '</svg>'
D['ACTORS'] = f'''<figure class="actors dark-fig">{svg}
<div class="legend"><span><i style="background:#1DE9B6"></i>Contacto aplicado</span><span><i style="background:#F29B38"></i>Contactado, sin respuesta</span><span><i style="background:#6C7270"></i>Referencia o proyección</span></div>
<div class="allies"><span class="eyebrow">Aliados del proyecto</span><p><b>Daniel Muñoz</b> · backend y logística · entrevista técnica y sesión presencial</p><p><b>Diego Guajardo</b> · Senior Product Designer, LATAM Airlines · revisión experta</p></div>
<figcaption class="cap">Fig. 2.2 · Actores por proximidad al aparato en desuso. e-cycle se ubica entre el hogar y el operador.</figcaption></figure>'''

# ---------- 5.5 Flujo de usuario ----------
def node(x,y,t,cls="n",w=136,h=58):
    lines=t.split("\n"); s=f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>'
    for k,l in enumerate(lines):
        s+=f'<text x="{x+w/2}" y="{y+h/2+5-(len(lines)-1)*8+k*16}" text-anchor="middle">{l}</text>'
    return s+'</g>'
fl = '<svg viewBox="0 0 980 330" role="img" aria-label="Flujo del ciudadano: explorar, entregar en un punto o pedir retiro, sumar puntos, canjear y seguimiento">'
fl += '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#19B99A"/></marker></defs>'
fl += '<text x="340" y="38" class="lane">PUNTO FÍSICO</text><text x="340" y="312" class="lane">RETIRO A DOMICILIO</text>'
P = dict(a=(10,136),b=(176,136),c=(340,52),d=(506,52),e=(340,222),f=(506,222),g=(672,136),h=(838,70),i=(838,206))
paths=[("a","b"),("b","c"),("b","e"),("c","d"),("e","f"),("d","g"),("f","g"),("g","h"),("g","i")]
for u,v in paths:
    (x1,y1),(x2,y2)=P[u],P[v]; x1+=136; y1+=29; y2+=29
    mx=(x1+x2)/2
    fl+=f'<path d="M{x1} {y1} C{mx} {y1} {mx} {y2} {x2-2} {y2}" class="ed{" dash" if v in ("f","i") else ""}" marker-end="url(#ar)"/>'
fl += node(*P['a'],"Aparato\nen desuso","n start")+node(*P['b'],"Explorar\nmapa y lista")+node(*P['c'],"Ir al punto\nmás cercano")
fl += node(*P['d'],"Escanear QR\ny declarar")+node(*P['e'],"Pedir retiro\nqué · dónde · cuándo")+node(*P['f'],"Camión del sector\nal llegar al peso","n sup")
fl += node(*P['g'],"Suma puntos\n+ dato educativo")+node(*P['h'],"Canjea en\nun comercio")+node(*P['i'],"¿Qué pasó con\nmi aparato?","n proj")
fl += '</svg>'
D['USERFLOW'] = f'''<figure class="uflow dark-fig">{fl}
<div class="legend"><span><i style="background:#19B99A"></i>En el MVP</span><span><i class="dash-o"></i>Supuesto: lo opera el gestor</span><span><i class="dash-g"></i>Proyección · ciclo 3</span></div>
<figcaption class="cap">Fig. 5.1 · Flujo del ciudadano en el MVP publicado. La cuenta se crea al final, con teléfono y SMS.</figcaption></figure>
<figure class="layers">
  <div class="ly on"><span class="eyebrow">Capa 1</span><b>Ciudadano</b><span>Explorar · Retiro · Escanear · Beneficios</span><em class="chip c-ver">Con código · Vercel</em></div>
  <div class="ly"><span class="eyebrow">Capa 2</span><b>Gestión (B2B)</b><span>Rutas, segunda clasificación y reportes REP</span><em class="chip c-pro">Solo en Figma</em></div>
  <div class="ly"><span class="eyebrow">Capa 3</span><b>Conductor</b><span>Retiro colectivo por sector</span><em class="chip c-pro">Solo en Figma</em></div>
  <figcaption class="cap">Fig. 5.2 · Tres capas del sistema. Solo la ciudadana está construida.</figcaption>
</figure>'''

# ---------- 5.8 Iteración entre ciclos ----------
def it_row(h,src,ch,res,st,stc,weak=False):
    return f'<li><div class="it-h"><span class="eyebrow">Hallazgo</span><p>{h}</p><small>{src}</small></div><div class="it-c"><span class="eyebrow">Cambio</span><p>{ch}</p></div><div class="it-r{" weak" if weak else ""}"><span class="eyebrow">Resultado</span><p>{res}</p><span class="chip {stc}">{st}</span></div></li>'
D['ITER'] = '<figure class="iter"><div class="it-stage"><div class="st"><b>01</b><span>Focus group<small>~15 personas · MVP en Vercel</small></span></div><i></i><div class="st"><b>02</b><span>Test en Maze<small>12 personas · Figma V2.1</small></span></div></div><ol>' + \
 it_row("No se sabía cuándo el retiro estaba listo","Focus group + experto","Peso siempre visible, kilos que faltan y botón activo solo al llegar a 5 kg","<b>91,7 %</b> completó el retiro · claridad 4,2 / 5","Aplicado","c-ver") + \
 it_row("No se encontraba dónde canjear","Focus group + experto","Filtro «Con beneficios» y botón «Ver dónde canjear en el mapa»","<b>75 %</b> · 3,5 / 5: sigue siendo débil","Aplicado","c-ver",True) + \
 it_row("Reescribir la dirección en cada retiro","Experto","Direcciones guardadas en la cuenta","Sin medición propia","Aplicado","c-ver") + \
 it_row("No se percibía qué recibe cada punto","Focus group","Sin cambio: la ficha y la lista ya existían","No medido","Ciclo 3","c-pro") + \
 '</ol><div class="it-stage"><div class="st"><b>02</b><span>Test en Maze<small>12 personas · Figma V2.1</small></span></div><i></i><div class="st ghost"><b>03</b><span>Entrega final<small>ajustes de diciembre</small></span></div></div><ol>' + \
 it_row("El retiro se completa con fricción","Maze · 40,1 % de clics fallidos","Ubicar los toques fallidos en los mapas de calor y corregir ese control","Para la entrega final","Pendiente","c-pro") + \
 it_row("El canje sigue siendo débil","Maze · 25 % de abandono","Acortar el camino al canje desde el inicio","Para la entrega final","Pendiente","c-pro") + \
 it_row("Se espera saber qué pasó con el aparato","Maze · 6 de 10 respuestas","Pantalla de estado del aparato (solo diseño)","Para la entrega final","Pendiente","c-pro") + \
 it_row("El cajón de la lista tapa el mapa y esconde los filtros","Referente Google Maps · decisión del autor (25/11)","Filtros bajo el buscador; sin cajón: los puntos cercanos se ven al abrir el buscador y el detalle al tocar un punto","Aplicado en Figma, sin medir","Aplicado","c-ver") + \
 it_row("Uso poco frecuente","Maze · 10 de 12","Se mantiene la web app sin tienda de apps","Decisión confirmada","Confirmado","c-ver") + \
 it_row("Piden misiones y ligas","Maze · 1 de 12","No se aplica: la gamificación se eliminó a propósito","Descartado con fundamento","Descartado","c-int") + \
 '</ol><figcaption class="cap">Fig. 5.4 · Cada cambio responde a un hallazgo concreto, y cada hallazgo indica su fuente.</figcaption></figure>'

# ---------- 5.10 Hitos: plan y real ----------
import datetime as dt
d0, d1 = dt.date(2026,10,20), dt.date(2026,12,16)
def pos(d): return (d-d0).days/(d1-d0).days*100
plan=[(dt.date(2026,11,2),"H1 · Corte B2B"),(dt.date(2026,11,6),"H2 · Datos y test"),(dt.date(2026,11,17),"H3 · Test analizado"),(dt.date(2026,12,4),"H4 · Marcha blanca"),(dt.date(2026,12,15),"Defensa")]
real=[(dt.date(2026,11,2),"B2B no validada","warn"),(dt.date(2026,11,17),"Reunión municipal","ok"),(dt.date(2026,11,23),"Maze n = 12","ok")]
months=[(dt.date(2026,11,1),"Nov"),(dt.date(2026,12,1),"Dic")]
hs='<figure class="hitos"><div class="ht-axis">'+''.join(f'<span style="left:{pos(d):.1f}%">{m}</span>' for d,m in months)+'<span style="left:0">Oct</span></div>'
hs+='<div class="ht-row"><span class="ht-lab">Plan</span><div class="ht-track">'+''.join(f'<div class="ht-m p" style="left:{pos(d):.1f}%"><i></i><span>{t}<small>{d.day:02d}/{d.month:02d}</small></span></div>' for d,t in plan)+'</div></div>'
hs+='<div class="ht-row"><span class="ht-lab">Real</span><div class="ht-track">'+''.join(f'<div class="ht-m r {c}" style="left:{pos(d):.1f}%"><i></i><span>{t}<small>{d.day:02d}/{d.month:02d}</small></span></div>' for d,t,c in real)+'</div></div>'
hs+='<figcaption class="cap">Fig. 5.10 · Hitos del plan de implementación frente a lo ocurrido. El focus group (ciclo 1) se hizo en noviembre; su fecha exacta está por confirmar.</figcaption></figure>'
D['HITOS']=hs

# ---------- Diagnóstico: FODA en cuadrantes ----------
D['FODA'] = '''<figure class="foda2">
<span class="ax ax-t">Interno</span><span class="ax ax-r">Externo</span><span class="ax ax-l">A favor</span><span class="ax ax-b">En contra</span>
<div class="q f"><h4>Fortalezas</h4><ul><li>MVP publicado y repositorio de código</li><li>Sistema de diseño y flujos modelados</li><li>Encuadre normativo verificado</li><li>Dos ciclos de testeo y una revisión experta</li></ul></div>
<div class="q o"><h4>Oportunidades</h4><ul><li>Ventana 2026–2028 antes de la meta doméstica</li><li>Canal doméstico casi vacío (313 de 5.677 t)</li><li>La Municipalidad abre un puente local</li></ul></div>
<div class="q d"><h4>Debilidades</h4><ul><li>Solo la capa ciudadana tiene código, sin backend</li><li>Ninguna conversación con un operador</li><li>Encuesta exploratoria pequeña, sin archivo crudo</li><li>El canje es la tarea más débil</li></ul></div>
<div class="q a"><h4>Amenazas</h4><ul><li>Los obligados priorizan el canal empresa (94 %)</li><li>Reciclapp y Redciclach ya operan en B2C</li><li>El retiro puede ser inviable a baja escala</li><li>Depende de un operador que aún no es socio</li></ul></div>
<figcaption class="cap">Fig. DG.1 · FODA del proyecto a noviembre de 2026.</figcaption></figure>'''

# ---------- 5.4 Componente de Retiro (igual a la app) ----------
D['SIM'] = '''
<figure class="appdemo">
  <div class="ad-txt">
    <span class="eyebrow">Interactivo · componente de la app</span>
    <h4>Paso 1 del retiro: el peso decide</h4>
    <p>Así funciona hoy en el MVP. Cuenta tus aparatos: la app estima el peso y el botón se activa al llegar a 5 kg, el mínimo para que el camión del sector pase gratis. Es la regla que hace posible el retiro colectivo.</p>
    <p class="cap">Réplica del paso 1 de Retiro con los tokens y pesos del repositorio e-cycle (<code>Pickup.tsx</code>, <code>ciudadano.ts</code>). Simulación del flujo, no dato de uso.</p>
  </div>
  <div class="phone app ec-dark" aria-label="Réplica del paso 1 de Retiro">
    <div class="ad-scroll">
      <div class="ad-step">Paso 1 de 4</div>
      <div class="ad-h1">¿Qué quieres reciclar?</div>
      <p class="ad-p">Cuenta cuántos tienes de cada uno. Con eso calculamos el peso; no necesitas pesarlos.</p>
      <div class="ad-list" id="adList"></div>
    </div>
    <div class="ad-co">
      <div class="ad-card" id="adCard"><div class="ad-row"><span>Peso estimado</span><b id="adKg">0 kg</b></div><div class="ad-pb"><div id="adPb"></div></div><p id="adMsg">Te faltan 5 kg para el retiro gratis.</p></div>
      <button type="button" class="ad-btn" id="adBtn" disabled>Agrega aparatos para continuar</button>
    </div>
    <nav class="ad-nav" aria-hidden="true"><span class="nb"><span class="ms">explore</span>Explorar</span><span class="nb on"><span class="ms">local_shipping</span>Retiro</span><span class="nb"><span class="ms">qr_code_scanner</span>Escanear</span><span class="nb"><span class="ms">redeem</span>Beneficios</span></nav>
  </div>
</figure>'''

# ---------- 5.7 Prototipo con pestañas ----------
D['PROTO'] = '''
<div class="proto">
  <div class="pv">
    <div class="pv-tabs" role="tablist" aria-label="Versión a mostrar">
      <button role="tab" aria-selected="true" data-src="https://e-cycle-tau.vercel.app" type="button">MVP en vivo</button>
      <button role="tab" aria-selected="false" data-src="https://embed.figma.com/proto/jV6NVg7yiB1AiKIu9M7VG6/E-Cycle-V2.1?node-id=4-8&amp;scaling=contain&amp;content-scaling=fixed&amp;hide-ui=1&amp;embed-host=share" type="button">Prototipo Figma</button>
    </div>
    <div class="phone"><div class="scr"><iframe id="pvFrame" src="https://e-cycle-tau.vercel.app" title="e-cycle" loading="lazy" allow="geolocation"></iframe></div></div>
    <p class="cap" style="text-align:center">¿No carga? <a href="https://e-cycle-tau.vercel.app" target="_blank" rel="noopener">Abrir el MVP ↗</a> · <a href="https://www.figma.com/proto/jV6NVg7yiB1AiKIu9M7VG6" target="_blank" rel="noopener">Abrir en Figma ↗</a></p>
  </div>
  <div class="proto-txt">
    <span class="eyebrow">Pruébalo aquí</span>
    <h4>El producto, funcionando</h4>
    <p>El MVP en Vercel es la versión de mayor fidelidad, con todos los ajustes del prototipo de Figma aplicados. Navega Explorar, Retiro y Beneficios dentro del marco, o cambia a la pestaña de Figma para ver el prototipo que se testeó en Maze.</p>
    <p class="cap">Solo frontend, sin backend ni datos de uso real. Los 12 puntos son reales; los comercios del canje, de ejemplo.</p>
  </div>
</div>
'''
