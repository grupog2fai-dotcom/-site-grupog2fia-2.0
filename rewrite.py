import os

filepath = r"C:\Users\HP\.gemini\antigravity\scratch\g2f-institutional-app\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. SEO
content = content.replace(
    "<title>Grupo G2F AI - Para quem quer mais</title>",
    """<title>Grupo G2F AI - Para quem quer mais</title>
    <meta name="description" content="Grupo G2F AI: Inteligência artificial, automação e engenharia de crescimento para PMEs. Pare de perder clientes no Google e WhatsApp. Resultado em 30 dias com garantia contratual.">
    <meta property="og:title" content="Grupo G2F AI - Para quem quer mais">
    <meta property="og:description" content="Grupo G2F AI: Inteligência artificial, automação e engenharia de crescimento para PMEs. Pare de perder clientes no Google e WhatsApp. Resultado em 30 dias com garantia contratual.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://127.0.0.1:3000/">
    <meta property="og:image" content="http://127.0.0.1:3000/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="http://127.0.0.1:3000/">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "Grupo G2F AI",
      "url": "http://127.0.0.1:3000/",
      "logo": "http://127.0.0.1:3000/logo.png",
      "description": "Inteligência artificial, automação e engenharia de crescimento para PMEs.",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Belo Horizonte",
        "addressRegion": "MG",
        "addressCountry": "BR"
      }
    }
    </script>"""
)

# 2. Focus Accessibility
content = content.replace(
    "box-sizing: border-box;\n        }",
    "box-sizing: border-box;\n        }\n\n        *:focus-visible {\n            outline: 2px solid var(--color-gold);\n            outline-offset: 2px;\n        }"
)

# 3. Will change
content = content.replace(
    "        .mobile-drawer {\n            position: fixed;",
    "        .mobile-drawer {\n            will-change: transform;\n            position: fixed;"
)
content = content.replace(
    "        .carousel-track {\n            display: flex;",
    "        .carousel-track {\n            display: flex;\n            will-change: transform;"
)
content = content.replace(
    "        .modal-content {\n            background-color: var(--color-surface-container);",
    "        .modal-content {\n            will-change: transform;\n            background-color: var(--color-surface-container);"
)

# 4. Hero Badge CSS
old_badge = """        .hero-tag {
            display: inline-block;
            padding: 6px 12px;
            background-color: var(--color-gold-hairline);
            border: 1px solid var(--color-gold);
            color: var(--color-gold);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 1px;
            border-radius: 100px;
            margin-bottom: 24px;
        }"""
new_badge = """        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background-color: rgba(201, 162, 39, 0.1);
            border: 1px solid rgba(201, 162, 39, 0.2);
            color: var(--color-gold);
            font-size: 0.875rem;
            font-weight: 600;
            border-radius: 100px;
            margin-bottom: 32px;
            backdrop-filter: blur(4px);
        }
        .hero-badge-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 20px;
            height: 20px;
            background-color: var(--color-gold);
            color: var(--color-surface);
            border-radius: 50%;
            font-size: 14px;
        }"""
content = content.replace(old_badge, new_badge)

# 5. Pillar number CSS -> icon
old_pillar_num = """        .pillar-number {
            width: 48px;
            height: 48px;
            border-radius: 8px;
            background-color: var(--color-surface-container-high);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-heading);
            color: var(--color-gold);
            font-size: 1.5rem;
            font-weight: 700;
        }"""
new_pillar_icon = """        .pillar-icon {
            width: 48px;
            height: 48px;
            border-radius: 8px;
            background-color: var(--color-surface-container-high);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--color-gold);
        }
        .pillar-icon .material-symbols-outlined {
            font-size: 28px;
        }"""
content = content.replace(old_pillar_num, new_pillar_icon)

# 6. Mobile menu display flex
content = content.replace(
    "            .mobile-menu-btn {\n                display: block;\n            }",
    "            .mobile-menu-btn {\n                display: flex;\n            }"
)

# 7. ARIA Labels
content = content.replace(
    '<button class="mobile-menu-btn material-symbols-outlined">menu</button>',
    '<button class="mobile-menu-btn material-symbols-outlined" aria-label="Abrir menu">menu</button>'
)
content = content.replace(
    '<button class="close-drawer material-symbols-outlined">close</button>',
    '<button class="close-drawer material-symbols-outlined" aria-label="Fechar menu">close</button>'
)
content = content.replace(
    '<button class="carousel-btn" id="carousel-prev"><span class="material-symbols-outlined">chevron_left</span></button>',
    '<button class="carousel-btn" id="carousel-prev" aria-label="Anterior"><span class="material-symbols-outlined">chevron_left</span></button>'
)
content = content.replace(
    '<button class="carousel-btn" id="carousel-next"><span class="material-symbols-outlined">chevron_right</span></button>',
    '<button class="carousel-btn" id="carousel-next" aria-label="Próximo"><span class="material-symbols-outlined">chevron_right</span></button>'
)
content = content.replace(
    '<button class="modal-close material-symbols-outlined" id="close-quiz">close</button>',
    '<button class="modal-close material-symbols-outlined" id="close-quiz" aria-label="Fechar modal">close</button>'
)
content = content.replace(
    '<a href="https://wa.me/5531990000000" target="_blank" class="whatsapp-float">',
    '<a href="https://wa.me/5531990000000" target="_blank" class="whatsapp-float" aria-label="Falar no WhatsApp">'
)

# 8. Hero Content
old_hero = """            <span class="hero-tag">PARA QUEM QUER MAIS CRESCIMENTO, MÉTRICAS E LUCRO</span>
            <h1 class="hero-title">Existe um G2F AI para cada fase da sua empresa</h1>
            <p class="hero-subtitle">Inteligência artificial, automação e engenharia de crescimento para PMEs que querem escalar com método, resultado em 30 dias e garantia contratual.</p>"""
new_hero = """            <div class="hero-badge">
                <span class="hero-badge-icon material-symbols-outlined">bolt</span>
                Engenharia de Crescimento para PMEs
            </div>
            <h1 class="hero-title">Sua empresa está perdendo clientes todos os dias para concorrentes mais visíveis</h1>
            <p class="hero-subtitle">Enquanto sua equipe demora para responder no WhatsApp ou seu negócio não aparece no Top 3 do Google Maps, <strong>o dinheiro fica na mesa</strong>. O Grupo G2F AI instala inteligência artificial e engenharia de vendas na sua PME com resultado garantido em <strong>30 dias ou 100% do seu dinheiro de volta</strong>.</p>"""
content = content.replace(old_hero, new_hero)

# 9. Pillars HTML
old_pillars = """                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-number">1</div>
                        <h3 class="pillar-title">LEARNING</h3>
                    </div>
                    <p class="pillar-desc"><strong>G2F Academy:</strong> Cursos, imersões e formações práticas em IA e growth para empresários que querem dominar as ferramentas que geram receita.</p>
                </div>
                
                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-number">2</div>
                        <h3 class="pillar-title">SCALE</h3>
                    </div>
                    <p class="pillar-desc"><strong>Tração Rápida:</strong> G2F SEO Local coloca seu negócio no Top 3 do Google Maps. G2F Launch entrega landing page + tráfego pago em 15 dias. Resultado em 30 dias ou dinheiro de volta.</p>
                </div>

                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-number">3</div>
                        <h3 class="pillar-title">CLUB</h3>
                    </div>
                    <p class="pillar-desc"><strong>Partner Program:</strong> Rede de parceiros licenciados G2F com 20% de comissão recorrente. Comunidade, suporte e uma nova direção para o seu negócio.</p>
                </div>

                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-number">4</div>
                        <h3 class="pillar-title">TOOLS</h3>
                    </div>
                    <p class="pillar-desc"><strong>Tecnologia & IA:</strong> G2F Business OS unifica MRR, Churn, CAC e LTV em um dashboard. Agentes de WhatsApp IA atendem seus clientes 24/7 sem perder nenhuma venda.</p>
                </div>"""
new_pillars = """                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-icon">
                            <span class="material-symbols-outlined">school</span>
                        </div>
                        <h3 class="pillar-title">LEARNING</h3>
                    </div>
                    <p class="pillar-desc"><strong>G2F Academy:</strong> Cursos, imersões e formações práticas em <strong>IA e growth</strong> para empresários que querem dominar as ferramentas que <strong>geram receita</strong>.</p>
                </div>
                
                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-icon">
                            <span class="material-symbols-outlined">trending_up</span>
                        </div>
                        <h3 class="pillar-title">SCALE</h3>
                    </div>
                    <p class="pillar-desc"><strong>Tração Rápida:</strong> G2F SEO Local coloca seu negócio no <strong>Top 3 do Google Maps</strong>. G2F Launch entrega landing page + tráfego pago em <strong>15 dias</strong>. Resultado em <strong>30 dias ou dinheiro de volta</strong>.</p>
                </div>

                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-icon">
                            <span class="material-symbols-outlined">groups</span>
                        </div>
                        <h3 class="pillar-title">CLUB</h3>
                    </div>
                    <p class="pillar-desc"><strong>Partner Program:</strong> Rede de parceiros licenciados G2F com <strong>20% de comissão recorrente</strong>. Comunidade, suporte e uma <strong>nova direção</strong> para o seu negócio.</p>
                </div>

                <div class="pillar-card">
                    <div class="pillar-header">
                        <div class="pillar-icon">
                            <span class="material-symbols-outlined">build</span>
                        </div>
                        <h3 class="pillar-title">TOOLS</h3>
                    </div>
                    <p class="pillar-desc"><strong>Tecnologia & IA:</strong> G2F Business OS unifica <strong>MRR, Churn, CAC e LTV</strong> em um dashboard. Agentes de WhatsApp IA atendem seus clientes <strong>24/7 sem perder nenhuma venda</strong>.</p>
                </div>"""
content = content.replace(old_pillars, new_pillars)

# 10. Price Anchoring
old_price_1 = '<div class="program-price">R$ 357 Pix</div>'
new_price_1 = '<div class="program-price">\n                            <div style="font-size: 0.875rem; color: var(--color-on-surface-variant); font-weight: normal;">De <del>R$ 1.500/mês</del></div>\n                            por apenas R$ 357 Pix <span style="font-size: 0.875rem; font-weight: normal;">(Pagamento Único)</span>\n                        </div>'
content = content.replace(old_price_1, new_price_1)

old_price_2 = '<div class="program-price">R$ 1.347 Pix</div>'
new_price_2 = '<div class="program-price">\n                            <div style="font-size: 0.875rem; color: var(--color-on-surface-variant); font-weight: normal;">Substitua até 3 atendentes (R$ 4.500/mês)</div>\n                            por apenas R$ 1.347 Pix <span style="font-size: 0.875rem; font-weight: normal;">(Sem mensalidade de setup)</span>\n                        </div>'
content = content.replace(old_price_2, new_price_2)

old_price_3 = '<div class="program-price">R$ 2.247 Pix</div>'
new_price_3 = '<div class="program-price">\n                            <div style="font-size: 0.875rem; color: var(--color-on-surface-variant); font-weight: normal;">Consultorias cobram R$ 8.000</div>\n                            entregamos LP + Tráfego por R$ 2.247 Pix\n                        </div>'
content = content.replace(old_price_3, new_price_3)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
