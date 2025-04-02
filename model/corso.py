from dataclasses import dataclass



@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    #studenti: list[Studente] = None  #lazy initialization
    #matricole: list[str] = None

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU - {self.pd} PERIODO"