import pytest
import usuario as usr

@pytest.mark.parametrize('entrada_usuario, usuario', [
  (usr.usuario('Dummy'), "Dummy")
])
def test_crear_usuario(entrada_usuario, usuario):
    assert entrada_usuario.usuario == usuario


@pytest.mark.parametrize('tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda', [
  ("credito", "Uno", 5, 2000)
])
def test_agregar_tarjeta(tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda):
    usuariotest = usr.usuario('Dummy')
    usuariotest.agregar_tarjeta(tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda)
    assert usuariotest.lista_tarjetas[0].tarjeta_servicio  == False
    assert usuariotest.lista_tarjetas[0].nombre_tarjeta == nombre_tarjeta
    assert usuariotest.lista_tarjetas[0].tasa_interes == tasa_interes
    assert usuariotest.lista_tarjetas[0].deuda == deuda

@pytest.mark.parametrize('tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda', [
  ("servicio", "Uno", 5, 2000)
])
def test_agregar_tarjeta_servicio(tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda):
    usuariotest = usr.usuario('Dummy')
    usuariotest.agregar_tarjeta(tipo_tarjeta, nombre_tarjeta, tasa_interes, deuda)
    assert usuariotest.lista_tarjetas[0].tarjeta_servicio  == True
    assert usuariotest.lista_tarjetas[0].nombre_tarjeta == nombre_tarjeta
    assert usuariotest.lista_tarjetas[0].tasa_interes == tasa_interes
    assert usuariotest.lista_tarjetas[0].deuda == deuda

def test_get_index_lista_tarjetas():
    usuariotest = usr.usuario('Dummy')
    usuariotest.agregar_tarjeta('credito','Uno', 5, 2000)
    usuariotest.agregar_tarjeta('credito','Dos', 5, 2000)
    usuariotest.agregar_tarjeta('credito','Tres', 5, 2000)
    assert usuariotest.get_index_lista_tarjetas("Uno") == 0
    assert usuariotest.get_index_lista_tarjetas("Dos") == 1
    assert usuariotest.get_index_lista_tarjetas("Tres") == 2

    assert usuariotest.get_index_lista_tarjetas("Cuatro") == -1

def test_eliminar_tarjeta_x_nombre():
    usuariotest = usr.usuario('Dummy')
    usuariotest.agregar_tarjeta('credito','Uno', 5, 2000)
    usuariotest.agregar_tarjeta('credito','Dos', 5, 2000)
    usuariotest.agregar_tarjeta('credito','Tres', 5, 2000)
    usuariotest.eliminar_tarjeta_x_nombre("Uno")

    assert usuariotest.get_index_lista_tarjetas("Uno") == -1