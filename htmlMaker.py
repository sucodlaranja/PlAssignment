import re 

index = open("htmlFiles/index.html",'w')

print('''<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
    <h3 class="title">Trabalho super mega bem top </h3>
    <div class="index">
    <a href="teste.html" class="alinea">(a) Datas extermas dos registos no dataset</a>
    <a href="" class="alinea">(b) Distribuição por género em cada ano e no total</a>
    <a href="teste.html" class="alinea">(c) Distribuição por modalidade em cada ano e no total</a>
    <a href="" class="alinea">(d) Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)</a>
    <a href="teste.html" class="alinea">(e) Distribuição por morada</a>
    <a href="" class="alinea">(f) Distribuição por estatuto de federado em cada ano</a>
    <a href="" class="alinea">(g) Percentagem de aptos e não aptos por ano.</a>
    </div>
</body>
<footer class="footer">
<h2>Made by:</h2>
<h3>&nbsp;&nbsp;João Martins a91669, Jorge Lima a93183</h3>
<h3>&nbsp;&nbsp;<a href="">Relatorio aqui<a><h3>

</footer>
    
</html>''',file=index)

index.close()

