from datetime import date


class SimpleReport:
    @staticmethod
    def generate(data: list) -> list:
        nearest_data_val = SimpleReport.get_nearest_data_val(data)
        old_data_fab = SimpleReport.get_old_data_fab(data)
        company_more_product = SimpleReport.get_company_more_product(data)
        return (
            f'Data de fabricação mais antiga: {old_data_fab}\n'
            f'Data de validade mais próxima: {nearest_data_val}\n'
            f'Empresa com mais produtos: {company_more_product}'
        )

    def get_nearest_data_val(data: list) -> str:
        valid_dates = []
        for d in data:
            if date.fromisoformat(d["data_de_validade"]) > date.today():
                valid_dates.append(d["data_de_validade"])
        nearest_data = min(valid_dates) if valid_dates else None
        return nearest_data

    def get_old_data_fab(data: list) -> str:
        valid_dates = []
        for d in data:
            if date.fromisoformat(d["data_de_fabricacao"]) < date.today():
                valid_dates.append(d["data_de_fabricacao"])
        old_date = min(valid_dates) if valid_dates else None
        return old_date

    def get_company_more_product(data: list) -> str:
        companies = {}
        for company in data:
            if company['nome_da_empresa'] in companies:
                companies[company['nome_da_empresa']] += 1
            else:
                companies[company['nome_da_empresa']] = 1

        return max(companies, key=companies.get)
