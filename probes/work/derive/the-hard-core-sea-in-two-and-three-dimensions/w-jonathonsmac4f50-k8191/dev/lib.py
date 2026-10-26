import numpy as np, itertools, math
import scipy.sparse as sp
import scipy.sparse.linalg as sla

def torus_bonds(dims):
    """sites indexed x + L0*y + L0*L1*z ; returns list of (a,b,dir,t) with t = signed real hop of gauged model
    (x-link 1/2, y-link (-1)^x /2, z-link (-1)^(x+y) /2), a=site, b=site+e_dir (periodic)."""
    d=len(dims); n=int(np.prod(dims))
    def idx(c):
        i=0; m=1
        for k in range(d):
            i+=c[k]*m; m*=dims[k]
        return i
    bonds=[]
    for c in itertools.product(*[range(L) for L in dims][::-1]):
        c=c[::-1]
        for j in range(d):
            c2=list(c); c2[j]=(c2[j]+1)%dims[j]
            sign=1
            if j>=1: sign=(-1)**(sum(c[:j]))
            bonds.append((idx(c),idx(c2),j,sign*0.5,c))
    return n,bonds

def combos(n,N):
    return [sum(1<<i for i in cmb) for cmb in itertools.combinations(range(n),N)]

def build_sector(n,bonds,N,Nup,fermion,wts=None):
    """Hard-core Hamiltonian (gauged, real) in sector N records, Nup up-coins. code = occ | up<<n.
    wts: optional dict bond_index -> multiplicative weight. returns sparse csr and sorted codes."""
    occs=np.array(combos(n,N),dtype=np.int64)
    codes=[]
    # for each occ choose which Nup of the N occupied sites are up
    for occ in occs:
        sites=[i for i in range(n) if occ>>i &1]
        for sub in itertools.combinations(sites,Nup):
            up=0
            for s in sub: up|=1<<s
            codes.append(int(occ)|(up<<n))
    codes=np.array(sorted(codes),dtype=np.int64)
    dim=len(codes)
    mask=(1<<n)-1
    occ=codes&mask; up=codes>>n
    rows=[];cols=[];vals=[]
    for bi,(a,b,j,t,c) in enumerate(bonds):
        w=1.0 if wts is None else wts[bi]
        lo,hi=min(a,b),max(a,b)
        between=((1<<hi)-1) & ~((1<<(lo+1))-1)
        for (s,e) in ((a,b),(b,a)):
            sel=np.nonzero(((occ>>s)&1==1)&((occ>>e)&1==0))[0]
            if len(sel)==0: continue
            o=occ[sel]; u=up[sel]
            isup=(u>>s)&1
            o2=o^(1<<s)^(1<<e)
            u2=u^(isup*((1<<s)^(1<<e)))
            c2=o2|(u2<<n)
            col=sel
            row=np.searchsorted(codes,c2)
            if fermion:
                x=o&between
                # popcount parity
                x=x^(x>>32); x=x^(x>>16); x=x^(x>>8); x=x^(x>>4); x=x^(x>>2); x=x^(x>>1)
                sg=1-2*(x&1)
            else:
                sg=np.ones(len(sel),dtype=np.int64)
            rows.append(row);cols.append(col);vals.append(t*w*sg)
    r=np.concatenate(rows);cc=np.concatenate(cols);v=np.concatenate(vals)
    H=sp.csr_matrix((v,(r,cc)),shape=(dim,dim))
    return H,codes
