import numpy as np, json, time
from yukawa_euclid_gap import run
rows=[]
print("== P3: slope at eps=1 (m=mu=0.5), Ns=48 ==")
for eps in [1.04,1.02,1.01,1.0,0.99,0.98,0.96]:
    r48=run(48,48,eps,0.5,0.5); r96=run(96,48,eps,0.5,0.5); r64=run(64,64,eps,0.5,0.5)
    print(f"eps={eps:5.2f} gap Nt48={r48['gap']: .7f} Nt96,Ns48={r96['gap']: .7f} N64={r64['gap']: .7f}")
    rows.append(dict(eps=eps,gap48=r48['gap'],gap96=r96['gap'],gap64=r64['gap']))
g={r['eps']:r['gap64'] for r in rows}
slope=(g[1.01]-g[0.99])/0.02
slope2=(g[1.02]-g[0.98])/0.04
print("centered slope d gap/d eps at 1 (h=0.01,0.02):",slope,slope2)
json.dump(rows,open('scan3.json','w'),indent=1)
