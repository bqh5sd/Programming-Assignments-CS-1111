def mean_all(table):
	total = 0
	count = 0
	for column in table:
		for list_number in column:
			count += 1
			total += list_number
			print("count:" + str(count))
			print(total)
	return float(total/count)

def mean_by_row(table):
	row_total = 0
	row_count = len(table[0][:])
	row_mean_list = []
	for row_list in table:
		for list_number in row_list:
			row_total += list_number
		row_mean = float(row_total/row_count)
		row_mean_list += [row_mean]
		row_total = 0
	return row_mean_list

def mean_by_col(table):
	column_list_index = 0
	column_total = 0
	len_col = len(table)
	len_row = len(table[0][:])
	col_mean_list = []
	count = 0
	while count < len_col + 1:
		for list in table:
			count += 1
			column_total += list[column_list_index]
			if count == len_col:
				col_mean_list += [column_total/len_col]
				column_list_index += 1
				count = 0
				column_total = 0 
				if column_list_index == len_row - 0:
					return col_mean_list
		
		

		
		


