from inventory_report.inventory.product import Product


def test_cria_produto():
    product_test = Product(
        1,
        'perfume',
        'boticario',
        '12/04/23',
        '12/04/25',
        'COD123456',
        'Não ingerir')
    assert product_test.id == 1
    assert product_test.nome_do_produto == 'perfume'
    assert product_test.nome_da_empresa == 'boticario'
    assert product_test.data_de_fabricacao == '12/04/23'
    assert product_test.data_de_validade == '12/04/25'
    assert product_test.numero_de_serie == 'COD123456'
    assert product_test.instrucoes_de_armazenamento == 'Não ingerir'
