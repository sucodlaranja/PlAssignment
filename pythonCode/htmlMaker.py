import re 
from readFiles import read_emd
back = "<a href=\"../index.html\">back<a>"
min_year, max_year, dic_by_gender_year, dic_by_modality_year, dic_by_age_gender, dic_by_year_federated,apto_per,apto_per, dic_address = read_emd("../InputFiles/emd.csv")
def makeIndex():
    index = open("../htmlFiles/index.html",'w')

    print('''<!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h3 class="title">Trabalho super mega bem top </h3>
        <div class="index">
        <a href="Pages/a.html" class="alinea">(a) Datas extermas dos registos no dataset</a>
        <a href="Pages/b.html" class="alinea">(b) Distribuição por género em cada ano e no total</a>
        <a href="Pages/c.html" class="alinea">(c) Distribuição por modalidade em cada ano e no total</a>
        <a href="Pages/d.html" class="alinea">(d) Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)</a>
        <a href="Pages/e.html" class="alinea">(e) Distribuição por morada</a>
        <a href="Pages/f.html" class="alinea">(f) Distribuição por estatuto de federado em cada ano</a>
        <a href="Pages/g.html" class="alinea">(g) Percentagem de aptos e não aptos por ano.</a>
        </div>
    </body>
    <footer class="footer">
    <h2>Made by:</h2>
    <h3>&nbsp;&nbsp;João Martins a91669, Jorge Lima a93183</h3>
    <h3>&nbsp;&nbsp;<a href="">Relatorio aqui<a><h3>

    </footer>
        
    </html>''',file=index)

    index.close()


    
def makeA():
    a = open("../htmlFiles/Pages/a.html",'w')
    print('''
          %s
          <h1>Datas extermas dos registos no Dataset<h1>
          <h3>Data minima: %s<h3>
          <h3>Data maxima: %s<h3>
          '''% (back,min_year,max_year),file=a)
    a.close()

def makeB():
    b = open("../htmlFiles/Pages/b.html",'w')
    for ano in dic_by_gender_year.keys():
        anohtml = re.sub("(.)","<h1>\1:<h1>",ano)
        print("%s"% anohtml,file=b)
        for genero in dic_by_gender_year[ano].keys():
            for h in dic_by_gender_year[ano][genero]:
                print(h[0])
    
    
makeB()


