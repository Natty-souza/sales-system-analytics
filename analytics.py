import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
data = pd.read_csv("sales_data.csv")

# calcular total por linha
data["total"] = data["quantity"] * data["price"]

print("Total Sales:", data["total"].sum())

# gráfico
plt.bar(data["product"], data["total"])
plt.title("Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.savefig("report.png")
print("Report generated: report.png")
