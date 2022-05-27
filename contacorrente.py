class ContaCorrente:
    def __init__(self, nome_titular,numero_agencia,numero_conta,saldo):
        self.__nome_titular = nome_titular;
        self.__numero_agencia = numero_agencia;
        self.__numero_conta = numero_conta;
        self.__saldo = saldo;
        self.__limite = 1000.0;
        
    @property
    def saldo(self):
        return self.__saldo;
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor;
         