def setor():   
    
    print("Olá!! Bem vindo(a) ao Super Mercado do Ximbica, está tudo bem? Espero que sim!, bem agora eu irei lhe mostrar nossos setores, por favor escolha o de sua preferência.")
    print("   ")
    print(" 1. Higiene e Beleza\n","2. Lipeza\n","3. Bebidas\n","4. Mercearia\n","5. Laticinios\n","6. Refrigerados\n","7. Horti-fruti\n","8. Padaria\n","9. Açougue")
    print("   ")
    setor = int(input("decidiu qual Setor irá visitar primeiro? se sim, digite seu numero aqui: "))

    return setor


def biblioteca(valor):    
    d = {}
    d[1] = "Papel Higiênico"
    d[2] = "Shampoo"
    d[3] = "Higiene Bocal"
    d[4] = "Maquiagens"
    d[5] = "Detergente"
    d[6] = "Desinfetante"
    d[7] = "Amaciante"
    d[8] = "Sabão em Pó"
    d[9] = "Cervejas"
    d[10] = "Refrigerantes"
    d[11] = "Vinhos"
    d[12] = "Sucos Naturais"
    d[13] = "Serrote"
    d[14] = "Furadeiras e Pregos"
    d[15] = "Serra Circular"
    d[16] = "Lixadeira"
    d[17] = "Leite"
    d[18] = "derivados de lactobacilos"
    d[19] = "Proteina"
    d[20] = "Grãos"
    d[21] = "Hamburguer"
    d[22] = "Comida Congelada"
    d[23] = "Nuggets"
    d[24] = "Massas Congeladas"
    d[25] = "Legumes"
    d[26] = "Verduras"
    d[27] = "Vegetais"
    d[28] = "Frutas"
    d[29] = "Pães"
    d[30] = "Doces"
    d[31] = "Frios"
    d[32] = "Bebidas Quentes"
    d[33] = "Carne de Boi"
    d[34] = "Carne de Porco"
    d[35] = "Carne pra Churrasco"
    d[36] = "Linguiça"

    return d[valor]




def produtos_1():    
    produtos_1 = (" 1. Papel Higiênico\n 2. Shampoo\n 3. Higiene Bocal\n 4. Maquiagens")
    return print(produtos_1)
def produtos_2():
    produtos_2 = (" 5. Detergente\n 6. Desinfetante\n 7. Amaciante\n 8. Sabão em pó")
    return print(produtos_2)
def produtos_3():
    produtos_3 = (" 9. Cervejas\n 10. Refrigerantes\n 11. Vinhos\n 12. Sucos Naturais")
    return print(produtos_3)

def produtos_4():
    produtos_4 = (" 13. Serrote\n 14. Furadeira e Pregos\n 15. Serra Circular\n 16. Lixadeira")
    return print(produtos_4)
def produtos_5():
    produtos_5 = (" 17. Leite\n 18. derivados de lactobacilos\n 19. Proteína\n 20. Grãos")
    return print(produtos_5)
def produtos_6():
    produtos_6 = (" 21. Hamburguer\n 22. Comida Congelada\n 23. Nuggets\n 24. Massas Congeladas")
    return print(produtos_6)
def produtos_7():
    produtos_7 = (" 25. Legumes\n 26. Verduras\n 27. Vegetais\n 28. Frutas")
    return print(produtos_7)
def produtos_8():
    produtos_8 = (" 29. Pães\n 30. Doces\n 31. Frios\n 32. Café")
    return print(produtos_8)
def produtos_9():
    produtos_9 = (" 33. Carne de Boi\n 34. Carne de Porco\n 35. Carne para Churrasco\n 36. Linguiça")
    return print(produtos_9)



def escolha_produto():
        
    numo = setor() 

    if numo == 1:
        print("certo agora iremos te mostrar os produtos do setor 1, por favor escolha o de seu agrado.")
        print(' ')
        produtos_1()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 2:
        print("certo agora iremos te mostrar os produtos do setor 2, por favor escolha o de seu agrado.")
        print(' ')
        produtos_2()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 3:
        print("certo agora iremos te mostrar os produtos do setor 3, por favor escolha o de seu agrado.")
        print(' ')
        produtos_3()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 4:
        print("certo agora iremos te mostrar os produtos do setor 4, por favor escolha o de seu agrado.")
        print(' ')
        produtos_4()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 5:
        print("certo agora iremos te mostrar os produtos do setor 5, por favor escolha o de seu agrado.")
        print(' ')
        produtos_5()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 6:
        print("certo agora iremos te mostrar os produtos do setor 6, por favor escolha o de seu agrado.")
        print(' ')
        produtos_6()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 7:
        print("certo agora iremos te mostrar os produtos do setor 7, por favor escolha o de seu agrado.")
        print(' ')
        produtos_7()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 8:
        print("certo agora iremos te mostrar os produtos do setor 8, por favor escolha o de seu agrado.")
        print(' ')
        produtos_8()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")

    if numo == 9:
        print("certo agora iremos te mostrar os produtos do setor 9, por favor escolha o de seu agrado.")
        print(' ')
        produtos_9()
        print(' ')
        num_produto = int(input("digite o código do seu produto: "))
        print(" ")
    
    return num_produto



def carrinho():
    prod = escolha_produto()
    carrinho_compras = []
    carrinho_compras.append(biblioteca(prod))

    mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
    print(" ")

    while mais_prod == 55:
        print(" ")
        prod = escolha_produto()
        carrinho_compras.append(biblioteca(prod))
        mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
        print(" ")
    
    else:
        print("Carrinhos:", carrinho_compras)
        confirmação = int(input(" o carrinho está correto ou gostaria de acrescentar algo?\n digite 00 para confirmar o carrinho digite 11 para acrescentar algo mais: "))
        print(" ")

        while confirmação == 11:
            prod = escolha_produto()
            carrinho_compras.append(biblioteca(prod))
            print(" ")
            mais_prod = int(input(" Deseja adicionar mais produtos para seu carrinho?\n digite 55 para sim,  digite 56 para não: "))
            print(" ")

            if mais_prod == 56:
                print("Carrinhos:", carrinho_compras)
                print("Obrigado pro vir ao mercado do Xinbica, Até Mais!!!")
                break
                

        if confirmação == 00:
            
            print("Obrigado pro vir ao mercado do Xinbica, Até Mais!!!")

    return carrinho_compras
            
        

def dicionario_coord(produto):
    tup = {}
    tup["Papel Higiênico"] = (0, 0)
    tup["Shampoo"] = (0, 1)
    tup["Higiene Bocal"] = (0, 2)
    tup["Maquiagens"] = (0, 3)
    tup["Detergente"] = (0, 4)
    tup["Desinfetante"] = (0, 5)
    tup["Amaciante"] = (0, 6)
    tup["Sabão em pó"] = (0, 7)
    tup["Cervejas"] = (0, 8)
    tup["Refrigerantes"] = (0, 9) 
    tup["Vinhos"] = (1, 0)
    tup["Sucos Naturais"] = (1, 1)
    tup["Serrote"] = (1, 2)
    tup["Furadeira e Pregos"] = (1, 3)
    tup["Serra Circular"] = (1, 4)
    tup["Lixadeira"] = (1, 5)
    tup["Leite"] = (1, 6)
    tup["derivados de lactobacilos"] = (1, 7)
    tup["Proteína"] = (1, 8)
    tup["Grãos"] = (1, 9)
    tup["Hamburguer"] = (2, 0)
    tup["Comida Congelada"] = (2, 7)
    tup["Nuggets"] = (2, 3)
    tup["Massas Congeladas"] = (2, 4)
    tup["Legumes"] = (2, 5)
    tup["Verduras"] = (2, 6)
    tup["Vegetais"] = (2, 7)
    tup["Frutas"] = (2, 8)
    tup["Pães"] = (2, 9) 
    tup["Doces"] = (3, 0)
    tup["Frios"] = (3, 1)
    tup["Café"] = (3, 2)
    tup["Carne de Boi"] = (3, 3)
    tup["Carne de Porco"] = (3, 4)
    tup["Carne para Churrasco"] = (3, 5)
    tup["Linguiça"] = (3, 6)
    
    return tup[produto]




def trans_prod_em_coord():
    prod_carrinho = carrinho()
    lista_coord_prod = []

    for i in range(len(prod_carrinho)):
        lista_coord_prod.append(dicionario_coord(prod_carrinho[i]))

    return sorted(lista_coord_prod)