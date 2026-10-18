exec(open('b18lib.py').read())
import time
PIV=[np.array(v) for v in itertools.product((0,1),repeat=3) if any(v)]
OM=[1,-1,1j,-1j]
t0=time.time()
for nm,bl in (("H_link",blli),("S",blS),("H_on",onsite_blocks(Hon0)),("Lam",onsite_blocks(Lam))):
    for e in PIV:
        row=[]
        for om in OM:
            B,_=intertwiners(bl,shifted(bl,e,om),r=0)
            row.append((om,len(B),round(generic_invertible(B),3)))
        print(nm,e,row,flush=True)
print(time.time()-t0)
