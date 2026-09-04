"""T12 - production scan: improved operator, m=0, nk=1, three polarisations,
per-polarisation and joint fits."""
import numpy as np, sys, time, json; sys.path.insert(0,".")
from bridge_fit import *
L=int(sys.argv[1]); TAUS=[float(x) for x in sys.argv[2].split(',')]
IMP=[True] if len(sys.argv)<4 else [s=='1' for s in sys.argv[3].split(',')]
NK=1 if len(sys.argv)<5 else int(sys.argv[4])
ALPHAS=[[1,1,1,1],[0,1,0,0],[0,1,-1,0]]
SET=[(t,0.0,i) for i in IMP for t in TAUS]
t0=time.time()
ch=channels(L,0.03,NK,ALPHAS,SET,verbose=True)
res=summarise(L,NK,SET,ch)
print(f"# T12  L={L}  nk={NK}  amp=0.03  m=0   ({time.time()-t0:.0f}s)"); print(HDR)
for d in res: print(line(d), flush=True)
json.dump([{k:(v if not isinstance(v,list) else list(map(float,v))) for k,v in d.items()} for d in res],
          open(f"t12_L{L}_nk{NK}.json","w"), indent=0)
