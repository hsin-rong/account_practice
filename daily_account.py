#讀取檔案

#寫入檔案
with open('daily_account.csv','w') as f :
    product =[]
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入價格:')
        product.append([name,price])
    print(product)#輸出資料

