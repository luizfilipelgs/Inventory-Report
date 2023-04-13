from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data: list) -> str:
        companies = {}
        for company in data:
            if company['nome_da_empresa'] in companies:
                companies[company['nome_da_empresa']] += 1
            else:
                companies[company['nome_da_empresa']] = 1

        report = '\nProdutos estocados por empresa:\n'
        for company, quantity in companies.items():
            report += f'- {company}: {quantity}\n'

        return SimpleReport.generate(data) + report

