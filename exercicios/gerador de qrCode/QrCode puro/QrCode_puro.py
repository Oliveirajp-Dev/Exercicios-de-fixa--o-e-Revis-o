import qrcode

imagem=qrcode.make(input('Cole sua URL aqui para gerar um QrCode: '))   # criando a variavel imagem para armazenar oo qrCode, usando o metodo "make" para passar o endereço "URL" que eu quero gerer o meu qrCode.

imagem.save("meuQrcode.png") #salvando o qrcode gerado