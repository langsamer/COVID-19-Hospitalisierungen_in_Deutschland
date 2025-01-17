# %%
import pandas as pd
import streamlit as st
from datetime import date, timedelta

cv19h_frame = pd.read_csv("Aktuell_Deutschland_COVID-19-Hospitalisierungen.csv")
# print(cv19h_frame.shape)
# print(cv19h_frame.index)
# print(cv19h_frame.columns)

# %%

date_range = st.slider(
    label="Zeitraum",
    min_value=date(year=2020, month=3, day=5),
    max_value=date.today(),
    value=(date.today()+timedelta(days=-30), date.today()),
    )

df = cv19h_frame
recent = cv19h_frame.loc[
    (df.Bundesland == 'Bundesgebiet')
    & (df.Altersgruppe == '00+')
    & (df.Datum >= date_range[0].isoformat())
    & (df.Datum <= date_range[1].isoformat())
    ]

# %%
recent_by_date = recent.loc[:, ["Datum", "7T_Hospitalisierung_Inzidenz"]].set_index("Datum")
st.line_chart(recent_by_date)

st.write(f"7-Tage-Hospitalisierungs-Inzidenz im Zeitraum von {date_range[0].isoformat()} bis {date_range[1].isoformat()}")
st.markdown("Quelle: [Robert-Koch-Institut](https://github.com/robert-koch-institut/COVID-19-Hospitalisierungen_in_Deutschland)")
