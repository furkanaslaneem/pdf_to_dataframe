import tabula
import pandas as pd

# PDF dosyasını oku ve verileri bir DataFrame'e çevir
df = tabula.read_pdf("PDF dosyasının bulunduğu yolu buraya giriniz", pages='all')

# Birden fazla sayfa varsa, tüm sayfaları birleştirin
merged_df = pd.concat(df)

# Verileri görüntüle
print(merged_df)
