# Matheus

Para buildar o pacote basta fazer o seguinte:

````shell
# Install
pip install pyinstaller

# Empacota
pyinstaller --onefile -w src/app.py
````

<br>


Inicialmente o arquivo *.exe* gerado era reconhecido como vírus.
Li a respeito, era necessário recompilar o _bootloader_ do _pyinstaller_ e depois _buildar_ o projeto novamente.

Fiz, utilizando o conceito do
_post_ [Program made with PyInstaller now seen as a Trojan Horse by AVG](https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg).

<br>

-----

## Referências

- https://www.tutorialspoint.com/converting-tkinter-program-to-exe-file