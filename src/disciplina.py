class Disciplina:
    def __init__(self, id, titulo, data_inicio, data_termino, numero_vagas, verao):
        self.id = id
        self.titulo = titulo
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.numero_vagas = numero_vagas
        self.verao = verao

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,
            "numero_vagas": self.numero_vagas,
            "verao": self.verao
        }