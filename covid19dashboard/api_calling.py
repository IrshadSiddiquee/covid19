import pandas as pd
import numpy as np
from datetime import date, timedelta

# import state wise cases from API
df_state_wise_cases = pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')

# import month wise cases from API
df_month_wise_cases = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")

# import state wise per day cases case from API
df_state_wise_per_day_cases = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
