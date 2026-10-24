import pathlib, json

P = pathlib.Path(__file__).parent

CSS = r'''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Inter,sans-serif;color:#eef3ff;background:#050d24;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(900px 700px at 85% 25%,rgba(43,140,255,.35),transparent 65%),radial-gradient(700px 600px at 0% 100%,rgba(34,211,238,.14),transparent 60%),linear-gradient(180deg,#081634,#050d24)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:60px 60px;-webkit-mask-image:radial-gradient(ellipse at 60% 35%,#000 20%,transparent 70%)}
.top{position:absolute;left:70px;right:70px;top:60px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:14px}
.logo img{width:62px;height:62px}
.logo b{display:block;font-family:'Exo 2',Inter,sans-serif;font-weight:900;font-size:34px;letter-spacing:1px;line-height:1}
.logo b i{font-style:normal;color:#2b8cff}
.logo small{display:block;font-size:13px;font-weight:800;letter-spacing:6px;color:#67e8f9;margin-top:5px}
.tag{padding:10px 20px;border-radius:999px;background:rgba(43,140,255,.18);border:1px solid rgba(127,182,255,.35);color:#a9cdff;font-weight:800;font-size:20px;letter-spacing:.5px}
.tag.why{background:rgba(34,197,94,.16);border-color:rgba(74,222,128,.35);color:#86efac}
.head{position:absolute;left:70px;right:70px;top:170px}
.head .n{display:inline-block;font-weight:900;font-size:22px;color:#67e8f9;letter-spacing:3px;margin-bottom:16px}
h1{font-size:68px;font-weight:900;line-height:1.04;letter-spacing:-1.5px}
h1 em{font-style:normal;color:#5aa2ff}
.sub{margin-top:20px;font-size:29px;line-height:1.38;color:#b9c8e8;max-width:900px}
.vis{position:absolute;left:0;right:0;bottom:120px;top:520px;display:flex;align-items:center;justify-content:center;gap:28px}
.foot{position:absolute;left:70px;right:70px;bottom:46px;display:flex;justify-content:space-between;align-items:center;font-size:22px;font-weight:700;color:#8fa3c9}
.foot b{color:#fff}
.swipe{color:#67e8f9}
/* aparelhos */
.dev{height:100%;max-height:700px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))}
.shot{border-radius:22px;overflow:hidden;border:1px solid rgba(148,178,255,.25);box-shadow:0 30px 70px rgba(0,0,0,.55);background:#0a1838}
.shot .bar{display:flex;gap:9px;padding:14px 18px;background:#0a1838;border-bottom:1px solid rgba(148,178,255,.18)}
.shot .bar i{width:13px;height:13px;border-radius:50%;background:#f87171}.shot .bar i+i{background:#fbbf24}.shot .bar i+i+i{background:#34d399}
.shot img{display:block;width:100%}
/* celular */
.phone{position:relative;width:370px;height:740px;border-radius:58px;padding:12px;background:linear-gradient(135deg,#5b6170,#22252c 25%,#121418 55%,#3b404b 85%,#6b7280);box-shadow:0 40px 70px rgba(0,0,0,.6),inset 0 0 0 2px rgba(255,255,255,.15)}
.phone .glass{width:100%;height:100%;border-radius:47px;background:#000;padding:8px;overflow:hidden}
.phone .scr{position:relative;width:100%;height:100%;border-radius:40px;overflow:hidden;background:#e8eef8}
.phone .island{position:absolute;z-index:5;top:22px;left:50%;transform:translateX(-50%);width:110px;height:30px;border-radius:16px;background:#000}
.phone.tilt{transform:rotate(-5deg)}
/* tela do app (escala 340px de largura) */
.app{position:absolute;inset:0;display:flex;flex-direction:column;background:#e8eef8;color:#0b1a3a;font-size:15px}
.app-top{display:flex;align-items:center;gap:10px;padding:64px 16px 14px;background:linear-gradient(90deg,#071a4a,#0d2e7a,#1546b8);color:#fff}
.app-top .m{width:22px;height:16px;background:linear-gradient(#fff,#fff) 0 0/100% 3px no-repeat,linear-gradient(#fff,#fff) 0 50%/100% 3px no-repeat,linear-gradient(#fff,#fff) 0 100%/100% 3px no-repeat}
.app-top img{width:36px;height:36px}
.app-top b{display:block;font-size:11px;font-weight:900;letter-spacing:2px}.app-top b span{color:#67e8f9}
.app-top strong{display:block;font-size:18px;font-weight:800}
.app-top small{display:flex;align-items:center;gap:6px;font-size:12px;color:#c7d5f5}.app-top small i{width:8px;height:8px;border-radius:50%;background:#4ade80}
.app-top small i.off{background:#fbbf24}
.app-body{flex:1;padding:16px;display:flex;flex-direction:column;gap:12px}
.app-bottom{display:flex;align-items:center;gap:10px;padding:14px 16px 22px;background:linear-gradient(90deg,#071a4a,#0d2e7a,#1546b8);color:#fff}
.app-bottom div{flex:1}.app-bottom small{display:block;font-size:12px;color:#c7d5f5}.app-bottom b{font-size:28px;font-weight:900}
.app-bottom span{padding:14px 20px;border-radius:12px;background:#2b8cff;font-weight:900;font-size:16px;letter-spacing:1px}
.card{background:#fff;border:2px solid #c6d3ea;border-radius:16px;padding:14px}
.dlg-title{font-size:22px;font-weight:900;text-align:center;margin:6px 0 2px}
.dlg-sub{font-size:14px;color:#4b5c7e;text-align:center}
.total{font-size:40px;font-weight:900;text-align:center;color:#0b1a3a}
.pay{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pay div{border-radius:16px;padding:18px 10px;text-align:center;font-weight:900;font-size:17px;color:#fff}
.pay div small{display:block;font-size:12px;font-weight:700;opacity:.85;margin-top:3px}
.pay .din{background:#16a34a}.pay .deb{background:#1d5bff}.pay .cre{background:#7c3aed}.pay .pix{background:#0891b2}
.hl{outline:5px solid #fbbf24;outline-offset:3px;position:relative}
.btnrow{display:flex;gap:10px}.btnrow div{flex:1;border-radius:12px;padding:13px;text-align:center;font-weight:800;font-size:14px;background:#fff;border:2px solid #c6d3ea;color:#334155}
.big-ok{width:96px;height:96px;border-radius:50%;margin:10px auto 4px;display:grid;place-items:center;background:#16a34a;color:#fff;font-size:56px;font-weight:900}
.big-wait{width:110px;height:110px;border-radius:50%;margin:20px auto 4px;display:grid;place-items:center;border:8px solid #c6d3ea;border-top-color:#1d5bff;font-size:44px}
.senha{margin:8px auto;border-radius:14px;background:#0b1a3a;color:#fff;text-align:center;padding:16px;font-weight:900}
.senha small{display:block;font-size:13px;letter-spacing:3px;color:#67e8f9}
.senha b{font-size:54px;letter-spacing:2px}
.row{display:flex;justify-content:space-between;font-size:15px;padding:7px 0;border-bottom:1px dashed #d4dbe8}
.row b{font-weight:900}
.input{border:2px solid #c6d3ea;border-radius:12px;padding:12px 14px;font-size:20px;font-weight:800;background:#f7f9fd}
.lbl{font-size:12px;font-weight:800;color:#4b5c7e;letter-spacing:.5px;text-transform:uppercase;margin-bottom:5px}
.pill{display:inline-block;padding:6px 12px;border-radius:999px;font-size:12px;font-weight:800}
.warn{background:#fff4e2;color:#b45309;border:2px solid #fcd34d;border-radius:14px;padding:12px;font-weight:800;font-size:14px;text-align:center}
.qr{width:190px;height:190px;margin:4px auto;background:#fff;padding:10px;border-radius:12px;border:2px solid #c6d3ea}
/* lista de benefícios (posts "por que") */
.bullets{position:absolute;left:70px;right:70px;top:500px;bottom:130px;display:grid;gap:22px;align-content:center}
.bullets div{display:flex;gap:24px;align-items:center;padding:34px 34px;border-radius:22px;background:linear-gradient(180deg,#122656,#0e1f48);border:1px solid rgba(148,178,255,.18);font-size:34px;font-weight:700}
.bullets i{flex:0 0 auto;width:72px;height:72px;border-radius:16px;display:grid;place-items:center;background:rgba(43,140,255,.2);color:#7fb6ff;font-style:normal;font-size:30px}
.bignum{font-size:200px;font-weight:900;line-height:.9;background:linear-gradient(90deg,#fff,#67e8f9);-webkit-background-clip:text;color:transparent}
.food{display:grid;grid-template-columns:repeat(3,270px);gap:20px}
.food div{background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.4)}
.food img{width:100%;height:220px;object-fit:contain;background:#fff;display:block}
.food p{padding:10px;text-align:center;color:#0b1a3a;font-weight:900;font-size:20px}
.food p small{display:block;color:#0b6fa8;font-size:17px}
.cta-box{position:absolute;left:70px;right:70px;top:600px;display:grid;gap:18px}
.cta-box div{display:flex;align-items:center;gap:22px;padding:26px 30px;border-radius:24px;background:linear-gradient(180deg,#122656,#0e1f48);border:1px solid rgba(148,178,255,.2);font-size:32px;font-weight:800}
.cta-box i{width:66px;height:66px;border-radius:18px;display:grid;place-items:center;background:#16a34a;font-style:normal;font-size:34px}
.cta-box small{display:block;font-size:20px;color:#9fb0cf;font-weight:600}
'''

def phone(inner, tilt=False, extra_style=''):
    return f'<div class="phone{" tilt" if tilt else ""}" style="{extra_style}"><div class="glass"><div class="scr"><div class="island"></div>{inner}</div></div></div>'

def app(body, event='Festa da Cidade', status='Online • Caixa 03', bottom=None, off=False):
    st = f'<small><i class="{"off" if off else ""}"></i>{status}</small>'
    bt = bottom if bottom is not None else ''
    return f'<div class="app"><div class="app-top"><i class="m"></i><img src="img/evolua-mark.svg"><div><b>EVOLUA <span>TICKET</span></b><strong>{event}</strong>{st}</div></div><div class="app-body">{body}</div>{bt}</div>'

def bottom(n, t, hl=False):
    return f'<div class="app-bottom"><div><small>{n} • toque para ver</small><b>{t}</b></div><span class="{"hl" if hl else ""}">COBRAR</span></div>'

def screen_img(name):
    return f'<img src="img/scr-{name}.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top">'

def shot(img, w):
    return f'<div class="shot" style="width:{w}px"><div class="bar"><i></i><i></i><i></i></div><img src="img/{img}.webp"></div>'

QR = '<svg viewBox="0 0 21 21" style="width:100%;height:100%" shape-rendering="crispEdges">' + ''.join(
    f'<rect x="{x}" y="{y}" width="1" height="1"/>' for y in range(21) for x in range(21)
    if (x < 7 and y < 7 and (x in (0, 6) or y in (0, 6) or (2 <= x <= 4 and 2 <= y <= 4)))
    or (x > 13 and y < 7 and (x in (14, 20) or y in (0, 6) or (16 <= x <= 18 and 2 <= y <= 4)))
    or (x < 7 and y > 13 and (x in (0, 6) or y in (14, 20) or (2 <= x <= 4 and 16 <= y <= 18)))
    or (not (x < 8 and y < 8) and not (x > 12 and y < 8) and not (x < 8 and y > 12) and (x * 7 + y * 13 + x * y) % 3 == 0)) + '</svg>'

PAY = '''<div class="card"><div class="dlg-title">Como você quer pagar?</div><div class="total">R$ 29,00</div><div class="dlg-sub">3 itens</div></div>
<div class="pay"><div class="din{h0}">Dinheiro<small>troco na tela</small></div><div class="deb{h1}">Débito</div><div class="cre{h2}">Crédito</div><div class="pix{h3}">PIX<small>QR Code</small></div></div>
<div class="btnrow"><div>Dividir pagamento</div><div>Desconto / acréscimo</div></div>'''

def pay(h=None):
    return PAY.format(**{f'h{i}': (' hl' if h == i else '') for i in range(4)})

posts = []
def post(kind, n, title, sub, vis, caption):
    posts.append(dict(kind=kind, n=n, title=title, sub=sub, vis=vis, caption=caption))

# ---------------------------------------------------------------- COMO FUNCIONA (20)
post('how', 1, 'Conheça o <em>Evolua Ticket</em>',
     'O sistema de fichas para eventos que vende, cobra e imprime direto na maquininha de cartão.',
     ''.join(f'<img class="dev" style="max-height:690px" src="img/ficha-{n}.webp">' for n in ['moderninha-smart-2', 'stone', 'cielo']),
     'Conheça o Evolua Ticket 🎟️\n\nO sistema de fichas para eventos que transforma a maquininha de cartão em um caixa completo: o operador toca nos produtos, cobra no cartão ou no PIX e a ficha sai impressa na hora.\n\nNesta série a gente mostra, passo a passo, como ele funciona. Salva o post e acompanha! 👇')
post('how', 2, 'Tudo começa <em>no painel</em>',
     'Crie o evento pelo computador ou pelo celular. Em poucos cliques ele já aparece nas maquininhas.',
     shot('dashboard', 940),
     'Passo 1: crie seu evento no painel 💻\n\nNo painel do cliente você cria o evento, define os caixas e acompanha tudo em tempo real. Funciona no computador e no celular, de qualquer lugar.')
post('how', 3, 'Produtos com <em>foto e preço</em>',
     'Cadastre o cardápio com foto. Na maquininha, o operador encontra tudo com um toque.',
     phone(screen_img('bebidas')),
     'Passo 2: cadastre seus produtos 🍺🥤\n\nCada produto com nome, preço e foto. Na tela da maquininha fica tudo visual: o operador encontra o item na hora e a fila anda.')
post('how', 4, 'Organizado <em>por grupos</em>',
     'Bebidas, lanches, doces: cada grupo com a sua cor. É só deslizar para trocar.',
     phone(screen_img('comidas'), tilt=True),
     'Passo 3: organize por grupos 🍔🍫\n\nBebidas, lanches, doces, combos... Cada grupo com a sua cor. O operador desliza para trocar de grupo e vende sem procurar.')
post('how', 5, 'Abra o caixa <em>em segundos</em>',
     'O operador informa o valor do troco inicial e começa a vender. Cada caixa fica registrado no nome dele.',
     phone(app('''<div class="card"><div class="dlg-title">Abrir caixa</div><div class="dlg-sub">Operador: Carla</div></div>
<div class="card"><div class="lbl">Troco inicial</div><div class="input">R$ 100,00</div></div>
<div class="card"><div class="row"><span>Evento</span><b>Festa da Cidade</b></div><div class="row"><span>Máquina</span><b>Caixa 03</b></div><div class="row" style="border:0"><span>Horário</span><b>19:02</b></div></div>
<div style="margin-top:auto;border-radius:14px;background:#16a34a;color:#fff;text-align:center;padding:18px;font-weight:900;font-size:18px" class="hl">ABRIR CAIXA</div>''')),
     'Passo 4: abra o caixa 💵\n\nAntes de começar, o operador informa o troco inicial. A partir daí, cada venda fica registrada no caixa dele, com horário e forma de pagamento.')
post('how', 6, 'Toque e <em>monte o pedido</em>',
     'Cada toque soma um item. O contador mostra a quantidade e o total aparece embaixo.',
     phone(screen_img('celular')),
     'Passo 5: toque nos produtos 👆\n\nCada toque soma um item ao pedido. O número verde mostra a quantidade e o total aparece na barra de baixo. Simples para qualquer operador.')
post('how', 7, 'Botão <em>COBRAR</em>',
     'Com o pedido pronto, um toque em COBRAR abre as formas de pagamento.',
     phone(app('''<div class="card"><div class="row"><span>2x Skol</span><b>R$ 16,00</b></div><div class="row"><span>1x Água</span><b>R$ 5,00</b></div><div class="row" style="border:0"><span>1x Guaraná</span><b>R$ 6,00</b></div></div>
<div class="card" style="text-align:center"><div class="lbl">Total do pedido</div><div class="total">R$ 27,00</div></div>''', bottom=bottom('4 itens', 'R$ 27,00', hl=True))),
     'Passo 6: toque em COBRAR 💳\n\nO pedido aparece conferido na tela e, com um toque em COBRAR, o sistema abre as formas de pagamento. Sem digitar valor na maquininha: o total vai direto.')
post('how', 8, 'Escolha a <em>forma de pagamento</em>',
     'Dinheiro, débito, crédito ou PIX. O valor vai direto para a cobrança, sem digitar.',
     phone(app(pay())),
     'Passo 7: escolha como receber 💰\n\nDinheiro (com cálculo de troco), débito, crédito ou PIX. Dá também para dividir o pagamento e aplicar desconto ou acréscimo.')
post('how', 9, 'No cartão: <em>aproxime ou insira</em>',
     'A cobrança acontece na própria maquininha. As mensagens do cartão aparecem na tela do Evolua Ticket.',
     phone(app('''<div class="card" style="text-align:center"><div class="lbl">Débito</div><div class="total">R$ 27,00</div></div>
<div class="big-wait">💳</div><div class="dlg-title">APROXIME, INSIRA OU PASSE O CARTÃO</div><div class="dlg-sub">Aguardando o cartão...</div>
<div style="margin-top:auto" class="btnrow"><div>Cancelar operação</div></div>''')),
     'Passo 8: cartão na própria maquininha 💳\n\nO cliente aproxima ou insere o cartão ali mesmo. As mensagens da maquininha aparecem na tela do Evolua Ticket, e o operador acompanha tudo.')
post('how', 10, 'PIX <em>sem complicação</em>',
     'O QR Code aparece na tela. O cliente paga pelo celular e a venda é confirmada.',
     phone(app(f'''<div class="card" style="text-align:center"><div class="lbl">PIX</div><div class="total">R$ 27,00</div></div>
<div class="qr">{QR}</div><div class="dlg-title">Escaneie o QR Code</div><div class="dlg-sub">Pague pelo app do seu banco</div>
<div style="margin-top:auto" class="btnrow"><div>Cancelar operação</div></div>''')),
     'Passo 9: PIX na hora ⚡\n\nEscolheu PIX? O QR Code aparece na tela, o cliente paga pelo app do banco e a venda é confirmada.')
post('how', 11, 'Aprovado: <em>ficha na mão</em>',
     'Pagamento aprovado, as fichas saem impressas na hora. Uma ficha por item, pronta para retirar.',
     phone(app('''<div class="big-ok">✓</div><div class="dlg-title">Pagamento aprovado!</div><div class="dlg-sub">Retire suas fichas na impressora abaixo.</div>
<div class="card"><div class="row"><span>Pedido</span><b>#128</b></div><div class="row"><span>Forma</span><b>Débito</b></div><div class="row" style="border:0"><span>Fichas</span><b>4 impressas</b></div></div>
<div style="margin-top:auto;border-radius:14px;background:#1d5bff;color:#fff;text-align:center;padding:16px;font-weight:900">NOVA VENDA</div>''')) +
     '<img src="img/ficha-festa.png" style="height:560px;filter:drop-shadow(0 20px 30px rgba(0,0,0,.5));transform:rotate(4deg)">',
     'Passo 10: aprovado, ficha impressa 🧾\n\nCom o pagamento aprovado, as fichas saem na impressora da maquininha na mesma hora. Uma ficha por item, pronta para trocar no balcão.')
post('how', 12, 'Ficha com <em>QR Code</em>',
     'Cada ficha sai com código de barras, QR Code, número do pedido e forma de pagamento.',
     '<img src="img/ficha-festa.png" style="height:640px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.55))">',
     'Detalhe que faz diferença 🔍\n\nCada ficha sai com o nome do evento, o produto, código de barras, QR Code, número do pedido, data e forma de pagamento. Mais controle e menos fraude no balcão.')
post('how', 13, 'Senha para <em>retirada</em>',
     'Lanches e pratos saem com senha. A cozinha chama pelo número e ninguém se perde.',
     phone(app('''<div class="big-ok">✓</div><div class="dlg-title">Venda concluída!</div>
<div class="senha"><small>SUA SENHA</small><b>A13</b></div><div class="dlg-sub">Aguarde chamar a sua senha no balcão</div>
<div class="card"><div class="row"><span>1x X-Salada</span><b>R$ 24,00</b></div><div class="row" style="border:0"><span>1x Batata frita</span><b>R$ 15,00</b></div></div>''', event='Quermesse São José', status='Online • Barraca 2')),
     'Senha para retirada 🔢\n\nProdutos de cozinha saem com senha na ficha. O pedido também pode ir para a impressora da cozinha, e o cliente retira quando a senha for chamada.')
post('how', 14, 'Dividir <em>o pagamento</em>',
     'Parte no PIX, parte no cartão, parte em dinheiro. O sistema controla quanto falta.',
     phone(app('''<div class="card"><div class="dlg-title">Dividir pagamento</div><div class="total">R$ 60,00</div></div>
<div class="card"><div class="row"><span>PIX</span><b>R$ 30,00 ✓</b></div><div class="row"><span>Crédito</span><b>R$ 20,00 ✓</b></div><div class="row" style="border:0"><span>Falta</span><b style="color:#d92d3a">R$ 10,00</b></div></div>
<div class="pay"><div class="din hl">Dinheiro</div><div class="deb">Débito</div></div>''')),
     'Dividir pagamento 🤝\n\nA galera quer rachar a conta? Sem problema: parte no PIX, parte no cartão, parte em dinheiro. O sistema mostra quanto falta até fechar.')
post('how', 15, 'Taxa de <em>garçom</em>',
     'Ative a taxa de serviço no evento. Ela entra no pedido e o operador pode retirar se o cliente pedir.',
     phone(app('''<div class="card"><div class="row"><span>Subtotal</span><b>R$ 80,00</b></div><div class="row"><span>Taxa de garçom (10%)</span><b>R$ 8,00</b></div><div class="row" style="border:0"><span>Total</span><b>R$ 88,00</b></div></div>
<div class="btnrow"><div class="hl">Retirar taxa</div><div>Dividir pagamento</div></div>
<div class="pay"><div class="din">Dinheiro</div><div class="deb">Débito</div><div class="cre">Crédito</div><div class="pix">PIX</div></div>''')),
     'Taxa de garçom 🤵\n\nPara bares e eventos com atendimento na mesa: ative a taxa no painel e ela entra automaticamente no pedido. Se o cliente pedir, o operador retira com um toque. O valor aparece separado nos relatórios.')
post('how', 16, 'Desconto ou <em>acréscimo</em>',
     'Aplique desconto ou acréscimo em valor ou porcentagem, direto na tela de pagamento.',
     phone(app('''<div class="card"><div class="dlg-title">Desconto / acréscimo</div></div>
<div class="btnrow"><div class="hl">Desconto</div><div>Acréscimo</div></div>
<div class="btnrow"><div>R$</div><div class="hl">%</div></div>
<div class="card"><div class="lbl">Valor</div><div class="input">10%</div></div>
<div class="card"><div class="row"><span>Antes</span><b>R$ 50,00</b></div><div class="row" style="border:0"><span>Novo total</span><b style="color:#16a34a">R$ 45,00</b></div></div>''')),
     'Desconto ou acréscimo 🏷️\n\nPromoção de última hora? Aplique desconto ou acréscimo em reais ou em porcentagem, direto na tela de pagamento. Tudo registrado na venda.')
post('how', 17, 'Caiu a internet? <em>Continua vendendo</em>',
     'As vendas ficam guardadas na maquininha e sobem sozinhas para o painel quando a conexão volta.',
     phone(screen_img('combos') + '<div class="warn" style="position:absolute;z-index:4;left:14px;right:14px;top:232px;box-shadow:0 10px 24px rgba(0,0,0,.25)">📶 Sem internet • 12 vendas guardadas na máquina</div>'),
     'Sem internet? Sem problema 📶❌\n\nEm evento, a internet cai. O Evolua Ticket continua vendendo: as vendas ficam guardadas na maquininha e sobem sozinhas para o painel quando a conexão volta, sem duplicar nada.')
post('how', 18, 'Estorno <em>com segurança</em>',
     'Cancelamento só com senha ou cartão de administrador. Tudo fica registrado.',
     phone(app('''<div class="card"><div class="dlg-title">Estorno</div><div class="dlg-sub">Pedido #128 • Débito • R$ 27,00</div></div>
<div class="card" style="text-align:center"><div style="font-size:54px">🔐</div><div class="dlg-title" style="font-size:18px">Aproxime o cartão de administrador</div><div class="dlg-sub">ou digite a senha</div></div>
<div class="card"><div class="lbl">Senha do administrador</div><div class="input">••••</div></div>
<div style="margin-top:auto;border-radius:14px;background:#d92d3a;color:#fff;text-align:center;padding:16px;font-weight:900">CONFIRMAR ESTORNO</div>''')),
     'Estorno seguro 🔐\n\nCancelar uma venda exige senha ou o cartão NFC de administrador. O estorno é feito na maquininha e fica registrado no relatório. Sem cancelamento escondido.')
post('how', 19, 'Sangria e <em>fechamento</em>',
     'O sistema avisa quando a gaveta enche. No fim, o fechamento mostra tudo por forma de pagamento.',
     phone(app('''<div class="card"><div class="dlg-title">Fechar caixa</div><div class="dlg-sub">Carla • aberto às 19:02</div></div>
<div class="card"><div class="row"><span>Dinheiro</span><b>R$ 472,00</b></div><div class="row"><span>Débito</span><b>R$ 923,00</b></div><div class="row"><span>Crédito</span><b>R$ 832,00</b></div><div class="row"><span>PIX</span><b>R$ 1.333,00</b></div><div class="row" style="border:0"><span>Total</span><b>R$ 3.560,00</b></div></div>
<div class="card"><div class="row"><span>Troco inicial</span><b>R$ 100,00</b></div><div class="row"><span>Sangrias</span><b>- R$ 0,00</b></div><div class="row" style="border:0"><span>Na gaveta</span><b>R$ 572,00</b></div></div>
<div style="margin-top:auto;border-radius:14px;background:#0b1a3a;color:#fff;text-align:center;padding:16px;font-weight:900">FECHAR CAIXA</div>''')),
     'Sangria e fechamento de caixa 💼\n\nQuando a gaveta passa do limite, o sistema avisa que é hora da sangria. No fim do evento, o fechamento mostra o total por forma de pagamento e o dinheiro que deve estar na gaveta.')
post('how', 20, 'Monitor das <em>máquinas</em>',
     'Bateria, caixa aberto, vendas e alertas de cada maquininha, ao vivo no painel.',
     shot('monitor', 960),
     'Monitor das máquinas 🔋📊\n\nNo painel você vê cada maquininha ao vivo: online ou offline, bateria, operador, vendas por forma de pagamento, dinheiro na gaveta e fichas impressas. Com alerta de sangria e de carregador.\n\nE os relatórios fecham o evento em PDF. Quer ver funcionando? Chama no direct ou no WhatsApp! 📲')

# ---------------------------------------------------------------- POR QUE CONTRATAR (10)
def bullets(items):
    return '<div class="bullets">' + ''.join(f'<div><i>{e}</i><span>{t}</span></div>' for e, t in items) + '</div>'

post('why', 1, 'Fila <em>andando</em>',
     'Cada venda leva segundos: toque, cobre e entregue a ficha.',
     bullets([('⚡', 'Produtos com foto, um toque por item'), ('💳', 'Valor vai direto para a cobrança'), ('🧾', 'Ficha impressa na hora'), ('😊', 'Cliente atendido rápido volta a comprar')]),
     'Por que ter o Evolua Ticket? #1: fila andando ⚡\n\nFila grande é venda perdida. Com o Evolua Ticket o operador toca nos produtos, cobra e entrega a ficha em segundos. Mais gente atendida, mais faturamento.')
post('why', 2, 'Adeus, <em>caixa furado</em>',
     'Cada venda registrada com operador, horário e forma de pagamento.',
     bullets([('👤', 'Caixa aberto no nome de cada operador'), ('🧮', 'Troco calculado pelo sistema'), ('💵', 'Dinheiro na gaveta sempre conferido'), ('📋', 'Fechamento com tudo separado')]),
     'Por que ter o Evolua Ticket? #2: caixa que bate 🧮\n\nCada venda fica registrada com operador, horário e forma de pagamento. No fechamento você sabe exatamente quanto deve ter na gaveta.')
post('why', 3, 'Ficha com <em>controle</em>',
     'Chega de bloco de ficha impressa antes: cada ficha nasce de uma venda paga.',
     '<img src="img/ficha-quermesse.png" style="height:600px;filter:drop-shadow(0 26px 34px rgba(0,0,0,.55));transform:rotate(-3deg)">',
     'Por que ter o Evolua Ticket? #3: fichas com controle 🔍\n\nNada de bloco de fichas impresso antes do evento. Cada ficha só existe porque uma venda foi paga, e sai com código de barras, QR Code e número do pedido.')
post('why', 4, 'Funciona <em>sem internet</em>',
     'Sinal ruim no evento não para a sua venda.',
     bullets([('📶', 'Vende mesmo com a internet fora'), ('💾', 'Vendas guardadas na maquininha'), ('🔄', 'Sincroniza sozinho quando volta'), ('✅', 'Sem venda duplicada')]),
     'Por que ter o Evolua Ticket? #4: não para quando a internet cai 📶\n\nEvento no meio do campo, festa lotada, sinal fraco... O Evolua Ticket continua vendendo e manda tudo para o painel quando a conexão volta.')
post('why', 5, '<em>Tudo em um</em> só aparelho',
     'Sem notebook, sem fio, sem impressora separada.',
     ''.join(f'<img class="dev" style="max-height:640px" src="img/ficha-{n}.webp">' for n in ['moderninha-smart-2', 'stone']),
     'Por que ter o Evolua Ticket? #5: tudo em um aparelho 📱\n\nVenda, cobrança no cartão ou PIX e impressão da ficha no mesmo equipamento. Sem notebook, sem fio, sem impressora separada. Liga e vende.')
post('why', 6, 'Acompanhe <em>de qualquer lugar</em>',
     'Do celular, você vê o evento inteiro em tempo real.',
     shot('graficos', 960),
     'Por que ter o Evolua Ticket? #6: o evento na palma da mão 📊\n\nVendas, produtos mais vendidos, caixas e máquinas em tempo real, pelo celular ou computador. Você não precisa estar no caixa para saber como está indo.')
post('why', 7, 'Saiba o <em>lucro real</em>',
     'Cadastre equipe e despesas e veja quanto o evento deu de verdade.',
     bullets([('👷', 'Funcionários e comissões'), ('🧾', 'Despesas do evento'), ('📈', 'Lucro calculado pelo sistema'), ('📄', 'Relatórios em PDF')]),
     'Por que ter o Evolua Ticket? #7: lucro de verdade 📈\n\nFaturamento não é lucro. No painel você cadastra equipe e despesas do evento e o sistema mostra quanto sobrou de verdade.')
post('why', 8, 'Controle por <em>operador</em>',
     'Saiba quem vendeu, quanto vendeu e em qual caixa.',
     bullets([('🏆', 'Vendas por operador'), ('🔐', 'Estorno só com autorização'), ('🔋', 'Máquinas monitoradas ao vivo'), ('🗂️', 'Histórico de tudo')]),
     'Por que ter o Evolua Ticket? #8: controle da equipe 👥\n\nRelatório de vendas por operador, estorno só com senha ou cartão de administrador e monitor das máquinas ao vivo. Você confia na equipe e confere quando quiser.')
post('why', 9, 'Cardápio que <em>vende mais</em>',
     'Produto com foto chama atenção e acelera a escolha.',
     '<div class="food">' + ''.join(f'<div><img src="img/{f}.jpg"><p>{n}<small>R$ {p}</small></p></div>' for f, n, p in [
         ('hamburguer-salada', 'X-Salada', '24,00'), ('cachorro-quente', 'Cachorro-quente', '12,00'), ('batata-frita', 'Batata frita', '15,00'),
         ('churros-chocolate', 'Churros', '10,00'), ('cerveja-skol', 'Skol', '8,00'), ('maca-do-amor', 'Maçã do amor', '8,00')]) + '</div>',
     'Por que ter o Evolua Ticket? #9: cardápio que dá água na boca 🍔\n\nCom foto em cada produto, o operador acha rápido e o cliente decide na hora. Você muda preço e produto pelo painel e a maquininha atualiza.')
post('why', 10, 'Vem <em>evoluir</em> com a gente',
     'Fale com a nossa equipe e veja o Evolua Ticket funcionando no seu evento.',
     '<div class="cta-box"><div><i>💬</i><span>(49) 98862-5010<small>WhatsApp</small></span></div><div><i style="background:#1d5bff">🌐</i><span>evoluatecnologia.com.br<small>Site</small></span></div><div><i style="background:#c026d3">📸</i><span>@evoluaticket<small>Instagram</small></span></div></div>',
     'Vem evoluir com a gente 🚀\n\nFesta, quermesse, show, rodeio, feira, bar ou food park: o Evolua Ticket deixa a venda mais rápida, o caixa mais seguro e você no controle.\n\n📲 WhatsApp: (49) 98862-5010\n🌐 evoluatecnologia.com.br')

HASHTAGS = '#EvoluaTicket #EvoluaTecnologia #fichas #eventos #sistemaparaeventos #maquininha #pdv #festas #quermesse #bar #foodpark #gestaodeeventos #SantaCatarina'

for i, p in enumerate(posts, 1):
    tag = f'Como funciona • {p["n"]}/20' if p['kind'] == 'how' else f'Por que contratar • {p["n"]}/10'
    head = '' if p['kind'] == 'why' and p['n'] in () else ''
    vis = p['vis'] if p['vis'].startswith('<div class="bullets">') or p['vis'].startswith('<div class="cta-box">') else f'<div class="vis">{p["vis"]}</div>'
    html = f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@800;900&family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="bg"></div><div class="grid"></div>
<div class="top"><div class="logo"><img src="img/evolua-mark.svg"><div><b>EVOLU<i>A</i></b><small>TICKET</small></div></div><span class="tag{" why" if p["kind"]=="why" else ""}">{tag}</span></div>
<div class="head"><h1>{p["title"]}</h1><p class="sub">{p["sub"]}</p></div>
{vis}
<div class="foot"><span><b>@evoluaticket</b> • evoluatecnologia.com.br</span><span class="swipe">{"Salve este post ➜" if i < 30 else "Chama no WhatsApp ➜"}</span></div>
</body></html>'''
    (P / f'p{i:02d}.html').write_text(html, encoding='utf-8')

with open(P / 'out' / 'legendas.txt', 'w', encoding='utf-8') as f:
    for i, p in enumerate(posts, 1):
        f.write(f'===== POST {i:02d} =====\n{p["caption"]}\n\n{HASHTAGS}\n\n')
print(len(posts))
