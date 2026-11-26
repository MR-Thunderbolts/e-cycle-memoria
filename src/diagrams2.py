# Segunda versión de los diagramas más exigidos (diamante, actores, FODA, flujo, Gantt).
import math, datetime as dt
D = {}

# ---------- Doble Diamante ----------
W, H, cy = 1000, 300, 150
q = W / 4
halves = [
 (0, "01", "Descubrir", "Divergir", "#0B3B33", "#E2E2E2"),
 (1, "02", "Definir", "Converger", "#004D40", "#E2E2E2"),
 (2, "03", "Desarrollar", "Divergir", "#0E8A70", "#F5F4EB"),
 (3, "04", "Entregar", "Converger", "#1DE9B6", "#0B2E28"),
]
svg = f'<svg viewBox="0 -34 {W} {H+70}" role="img" aria-label="Doble Diamante en cuatro fases: descubrir, definir, desarrollar y entregar">'
svg += f'<line class="axis" x1="0" y1="{cy}" x2="{W}" y2="{cy}" stroke="#C9CCC6" stroke-dasharray="2 6"/>'
for i, n, name, verb, fill, ink in halves:
    x0, x1 = i*q, (i+1)*q
    if i % 2 == 0:  # diverge: point at left
        pts = f"{x0},{cy} {x1},{cy-130} {x1},{cy+130}"
        tx = x0 + q*0.62
    else:
        pts = f"{x0},{cy-130} {x1},{cy} {x0},{cy+130}"
        tx = x0 + q*0.38
    svg += f'<g class="half" style="--rd:{i*.28:.2f}s;transform-origin:{x0}px {cy}px"><polygon points="{pts}" fill="{fill}"/>'
    svg += f'<text x="{tx}" y="{cy-14}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="13" font-weight="700" fill="{ink}" opacity=".7">{n}</text>'
    svg += f'<text x="{tx}" y="{cy+10}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="21" font-weight="700" fill="{ink}">{name}</text>'
    svg += f'<text x="{tx}" y="{cy+32}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="12" font-weight="600" fill="{ink}" opacity=".7" letter-spacing="1.5">{verb.upper()}</text></g>'
# pins
for x, lab, sub in [(0, "Inicio", "Aparatos que no salen del hogar"), (2*q, "Problema definido", "Falta una capa que clasifique y trace"), (W, "Solución evaluada", "Capa ciudadana · 2 ciclos de testeo")]:
    anchor = "start" if x == 0 else ("end" if x == W else "middle")
    svg += f'<g class="pin" style="--rd:{.2+x/W*1.0:.2f}s"><circle cx="{x}" cy="{cy}" r="7" fill="#121212" stroke="#FAFAF7" stroke-width="3"/>'
    svg += f'<text x="{x}" y="-12" text-anchor="{anchor}" font-family="Plus Jakarta Sans, sans-serif" font-size="13" font-weight="700" fill="#14201E">{lab}</text>'
    svg += f'<text x="{x}" y="6" text-anchor="{anchor}" font-family="Plus Jakarta Sans, sans-serif" font-size="11.5" fill="#4F5957">{sub}</text></g>'
svg += '</svg>'
methods = [
 ["Investigación documental", "Encuesta exploratoria 2025", "Benchmark de 7 casos", "Visita a terreno"],
 ["5 porqués", "FODA y PESTEL", "Pregunta y objetivos", "Requerimientos"],
 ["Flujos en FigJam", "Sistema de diseño v2", "Prototipo Figma V2.1", "MVP en Vercel"],
 ["Entrevista técnica", "Reunión municipal", "Focus group · Maze", "Revisión experta"],
]
cols = ''.join(f'<div class="ph p{i}"><span class="ph-n">{halves[i][1]} · {halves[i][2]}</span><ul>' + ''.join(f'<li>{m}</li>' for m in ms) + '</ul></div>' for i, ms in enumerate(methods))
D['DIAMOND'] = f'<figure class="diamond2">{svg}<p class="dd2-t">Qué se hizo en cada fase</p><div class="dd2">{cols}</div><figcaption class="cap">Fig. 1.3 · Doble Diamante con enfoque sistémico: los métodos que se usaron en cada fase.</figcaption></figure>'

# ---------- Mapa de actores ----------
cx, cy = 420, 330
R = [100, 190, 280]
sectors = [(90, 210, "CIUDADANÍA Y COMERCIO"), (-30, 90, "OPERACIÓN Y VALORIZACIÓN"), (210, 330, "ESTADO Y SISTEMA DE GESTIÓN")]
nodes = [
 ("Hogar · vecinos", 0, 150, "ok"), ("Comercios del canje", 1, 150, "proj"), ("Reciclapp", 2, 122, "ref"), ("Redciclach", 2, 178, "ref"),
 ("Pañiwe", 0, 30, "warn"), ("Midas Chile", 1, -12, "ref"), ("Chilenter", 1, 32, "ref"), ("ReSimple · modelo", 2, 62, "ref"),
 ("Municipalidad La Florida", 0, 270, "ok"), ("TRAEE", 1, 318, "ref"), ("Productores obligados", 2, 298, "ref"), ("MMA · SMA", 2, 242, "ref"),
]
col = {"ok": "#1DE9B6", "warn": "#F29B38", "ref": "#8E9492", "proj": "#8E9492"}
def P(r, a): a = math.radians(a); return cx + r*math.cos(a), cy - r*math.sin(a)
s = f'<svg viewBox="0 0 840 660" role="img" aria-label="Mapa de actores en tres anillos de proximidad y tres sectores">'
s += '<defs><radialGradient id="rg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#0F3D35"/><stop offset="1" stop-color="#121212"/></radialGradient></defs>'
RD = {0: .35, 1: 1.15, 2: 1.95}
for i, (r, fill) in enumerate(zip(R[::-1], ["#161A19", "#13211E", "#0F2B26"])):
    s += f'<circle class="ring" style="--rd:{RD[2-i]:.2f}s" cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#2A3331" stroke-width="1"/>'
for a0, a1, lab in sectors:
    x, y = P(R[2], a0); s += f'<line class="sl" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#2A3331" stroke-width="1.5" pathLength="1"/>'
    lx, ly, anc = {"CIUDADANÍA Y COMERCIO": (16, 30, "start"), "OPERACIÓN Y VALORIZACIÓN": (824, 30, "end"), "ESTADO Y SISTEMA DE GESTIÓN": (420, 650, "middle")}[lab]
    s += f'<text class="slab" x="{lx}" y="{ly}" text-anchor="{anc}" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#8E9492" letter-spacing="2">{lab}</text>'
for k, (r, lab) in enumerate(zip(R, ["DIRECTO", "CADENA", "SISTEMA"])):
    x, y = P(r-14, 92); s += f'<text class="rlab" style="--rd:{RD[k]+.25:.2f}s" x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#9AA3A0" letter-spacing="2">{lab}</text>'
# vínculos del centro con los actores directos
for lab, ri, ang, st in nodes:
    if ri == 0:
        x, y = P(R[0], ang)
        dash = ' stroke-dasharray="4 4"' if st == "warn" else ''
        s += f'<line class="lk" style="--rd:.6s" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{col[st]}" stroke-width="1.5" opacity=".7"{dash}/>'
s += f'<g class="core"><circle cx="{cx}" cy="{cy}" r="52" fill="#004D40" stroke="#1DE9B6" stroke-opacity=".5"/>'
s += f'<text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-weight="700" font-size="13" fill="#F5F4EB">Aparato</text><text x="{cx}" y="{cy+13}" text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-weight="700" font-size="13" fill="#F5F4EB">en desuso</text></g>'
for lab, ri, ang, st in nodes:
    x, y = P(R[ri], ang)
    w = len(lab)*7.3 + 34; h = 28
    fill = {"ok": "#0F3D35", "warn": "#3A2A14", "ref": "#1E1E1E", "proj": "#1E1E1E"}[st]
    dash = ' stroke-dasharray="4 3"' if st == "proj" else ''
    s += f'<g class="an" style="--rd:{RD[ri]+.3+(ang%360)/360*.35:.2f}s"><rect x="{x-w/2:.1f}" y="{y-h/2:.1f}" width="{w:.1f}" height="{h}" rx="14" fill="{fill}" stroke="{col[st]}" stroke-opacity=".8"{dash}/>'
    s += f'<circle cx="{x-w/2+13:.1f}" cy="{y:.1f}" r="4" fill="{col[st]}"/>'
    s += f'<text x="{x-w/2+24:.1f}" y="{y+4.5:.1f}" text-anchor="start" font-family="Plus Jakarta Sans, sans-serif" font-size="12.5" font-weight="600" fill="#E2E2E2">{lab}</text></g>'
s += '</svg>'
D['ACTORS'] = f'''<figure class="actors dark-fig">{s}
<div class="legend"><span><i style="background:#1DE9B6"></i>Contacto aplicado</span><span><i style="background:#F29B38"></i>Contactado, sin respuesta</span><span><i style="background:#8E9492"></i>Referencia</span><span><i class="dash-g"></i>Proyección</span></div>
<div class="allies"><span class="eyebrow">Aliado y consultor</span><p><b>Diego Guajardo</b> · aliado del proyecto · Senior Product Designer, LATAM Airlines · revisión experta del prototipo</p><p><b>Daniel Muñoz</b> · consultor técnico · backend y logística · entrevista técnica y sesión presencial</p></div>
<figcaption class="cap">Fig. 2.2 · Actores por proximidad al aparato en desuso (anillos) y por tipo de rol (sectores). e-cycle opera en el anillo directo, entre el hogar y el operador.</figcaption></figure>'''

# ---------- FODA ----------
D['FODA'] = '''<figure class="swot">
  <div class="sw-grid">
    <span class="sw-c"></span><span class="sw-hd">Favorable</span><span class="sw-hd">Desfavorable</span>
    <span class="sw-rh">Origen interno</span>
    <div class="sw f"><b class="L">F</b><h4>Fortalezas</h4><ul><li>MVP publicado y repositorio de código</li><li>Sistema de diseño y flujos modelados</li><li>Encuadre normativo verificado</li><li>Dos ciclos de testeo y una revisión experta</li></ul></div>
    <div class="sw d"><b class="L">D</b><h4>Debilidades</h4><ul><li>Solo la capa ciudadana tiene código, sin backend</li><li>Ninguna conversación con un operador</li><li>Encuesta exploratoria pequeña, sin archivo crudo</li><li>El canje es la tarea más débil (75 %)</li></ul></div>
    <span class="sw-rh">Origen externo</span>
    <div class="sw o"><b class="L">O</b><h4>Oportunidades</h4><ul><li>Ventana 2026–2028 antes de la meta doméstica</li><li>Canal doméstico casi vacío (313 de 5.677 t)</li><li>La Municipalidad abre un puente local</li></ul></div>
    <div class="sw a"><b class="L">A</b><h4>Amenazas</h4><ul><li>Los obligados priorizan el canal empresa (94 %)</li><li>Reciclapp y Redciclach ya operan en B2C</li><li>El retiro puede ser inviable a baja escala</li><li>Depende de un operador que aún no es socio</li></ul></div>
  </div>
  <figcaption class="cap">Fig. DG.1 · Matriz FODA a noviembre de 2026.</figcaption>
</figure>'''

# ---------- Flujo de usuario con conectores en codo ----------
NW, NH = 140, 58
PTS = dict(a=(10, 136), b=(190, 136), c=(370, 52), d=(550, 52), e=(370, 222), f=(550, 222), g=(730, 136), h=(905, 62), i=(905, 210))
def elbow(x1, y1, x2, y2, r=10):
    if abs(y2-y1) < 1: return f"M{x1} {y1} H{x2}"
    mx = (x1+x2)/2; sg = 1 if y2 > y1 else -1; r = min(r, abs(y2-y1)/2, (x2-x1)/2)
    return f"M{x1} {y1} H{mx-r} Q{mx} {y1} {mx} {y1+sg*r} V{y2-sg*r} Q{mx} {y2} {mx+r} {y2} H{x2}"
def nd(k, t, cls="n"):
    x, y = PTS[k]; lines = t.split("\n")
    o = f'<g class="{cls}"><rect x="{x}" y="{y}" width="{NW}" height="{NH}" rx="12"/>'
    for j, l in enumerate(lines): o += f'<text x="{x+NW/2}" y="{y+NH/2+5-(len(lines)-1)*8+j*16}" text-anchor="middle">{l}</text>'
    return o + '</g>'
fl = '<svg viewBox="0 0 1060 320" role="img" aria-label="Flujo del ciudadano: explorar, entregar en un punto o pedir retiro, sumar puntos, canjear y seguimiento">'
fl += '<defs><marker id="ar" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1L10 5L0 9z" fill="#19B99A"/></marker><marker id="arg" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1L10 5L0 9z" fill="#8E9492"/></marker></defs>'
fl += '<text x="370" y="34" class="lane">PUNTO FÍSICO</text><text x="370" y="306" class="lane">RETIRO A DOMICILIO</text>'
for u, v, dash in [("a","b",0),("b","c",0),("b","e",0),("c","d",0),("e","f",1),("d","g",0),("f","g",0),("g","h",0),("g","i",2)]:
    (x1, y1), (x2, y2) = PTS[u], PTS[v]
    x1 += NW; y1 += NH/2; y2 += NH/2; x2 -= 3
    cls = "ed" + (" dash" if dash == 2 else (" sup" if dash == 1 else ""))
    mk = "arg" if dash == 2 else "ar"
    fl += f'<path d="{elbow(x1, y1, x2, y2)}" class="{cls}" marker-end="url(#{mk})"/>'
fl += nd('a', "Aparato\nen desuso", "n start") + nd('b', "Explorar\nmapa y lista") + nd('c', "Ir al punto\nmás cercano") + nd('d', "Escanear QR\ny declarar")
fl += nd('e', "Pedir retiro\nqué · dónde · cuándo") + nd('f', "Camión del sector\nal llegar al peso", "n sup") + nd('g', "Suma puntos\n+ dato educativo")
fl += nd('h', "Canjea en\nun comercio") + nd('i', "¿Qué pasó con\nmi aparato?", "n proj")
fl += '</svg>'
D['USERFLOW_SVG'] = fl

# ---------- 5.10 Gantt plan vs real ----------
d0, d1 = dt.date(2026, 10, 13), dt.date(2026, 12, 17)
span = (d1 - d0).days
def x(d): return (d - d0).days / span * 100
def D_(m, d): return dt.date(2026, m, d)
rows = [
 ("Fase 0", "MVP y plan", (D_(10,13), D_(10,21)), [("bar", D_(10,13), D_(10,17), "MVP publicado")]),
 ("A1", "Municipio y Pañiwe", (D_(10,21), D_(11,6)), [("warn", D_(11,2), None, "Pañiwe sin respuesta"), ("pt", D_(11,17), None, "Reunión municipal")]),
 ("A2", "Preparar MVP y test", (D_(10,28), D_(11,6)), [("pt", D_(11,11), None, "Listo"), ("pt", D_(11,24), None, "Puntos reales")]),
 ("A3", "Difusión con QR", (D_(10,28), D_(11,7)), [("pt", D_(11,23), None, "QR del test compartido")]),
 ("A4.1", "Test ciclo 1: focus group", (D_(11,10), D_(11,17)), [("pt", D_(11,12), None, "~15 personas")]),
 ("A4.2", "Test ciclo 2: Maze", (D_(11,10), D_(11,17)), [("bar", D_(11,23), D_(11,24), "12 personas")]),
 ("A5", "Marcha blanca con vecinos", (D_(11,18), D_(11,25)), [("tbd", None, None, "Pendiente")]),
 ("A6", "Marcha blanca en INACAP", (D_(11,24), D_(12,4)), [("tbd", None, None, "Pendiente")]),
]
miles = [(D_(11,2), "H1"), (D_(11,6), "H2"), (D_(11,17), "H3"), (D_(12,4), "H4"), (D_(12,15), "Defensa")]
weeks = []
w = D_(10,19)
while w < d1: weeks.append(w); w += dt.timedelta(days=7)
g = '<figure class="gantt"><div class="gt">'
g += '<div class="gt-head"><span class="gt-l"></span><div class="gt-t">' + ''.join(f'<span class="wk" style="left:{x(wk):.2f}%">{wk.day:02d}/{wk.month:02d}</span>' for wk in weeks)
g += ''.join(f'<span class="mst" style="left:{x(d):.2f}%" title="{t}"><i></i><b>{t}</b></span>' for d, t in miles) + '</div></div>'
today = D_(11,25)
for code, name, (p0, p1), real in rows:
    g += f'<div class="gt-row"><span class="gt-l"><b>{code}</b>{name}</span><div class="gt-t">'
    g += ''.join(f'<i class="gl" style="left:{x(wk):.2f}%"></i>' for wk in weeks)
    g += f'<span class="pl" style="left:{x(p0):.2f}%;width:{x(p1)-x(p0):.2f}%"></span>'
    for kind, a, b, lab in real:
        if kind == "bar":
            g += f'<span class="rb" style="left:{x(a):.2f}%;width:max({x(b)-x(a):.2f}%,10px)"></span>'
            g += f'<span class="glab" style="left:calc({max(x(b), x(p1)):.2f}% + 10px)">{lab}</span>'
        elif kind in ("pt", "warn"):
            g += f'<span class="rp {kind}" style="left:{x(a):.2f}%"></span>'
            g += f'<span class="glab {kind}" style="left:calc({x(a):.2f}% + 12px)">{lab}</span>'
        else:
            g += f'<span class="tbd" style="left:{x(p1):.2f}%"></span><span class="glab tb" style="left:calc({x(p1):.2f}% + 28px)">{lab}</span>'
    g += '</div></div>'
g += f'<div class="today" data-d0="{d0.isoformat()}" data-d1="{d1.isoformat()}" hidden><span></span></div>'
g += '</div><div class="legend lt"><span><i class="lg-pl"></i>Planificado</span><span><i class="lg-rb"></i>Realizado</span><span><i class="lg-w"></i>Sin respuesta</span><span><i class="lg-t"></i>Por confirmar</span><span><i class="lg-hoy"></i>Hoy</span></div>'
g += '<figcaption class="cap">Fig. 5.10 · Carta Gantt del plan de implementación (Unidad 2) frente a lo ocurrido. La línea menta marca el día en que se lee.</figcaption></figure>'
D['HITOS'] = g

# ---------- 1.3 Cadena de porqués v2 ----------
rungs = [
 ("P", "Problema", "Los RAEE de los hogares casi no llegan al circuito formal: el canal doméstico fue el 5,5 % de lo recolectado en 2017.", "ver", "MMA, FCh y E2BIZ, 2019"),
 ("1", "¿Por qué?", "Los hogares guardan los aparatos en vez de entregarlos: 7 de 12 los dejan en un cajón.", "ver", "Encuesta propia, n = 12"),
 ("2", "¿Por qué?", "No saben dónde llevarlos (62,5 %) y el esfuerzo es desproporcionado al objeto (50 % menciona distancia u horarios).", "ver", "Encuesta propia, n = 12"),
 ("3", "¿Por qué?", "La recolección formal está pensada para el canal empresa (94 % de lo recolectado); el hogar no tiene un canal propio.", "int", "Dato verificado · lectura del autor"),
 ("4", "¿Por qué?", "Para el sistema, el canal doméstico es caro y disperso, y no hay cómo trazar cada aparato para las metas del DS 22.", "sup", "Sin entrevista a un operador"),
]
lab = {"ver": "Verificado", "int": "Interpretación", "sup": "Supuesto"}
lv = ''.join(f'<li class="lv {k}" style="--i:{i}"><span class="node">{n}</span><div class="card"><span class="lvl">{h}</span><p>{t}</p><footer><span class="chip c-{k}">{lab[k]}</span><small>{s}</small></footer></div></li>' for i,(n,h,t,k,s) in enumerate(rungs))
D['LADDER'] = ('<figure class="why"><div class="why-strength"><span>Evidencia</span><i></i><span>Supuesto</span></div><ol>' + lv +
  '<li class="lv root" style="--i:5"><span class="node">R</span><div class="card"><span class="lvl">Causa raíz</span><p>Falta una capa que clasifique, trace y reporte el aparato doméstico de punta a punta, conectando al hogar con quien debe cumplir la meta.</p><footer><span class="chip c-sup">Supuesto</span><small>Conclusión de la cadena</small></footer></div>'
  '<div class="opp"><span class="eyebrow">Oportunidad de diseño</span><svg class="brandSvg opp-logo" role="img" aria-label="e-cycle"></svg><span>clasificar · trazar · educar</span></div></li></ol>'
  '<figcaption class="cap">Fig. 1.1 · Cadena de los 5 porqués. Mientras más profunda la causa, menos evidencia la respalda: los dos últimos eslabones se validan con un operador.</figcaption></figure>')
