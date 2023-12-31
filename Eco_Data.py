 %%
import stats_can

eco_vec_map = {'CPI':'v41690973',
               'Exchange_Rate_USD':'v111666275',
               'GDP':'v65201210',
               #'Unemployment_Rate':'v91506256',
               'TSX':'v122620',
               "New housing price indexes":"v111955442"}
vectors = list(eco_vec_map.values())
N = 27
df = stats_can.sc.vectors_to_df(vectors, periods = N)
vectors = list(eco_vec_map.values())
df = stats_can.sc.vectors_to_df(vectors, periods = N)

inv_map = {v: k for k, v in eco_vec_map.items()}
df.columns = df.columns.to_series().map(inv_map)
df.index.names = ['Date']

# plot
df.plot(subplots = True, figsize = (14,8), layout = (3,2))


# %%
