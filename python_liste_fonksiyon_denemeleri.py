# Listeyi düzleştiren (flatten) ve iç içe geçmiş tüm elemanları tek bir listeye çeviren fonksiyon
def flatten_list(nested_list):
    result = []  # Düzleştirilmiş elemanları saklamak için boş bir liste oluşturuyoruz
    for item in nested_list:  # Liste elemanlarını sırayla geziyoruz
        if isinstance(item, list):  # Eğer eleman bir liste ise
            result.extend(flatten_list(item))  # Rekürsif olarak elemanı açıyoruz ve düzleştirilmiş listeye ekliyoruz
        else:
            result.append(item)  # Eğer eleman liste değilse, doğrudan listeye ekliyoruz
    return result  # Düzleştirilmiş listeyi döndürüyoruz

# Örnek kullanım
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print("Orjinal Hali-1 :", input_list)
print("Düzleştirilmiş Liste:", flatten_list(input_list))  
# Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]


# Listeyi ve içindeki elemanları tersine döndüren fonksiyon
def reverse_nested_list(nested_list):
    reversed_list = []  # Tersine çevrilecek listeyi saklamak için boş bir liste oluşturuyoruz
    for item in reversed(nested_list):  # Ana listeyi ters sırayla geziyoruz
        if isinstance(item, list):  # Eğer eleman bir liste ise
            reversed_list.append(reverse_nested_list(item))  # Rekürsif olarak elemanı tersine çeviriyoruz
        else:
            reversed_list.append(item)  # Eğer eleman liste değilse, doğrudan listeye ekliyoruz
    return reversed_list  # Tersine çevrilmiş listeyi döndürüyoruz

# Örnek kullanım
input_list_2 = [[1, 2], [3, 4], [5, 6, 7]]
print("Orjinal Hali-2 :", input_list_2)
print("Tersine Çevrilmiş Liste:", reverse_nested_list(input_list_2))  
# Çıktı: [[7, 6, 5], [4, 3], [2, 1]]