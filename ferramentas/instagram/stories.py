import pathlib

P = pathlib.Path(__file__).parent
SRC = (P / 'make.py').read_text(encoding='utf-8')
exec(SRC[:SRC.index('posts = []')])  # CSS e componentes dos posts (celular, telas do app, ficha, prints)

STORY_CSS = CSS.replace('html,body{width:1080px;height:1350px;overflow:hidden}', 'html,body{width:1080px;height:1920px;overflow:hidden}') + r'''
.top{top:150px}
.logo b{font-size:38px}.logo small{font-size:14px}
.prog{position:absolute;left:70px;right:70px;top:90px;display:flex;gap:10px}
.prog i{flex:1;height:7px;border-radius:4px;background:rgba(255,255,255,.22)}
.prog i.on{background:#fff}
.head{top:300px}
.head .kick{display:inline-block;font-size:26px;font-weight:900;letter-spacing:4px;color:#67e8f9;text-transform:uppercase;margin-bottom:22px}
h1{font-size:92px;line-height:1.02;letter-spacing:-2px}
.sub{font-size:38px;line-height:1.4;margin-top:28px}
.vis{top:820px;bottom:250px}
.phone{width:450px;height:900px;border-radius:70px;padding:14px}
.phone .glass{border-radius:57px;padding:10px}
.phone .scr{border-radius:48px}
.phone .island{top:26px;width:130px;height:36px}
.app{font-size:17px}
.app-top{padding-top:76px}
.dev{max-height:950px}
.bullets{top:830px;bottom:300px}
.bullets div{font-size:40px;padding:40px 40px}
.bullets i{width:84px;height:84px;font-size:40px}
.cta-box{top:880px}
.cta-box div{font-size:42px;padding:34px 38px}
.cta-box i{width:84px;height:84px;font-size:42px}
.cta-box small{font-size:26px}
.foot{bottom:110px;font-size:28px}
.big{position:absolute;left:70px;right:70px;top:820px;bottom:300px;display:flex;flex-direction:column;justify-content:center;gap:26px}
.big .stat{padding:44px;border-radius:30px;background:linear-gradient(180deg,#122656,#0e1f48);border:1px solid rgba(148,178,255,.2)}
.big .stat b{display:block;font-size:76px;font-weight:900;color:#5aa2ff;line-height:1}
.big .stat span{display:block;font-size:34px;color:#c9d6f2;margin-top:12px;font-weight:600}
.chips{position:absolute;left:70px;right:70px;top:840px;display:flex;flex-wrap:wrap;gap:20px}
.chips span{padding:26px 34px;border-radius:24px;background:linear-gradient(180deg,#122656,#0e1f48);border:1px solid rgba(148,178,255,.2);font-size:38px;font-weight:800}
.food{grid-template-columns:repeat(3,290px);gap:22px}
.food img{height:240px}
.food p{font-size:24px}.food p small{font-size:20px}
.mark{display:flex;flex-direction:column;align-items:center;gap:30px}
.mark img{width:360px;height:360px;filter:drop-shadow(0 0 60px rgba(43,140,255,.55))}
.mark b{font-family:'Exo 2',Inter,sans-serif;font-size:120px;font-weight:900;letter-spacing:4px;line-height:1}
.mark b i{font-style:normal;color:#2b8cff}
.mark small{font-size:34px;font-weight:800;letter-spacing:16px;color:#67e8f9}
.products3{position:absolute;left:70px;right:70px;top:830px;display:grid;gap:24px}
.products3 div{display:flex;gap:28px;align-items:center;padding:34px 38px;border-radius:28px;background:linear-gradient(180deg,#122656,#0e1f48);border:1px solid rgba(148,178,255,.2)}
.products3 i{flex:0 0 auto;width:96px;height:96px;border-radius:26px;display:grid;place-items:center;font-style:normal;font-size:48px}
.products3 b{display:block;font-size:42px;font-weight:900}
.products3 span{display:block;font-size:28px;color:#a3b3d4;margin-top:6px}
.products3 em{font-style:normal;font-size:22px;font-weight:800;padding:6px 14px;border-radius:999px;margin-left:12px;vertical-align:6px}
'''

GROUPS = [
    ('quem-somos', 'Quem somos'), ('evolua-ticket', 'Evolua Ticket'), ('como-funciona', 'Como funciona'),
    ('pagamentos', 'Pagamentos'), ('fichas', 'Fichas'), ('painel', 'Painel'), ('para-quem', 'Para quem'), ('contato', 'Contato'),
]

stories = {g: [] for g, _ in GROUPS}
def story(group, kick, title, sub, vis):
    stories[group].append(dict(kick=kick, title=title, sub=sub, vis=vis))

def bul(items):
    return '<div class="bullets">' + ''.join(f'<div><i>{e}</i><span>{t}</span></div>' for e, t in items) + '</div>'

DEVS3 = ''.join(f'<img class="dev" style="max-height:900px;width:31%;object-fit:contain" src="img/ficha-{n}.webp">' for n in ['moderninha-smart-2', 'stone', 'cielo'])

# ---------------------------------------------------------------- 1. QUEM SOMOS
story('quem-somos', 'Quem somos', 'Evolua <em>Tecnologia e Sistemas</em>',
      'Somos uma empresa de software de Cordilheira Alta - SC.',
      '<div class="mark"><img src="img/evolua-mark.svg"><b>EVOLU<i>A</i></b><small>TECNOLOGIA</small></div>')
story('quem-somos', 'O que fazemos', 'Sistemas de venda <em>que funcionam</em>',
      'Desenvolvemos soluções de automação comercial para quem vende muito e não pode parar.',
      bul([('📱', 'Aplicativos para maquininhas Android'), ('💻', 'Painel de gestão na nuvem'), ('🖨️', 'Impressão de fichas e comprovantes'), ('🤝', 'Suporte direto com quem desenvolve')]))
story('quem-somos', 'Nossos produtos', 'Uma família <em>de sistemas</em>',
      'Começamos pelos eventos e estamos levando a mesma tecnologia para outros negócios.',
      '<div class="products3">'
      '<div><i style="background:#1d5bff">🎟️</i><span><b>Evolua Ticket <em style="background:rgba(34,197,94,.18);color:#4ade80">Disponível</em></b><span>Venda de fichas para eventos</span></span></div>'
      '<div><i style="background:#f59e0b">🅿️</i><span><b>Evolua Parking <em style="background:rgba(245,158,11,.18);color:#fbbf24">Em desenvolvimento</em></b><span>Estacionamentos</span></span></div>'
      '<div><i style="background:#0891b2">🖥️</i><span><b>Evolua PDV <em style="background:rgba(43,140,255,.2);color:#7fb6ff">Em breve</em></b><span>Comércio • Windows e Android</span></span></div>'
      '</div>')
story('quem-somos', 'Nosso jeito', 'Feito por quem <em>vive o evento</em>',
      'Criamos o sistema dentro da rotina de festas, barracas e bares. Cada recurso resolve um problema real do caixa.',
      bul([('⚡', 'Velocidade na fila'), ('🔒', 'Segurança no caixa'), ('📊', 'Controle em tempo real')]))
story('quem-somos', 'Onde estamos', 'Rodovia SC-157, <em>Km 98</em>',
      'Bairro Industrial • Cordilheira Alta - SC',
      '<div class="cta-box" style="top:900px"><div><i style="background:#1d5bff">📍</i><span>Cordilheira Alta - SC<small>Rodovia SC-157, Km 98, Bairro Industrial</small></span></div><div><i>💬</i><span>(49) 98862-5010<small>WhatsApp</small></span></div><div><i style="background:#0f172a">🏢</i><span>JR Eventos e Serviços<small>CNPJ 17.735.913/0001-59</small></span></div></div>')

# ---------------------------------------------------------------- 2. EVOLUA TICKET
story('evolua-ticket', 'Evolua Ticket', 'O caixa do seu evento <em>na maquininha</em>',
      'Venda, cobrança e impressão das fichas no mesmo aparelho.', DEVS3)
story('evolua-ticket', 'Para que serve', 'Vender fichas <em>sem fila e sem furo</em>',
      'Substitui o bloco de fichas e a calculadora por um sistema que registra cada venda.',
      bul([('🎟️', 'Fichas impressas na hora da venda'), ('💳', 'Cartão, PIX e dinheiro'), ('🧾', 'Cada venda registrada'), ('📈', 'Relatórios no fim do evento')]))
story('evolua-ticket', 'Tudo em um', 'Sem notebook, <em>sem fio</em>',
      'A maquininha vira um ponto de venda completo. Liga, abre o caixa e vende.',
      '<img class="dev" style="max-height:900px" src="img/ficha-moderninha-smart-2.webp">')
story('evolua-ticket', 'Também no celular', 'Android + <em>impressora</em>',
      'Use o celular com uma impressora Bluetooth para barracas e pontos extras.',
      '<img src="img/celular-impressora.webp" style="max-height:950px;max-width:94%;object-fit:contain;filter:drop-shadow(0 30px 40px rgba(0,0,0,.5))">')
story('evolua-ticket', 'Diferencial', 'Funciona <em>sem internet</em>',
      'As vendas ficam guardadas na maquininha e sobem sozinhas para o painel quando a conexão volta.',
      phone(screen_img('combos') + '<div class="warn" style="position:absolute;z-index:4;left:16px;right:16px;top:300px;font-size:17px;box-shadow:0 10px 24px rgba(0,0,0,.25)">📶 Sem internet • 12 vendas guardadas</div>'))

# ---------------------------------------------------------------- 3. COMO FUNCIONA
story('como-funciona', 'Passo 1', 'Crie seu <em>evento</em>',
      'No painel, pelo computador ou pelo celular. Em poucos cliques ele aparece nas maquininhas.',
      shot('dashboard', 960))
story('como-funciona', 'Passo 2', 'Cadastre os <em>produtos</em>',
      'Nome, preço, foto e grupo. A maquininha atualiza o cardápio sozinha.',
      phone(screen_img('bebidas')))
story('como-funciona', 'Passo 3', 'Abra o <em>caixa</em>',
      'O operador informa o troco inicial e começa a vender.',
      phone(app('''<div class="card"><div class="dlg-title">Abrir caixa</div><div class="dlg-sub">Operador: Carla</div></div>
<div class="card"><div class="lbl">Troco inicial</div><div class="input">R$ 100,00</div></div>
<div class="card"><div class="row"><span>Evento</span><b>Festa da Cidade</b></div><div class="row" style="border:0"><span>Máquina</span><b>Caixa 03</b></div></div>
<div style="margin-top:auto;border-radius:14px;background:#16a34a;color:#fff;text-align:center;padding:20px;font-weight:900;font-size:20px" class="hl">ABRIR CAIXA</div>''')))
story('como-funciona', 'Passo 4', 'Toque e <em>cobre</em>',
      'Cada toque soma um item. Com o pedido pronto, é só tocar em COBRAR.',
      phone(screen_img('celular')))
story('como-funciona', 'Passo 5', 'Entregue <em>a ficha</em>',
      'Pagamento aprovado, a ficha sai impressa. Próximo cliente!',
      phone(app('''<div class="big-ok">✓</div><div class="dlg-title">Pagamento aprovado!</div><div class="dlg-sub">Retire suas fichas na impressora abaixo.</div>
<div class="card"><div class="row"><span>Pedido</span><b>#128</b></div><div class="row"><span>Forma</span><b>PIX</b></div><div class="row" style="border:0"><span>Fichas</span><b>4 impressas</b></div></div>
<div style="margin-top:auto;border-radius:14px;background:#1d5bff;color:#fff;text-align:center;padding:18px;font-weight:900">NOVA VENDA</div>''')))

# ---------------------------------------------------------------- 4. PAGAMENTOS
story('pagamentos', 'Pagamentos', 'Como o cliente <em>quiser pagar</em>',
      'Dinheiro, débito, crédito ou PIX, direto na tela do Evolua Ticket.', phone(app(pay())))
story('pagamentos', 'Cartão', 'Aproxime <em>ou insira</em>',
      'A cobrança acontece na própria maquininha, sem digitar o valor.',
      phone(app('''<div class="card" style="text-align:center"><div class="lbl">Crédito</div><div class="total">R$ 27,00</div></div>
<div class="big-wait">💳</div><div class="dlg-title">APROXIME, INSIRA OU PASSE O CARTÃO</div><div class="dlg-sub">Aguardando o cartão...</div>
<div style="margin-top:auto" class="btnrow"><div>Cancelar operação</div></div>''')))
story('pagamentos', 'PIX', 'QR Code <em>na tela</em>',
      'O cliente paga pelo app do banco e a venda é confirmada.',
      phone(app(f'''<div class="card" style="text-align:center"><div class="lbl">PIX</div><div class="total">R$ 27,00</div></div>
<div class="qr" style="width:230px;height:230px">{QR}</div><div class="dlg-title">Escaneie o QR Code</div><div class="dlg-sub">Pague pelo app do seu banco</div>''')))
story('pagamentos', 'Dinheiro', 'Troco <em>calculado</em>',
      'O operador digita o valor recebido e o sistema mostra o troco.',
      phone(app('''<div class="card" style="text-align:center"><div class="lbl">Dinheiro</div><div class="total">R$ 27,00</div></div>
<div class="card"><div class="lbl">Valor recebido</div><div class="input">R$ 50,00</div></div>
<div class="senha" style="background:#16a34a"><small style="color:#dcfce7">TROCO</small><b>R$ 23,00</b></div>
<div style="margin-top:auto;border-radius:14px;background:#16a34a;color:#fff;text-align:center;padding:18px;font-weight:900">CONFIRMAR</div>''')))
story('pagamentos', 'Flexível', 'Dividir, desconto <em>e taxa</em>',
      'Recursos que o dia a dia do evento pede.',
      bul([('🤝', 'Dividir o pagamento em várias formas'), ('🏷️', 'Desconto ou acréscimo'), ('🤵', 'Taxa de garçom opcional'), ('🔐', 'Estorno com senha de administrador')]))

# ---------------------------------------------------------------- 5. FICHAS
story('fichas', 'Fichas', 'A ficha sai <em>na hora</em>',
      'Impressa pela própria maquininha logo depois do pagamento.',
      '<img class="dev" style="max-height:950px" src="img/ficha-stone.webp">')
story('fichas', 'Controle', 'Com <em>QR Code</em>',
      'Código de barras, QR Code, número do pedido, data e forma de pagamento.',
      '<img src="img/ficha-festa.png" style="height:950px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))">')
story('fichas', 'Uma por item', 'Troca rápida <em>no balcão</em>',
      'Cada item sai em uma ficha própria. O balcão confere e entrega.',
      '<img src="img/ficha-show.png" style="height:820px;transform:rotate(-6deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))"><img src="img/ficha-quermesse.png" style="height:820px;transform:rotate(5deg);margin-left:-120px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))">')
story('fichas', 'Cozinha', 'Senha para <em>retirada</em>',
      'Lanches saem com senha e o pedido pode ir direto para a impressora da cozinha.',
      phone(app('''<div class="big-ok">✓</div><div class="dlg-title">Venda concluída!</div>
<div class="senha"><small>SUA SENHA</small><b>A13</b></div><div class="dlg-sub">Aguarde chamar a sua senha no balcão</div>
<div class="card"><div class="row"><span>1x X-Salada</span><b>R$ 24,00</b></div><div class="row" style="border:0"><span>1x Batata frita</span><b>R$ 15,00</b></div></div>''', event='Quermesse São José', status='Online • Barraca 2')))
story('fichas', 'Segurança', 'Sem bloco de ficha <em>pré-impresso</em>',
      'Cada ficha só existe porque uma venda foi paga.',
      bul([('🚫', 'Nada de ficha impressa antes do evento'), ('🔍', 'Conferência pelo QR Code'), ('🧾', 'Venda e ficha sempre batem')]))

# ---------------------------------------------------------------- 6. PAINEL
story('painel', 'Painel', 'O evento <em>em tempo real</em>',
      'Cada venda chega ao painel em segundos.', shot('dashboard', 960))
story('painel', 'Faturamento', 'Separado por <em>forma de pagamento</em>',
      'Dinheiro, PIX, débito, crédito, ticket médio e quantidade de fichas.',
      '<div class="big" style="top:800px"><div class="stat"><b>R$ 19.363</b><span>vendidos no evento</span></div><div class="stat"><b>602</b><span>vendas pagas</span></div><div class="stat"><b>R$ 32,16</b><span>ticket médio</span></div></div>')
story('painel', 'Indicadores', 'O que <em>mais vende</em>',
      'Produtos, grupos, venda anual e comparação entre eventos.', shot('graficos', 960))
story('painel', 'Monitor', 'Cada máquina <em>ao vivo</em>',
      'Bateria, conexão, operador, caixa e alertas de sangria e carregador.', shot('monitor', 960))
story('painel', 'Fechamento', 'Relatórios <em>em PDF</em>',
      'Feche o evento com tudo documentado.',
      bul([('📄', 'Totais de vendas'), ('👤', 'Vendas por operador'), ('📦', 'Quantidade vendida'), ('💼', 'Caixas e sangrias'), ('📈', 'Lucro com equipe e despesas')]))

# ---------------------------------------------------------------- 7. PARA QUEM
story('para-quem', 'Para quem', 'Para quem vende <em>muito e rápido</em>',
      'Onde tem fila, o Evolua Ticket trabalha.',
      '<div class="chips"><span>🎉 Festas</span><span>⛪ Quermesses</span><span>🎤 Shows</span><span>🤠 Rodeios</span><span>⚽ Eventos esportivos</span><span>🍺 Bares</span><span>🍔 Food parks</span><span>🎪 Feiras</span><span>🏫 Cantinas</span></div>')
story('para-quem', 'Festas e quermesses', 'Barracas <em>organizadas</em>',
      'Cada barraca com a sua maquininha e o organizador vendo tudo no painel.',
      phone(screen_img('comidas')))
story('para-quem', 'Shows e festivais', 'Fila grande, <em>venda rápida</em>',
      'Várias maquininhas ao mesmo tempo, todas no mesmo painel.',
      '<div class="food">' + ''.join(f'<div><img src="img/{f}.jpg"><p>{n}<small>R$ {p}</small></p></div>' for f, n, p in [
          ('cerveja-heineken', 'Heineken', '12,00'), ('cerveja-skol', 'Skol', '8,00'), ('agua-crystal', 'Água', '5,00'),
          ('balde-cerveja', 'Balde', '55,00'), ('vodka-smirnoff', 'Dose', '15,00'), ('lata-guarana', 'Guaraná', '6,00')]) + '</div>')
story('para-quem', 'Bares e food parks', 'Cardápio <em>com foto</em>',
      'Taxa de garçom, senha para retirada e impressora da cozinha.',
      '<div class="food">' + ''.join(f'<div><img src="img/{f}.jpg"><p>{n}<small>R$ {p}</small></p></div>' for f, n, p in [
          ('hamburguer-salada', 'X-Salada', '24,00'), ('hamburguer-duplo-bacon', 'Duplo Bacon', '34,00'), ('batata-frita', 'Batata frita', '15,00'),
          ('cachorro-quente', 'Cachorro-quente', '12,00'), ('churros-chocolate', 'Churros', '10,00'), ('crepe', 'Crepe', '14,00')]) + '</div>')
story('para-quem', 'Organizadores', 'Você <em>no controle</em>',
      'Saiba quanto vendeu, quem vendeu e quanto sobrou, sem esperar o fim da noite.',
      bul([('📊', 'Painel no celular'), ('👥', 'Vendas por operador'), ('🔋', 'Máquinas monitoradas'), ('💰', 'Lucro real do evento')]))

# ---------------------------------------------------------------- 8. CONTATO
CONTACTS = '<div class="cta-box"><div><i>💬</i><span>(49) 98862-5010<small>WhatsApp</small></span></div><div><i style="background:#1d5bff">🌐</i><span>evoluatecnologia.com.br<small>Site</small></span></div><div><i style="background:#0f172a">✉️</i><span>joelsonsistemas@gmail.com<small>E-mail</small></span></div></div>'
story('contato', 'Contato', 'Vamos <em>conversar?</em>',
      'Fale com a nossa equipe e tire as suas dúvidas.', CONTACTS)
story('contato', 'Demonstração', 'Veja <em>funcionando</em>',
      'Agende uma demonstração do Evolua Ticket na maquininha.',
      '<img class="dev" style="max-height:950px" src="img/ficha-cielo.webp">')
story('contato', 'WhatsApp', '(49) <em>98862-5010</em>',
      'Atendimento direto com quem desenvolve o sistema.',
      '<div class="mark"><div style="width:300px;height:300px;border-radius:80px;background:#16a34a;display:grid;place-items:center;font-size:170px;box-shadow:0 30px 60px rgba(22,163,74,.4)">💬</div></div>')
story('contato', 'Site', 'Conheça o <em>nosso site</em>',
      'www.evoluatecnologia.com.br: produtos, painel e maquininhas.', shot('dashboard', 960))
story('contato', 'Endereço', 'Venha <em>nos visitar</em>',
      'Rodovia SC-157, Km 98, Bairro Industrial, Cordilheira Alta - SC.',
      '<div class="mark"><img src="img/evolua-mark.svg"><b>EVOLU<i>A</i></b><small>TECNOLOGIA</small></div>')

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@800;900&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">'
count = 0
for gi, (g, gname) in enumerate(GROUPS, 1):
    for si, s in enumerate(stories[g], 1):
        count += 1
        prog = ''.join(f'<i class="{"on" if k <= si else ""}"></i>' for k in range(1, 6))
        vis = s['vis'] if s['vis'].startswith(('<div class="bullets">', '<div class="cta-box"', '<div class="big"', '<div class="chips">', '<div class="products3">')) else f'<div class="vis">{s["vis"]}</div>'
        html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{STORY_CSS}</style></head><body><div class="bg"></div><div class="grid"></div>
<div class="prog">{prog}</div>
<div class="top"><div class="logo"><img src="img/evolua-mark.svg"><div><b>EVOLU<i>A</i></b><small>TECNOLOGIA</small></div></div><span class="tag">{gname}</span></div>
<div class="head"><span class="kick">{s["kick"]}</span><h1>{s["title"]}</h1><p class="sub">{s["sub"]}</p></div>
{vis}
<div class="foot"><span><b>Evolua Tecnologia e Sistemas</b></span><span class="swipe">evoluatecnologia.com.br</span></div>
</body></html>'''
        (P / f's{gi}-{si}.html').write_text(html, encoding='utf-8')

# capas dos destaques (1080x1920, com o ícone no centro para recorte redondo)
ICONS = {'quem-somos': '🏢', 'evolua-ticket': '🎟️', 'como-funciona': '⚙️', 'pagamentos': '💳', 'fichas': '🧾', 'painel': '📊', 'para-quem': '🎉', 'contato': '💬'}
for gi, (g, gname) in enumerate(GROUPS, 1):
    html = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>*{{margin:0}}html,body{{width:1080px;height:1920px}}
body{{background:radial-gradient(700px 700px at 50% 50%,#1546b8,#071a4a 60%,#050d24);display:grid;place-items:center;font-family:Inter,sans-serif}}
.c{{width:620px;height:620px;border-radius:50%;background:linear-gradient(135deg,#2b8cff,#1d5bff 55%,#0d2e7a);display:grid;place-items:center;box-shadow:0 0 0 16px rgba(103,232,249,.35),0 40px 80px rgba(0,0,0,.5)}}
.c span{{font-size:300px}}</style></head><body><div class="c"><span>{ICONS[g]}</span></div></body></html>'''
    (P / f'capa{gi}.html').write_text(html, encoding='utf-8')
print(count)
