# DKA3223 PRACTICAL TEST 1
## AgriVision-CNN — Laporan Ringkas

**Nama:** ______________________________  
**No. Kad Pengenalan:** __________________  
**Angka Giliran:** _______________________  
**Tarikh:** ______________________________  

### 1. Pengenalan
Projek ini membangunkan prototaip pengelasan imej menggunakan
Convolutional Neural Network (CNN) dengan PyTorch. Dataset CIFAR-10 digunakan
sebagai dataset contoh untuk latihan dan visualisasi.

### 2. Struktur Projek
Masukkan screenshot struktur folder/repository sendiri di bawah.

**[SCREENSHOT SENDIRI — STRUKTUR PROJEK]**

### 3. Visualisasi Dataset
Terangkan bahawa `dataset_handler.py` menggunakan torchvision untuk memuatkan
dataset, NumPy untuk penukaran susunan data imej, dan Matplotlib untuk
memaparkan tiga sampel pertama bersama label.

**[SCREENSHOT SENDIRI — 3 GAMBAR MATPLOTLIB + LABEL]**

### 4. Model CNN
Fail `cnn_model.py` mengandungi kelas CNN dengan sekurang-kurangnya dua
convolutional layers dan fully connected layers.

**[SCREENSHOT SENDIRI — cnn_model.py]**

### 5. Prompt AI Code Assistant
Masukkan screenshot komen prompt AI yang digunakan dalam `cnn_model.py`.

**[SCREENSHOT SENDIRI — PROMPT AI, MINIMUM 3 BARIS]**

### 6. Hyperparameter
| Hyperparameter | Nilai |
|---|---:|
| Learning Rate | 0.001 |
| Epochs | 3 |
| Batch Size | 32 |

**[SCREENSHOT SENDIRI — train.py]**

### 7. Forward & Backward Propagation
Ringkasan:
- Forward: input dihantar melalui model untuk menghasilkan output.
- Loss: `CrossEntropyLoss` membandingkan output dengan label.
- Backward: `loss.backward()` mengira gradient.
- Update: `optimizer.step()` mengemas kini parameter model.

**[SCREENSHOT SENDIRI — OUTPUT LATIHAN]**

### 8. Output Loss
Masukkan output sebenar daripada komputer sendiri. Jangan reka nilai.

**[SCREENSHOT SENDIRI — 3 EPOCH + LOSS]**

### 9. Git & GitHub
Repository GitHub:
**[MASUKKAN URL REPOSITORY SENDIRI]**

Branch:
`feature-hyperparameter`

**[SCREENSHOT SENDIRI — GITHUB BRANCH + FAIL]**

**[SCREENSHOT SENDIRI — COMMIT HISTORY]**

### 10. Kesimpulan
Projek berjaya dibina secara modular menggunakan Python dan PyTorch.
Proses latihan melibatkan forward propagation, pengiraan loss, backward
propagation dan kemas kini parameter menggunakan optimizer. Kod juga diurus
menggunakan Git dan dihantar ke repository GitHub melalui branch yang sesuai.

### Checklist sebelum hantar
- [ ] Repository bernama `AgriVision-CNN`
- [ ] `dataset_handler.py`
- [ ] `cnn_model.py`
- [ ] `train.py`
- [ ] Learning Rate = 0.001
- [ ] Epochs = 3
- [ ] Batch Size = 32
- [ ] 2 convolutional layers minimum
- [ ] 1 fully connected layer minimum
- [ ] Prompt AI minimum 3 baris komen
- [ ] Forward propagation
- [ ] Loss calculation
- [ ] Backward propagation
- [ ] Branch `feature-hyperparameter`
- [ ] Commit
- [ ] Push
- [ ] Screenshot 3 imej
- [ ] Screenshot output loss
- [ ] Screenshot GitHub branch
- [ ] Laporan PDF
- [ ] URL GitHub
- [ ] Upload ke Google Classroom
- [ ] Cetak laporan
