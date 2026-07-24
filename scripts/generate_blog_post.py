import json
import os
import sys
import re
import datetime
import urllib.request
import argparse
import random

# Pre-set strategic topics
TOPICS = {
    "seo local": {
        "title": "Como colocar seu negócio no Top 3 do Google Maps em 30 dias",
        "slug": "seo-local-google-maps",
        "category": "Atração & SEO",
        "content": [
            "<h2>A invisibilidade custa muito caro</h2>",
            "<p>Se sua empresa não está no <strong>Top 3 do Google Maps</strong>, você está literalmente <strong>deixando dinheiro na mesa</strong> para o seu concorrente. A maioria das buscas locais resulta em visitas físicas ou ligações imediatas.</p>",
            "<h3>Por que o Google Meu Negócio não é suficiente?</h3>",
            "<p>Criar o perfil é apenas o começo. O algoritmo do Google prioriza negócios com <strong>avaliações consistentes</strong>, palavras-chave bem estruturadas e sinais de autoridade local. Se você apenas criou a ficha e a abandonou, o Google também abandonou você e seus clientes.</p>",
            "<h2>A Solução: Engenharia de Crescimento</h2>",
            "<p>Com o G2F SEO Local, aplicamos um método comprovado para otimizar sua presença digital. Nós construímos autoridade, respondemos às intenções de busca do seu cliente e transformamos seu perfil em uma máquina de captação de clientes que trabalha 24 horas por dia.</p>"
        ],
        "cta_title": "Domine as buscas locais na sua região",
        "cta_text": "Queremos colocar sua empresa no Top 3 do Google Maps. Se não entregarmos resultado em 30 dias, devolvemos 100% do seu dinheiro."
    },
    "whatsapp ai": {
        "title": "Agentes de WhatsApp IA: o futuro do atendimento comercial",
        "slug": "agente-whatsapp-ia",
        "category": "Automação & IA",
        "content": [
            "<h2>A demora na resposta é a morte da venda</h2>",
            "<p>Você investe rios de dinheiro em tráfego, o cliente chama no WhatsApp e a sua equipe demora 30 minutos para responder. O resultado? <strong>O cliente já comprou do concorrente.</strong> O consumidor moderno simplesmente não tem paciência para esperar.</p>",
            "<h3>Atendimento 24/7 com Personalização Absoluta</h3>",
            "<p>A Inteligência Artificial não serve para criar robôs engessados que irritam as pessoas. Os novos Agentes de WhatsApp da G2F AI são treinados com o script de vendas da sua empresa, compreendem áudios, respondem dúvidas complexas e <strong>qualificam leads automaticamente</strong>.</p>",
            "<h2>Escala infinita sem aumentar a folha de pagamento</h2>",
            "<p>Com um agente de IA, você atende centenas de clientes simultaneamente, mantendo o padrão de qualidade e direcionando os humanos apenas para o fechamento. É escala com lucro máximo e zero dor de cabeça.</p>"
        ],
        "cta_title": "Automatize seu WhatsApp hoje",
        "cta_text": "Implemente um Agente IA treinado no seu WhatsApp e pare definitivamente de perder vendas por demora no atendimento."
    },
    "growth metrics": {
        "title": "MRR, Churn, CAC e LTV: as 4 métricas vitais para PMEs",
        "slug": "metricas-mrr-cac-ltv",
        "category": "Gestão",
        "content": [
            "<h2>O perigo silencioso da gestão baseada em achismos</h2>",
            "<p>Muitos empresários tomam decisões com base no saldo bancário. Isso é o mesmo que dirigir a 120km/h com os olhos vendados. Se você não mede, você não gerencia. O <strong>crescimento sustentável</strong> exige números claros e precisos.</p>",
            "<h3>O quarteto da escalabilidade</h3>",
            "<p>Para escalar com segurança, você precisa saber quanto custa adquirir um cliente (<strong>CAC</strong>), quanto ele gasta com você ao longo do tempo (<strong>LTV</strong>), quanto de receita recorrente você tem (<strong>MRR</strong>) e quantos clientes estão indo embora (<strong>Churn</strong>).</p>",
            "<h2>Business OS: O seu centro de comando</h2>",
            "<p>Entender as métricas é o primeiro passo. Acompanhá-las em tempo real é o que separa as empresas que estagnam daquelas que dominam o mercado. Um painel centralizado elimina a confusão e te dá clareza absoluta para tomar decisões.</p>"
        ],
        "cta_title": "Assuma o controle total do seu negócio",
        "cta_text": "Conheça o G2F Business OS e tenha todas as métricas vitais da sua empresa em um único painel em tempo real."
    },
    "automation": {
        "title": "Como automatizar 80% da sua operação e focar no estratégico",
        "slug": "automacao-operacao",
        "category": "Automação & IA",
        "content": [
            "<h2>O maior gargalo do seu negócio é você</h2>",
            "<p>Se sua empresa depende de você para aprovar cada pequena etapa, preencher planilhas ou enviar propostas, <strong>você se tornou o maior obstáculo para o crescimento do seu próprio negócio</strong>. A operação diária está sugando sua energia estratégica.</p>",
            "<h3>A Nova Era da Produtividade Extrema</h3>",
            "<p>Ferramentas de automação e Inteligência Artificial permitem que tarefas repetitivas sejam executadas sem nenhuma intervenção humana. Integrações inteligentes entre CRM, e-mail, WhatsApp e financeiro criam um fluxo de trabalho contínuo e à prova de falhas.</p>",
            "<h2>Trabalhe NO negócio, não PARA o negócio</h2>",
            "<p>Delegar para a máquina as tarefas de baixo valor agregado permite que você foque em inovação, estratégia e relacionamento com grandes clientes. Isso não é futuro, isso é a engenharia de crescimento aplicada hoje.</p>"
        ],
        "cta_title": "Libere seu tempo e dobre seus lucros",
        "cta_text": "Agende uma consultoria gratuita e descubra exatamente como podemos automatizar seus processos para escalar suas vendas."
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Blog G2F AI</title>
    <meta name="description" content="{description}">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --color-surface: #080e18;
            --color-gold: #c9a227;
            --color-gold-hover: #e5b82e;
            --color-text: #e2e9f5;
            --color-text-muted: #bac6d9;
            --font-body: 'Manrope', sans-serif;
            --font-heading: 'Playfair Display', serif;
        }}
        body {{
            background-color: var(--color-surface);
            color: var(--color-text);
            font-family: var(--font-body);
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }}
        a {{ color: var(--color-gold); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        
        .header {{ border-bottom: 1px solid rgba(255,255,255,0.1); padding: 20px 0; }}
        .nav-container {{ max-width: 800px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; }}
        .nav-logo {{ font-family: var(--font-heading); font-size: 24px; font-weight: bold; color: var(--color-gold); }}
        
        .article-container {{ max-width: 800px; margin: 60px auto; padding: 0 24px; }}
        .article-category {{ color: var(--color-gold); font-weight: bold; text-transform: uppercase; font-size: 14px; letter-spacing: 1px; margin-bottom: 16px; display: block; }}
        .article-title {{ font-family: var(--font-heading); font-size: 42px; line-height: 1.2; margin: 0 0 24px 0; color: #fff; }}
        
        .author-box {{ display: flex; align-items: center; gap: 16px; padding: 24px 0; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 40px; }}
        .author-avatar {{ width: 50px; height: 50px; border-radius: 50%; background-color: var(--color-gold); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--color-surface); font-size: 20px; }}
        .author-info h4 {{ margin: 0 0 4px 0; color: #fff; }}
        .author-info p {{ margin: 0; font-size: 14px; color: var(--color-text-muted); }}
        
        .article-content h2 {{ font-family: var(--font-heading); font-size: 32px; color: #fff; margin-top: 48px; margin-bottom: 24px; }}
        .article-content h3 {{ font-family: var(--font-heading); font-size: 24px; color: #fff; margin-top: 36px; margin-bottom: 16px; }}
        .article-content p {{ margin-bottom: 24px; font-size: 18px; }}
        .article-content strong {{ color: #fff; }}
        
        .cta-box {{ background: linear-gradient(135deg, rgba(201,162,39,0.1) 0%, rgba(201,162,39,0.02) 100%); border: 1px solid var(--color-gold); border-radius: 12px; padding: 40px; text-align: center; margin-top: 60px; }}
        .cta-box h3 {{ font-family: var(--font-heading); font-size: 28px; color: var(--color-gold); margin: 0 0 16px 0; }}
        .cta-box p {{ font-size: 18px; margin-bottom: 32px; }}
        .btn-gold {{ display: inline-block; background-color: var(--color-gold); color: #000; font-weight: bold; padding: 16px 32px; border-radius: 4px; text-transform: uppercase; letter-spacing: 1px; transition: transform 0.2s; }}
        .btn-gold:hover {{ transform: translateY(-2px); text-decoration: none; }}
        
        .footer {{ padding: 40px 0; text-align: center; color: var(--color-text-muted); border-top: 1px solid rgba(255,255,255,0.1); margin-top: 80px; font-size: 14px; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="nav-container">
            <a href="../index.html" class="nav-logo">G2F <span style="font-style:italic">AI</span></a>
            <a href="../blog.html">Voltar para o Blog</a>
        </div>
    </header>

    <main class="article-container">
        <article>
            <span class="article-category">{category}</span>
            <h1 class="article-title">{title}</h1>
            
            <div class="author-box">
                <div class="author-avatar">GA</div>
                <div class="author-info">
                    <h4>Gabriel Alexandre</h4>
                    <p>Fundador & CEO do Grupo G2F AI • {date}</p>
                </div>
            </div>

            <div class="article-content">
                {content}
            </div>

            <div class="cta-box">
                <h3>{cta_title}</h3>
                <p>{cta_text}</p>
                <a href="../solucoes.html" class="btn-gold">Conhecer Soluções G2F AI</a>
            </div>
        </article>
    </main>

    <footer class="footer">
        <p>Grupo G2F AI LTDA © 2026. Todos os direitos reservados.</p>
    </footer>
</body>
</html>"""

BLOG_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog | Grupo G2F AI</title>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --color-surface: #080e18;
            --color-gold: #c9a227;
            --color-text: #e2e9f5;
            --font-body: 'Manrope', sans-serif;
            --font-heading: 'Playfair Display', serif;
        }}
        body {{
            background-color: var(--color-surface);
            color: var(--color-text);
            font-family: var(--font-body);
            margin: 0; padding: 0;
        }}
        .header {{ padding: 24px 48px; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; }}
        .header a {{ color: var(--color-text); text-decoration: none; }}
        .logo {{ font-family: var(--font-heading); color: var(--color-gold); font-size: 24px; font-weight: bold; }}
        
        .hero {{ text-align: center; padding: 80px 24px; }}
        .hero h1 {{ font-family: var(--font-heading); font-size: 48px; margin: 0 0 16px; }}
        .hero p {{ font-size: 18px; color: #bac6d9; max-width: 600px; margin: 0 auto; }}
        
        .blog-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 32px; max-width: 1200px; margin: 0 auto 80px; padding: 0 24px; }}
        
        .post-card {{ display: block; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 24px; text-decoration: none; color: inherit; transition: border-color 0.3s; background: rgba(255,255,255,0.02); }}
        .post-card:hover {{ border-color: var(--color-gold); }}
        .post-category {{ color: var(--color-gold); font-size: 12px; font-weight: bold; text-transform: uppercase; margin-bottom: 12px; display: block; }}
        .post-title {{ font-family: var(--font-heading); font-size: 22px; margin: 0 0 12px; line-height: 1.3; color: #fff; }}
        .post-date {{ font-size: 14px; color: #bac6d9; }}
        
        /* POSTS_GRID_START */
        /* POSTS_GRID_END */
    </style>
</head>
<body>
    <header class="header">
        <a href="index.html" class="logo">G2F <span style="font-style:italic">AI</span></a>
        <a href="index.html">Voltar para Início</a>
    </header>

    <div class="hero">
        <h1>Blog G2F AI</h1>
        <p>Estratégias avançadas de inteligência artificial, SEO e engenharia de vendas para dominar o seu mercado.</p>
    </div>

    <div class="blog-grid" id="blog-grid">
        <!-- POSTS_GRID_START -->
        <!-- POSTS_GRID_END -->
    </div>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(description="Auto-Blog Script for G2F AI")
    parser.add_argument("--topic", "--keyword", dest="topic", type=str, help="Topic or keyword to generate", default="")
    args = parser.parse_args()

    # Determine topic
    selected_topic_key = None
    if args.topic:
        search_key = args.topic.lower()
        for key in TOPICS.keys():
            if search_key in key or key in search_key:
                selected_topic_key = key
                break
    
    if not selected_topic_key:
        selected_topic_key = random.choice(list(TOPICS.keys()))
        print(f"\033[93m[INFO] No exact topic match. Auto-selected: {selected_topic_key}\033[0m")

    topic_data = TOPICS[selected_topic_key]
    
    # Setup directories
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    artigos_dir = os.path.join(base_dir, "artigos")
    os.makedirs(artigos_dir, exist_ok=True)
    
    # Prepare data
    today_str = datetime.datetime.now().strftime("%d de %B de %Y")
    
    # Replace months with Portuguese if needed, but keeping it simple
    months_pt = {
        "January": "Janeiro", "February": "Fevereiro", "March": "Março", "April": "Abril",
        "May": "Maio", "June": "Junho", "July": "Julho", "August": "Agosto",
        "September": "Setembro", "October": "Outubro", "November": "Novembro", "December": "Dezembro"
    }
    for eng, pt in months_pt.items():
        today_str = today_str.replace(eng, pt)
    
    html_content = HTML_TEMPLATE.format(
        title=topic_data["title"],
        description=re.sub('<[^<]+>', '', "".join(topic_data["content"][:2])), # strip html for meta desc
        category=topic_data["category"],
        date=today_str,
        content="\n".join(topic_data["content"]),
        cta_title=topic_data["cta_title"],
        cta_text=topic_data["cta_text"]
    )
    
    file_path = os.path.join(artigos_dir, f"{topic_data['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"\033[92m[SUCCESS] Published: artigos/{topic_data['slug']}.html\033[0m")
    
    # Update posts.json
    posts_json_path = os.path.join(base_dir, "posts.json")
    posts = []
    if os.path.exists(posts_json_path):
        with open(posts_json_path, "r", encoding="utf-8") as f:
            try:
                posts = json.load(f)
            except:
                pass
                
    new_post = {
        "title": topic_data["title"],
        "slug": topic_data["slug"],
        "category": topic_data["category"],
        "date": today_str
    }
    
    # Check if already exists
    if not any(p.get("slug") == topic_data["slug"] for p in posts):
        posts.insert(0, new_post)
        with open(posts_json_path, "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=4, ensure_ascii=False)
        print(f"\033[94m[INFO] Updated: posts.json\033[0m")
    
    # Update blog.html
    blog_html_path = os.path.join(base_dir, "blog.html")
    if not os.path.exists(blog_html_path):
        with open(blog_html_path, "w", encoding="utf-8") as f:
            f.write(BLOG_HTML_TEMPLATE)
            
    with open(blog_html_path, "r", encoding="utf-8") as f:
        blog_html = f.read()
        
    post_card_html = f'''
        <a href="artigos/{topic_data["slug"]}.html" class="post-card">
            <span class="post-category">{topic_data["category"]}</span>
            <h2 class="post-title">{topic_data["title"]}</h2>
            <span class="post-date">{today_str}</span>
        </a>'''
        
    if post_card_html not in blog_html:
        blog_html = blog_html.replace("<!-- POSTS_GRID_START -->", f"<!-- POSTS_GRID_START -->\\n{post_card_html}")
        with open(blog_html_path, "w", encoding="utf-8") as f:
            f.write(blog_html)
        print(f"\\033[94m[INFO] Injected new post card into blog.html\\033[0m")

if __name__ == "__main__":
    main()
