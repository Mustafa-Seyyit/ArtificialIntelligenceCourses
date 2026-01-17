import product_file_operations as pfo

while True:
    print("\n1-Ürün ekle \n2-Ürünleri göster \n3-Ürün Sil \n4-Çıkış")
    choice = input("Seçim(1-4): ")

    if choice == "1":
        product = input("ürün adı giriniz.")
        pfo.save_product(product)
    elif choice == "2":
        pfo.show_products(pfo.read_products())
    elif choice == "3":
        prd = input("silmek istediğiniz ürünü belirtiniz.")
        pfo.delete_product(prd)
    elif choice == "4":
        print("programdan çıkılıyor.")
        break
    else:
        print("geçersiz giriş!")