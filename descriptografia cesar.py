def criptografar( mensagem, rot):
    alf = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z" ]

    n = len(alf)
    mensagem.lower()

    cifra = " "


    for letra in mensagem:
        if letra in alf:
            indice = alf.index(letra)
            nova_letra = alf[(indice + rot)%n]
            cifra = cifra + nova_letra
        else:
            cifra += letra
    return cifra

def descriptografar( mensagem, rot):
    return criptografar( mensagem, - rot)


arquivo = open("arquivo.txt", "r", encoding="utf8")
conteudo = arquivo.read()
arquivo.close


rot = 13
cifra = criptografar(conteudo,rot)



arquivo = open("mensagem_cifrada.txt", "r")
conteudo = arquivo.read()
arquivo.close()

decifrada = descriptografar(conteudo, rot)

arquivo = open("mensagem_decifrada.txt", "w")
arquivo.write(decifrada)
arquivo.close()
print("mensagem decifrada com sucesso ")
