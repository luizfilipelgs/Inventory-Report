from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file_path):
        if not file_path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as xml_file:
            xml_reader = xml_file.read()
            xml_todict = xmltodict.parse(xml_reader)['dataset']['record']
        return xml_todict
