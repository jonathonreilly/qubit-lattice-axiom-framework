import numpy as np, itertools
N=9
# two hard-core bosons / fermions on a ring N; basis pairs i<j
st=[(i,j) for i in range(N) for j in range(i+1,N)]
idx={s:k for k,s in enumerate(st)}
def hop_bond(b,U,fer=True):
    # operator h_b acting on bond b=(b,b+1 mod N): hop + U n n
    n=len(st); M=np.zeros((n,n),complex)
    b2=(b+1)%N
    for s in st:
        i,j=s; k=idx[s]
        occ={i,j}
        if b in occ and b2 in occ: M[k,k]+=U
        elif (b in occ) != (b2 in occ):
            if b in occ: new=(occ-{b})|{b2}
            else: new=(occ-{b2})|{b}
            t=tuple(sorted(new)); sign=1
            M[idx[t],k]+=0.5*sign
    return M
for U in (0,0.7):
    h=[hop_bond(b,U) for b in range(N)]
    H=sum(h)
    Q=sum(1j*(h[b]@h[(b+1)%N]-h[(b+1)%N]@h[b]) for b in range(N))
    print(U,np.abs(H@Q-Q@H).max())
