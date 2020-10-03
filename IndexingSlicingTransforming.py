#Indexing Practice
"""
dataframe_week = pd.DataFrame({
    "hari-ke":[1,2,3,4,5,6,7,8], "minggu-gol":["wekdae" for i in range(5)] + ["wekend" for i in range(3)]
})
dataframe_week.index = [i for i in range (8)]
print(dataframe_week)
dataframe_week.reset_index(drop=True)
print(dataframe_week)
"""

#Indexing Part 4
"""
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep = "\t", nrows = 10)
# Cetak data frame awal
print("Dataframe awal:\n",df)
df.index = ["Pesanan ke-" + str(i) for i in range (1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)
"""

#Indexing Part 5
"""
# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep="\t", index_col=["order_date","order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n",df.head(8))
"""

#Slicing Part 1
"""
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == "18055") &
		          (df["product_id"].isin(["P0029", "P0040", "P0041", "P0116", "P0117"]))
				 ]
print("Slice langsung berdasarkan kolom:\n", df_slice)
"""

#Slicing Part 2
"""
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")

# Set index dari df sesuai instruksi
df = df.set_index(["order_date","product_id"])
# Cara 1 : Gunakan .loc
df_slice1 = df.loc[("2019-01-01", ["P2154","P2556"]),:]
print("Cara 1:\n", df_slice1)
# Cara 2 : Gunakan pd.Indexslice dan terapkan dengan .loc
idx = pd.IndexSlice
df_slice2 = df.sort_index().loc[pd.IndexSlice["2019-01-01", "P2154": "P2556"], :]
print("Cara 2:\n", df_slice2)

# Cara 3
# Set index dari df sesuai instruksi
df = df.set_index(["order_date", "order_id", "product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01", "1612339", ["P2154","P2159"]), :]
print("Slice df:\n", df_slice)
"""

#Transforming Part 1
"""
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)
"""

#Transforming Part 2
"""
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom quantity menjadi tipe data numerik float
df["quantity"] = pd.to_numeric(df["quantity"], downcast="float")
# Ubah tipe data kolom city menjadi tipe data category
df["city"] = df["city"].astype("category")
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)
"""

#Transforming Part 3
"""
import pandas as pd
# Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
# Cetak 5 baris teratas kolom brand
print("Kolom brand awal:\n", df["brand"].head())
# Gunakan method apply untuk merubah isi kolom menjadi lower case
df["brand"] = df["brand"].apply(lambda x: x.lower())
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah apply:\n", df["brand"].head())
# Gunakan method map untuk mengambil kode brand yaitu karakter terakhirnya
df["brand"] = df["brand"].apply(lambda x: x[-1])
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah map:\n", df["brand"].head())
"""

#Transforming Part 4

# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu sama ketika kita run
np.random.seed(1234)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3,4))
# Cetak dataframe
print("Dataframe:\n", df_tr)
# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x
df_tr1 = df_tr.applymap(lambda x: x**2+3*x+2)
print("\nDataframe - cara 1:\n", df_tr1)
# Cara 2 dengan define function
def quadratic_fun(x):
	return x**2+3*x+2
df_tr2 = df_tr.applymap(quadratic_fun)
print("\nDataframe - cara 2:\n", df_tr2)