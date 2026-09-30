import math, importlib.util
spec = importlib.util.spec_from_file_location('t', 'test_T73.py')
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
for w in (0.01,0.1,0.3,1.0,3.0,10.0,100.0):
    row=[]
    for L in (10,14,18,22):
        _,adj=t.grid_adj(L,1); d=t.frozen_distribution(adj,w); S1=t.renyi(d)[0]
        row.append((L,round(S1,3),round(S1/math.log(len(d)),3)))
    inc=(row[-1][1]-row[0][1])/(row[-1][0]-row[0][0])
    print(f"w={w:<6} (L,S1,S1/S0)={row}  slope dS1/dL={inc:.4f}",flush=True)
