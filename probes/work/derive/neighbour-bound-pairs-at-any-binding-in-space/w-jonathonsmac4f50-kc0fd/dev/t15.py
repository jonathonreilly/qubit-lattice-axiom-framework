import pickle,numpy as np,collections
rows=pickle.load(open('scan600.pkl','rb'))
EC=2*np.sqrt(3)
byE=collections.defaultdict(list)
for r in rows: byE[round(r[1],4)].append(r)
print('E  g-range  max Wsum  (count>3, count>1.6)')
for E in sorted(byE)[::3]:
    rr=byE[E]
    gs=[r[2] for r in rr]
    mx=max(r[4] for r in rr); 
    print('E=%.3f g in [%.1f,%.1f] max=%.2f  n>3:%d n>1.6:%d  of %d'%(E,min(gs),max(gs),mx,sum(r[4]>3 for r in rr),sum(r[4]>1.6 for r in rr),len(rr)))
