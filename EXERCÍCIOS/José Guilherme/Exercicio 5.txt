class Registro:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def __enter__(self):
        with open(self.caminho_arquivo, 'a') as f:
            f.write("Começo\n")
        return self

    def __exit__(self, tipo, valor, traceback):
        with open(self.caminho_arquivo, 'a') as f:
            f.write("Fim\n")
