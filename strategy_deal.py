
class StrategyDeal:
	def __init__(self, data):
		
		self.bank = data[0]
		self.name_stocks = data[1]
		self.price_input = data[2]
		self.targets = data[3]
		self.price_leave = data[4]

	def get_targets(self):
		return self.targets

	def get_target_percents(self):
		result_list = []
		for target in self.targets:
			result_list.append(round(((target - self.price_input) / self.price_input) * 100, 1)) 
		return result_list

	def target_banks(self):
		list_percents = self.get_target_percents()
		result_list = []
		for percent in list_percents:
			result_list.append(round(self.bank * (1 + percent/100), 1)) 
		return result_list

	def str(self):
		output_list = []
		
		output_list.append(f'BANK: {self.bank}')
		output_list.append(f'START_PRICE: {self.price_input}')
		output_list.append(f'STOP_PRICE: {self.price_leave}; {self.bank} - {self.price_leave} * {round(self.bank / self.price_input, 3)} = {round(self.bank - self.price_leave * (self.bank / self.price_input), 3)} FTT')
		output_list.append(f'PAIR: {self.name_stocks}')
		output_list.append('\n')

		
		all_stonks = self.bank / self.price_input
		part_stonks = all_stonks / len(self.targets)
		i = 1
		sum = 0
		for target in self.targets:
			output_list.append(f'{i} target: {target} FTT')
			percent = round((target - self.price_input) * 100 / self.price_input, 3)
			output_list.append(f'Percent: {percent}%')
			output_list.append(f'Bank: {round(self.bank * (1 + percent/100), 3)} FTT')
			output_list.append(f'Target size: {round(part_stonks, 3)} * {target} = {round(part_stonks*target, 3)} FTT')
			output_list.append('\n')
			sum += part_stonks*target
			i+=1

		output_list.append(f'Strategy income: {round(sum, 3)} - {self.bank} = {round(sum - self.bank, 3)}; percent: {round((sum - self.bank) * 100/self.bank, 3)}')
		output_list.append('----------')
		return output_list

