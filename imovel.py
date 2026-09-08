"""
Módulo de classes de Imóveis.

Aplica os conceitos de Orientação a Objetos exigidos no desafio:
- Abstração (classe base Imovel)
- Herança (Apartamento, Casa e Estudio herdam de Imovel)
- Polimorfismo (cada classe implementa calcular_valor_aluguel() do seu jeito)
- Encapsulamento (atributos "privados" com _underscore e properties)
"""

from abc import ABC, abstractmethod


class Imovel(ABC):
    """Classe base abstrata para qualquer tipo de imóvel da imobiliária R.M."""

    def __init__(self, tipo: str, valor_base: float):
        self._tipo = tipo
        self._valor_base = valor_base

    @property
    def tipo(self) -> str:
        return self._tipo

    @abstractmethod
    def calcular_valor_aluguel(self) -> float:
        """Cada subclasse deve implementar sua própria regra de cálculo."""
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self._tipo} - Valor do aluguel: R$ {self.calcular_valor_aluguel():.2f}"


class Apartamento(Imovel):
    """
    Regras:
    - Valor base: R$ 700,00 (1 quarto)
    - 2 quartos: +R$ 200,00
    - Vaga de garagem: +R$ 300,00
    - Desconto de 5% para quem não possui crianças
    """

    VALOR_BASE = 700.00
    ACRESCIMO_2_QUARTOS = 200.00
    ACRESCIMO_GARAGEM = 300.00
    DESCONTO_SEM_CRIANCAS = 0.05

    def __init__(self, quartos: int = 1, vaga_garagem: bool = False, tem_criancas: bool = True):
        super().__init__(tipo="Apartamento", valor_base=self.VALOR_BASE)
        self.quartos = quartos
        self.vaga_garagem = vaga_garagem
        self.tem_criancas = tem_criancas

    def calcular_valor_aluguel(self) -> float:
        valor = self._valor_base

        if self.quartos == 2:
            valor += self.ACRESCIMO_2_QUARTOS

        if self.vaga_garagem:
            valor += self.ACRESCIMO_GARAGEM

        if not self.tem_criancas:
            valor -= valor * self.DESCONTO_SEM_CRIANCAS

        return round(valor, 2)


class Casa(Imovel):
    """
    Regras:
    - Valor base: R$ 900,00 (1 quarto)
    - 2 quartos: +R$ 250,00
    - Vaga de garagem: +R$ 300,00
    """

    VALOR_BASE = 900.00
    ACRESCIMO_2_QUARTOS = 250.00
    ACRESCIMO_GARAGEM = 300.00

    def __init__(self, quartos: int = 1, vaga_garagem: bool = False):
        super().__init__(tipo="Casa", valor_base=self.VALOR_BASE)
        self.quartos = quartos
        self.vaga_garagem = vaga_garagem

    def calcular_valor_aluguel(self) -> float:
        valor = self._valor_base

        if self.quartos == 2:
            valor += self.ACRESCIMO_2_QUARTOS

        if self.vaga_garagem:
            valor += self.ACRESCIMO_GARAGEM

        return round(valor, 2)


class Estudio(Imovel):
    """
    Regras:
    - Valor base: R$ 1.200,00
    - 2 vagas de estacionamento: +R$ 250,00
    - Cada vaga extra (acima de 2): +R$ 60,00
    """

    VALOR_BASE = 1200.00
    VALOR_2_VAGAS = 250.00
    VALOR_VAGA_EXTRA = 60.00

    def __init__(self, vagas_estacionamento: int = 0):
        super().__init__(tipo="Estúdio", valor_base=self.VALOR_BASE)
        self.vagas_estacionamento = vagas_estacionamento

    def calcular_valor_aluguel(self) -> float:
        valor = self._valor_base

        if self.vagas_estacionamento >= 2:
            vagas_extras = self.vagas_estacionamento - 2
            valor += self.VALOR_2_VAGAS + (vagas_extras * self.VALOR_VAGA_EXTRA)

        return round(valor, 2)
