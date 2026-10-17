import sys, itertools, numpy as np
sys.argv=['x','4']
import corner_psg as C
# completeness of the cycle constraints
rows=[]
for k,cs in C.cycles.items():
    for c in cs: rows.append(c)
piv={}
for r in rows:
    x=0
    for j in r: x^=1<<j
    while x:
        c=x.bit_length()-1
        if c in piv: x^=piv[c]
        else: piv[c]=x; break
nE=C.nE; nV=len(C.VERTS)
print('cycle-space dim',nE-nV+1,'rank of listed cycles',len(piv),'(3 torus holonomies expected missing)')
# PSG invariants for each flux pattern
def rotm(R): return lambda q,R=R: C.rot_vert(R,q)
def tm(t): return lambda q,t=t: C.trans_vert(t,q)
def comp(ops):
    """product of monomial maps (applied right-to-left as operators): returns (perm, sign)"""
    n=nV; perm=np.arange(n); sign=np.zeros(n,np.uint8)
    for P,s in reversed(ops):
        sign=sign^s[perm]; perm=P[perm]
    return perm,sign
def inv(P,s):
    n=len(P); Pi=np.empty(n,int); Pi[P]=np.arange(n); return Pi, s[Pi]
def rel(ops):
    perm,sign=comp(ops)
    assert (perm==np.arange(nV)).all()
    v=set(sign.tolist()); assert len(v)==1
    return -1 if v.pop() else 1
C4z=np.array([[0,-1,0],[1,0,0],[0,0,1]]); C2z=C4z@C4z
C3=np.array([[0,0,1],[1,0,0],[0,1,0]])
for Fb in itertools.product((0,1),repeat=4):
    F=dict(zip(('square','triangle','plaquette','tube'),Fb)); u=C.solve_u(F)
    g={}
    for name,f in (('Tx',tm((1,0,0))),('Ty',tm((0,1,0))),('Tz',tm((0,0,1))),('C4z',rotm(C4z)),('C2z',rotm(C2z)),('C3',rotm(C3))):
        g[name]=C.psg_sign(f,u)
    I=lambda *ns: rel([g[n] if not n.endswith("'") else inv(*g[n[:-1]]) for n in ns])
    I1=I('Tx','Ty',"Tx'","Ty'")
    I2=I('C4z','Tz',"C4z'","Tz'")
    I3=I('C2z','Tx',"C2z'",'Tx')
    print({k:('pi' if v else '0') for k,v in F.items()}, 'TxTy comm',I1,' C4z.Tz.C4z^-1.Tz^-1',I2,' C2z.Tx.C2z^-1.Tx',I3)
