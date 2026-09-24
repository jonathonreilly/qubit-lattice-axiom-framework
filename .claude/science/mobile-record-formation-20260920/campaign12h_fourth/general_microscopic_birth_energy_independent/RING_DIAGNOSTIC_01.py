"""Source of the exploratory diagnostic initially run as a shell heredoc."""
import matrix_control as m
import numpy as np,json
rows=[]
for S in (None,1,2,4,8):
    p=m.matrices(6,3,S=S);q=m.matrices(6,5,S=S)
    z=(tuple(int(i in p['A']) for i in range(6)),None if S is None else (0,)*6)
    col=list(p['P']).index(p['index'][z]);J=m.jump(p,q,0,1)
    e=.003
    hp,_,_,vp=m.canonical(p,e);hq,_,uq,vq=m.canonical(q,e)
    d=vp[:,col];y=J@d;y/=np.linalg.norm(y);hy=hq@y
    mean=np.vdot(y,hy).real;v=(np.vdot(hy,hy).real-mean*mean)/e**6
    high=np.linalg.norm(uq[:,len(q['P']):].conj().T@y)**2/e**6
    rows.append({'S':S,'eps':e,'eps2_variance':v,'high_over_eps6':high,'post_mean':mean/e**4})
print(json.dumps(rows,indent=2))
