import json
import os
import re

# Dosya yolları
input_folder = r"c:\Users\IT\Desktop\datas\Chunked-1400-200"
output_folder = r"c:\Users\IT\Desktop\datas\AnythingLLM_Ready"
jsonl_files = ["case_law.jsonl", "explanation.jsonl"]
html_file = "avukatGPT_training.html"

# Çıktı klasörünü oluştur
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def clean_text(text):
    """Metni temizler ve düzenler."""
    if not text:
        return ""
    # Gereksiz boşlukları temizle
    text = text.strip()
    return text

def process_jsonl(file_name):
    """JSONL dosyasını işler ve Markdown formatına çevirir."""
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name.replace(".jsonl", ".md"))
    
    print(f"İşleniyor: {file_name} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            try:
                data = json.loads(line)
                
                # Alanları al
                title = data.get("title", "Başlıksız")
                category = data.get("category", "Genel")
                response = data.get("response", "")
                instruction = data.get("instruction", "")
                
                # Markdown formatında yaz
                outfile.write(f"# {title}\n")
                outfile.write(f"**Kategori:** {category}\n\n")
                if instruction:
                    outfile.write(f"**Soru/Talimat:** {instruction}\n\n")
                outfile.write(f"{clean_text(response)}\n")
                outfile.write("\n---\n\n") # Ayraç
                
            except json.JSONDecodeError:
                continue

def process_html(file_name):
    """HTML dosyasını işler ve Markdown formatına çevirir."""
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name.replace(".html", ".md"))
    
    print(f"İşleniyor: {file_name} -> {output_path}")
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        content = infile.read()
        
        # Sectionları bul (Regex ile basit parsing)
        # <section id='...'> ... </section> bloklarını bulmaya çalışacağız
        # Ancak dosya çok büyük olduğu için satır satır veya blok blok gitmek daha güvenli olabilir.
        # Basit regex yaklaşımı (bellek dostu olması için finditer kullanıyoruz)
        
        # Not: HTML yapısı düzenli görünüyor, regex ile title ve content'i alacağız.
        # <title>(.*?)</title> ve <content>(.*?)</content>
        
        sections = re.finditer(r"<section id='(.*?)'>\s*<title>(.*?)</title>\s*<content>(.*?)</content>\s*</section>", content, re.DOTALL)
        
        for match in sections:
            section_id = match.group(1)
            title = match.group(2)
            text_content = match.group(3)
            
            outfile.write(f"# {title}\n")
            outfile.write(f"**ID:** {section_id}\n\n")
            outfile.write(f"{clean_text(text_content)}\n")
            outfile.write("\n---\n\n")

# İşlemleri başlat
print("Dönüştürme işlemi başlıyor...")

# 1. JSONL Dosyalarını Dönüştür
for f in jsonl_files:
    if os.path.exists(os.path.join(input_folder, f)):
        process_jsonl(f)
    else:
        print(f"Uyarı: {f} bulunamadı.")

# 2. HTML Dosyasını Dönüştür
if os.path.exists(os.path.join(input_folder, html_file)):
    process_html(html_file)
else:
    print(f"Uyarı: {html_file} bulunamadı.")

print("İşlem tamamlandı. Dosyalar 'AnythingLLM_Ready' klasöründe.")
