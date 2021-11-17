# %%
import pandas as pd

cv19h_frame = pd.read_csv("Aktuell_Deutschland_COVID-19-Hospitalisierungen.csv")
print(cv19h_frame.shape)
print(cv19h_frame.index)
print(cv19h_frame.columns)

# %%
cv19h_indexed = cv19h_frame.set_index(["Datum", "Bundesland", "Altersgruppe"])
# %%
cv19h_indexed
