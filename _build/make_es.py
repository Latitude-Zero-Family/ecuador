import re,glob,json,html as H
D=json.load(open('es.json'))
SKIP=('script','style','svg','code')
def tr_text(html):
    out=[];i=0;stack=[]
    for m in re.finditer(r'<(/?)([a-zA-Z0-9]+)[^>]*?(/?)>|<!--.*?-->|<!doctype[^>]*>',html,re.S):
        txt=html[i:m.start()]
        st=txt.strip()
        if st and st in D and not any(t in SKIP for t in stack):
            txt=txt.replace(st,D[st],1)
        out.append(txt)
        tg=m.group(0)
        if m.group(2):
            tag=m.group(2).lower()
            if m.group(1):
                if tag in stack:
                    while stack and stack.pop()!=tag: pass
            elif tag in SKIP and not m.group(3): stack.append(tag)
            tg=re.sub(r'((?:alt|aria-label)=")([^"]+)(")',lambda a:a.group(1)+D.get(a.group(2),a.group(2))+a.group(3),tg)
            if tag=='meta' and re.search(r'(name|property)="(description|og:title|og:description)"',tg):
                tg=re.sub(r'(content=")([^"]+)(")',lambda a:a.group(1)+H.escape(D.get(H.unescape(a.group(2)),H.unescape(a.group(2))),quote=True)+a.group(3),tg)
        out.append(tg); i=m.end()
    out.append(html[i:]); return ''.join(out)
def esname(f): return 'es.html' if f in ('index.html','./') else f.replace('.html','-es.html')
def links(html):
    def rep(m):
        h=m.group(1)
        if h=='./': return 'href="es.html"'
        mm=re.fullmatch(r'([a-z0-9\-]+\.html)(#.*)?',h)
        if mm and not mm.group(1).endswith('-es.html') and mm.group(1)!='es.html': return f'href="{esname(mm.group(1))}{mm.group(2) or ""}"'
        return m.group(0)
    return re.sub(r'href="([^"]+)"',rep,html)
import re as _r
skel=_r.sub(r'<title>.*?</title>','<title>Latitude Zero</title>',open('about.html').read().split('<nav')[0])
for f in sorted(glob.glob('*.html')):
    if f.endswith('-es.html') or f=='es.html': continue
    h=open(f).read()
    if f=='index.html': h=skel+'<nav'+h.split('<nav',1)[1]+'\n</body>\n</html>\n'
    h=h.replace('<html lang="en">','<html lang="es">')
    en_href='./' if f=='index.html' else f
    h=re.sub(r'<a href="#" aria-current="true" lang="en">EN</a><a href="[^"]+" lang="es" hreflang="es">ES</a>','__LANG__',h)
    h=tr_text(h); h=links(h)
    # canonical, og:url and locale point at the Spanish page
    h=re.sub(r'(<link rel="canonical" href=")https://latitudezerofamily.com/([^"]*)(">)',lambda a:a.group(1)+'https://latitudezerofamily.com/'+esname(a.group(2) or 'index.html')+a.group(3),h)
    h=re.sub(r'(<meta property="og:url" content=")https://latitudezerofamily.com/([^"]*)(">)',lambda a:a.group(1)+'https://latitudezerofamily.com/'+esname(a.group(2) or 'index.html')+a.group(3),h)
    h=h.replace('<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="es_EC">','<meta property="og:locale" content="es_EC">\n<meta property="og:locale:alternate" content="en_US">')
    def ld(a):
        o=json.loads(a.group(1))
        def walk(x):
            if isinstance(x,dict): return {k:(walk(v) if k not in ('@type','@context','url','logo','email','image','mainEntityOfPage','datePublished') else v) for k,v in x.items()}
            if isinstance(x,list): return [walk(v) for v in x]
            if isinstance(x,str): return D.get(x,x)
            return x
        o=walk(o)
        if 'inLanguage' in o and o['inLanguage']=='en': o['inLanguage']='es'
        s_=json.dumps(o,ensure_ascii=False)
        s_=re.sub(r'https://latitudezerofamily.com/([a-z0-9-]+)\.html',lambda b:'https://latitudezerofamily.com/'+esname(b.group(1)+'.html'),s_)
        return '<script type="application/ld+json">'+s_+'</script>'
    h=re.sub(r'<script type="application/ld\+json">(.*?)</script>',ld,h)
    h=h.replace('__LANG__',f'<a href="{en_href}" lang="en" hreflang="en">EN</a><a href="#" aria-current="true" lang="es">ES</a>')
    h=h.replace("' of '","' de '").replace("' visited'","' visitados'").replace("'Copied'","'Copiado'").replace("'Copy email'","'Copiar correo'").replace("'Selected'","'Seleccionado'").replace("' done'","' listos'").replace("'Your pick: '","'Tu elección: '").replace("'. Tell us why on Instagram @latitudezerofamily!'","'. ¡Cuéntanos por qué en Instagram @latitudezerofamily!'").replace("'Choose a place first.'","'Primero elige un lugar.'").replace("'Copy link'","'Copiar enlace'").replace("' days to go'","' días para la mudanza'").replace("'1 day to go'","'Falta 1 día'").replace("'We made it!'","'¡Llegamos!'")
    open(esname(f),'w').write(h)
    print(esname(f))
