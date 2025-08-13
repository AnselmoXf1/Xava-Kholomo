from flask import Flask, render_template, request, redirect, url_for
import urllib.parse

app = Flask(__name__)

# Lista de produtos (simulando banco de dados)
# Atualizando a lista de produtos com links externos
produtos = [
    {
        "id": 1,
        "nome": "Curso de Front-end Básico",
        "categoria": "Front-end",
        "descricao": "Aprenda HTML, CSS e JavaScript do zero.",
        "preco": "MZN 150,00",
        "imagem": "https://via.placeholder.com/300x180?text=Curso+Front-end",
        "detalhes": "Neste curso, você aprenderá os fundamentos de desenvolvimento front-end com HTML5, CSS3 e JavaScript ES6. Ideal para iniciantes.",
        "bonus": "Acesso a comunidade exclusiva + Ebook complementar",
        "link_externo": "https://www.udemy.com/course/front-end-basico/"
    },
    {
        "id": 2,
        "nome": "Curso de Back-end com Node.js",
        "categoria": "Back-end",
        "descricao": "Desenvolva APIs robustas e escaláveis.",
        "preco": "MZN 150,00",
        "imagem": "https://via.placeholder.com/300x180?text=Curso+Back-end",
        "detalhes": "Aprenda a criar APIs com Node.js e Express, com foco em backend escalável.",
        "bonus": "Mentoria de 1 hora + Templates de código",
        "link_externo": "https://www.udemy.com/course/backend-nodejs/"
    },
    {
        "id": 3,
        "nome": "Ebook de Marketing Digital",
        "categoria": "Marketing",
        "descricao": "Estratégias para crescer seu negócio online.",
        "preco": "MZN 200,00",
        "imagem": "https://via.placeholder.com/300x180?text=Ebook+Marketing",
        "detalhes": "Guia completo com estratégias de marketing digital para Moçambique.",
        "bonus": "Checklist de campanhas + Templates",
        "link_externo": "https://www.coursera.org/learn/marketing-digital"
    },
    {
        "id": 4,
        "nome": "Curso de Design Gráfico",
        "categoria": "Design",
        "descricao": "Domine Photoshop e Illustrator.",
        "preco": "MZN 200,00",
        "imagem": "https://via.placeholder.com/300x180?text=Curso+Design",
        "detalhes": "Curso prático para criar designs incríveis com Adobe Photoshop e Illustrator.",
        "bonus": "Pacote de recursos gráficos",
        "link_externo": "https://www.udemy.com/course/design-grafico/"
    }
]


# Página inicial
@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

# Página de produto
@app.route('/product/<int:id>')
def product(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    return render_template('product.html', produto=produto)

# Página Sobre
@app.route('/about')
def about():
    return render_template('about.html')

# Página de Contato
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']
        mensagem_whatsapp = f"Olá, Anselmo! Sou {nome}, email: {email}. Mensagem: {mensagem}"
        encoded_message = urllib.parse.quote(mensagem_whatsapp)
        return redirect(f"https://wa.me/258845462448?text={encoded_message}")
    return render_template('contact.html')

# Página de Checkout (manual)
@app.route('/checkout/<int:id>', methods=['GET', 'POST'])
def checkout(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        whatsapp = request.form['whatsapp']
        mensagem = f"Olá, Anselmo! Quero comprar o {produto['nome']} por {produto['preco']}. Nome: {nome}, Email: {email}, WhatsApp: {whatsapp}"
        encoded_message = urllib.parse.quote(mensagem)
        return redirect(f"/confirmation?message={encoded_message}")
    return render_template('checkout.html', produto=produto)

# Página de Confirmação
@app.route('/confirmation')
def confirmation():
    mensagem = request.args.get('message', '')
    return render_template('confirmation.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)