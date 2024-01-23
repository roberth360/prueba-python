class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            raise ValueError("No se puede retirar más dinero del que hay en la cuenta")

    def consultar_saldo(self):
        return self.saldo
cuenta = CuentaBancaria("Roberth Atagón", 1000)

cuenta.depositar(500)
print(cuenta.consultar_saldo())

cuenta.retirar(300)
print(cuenta.consultar_saldo())
