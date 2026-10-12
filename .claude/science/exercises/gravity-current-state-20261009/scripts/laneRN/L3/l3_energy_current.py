"""L3 check 3 (illustration, 1D periodic chains): is the TOTAL energy current conserved?
First-class lapse+shift coupling to H_N needs the shift source = (energy current)/J + curl, and that source
conserved => the total energy current must be conserved (up to i[H,W], W local).  Free (XX), integrable (XXZ)
and non-integrable (XXZ + NNN, tilted Ising) chains. J_tot = (i/2) sum_{b,b'} (R_b' - R_b) [h_b, h_b'], R = term centre
(minimal image)."""
import numpy as np, itertools, sys
L = int(sys.argv[1]) if len(sys.argv)>1 else 10
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1.]).astype(complex); I2=np.eye(2)
def op(ops):  # dict site->2x2
    m=np.array([[1.]],complex)
    for s in range(L): m=np.kron(m, ops.get(s,I2))
    return m
def terms(model):
    T=[]  # list of (centre, matrix)
    for x in range(L):
        y=(x+1)%L; z=(x+2)%L
        if model in ("XX","XXZ","XXZ+NNN"):
            D = {"XX":0.0,"XXZ":0.6,"XXZ+NNN":0.6}[model]
            h=op({x:sx,y:sx})+op({x:sy,y:sy})+D*op({x:sz,y:sz})
            T.append((x+0.5,h))
            if model=="XXZ+NNN":
                T.append((x+1.0, 0.5*(op({x:sx,z:sx})+op({x:sy,z:sy})+0.6*op({x:sz,z:sz}))))
        elif model=="Ising-tilted":
            T.append((x+0.5, op({x:sz,y:sz})))
            T.append((float(x), 0.9045*op({x:sx}) + 0.8090*op({x:sz})))
        elif model=="Ising-transverse":
            T.append((x+0.5, op({x:sz,y:sz})))
            T.append((float(x), 0.9045*op({x:sx})))
    return T
def mind(a,b):
    d=(b-a)%L
    return d-L if d>L/2 else d
for model in ("XX","XXZ","XXZ+NNN","Ising-transverse","Ising-tilted"):
    T=terms(model); H=sum(t[1] for t in T)
    J=np.zeros_like(H)
    for (ra,ha),(rb,hb) in itertools.product(T,T):
        d=mind(ra,rb)
        if abs(d)>2.01: continue
        c=ha@hb-hb@ha
        if np.abs(c).max()>1e-14: J+=0.5j*d*c
    C=H@J-J@H
    print(f"{model:17s} L={L}: ||[H,J_E]||_F/(||H||_F ||J_E||_F/sqrt(dim)) = {np.linalg.norm(C)/(np.linalg.norm(H)*np.linalg.norm(J)/np.sqrt(H.shape[0])):.3e}")
