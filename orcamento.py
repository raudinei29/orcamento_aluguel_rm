"""
Módulo responsável por gerar o Orçamento final:
- Junta o valor do aluguel (vindo do Imóvel) com o valor do contrato imobiliário.
- Permite parcelar o contrato em até 5 vezes.
- Gera um arquivo .csv com as 12 parcelas (meses) do orçamento anual.
"""

import csv
from imovel import Imovel


class Orcamento:

    VALOR_CONTRATO = 2000.00
    MAX_PARCELAS_CONTRATO = 5
    MESES_ANO = 12

    def __init__(self, imovel: Imovel, parcelas_contrato: int = 1):
        self.imovel = imovel

        if not (1 <= parcelas_contrato <= self.MAX_PARCELAS_CONTRATO):
            raise ValueError("O contrato só pode ser parcelado em até 5 vezes.")

        self.parcelas_contrato = parcelas_contrato

    @property
    def valor_aluguel_mensal(self) -> float:
        return self.imovel.calcular_valor_aluguel()

    @property
    def valor_parcela_contrato(self) -> float:
        return round(self.VALOR_CONTRATO / self.parcelas_contrato, 2)

    def resumo(self) -> str:
        linhas = [
            "===== ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M =====",
            f"Tipo de imóvel: {self.imovel.tipo}",
            f"Valor do aluguel mensal: R$ {self.valor_aluguel_mensal:.2f}",
            f"Valor do contrato: R$ {self.VALOR_CONTRATO:.2f} "
            f"em {self.parcelas_contrato}x de R$ {self.valor_parcela_contrato:.2f}",
        ]
        return "\n".join(linhas)

    def gerar_csv(self, caminho: str = "orcamento.csv") -> str:
        """
        Gera um .csv com as 12 parcelas (meses) do orçamento.
        Nos primeiros meses (conforme parcelas_contrato) soma-se também
        a parcela do contrato de locação.
        """
        with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(
                ["Mes", "Valor Aluguel (R$)", "Parcela Contrato (R$)", "Total do Mes (R$)"]
            )

            for mes in range(1, self.MESES_ANO + 1):
                parcela_contrato = (
                    self.valor_parcela_contrato if mes <= self.parcelas_contrato else 0.00
                )
                total_mes = self.valor_aluguel_mensal + parcela_contrato

                escritor.writerow(
                    [
                        mes,
                        f"{self.valor_aluguel_mensal:.2f}",
                        f"{parcela_contrato:.2f}",
                        f"{total_mes:.2f}",
                    ]
                )

        return caminho
