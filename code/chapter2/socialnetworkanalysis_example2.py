import pandas as pd
import d3py
import networkx as nx
import matplotlib.pyplot as plt

df1 = pd.DataFrame().from_csv("sna_example1.csv",index_col=False)
df2 = pd.DataFrame().from_csv("sna_example2.csv",index_col=False)

G1 = nx.from_pandas_dataframe(df1,"source","target")
G2 = nx.from_pandas_dataframe(df2,"source","target")

G = nx.compose(G1,G2)
nx.draw(G, with_labels=True)
plt.savefig("sna_example2.png")

