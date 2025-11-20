import random

class Foo:
    def __init__(self, num:int):
        self.num = num
    def __str__(self):
        return f"{self.num}"
    def __repr__(self):
        return str(self)

lista_num = []
lista_obj = []

lista_num_cheio = [0, 1, 2, 3, 4, 5]
lista_obj_cheio = [Foo(1), Foo(2), Foo(3)]

print("tamanho das listas iniciais:")
print(len(lista_num_cheio))
print(len(lista_obj_cheio))

lista_num.append(10)
lista_obj_cheio.append(Foo(4))

print("após append:")
print(lista_num)
print(lista_obj_cheio)

lista_num_cheio.pop()
lista_obj_cheio.pop()

print("após pop:")
print(lista_num_cheio)
print(lista_obj_cheio)

lista_num_cheio.insert(0, -1)
lista_obj_cheio.insert(0, Foo(99))

print("após insert:")
print(lista_num_cheio)
print(lista_obj_cheio)

lista_num_cheio.remove(2)
lista_obj_cheio.remove(lista_obj_cheio[2])

print("após apagar:")
print(lista_num)
print(lista_obj)


arr_random = [random.randint(0, 50) for _ in range(6)]
print("array aleatório:")
print(arr_random)

arr_seq = list(range(10))
print("array em sequência:")
print(arr_seq)

print("acessando elementos:")
print("index 4:", arr_seq[4])
print("último:", arr_seq[-1])

print("array como string:")
print("-".join(map(str, arr_seq)))

print("array com pares")
pares = [x for x in arr_seq if x % 2 == 0]
quadrados = [x**2 for x in pares]

print("pares:", pares)
print("quadrados dos pares:", quadrados)

arr_seq.sort(reverse=True)
print("array em ordem decrescente:")
print(arr_seq)

num = 5 
print(f"buscando número {num}...")
if num in arr_seq:
    print(f"{num} foi encontrado.")
else:
    print(f"{num} não foi encontrado.")

def buscar_elemento(arr, valor):
    return f"{valor} está na lista." if valor in arr else f"{valor} não está na lista."

print(buscar_elemento(arr_seq, num))

arr_slice = list(range(20))
print("slice 5:15:2")
print(arr_slice[5:15:2])

lista_extendida = [1, 2, 3]
lista_extendida.extend([4, 5, 6])
print("após extend:")
print(lista_extendida)

nums = [10, 3, 6, 2, 8, 4]
print("Verificações:")
print("tem número par?:", any(n % 2 == 0 for n in nums))
print("todos são positivos?:", all(n > 0 for n in nums))

print("valores estatísticos:")
print("máx:", max(nums))
print("mín:", min(nums))
print("soma:", sum(nums))
print("ordenado:", sorted(nums))

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
