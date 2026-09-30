"""Independent brute-force count of gauge-neutral many-body states for N_g generations of the base x fibre C^8,
k particles.  Modes are the weight basis: quark modes (colour c=0..2, weak w=0,1), lepton modes (w=0,1).
Singlet count = dim of joint kernel of all 12 generators, computed on the zero-weight subspace only."""
import sys, itertools, numpy as np, scipy.sparse as sp
Ng=int(sys.argv[1]); ks=[int(x) for x in sys.argv[2:]]
# single-particle modes per generation: ('q',c,w) c in 0..2, w in 0,1 ; ('l',w)
modes1=[('q',c,w) for c in range(3) for w in range(2)]+[('l',None,w) for w in range(2)]
modes=[(g,)+m for g in range(Ng) for m in modes1]
n=len(modes)
# Gell-Mann/2 on colour index; sigma/2 on weak index; Y
gm=[np.array(m,dtype=complex) for m in (
 [[0,1,0],[1,0,0],[0,0,0]],[[0,-1j,0],[1j,0,0],[0,0,0]],[[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]],[[0,0,-1j],[0,0,0],[1j,0,0]],[[0,0,0],[0,0,1],[0,1,0]],
 [[0,0,0],[0,0,-1j],[0,1j,0]],(np.diag([1,1,-2])/np.sqrt(3)).tolist())]
gm=[g/2 for g in gm]
sg=[np.array([[0,1],[1,0]])/2,np.array([[0,-1j],[1j,0]])/2,np.array([[1,0],[0,-1]])/2]
idx={m:i for i,m in enumerate(modes)}
def gen_colour(a):
    M=sp.lil_matrix((n,n),dtype=complex)
    for g in range(Ng):
        for w in range(2):
            for c in range(3):
                for c2 in range(3):
                    if abs(gm[a][c,c2])>1e-14: M[idx[(g,'q',c,w)],idx[(g,'q',c2,w)]]=gm[a][c,c2]
    return M.tocsr()
def gen_weak(a):
    M=sp.lil_matrix((n,n),dtype=complex)
    for g in range(Ng):
        for w in range(2):
            for w2 in range(2):
                if abs(sg[a][w,w2])>1e-14:
                    for c in range(3): M[idx[(g,'q',c,w)],idx[(g,'q',c,w2)]]=sg[a][w,w2]
                    M[idx[(g,'l',None,w)],idx[(g,'l',None,w2)]]=sg[a][w,w2]
    return M.tocsr()
Ymat=np.zeros(n)
for i,m in enumerate(modes): Ymat[i]=1/3 if m[1]=='q' else -1.0
onebody=[gen_colour(a) for a in range(8)]+[gen_weak(a) for a in range(3)]
# weights (diagonal generators): colour 3,8 ; weak 3 ; Y
w_T3=np.array([gm[2][m[2],m[2]].real if m[1]=='q' else 0 for m in modes])
w_T8=np.array([gm[7][m[2],m[2]].real if m[1]=='q' else 0 for m in modes])
w_J3=np.array([sg[2][m[3],m[3]].real for m in modes])
def apply_onebody(M, states, table):
    """sum M_ij c_i^dag c_j on each state in `states` (int bitmasks); returns sparse matrix (dim_sector x len(states))"""
    Mc=M.tocoo(); rows=[];cols=[];vals=[]
    for col,st in enumerate(states):
        for i,j,v in zip(Mc.row,Mc.col,Mc.data):
            if not (st>>j)&1: continue
            if i!=j and (st>>i)&1: continue
            s1=bin(st&((1<<j)-1)).count('1')
            st2=st&~(1<<j)
            s2=bin(st2&((1<<i)-1)).count('1')
            st3=st2|(1<<i)
            rows.append(table[st3]);cols.append(col);vals.append(v*(-1)**(s1+s2))
    return sp.csr_matrix((vals,(rows,cols)),shape=(len(table),len(states)),dtype=complex)
for k in ks:
    combos=list(itertools.combinations(range(n),k))
    masks=[sum(1<<i for i in c) for c in combos]
    table={m:i for i,m in enumerate(masks)}
    W=np.zeros((len(combos),4))
    for r,c in enumerate(combos):
        c=list(c)
        W[r]=[w_T3[c].sum(),w_T8[c].sum(),w_J3[c].sum(),Ymat[c].sum()]
    zero=np.where(np.abs(W).max(axis=1)<1e-9)[0]
    zs=[masks[i] for i in zero]
    S=sp.csr_matrix((len(zs),len(zs)),dtype=complex)
    for M in onebody:
        A=apply_onebody(M,zs,table)      # (dim x Z)
        S=S+(A.conj().T@A)
    ev=np.linalg.eigvalsh(S.toarray()) if len(zs)>0 else np.array([])
    print(f"N_g={Ng} k={k}: sector dim {len(combos)}, zero-weight dim {len(zs)}, gauge singlets = {int((ev<1e-8).sum())}",flush=True)
