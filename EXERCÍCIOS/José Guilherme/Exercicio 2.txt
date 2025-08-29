class Relogio:
    def __init__(self, horas, minutos):
        self.horas = horas % 24
        self.minutos = minutos % 60

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
