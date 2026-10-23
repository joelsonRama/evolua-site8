/* =========================================================
   EVOLUA TECNOLOGIA - CONFIGURAÇÃO DO SITE
   Preencha os contatos aqui. Campo vazio = não aparece no site.
========================================================= */
const EVOLUA = {
    whatsapp: '5549988625010', // só números, com DDI e DDD. Ex.: '5511999999999'
    telefone: '(49) 98862-5010', // como deve aparecer. Ex.: '(11) 99999-9999'
    email: 'joelsonsistemas@gmail.com', // Ex.: 'contato@evoluatecnologia.com.br'
    instagram: 'evoluaticket', // só o usuário, sem @. Ex.: 'evoluatecnologia'
    cidade: 'Rodovia SC-157, Km 98, Bairro Industrial, Cordilheira Alta - SC', // Ex.: 'São Paulo - SP'
    // Endereço que recebe as mensagens dos formulários (painel do Administrador Geral > Mensagens do site).
    // Vazio: o formulário abre o WhatsApp com a mensagem pronta.
    mensagens: '',
    empresa: 'Evolua Tecnologia • CNPJ 17.735.913/0001-59' // razão social e CNPJ. Ex.: 'Evolua Tecnologia LTDA • CNPJ 00.000.000/0001-00'
};

(function () {
    'use strict';

    /* Menu do celular */
    const menuBtn = document.querySelector('.menu-btn');
    const nav = document.querySelector('.nav');
    if (menuBtn && nav) {
        menuBtn.addEventListener('click', function () {
            const open = nav.classList.toggle('open');
            menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        nav.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () { nav.classList.remove('open'); });
        });
    }

    /* Ano no rodapé */
    document.querySelectorAll('[data-year]').forEach(function (el) {
        el.textContent = new Date().getFullYear();
    });

    /* Contatos */
    const waLink = function (msg) {
        return 'https://wa.me/' + EVOLUA.whatsapp + (msg ? '?text=' + encodeURIComponent(msg) : '');
    };
    const contacts = {
        whatsapp: EVOLUA.whatsapp && { href: waLink('Olá! Vim pelo site da Evolua Tecnologia.'), text: EVOLUA.telefone || '+' + EVOLUA.whatsapp },
        email: EVOLUA.email && { href: 'mailto:' + EVOLUA.email, text: EVOLUA.email },
        instagram: EVOLUA.instagram && { href: 'https://instagram.com/' + EVOLUA.instagram, text: '@' + EVOLUA.instagram },
        cidade: EVOLUA.cidade && { href: '', text: EVOLUA.cidade },
        empresa: EVOLUA.empresa && { href: '', text: EVOLUA.empresa }
    };
    document.querySelectorAll('[data-contact]').forEach(function (el) {
        const c = contacts[el.getAttribute('data-contact')];
        if (!c) { el.hidden = true; return; }
        el.hidden = false;
        const label = el.querySelector('[data-contact-text]');
        if (label) label.textContent = c.text;
        if (el.tagName === 'A' && c.href) {
            el.href = c.href;
            if (!c.href.startsWith('mailto:')) { el.target = '_blank'; el.rel = 'noopener'; }
        }
    });
    document.querySelectorAll('[data-contact-empty]').forEach(function (el) {
        el.hidden = ['whatsapp', 'email', 'instagram', 'cidade'].some(function (k) { return contacts[k]; });
    });
    const waFloat = document.querySelector('.wa-float');
    if (waFloat && EVOLUA.whatsapp) {
        waFloat.href = waLink('Olá! Vim pelo site da Evolua Tecnologia.');
        waFloat.hidden = false;
    }

    /* Formulários: enviam para o painel (EVOLUA.mensagens); sem endereço ou se falhar, abrem o WhatsApp com a mensagem pronta */
    const openWhatsApp = function (form) {
        const lines = [form.getAttribute('data-send')];
        form.querySelectorAll('[name]').forEach(function (f) {
            const v = (f.value || '').trim();
            if (v && f.name !== 'site') lines.push((f.getAttribute('data-label') || f.name) + ': ' + v);
        });
        const msg = lines.join('\n');
        if (EVOLUA.whatsapp) {
            window.open(waLink(msg), '_blank', 'noopener');
        } else if (EVOLUA.email) {
            window.location.href = 'mailto:' + EVOLUA.email + '?subject=' + encodeURIComponent(lines[0]) + '&body=' + encodeURIComponent(msg);
        }
    };
    document.querySelectorAll('form[data-send]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            if (!EVOLUA.mensagens) { openWhatsApp(form); return; }
            const btn = form.querySelector('button[type=submit]');
            const data = new FormData(form);
            if (!data.get('assunto')) data.set('assunto', form.getAttribute('data-send'));
            data.set('origem', location.pathname.split('/').pop() || 'index.html');
            if (btn) { btn.disabled = true; btn.dataset.text = btn.innerHTML; btn.textContent = 'Enviando...'; }
            fetch(EVOLUA.mensagens, { method: 'POST', body: data })
                .then(function (r) { return r.json(); })
                .then(function (r) {
                    if (!r.ok) throw new Error(r.error || 'erro');
                    form.innerHTML = '<div class="form-done"><b>Mensagem enviada!</b><p>Obrigado pelo contato. A nossa equipe vai responder em breve.</p></div>';
                })
                .catch(function () {
                    if (btn) { btn.disabled = false; btn.innerHTML = btn.dataset.text; }
                    openWhatsApp(form);
                });
        });
    });

    /* Animação ao rolar */
    const items = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
            });
        }, { threshold: 0.12 });
        items.forEach(function (el) { io.observe(el); });
    } else {
        items.forEach(function (el) { el.classList.add('in'); });
    }
})();
