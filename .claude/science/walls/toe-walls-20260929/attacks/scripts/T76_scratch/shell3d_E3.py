import sys, collections
import count3d as c
A=(0,2,3,4,5,6); Aset=set(A)
for L in (2,3,4):
    fs,sites,nb=c.frozen_all(L,A,10**7)
    memo={}
    rs=[m for m in fs if c.reachable_set(m,nb,Aset,memo)]
    out=[]
    for name,states in (("frozen",fs),("reachable",rs)):
        for depth in (1,2):
            g=collections.Counter()
            for m in states:
                key=tuple((m>>i)&1 for i,s in enumerate(sites) if min(min(x,L-1-x) for x in s)<depth)
                g[key]+=1
            out.append(f"{name} d{depth}: shells={len(g)} max={max(g.values())}")
    print(f"3D E3 L={L}: frozen={len(fs)} reachable={len(rs)} | "+" | ".join(out),flush=True)
