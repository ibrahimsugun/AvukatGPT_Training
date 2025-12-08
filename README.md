# AvukatGPT/YASAMASA Training Dataset

[English](#english) | [Türkçe](#türkçe)

---

## English

### Overview

This repository contains training datasets for **YASAMASA**, a legal AI assistant specialized in Turkish law. The dataset includes comprehensive legal materials, case law, and legal documentation formatted for both fine-tuning and RAG (Retrieval Augmented Generation) applications.

### Repository Structure

```
AvukatGPT_Training/
├── FINE-Tune/                    # Fine-tuning datasets
│   ├── AnythingLLM_Ready/        # Markdown files ready for AnythingLLM
│   │   ├── case_law.md
│   │   └── case_law_chunked.md
│   └── Chunked-1400-200/         # JSONL files for fine-tuning
│       ├── case_law.jsonl
│       ├── case_law_chunked.jsonl
│       ├── example.jsonl
│       └── convert_to_md.py      # Conversion script
│
└── RAG/                          # RAG (Retrieval Augmented Generation) datasets
    ├── avukatGPT_training.html   # Main training HTML file
    └── blog_contents/            # Legal blog content
        ├── AnythingLLM_Ready/   # Processed markdown files
        └── blog_contents/
            ├── converted_markdown/  # 1960+ markdown files
            └── txt_contents/        # Original text files
```

### Dataset Contents

#### Fine-Tuning Data (`FINE-Tune/`)
- **JSONL Format**: Structured training data with 1400-200 token chunks
- **Markdown Format**: Human-readable legal documents ready for LLM ingestion
- **Case Law**: Comprehensive Turkish legal case law and precedents

#### RAG Data (`RAG/`)
- **Legal Blog Content**: 1960+ markdown files covering various legal topics
- **Turkish Legal System**: Comprehensive coverage of:
  - Civil Law (HMK - Hukuk Muhakemeleri Kanunu)
  - Criminal Law (TCK - Türk Ceza Kanunu)
  - Administrative Law
  - Tax Law
  - Compensation Law
  - And many more legal domains

### Large File Storage

This repository uses **Git LFS (Large File Storage)** for files larger than 50MB:
- Large training files are stored efficiently

### Usage

#### For Fine-Tuning
```bash
# Use the JSONL files in FINE-Tune/Chunked-1400-200/
# These are formatted for direct fine-tuning with LLMs
```

#### For RAG Applications
```bash
# Use the markdown files in RAG/blog_contents/
# These are optimized for vector database ingestion
```

### Requirements

- Git LFS installed and configured
- Python 3.x (for conversion scripts)

### Installation

```bash
# Clone the repository
git clone https://github.com/ibrahimsugun/AvukatGPT_Training.git
cd AvukatGPT_Training

# Initialize Git LFS (if not already done)
git lfs install

# Pull LFS files
git lfs pull
```

### Contributing

This is a training dataset repository. For issues or contributions, please open an issue or contact the repository maintainer.

### License

[Specify your license here]

---

## Türkçe

### Genel Bakış

Bu depo, Türk hukuku konusunda uzmanlaşmış bir yasal AI asistanı olan **YASAMASA** için eğitim veri setlerini içermektedir. Veri seti, hem fine-tuning hem de RAG (Retrieval Augmented Generation) uygulamaları için formatlanmış kapsamlı yasal materyaller, içtihat hukuku ve yasal dokümantasyon içerir.

### Depo Yapısı

```
AvukatGPT_Training/
├── FINE-Tune/                    # Fine-tuning veri setleri
│   ├── AnythingLLM_Ready/        # AnythingLLM için hazır markdown dosyaları
│   │   ├── case_law.md
│   │   └── case_law_chunked.md
│   └── Chunked-1400-200/         # Fine-tuning için JSONL dosyaları
│       ├── case_law.jsonl
│       ├── case_law_chunked.jsonl
│       ├── example.jsonl
│       └── convert_to_md.py      # Dönüştürme scripti
│
└── RAG/                          # RAG (Retrieval Augmented Generation) veri setleri
    ├── avukatGPT_training.html   # Ana eğitim HTML dosyası
    └── blog_contents/            # Yasal blog içerikleri
        ├── AnythingLLM_Ready/   # İşlenmiş markdown dosyaları
        └── blog_contents/
            ├── converted_markdown/  # 1960+ markdown dosyası
            └── txt_contents/        # Orijinal metin dosyaları
```

### Veri Seti İçeriği

#### Fine-Tuning Verileri (`FINE-Tune/`)
- **JSONL Formatı**: 1400-200 token parçalarıyla yapılandırılmış eğitim verileri
- **Markdown Formatı**: LLM tarafından işlenmeye hazır, insan tarafından okunabilir yasal belgeler
- **İçtihat Hukuku**: Kapsamlı Türk yasal içtihat hukuku ve emsal kararlar

#### RAG Verileri (`RAG/`)
- **Yasal Blog İçerikleri**: Çeşitli yasal konuları kapsayan 1960+ markdown dosyası
- **Türk Hukuk Sistemi**: Kapsamlı kapsam:
  - Medeni Hukuk (HMK - Hukuk Muhakemeleri Kanunu)
  - Ceza Hukuku (TCK - Türk Ceza Kanunu)
  - İdare Hukuku
  - Vergi Hukuku
  - Tazminat Hukuku
  - Ve daha birçok hukuk alanı

### Büyük Dosya Depolama

Bu depo, 50MB'dan büyük dosyalar için **Git LFS (Large File Storage)** kullanmaktadır:
- Tüm `.jsonl` dosyaları Git LFS ile takip edilir
- Tüm `.md` dosyaları Git LFS ile takip edilir
- Büyük eğitim dosyaları verimli bir şekilde depolanır

### Kullanım

#### Fine-Tuning İçin
```bash
# FINE-Tune/Chunked-1400-200/ klasöründeki JSONL dosyalarını kullanın
# Bunlar LLM'lerle doğrudan fine-tuning için formatlanmıştır
```

#### RAG Uygulamaları İçin
```bash
# RAG/blog_contents/ klasöründeki markdown dosyalarını kullanın
# Bunlar vektör veritabanı işleme için optimize edilmiştir
```

### Gereksinimler

- Git LFS kurulu ve yapılandırılmış
- Python 3.x (dönüştürme scriptleri için)

### Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/ibrahimsugun/AvukatGPT_Training.git
cd AvukatGPT_Training
```

### Katkıda Bulunma

Bu bir eğitim veri seti deposudur. Sorunlar veya katkılar için lütfen bir issue açın veya depo yöneticisiyle iletişime geçin.

### Lisans

[Lisansınızı buraya belirtin]


version https://git-lfs.github.com/spec/v1
oid sha256:6a80d6c8e784fa7f836aacd6e5901818f240a57fcc60cf6fc3ac20d6c4b35ece
size 7976
