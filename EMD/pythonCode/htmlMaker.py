import re
from readFiles import read_emd
back = "<a href=\"../index.html\">back<a>"
min_year, max_year, dic_by_gender_year, dic_by_modality_year, dic_by_age_gender, dic_by_year_federated, apto_per, dic_address = read_emd(
    "../InputFiles/emd.csv")
def back(x):
    print("<a href=\"../index.html\">back<a>",file=x)

def makeIndex():
    index = open("../htmlFiles/index.html", 'w')

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
        
    </html>''', file=index)

    index.close()


def makeA():
    a = open("../htmlFiles/Pages/a.html", 'w')
    print('''
          %s
          <h1>Datas extermas dos registos no Dataset<h1>
          <h3>Data minima: %s<h3>
          <h3>Data maxima: %s<h3>
          ''' % (back, min_year, max_year), file=a)
    a.close()


def makeB():
    b = open("../htmlFiles/Pages/b.html", 'w')
    back(b)
    dic_by_gender_year_sorted = sorted(dic_by_gender_year.keys())
    for year in dic_by_gender_year_sorted:
        print(re.sub(r'(.+)', r'<h1>\1<h1>', year), file=b)
        for gender in dic_by_gender_year[year].keys():
            print(re.sub(r'(.+)', r'<h2>\1<h2>', gender), file=b)
            dic_ordened = sorted(
                dic_by_gender_year[year][gender], key=lambda x: x[0], reverse=False)
            for person in dic_ordened:
                print("<p> Nome: %s </p><p>Modalidade: %s</p><hr/>" %
                      (person[0], person[1]), file=b)
    b.close()


def makeC():
    c = open("../htmlFiles/Pages/c.html", 'w')
    back(c)
    dic_by_modality_year_sorted = sorted(dic_by_modality_year.keys())

    for year in dic_by_modality_year_sorted:
        print(re.sub(r'(.+)', r'<h1>\1<h1>', year), file=c)
        dic_modality_sorted = sorted(dic_by_modality_year[year])

        for modality in dic_modality_sorted:
            print(re.sub(r'(.+)', r'<h2>\1<h2>', modality), file=c)
            dic_ordened = sorted(
                dic_by_modality_year[year][modality], key=lambda x: x[0], reverse=False)

            for person in dic_ordened:
                print("<p> Nome: %s </p><p>Modalidade: %s</p><hr/>" %
                      (person[0], person[1]), file=c)
    c.close()


def makeD():
    d = open("../htmlFiles/Pages/d.html", 'w')
    back(d)

    for age in dic_by_age_gender:
        print(re.sub(r'(.+)', r'<h1>\1<h1>', age), file=d)
        dic_by_age_sorted = sorted(dic_by_age_gender[age])

        for gender in dic_by_age_sorted:
            print(re.sub(r'(.+)', r'<h2>\1<h2>', gender), file=d)
            dic_ordened = sorted(
                dic_by_age_gender[age][gender], key=lambda x: x[0], reverse=False)

            for person in dic_ordened:
                print("<p> Nome: %s %s </p><p>Modalidade: %s</p><hr/>" %
                      (person[0], person[1], person[2]), file=d)
    d.close()


def makeE():
    e = open("../htmlFiles/Pages/e.html", 'w')
    back(e)
    adress_ordened = sorted(dic_address.keys(), reverse=False)
    for adress in adress_ordened:
        print(re.sub(r'(.+)', r'<h1>\1<h1>', adress), file=e)

        person_ordened = sorted(dic_address[adress], key=lambda x: x[0])
        for person in person_ordened:
            print("<p> Nome: %s %s </p><p>Modalidade: %s</p><hr/>" %
                  (person[0], person[1], person[2]), file=e)

    e.close()


def makeF():
    f = open("../htmlFiles/Pages/f.html", 'w')
    back(f)
    order_year = sorted(dic_by_year_federated.keys())
    for year in order_year:
        print(re.sub(r'(.+)', r'<h1>\1<h1>', year), file=f)
        for federated in dic_by_year_federated[year]:
            if(federated == 'true'):
                print("<h2>Federado<h2>", file=f)
            else:
                print("<h2>Não Federado<h2>", file=f)

            dic_ordened = sorted(
                dic_by_year_federated[year][federated], key=lambda x: x[0], reverse=False)
            for person in dic_ordened:
                print("<p> Nome: %s </p><p>Modalidade: %s</p><hr/>" %
                      (person[0], person[1]), file=f)
    f.close()


# TODO ta so a dar um valor
def makeG():
    
    g = open("../htmlFiles/Pages/g.html", 'w')
    back(g)
    
    order_years = sorted(apto_per)
    for year in order_years:
        print('''
            <h1>%s</h1>
            <h3>Percentagem de apto: %s<h3>
            <p> Percentagem não apta: %s <p>
            ''' % (year,apto_per[year][0],100-apto_per[year][0]), file=g)
        


makeB()
makeC()
makeD()
makeE()
makeF()
makeG()
makeIndex()
