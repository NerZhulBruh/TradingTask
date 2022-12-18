import os


def read_task_io_file():
	input_data = []
	with open("task.io", 'r', encoding='utf-8') as f:
		for line in f:
			if line == '\n':
				continue
			input_data.append(line.replace('\n', ''))
		i = 6
		flag = True  
		while i < len(input_data):
			if '-----' in input_data[i]:
				i += 7
				continue
			else:
				flag = False
				return "Ошибка. Некорректно указаны разделители"


	return_list = []
	temp_list = []
	flag_name = False
	for element in input_data:
		if 'BANK' in element:
			temp_list.append(float(element.split(':')[1].replace(' ', '')))
			flag_name = True
			continue
		elif flag_name is True:
			temp_list.append(element)
			flag_name = False
			continue
		elif 'Вход' in element:
			temp_list.append(float(element.split(':')[1].replace(' ', '')))
			continue
		elif 'Таргет' in element:
			targets = element.split(':')[1].replace(' ', '').split(';')
			temp_target_list = []
			for target in targets:
				temp_target_list.append(float(target))
			temp_list.append(temp_target_list)
			continue
		elif 'Выход' in element:
			temp_list.append(float(element.split(':')[1].replace(' ', '')))
			continue
		elif '-----' in element:
			return_list.append(temp_list)
			temp_list = []
			continue
	return return_list


def write_out_file(data):
	if not os.path.exists('out.txt'):
		with open('out.txt', 'w') as f:
			for el in data:
				f.write(el)
				f.write('\n')
	else:
		with open('out.txt', 'a') as f:
			for el in data:
				f.write(el)
				f.write('\n')


