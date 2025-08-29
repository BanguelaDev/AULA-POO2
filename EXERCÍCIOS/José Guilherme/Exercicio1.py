class Livro:
    def __init__(self, titulo, estoque):
        self.titulo = titulo
        self._estoque = 0
        self.estoque = estoque  # usa o setter

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self._estoque = valor

    def __str__(self):
        return f"{self.titulo} - Estoque: {self.estoque}"