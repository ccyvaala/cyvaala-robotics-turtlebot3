# Laporan Modul 1: Dockerized ROS 2 Development Environment

## Tabel 1.1 Metrik Lingkungan Pengembangan
| No | Parameter | Satuan | Hasil |
|---|---|:---:|:---:|
| 1 | Waktu docker pull image dasar | s | 250 |
| 2 | Waktu build image pertama (tanpa cache) | s | 186.2 |
| 3 | Waktu build image kedua (dengan cache) | s | ~2 |
| 4 | Ukuran image robotics-lab:dev | GB | 1.92 |
| 5 | Waktu startup container | s | ~1 |
| 6 | Waktu colcon build pertama | s | 1.36 |
| 7 | Jumlah package terbangun | buah | 1 |
| 8 | Commit hash | — | 2818127 |

## Tabel 1.2 Perbandingan Bind Mount vs Named Volume
| Aspek | Bind mount `../src:/ws/src` | Named volume `ws_install` |
|---|:---:|:---:|
| Terlihat di host | Ya | Tidak |
| Bertahan setelah docker compose down | Ya | Ya |
| Cocok untuk kode sumber | Ya | Tidak |
| Cocok untuk artefak build | Tidak | Ya |
