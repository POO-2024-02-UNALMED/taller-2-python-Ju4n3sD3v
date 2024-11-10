class Auto:
    cantidadAutos = 0

    def __init__(self, modelo, precio, Asientos, marca, Motor, registro) -> None:
        self.modelo = modelo   
        self.precio = precio
        self.Asientos = Asientos
        self.marca = marca
        self.Motor = Motor
        self.registro = registro   

    def cantidadAsientos(self) -> int:
        for asiento in self.Asientos:
            if type(asiento) == None:
                self.Asientos.pop(asiento)
        nroAsientos = len(self.Asientos)
        return nroAsientos
    
    def verificarIntegridad(self) -> str:
        registros = set(self.registro, self.Motor.registro)
        for asiento in self.Asientos:
            registros.add(asiento.registro)

        if len(registros) > 1:
            return 'Las piezas no son originales'
        return 'Auto original'


class Motor:
    def __init__(self, numeroCilindros, tipo, registro) -> None:
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistros(self, nuevoRegistro: int):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo: str):
        if nuevoTipo.lower() in ['electrico', 'gasolina']:
            self.tipo = nuevoTipo


class Asiento:
    def __init__(self, color, precio, registro) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor: str) -> None:
        if nuevoColor.lower() in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
            self.color = nuevoColor

