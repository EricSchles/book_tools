import pandas as pd
import d3py
import networkx as nx
import matplotlib.pyplot as plt

df = pd.DataFrame().from_csv("sna_example1.csv",index_col=False)
G = nx.from_pandas_dataframe(df,"source","target")

nx.draw(G, with_labels=True)
plt.savefig("sna_example1.png")

