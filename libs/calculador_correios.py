import requests
from xml.etree.ElementTree import fromstring

class ShippingOptions:

	def __init__(self):

		self.correios = requests.get('http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPreco?nCdEmpresa=&sDsSenha=&nCdServico=41106&sCepOrigem=97032120&sCepDestino=71939360&nVlPeso=1&nCdFormato=1&nVlComprimento=10&nVlAltura=10&nVlLargura=10&nVlDiametro=0&sCdMaoPropria=s&nVlValorDeclarado=0&sCdAvisoRecebimento=n')
		
	def get_shipping_info(self):

		self.correios = self.correios.content
		print(self.correios)
		tree = fromstring(self.correios)
		self.correios = self.parse_results(tree)

		return self.correios

	def parse_results(self, tree):
		results = []
		print(tree.tag)
		for servico in tree.findall('Servicos'):
			print(servico.attrib)
			#results.append({'codigo': tree.find('Codigo'),'valor': i.find('Valor').text,})
		return results
