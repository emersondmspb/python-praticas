Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
10
10
type(10)
<class 'int'>
type("tudo")
<class 'str'>
5/2
2.5
type(5/2)
<class 'float'>
10/3
3.3333333333333335
10//3
3
>>> 10%3
1
>>> peso=78
>>> altura=1.83
>>> peso
78
>>> type(altura)
<class 'float'>
>>> altura
1.83
>>> imc=peso/(altura**2)
>>> imc
23.291229956104985
>>> imcinteiro=int(imc)
>>> imcinteiro
23
>>> texto="bom dia"
>>> texto
'bom dia'
>>> len(texto)
7
>>> len(imc)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(imc)
TypeError: object of type 'float' has no len()
>>> temp=str(texto)
>>> temp=str(imc)
>>> temp
'23.291229956104985'
>>> len(imc)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    len(imc)
TypeError: object of type 'float' has no len()
>>> len(temp)
18
>>> len(str(imc))
18
