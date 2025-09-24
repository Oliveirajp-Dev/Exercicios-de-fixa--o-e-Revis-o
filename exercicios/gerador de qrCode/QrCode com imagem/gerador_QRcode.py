import qrcode 
from qrcode.image.styledpil import StyledPilImage
from qrcode.constants import ERROR_CORRECT_H # importando a constante de correção de erro para o QR code, que faz com que o QR code funcione mesmo com uma imagem sobreposta


qr=qrcode.QRCode( # criando o objeto QRCode
    
    version=10, # tamanho do QR code 
    error_correction=ERROR_CORRECT_H,# <-- CORREÇÃO DE ERRO 
    box_size=8, # tamanho de cada quadradinho do QR code
    border=2, # tamanho da borda (mínimo 4
    
)
qr.add_data( "www.linkedin.com/in/joão-pedro-oliveiradev")
imagem=qr.make_image( # criando a imagem do QR code para salvar em um arquivo, com a imagem sobreposta
    image_factory=StyledPilImage,
    embeded_image_path="exercicios/gerador de qrCode/minha_imagem.png" # caminho da imagem que vai ser sobreposta no QR code
    
    
)

imagem.save("meu_QRcode_com_imagem.png")

