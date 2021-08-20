#讀取檔案
product = []

def read_file(file):
        with open(file,'r',encoding = 'utf-8')as f:
            print(f)
def user_input():
    while True:
        pro = input('請輸入商品:')
        if pro == 'q':
            break
        price = input('請輸入價格:')
        product.append([pro,price])
def print_product():
    print('新加入的商品:')
    for p in product:
        print(p)
def write_file(file):
    with open(file,'w',encoding = 'utf-8') as f:
        for p in product:
            f.write(p[0] + ',' + p[1] + '\n')

read_file('daily_account.csv')
user_input()
print_product()
write_file('daily_account.csv')