import sys
import numpy as np
from PIL import Image

# 1. Buka gambar dan konversi ke grayscale ('L')
img_path = sys.argv[1]
img = np.array(Image.open(img_path).convert('L'))

# 2. Cetak Header Angka Kolom (ASCII Art)
print('    ' + ''.join(str(c % 10) for c in range(img.shape[1])))

# 3. Cetak Baris Gambar Peta
for i, row in enumerate(img):
    print(f'{i:3d} ' + ''.join('#' if v < 100 else ('.' if v > 240 else ' ') for v in row))

# 4. Hitung Statistik Peta (ROS Map standard)
total_cells = img.size
occupied_cells = np.sum(img < 100)      # Dinding/Hambatan (#)
free_cells = np.sum(img > 240)          # Area Bebas (.)
unknown_cells = np.sum((img >= 100) & (img <= 240))  # Area Belum Terjamah (spasi)
unknown_pct = (unknown_cells / total_cells) * 100

# 5. Cetak Hasil Analisis Utama
print("\n" + "="*40)
print(f"ukuran peta (baris x kolom): {img.shape}")
print(f"occupied cells: {occupied_cells}")
print(f"unknown cells: {unknown_cells}")
print(f"unknown (%): {unknown_pct:.1f}")

# 6. Cetak Jarak Antar Dinding HANYA jika nomor baris diberikan di terminal
if len(sys.argv) > 2:
    target_row = int(sys.argv[2])
    resolution = 0.05  # Resolusi default ROS map (5cm/pixel)
    row_pixels = img[target_row]
    occupied_indices = np.where(row_pixels < 100)[0]

    if len(occupied_indices) >= 2:
        wall_distance = (occupied_indices[-1] - occupied_indices[0]) * resolution
    else:
        wall_distance = 0.0

    print(f"baris {target_row} -> jarak antar dinding (m): {wall_distance:.2f}")
