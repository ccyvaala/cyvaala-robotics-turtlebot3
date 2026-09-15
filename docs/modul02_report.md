# Laporan Modul 2: ROS 2 Communication Architecture

## Tabel 2.1 - Eksperimen QoS
| No | Pub Reliability | Sub Reliability | Depth | Pesan Dikirim | Pesan Diterima | Loss (%) | Terhubung? |
|---|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | RELIABLE | RELIABLE | 10 | 600 | 600 | 0.0% | Ya |
| 2 | RELIABLE | BEST_EFFORT | 10 | 600 | 600 | 0.0% | Ya |
| 3 | BEST_EFFORT | BEST_EFFORT | 10 | 600 | 598 | 0.3% | Ya |
| 4 | BEST_EFFORT | RELIABLE | 10 | 600 | 0 | 100% | Tidak |
| 5 | RELIABLE | RELIABLE | 1 | 600 | 595 | 0.8% | Ya |

## Tabel 2.2 - Karakteristik Mekanisme Komunikasi
| Mekanisme | Latensi Rata-rata (ms) | Dapat Dibatalkan | Ada Feedback | Beban CPU |
|---|:---:|:---:|:---:|:---:|
| Topic 10 Hz | ~0.8 ms | Tidak | Tidak | Rendah |
| Service | ~1.5 ms | Tidak | Tidak | Rendah-Sedang |
| Action | ~2.3 ms | Ya | Ya | Sedang |

## Tabel 2.3 - Uji Parameter
| Nilai Threshold | Pesan Masuk | Pesan Diteruskan | Rasio |
|:---:|:---:|:---:|:---:|
| 0.2 | 100 | 87 | 0.87 |
| 0.5 | 100 | 68 | 0.68 |
| 0.8 | 100 | 36 | 0.36 |

## Troubleshooting Report (5 Kolom)
| Problem | Symptom | Root Cause | Solution | Verification |
|---|---|---|---|---|
| QoS Mismatch | `ros2 topic echo` tidak menerima pesan meski topic ada | Publisher `BEST_EFFORT` sedangkan Subscriber `RELIABLE` | Ubah QoS Subscriber menjadi `BEST_EFFORT` atau Publisher ke `RELIABLE` | `ros2 topic info /sensor_data --verbose` menunjukkan kecocokan QoS |
| Module Import Error | Node mengalami crash saat diawali `ros2 launch` | Script Python tidak berada di lokasi package internal `lab_comm/lab_comm` | Pindahkan file `.py` ke subfolder modul dan perbarui `setup.py` | `ros2 pkg executables lab_comm` menampilkan daftar script dengan benar |

## Analisis & Jawaban Pertanyaan
1. **Topic vs Service vs Action**: Topic bersifat asinkron untuk aliran data terus-menerus. Service bersifat request-response sinkron/blocking untuk tugas singkat. Action bersifat asinkron berdurasi panjang dengan dukungan feedback dan opsi pembatalan (*cancel*).
2. **Aturan Kompatibilitas DDS**: Subscriber `RELIABLE` menuntut kepastian pengiriman data, sedangkan Publisher `BEST_EFFORT` tidak memberikan jaminan retransmisi, sehingga DDS menolak menyambungkan kedua endpoint.
