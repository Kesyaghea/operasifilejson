import json
import os

class JsonKu:
    def __init__(self, nama_file):
        self.nama_file = nama_file
    
    def baca(self):
        if os.path.exists(self.nama_file):
            with open(self.nama_file, 'r') as file:
                data = json.load(file)
                return data
        else:
            return {}

    def tulis(self, data):
        with open(self.nama_file, 'w') as file:
            json.dump(data, file, indent=5)
    
    def update(self, key, value):
        data = self.baca()
        data[key] = value
        self.tulis(data)
    
    def delete(self, key):
        data = self.baca()
        if key in data:
            del data[key]
            self.tulis(data)
        else:
            print(f"kata kunci '{key}' tidak di mengerti")

# Program utama 
if __name__ == "__main__":
    # menyimpan lokasi file 
    nama_file = 'data.json'
    json_ku = JsonKu(nama_file)
    # menulis data awal
    data_utama = {
        "Nama": "Keysa ghea",
        "umur": 17,
        "sekolah": "SMKN 9 MALANG",
        "Alamat": "prum puri bunga nirwana"
    }
    json_ku.tulis(data_utama)

    # untuk membaca dan menampilkan data
    print("Data After di tulis:")
    print(json_ku.baca())

    # update file
    json_ku.update("umur", 18)
    print("\nData After di update:")
    print(json_ku.baca())

    # delete 
    json_ku.delete("Alamat")
    print("\nData After di delete:")
    print(json_ku.baca())
