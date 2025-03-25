
#a partir def aca vamos a llamar la clase creando instancias


from clases.perro import PerroTeste


perro1=PerroTeste("Firulais", 3) #esta llamando por detras al contrusctor pasandole nombre y edad
perro2= PerroTeste("Luma", 10)
#--------------------------------- se termina el instanciamento
#--------------------------------- aqui vamos a imprimirlo

#aca estamos usando template strings con las variables propias de la instancia de una clase(objeto)
print(f"{perro1.nombre} tiene {perro1.edad} años y dice {perro1.ladra()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice {perro2.ladra()}")