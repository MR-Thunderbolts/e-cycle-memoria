import re, sys, markdown
import os; HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from blocks import BLOCKS
from diagrams import D
BLOCKS.update(D)
from diagrams2 import D as D2
BLOCKS['USERFLOW']=re.sub(r'<svg.*?</svg>', lambda m: D2['USERFLOW_SVG'], BLOCKS['USERFLOW'], count=1, flags=re.S)
for k in ('DIAMOND','ACTORS','FODA','HITOS','LADDER'): BLOCKS[k]=D2[k]
from diagrams3 import D as D3
BLOCKS.update(D3)

src = open(os.path.join(HERE,'content.md')).read()
logo_js = open(os.path.join(HERE,'logo-anim.js')).read()
parts = re.split(r'<!--CH (.+?)-->', src)
chapters = []
for i in range(1, len(parts), 2):
    cid, num, title, lead = parts[i].split('|')
    md = parts[i+1]
    html = markdown.markdown(md, extensions=['tables', 'attr_list'])
    for k, v in BLOCKS.items():
        html = html.replace(f'<!--{k}-->', v)
    subs = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    chapters.append(dict(id=cid, num=num, title=title, lead=lead, html=html, subs=subs))

nav = ''
for c in chapters:
    sub = ''.join(f'<li><a href="#{sid}">{re.sub("<.*?>","",t)}</a></li>' for sid, t in c['subs']) if len(c['subs']) > 1 else ''
    nav += f'<li><a class="ch" href="#{c["id"]}"><span>{c["num"]}</span>{c["title"]}</a>' + (f'<ol>{sub}</ol>' if sub else '') + '</li>'

body = ''
for c in chapters:
    body += f'''
<section class="chapter" id="{c["id"]}">
  <header class="opener"><div class="pxgrid" data-cols="18"></div>
    <div class="op-in"><span class="eyebrow">Capítulo</span><span class="op-num">{c["num"]}</span><h2 class="op-title">{c["title"]}</h2><p class="op-lead">{c["lead"]}</p></div>
  </header>
  <div class="prose">{c["html"]}</div>
</section>'''

tpl = open(os.path.join(HERE,'template.html')).read()
out = tpl.replace('{{NAV}}', nav).replace('{{BODY}}', body).replace('{{LOGOJS}}', logo_js)
open(os.path.join(HERE,'..','index.html'), 'w').write(out)
print('ok', len(out), [c['id'] for c in chapters])
