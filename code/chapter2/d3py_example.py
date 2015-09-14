import pandas as pd
import d3py
import networkx as nx

df = pd.DataFrame().from_csv("sna_example1.csv",index_col=False)
G = nx.from_pandas_dataframe(df,"source","target")

with d3py.NetworkXFigure(G, name="graph", width=200, height=200) as p:
    p += d3py.ForceLayout()
    # To Do - add labels to d3py graphs
    p.css['.node'] = {'fill': 'blue', 'stroke': 'magenta','label':'test', "font-family":"Arial","font-size":12}
    p.save()
    p.show()
