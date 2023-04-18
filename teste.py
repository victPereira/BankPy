from models.cliente import Cliente
from models.conta import Conta

victor = Cliente('Victor Pereira', 'victor@example.com', '123.456.789-00', '28/06/2000')
julia = Cliente('Julia Garcia', 'julia@example.com', '789.456.123-00', '20/03/2000')

contavictor = Conta(victor)
contajulia = Conta(julia)

#print(contajulia)
#print(contavictor)
