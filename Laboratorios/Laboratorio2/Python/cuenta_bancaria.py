class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.

    :param saldo: Saldo inicial de la cuenta.
    """

    def __init__(self, saldo=0):
        """
        Constructor de la clase CuentaBancaria.

        :param saldo: El saldo inicial de la cuenta. El valor por defecto es 0.
        """
        self.saldo = saldo

    def depositar(self, cantidad):
        """
        Deposita una cantidad de dinero en la cuenta.

        :param cantidad: La cantidad a depositar.
        :raise ValueError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        self.saldo += cantidad

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta.

        :param cantidad: La cantidad a retirar.
        :raise ValueError: Si la cantidad es negativa o el saldo es insuficiente.
        """
        if cantidad < 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def consultar_saldo(self):
        """
        Consulta el saldo de la cuenta.

        :return: El saldo actual de la cuenta.
        """
        return self.saldo


# Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    print(f"Saldo actual: {cuenta.consultar_saldo()}")  # Imprime 1300s