/* =========================================================
   EVOLUA TECNOLOGIA - CONFIGURAÇÃO DO SITE
   Preencha os contatos aqui. Campo vazio = não aparece no site.
========================================================= */
const EVOLUA = {
    whatsapp: '',        // só números, com DDI e DDD. Ex.: '5511999999999'
    telefone: '',        // como deve aparecer. Ex.: '(11) 99999-9999'
    email: '',           // Ex.: 'contato@evoluatecnologia.com.br'
    instagram: '',       // só o usuário, sem @. Ex.: 'evoluatecnologia'
    cidade: ''           // Ex.: 'São Paulo - SP'
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
        cidade: EVOLUA.cidade && { href: '', text: EVOLUA.cidade }
    };
    document.querySelectorAll('[data-contact]').forEach(function (el) {
        const c = contacts[el.getAttribute('data-contact')];
        if (!c) { el.hidden = true; return; }
        const label = el.querySelector('[data-contact-text]');
        if (label) label.textContent = c.text;
        if (el.tagName === 'A' && c.href) {
            el.href = c.href;
            if (!c.href.startsWith('mailto:')) { el.target = '_blank'; el.rel = 'noopener'; }
        }
    });
    document.querySelectorAll('[data-contact-empty]').forEach(function (el) {
        el.hidden = Object.values(contacts).some(Boolean);
    });
    const waFloat = document.querySelector('.wa-float');
    if (waFloat && EVOLUA.whatsapp) {
        waFloat.href = waLink('Olá! Vim pelo site da Evolua Tecnologia.');
        waFloat.hidden = false;
    }

    /* Formulários: montam a mensagem e abrem o WhatsApp (ou o e-mail) */
    document.querySelectorAll('form[data-send]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const lines = [form.getAttribute('data-send')];
            form.querySelectorAll('[name]').forEach(function (f) {
                const v = (f.value || '').trim();
                if (v) lines.push((f.getAttribute('data-label') || f.name) + ': ' + v);
            });
            const msg = lines.join('\n');
            if (EVOLUA.whatsapp) {
                window.open(waLink(msg), '_blank', 'noopener');
            } else if (EVOLUA.email) {
                window.location.href = 'mailto:' + EVOLUA.email + '?subject=' + encodeURIComponent(lines[0]) + '&body=' + encodeURIComponent(msg);
            } else {
                alert('Os contatos ainda estão sendo configurados. Tente novamente em breve.');
            }
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
