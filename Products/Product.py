from collections import namedtuple

class Product(namedtuple('Product', "prodid name category price") ):
    _lastid = 0

    def __new__(cls, name, category, price):
        cls._lastid += 1
        return super(Product, cls).__new__(cls, cls._lastid, name, category, price)

    def toDict(self):
        return {'productName': self.name,
                'productPrice': self.price,
                'productCategory': self.category}


nbPear   = Product(u'Notebook Pear', u'Informatica', 3500)
nbHal    = Product(u'Notebook HAL', u'Informatica', 2500)
youPhone = Product(u'Celular Pear youPhone', u'Telefonia', 1800)
robot    = Product(u'Celular Blue Robot', u'Telefonia', 1600)
youClone = Product(u'Celular youClone com 8 chips', u'Telefonia', 500)
busPhone = Product(u'Celular ScritorioPhone for Business', u'Telefonia', 1200)
mike     = Product(u'Tenis Mike', u'Roupas e Acessorios', 300)
rei      = Product(u'Tenis Rei', u'Roupas e Acessorios', 150)
earphone = Product(u'Earphone youPhone original', u'Acessorios de Informatica', 90)
mouseChp = Product(u'Mouse CheapJunk Systems', u'Acessorios de Informatica', 5)
mouseMH  = Product(u'Mouse MacroHard sem fio', u'Acessorios de Informatica', 90)
boyBand  = Product(u'CD "Live Acustico" de Boy Band', u'Musica', 25)
jazz     = Product(u'CD "Cool Jazz" de Km Davis', u'Musica', 25)
fraldas  = Product(u'Fraldas Pimpolho - 200 unidades', u'Bebe', 50)
carrinho = Product(u'Carrinho de Bebe Heracles', u'Bebe', 150)
cerveja  = Product(u'Cerveja Deva - 6 pack', u'Alimentos e Bebidas', 15)
vinho    = Product(u'Vinho Petit Chateau Verdot', u'Alimentos e Bebidas', 150)
godBatt  = Product(u'Jogo - God of Battle', u'Jogos', 50)
receitas = Product(u'Livro "Receitas para Solteiros"', u'Livros', 25)
godLivro = Product(u'Livro "God of Battle - Estrategias"',  u'Livros', 25)
livroPai = Product(u'Livro "Como Nao Matar o Seu Bebe: a Arte da Guerra para pais solteiros"', u"Livros", 25)
livroEsp = Product(u'Livro "Espeleologia Comparada: Introducao ao Calculo Multiplexado"', u'Livros', 50)
allProducts = [nbPear, nbHal, youPhone, robot, youClone, busPhone, mike, rei, earphone, mouseChp, mouseMH, boyBand, jazz, fraldas, carrinho, cerveja, vinho, godBatt, receitas, godLivro, livroPai, livroEsp]

