# Orçamento de Aluguel - Imobiliária R.M

Aplicação em Python (Orientação a Objetos) que gera o orçamento mensal de
aluguel de Apartamentos, Casas e Estúdios, incluindo o parcelamento do
contrato imobiliário e a exportação de um arquivo `.csv` com as 12 parcelas
do orçamento anual.

## Estrutura do projeto

```
orcamento_aluguel/
├── imovel.py       # Classes Imovel (abstrata), Apartamento, Casa, Estudio
├── orcamento.py     # Classe Orcamento (contrato, parcelamento, CSV)
├── main.py          # Interface de linha de comando (ponto de entrada)
└── README.md
```

## Conceitos de POO aplicados

- **Abstração**: `Imovel` é uma classe abstrata (ABC) que define o contrato
  que todo imóvel deve seguir.
- **Herança**: `Apartamento`, `Casa` e `Estudio` herdam de `Imovel`.
- **Polimorfismo**: cada subclasse implementa `calcular_valor_aluguel()` com
  sua própria regra de negócio.
- **Encapsulamento**: atributos internos protegidos (`_tipo`, `_valor_base`)
  acessados via `property`.

## Regras de negócio implementadas

- Apartamento: R$ 700 (1 quarto); +R$ 200 (2 quartos); +R$ 300 (garagem);
  -5% de desconto para quem não tem crianças.
- Casa: R$ 900 (1 quarto); +R$ 250 (2 quartos); +R$ 300 (garagem).
- Estúdio: R$ 1.200; +R$ 250 (2 vagas de estacionamento); +R$ 60 por vaga
  extra.
- Contrato imobiliário: R$ 2.000, parcelável em até 5x.
- Exportação de `.csv` com as 12 parcelas mensais do orçamento (aluguel +
  parcela do contrato nos meses correspondentes).

## Como executar

```bash
python main.py
```

Siga as perguntas no terminal para montar o orçamento. Ao final, é possível
gerar o arquivo `orcamento.csv` com as 12 parcelas.
