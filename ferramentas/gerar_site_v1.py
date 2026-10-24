import pathlib

OUT = pathlib.Path('/home/user/giropdv-server/site')
PAINEL = 'https://giropdv-server-production.up.railway.app'
CLIENTE = PAINEL + '/index.php'
VENDEDOR = PAINEL + '/vendedor.php'
COMPRAR = PAINEL + '/comprar.php'
DOMAIN = 'https://www.evoluatecnologia.com.br'

def ic(d, extra=''):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{d}</svg>'

I = {
    'check': ic('<path d="M20 6 9 17l-5-5"/>'),
    'circle_check': ic('<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>'),
    'arrow': ic('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    'user': ic('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>'),
    'briefcase': ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>'),
    'ticket': ic('<path d="M3 8a2 2 0 0 0 2-2h14a2 2 0 0 0 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 0-2 2H5a2 2 0 0 0-2-2v-2a2 2 0 0 0 0-4Z"/><path d="M14 6v12" stroke-dasharray="2 2"/>'),
    'parking': ic('<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/>'),
    'pdv': ic('<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/><path d="M6 9h5M6 12h3"/>'),
    'wifi_off': ic('<path d="M2 2l20 20M8.5 16.5a5 5 0 0 1 7 0M5 13a10 10 0 0 1 5.2-2.8M19 13a10 10 0 0 0-2.1-1.6M2 8.8a15 15 0 0 1 4.2-2.7M22 8.8A15 15 0 0 0 11 5"/><circle cx="12" cy="20" r="1"/>'),
    'chart': ic('<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>'),
    'pix': ic('<path d="m12 2 4 4-4 4-4-4Z"/><path d="m12 14 4 4-4 4-4-4Z"/><path d="m2 12 4-4 4 4-4 4Z"/><path d="m14 12 4-4 4 4-4 4Z"/>'),
    'support': ic('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/><path d="M8 9h8M8 13h5"/>'),
    'printer': ic('<path d="M6 9V2h12v7"/><rect x="2" y="9" width="20" height="8" rx="2"/><path d="M6 14h12v8H6z"/>'),
    'cash': ic('<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>'),
    'undo': ic('<path d="M9 14 4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/>'),
    'box': ic('<path d="M21 8 12 3 3 8v8l9 5 9-5Z"/><path d="m3 8 9 5 9-5M12 13v8"/>'),
    'team': ic('<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-6 7-6s7 2.5 7 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M22 20c0-3-2-5-5-5.7"/>'),
    'monitor': ic('<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M9 6h6M12 18h.01"/><path d="M16 10v4"/>'),
    'calendar': ic('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
    'shield': ic('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>'),
    'zap': ic('<path d="M13 2 3 14h9l-1 8 10-12h-9Z"/>'),
    'car': ic('<path d="M5 17h14v-5l-2-5H7l-2 5Z"/><circle cx="7.5" cy="17.5" r="1.5"/><circle cx="16.5" cy="17.5" r="1.5"/><path d="M5 12h14"/>'),
    'clock': ic('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'),
    'card': ic('<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>'),
    'repeat': ic('<path d="m17 1 4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>'),
    'barcode': ic('<path d="M3 5v14M7 5v14M11 5v14M14 5v14M18 5v14M21 5v14"/>'),
    'layers': ic('<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>'),
    'cloud': ic('<path d="M17.5 19a4.5 4.5 0 0 0 0-9h-1.3A7 7 0 1 0 4 15.3"/><path d="M8 19h9.5"/>'),
    'mail': ic('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>'),
    'insta': ic('<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>'),
    'pin': ic('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>'),
    'menu': ic('<path d="M3 6h18M3 12h18M3 18h18"/>'),
    'windows': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 5.5 10.5 4.5v7H3zM11.5 4.3 21 3v8.5h-9.5zM3 12.5h7.5v7L3 18.5zM11.5 12.5H21V21l-9.5-1.3z"/></svg>',
    'android': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.6 9.48l1.84-3.18a.38.38 0 0 0-.66-.38l-1.86 3.22a11.4 11.4 0 0 0-9.84 0L5.22 5.92a.38.38 0 0 0-.66.38L6.4 9.48A10.8 10.8 0 0 0 1 18h22a10.8 10.8 0 0 0-5.4-8.52ZM7 15.25a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5Zm10 0a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5Z"/></svg>',
    'whatsapp': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35ZM12.04 21.5h-.01a9.43 9.43 0 0 1-4.8-1.32l-.35-.2-3.57.94.95-3.48-.22-.36A9.42 9.42 0 0 1 2.6 12.05C2.6 6.84 6.84 2.6 12.05 2.6c2.52 0 4.9.99 6.68 2.77a9.37 9.37 0 0 1 2.76 6.68c0 5.21-4.24 9.45-9.45 9.45Zm8.04-17.5A11.3 11.3 0 0 0 12.04.7C5.78.7.68 5.8.68 12.05c0 2 .52 3.95 1.52 5.67L.58 23.3l5.72-1.5a11.3 11.3 0 0 0 5.74 1.46h.01c6.26 0 11.36-5.1 11.36-11.35 0-3.04-1.18-5.89-3.33-8.03Z"/></svg>',
}

NAV = [
    ('index.html', 'Início'),
    ('evolua-ticket.html', 'Evolua Ticket'),
    ('evolua-parking.html', 'Evolua Parking'),
    ('evolua-pdv.html', 'Evolua PDV'),
    ('contato.html', 'Contato'),
]

def brand(sub='TECNOLOGIA', href='index.html'):
    return (f'<a class="brand" href="{href}" aria-label="Evolua Tecnologia - início">'
            f'<img src="assets/img/evolua-mark.svg" alt="" width="40" height="40">'
            f'<span class="brand-name">EVOLU<i>A</i><span class="brand-sub">{sub}</span></span></a>')

def header(active):
    links = ''.join(
        f'<a href="{h}"{" class=\"active\" aria-current=\"page\"" if h == active else ""}>{t}</a>'
        for h, t in NAV)
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
        <p class="about">Sistemas para quem vende: eventos, estacionamentos e comércio. Rápidos, simples e prontos para funcionar até sem internet.</p>
      </div>
      <div>
        <h4>Sistemas</h4>
        <ul>
          <li><a href="evolua-ticket.html">Evolua Ticket</a></li>
          <li><a href="evolua-parking.html">Evolua Parking</a></li>
          <li><a href="evolua-pdv.html">Evolua PDV</a></li>
        </ul>
      </div>
      <div>
        <h4>Acesso</h4>
        <ul>
          <li><a href="{CLIENTE}">Painel do Cliente</a></li>
          <li><a href="{VENDEDOR}">Painel do Vendedor</a></li>
          <li><a href="{COMPRAR}">Comprar licença</a></li>
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
      <span class="dev"><i class="status-dot"></i> Desenvolvido por <img src="assets/img/evolua-mark.svg" alt="" width="20" height="20"><b>Evolua Tecnologia</b></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="contato.html" aria-label="Falar no WhatsApp" hidden>{I['whatsapp']}</a>
<script src="assets/js/main.js"></script>'''

def page(file, title, desc, active, body):
    url = DOMAIN + ('/' if file == 'index.html' else '/' + file)
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#050a16">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Evolua Tecnologia">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/evolua-icon.svg">
<link rel="icon" type="image/svg+xml" href="assets/img/evolua-icon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700;800;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
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

def li(items):
    return ''.join(f'<li>{I["check"]}<span>{t}</span></li>' for t in items)

def features(items, cols=''):
    return f'<div class="features {cols}">' + ''.join(
        f'<div class="feature reveal"><div class="f-ic">{I[k]}</div><h3>{t}</h3><p>{d}</p></div>'
        for k, t, d in items) + '</div>'

def cta(title, text, actions):
    return f'''<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="actions">{actions}</div>
    </div>
  </div>
</section>'''

ACCESS_STRIP = f'''<section class="access">
  <div class="wrap">
    <div class="access-grid">
      <a class="access-card" href="{CLIENTE}">
        <span class="ic">{I['user']}</span>
        <span><h3>Painel do Cliente</h3><p>Eventos, vendas, caixa e relatórios em tempo real.</p></span>
        <span class="go">{I['arrow']}</span>
      </a>
      <a class="access-card" href="{VENDEDOR}">
        <span class="ic alt">{I['briefcase']}</span>
        <span><h3>Painel do Vendedor</h3><p>Seus clientes, licenças e comissões em um só lugar.</p></span>
        <span class="go">{I['arrow']}</span>
      </a>
    </div>
  </div>
</section>'''

# ------------------------------------------------------------------ INÍCIO
page('index.html',
     'Evolua Tecnologia | Sistemas para eventos, estacionamentos e comércio',
     'A Evolua Tecnologia cria sistemas de venda rápidos e simples: Evolua Ticket para eventos, Evolua Parking para estacionamentos e Evolua PDV para o comércio.',
     'index.html', f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Evolua Tecnologia</span>
      <h1>Tecnologia que faz o seu negócio <span class="grad">evoluir.</span></h1>
      <p class="lead">Sistemas de venda para eventos, estacionamentos e comércio. Rápidos no caixa, simples de usar e prontos para funcionar até sem internet.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#sistemas">Conheça os sistemas {I['arrow']}</a>
        <a class="btn btn-ghost" href="acesso.html">{I['user']} Acessar painel</a>
      </div>
      <div class="hero-meta">
        <span>{I['wifi_off']} Vende sem internet</span>
        <span>{I['chart']} Relatórios em tempo real</span>
        <span>{I['pix']} Licença via PIX</span>
      </div>
    </div>
    <div class="device-scene" aria-hidden="true">
      <div class="device-glow"></div>
      <div class="device">
        <div class="device-screen">
          <div class="ds-top"><b>EVOLUA TICKET</b><span>● Online</span></div>
          <div class="ds-grid">
            <div class="ds-item">Cerveja<small>R$ 12,00</small></div>
            <div class="ds-item">Refrigerante<small>R$ 7,00</small></div>
            <div class="ds-item">Água<small>R$ 5,00</small></div>
            <div class="ds-item">Espetinho<small>R$ 15,00</small></div>
          </div>
          <div class="ds-total"><span>Total</span><span>R$ 39,00</span></div>
        </div>
        <div class="device-keys"><i></i><i></i><i></i><i></i><i></i><i></i></div>
      </div>
      <div class="ticket">
        <div class="t-brand">EVOLU<i>A</i> TICKET</div>
        <div class="t-item">1x CERVEJA</div>
        <div class="t-sub">Festa da Cidade • Caixa 03</div>
        <div class="t-cut"></div>
        <div class="t-code">{'<span></span>' * 22}</div>
      </div>
      <div class="chip"><span class="ic">{I['circle_check']}</span><span>Venda sincronizada<small>agora mesmo</small></span></div>
    </div>
  </div>
</section>

{ACCESS_STRIP}

<section class="section" id="sistemas">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Nossos sistemas</span>
      <h2>Um sistema para cada tipo de venda</h2>
      <p>Começamos pelos eventos e estamos levando a mesma rapidez e simplicidade para estacionamentos e para o comércio.</p>
    </div>
    <div class="products">
      <article class="product reveal">
        <span class="badge badge-live"><i class="pulse"></i>Disponível</span>
        <div class="p-icon">{I['ticket']}</div>
        <h3>Evolua <i>Ticket</i></h3>
        <div class="p-tag">Vendas em eventos</div>
        <p class="desc">Venda de fichas na maquininha, com impressão na hora, controle de caixa e relatórios completos do evento.</p>
        <ul>{li(['Funciona sem internet', 'Fichas impressas na hora', 'Caixa, estorno e relatórios'])}</ul>
        <a class="btn btn-primary btn-block" href="evolua-ticket.html">Conhecer o Evolua Ticket</a>
      </article>
      <article class="product reveal" style="--accent:linear-gradient(90deg,#f59e0b,#fbbf24);--icon-bg:linear-gradient(135deg,#f59e0b,#d97706)">
        <span class="badge badge-dev"><i class="pulse"></i>Em desenvolvimento</span>
        <div class="p-icon" style="box-shadow:0 12px 26px rgba(217,119,6,.25)">{I['parking']}</div>
        <h3>Evolua <i>Parking</i></h3>
        <div class="p-tag">Estacionamentos</div>
        <p class="desc">Controle de entrada e saída de veículos, cobrança por tempo e ticket impresso, com a mesma simplicidade do Ticket.</p>
        <ul>{li(['Entrada e saída por placa', 'Tabela de preços por tempo', 'Mensalistas e relatórios'])}</ul>
        <a class="btn btn-light btn-block" href="evolua-parking.html">Ver o que vem por aí</a>
      </article>
      <article class="product reveal" style="--accent:linear-gradient(90deg,#22d3ee,#0891b2);--icon-bg:linear-gradient(135deg,#22d3ee,#0891b2)">
        <span class="badge badge-soon"><i class="pulse"></i>Em breve</span>
        <div class="p-icon" style="box-shadow:0 12px 26px rgba(8,145,178,.25)">{I['pdv']}</div>
        <h3>Evolua <i>PDV</i></h3>
        <div class="p-tag">Comércio • Windows e Android</div>
        <p class="desc">Ponto de venda completo para o computador do seu comércio, com versão para Android quando precisar.</p>
        <ul>{li(['Feito para Windows', 'Também roda no Android', 'Caixa, estoque e relatórios'])}</ul>
        <a class="btn btn-light btn-block" href="evolua-pdv.html">Saiba mais</a>
      </article>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Por que a Evolua</span>
      <h2>Feito para quem não pode parar de vender</h2>
      <p>Fila andando, caixa batendo e você acompanhando tudo de qualquer lugar.</p>
    </div>
    {features([
        ('wifi_off', 'Vende sem internet', 'As vendas ficam guardadas na máquina e sobem sozinhas quando a conexão voltar.'),
        ('zap', 'Rápido no caixa', 'Telas pensadas para vender em poucos toques, mesmo com fila grande.'),
        ('chart', 'Tudo em tempo real', 'Acompanhe vendas, caixas e máquinas pelo painel, do celular ou do computador.'),
        ('support', 'Suporte de verdade', 'Atendimento direto com quem desenvolve o sistema, sem robô e sem enrolação.'),
    ])}
    <div class="stats">
      <div class="stat reveal"><b>100%</b><span>na nuvem e na máquina</span></div>
      <div class="stat reveal"><b>24h</b><span>painel disponível</span></div>
      <div class="stat reveal"><b>3</b><span>sistemas na família Evolua</span></div>
      <div class="stat reveal"><b>PIX</b><span>licença liberada na hora</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Como começar</span>
      <h2>Do cadastro à primeira venda em minutos</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Escolha seu plano</h3><p>Compre a licença direto pelo site, com pagamento via PIX e liberação automática.</p></div>
      <div class="step reveal"><h3>Cadastre seus produtos</h3><p>No painel do cliente, monte o evento, os grupos, os produtos e os operadores.</p></div>
      <div class="step reveal"><h3>Comece a vender</h3><p>Ative a maquininha com o seu código e acompanhe cada venda pelo painel.</p></div>
    </div>
  </div>
</section>

{cta('Pronto para evoluir as suas vendas?', 'Compre sua licença agora ou fale com a gente para tirar dúvidas e conhecer o sistema.',
     f'<a class="btn btn-light" href="{COMPRAR}">Comprar licença</a><a class="btn btn-ghost" href="contato.html">Falar com a Evolua</a>')}
''')

# ------------------------------------------------------------------ TICKET
page('evolua-ticket.html',
     'Evolua Ticket | Sistema de fichas para eventos | Evolua Tecnologia',
     'Evolua Ticket: venda de fichas na maquininha para eventos, com impressão na hora, funcionamento sem internet, controle de caixa, estorno e relatórios em tempo real.',
     'evolua-ticket.html', f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Disponível agora</span>
      <h1>Evolua <span class="grad">Ticket</span></h1>
      <p class="lead">O sistema de fichas para eventos que não trava a sua fila. Venda na maquininha, imprima a ficha na hora e acompanhe tudo pelo painel, até sem internet.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{COMPRAR}">Comprar licença {I['arrow']}</a>
        <a class="btn btn-ghost" href="{CLIENTE}">{I['user']} Painel do Cliente</a>
      </div>
      <div class="hero-meta">
        <span>{I['wifi_off']} Modo offline</span>
        <span>{I['printer']} Impressão na hora</span>
        <span>{I['monitor']} Maquininhas Android</span>
      </div>
    </div>
    <div class="device-scene" aria-hidden="true">
      <div class="device-glow"></div>
      <div class="device">
        <div class="device-screen">
          <div class="ds-top"><b>CAIXA 03</b><span>● Offline</span></div>
          <div class="ds-grid">
            <div class="ds-item">Chopp<small>R$ 14,00</small></div>
            <div class="ds-item">Pastel<small>R$ 10,00</small></div>
            <div class="ds-item">Suco<small>R$ 8,00</small></div>
            <div class="ds-item">Combo<small>R$ 30,00</small></div>
          </div>
          <div class="ds-total"><span>3 itens</span><span>R$ 32,00</span></div>
        </div>
        <div class="device-keys"><i></i><i></i><i></i><i></i><i></i><i></i></div>
      </div>
      <div class="ticket">
        <div class="t-brand">EVOLU<i>A</i> TICKET</div>
        <div class="t-item">1x CHOPP</div>
        <div class="t-sub">Válido somente hoje</div>
        <div class="t-cut"></div>
        <div class="t-code">{'<span></span>' * 22}</div>
      </div>
      <div class="chip"><span class="ic">{I['cloud']}</span><span>12 vendas na fila<small>sobem quando a internet voltar</small></span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Como funciona</span>
      <h2>Simples para o operador, completo para o dono</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Monte o evento</h3><p>Cadastre grupos, produtos, preços e operadores pelo painel do cliente.</p></div>
      <div class="step reveal"><h3>Venda na maquininha</h3><p>O operador abre o caixa, toca nos produtos e a ficha sai impressa na hora.</p></div>
      <div class="step reveal"><h3>Acompanhe e feche</h3><p>Veja as vendas em tempo real, feche os caixas e confira o lucro do evento.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">Recursos</span>
      <h2>Tudo o que o seu evento precisa</h2>
      <p>Do primeiro produto cadastrado ao relatório final do evento.</p>
    </div>
    {features([
        ('wifi_off', 'Funciona sem internet', 'A máquina continua vendendo e sincroniza as vendas automaticamente depois, sem duplicar nada.'),
        ('printer', 'Fichas impressas', 'Impressão da ficha na própria maquininha e envio de pedidos para a impressora da cozinha.'),
        ('cash', 'Controle de caixa', 'Abertura e fechamento de caixa por operador, com conferência de valores.'),
        ('undo', 'Estorno seguro', 'Cancelamento de vendas com senha de administrador e registro de tudo.'),
        ('box', 'Grupos e produtos', 'Organize o cardápio por grupos e mude preços em segundos pelo painel.'),
        ('team', 'Funcionários e despesas', 'Cadastre a equipe e as despesas do evento e veja o lucro de verdade.'),
        ('chart', 'Relatórios completos', 'Totais de vendas, vendas por operador, quantidade vendida e caixa, com exportação em PDF.'),
        ('monitor', 'Monitor das máquinas', 'Veja bateria, conexão e situação de cada maquininha em tempo real.'),
        ('pix', 'Licença via PIX', 'Compre ou renove a licença pelo site e ela é liberada assim que o pagamento cai.'),
    ], 'cols-3')}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Painel do cliente</span>
      <h2>O evento inteiro na palma da mão</h2>
      <p>Acompanhe de qualquer lugar quanto já foi vendido, quais produtos saem mais e como está cada caixa.</p>
      <ul class="checklist">
        <li>{I['circle_check']}<span>Gráficos de produtos, grupos e eventos</span></li>
        <li>{I['circle_check']}<span>Vários eventos na mesma conta</span></li>
        <li>{I['circle_check']}<span>Acesso pelo celular ou computador</span></li>
        <li>{I['circle_check']}<span>Modo escuro para a noite do evento</span></li>
      </ul>
      <div class="hero-actions"><a class="btn btn-primary" href="{CLIENTE}">Entrar no painel {I['arrow']}</a></div>
    </div>
    <div class="panel-card reveal" aria-hidden="true">
      <div class="pc-head"><b>Festa da Cidade</b><span>Ao vivo</span></div>
      <div class="pc-kpis">
        <div class="pc-kpi"><small>Vendido hoje</small><b>R$ 18.420</b></div>
        <div class="pc-kpi"><small>Fichas</small><b>1.536</b></div>
        <div class="pc-kpi"><small>Caixas abertos</small><b>8</b></div>
        <div class="pc-kpi"><small>Ticket médio</small><b>R$ 12,00</b></div>
      </div>
      <div class="pc-bars"><i style="height:35%"></i><i style="height:52%"></i><i style="height:44%"></i><i style="height:70%"></i><i style="height:62%"></i><i style="height:88%"></i><i style="height:100%"></i><i style="height:76%"></i></div>
    </div>
  </div>
</section>

{cta('Leve o Evolua Ticket para o seu próximo evento', 'Licença liberada na hora via PIX. Se preferir, fale com a gente e tire suas dúvidas antes.',
     f'<a class="btn btn-light" href="{COMPRAR}">Comprar licença</a><a class="btn btn-ghost" href="contato.html">Falar com a Evolua</a>')}
''')

# ------------------------------------------------------------------ PARKING
def interest_form(produto):
    return f'''<form class="form-card reveal" data-send="Quero saber mais sobre o {produto}">
      <h3>Quero ser avisado</h3>
      <p>Deixe seu contato e avisamos assim que o {produto} estiver disponível.</p>
      <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" data-label="Nome" required autocomplete="name"></div>
      <div class="field-row">
        <div class="field"><label for="f-tel">WhatsApp</label><input id="f-tel" name="whatsapp" data-label="WhatsApp" inputmode="tel" required autocomplete="tel"></div>
        <div class="field"><label for="f-cidade">Cidade</label><input id="f-cidade" name="cidade" data-label="Cidade" autocomplete="address-level2"></div>
      </div>
      <div class="field"><label for="f-neg">Seu negócio</label><input id="f-neg" name="negocio" data-label="Negócio"></div>
      <button class="btn btn-primary btn-block" type="submit">Quero ser avisado</button>
      <p class="form-note">Ao enviar, abrimos uma conversa com a Evolua.</p>
    </form>'''

page('evolua-parking.html',
     'Evolua Parking | Sistema para estacionamentos | Evolua Tecnologia',
     'Evolua Parking: sistema para estacionamentos com entrada e saída por placa, cobrança por tempo, ticket impresso e mensalistas. Em desenvolvimento pela Evolua Tecnologia.',
     'evolua-parking.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow" style="color:#fbbf24;background:rgba(245,158,11,.12);border-color:rgba(245,158,11,.3)"><i class="dot" style="background:#fbbf24;box-shadow:0 0 10px #fbbf24"></i> Em desenvolvimento</span>
      <h1>Evolua <span class="grad">Parking</span></h1>
      <p class="lead">O sistema para estacionamentos da Evolua. Entrada e saída rápidas, cobrança certa por tempo e o controle do pátio na palma da mão.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#avise-me">Quero ser avisado {I['arrow']}</a>
        <a class="btn btn-ghost" href="contato.html">Falar com a Evolua</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">O que está sendo planejado</span>
      <h2>Tudo para o seu estacionamento</h2>
      <p>Os recursos abaixo fazem parte do projeto e podem mudar até o lançamento.</p>
    </div>
    {features([
        ('car', 'Entrada e saída por placa', 'Registro rápido do veículo na entrada e cálculo automático na saída.'),
        ('clock', 'Cobrança por tempo', 'Tabelas por fração, hora, diária e período, do seu jeito.'),
        ('printer', 'Ticket impresso', 'Comprovante de entrada e de pagamento impressos na hora.'),
        ('repeat', 'Mensalistas', 'Cadastro de mensalistas com controle de vencimento.'),
        ('wifi_off', 'Funciona sem internet', 'A mesma base offline do Evolua Ticket: o pátio nunca para.'),
        ('chart', 'Relatórios', 'Movimento por dia, ocupação, caixa e faturamento pelo painel.'),
    ], 'cols-3')}
  </div>
</section>

<section class="section section-alt" id="avise-me">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Andamento</span>
      <h2>Construído sobre o que já funciona</h2>
      <p>O Evolua Parking aproveita a base já testada em eventos do Evolua Ticket: painel na nuvem, maquininhas Android, licença via PIX e vendas offline.</p>
      <div class="roadmap" style="grid-template-columns:1fr;margin-top:24px">
        <div class="rm done"><small>Pronto</small><h4>Base da plataforma</h4><p>Painel, licenças, PIX e sincronização offline do Evolua Ticket.</p></div>
        <div class="rm"><small>Próximo passo</small><h4>Desenvolvimento do Parking</h4><p>Telas de entrada e saída, tabelas de preço e mensalistas.</p></div>
        <div class="rm"><small>Depois</small><h4>Lançamento</h4><p>Liberação para os primeiros estacionamentos parceiros.</p></div>
      </div>
    </div>
    {interest_form('Evolua Parking')}
  </div>
</section>
''')

# ------------------------------------------------------------------ PDV
page('evolua-pdv.html',
     'Evolua PDV | Ponto de venda para Windows e Android | Evolua Tecnologia',
     'Evolua PDV: ponto de venda para o comércio, feito para computador Windows e com versão para Android. Caixa, estoque e relatórios. Em breve pela Evolua Tecnologia.',
     'evolua-pdv.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Em breve</span>
      <h1>Evolua <span class="grad">PDV</span></h1>
      <p class="lead">O ponto de venda da Evolua para o comércio. Feito principalmente para o computador do seu caixa, com versão para Android quando você precisar vender em qualquer lugar.</p>
      <div class="platforms">
        <span class="platform">{I['windows']} Windows <small>principal</small></span>
        <span class="platform">{I['android']} Android <small>também</small></span>
      </div>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#avise-me">Quero ser avisado {I['arrow']}</a>
        <a class="btn btn-ghost" href="contato.html">Falar com a Evolua</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">O que está sendo planejado</span>
      <h2>Um caixa completo para o seu comércio</h2>
      <p>Os recursos abaixo fazem parte do projeto e podem mudar até o lançamento.</p>
    </div>
    {features([
        ('zap', 'Venda rápida no balcão', 'Busca por código ou nome, atalhos de teclado e leitor de código de barras.'),
        ('box', 'Estoque', 'Entradas, saídas e aviso de estoque baixo.'),
        ('cash', 'Caixa', 'Abertura, sangria, suprimento e fechamento por operador.'),
        ('card', 'Várias formas de pagamento', 'Dinheiro, cartão e PIX na mesma venda.'),
        ('layers', 'Windows e Android', 'O mesmo sistema no computador do caixa e no celular ou maquininha.'),
        ('chart', 'Relatórios na nuvem', 'Acompanhe vendas e produtos pelo painel, de onde estiver.'),
    ], 'cols-3')}
  </div>
</section>

<section class="section section-alt" id="avise-me">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Para quem é</span>
      <h2>Feito para o dia a dia do comércio</h2>
      <p>Mercadinhos, lanchonetes, lojas, conveniências e qualquer negócio que precisa de um caixa rápido e confiável.</p>
      <ul class="checklist">
        <li>{I['circle_check']}<span>Funciona no computador que você já tem</span></li>
        <li>{I['circle_check']}<span>Continua vendendo se a internet cair</span></li>
        <li>{I['circle_check']}<span>Mesmo suporte e mesmo painel da família Evolua</span></li>
      </ul>
    </div>
    {interest_form('Evolua PDV')}
  </div>
</section>
''')

# ------------------------------------------------------------------ ACESSO
page('acesso.html',
     'Acessar painel | Evolua Tecnologia',
     'Acesse o Painel do Cliente ou o Painel do Vendedor da Evolua Tecnologia.',
     'acesso.html', f'''
<section class="hero hero-sm">
  <div class="wrap" style="text-align:center">
    <div>
      <span class="eyebrow"><i class="dot"></i> Área restrita</span>
      <h1>Acessar <span class="grad">painel</span></h1>
      <p class="lead" style="margin:0 auto">Escolha o seu tipo de acesso para entrar.</p>
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
          <li>{I['check']}<span>Relatórios e compra de licenças</span></li>
        </ul>
        <a class="btn btn-primary btn-block" href="{CLIENTE}">Entrar como cliente {I['arrow']}</a>
      </div>
      <div class="card reveal">
        <div class="ic alt">{I['briefcase']}</div>
        <h2>Painel do Vendedor</h2>
        <p>Para os vendedores e revendedores parceiros da Evolua.</p>
        <ul>
          <li>{I['check']}<span>Cadastro e acompanhamento de clientes</span></li>
          <li>{I['check']}<span>Licenças dos seus clientes</span></li>
          <li>{I['check']}<span>Comissões e repasses</span></li>
        </ul>
        <a class="btn btn-primary btn-block" href="{VENDEDOR}" style="background:linear-gradient(135deg,#22d3ee,#0891b2);box-shadow:0 12px 28px rgba(8,145,178,.3)">Entrar como vendedor {I['arrow']}</a>
      </div>
    </div>
    <p class="help-line reveal">Ainda não é cliente? <a href="{COMPRAR}">Compre sua licença</a> • Esqueceu a senha? <a href="contato.html">Fale com o suporte</a></p>
  </div>
</section>
''')

# ------------------------------------------------------------------ CONTATO
page('contato.html',
     'Contato | Evolua Tecnologia',
     'Fale com a Evolua Tecnologia: dúvidas, suporte, orçamentos e parcerias para o Evolua Ticket, Evolua Parking e Evolua PDV.',
     'contato.html', f'''
<section class="hero hero-sm">
  <div class="wrap">
    <div>
      <span class="eyebrow"><i class="dot"></i> Fale conosco</span>
      <h1>Vamos <span class="grad">conversar?</span></h1>
      <p class="lead">Dúvidas, suporte, orçamento ou quer ser um vendedor parceiro? Mande uma mensagem e respondemos o mais rápido possível.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <span class="kicker">Canais de atendimento</span>
      <h2>Atendimento direto com quem faz o sistema</h2>
      <div class="contact-list" style="margin-top:26px">
        <a class="contact-item" data-contact="whatsapp" hidden><span class="ic">{I['whatsapp']}</span><span><small>WhatsApp</small><b data-contact-text></b></span></a>
        <a class="contact-item" data-contact="email" hidden><span class="ic">{I['mail']}</span><span><small>E-mail</small><b data-contact-text></b></span></a>
        <a class="contact-item" data-contact="instagram" hidden><span class="ic">{I['insta']}</span><span><small>Instagram</small><b data-contact-text></b></span></a>
        <div class="contact-item" data-contact="cidade" hidden><span class="ic">{I['pin']}</span><span><small>Localização</small><b data-contact-text></b></span></div>
        <div class="contact-item" data-contact-empty><span class="ic">{I['support']}</span><span><small>Contatos</small><b>Em breve por aqui</b></span></div>
      </div>
    </div>
    <form class="form-card reveal" data-send="Contato pelo site da Evolua Tecnologia">
      <h3>Envie sua mensagem</h3>
      <p>Preencha os campos e abrimos a conversa com a Evolua.</p>
      <div class="field"><label for="c-nome">Nome</label><input id="c-nome" name="nome" data-label="Nome" required autocomplete="name"></div>
      <div class="field-row">
        <div class="field"><label for="c-tel">WhatsApp</label><input id="c-tel" name="whatsapp" data-label="WhatsApp" inputmode="tel" required autocomplete="tel"></div>
        <div class="field"><label for="c-assunto">Assunto</label>
          <select id="c-assunto" name="assunto" data-label="Assunto">
            <option>Quero conhecer o Evolua Ticket</option>
            <option>Evolua Parking</option>
            <option>Evolua PDV</option>
            <option>Suporte</option>
            <option>Quero ser vendedor parceiro</option>
            <option>Outro assunto</option>
          </select>
        </div>
      </div>
      <div class="field"><label for="c-msg">Mensagem</label><textarea id="c-msg" name="mensagem" data-label="Mensagem" required></textarea></div>
      <button class="btn btn-primary btn-block" type="submit">Enviar mensagem {I['arrow']}</button>
    </form>
  </div>
</section>
''')

# ------------------------------------------------------------------ 404
page('404.html',
     'Página não encontrada | Evolua Tecnologia',
     'Página não encontrada.',
     '', f'''
<section class="hero notfound">
  <div class="wrap" style="display:block;text-align:center">
    <b>404</b>
    <h1 style="font-size:32px">Página não encontrada</h1>
    <p class="lead" style="margin:0 auto">O endereço pode ter mudado. Volte para o início ou acesse o seu painel.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary" href="index.html">Voltar ao início</a>
      <a class="btn btn-ghost" href="acesso.html">Acessar painel</a>
    </div>
  </div>
</section>
''')

(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
pages = ['', 'evolua-ticket.html', 'evolua-parking.html', 'evolua-pdv.html', 'acesso.html', 'contato.html']
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{DOMAIN}/{p}</loc></url>\n' for p in pages) + '</urlset>\n')
print('ok')
