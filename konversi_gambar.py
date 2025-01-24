import os
from PIL import Image
import datetime

def convert_images(input_folder, output_folder):
    """Mengubah semua file JPG di dalam folder input menjadi PNG dan menyimpannya di folder output dengan nama baru yang berisi tanggal dan waktu.

    Args:
        input_folder (str): Path ke folder yang berisi file JPG.
        output_folder (str): Path ke folder tujuan untuk menyimpan file PNG.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            try:
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)

                # Ambil tanggal dan waktu saat ini
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y%m%d_%H%M%S")

                # Buat nama file baru dengan format: nama_asli_tanggal_waktu.png
                new_filename = f"{os.path.splitext(filename)[0]}_{timestamp}.png"
                new_filepath = os.path.join(output_folder, new_filename)

                img.save(new_filepath, "PNG")
                print(f"File {filename} berhasil dikonversi menjadi {new_filename}")

            except Exception as e:
                print(f"Gagal mengonversi file {filename}: {e}")

if __name__ == "__main__":
    # Input dari pengguna untuk folder input dan output
    input_folder = input("D:\Pemrograman Python Lanjut: ").strip()
    output_folder = input("D:\Pemrograman Python Lanjut: ").strip()

    # Validasi folder input
    if not os.path.exists(input_folder):
        print("Folder input tidak ditemukan. Pastikan path benar.")
    else:
        # Jalankan fungsi konversi
        convert_images(input_folder, output_folder)

    print("Proses selesai.")