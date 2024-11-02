# # Arbeidskrav 1
# ## ANZ
# ### 2024 11 02

# In[56]:

#Python-program som beregner og presenterer de årlige totalkostnadene
#for elbil og for bensinbil samt årlig kostnadsdifferanse utifra info under

#Variabler
kjørte_kilometer_per_år = 10000  # km/år
forsikring_elbil = 5000  # kr/år
forsikring_bensinbil = 7500  # kr/år
trafikkforsikringsavgift_per_dag = 8.38  # kr/dag
drivstoffbruk_elbil_per_km = 0.2  # kWh/km
strømpris_per_kWh = 2.00  # kr/kWh
drivstoffpris_bensinbil_per_km = 1.00  # kr/km
bomavgift_elbil_per_km = 0.1  # kr/km
bomavgift_bensinbil_per_km = 0.3  # kr/km

#Forsikringsavgift for hele året
trafikkforsikringsavgift_år = 8.38 * 365  # trafikkforsikringsavgift per dag * 365 dager

#Årlig totalkostnad elbil
drivstoffkostnad_elbil = 10000 * 0.2 * 2.00  # kjørte_kilometer_per_år * drivstoffbruk_elbil_per_km * strømpris_per_kWh
bomkostnad_elbil = 10000 * 0.1  # kjørte_kilometer_per_år * bomavgift_elbil_per_km
totalkostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_år + drivstoffkostnad_elbil + bomkostnad_elbil

#Årlig totalkostnad bensinbil
drivstoffkostnad_bensinbil = 10000 * 1.00  # kjørte_kilometer_per_år * drivstoffpris_bensinbil_per_km 
bomkostnad_bensinbil = 10000 * 0.3  # kjørte_kilometer_per_år * bomavgift_bensinbil_per_km
totalkostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_år + drivstoffkostnad_bensinbil + bomkostnad_bensinbil

#Kostnadsdifferanse mellom elbil og bensinbil
differanse = totalkostnad_bensinbil - totalkostnad_elbil

print('totalkostnad_elbil =', totalkostnad_elbil)
print('totalkostnad_bensinbil =', totalkostnad_bensinbil)
print('differanse =', differanse)

# In[ ]:




