class Auto:
    cantidadAutos = 0

    def __init__(self, modelo, precio, Asientos, marca, Motor, registro) -> None:
        self.modelo = modelo   
        self.precio = precio
        self.asientos = Asientos
        self.marca = marca
        self.motor = Motor
        self.registro = registro   

    def cantidadAsientos(self) -> int:
        nroAsientos = len(self.asientos) - self.asientos.count(None)

        return nroAsientos
    
    def verificarIntegridad(self) -> str:
        registros = {self.registro, self.motor.registro}
        for asiento in self.asientos:
            if asiento != None:
                registros.add(asiento.registro)

        if len(registros) > 1:
            return 'Las piezas no son originales'
        return 'Auto original'


class Motor:
    def __init__(self, numeroCilindros, tipo, registro) -> None:
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo.lower() in ['electrico', 'gasolina']:
            self.tipo = nuevoTipo


class Asiento:
    def __init__(self, color, precio, registro) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor) -> None:
        if nuevoColor.lower() in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
            self.color = nuevoColor

