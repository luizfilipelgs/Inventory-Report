from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():

    list_products = [
        {
            "id": "10",
            "nome_do_produto": "perfume",
            "nome_da_empresa": "boticario",
            "data_de_fabricacao": "2023-04-11",
            "data_de_validade": "2025-04-11",
            "numero_de_serie": "COD123456",
            "instrucoes_de_armazenamento": "em temperatura ambiente",
        },
        {
            "id": "11",
            "nome_do_produto": "sabonete",
            "nome_da_empresa": "boticario",
            "data_de_fabricacao": "2023-04-12",
            "data_de_validade": "2025-04-12",
            "numero_de_serie": "COD654321",
            "instrucoes_de_armazenamento": "em temperatura ambiente",
        },
    ]

    colored = ColoredReport(SimpleReport)
    result = colored.generate(list_products)

    assert result == (
        "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2023-04-11\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2025-04-11\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m \033[31mboticario\033[0m"
    )
