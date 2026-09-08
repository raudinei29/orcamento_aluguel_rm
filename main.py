"""
Orçamento de Aluguel - Imobiliária R.M
Trabalho de Algorithmic Thinking / Introduction to Object-Oriented Programming

Como executar:
    python main.py
"""

from imovel import Apartamento, Casa, Estudio
from orcamento import Orcamento


def ler_opcao(pergunta: str, opcoes: dict):
    """Lê uma opção numérica válida do usuário a partir de um dicionário {numero: texto}."""
    print(pergunta)
    for numero, texto in opcoes.items():
        print(f"  {numero} - {texto}")

    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha in opcoes:
            return escolha
        print("Opção inválida, tente novamente.")


def ler_sim_nao(pergunta: str) -> bool:
    while True:
        resposta = input(f"{pergunta} (S/N): ").strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print("Digite apenas S ou N.")


def ler_inteiro(pergunta: str, minimo: int, maximo: int) -> int:
    while True:
        try:
            valor = int(input(pergunta))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite um número válido.")


def montar_imovel():
    tipo = ler_opcao(
        "\nQual tipo de imóvel deseja alugar?",
        {"1": "Apartamento", "2": "Casa", "3": "Estúdio"},
    )

    if tipo == "1":
        quartos = ler_inteiro("Quantos quartos (1 ou 2)? ", 1, 2)
        vaga_garagem = ler_sim_nao("Deseja incluir vaga de garagem?")
        tem_criancas = ler_sim_nao("Possui crianças?")
        return Apartamento(quartos=quartos, vaga_garagem=vaga_garagem, tem_criancas=tem_criancas)

    if tipo == "2":
        quartos = ler_inteiro("Quantos quartos (1 ou 2)? ", 1, 2)
        vaga_garagem = ler_sim_nao("Deseja incluir vaga de garagem?")
        return Casa(quartos=quartos, vaga_garagem=vaga_garagem)

    # Estúdio
    quer_vaga = ler_sim_nao("Deseja incluir vagas de estacionamento?")
    vagas = 0
    if quer_vaga:
        vagas = ler_inteiro("Quantas vagas (mínimo 2)? ", 2, 10)
    return Estudio(vagas_estacionamento=vagas)


def main():
    print("=" * 55)
    print("   ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M")
    print("=" * 55)

    imovel = montar_imovel()
    parcelas_contrato = ler_inteiro(
        "\nEm quantas vezes deseja parcelar o contrato (1 a 5)? ", 1, 5
    )

    orcamento = Orcamento(imovel=imovel, parcelas_contrato=parcelas_contrato)

    print("\n" + orcamento.resumo())

    if ler_sim_nao("\nDeseja gerar o arquivo .csv com as 12 parcelas do orçamento?"):
        caminho = orcamento.gerar_csv("orcamento.csv")
        print(f"Arquivo gerado com sucesso: {caminho}")

    print("\nObrigado por usar o sistema da Imobiliária R.M!")


if __name__ == "__main__":
    main()
