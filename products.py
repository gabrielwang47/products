# 讀取檔案
products = [] #大清單
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 跳到下一迴圈
		name, price = line.strip().split(',')
		products.append([name, price])
		
		#s = line.strip().split(',')
print(products)

# 讓使用者輸入
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

#products[0][0] #products中的第0格中 的第0格 (2維)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#utf-8 解決中文變亂碼

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')




