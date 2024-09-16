class OpcaoInvalidaError(Exception):
    def __init__(self):
        self.message = f"Tecla inválida! Seu ponto vai para o adversário."
