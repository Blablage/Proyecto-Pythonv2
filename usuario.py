import tarjeta as tjt

class usuario():

    def __init__(self, nombre):
        self.usuario = nombre
        self.lista_tarjetas = []

    def agregar_tarjeta(self, tipo_tarjeta, nombre, t_interes, deuda):
        if tipo_tarjeta == "servicio":
            nueva_tarjeta = tjt.tarjeta_de_servicios(nombre, t_interes, deuda)
        else:
            nueva_tarjeta = tjt.tarjeta(nombre, t_interes, deuda)
        self.lista_tarjetas.append(nueva_tarjeta)

    def get_index_lista_tarjetas(self, nombre):
        busqueda_exitosa = False
        for obj in self.lista_tarjetas:
            if nombre == obj.nombre_tarjeta:
                print("Tarjeta {0} encontrada".format(nombre))
                return self.lista_tarjetas.index(obj)
        return -1

    def eliminar_tarjeta_x_nombre(self, nombre):
        eliminacion_exitosa = False
        tarjeta_index = self.get_index_lista_tarjetas(nombre)

        if tarjeta_index >= 0:
            self.lista_tarjetas.pop(tarjeta_index)
            eliminacion_exitosa = True
            print("Tarjeta {0} eliminida".format(nombre))

        if eliminacion_exitosa == False:
            print("Tarjeta no encontrada")

    """
    Imprime los valores de la tarjetas
    """
    def imprimir_reporte (tarj):
        print("Nombre: {0} Tasa_Interes: {1} Deuda Inicial: {2} Pagos a abonar: {3}".format(tarj.nombre_tarjeta,str(tarj.tasa_interes),str(tarj.deuda),str(tarj.abono_a_realizar)))

    """
    Imprime N reportes de tarjetas
    """
    def multiples_reportes(self):
        for obj in self.lista_tarjetas:
            usuario.imprimir_reporte(obj)