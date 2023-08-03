money = 30
item = {'anggur':3,'pepaya':2,'durian':10}

for items in item:
    print('-'*40)
    print("Hallo selamat belanja di toko kami")
    print('-'*40)
    print(f"Anda memiliki {str(money)} dolar di dompet anda")

    print(f"Harga setiap {items} adalah {item[items]} dolar")
    print('-'*40)

    input_count = int(input(f"Mau beli barapa {items} ?: "))
    print(f"Anda akan membeli {items} sebanyak {str(input_count)}")

    total_price = item[items] * input_count
    print(f"Total harga = {str(total_price)}")
    if money >= total_price:
        money -= total_price
        print(f"Sisa Uang anda: {str(money)}")
        if money == 0:
            break
    else:
        print("uang anda tidak cukup")
        break

    incontinue = input("Apakah anda ingin lanjut berbelanja atau tidak? (y/n)").lower()
    if incontinue == 'n':
        break
