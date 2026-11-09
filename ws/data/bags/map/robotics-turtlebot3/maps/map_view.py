import sys
import numpy as np
from PIL import Image

# Konversi gambar ke Grayscale ('L') agar aman dari error channel RGB
img = np.array(Image.open(sys.argv[1]).convert('L'))

# Header nomor kolom (angka 0-9 berulang)
print('    ' + ''.join(str(c % 10) for c in range(img.shape[1])))

# Baris cetakan peta ASCII
for i, row in enumerate(img):
    print(f'{i:3d} ' + ''.join('#' if v < 100 else ('.' if v > 240 else ' ') for v in row))
