class tarjeta():

    """
    Toma los valores iniciales para crear la tarjeta
    """
    def __init__(self, nombre, t_interes, deuda):
        self.nombre_tarjeta = nombre
        self.tasa_interes = t_interes
        self.deuda= deuda
        self.abono_a_realizar = 0
        self.tarjeta_servicio = False

    
    def abonar_tarjeta(self):

        abono= input("Ingrese el Abono a realizar: ")
        while int(abono) > self.deuda:
            print("Monto no valido. Ingrese de nuevo: ")
            abono= input()

        self.abono_a_realizar = int(abono)

    """
    Captura un nuevo cargo
    """
    def captura_nuevo_cargo (self):

        nuevo_cargo= int(input("Ingrese el monto del nuevo cargo: "))

        interes_mensual = self.tasa_interes/12
        deuda_recalculada = (self.deuda - self.abono_a_realizar)*(1+interes_mensual)
        self.deuda = deuda_recalculada + nuevo_cargo

        print("Deuda actualizada, usted debe: " + str(self.deuda))
        
    """
    Funcion que emula los pagos abonados a travez de los meses
    """
    def pago_recurrente (self):

        deuda_actual = self.deuda
        print("El abono actual ingresado es d: " + str(self.abono_a_realizar))
        print("Proyectando pagos...")
        num_pagos = 0
        while deuda_actual > 0:
            num_pagos+=1
            deuda_actual = deuda_actual - self.abono_a_realizar
            print("Pago {0}: Deuda total: {1}".format(num_pagos,deuda_actual))

        print("Su deuda quedaria saldada en {0} meses".format(num_pagos))

class tarjeta_de_servicios(tarjeta):
    def __init__(self, nombre, t_interes, deuda):
        super().__init__(nombre, t_interes, deuda)
        self.tarjeta_servicio = True

    def abonar_tarjeta(self):
        abono= input("Realiza el pago total de ${0} de su deuda: ".format(self.deuda))
        while int(abono) != self.deuda:
            print("Monto no valido. Ingrese de nuevo")
            abono= input()

        self.abono_a_realizar = int(abono)

    def pago_recurrente (self):

        deuda_actual = self.deuda
        print("El abono actual ingresado es de: " + str(self.abono_a_realizar))
        print("Proyectando pagos...")
        if deuda_actual == self.abono_a_realizar:
            deuda_actual = deuda_actual - self.abono_a_realizar
            print("Pago 1: Deuda total: {0}".format(deuda_actual))
            print("Por ser tajeta de servicio su deuda va a ser saldada en una exhibicion")
        else:
            print("El Abono a realizar debe ser la totalidad de la deuda. Reingrese su Abono")