import pandas as pd

# Cambiá las rutas a donde tengas los archivos en tu PC
categories = pd.read_csv("C:/Users/jmleo/Desktop/Juan Martin/Austral/2° Cuatri 2° año/marketing/retail_dw_lab/raw/categories.csv")
products = pd.read_csv("C:/Users/jmleo/Desktop/Juan Martin/Austral/2° Cuatri 2° año/marketing/retail_dw_lab/raw/products.csv")

# Join por category_id
merged = products.merge(categories, on="category_id", how="left")

# Guardar el nuevo CSV en cualquier carpeta
merged.to_csv("C:/Users/jmleo/Desktop/Juan Martin/Austral/2° Cuatri 2° año/marketing/retail_dw_lab/raw/products_denormalized.csv", index=False)

print("Archivo 'products_denormalized.csv' creado con éxito.")
