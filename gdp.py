import pandas as pd
from matplotlib import pyplot as plt

COUNTRY = "Country Name"
YEAR = "Year"
VALUE = "Value"
GDP = "GDP"
USA = "United States"
EU = "European Union"
CN = "China"

url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"
sample_data=pd.read_csv(url)

usa_dat = sample_data.loc[sample_data[COUNTRY] == USA]
eu_dat = sample_data.loc[sample_data[COUNTRY] == EU]
cn_dat = sample_data.loc[sample_data[COUNTRY] == CN]

plt.plot(usa_dat[YEAR], usa_dat[VALUE])
plt.plot(eu_dat[YEAR], eu_dat[VALUE])
plt.plot(cn_dat[YEAR], cn_dat[VALUE])
plt.legend([USA, EU, CN])
plt.xlabel(YEAR)
plt.ylabel(GDP)
plt.title("Annual GDP Values")
plt.show()
