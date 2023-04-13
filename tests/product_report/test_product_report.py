from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        10,
        'perfume',
        'boticario',
        '12/04/23',
        '12/04/25',
        'COD123456',
        'em temperatura ambiente',
    )

    representation = str(product.__repr__())

    assert representation == (
        "O produto perfume"
        " fabricado em 12/04/23"
        " por boticario com validade"
        " até 12/04/25"
        " precisa ser armazenado em temperatura ambiente."
    )
