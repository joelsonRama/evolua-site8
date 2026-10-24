import pathlib, re

OLD = pathlib.Path('/tmp/claude-0/-home-user-giropdv-server/b586bf02-3b37-5632-ad1c-ff0144760db1/scratchpad/build_old.py').read_text()
exec(OLD[OLD.index('def ic('):OLD.index('NAV = [')])  # ic() e I{} (ícones)

def _i(d): return ic(d)
I.update({
    'music': _i('<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>'),
    'flag': _i('<path d="M4 22V4a1 1 0 0 1 1-1h12l-2 4 2 4H5"/>'),
    'cup': _i('<path d="M5 3h14l-1.5 17a2 2 0 0 1-2 1.8h-7a2 2 0 0 1-2-1.8Z"/><path d="M5.5 8h13"/>'),
    'store': _i('<path d="M3 9 4.5 4h15L21 9"/><path d="M3 9h18v2a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0Z"/><path d="M5 13v8h14v-8"/>'),
    'trophy': _i('<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0Z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>'),
    'file': _i('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>'),
    'lock': _i('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
    'bluetooth': _i('<path d="m7 7 10 10-5 5V2l5 5L7 17"/>'),
    'nfc': _i('<path d="M6 8.3a6 6 0 0 1 0 7.4M9.5 6a10 10 0 0 1 0 12M13 4a14 14 0 0 1 0 16"/>'),
})

OUT = pathlib.Path('/home/user/evolua-site8')
PAINEL = 'https://painel.evoluatecnologia.com.br'
CLIENTE = PAINEL + '/index.php'
VENDEDOR = PAINEL + '/vendedor.php'
DOMAIN = 'https://www.evoluatecnologia.com.br'

NAV = [
    ('index.html', 'Início'),
    ('evolua-ticket.html', 'Evolua Ticket'),
    ('index.html#compatibilidade', 'Maquininhas'),
    ('index.html#produtos', 'Produtos'),
    ('contato.html', 'Contato'),
]

def brand():
    return ('<a class="brand" href="index.html" aria-label="Evolua Tecnologia - início">'
            '<img src="assets/img/evolua-mark.svg" alt="" width="34" height="34">'
            '<span><span class="brand-name">Evolua</span><span class="brand-sub">Tecnologia</span></span></a>')

def header(active):
    links = ''.join(f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''<header class="header">
  <div class="wrap">
    {brand()}
    <button class="menu-btn" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu">{I['menu']}</button>
    <nav class="nav" id="menu" aria-label="Menu principal">
      {links}
      <a class="btn btn-primary btn-sm" href="acesso.html">{I['user']} Acessar painel</a>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        {brand()}
        <p class="about">A Evolua Tecnologia desenvolve sistemas de venda para maquininhas Android: rápidos no caixa, simples de usar e prontos para funcionar sem internet.</p>
        <p class="company" data-contact="empresa" hidden><span data-contact-text></span></p>
      </div>
      <div>
        <h4>Produtos</h4>
        <ul>
          <li><a href="evolua-ticket.html">Evolua Ticket</a></li>
          <li><a href="evolua-parking.html">Evolua Parking</a></li>
          <li><a href="evolua-pdv.html">Evolua PDV</a></li>
          <li><a href="index.html#compatibilidade">Maquininhas compatíveis</a></li>
        </ul>
      </div>
      <div>
        <h4>Acesso</h4>
        <ul>
          <li><a href="{CLIENTE}">Painel do Cliente</a></li>
          <li><a href="{VENDEDOR}">Painel do Vendedor</a></li>
          <li><a href="privacidade.html">Política de Privacidade</a></li>
          <li><a href="termos.html">Termos de Uso</a></li>
        </ul>
      </div>
      <div>
        <h4>Contato</h4>
        <ul>
          <li><a href="contato.html">Fale conosco</a></li>
          <li><a data-contact="whatsapp" hidden>WhatsApp: <span data-contact-text></span></a></li>
          <li><a data-contact="email" hidden><span data-contact-text></span></a></li>
          <li><a data-contact="instagram" hidden>Instagram: <span data-contact-text></span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Evolua Tecnologia. Todos os direitos reservados.</span>
      <span>Desenvolvido por <b>Evolua Tecnologia</b></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="contato.html" aria-label="Falar no WhatsApp" hidden>{I['whatsapp']}</a>
<script src="assets/js/main.js?v=202610241849"></script>'''

def page(file, title, desc, active, body):
    url = DOMAIN + ('/' if file == 'index.html' else '/' + file)
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0a0a0c">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Evolua Tecnologia">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<link rel="icon" type="image/svg+xml" href="assets/img/evolua-icon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v=202610241849">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
'''
    (OUT / file).write_text(html, encoding='utf-8')

# ---------------------------------------------------------------- peças
def li_check(items):
    return ''.join(f'<li>{I["circle_check"]}<span>{t}</span></li>' for t in items)

def features(items, cols=''):
    return f'<div class="features {cols}">' + ''.join(
        f'<div class="feature reveal"><div class="f-ic">{I[k]}</div><h3>{t}</h3><p>{d}</p></div>' for k, t, d in items) + '</div>'

def app(event, status, chips, items, count, total):
    ch = ''.join(f'<span{" class=\"on\"" if i == 0 else ""}>{c}</span>' for i, c in enumerate(chips))
    it = ''.join(f'<div style="--c:{c}">{"<em>" + str(q) + "</em>" if q else ""}<b>{n}</b><small>{p}</small></div>' for n, p, c, q in items)
    return (f'<div class="app"><div class="app-top"><i class="app-menu"></i><img src="assets/img/evolua-mark.svg" alt="">'
            f'<div><b>EVOLUA <span>TICKET</span></b><strong>{event}</strong><small><i></i>{status}</small></div></div>'
            f'<div class="app-chips">{ch}</div><div class="app-grid">{it}</div>'
            f'<div class="app-bottom"><div><small>{count} • toque para ver</small><b>{total}</b></div><span>COBRAR</span></div></div>')

def paper(item, sub):
    return f'<div class="paper"><b>EVOLU<i>A</i> TICKET</b><strong>{item}</strong><small>{sub}</small><hr><div class="code"></div></div>'

B, O, G, P = '#2b8cff', '#f59e0b', '#22c55e', '#a855f7'
SCR_BEBIDAS = app('Festa da Cidade', 'Online • Caixa 03', ['Bebidas', 'Comidas', 'Doces'],
    [('Cerveja', 'R$ 12,00', B, 2), ('Refrigerante', 'R$ 7,00', B, 0), ('Água', 'R$ 5,00', B, 1),
     ('Chopp', 'R$ 14,00', B, 0), ('Suco', 'R$ 8,00', B, 0), ('Energético', 'R$ 15,00', B, 0)], '3 itens', 'R$ 29,00')
SCR_COMIDAS = app('Quermesse São José', 'Online • Barraca 2', ['Comidas', 'Bebidas'],
    [('Pastel', 'R$ 10,00', O, 1), ('Espetinho', 'R$ 15,00', O, 0), ('Cachorro-quente', 'R$ 9,00', O, 1),
     ('Pipoca', 'R$ 6,00', O, 0), ('Milho', 'R$ 7,00', O, 0), ('Canjica', 'R$ 8,00', O, 0)], '2 itens', 'R$ 19,00')
SCR_COMBOS = app('Show na Praça', 'Sem internet • vendas guardadas', ['Combos', 'Bebidas', 'Lanches'],
    [('Combo Casal', 'R$ 45,00', P, 1), ('Combo Galera', 'R$ 89,00', P, 0), ('Balde 6 un.', 'R$ 60,00', G, 0),
     ('Dose', 'R$ 20,00', G, 0), ('Porção', 'R$ 35,00', O, 0), ('Água', 'R$ 5,00', B, 0)], '1 item', 'R$ 45,00')

def device(kind, screen, ticket=None):
    cls = {'gpos': 'dv yellow', 'a930': 'dv short', 'p2': 'dv slim yellow', 'pos': 'dv light', 'phone': 'dv phone'}[kind]
    head = '' if kind == 'phone' else '<div class="dv-head"></div>'
    extra = '' if kind in ('phone', 'p2') else '<div class="dv-chin"></div><div class="dv-slot"></div>'
    if kind == 'p2': extra = '<div class="dv-chin"></div>'
    return f'<div class="{cls}" aria-hidden="true">{ticket or ""}{head}<div class="dv-screen">{screen}</div>{extra}</div>'

def fig(dev, model, sub):
    return f'<figure>{dev}<figcaption><b>{model}</b>{sub}</figcaption></figure>'

ACQUIRERS = ['Getnet', 'Rede Itaú', 'Sicredi', 'Caixa', 'Sipag', 'Bin', 'Clover', 'BoltCard']

COMPAT = f'''<section class="section section-soft" id="compatibilidade">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Evolua Ticket</span>
      <h2>Venda, cobrança e impressão em um único equipamento</h2>
      <p>O Evolua Ticket transforma a maquininha de cartão em um ponto de venda completo: o operador seleciona os produtos, recebe no cartão ou no PIX e entrega a ficha impressa na hora, com QR Code para conferência. Tudo sincronizado em tempo real com o painel de gestão.</p>
    </div>
    <div class="compat">
      <article class="compat-card wide reveal">
        <div class="compat-head"><div><h3>Na maquininha de cartão</h3><small>Pagamento integrado, impressão das fichas e leitura NFC no mesmo aparelho</small></div><span class="pill">Tudo em um</span></div>
        <div class="compat-devices real">
          <figure><img src="assets/img/maquininhas/ficha-moderninha-smart-2.webp" alt="Ficha do Evolua Ticket saindo da Moderninha Smart 2" loading="lazy"><figcaption><b>PagBank</b>Moderninha Smart 2</figcaption></figure>
          <figure><img src="assets/img/maquininhas/ficha-stone.webp" alt="Ficha do Evolua Ticket saindo da maquininha Stone" loading="lazy"><figcaption><b>Stone</b>POS Android</figcaption></figure>
          <figure><img src="assets/img/maquininhas/ficha-cielo.webp" alt="Ficha do Evolua Ticket saindo da Cielo LIO" loading="lazy"><figcaption><b>Cielo</b>LIO</figcaption></figure>
        </div>
      </article>
      <article class="compat-card phone-card reveal">
        <div class="compat-head"><div><h3>No celular</h3><small>Android com impressora térmica Bluetooth para barracas e pontos extras</small></div><span class="pill blue">Mobilidade</span></div>
        <div class="compat-devices real">
          <figure class="phone-set"><img src="assets/img/maquininhas/celular-impressora.webp" alt="Evolua Ticket no celular Android com a ficha saindo da impressora Bluetooth" loading="lazy"><figcaption><b>Android</b>+ impressora Bluetooth</figcaption></figure>
        </div>
      </article>
    </div>
  </div>
</section>'''

TICKET_FEATURES = [
    ('card', 'Cartão e PIX na maquininha', 'A cobrança é feita pelo próprio aplicativo de pagamento da credenciadora, sem digitar valor duas vezes.'),
    ('printer', 'Fichas impressas na hora', 'Cada item sai em uma ficha própria, pronta para trocar no balcão. Também envia pedidos para a impressora da cozinha.'),
    ('wifi_off', 'Funciona sem internet', 'As vendas ficam guardadas na maquininha e sobem sozinhas para o painel quando a conexão volta, sem duplicar.'),
    ('cash', 'Controle de caixa', 'Abertura, sangria e fechamento de caixa por operador, com conferência de valores.'),
    ('undo', 'Estorno seguro', 'Cancelamento protegido por senha ou cartão NFC de administrador, com tudo registrado.'),
    ('chart', 'Relatórios completos', 'Totais de vendas, vendas por operador, quantidade vendida e caixa, com exportação em PDF.'),
    ('monitor', 'Monitor das máquinas', 'Bateria, conexão e situação de cada maquininha do evento em tempo real.'),
    ('team', 'Equipe e despesas', 'Cadastro de funcionários e despesas para chegar ao lucro real do evento.'),
    ('shield', 'Acesso protegido', 'Cada maquininha é ativada por licença e o painel é acessado com login e senha.'),
]

STEPS = '''<div class="steps">
      <div class="step reveal"><h3>Crie seu evento</h3><p>No painel, o evento fica pronto em poucos cliques e já aparece nas maquininhas.</p></div>
      <div class="step reveal"><h3>Cadastre seus produtos</h3><p>Grupos, produtos, preços e fotos, pelo computador ou pelo celular.</p></div>
      <div class="step reveal"><h3>Saia vendendo</h3><p>Selecione os produtos, receba o pagamento e entregue a ficha impressa em poucos segundos.</p></div>
    </div>'''

PANEL = f'''<div class="panel reveal" aria-hidden="true">
      <div class="panel-bar"><i></i><i></i><i></i><span>Painel do cliente • Evolua Ticket</span></div>
      <div class="panel-body">
        <div class="panel-side"><img src="assets/img/evolua-mark.svg" alt=""><i class="on"></i><i></i><i></i><i></i><i></i><i></i></div>
        <div class="panel-main">
          <h4>Festa da Cidade • Visão geral</h4>
          <div class="kpis">
            <div class="kpi"><small>Vendido hoje</small><b>R$ 18.420</b></div>
            <div class="kpi"><small>Fichas</small><b>1.536</b></div>
            <div class="kpi"><small>Caixas abertos</small><b>8</b></div>
          </div>
          <div class="bars"><i style="height:35%"></i><i style="height:52%"></i><i style="height:44%"></i><i style="height:70%"></i><i style="height:62%"></i><i style="height:88%"></i><i style="height:100%"></i><i style="height:76%"></i></div>
        </div>
      </div>
    </div>'''

def browser(img, alt, title):
    return f'<figure class="shot reveal"><div class="shot-bar"><i></i><i></i><i></i><span>{title}</span></div><img src="assets/img/painel/{img}.webp" alt="{alt}" loading="lazy"></figure>'

def panel_section(cta=True):
    btn = f'<div class="hero-actions"><a class="btn btn-primary" href="{CLIENTE}">Acessar o painel {I["arrow"]}</a></div>' if cta else ''
    return f'''<section class="section panel-section" id="painel">
  <div class="wrap">
    <div class="split panel-intro">
      <div class="reveal">
        <span class="kicker">Painel de gestão</span>
        <h2>Controle total do seu evento, em tempo real</h2>
        <p>Cada venda feita na maquininha chega ao painel em segundos. Você acompanha o faturamento por forma de pagamento, o ticket médio e os produtos mais vendidos, do computador ou do celular, de onde estiver.</p>
        <ul class="checklist">{li_check(['Faturamento em dinheiro, PIX, débito e crédito separado', 'Vários eventos e maquininhas na mesma conta', 'Relatórios de vendas, operadores e caixas em PDF', 'Acesso seguro com login e senha'])}</ul>
        {btn}
      </div>
      {browser('dashboard', 'Painel do cliente do Evolua Ticket com o faturamento do evento', 'Painel do Cliente • Dashboard')}
    </div>
    <div class="panel-duo">
      <div class="duo-item reveal">
        {browser('graficos', 'Gráficos de produtos, grupos, venda anual e eventos no painel do Evolua Ticket', 'Painel do Cliente • Indicadores')}
        <h3>Indicadores que orientam a decisão</h3>
        <p>Descubra o que mais vende, qual grupo fatura mais e como cada evento se compara aos anteriores. Informação clara para ajustar o cardápio, a equipe e o estoque.</p>
      </div>
      <div class="duo-item reveal">
        {browser('monitor', 'Monitor das máquinas do Evolua Ticket com bateria, caixa e vendas de cada maquininha', 'Painel do Cliente • Monitor das máquinas')}
        <h3>Monitor das máquinas</h3>
        <p>Veja cada maquininha ao vivo: conexão, bateria, operador, caixa aberto, vendas por forma de pagamento, dinheiro na gaveta e fichas impressas. O sistema avisa quando é hora de fazer sangria ou colocar a máquina no carregador.</p>
      </div>
    </div>
  </div>
</section>'''

USES = f'''<div class="uses">
      <span>{I['flag']} Festas e quermesses</span><span>{I['music']} Shows e festivais</span><span>{I['trophy']} Eventos esportivos</span>
      <span>{I['cup']} Bares e food parks</span><span>{I['calendar']} Feiras e exposições</span>
    </div>'''

def cta(title, text):
    return f'''<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="actions"><a class="btn btn-white" href="contato.html">Fale conosco</a><a class="btn btn-ghost" href="{CLIENTE}">Área do cliente</a></div>
    </div>
  </div>
</section>'''

def real_dev(file, alt, cls=''):
    return f'<figure class="real-dev {cls}"><img src="assets/img/maquininhas/{file}.webp" alt="{alt}" loading="eager"><span class="stamp">Em breve</span></figure>'

REAL_DEVICES = f'''<div class="real-devices">
      {real_dev('moderninha-smart-2', 'Evolua Ticket na maquininha Moderninha Smart 2 da PagBank')}
      {real_dev('stone', 'Evolua Ticket na maquininha da Stone', 'mid')}
      {real_dev('cielo', 'Evolua Ticket na maquininha Cielo LIO')}
    </div>'''

HERO_BRAND = f'''<section class="hero hero-brand">
  <div class="wrap">
    <div>
      <div class="lockup" role="img" aria-label="Evolua Tecnologia">
        <img src="assets/img/evolua-mark.svg" alt="" width="84" height="84">
        <div><b>EVOLU<i>A</i></b><small>TECNOLOGIA</small></div>
      </div>
      <h1>Software de vendas <span class="hl">integrado às maquininhas de cartão</span></h1>
      <p class="lead">A Evolua Tecnologia desenvolve soluções de automação comercial para terminais POS Android. Nosso principal produto, o Evolua Ticket, reúne venda, pagamento e emissão de fichas em um único equipamento, com gestão completa em tempo real pela nuvem.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="evolua-ticket.html">Conhecer o Evolua Ticket {I['arrow']}</a>
        <a class="btn btn-outline" href="contato.html">Fale com a gente</a>
      </div>
    </div>
    {REAL_DEVICES}
  </div>
</section>'''

HERO_DEVICES = f'''<div class="hero-devices">
      {device('a930', SCR_COMIDAS)}
      {device('gpos', SCR_BEBIDAS, paper('1x CERVEJA', 'Festa da Cidade'))}
      {device('p2', SCR_COMBOS)}
    </div>'''

# ---------------------------------------------------------------- INÍCIO
page('index.html',
     'Evolua Tecnologia | Sistemas de venda para maquininhas Android',
     'A Evolua Tecnologia desenvolve o Evolua Ticket, sistema de venda de fichas para eventos que roda direto na maquininha de cartão: cobra no cartão e no PIX, imprime as fichas e funciona sem internet.',
     'index.html', f'''
{HERO_BRAND}


<section class="strip">
  <div class="wrap">
    <div>{I['card']} Pagamento integrado</div>
    <div>{I['printer']} Impressão na maquininha</div>
    <div>{I['wifi_off']} Modo offline</div>
    <div>{I['chart']} Painel em tempo real</div>
  </div>
</section>

{COMPAT}

{panel_section(cta=False)}

<section class="section section-compact">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Como funciona</span>
      <h2>Do cadastro à venda em minutos</h2>
    </div>
    {STEPS}
  </div>
</section>

<section class="section section-soft">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Recursos</span>
      <h2>Feito para quem não pode parar de vender</h2>
      <p>Fila andando, caixa batendo e o organizador acompanhando tudo de qualquer lugar.</p>
    </div>
    {features(TICKET_FEATURES[:6])}
  </div>
</section>



<section class="section section-compact">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Para quem</span>
      <h2>Onde o Evolua Ticket trabalha</h2>
    </div>
    {USES}
  </div>
</section>

{cta('Quer conhecer o Evolua Ticket?', 'Fale com a nossa equipe para tirar dúvidas e agendar uma demonstração, ou acesse a área do cliente.')}

<section class="section section-soft" id="produtos">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Produtos Evolua</span>
      <h2>Uma família de sistemas para quem vende</h2>
      <p>Começamos pelos eventos e estamos levando a mesma tecnologia para estacionamentos e para o comércio.</p>
    </div>
    <div class="products">
      <article class="product reveal">
        <div class="p-ic">{I['ticket']}</div>
        <h3>Evolua Ticket</h3><span class="pill">Em operação</span>
        <p>Venda de fichas para eventos direto na maquininha, com pagamento, impressão, caixa e relatórios.</p>
        <a class="btn btn-outline btn-sm" href="evolua-ticket.html">Ver detalhes {I['arrow']}</a>
      </article>
      <article class="product reveal">
        <div class="p-ic amber">{I['parking']}</div>
        <h3>Evolua Parking</h3><span class="pill amber">Em desenvolvimento</span>
        <p>Controle de entrada e saída de veículos, cobrança por tempo e ticket impresso para estacionamentos.</p>
        <a class="btn btn-outline btn-sm" href="evolua-parking.html">Ver detalhes {I['arrow']}</a>
      </article>
      <article class="product reveal">
        <div class="p-ic cyan">{I['pdv']}</div>
        <h3>Evolua PDV</h3><span class="pill blue">Em breve</span>
        <p>Ponto de venda para o comércio, feito para computador Windows e com versão para Android.</p>
        <a class="btn btn-outline btn-sm" href="evolua-pdv.html">Ver detalhes {I['arrow']}</a>
      </article>
    </div>
  </div>
</section>
''')

# ---------------------------------------------------------------- TICKET
page('evolua-ticket.html',
     'Evolua Ticket | Sistema de fichas para eventos na maquininha | Evolua Tecnologia',
     'Evolua Ticket: sistema de venda de fichas para eventos que roda na maquininha de cartão Android, com pagamento no cartão e PIX, impressão das fichas, modo offline, controle de caixa e relatórios.',
     'evolua-ticket.html', f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Evolua Ticket</span>
      <h1>Sistema de fichas para eventos <span class="hl">na maquininha de cartão</span></h1>
      <p class="lead">Venda, cobrança e impressão no mesmo aparelho. O operador toca nos produtos, cobra no cartão ou no PIX e a ficha sai na hora. O organizador acompanha tudo pelo painel.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#compatibilidade">Maquininhas compatíveis {I['arrow']}</a>
        <a class="btn btn-outline" href="contato.html">Falar com a Evolua</a>
      </div>
      <div class="hero-checks">
        <span>{I['circle_check']} Cartão e PIX</span><span>{I['circle_check']} Impressão integrada</span><span>{I['circle_check']} Modo offline</span>
      </div>
    </div>
    {REAL_DEVICES}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Como funciona</span>
      <h2>Simples para o operador, completo para o organizador</h2>
    </div>
    {STEPS}
  </div>
</section>

{COMPAT}

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Recursos</span>
      <h2>Tudo o que o evento precisa</h2>
      <p>Do primeiro produto cadastrado ao relatório final do evento.</p>
    </div>
    {features(TICKET_FEATURES)}
  </div>
</section>

{panel_section()}

<section class="section section-soft">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Para quem</span>
      <h2>Onde o Evolua Ticket trabalha</h2>
    </div>
    {USES}
  </div>
</section>

{cta('Quer ver o Evolua Ticket funcionando?', 'Fale com a nossa equipe para agendar uma demonstração na maquininha, ou acesse a área do cliente.')}
''')

# ---------------------------------------------------------------- PARKING / PDV
def interest_form(produto):
    return f'''<form class="form-card reveal" data-send="Quero saber mais sobre o {produto}">
      <h3>Quero ser avisado</h3>
      <p>Deixe seu contato e avisamos quando o {produto} estiver disponível.</p>
      <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" data-label="Nome" required autocomplete="name"></div>
      <div class="field-row">
        <div class="field"><label for="f-tel">WhatsApp</label><input id="f-tel" name="whatsapp" data-label="WhatsApp" inputmode="tel" required autocomplete="tel"></div>
        <div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" data-label="Cidade" autocomplete="address-level2"></div>
      </div>
      <div class="field"><label for="f-neg">Seu negócio</label><input id="f-neg" name="negocio" data-label="Negócio"></div>
      <input class="hp" type="text" name="site" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary btn-block" type="submit">Quero ser avisado</button>
      <p class="form-note">A nossa equipe retorna pelo WhatsApp informado.</p>
    </form>'''

page('evolua-parking.html',
     'Evolua Parking | Sistema para estacionamentos | Evolua Tecnologia',
     'Evolua Parking: sistema para estacionamentos com entrada e saída por placa, cobrança por tempo, ticket impresso e mensalistas. Em desenvolvimento pela Evolua Tecnologia.',
     'evolua-parking.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow amber"><i class="dot"></i> Em desenvolvimento</span>
      <h1>Evolua <span class="hl">Parking</span></h1>
      <p class="lead">O sistema para estacionamentos da Evolua: entrada e saída rápidas, cobrança certa por tempo e o controle do pátio na maquininha.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="#avise-me">Quero ser avisado {I['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">O que está planejado</span>
      <h2>Tudo para o estacionamento</h2>
      <p>Os recursos abaixo fazem parte do projeto e podem mudar até o lançamento.</p>
    </div>
    {features([
        ('car', 'Entrada e saída por placa', 'Registro rápido do veículo na entrada e cálculo automático na saída.'),
        ('clock', 'Cobrança por tempo', 'Tabelas por fração, hora, diária e período.'),
        ('printer', 'Ticket impresso', 'Comprovante de entrada e de pagamento impressos na maquininha.'),
        ('repeat', 'Mensalistas', 'Cadastro de mensalistas com controle de vencimento.'),
        ('wifi_off', 'Funciona sem internet', 'A mesma base offline do Evolua Ticket.'),
        ('chart', 'Relatórios', 'Movimento por dia, ocupação, caixa e faturamento pelo painel.'),
    ])}
  </div>
</section>

<section class="section section-soft" id="avise-me">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Andamento</span>
      <h2>Construído sobre o que já funciona</h2>
      <p>O Evolua Parking aproveita a base do Evolua Ticket: painel na nuvem, maquininhas Android, pagamento integrado e vendas offline.</p>
      <div class="roadmap">
        <div class="rm done"><small>Pronto</small><h4>Base da plataforma</h4><p>Painel, licenças, pagamento integrado e sincronização offline.</p></div>
        <div class="rm"><small>Agora</small><h4>Desenvolvimento do Parking</h4><p>Telas de entrada e saída, tabelas de preço e mensalistas.</p></div>
        <div class="rm"><small>Depois</small><h4>Lançamento</h4><p>Liberação para os primeiros estacionamentos parceiros.</p></div>
      </div>
    </div>
    {interest_form('Evolua Parking')}
  </div>
</section>
''')

page('evolua-pdv.html',
     'Evolua PDV | Ponto de venda para Windows e Android | Evolua Tecnologia',
     'Evolua PDV: ponto de venda para o comércio, feito para computador Windows e com versão para Android. Em breve pela Evolua Tecnologia.',
     'evolua-pdv.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Em breve</span>
      <h1>Evolua <span class="hl">PDV</span></h1>
      <p class="lead">O ponto de venda da Evolua para o comércio. Feito principalmente para o computador do caixa, com versão para Android quando for preciso vender em qualquer lugar.</p>
      <div class="platforms">
        <span class="platform">{I['windows']} Windows <small>principal</small></span>
        <span class="platform">{I['android']} Android <small>também</small></span>
      </div>
      <div class="hero-actions"><a class="btn btn-primary" href="#avise-me">Quero ser avisado {I['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">O que está planejado</span>
      <h2>Um caixa completo para o comércio</h2>
      <p>Os recursos abaixo fazem parte do projeto e podem mudar até o lançamento.</p>
    </div>
    {features([
        ('zap', 'Venda rápida no balcão', 'Busca por código ou nome, atalhos de teclado e leitor de código de barras.'),
        ('box', 'Estoque', 'Entradas, saídas e aviso de estoque baixo.'),
        ('cash', 'Caixa', 'Abertura, sangria, suprimento e fechamento por operador.'),
        ('card', 'Várias formas de pagamento', 'Dinheiro, cartão e PIX na mesma venda.'),
        ('layers', 'Windows e Android', 'O mesmo sistema no computador do caixa e na maquininha.'),
        ('chart', 'Relatórios na nuvem', 'Vendas e produtos pelo painel, de onde estiver.'),
    ])}
  </div>
</section>

<section class="section section-soft" id="avise-me">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Para quem é</span>
      <h2>Feito para o dia a dia do comércio</h2>
      <p>Mercadinhos, lanchonetes, lojas, conveniências e qualquer negócio que precisa de um caixa rápido e confiável.</p>
      <ul class="checklist">{li_check(['Funciona no computador que você já tem', 'Continua vendendo se a internet cair', 'Mesmo suporte e mesmo painel da família Evolua'])}</ul>
    </div>
    {interest_form('Evolua PDV')}
  </div>
</section>
''')

# ---------------------------------------------------------------- ACESSO
page('acesso.html', 'Acessar painel | Evolua Tecnologia', 'Acesse o Painel do Cliente ou o Painel do Vendedor da Evolua Tecnologia.', 'acesso.html', f'''
<section class="hero hero-sm">
  <div class="wrap" style="text-align:center">
    <div>
      <span class="eyebrow"><i class="dot"></i> Área restrita</span>
      <h1>Acessar <span class="hl">painel</span></h1>
      <p class="lead" style="margin:0 auto">Escolha o seu tipo de acesso.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="access-big">
      <div class="card reveal">
        <div class="ic">{I['user']}</div>
        <h2>Painel do Cliente</h2>
        <p>Para quem usa o Evolua Ticket no seu evento ou negócio.</p>
        <ul>
          <li>{I['check']}<span>Eventos, produtos e operadores</span></li>
          <li>{I['check']}<span>Vendas e caixas em tempo real</span></li>
          <li>{I['check']}<span>Relatórios e maquininhas</span></li>
        </ul>
        <a class="btn btn-primary btn-block" href="{CLIENTE}">Entrar como cliente {I['arrow']}</a>
      </div>
      <div class="card reveal">
        <div class="ic cyan">{I['briefcase']}</div>
        <h2>Painel do Vendedor</h2>
        <p>Para os vendedores e revendedores parceiros da Evolua.</p>
        <ul>
          <li>{I['check']}<span>Cadastro e acompanhamento de clientes</span></li>
          <li>{I['check']}<span>Licenças dos clientes</span></li>
          <li>{I['check']}<span>Comissões e repasses</span></li>
        </ul>
        <a class="btn btn-primary btn-block" href="{VENDEDOR}" style="background:#0891b2;box-shadow:0 10px 24px rgba(8,145,178,.25)">Entrar como vendedor {I['arrow']}</a>
      </div>
    </div>
    <p class="help-line reveal">Esqueceu a senha? <a href="contato.html">Fale com o suporte</a></p>
  </div>
</section>
''')

# ---------------------------------------------------------------- CONTATO
page('contato.html', 'Contato | Evolua Tecnologia',
     'Fale com a Evolua Tecnologia: demonstrações, suporte, parcerias, integração e homologação do Evolua Ticket.',
     'contato.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Fale conosco</span>
      <h1>Vamos <span class="hl">conversar?</span></h1>
      <p class="lead">Demonstração, suporte, parceria, integração ou homologação: mande uma mensagem e a nossa equipe responde.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <span class="kicker">Canais de atendimento</span>
      <h2>Atendimento direto com quem desenvolve o sistema</h2>
      <div class="contact-list">
        <a class="contact-item" data-contact="whatsapp" hidden><span class="ic">{I['whatsapp']}</span><span><small>WhatsApp</small><b data-contact-text></b></span></a>
        <a class="contact-item" data-contact="email" hidden><span class="ic">{I['mail']}</span><span><small>E-mail</small><b data-contact-text></b></span></a>
        <a class="contact-item" data-contact="instagram" hidden><span class="ic">{I['insta']}</span><span><small>Instagram</small><b data-contact-text></b></span></a>
        <div class="contact-item" data-contact="cidade" hidden><span class="ic">{I['pin']}</span><span><small>Localização</small><b data-contact-text></b></span></div>
        <div class="contact-item" data-contact-empty><span class="ic">{I['support']}</span><span><small>Contatos</small><b>Em breve por aqui</b></span></div>
      </div>
    </div>
    <form class="form-card reveal" data-send="Contato pelo site da Evolua Tecnologia">
      <h3>Envie sua mensagem</h3>
      <p>Preencha os campos e a nossa equipe retorna o contato.</p>
      <div class="field"><label for="c-nome">Nome</label><input id="c-nome" name="nome" data-label="Nome" required autocomplete="name"></div>
      <div class="field-row">
        <div class="field"><label for="c-tel">WhatsApp</label><input id="c-tel" name="whatsapp" data-label="WhatsApp" inputmode="tel" required autocomplete="tel"></div>
        <div class="field"><label for="c-assunto">Assunto</label>
          <select id="c-assunto" name="assunto" data-label="Assunto">
            <option>Conhecer o Evolua Ticket</option>
            <option>Integração e homologação</option>
            <option>Parceria / revenda</option>
            <option>Suporte</option>
            <option>Evolua Parking ou Evolua PDV</option>
            <option>Outro assunto</option>
          </select>
        </div>
      </div>
      <div class="field-row">
        <div class="field"><label for="c-email">E-mail (opcional)</label><input id="c-email" name="email" data-label="E-mail" type="email" autocomplete="email"></div>
        <div class="field"><label for="c-empresa">Empresa (opcional)</label><input id="c-empresa" name="empresa" data-label="Empresa" autocomplete="organization"></div>
      </div>
      <div class="field"><label for="c-msg">Mensagem</label><textarea id="c-msg" name="mensagem" data-label="Mensagem" required></textarea></div>
      <input class="hp" type="text" name="site" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-primary btn-block" type="submit">Enviar mensagem {I['arrow']}</button>
    </form>
  </div>
</section>
''')

# ---------------------------------------------------------------- LEGAL
def legal(file, title, desc, h1, body):
    page(file, f'{title} | Evolua Tecnologia', desc, file, f'''
<section class="hero hero-sm">
  <div class="wrap"><div><span class="eyebrow"><i class="dot"></i> Institucional</span><h1>{h1}</h1><p class="updated" style="margin-top:6px;color:var(--muted)">Última atualização: 22 de outubro de 2026</p></div></div>
</section>
<section class="section"><div class="wrap"><div class="legal">{body}</div></div></section>
''')

legal('privacidade.html', 'Política de Privacidade',
      'Política de Privacidade da Evolua Tecnologia e do Evolua Ticket.', 'Política de <span class="hl">Privacidade</span>', '''
<p>A Evolua Tecnologia é uma marca de <b>JR Eventos e Serviços</b>, inscrita no CNPJ 17.735.913/0001-59, com endereço na Rodovia SC-157, Km 98, Bairro Industrial, Cordilheira Alta - SC.</p>
<p>Esta política explica como a Evolua Tecnologia trata os dados pessoais no site www.evoluatecnologia.com.br, no aplicativo Evolua Ticket e nos painéis do cliente e do vendedor, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
<h2>1. Dados que tratamos</h2>
<ul>
<li><b>Cadastro de clientes e vendedores:</b> nome, e-mail, telefone, CPF ou CNPJ e dados de acesso ao painel.</li>
<li><b>Operação do sistema:</b> eventos, produtos, vendas, caixas, operadores, despesas e relatórios cadastrados pelo cliente.</li>
<li><b>Maquininhas:</b> número de série, modelo, nível de bateria, situação da conexão e versão do aplicativo, usados para ativar a licença e para o monitor das máquinas.</li>
<li><b>Pagamentos:</b> códigos de transação, bandeira e autorização devolvidos pela credenciadora. O Evolua Ticket <b>não lê, não grava e não armazena</b> número de cartão, senha ou dados sensíveis do portador: a captura do cartão é feita exclusivamente pelo aplicativo de pagamento da credenciadora.</li>
<li><b>Contato pelo site:</b> os dados que você digita no formulário, enviados para a nossa equipe pelo WhatsApp ou e-mail.</li>
</ul>
<h2>2. Para que usamos</h2>
<ul>
<li>Prestar o serviço contratado: vendas, impressão, sincronização, relatórios e suporte.</li>
<li>Ativar e controlar as licenças das maquininhas.</li>
<li>Conciliar vendas e estornos com a credenciadora.</li>
<li>Cumprir obrigações legais e fiscais e prevenir fraudes.</li>
<li>Responder contatos e solicitações.</li>
</ul>
<h2>3. Compartilhamento</h2>
<p>Os dados são compartilhados apenas com os parceiros necessários para o serviço funcionar: credenciadoras de pagamento, provedores de hospedagem e de pagamento da licença, sempre no limite do necessário. Não vendemos dados pessoais.</p>
<h2>4. Permissões do aplicativo</h2>
<p>O aplicativo pode pedir acesso ao Bluetooth e à localização aproximada do aparelho. Essas permissões são usadas somente para encontrar e conectar impressoras Bluetooth, como exige o Android, e não para rastrear o usuário.</p>
<h2>5. Armazenamento e segurança</h2>
<p>Os dados ficam em servidores com acesso protegido por senha. Na maquininha, as vendas ficam guardadas até serem enviadas ao servidor. Mantemos os dados pelo tempo necessário para o serviço e para as obrigações legais.</p>
<h2>6. Seus direitos</h2>
<p>Você pode pedir a confirmação, o acesso, a correção, a portabilidade ou a exclusão dos seus dados, além de informações sobre o compartilhamento, pelos canais da página de <a href="contato.html">contato</a>.</p>
<h2>7. Alterações</h2>
<p>Esta política pode ser atualizada. A data da última atualização fica sempre no topo da página.</p>
''')

legal('termos.html', 'Termos de Uso',
      'Termos de Uso do site e dos sistemas da Evolua Tecnologia.', 'Termos de <span class="hl">Uso</span>', '''
<p>A Evolua Tecnologia é uma marca de <b>JR Eventos e Serviços</b>, inscrita no CNPJ 17.735.913/0001-59, com endereço na Rodovia SC-157, Km 98, Bairro Industrial, Cordilheira Alta - SC.</p>
<p>Estes termos valem para o uso do site www.evoluatecnologia.com.br, do aplicativo Evolua Ticket e dos painéis do cliente e do vendedor, desenvolvidos pela Evolua Tecnologia.</p>
<h2>1. O serviço</h2>
<p>O Evolua Ticket é um sistema de venda de fichas para eventos que roda em maquininhas Android. A cobrança no cartão e no PIX é processada pela credenciadora da maquininha, conforme o contrato do cliente com ela. A Evolua não é instituição de pagamento e não recebe nem repassa os valores das vendas.</p>
<h2>2. Licença de uso</h2>
<p>Cada maquininha precisa de uma licença ativa. A licença é pessoal, intransferível e vale pelo período contratado. É proibido copiar, modificar, revender ou fazer engenharia reversa do sistema.</p>
<h2>3. Responsabilidades do cliente</h2>
<ul>
<li>Manter login e senhas em segurança e controlar quem opera as maquininhas.</li>
<li>Cadastrar produtos, preços e informações corretas.</li>
<li>Cumprir as obrigações fiscais e legais do seu evento ou negócio.</li>
<li>Usar o sistema apenas para atividades lícitas.</li>
</ul>
<h2>4. Disponibilidade</h2>
<p>Trabalhamos para manter o serviço disponível. O modo offline permite continuar vendendo sem internet, e as vendas são enviadas ao painel quando a conexão volta. Podem ocorrer pausas para manutenção ou falhas de terceiros, como internet e serviços da credenciadora.</p>
<h2>5. Suporte</h2>
<p>O suporte é feito pelos canais da página de <a href="contato.html">contato</a>.</p>
<h2>6. Privacidade</h2>
<p>O tratamento de dados segue a nossa <a href="privacidade.html">Política de Privacidade</a>.</p>
<h2>7. Alterações</h2>
<p>Estes termos podem ser atualizados. A data da última atualização fica sempre no topo da página.</p>
''')

# ---------------------------------------------------------------- PAGBANK (página de apresentação para homologação)
PB_ROWS = [
    ('Pagamento', 'Débito, crédito à vista e PIX iniciados pelo Evolua Ticket com o PlugPag. O valor vem do carrinho, sem digitação.'),
    ('Mensagens do terminal', 'As mensagens do PlugPag (insira o cartão, aproxime, senha) aparecem na tela do Evolua Ticket durante a cobrança.'),
    ('Cancelamento', 'Cancelamento da operação em andamento pelo operador.'),
    ('Estorno', 'Estorno de cartão e de PIX com os códigos da transação (transactionCode e transactionId), protegido por senha ou cartão de administrador.'),
    ('Comprovantes', 'Impressão das vias do cliente e do estabelecimento pela impressora da maquininha, conforme a configuração do evento.'),
    ('Impressão das fichas', 'As fichas da venda (com código de barras e QR Code) são impressas pela impressora da maquininha através do PlugPag.'),
    ('Leitura NFC', 'Leitura do cartão NFC de administrador para liberar estorno e funções protegidas, sem digitar senha.'),
    ('Serviços suportados', 'PlugPagService (terminais anteriores) e Terminal Service (terminais novos), detectados automaticamente.'),
    ('Modo offline', 'Vendas guardadas na maquininha e sincronizadas com o painel quando a conexão volta, sem duplicidade.'),
]
pb_rows = ''.join(f'<div class="pb-row"><b>{a}</b><span>{b}</span></div>' for a, b in PB_ROWS)

page('pagbank.html',
     'Evolua Ticket + PagBank | Apresentação da integração | Evolua Tecnologia',
     'Apresentação do Evolua Ticket, sistema de venda de fichas para eventos integrado ao PlugPag do PagBank.',
     '', f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow amber"><i class="dot"></i> Integração com o PagBank em andamento</span>
      <h1>Evolua Ticket <span class="hl">+ PagBank</span></h1>
      <p class="lead">Sistema de venda de fichas para eventos que roda nas maquininhas Android do PagBank. A venda, a cobrança no cartão ou no PIX e a impressão das fichas acontecem no mesmo equipamento, integradas pelo PlugPag.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#integracao">Ver a integração {I['arrow']}</a>
        <a class="btn btn-outline" href="#empresa">Dados da empresa</a>
      </div>
      <div class="hero-checks">
        <span>{I['circle_check']} Débito, crédito e PIX</span><span>{I['circle_check']} Estorno integrado</span><span>{I['circle_check']} Impressão na maquininha</span>
      </div>
    </div>
    <div class="pb-device">
      <img src="assets/img/maquininhas/ficha-moderninha-smart-2.webp" alt="Evolua Ticket na Moderninha Smart 2 com a ficha impressa">
    </div>
  </div>
</section>

<section class="section" id="integracao">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Integração PlugPag</span>
      <h2>O que o Evolua Ticket usa do terminal PagBank</h2>
      <p>O aplicativo é instalado na maquininha e conversa com o serviço de pagamento do PagBank. O processamento do cartão e do PIX é feito pelo PagBank; o Evolua Ticket não lê nem armazena dados do cartão.</p>
    </div>
    <div class="pb-table reveal">{pb_rows}</div>
  </div>
</section>

<section class="section section-soft">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Fluxo da venda</span>
      <h2>Do toque no produto à ficha impressa</h2>
    </div>
    <div class="steps pb-steps">
      <div class="step reveal"><h3>Seleção</h3><p>O operador toca nos produtos e o carrinho calcula o total.</p></div>
      <div class="step reveal"><h3>Pagamento</h3><p>Escolhe débito, crédito ou PIX e o Evolua Ticket chama o PlugPag com o valor.</p></div>
      <div class="step reveal"><h3>Aprovação</h3><p>Com o retorno aprovado, a venda é registrada com os códigos da transação.</p></div>
      <div class="step reveal"><h3>Impressão</h3><p>As fichas e, se configurado, o comprovante saem na impressora da maquininha.</p></div>
    </div>
  </div>
</section>

{panel_section(cta=False)}

<section class="section" id="empresa">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <span class="kicker">Empresa</span>
      <h2>Dados para o cadastro</h2>
      <p>A Evolua Tecnologia é a marca de software de JR Eventos e Serviços, que desenvolve e mantém o Evolua Ticket, o painel de gestão e a integração com os terminais.</p>
      <div class="pb-company">
        <div><small>Razão social</small><b>JR Eventos e Serviços</b></div>
        <div><small>CNPJ</small><b>17.735.913/0001-59</b></div>
        <div><small>Nome comercial</small><b>Evolua Tecnologia</b></div>
        <div><small>Produto</small><b>Evolua Ticket (Android)</b></div>
        <div class="full"><small>Endereço</small><b>Rodovia SC-157, Km 98, Bairro Industrial, Cordilheira Alta - SC</b></div>
        <div><small>Site</small><b>www.evoluatecnologia.com.br</b></div>
        <div><small>Instagram</small><b>@evoluaticket</b></div>
      </div>
    </div>
    <div class="reveal">
      <span class="kicker">Contato da integração</span>
      <h2>Fale com a equipe técnica</h2>
      <div class="contact-list">
        <a class="contact-item" data-contact="whatsapp" hidden><span class="ic">{I['whatsapp']}</span><span><small>WhatsApp</small><b data-contact-text></b></span></a>
        <a class="contact-item" data-contact="email" hidden><span class="ic">{I['mail']}</span><span><small>E-mail</small><b data-contact-text></b></span></a>
      </div>
      <p style="margin-top:18px">Documentos do site: <a class="pb-link" href="privacidade.html">Política de Privacidade</a> • <a class="pb-link" href="termos.html">Termos de Uso</a></p>
    </div>
  </div>
</section>
''')

# ---------------------------------------------------------------- 404
page('404.html', 'Página não encontrada | Evolua Tecnologia', 'Página não encontrada.', '', f'''
<section class="notfound">
  <div class="wrap">
    <b>404</b>
    <h1 style="font-size:30px;margin:10px 0">Página não encontrada</h1>
    <p style="color:var(--muted)">O endereço pode ter mudado. Volte para o início ou acesse o seu painel.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary" href="index.html">Voltar ao início</a>
      <a class="btn btn-outline" href="acesso.html">Acessar painel</a>
    </div>
  </div>
</section>
''')

pages = ['', 'evolua-ticket.html', 'evolua-parking.html', 'evolua-pdv.html', 'acesso.html', 'contato.html', 'privacidade.html', 'termos.html']
(OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{DOMAIN}/{p}</loc></url>\n' for p in pages) + '</urlset>\n')
print('ok')
