# Tercera tanda: Canvas como en el deck, mapa de navegación y anexo de testeo.
D = {}

def cell(cls, icon, title, body, chip=None):
    c = f'<div class="bc {cls}"><h5><span class="ms">{icon}</span>{title}</h5>{body}'
    if chip: c += f'<span class="bchip {chip[1]}">{chip[0]}</span>'
    return c + '</div>'

D['BMC'] = '<figure class="bmc2 dark-fig"><div class="bg">' + \
 cell('k1', 'handshake', 'Socios clave', '<p>Pañiwe, alianza ancla por confirmar. Municipalidad de La Florida, puente local. Comercios y servicios técnicos para el canje. TRAEE, posible financiador futuro.</p>', ('Supuesto', 'w')) + \
 cell('k2', 'construction', 'Actividades clave', '<p>Desarrollar el software de gestión y la web ciudadana. Mantener vigentes los datos de puntos.</p>') + \
 cell('k3', 'inventory_2', 'Recursos clave', '<p>MVP publicado, sistema de diseño y alianza técnica de backend y logística.</p>') + \
 cell('k4 hi', 'diamond', 'Propuesta de valor', '<div class="who"><span class="ib"><span class="ms">business</span></span><b>Operador</b></div><p>Gestión y trazabilidad por aparato y categoría, rutas por sector y reportes para la Ley REP, más volumen domiciliario.</p><div class="who"><span class="ib"><span class="ms">person</span></span><b>Ciudadano</b></div><p>Saber dónde y qué entregar, pedir retiro y recibir un beneficio.</p>') + \
 cell('k5', 'support_agent', 'Relación', '<p>Piloto acompañado con el operador y soporte continuo.</p>') + \
 cell('k6', 'hub', 'Canales', '<p>Web app (PWA) para el ciudadano, sin tienda de apps. Venta directa al operador. Municipio como puente.</p>') + \
 cell('k7', 'groups', 'Segmentos', '<div class="who"><span class="ib"><span class="ms">payments</span></span><b>Paga</b></div><p>Operadores de gestión de RAEE con puntos y campañas.</p><div class="who"><span class="ib"><span class="ms">person</span></span><b>Usa</b></div><p>Ciudadanos del sur de Santiago; piloto en La Florida.</p>', ('Supuesto', 'w')) + \
 cell('k8', 'receipt_long', 'Estructura de costos', '<p>Desarrollo y hosting del software; incorporación de comercios para el canje. La logística del retiro la asume el operador. Montos por estimar.</p>', ('Por estimar', 'g')) + \
 cell('k9 hi', 'trending_up', 'Fuentes de ingreso', '<p>Licencia de software más un fee por tonelada certificada, como ReSimple. e-cycle no puede ser Sistema de Gestión (Ley REP, art. 10): es proveedor tecnológico.</p>', ('Supuesto · validar con Pañiwe', 'w')) + \
 '</div><figcaption class="cap">Fig. 5.9 · Modelo de negocio, primer borrador (I+E III, evaluación 3). El operador paga por gestión y trazabilidad; el ciudadano usa gratis.</figcaption></figure>'

# ---------- Mapa de navegación ----------
tabs = [
 ("explore", "Explorar", "Encontrar dónde entregar", ["Mapa y lista de puntos", "Buscador", "Filtros por aparato · Con beneficios", "Ficha del punto", "Ficha del comercio"]),
 ("local_shipping", "Retiro", "Pedir que lo retiren en casa", ["1 · ¿Qué quieres reciclar?", "2 · ¿Dónde lo retiramos?", "3 · ¿Cuándo te acomoda?", "4 · Revisa tu retiro", "Solicitud recibida y seguimiento"]),
 ("qr_code_scanner", "Escanear", "Entregar en un punto", ["Cámara y lectura del QR", "¿Qué vas a depositar?", "Validando la entrega", "Puntos sumados + dato educativo"]),
 ("redeem", "Beneficios", "Canjear lo acumulado", ["Saldo de puntos", "Canjear", "Historial", "Ver dónde canjear en el mapa"]),
]
cols = ''
for ic, name, job, screens in tabs:
    cols += f'<div class="nm-col"><div class="nm-tab"><span class="ms">{ic}</span><b>{name}</b><small>{job}</small></div><ol>' + ''.join(f'<li>{s}</li>' for s in screens) + '</ol></div>'
D['NAVMAP'] = f'''<figure class="navmap">
<div class="nm-root"><span class="ms">smartphone</span><div><b>e-cycle · web app (PWA)</b><small>Barra de navegación inferior con cuatro destinos</small></div></div>
<div class="nm-bus"></div>
<div class="nm-cols">{cols}</div>
<div class="nm-acc"><span class="ms">person</span><div><b>Cuenta · transversal</b><small>Se crea al final, cuando hace falta: teléfono y código SMS. Sin cuenta, los puntos se guardan 30 días en el navegador.</small></div></div>
<figcaption class="cap">Fig. 5.6 · Mapa de navegación de la capa ciudadana, según el MVP publicado (repositorio e-cycle).</figcaption></figure>'''

# ---------- Anexo de testeo y validación ----------
items = [
 ("groups", "Ciclo 1 · Focus group", "12/11/2026 · ~15 estudiantes de INACAP · MVP en Vercel",
  "Tareas guiadas: encontrar y filtrar un punto, declarar un aparato, canjear y pedir retiro. Audio grabado y transcrito.",
  ["No se sabía cuándo el retiro estaba listo para salir", "No se encontraba dónde canjear", "No se percibía qué recibe cada punto", "«¿Qué es una web app?»: se explicó la PWA"], None),
 ("rate_review", "Revisión experta · Diego Guajardo", "Nov. 2026 · Senior Product Designer, LATAM Airlines",
  "Revisión del prototipo de alta fidelidad entre el ciclo 1 y el 2.",
  ["Peso estimado siempre visible", "Beneficios visibles desde el inicio", "Dirección guardada para no reescribirla", "Sopesar el impacto frente a la baja frecuencia de uso"], None),
 ("analytics", "Ciclo 2 · Test no moderado en Maze", "23–24/11/2026 · 12 personas · Figma V2.1",
  "Siete bloques: dos tareas de prototipo (pedir retiro, encontrar dónde canjear), dos escalas, un ranking, una pregunta abierta y frecuencia de descarte.",
  ["Retiro: 91,7 % de éxito, 40,1 % de clics fallidos", "Canje: 75 % de éxito, 25 % de abandono", "10 de 12 descartan cada 2–3 años o casi nunca", "6 de 10 piden saber qué pasó con su aparato"], ("Ver reporte de Maze", "https://app.maze.co/report/e-cycle-Retiro-y-beneficios/xX_q6E2r_UXWw9OS7qy0dwz89ydK1-zR/intro")),
 ("engineering", "Sesión con Daniel Muñoz · consultor técnico", "Nov. 2026 · presencial",
  "Navegó el MVP en persona. No se registró feedback escrito de esa sesión; su mirada técnica está en la entrevista del 15/09 (Taller, evaluación 1).",
  [], None),
 ("account_balance", "Reunión con la Municipalidad de La Florida", "17/11/2026 · Valeria Gutiérrez, Aseo y Ornato",
  "Cómo opera la recolección en la comuna y contacto directo de Pañiwe.",
  ["En los puntos fijos llegan otros desechos por falta de información", "Trabajan solo con Pañiwe; lo eligieron por confiabilidad logística", "Lo que Pañiwe no recibe (refrigeradores) queda sin derivación"], None),
]
cards = ''
for ic, t, meta, desc, finds, link in items:
    f = ''.join(f'<li>{x}</li>' for x in finds)
    l = f'<a class="btn ghost sm" href="{link[1]}" target="_blank" rel="noopener">{link[0]} ↗</a>' if link else ''
    cards += f'<article class="ax-card"><header><span class="ms">{ic}</span><div><b>{t}</b><small>{meta}</small></div></header><p>{desc}</p>' + (f'<ul>{f}</ul>' if f else '') + l + '</article>'
D['ANNEXTEST'] = f'<div class="ax-grid">{cards}</div>'

# ---------- Escalera 9R ----------
R=[("R0","Rechazar",0),("R1","Repensar",0),("R2","Reducir",0),("R3","Reutilizar",1),("R4","Reparar",1),("R5","Restaurar",1),("R6","Remanufacturar",1),("R7","Reasignar",1),("R8","Reciclar",2),("R9","Recuperar energía",2)]
mark={"R3":"Chilenter, aguas abajo","R4":"Beneficios del canje","R8":"Recolección e-cycle"}
grp=["Uso y fabricación más inteligentes","Alargar la vida del producto y sus partes","Aprovechar los materiales"]
li=''
for code,name,gi in R:
    m=mark.get(code)
    li+=f'<li class="g{gi}{" on" if m else ""}"><b>{code}</b><span>{name}</span>'+(f'<em>{m}</em>' if m else '')+'</li>'
D['NINER']=('<figure class="niner"><div class="nr-axis"><span>Más circular</span><i></i><span>Menos circular</span></div><ol>'+li+'</ol>'
 '<div class="nr-g">'+''.join(f'<span class="g{i}">{g}</span>' for i,g in enumerate(grp))+'</div>'
 '<figcaption class="cap">Fig. 3.1 · Escalera de estrategias de circularidad (9R), adaptada de <a href="#ref-potting">Potting et al. (2017)</a>. En menta, dónde actúa e-cycle.</figcaption></figure>')
