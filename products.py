import os # operating system  要查檔案 要先問過作業系統(政府)

def read_file(filename):
	products = [] #大清單 放在外面 不管有沒有檔案 都要產生空清單
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳到下一迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
		#s = line.strip().split(',')
	return products
		
# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ') #如果輸入q就不用再問價格
		price = int(price)
		#p = [] #小清單
		#p.append(name)
		#p.append(price)

		#p = [name, price]
		products.append([name, price])
	print(products)
	return products

#products[0][0] #products中的第0格中 的第0格 (2維)

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1]) #純粹印出 沒有改變東西 就不用回傳

#utf-8 解決中文變亂碼

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #寫到檔案內 不用回傳


def main(): #主程式
	filename = 'products.csv'
	if os.path.isfile(filename): #請問政府大人 是否有這個檔名
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

# refactor 重構

