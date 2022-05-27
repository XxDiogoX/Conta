class ContaCorrente:
    def __init__(self, nome_titular,numero_agencia,numero_conta,saldo):
        self.__nome_titular = nome_titular;
        self.__numero_agencia = numero_agencia;
        self.__numero_conta = numero_conta;
        self.__saldo = saldo;
        self.__limite = 1000.0;
        
        
    @property
    def nome(self):
        return self.__nome_titular;
    
    
    @property
    def numero_agencia(self):
        return self.__numero_agencia;
    
    @property
    def numero_conta(self):
        return self.__numero_conta;
        
    @property
    def saldo(self):
        return self.__saldo;
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor;
        
        
    def consultar_saldo(self):
        saldo = self.saldo;
        print(f"Saldo: R$ {saldo:.2f}");
        
        
    def sacar(self,valor):
        if(valor <= self.saldo):
            valor_restante = self.saldo - valor;
            self.saldo = valor_restante;
            print(f"Saque de R$ {valor:.2f} realizado.\nSaldo Atual: R$ {self.saldo:.2f}");
        else:
            print("Não foi possível realizar o saque!\nSaldo insuficiente..");
            
    
    def depositar(self, valor):
        if(valor > 0):
            valor_atual = self.saldo + valor;
            self.saldo = valor_atual;
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Impossível de realizar a operação");
            
    def transferir(self,valor,destinario):
        if(valor <= self.saldo):
            valor_restante = self.saldo - valor;
            destinario.depositar(valor);
            self.saldo = valor_restante;
            print(f"Realizada a transferência de R$ {valor:.2f}.\nPara: {destinario.nome}\nAgência: {destinario.numero_agencia}\nNúmero da Conta: {destinario.numero_conta}.");
        else:
            print("Não foi possível realiza a operação!!");
    
    
            
            

            
        
        
        
         