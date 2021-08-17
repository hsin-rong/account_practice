#讀取檔案

#寫入檔案
product =[]
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入價格:')
    product.append([name,price])
    #print(product)#輸出資料

with open('daily_account.csv','w') as f :
    for p in product:
        f.write(p[0] + ',' + p[1] + '\n')
    