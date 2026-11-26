/* Animación del logo: 'Armado de la C' de Amaro Latoja (módulo sin cambios, solo envuelto). */
window.ECLogo=(function(){
  var NS = 'http://www.w3.org/2000/svg';
  var ISO = { body: 'M19.8022 0H28.0532C30.2534 0 31.3535 1.10012 31.3535 3.30037V6.60074C31.3535 8.80099 30.2534 9.90111 28.0532 9.90111H20.6273C18.9771 9.90111 18.152 10.7262 18.152 12.3764V13.2015C18.152 14.8517 17.327 15.6768 15.6768 15.6768H13.2015C11.5513 15.6768 10.7262 16.5019 10.7262 18.152V29.7033C10.7262 31.3535 11.5513 32.1786 13.2015 32.1786H15.6768C17.327 32.1786 18.152 33.0037 18.152 34.6539V35.479C18.152 37.1292 18.9771 37.9543 20.6273 37.9543H29.7033C31.3535 37.9543 32.1786 37.1292 32.1786 35.479V34.6539C32.1786 33.0037 33.0037 32.1786 34.6539 32.1786H35.479C37.1292 32.1786 37.9543 31.3535 37.9543 29.7033V27.2281C37.9543 25.0278 39.0544 23.9277 41.2546 23.9277H44.555C46.7553 23.9277 47.8554 25.0278 47.8554 27.2281V33.8288C47.8554 36.0291 46.7553 37.1292 44.555 37.1292H43.7299C42.0797 37.1292 41.2546 37.9543 41.2546 39.6045V41.2546C41.2546 43.4549 40.1545 44.555 37.9543 44.555H36.3041C34.6539 44.555 33.8288 45.1051 33.8288 46.2052C33.8288 47.3053 32.7287 47.8554 30.5284 47.8554H18.152C15.9518 47.8554 14.8517 47.0303 14.8517 45.3801V44.555C14.8517 42.9048 14.0266 42.0797 12.3764 42.0797H9.90111C7.70087 42.0797 6.60074 40.9796 6.60074 38.7794V37.1292C6.60074 35.479 5.77565 34.6539 4.12546 34.6539H3.30037C1.10012 34.6539 0 33.5538 0 31.3535V16.5019C0 14.3016 1.10012 13.2015 3.30037 13.2015H4.12546C5.77565 13.2015 6.60074 12.3764 6.60074 10.7262V9.07602C6.60074 6.87577 7.70087 5.77565 9.90111 5.77565H12.3764C14.0266 5.77565 14.8517 4.95056 14.8517 3.30037C14.8517 1.10012 16.5019 0 19.8022 0Z', dots: ['M40.0171 2.47528H36.7167C35.5775 2.47528 34.654 3.3988 34.654 4.53802V7.83839C34.654 8.9776 35.5775 9.90112 36.7167 9.90112H40.0171C41.1563 9.90112 42.0798 8.9776 42.0798 7.83839V4.53802C42.0798 3.3988 41.1563 2.47528 40.0171 2.47528Z', 'M48.268 9.07604H46.6179C45.9343 9.07604 45.3802 9.63015 45.3802 10.3137V11.9639C45.3802 12.6474 45.9343 13.2015 46.6179 13.2015H48.268C48.9516 13.2015 49.5057 12.6474 49.5057 11.9639V10.3137C49.5057 9.63015 48.9516 9.07604 48.268 9.07604Z'] };
  var WORD = { x: 56.93, y: 3.83, w: 143.068, h: 40.1985, paths: ["M11.1662 31.8907C8.96269 31.8907 7.01232 31.4292 5.31504 30.5061C3.64755 29.5533 2.33738 28.2282 1.38452 26.5309C0.461445 24.8039 -9.31843e-05 22.7791 -9.31843e-05 20.4565V19.9205C-9.31843e-05 17.5979 0.461445 15.588 1.38452 13.8907C2.3076 12.1637 3.60289 10.8386 5.27038 9.91554C6.93787 8.96268 8.87336 8.48625 11.0768 8.48625C13.2505 8.48625 15.1414 8.97757 16.7493 9.9602C18.3572 10.9131 19.6079 12.253 20.5012 13.9801C21.3945 15.6773 21.8411 17.6575 21.8411 19.9205V21.8411H5.71703C5.77658 23.3597 6.34234 24.5954 7.4143 25.5483C8.48626 26.5011 9.79644 26.9776 11.3448 26.9776C12.923 26.9776 14.0843 26.6351 14.8287 25.9503C15.5731 25.2654 16.1389 24.7571 16.526 24.119H21.5348C21.5348 25.9535 20.0992 27.7071 19.2952 28.6302C18.521 29.5235 17.4788 30.2977 16.1686 30.9528C14.8585 31.5781 13.191 31.8907 11.1662 31.8907ZM5.7617 17.6426H16.124C16.0049 16.3622 15.4838 15.3349 14.5607 14.5607C13.6674 13.7865 12.4912 13.3994 11.0322 13.3994C9.51356 13.3994 8.3076 13.7865 7.4143 14.5607C6.521 15.3349 5.97013 16.3622 5.7617 17.6426Z", "M27.8225 17.7065H35.0008C35.6616 17.7065 36.1972 18.2422 36.1972 18.9029V21.2957C36.1972 21.9564 35.6616 22.4921 35.0008 22.4921H27.8225C27.1618 22.4921 26.6261 21.9564 26.6261 21.2957V18.9029C26.6261 18.2422 27.1618 17.7065 27.8225 17.7065Z", "M51.6643 31.8907C49.5204 31.8907 47.57 31.4441 45.8132 30.5508C44.0862 29.6575 42.7164 28.3622 41.704 26.6649C40.6916 24.9677 40.1854 22.9131 40.1854 20.5011V19.8758C40.1854 17.4639 40.6916 15.4093 41.704 13.7121C42.7164 12.0148 44.0862 10.7195 45.8132 9.82621C47.57 8.93291 49.5204 8.48625 51.6643 8.48625C53.7785 8.48625 55.5948 8.85846 57.1135 9.60288C58.6321 10.3473 59.8529 11.3746 60.776 12.6848C61.7288 13.9652 62.3542 15.4242 62.6519 17.0619L57.2028 18.2232C57.0837 17.3299 56.8157 16.526 56.3988 15.8113C55.9819 15.0967 55.3864 14.5309 54.6122 14.114C53.8678 13.6972 52.9298 13.4887 51.7983 13.4887C50.6668 13.4887 49.6395 13.7418 48.7164 14.248C47.8231 14.7245 47.1085 15.454 46.5725 16.4366C46.0663 17.3895 45.8132 18.5657 45.8132 19.9652V20.4118C45.8132 21.8113 46.0663 23.0024 46.5725 23.985C47.1085 24.9379 47.8231 25.6674 48.7164 26.1736C49.6395 26.65 50.6668 26.8882 51.7983 26.8882C53.4956 26.8882 54.776 26.4565 55.6395 25.593C56.5328 24.6997 57.0986 23.5384 57.3368 22.1091L62.7859 23.4044C62.3988 24.9825 61.7288 26.4267 60.776 27.7369C59.8529 29.0173 58.6321 30.0297 57.1135 30.7741C55.5948 31.5185 53.7785 31.8907 51.6643 31.8907Z", "M66.972 40.1984V35.2852H79.0316C79.8654 35.2852 80.2822 34.8386 80.2822 33.9453V28.3622H79.4783C79.24 28.8684 78.8678 29.3746 78.3616 29.8808C77.8554 30.387 77.1706 30.8038 76.307 31.1314C75.4435 31.4589 74.3418 31.6227 73.0018 31.6227C71.2748 31.6227 69.7562 31.2356 68.446 30.4614C67.1656 29.6574 66.1681 28.5557 65.4534 27.1562C64.7388 25.7567 64.3815 24.1487 64.3815 22.3324V9.11152H70.0093V21.8857C70.0093 23.5532 70.4113 24.8038 71.2152 25.6376C72.049 26.4713 73.2252 26.8882 74.7438 26.8882C76.4708 26.8882 77.8108 26.3224 78.7636 25.1909C79.7165 24.0296 80.1929 22.4217 80.1929 20.3671V9.11152H85.8207V35.1959C85.8207 36.7145 85.374 37.9205 84.4807 38.8138C83.5874 39.7368 82.3964 40.1984 80.9075 40.1984H66.972Z", "M99.2934 31.8907C97.1495 31.8907 95.1991 31.4441 93.4423 30.5508C91.7152 29.6575 90.3455 28.3622 89.3331 26.6649C88.3207 24.9677 87.8145 22.9131 87.8145 20.5011V19.8758C87.8145 17.4639 88.3207 15.4093 89.3331 13.7121C90.3455 12.0148 91.7152 10.7195 93.4423 9.82621C95.1991 8.93291 97.1495 8.48625 99.2934 8.48625C101.408 8.48625 103.224 8.85846 104.743 9.60288C106.261 10.3473 107.482 11.3746 108.405 12.6848C109.358 13.9652 109.983 15.4242 110.281 17.0619L104.832 18.2232C104.713 17.3299 104.445 16.526 104.028 15.8113C103.611 15.0967 103.015 14.5309 102.241 14.114C101.497 13.6972 100.559 13.4887 99.4274 13.4887C98.2959 13.4887 97.2686 13.7418 96.3455 14.248C95.4522 14.7245 94.7376 15.454 94.2016 16.4366C93.6954 17.3895 93.4423 18.5657 93.4423 19.9652V20.4118C93.4423 21.8113 93.6954 23.0024 94.2016 23.985C94.7376 24.9379 95.4522 25.6674 96.3455 26.1736C97.2686 26.65 98.2959 26.8882 99.4274 26.8882C101.125 26.8882 102.405 26.4565 103.269 25.593C104.162 24.6997 104.728 23.5384 104.966 22.1091L110.415 23.4044C110.028 24.9825 109.358 26.4267 108.405 27.7369C107.482 29.0173 106.261 30.0297 104.743 30.7741C103.224 31.5185 101.408 31.8907 99.2934 31.8907Z", "M113.206 31.2655V2.52192e-05H118.834V31.2655H113.206Z", "M132.394 31.8907C130.19 31.8907 128.24 31.4292 126.543 30.5061C124.875 29.5533 123.565 28.2282 122.612 26.5309C121.689 24.8039 121.228 22.7791 121.228 20.4565V19.9205C121.228 17.5979 121.689 15.588 122.612 13.8907C123.535 12.1637 124.831 10.8386 126.498 9.91554C128.166 8.96268 130.101 8.48625 132.305 8.48625C134.478 8.48625 136.369 8.97757 137.977 9.9602C139.585 10.9131 140.836 12.253 141.729 13.9801C142.622 15.6773 143.069 17.6575 143.069 19.9205V21.8411H126.945C127.004 23.3597 127.57 24.5954 128.642 25.5483C129.714 26.5011 131.024 26.9776 132.573 26.9776C134.151 26.9776 135.312 26.6351 136.056 25.9503C136.801 25.2654 137.367 24.7571 137.754 24.119H142.763C142.763 25.9535 141.327 27.7071 140.523 28.6302C139.749 29.5235 138.707 30.2977 137.396 30.9528C136.086 31.5781 134.419 31.8907 132.394 31.8907ZM126.989 17.6426H137.352C137.233 16.3622 136.711 15.3349 135.788 14.5607C134.895 13.7865 133.719 13.3994 132.26 13.3994C130.741 13.3994 129.535 13.7865 128.642 14.5607C127.749 15.3349 127.198 16.3622 126.989 17.6426Z"] };
  var CELL = 4.95057, COLS = 10, ROWS = 10, SLICES = 22;
  var uid = 0;

  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function clamp(x, a, b) { return Math.min(b, Math.max(a, x)); }
  function smooth(a, b, x) { var t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); }

  // Every grid cell that touches the symbol (25 sample points per cell). Together they cover the whole outline.
  var ctx = document.createElement('canvas').getContext('2d');
  var shape = new Path2D(ISO.body);
  var cells = [];
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    var hits = 0, mx = 0, my = 0;
    for (var a = 0; a < 5; a++) for (var b = 0; b < 5; b++) {
      var px = (c + (a + 0.5) / 5) * CELL, py = (r + (b + 0.5) / 5) * CELL;
      if (ctx.isPointInPath(shape, px, py)) { hits++; mx += px; my += py; }
    }
    // mx, my: centre of the part of the logo inside this cell, so a thin sliver is ordered with the body it belongs to.
    if (hits >= 1) cells.push({ c: c, r: r, x: c * CELL, y: r * CELL, hits: hits, mx: mx / hits, my: my / hits });
  }
  var N = cells.length;

  // Guide line through the middle of the stroke: top bar (right to left), left stem, bottom bar, hook of the tail.
  var ROUTE = [[31, 5], [24, 4.6], [15, 4.8], [9, 8], [5.2, 14], [4.8, 22], [6.5, 30], [11, 37], [17, 41.2], [24, 42.6], [31, 41.6], [37, 38], [42, 33], [45.2, 27], [46.5, 22]];
  var samples = [];
  (function () {
    for (var i = 0; i < ROUTE.length - 1; i++) for (var q = 0; q < 40; q++) {
      var f = q / 40, p0 = ROUTE[Math.max(0, i - 1)], p1 = ROUTE[i], p2 = ROUTE[i + 1], p3 = ROUTE[Math.min(ROUTE.length - 1, i + 2)];
      var t = f, t2 = t * t, t3 = t2 * t;
      samples.push([0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3),
                    0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)]);
    }
    samples.push(ROUTE[ROUTE.length - 1]);
  })();
  cells.forEach(function (k) {
    var cx = k.mx, cy = k.my, bi = 0, bd = Infinity;
    samples.forEach(function (sp, qi) { var d = Math.hypot(sp[0] - cx, sp[1] - cy); if (d < bd) { bd = d; bi = qi; } });
    var a = samples[Math.max(0, bi - 1)], b = samples[Math.min(samples.length - 1, bi + 1)];
    k.s = bi / (samples.length - 1);
    k.side = (b[0] - a[0]) * (cy - samples[bi][1]) - (b[1] - a[1]) * (cx - samples[bi][0]); // which side of the line, so a slice fills across
    k.slice = Math.floor(k.s * SLICES);
  });
  // Reading order: slice by slice along the contour, and across the stroke inside each slice.
  var order = cells.map(function (_, i) { return i; }).sort(function (p, q) {
    return cells[p].slice - cells[q].slice || cells[p].side - cells[q].side;
  });
  // Slices that actually hold cells, in order: one step each.
  var sliceIds = []; order.forEach(function (i) { if (sliceIds.indexOf(cells[i].slice) < 0) sliceIds.push(cells[i].slice); });
  var STEPS = sliceIds.length;
  cells.forEach(function (k) { k.step = sliceIds.indexOf(k.slice); });
  // Partial cells (the rounded edges) light up together with the full cell their logo area leans on,
  // so every step adds whole blocks and no edge piece shows up on its own.
  var at = {}; cells.forEach(function (k) { at[k.c + ',' + k.r] = k; });
  var full = function (k) { return k && k.hits === 25; };
  cells.forEach(function (k) {
    if (full(k)) return;
    var best = null, bd = Infinity;
    for (var dc = -1; dc <= 1; dc++) for (var dr = -1; dr <= 1; dr++) {
      var nb = at[(k.c + dc) + ',' + (k.r + dr)];
      if (!full(nb)) continue;
      var d = Math.hypot(nb.x + CELL / 2 - k.mx, nb.y + CELL / 2 - k.my) + (dc && dr ? 1.5 : 0);
      if (d < bd) { bd = d; best = nb; }
    }
    if (best) k.step = best.step;
  });
  // Close the gaps left by the regrouping so the snake never pauses on an empty step.
  var used = []; cells.forEach(function (k) { if (used.indexOf(k.step) < 0) used.push(k.step); });
  used.sort(function (p, q) { return p - q; });
  cells.forEach(function (k) { k.step = used.indexOf(k.step); });
  STEPS = used.length;

  function smoothstep(a, b, x) { return smooth(a, b, x); }
  function easeInOut(x) { return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }
  function padD(k) { var p = 0.6; return 'M' + (k.x - p) + ' ' + (k.y - p) + 'h' + (CELL + 2 * p) + 'v' + (CELL + 2 * p) + 'h' + (-(CELL + 2 * p)) + 'z'; }

  // Both animations last 3 s. dots: [small, big] start times. The icon's outline is drawn by the snake from B0, one step every STEP.
  // ---- Motion with weight. The pixels fall in a spiral toward the C's centre, speeding up as they get closer
  // (ease-in); the snake picks up at that same speed and slows down as it reaches the tail, without stopping dead,
  // and the fill starts while the tail is still settling.
  var DOT_C = (function () {               // centres of the two pixels, measured off the real paths
    var s = document.createElementNS(NS, 'svg'); s.setAttribute('width', 0); s.setAttribute('height', 0); s.style.position = 'absolute';
    document.body.appendChild(s);
    return ISO.dots.map(function (d) { var p = el('path', { d: d }, s); var b = p.getBBox(); return [b.x + b.width / 2, b.y + b.height / 2]; });
  })();
  var ROUTE_LEN = 0; for (var si = 1; si < samples.length; si++) ROUTE_LEN += Math.hypot(samples[si][0] - samples[si - 1][0], samples[si][1] - samples[si - 1][1]);
  var SPIRALS = {
    wide:   { name: 'Media vuelta amplia', desc: 'Entran de lejos y dan media vuelta abierta antes de aterrizar.', turns: 0.5, extra: 22, power: 1.6, trail: 5, gap: 0.035, grow: 0.35, solid: false },
    three:  { name: 'Tres cuartos', desc: 'La actual: tres cuartos de vuelta, crecen de cola a sólido.', turns: 0.75, extra: 11, power: 1.7, trail: 5, gap: 0.035, grow: 0.35, solid: false },
    tight:  { name: 'Vuelta cerrada', desc: 'Una vuelta y cuarto pegada al icono, como un remolino.', turns: 1.25, extra: 8, power: 1.8, trail: 6, gap: 0.03, grow: 0.45, solid: false },
    comet:  { name: 'Cometa', desc: 'Tres cuartos de vuelta con una estela larga de píxeles sólidos que se apaga.', turns: 0.75, extra: 13, power: 1.7, trail: 8, gap: 0.028, grow: 0.5, solid: true }
  };
  var SNAKE_A = 0.3, EASE_K = 2.4;   // progress p = A·x + (1−A)·(1 − (1−x)^K): fast start, still moving at the tail
  function makeMotion(key) {
    var O = SPIRALS[key];
    var M = { key: key, O: O, ARRIVE: [[0, 0.8], [0.12, 0.92]] };
    M.spiralPos = function (c, u) {
      var cx = 24.75, cy = 24.5;
      var a1 = Math.atan2(c[1] - cy, c[0] - cx), r1 = Math.hypot(c[0] - cx, c[1] - cy);
      var e = Math.pow(clamp(u, 0, 1), O.power);
      var a = a1 + (1 - e) * Math.PI * 2 * O.turns;     // counter-clockwise on screen, like the C
      var r = r1 + (1 - e) * O.extra;
      return [cx + Math.cos(a) * r, cy + Math.sin(a) * r];
    };
    var c = DOT_C[0], span = M.ARRIVE[1][1] - M.ARRIVE[1][0], h = 0.002;
    var p1 = M.spiralPos(c, 1), p0 = M.spiralPos(c, 1 - h);
    M.LAND_V = Math.hypot(p1[0] - p0[0], p1[1] - p0[1]) / (h * span);
    M.B0 = M.ARRIVE[1][1];
    M.SNAKE_D = clamp(ROUTE_LEN * (SNAKE_A + (1 - SNAKE_A) * EASE_K) / M.LAND_V, 0.7, 1.6);   // first speed = landing speed
    M.ICON_END = M.B0 + M.SNAKE_D;
    M.snakeP = function (t) { var x = clamp((t - M.B0) / M.SNAKE_D, 0, 1); return SNAKE_A * x + (1 - SNAKE_A) * (1 - Math.pow(1 - x, EASE_K)); };
    var E = M.ICON_END, F0 = E - 0.12;   // the fill starts as the tail lands
    M.PLANS = {
      together:  { fill: [F0, F0 + 0.45], move: null, text: 0.98, traceEnd: F0, textMode: 'trace' },
      trace:     { fill: [F0, F0 + 0.35], move: [E + 0.1, E + 0.6], text: E + 0.5, traceEnd: E + 1.0, textFill: [E + 0.95, E + 1.35], textMode: 'trace' },
      emerge:    { fill: [F0, F0 + 0.35], move: [E + 0.1, E + 0.8], text: E + 0.1, traceEnd: E + 0.1, textFill: [E + 0.85, E + 1.35], textMode: 'emerge' },
      letters:   { fill: [F0, F0 + 0.35], move: [E + 0.1, E + 0.6], text: E + 0.5, traceEnd: E + 0.5, textFill: [E + 1.0, E + 1.35], textMode: 'letters' }
    };
    M.PLANS.together.textFill = M.PLANS.together.fill;   // icon, pixels and name fill at the same moment
    M.PLANS.icon = { fill: [F0, F0 + 0.45], move: null, text: 99, traceEnd: 99, textFill: [99, 100], textMode: 'trace' };   // gallery: icon only
    M.TOTAL = Math.max(3.0, E + 1.45);
    return M;
  }
  var SPIRAL_KEY = 'three';
  var M = makeMotion(SPIRAL_KEY), TOTAL = M.TOTAL;
  var CENTER_SHIFT = (200 - 49.5) / 2; // icon centred in the lockup before it slides left
  var LETTER_DUR = 0.32, LETTER_GAP = 0.09;

  function createLogo(svg, plan, mot) {
    var MM = mot || M, ORBIT = MM.O, ARRIVE = MM.ARRIVE, B0 = MM.B0, ICON_END = MM.ICON_END, spiralPos = MM.spiralPos, snakeP = MM.snakeP;
    var P = MM.PLANS[plan];
    var id = 'k' + (++uid);
    svg.setAttribute('viewBox', '-6 -6 216 60');
    var defs = el('defs', {}, svg);
    var shapeClip = el('clipPath', { id: id + 's' }, defs); el('path', { d: ISO.body }, shapeClip);
    var drawnClip = el('clipPath', { id: id + 'd' }, defs), drawnPath = el('path', { d: '' }, drawnClip);
    var glow = el('filter', { id: id + 'g', x: '-10%', y: '-30%', width: '120%', height: '160%' }, defs);
    el('feGaussianBlur', { 'in': 'SourceGraphic', stdDeviation: '0.6', result: 'b' }, glow);
    var mg = el('feMerge', {}, glow); el('feMergeNode', { 'in': 'b' }, mg); el('feMergeNode', { 'in': 'SourceGraphic' }, mg);

    var icon = el('g', {}, svg);
    var grid = el('g', { 'class': 'grid', visibility: 'hidden' }, icon);
    for (var i = 0; i <= COLS; i++) {
      el('line', { x1: i * CELL, y1: 0, x2: i * CELL, y2: ROWS * CELL }, grid);
      el('line', { x1: 0, y1: i * CELL, x2: COLS * CELL, y2: i * CELL }, grid);
    }
    var iconFill = el('path', { 'class': 'sym', d: ISO.body, opacity: 0 }, icon);
    // The head is a light veil under the outline, so the front of the snake keeps its edge.
    var headG = el('g', { 'clip-path': 'url(#' + id + 's)' }, icon);
    var heads = cells.map(function (k) { return el('rect', { 'class': 'cell pix', x: k.x - 0.02, y: k.y - 0.02, width: CELL + 0.04, height: CELL + 0.04, visibility: 'hidden' }, headG); });
    var outlineG = el('g', { 'clip-path': 'url(#' + id + 'd)' }, icon);
    var outlinePix = el('path', { 'class': 'trace t-pix', d: ISO.body, filter: 'url(#' + id + 'g)' }, outlineG);
    var outlineSym = el('path', { 'class': 'trace t-sym', d: ISO.body, opacity: 0 }, outlineG);
    // The two pixels: outline first (their stroke is already their fill colour), fill together with the rest.
    var dots = ISO.dots.map(function (d) {
      var trail = []; for (var q = 0; q < ORBIT.trail; q++) trail.push(el('path', ORBIT.solid ? { 'class': 'pix', d: d, visibility: 'hidden' } : { 'class': 'trace t-pix', d: d, visibility: 'hidden', 'vector-effect': 'non-scaling-stroke' }, icon));
      var g = el('g', { visibility: 'hidden' }, icon);
      return { g: g, trail: trail, fill: el('path', { 'class': 'pix', d: d, opacity: 0 }, g), line: el('path', { 'class': 'trace t-pix', d: d, filter: 'url(#' + id + 'g)', 'vector-effect': 'non-scaling-stroke' }, g) };
    });
    var centers = DOT_C;
    // Offset from home on the spiral, snapped to a quarter cell so it moves in pixel steps.
    function spiral(c, u) {
      var p = spiralPos(c, u), q = CELL / 4;
      return [Math.round((p[0] - c[0]) / q) * q, Math.round((p[1] - c[1]) / q) * q];
    }

    // 2B: the name fades in over a soft 12-unit edge instead of a hard cut, so no line shows where it comes out.
    var grad = el('linearGradient', { id: id + 'eg', gradientUnits: 'userSpaceOnUse', x1: 0, y1: 0, x2: 12, y2: 0 }, defs);
    el('stop', { offset: 0, 'stop-color': '#000' }, grad); el('stop', { offset: 1, 'stop-color': '#fff' }, grad);
    var emergeMask = el('mask', { id: id + 'e', maskUnits: 'userSpaceOnUse', x: -80, y: -20, width: 400, height: 100 }, defs);
    el('rect', { x: -80, y: -20, width: 400, height: 100, fill: 'url(#' + id + 'eg)' }, emergeMask);
    var wordOuter = el('g', P.textMode === 'emerge' ? { mask: 'url(#' + id + 'e)' } : {}, svg);
    var word = el('g', { transform: 'translate(' + WORD.x + ' ' + WORD.y + ')' }, wordOuter);
    var fillG = el('g', { opacity: 0 }, word);
    WORD.paths.forEach(function (d) { el('path', { 'class': 'word', d: d }, fillG); });
    var pixG = el('g', { filter: 'url(#' + id + 'g)', opacity: 0 }, word);
    var symG = el('g', { opacity: 0 }, word);
    var strokes = [];
    WORD.paths.forEach(function (d) {
      strokes.push(el('path', { 'class': 'trace t-pix', d: d, pathLength: 1, 'stroke-dasharray': '1 1', 'stroke-dashoffset': 1 }, pixG));
      strokes.push(el('path', { 'class': 'trace t-word', d: d, pathLength: 1, 'stroke-dasharray': '1 1', 'stroke-dashoffset': 1 }, symG));
    });
    var END = ICON_END;

    return {
      grid: grid,
      draw: function (t) {
        // the two pixels: the small one first, then the big one
        var f = smoothstep(P.fill[0], P.fill[1], t);
        var order = [1, 0];   // the small pixel (second path) first
        order.forEach(function (di, n) {
          var p = dots[di], c = centers[di], A = ARRIVE[n], span = A[1] - A[0];
          var u = (t - A[0]) / span;
          if (u <= 0) { p.g.setAttribute('visibility', 'hidden'); p.trail.forEach(function (tr) { tr.setAttribute('visibility', 'hidden'); }); return; }
          var o = spiral(c, Math.min(u, 1));
          // it travels as a small tail-end pixel and grows solid as it lands
          var s = ORBIT.grow + (1 - ORBIT.grow) * Math.pow(Math.min(u, 1), ORBIT.power);
          p.g.setAttribute('visibility', 'visible');
          p.g.setAttribute('transform', 'translate(' + (c[0] + o[0]) + ' ' + (c[1] + o[1]) + ') scale(' + s.toFixed(3) + ') translate(' + (-c[0]) + ' ' + (-c[1]) + ')');
          p.fill.setAttribute('opacity', f);
          // a short trail of outlines behind it while it travels
          p.trail.forEach(function (tr, k) {
            var uk = u - (k + 1) * ORBIT.gap / span;
            if (uk >= 1 || uk <= 0) { tr.setAttribute('visibility', 'hidden'); return; }
            var ok = spiral(c, Math.min(uk, 1)), sk = (ORBIT.grow + (1 - ORBIT.grow) * Math.pow(Math.min(uk, 1), ORBIT.power)) * (1 - (k + 1) * (0.5 / ORBIT.trail));
            tr.setAttribute('visibility', 'visible');
            tr.setAttribute('opacity', ((ORBIT.solid ? 0.7 : 0.5) * (1 - k / ORBIT.trail)).toFixed(2));
            tr.setAttribute('transform', 'translate(' + (c[0] + ok[0]) + ' ' + (c[1] + ok[1]) + ') scale(' + sk.toFixed(3) + ') translate(' + (-c[0]) + ' ' + (-c[1]) + ')');
          });
        });
        // the snake: each step reveals the real outline of the C inside the cells it covers
        var step = t < B0 ? -1 : Math.min(STEPS - 1, Math.floor(snakeP(t) * STEPS));
        if (step >= 0) {
          var d = ''; cells.forEach(function (k) { if (k.step <= step) d += padD(k); });
          drawnPath.setAttribute('d', d);
        }
        outlineG.setAttribute('visibility', step >= 0 ? 'visible' : 'hidden');
        cells.forEach(function (k, i) {
          var show = step >= 0 && t < END && (k.step === step || k.step === step - 1);
          heads[i].setAttribute('visibility', show ? 'visible' : 'hidden');
          if (show) heads[i].setAttribute('opacity', k.step === step ? 0.4 : 0.15);
        });
        // once the outline is complete: fill fades in and the stroke turns the fill colour
        iconFill.setAttribute('opacity', f);
        outlinePix.setAttribute('opacity', 1 - f);
        outlineSym.setAttribute('opacity', f);
        // second animation: the icon starts centred and slides to its place
        var mv = P.move ? easeInOut(clamp((t - P.move[0]) / (P.move[1] - P.move[0]), 0, 1)) : 1;
        var shift = P.move ? CENTER_SHIFT * (1 - mv) : 0;
        icon.setAttribute('transform', 'translate(' + shift.toFixed(3) + ' 0)');
        // the name: outline first, then the fill fades in and the stroke takes the fill colour
        var q = smoothstep(P.textFill[0], P.textFill[1], t);
        if (P.textMode === 'letters') {
          strokes.forEach(function (p, j) {
            var li = Math.floor(j / 2), s0 = P.text + li * LETTER_GAP;
            p.setAttribute('stroke-dashoffset', 1 - smoothstep(s0, s0 + LETTER_DUR, t));
          });
        } else {
          // 'emerge' shows the outline whole while it slides out from behind the icon
          var tr = P.textMode === 'emerge' ? 1 : smoothstep(P.text, P.traceEnd, t);
          strokes.forEach(function (p) { p.setAttribute('stroke-dashoffset', 1 - tr); });
        }
        if (P.textMode === 'emerge') {
          // starts with its right end tucked behind the centred icon and slides out to its place
          var x0 = CENTER_SHIFT + 44 - WORD.w, x = x0 + (WORD.x - x0) * mv;   // right end starts exactly at the fade edge
          word.setAttribute('transform', 'translate(' + x.toFixed(3) + ' ' + WORD.y + ')');
          var edge = shift + 44;                                          // fade starts inside the C's opening
          grad.setAttribute('x1', edge.toFixed(3)); grad.setAttribute('x2', (edge + 12).toFixed(3));
        }
        pixG.setAttribute('opacity', t > P.text ? 1 - q : 0);
        symG.setAttribute('opacity', t > P.text ? q : 0);
        fillG.setAttribute('opacity', q);
        // Sin líneas finas: un trazo ya completo se dibuja sin guiones (el corte del guion dejaba una costura
        // en el punto de inicio de cada letra) y la C completa ya no pasa por el recorte de celdas.
        strokes.forEach(function (p) { p.setAttribute('stroke-dasharray', parseFloat(p.getAttribute('stroke-dashoffset')) <= 1e-4 ? 'none' : '1 1'); });
        if (step >= STEPS - 1) outlineG.removeAttribute('clip-path'); else outlineG.setAttribute('clip-path', 'url(#' + id + 'd)');
      }
    };
  }


  return {create:createLogo,total:function(){return M.TOTAL},plans:function(){return M.PLANS}};
})();
