import numpy as np, itertools
def ring_full(L,m,V,s1=1,s2=1,d=2):
    # psi-gauge walker: h = s*S + m*eps, S=(T-T^-1)/(2i), (T psi)(x)=psi(x-1)
    # distinguishable, exclusion x1!=x2, V at |x1-x2|=d (mod L both ways)
    idx={}
    for a in range(L):
        for b in range(L):
            if a!=b: idx[(a,b)]=len(idx)
    n=len(idx); H=np.zeros((n,n),complex)
    def h1(s):
        h=np.zeros((L,L),complex)
        for x in range(L):
            # (S psi)(x) = (psi(x-1)-psi(x+1))/(2i)
            h[x,(x-1)%L]+=s/(2j); h[x,(x+1)%L]-=s/(2j)
            h[x,x]+=m*(-1)**x
        return h
    ha,hb=h1(s1),h1(s2)
    for (a,b),i in idx.items():
        for a2 in range(L):
            if ha[a,a2]!=0 and (a2,b) in idx: H[i,idx[(a2,b)]]+=ha[a,a2]
        for b2 in range(L):
            if hb[b,b2]!=0 and (a,b2) in idx: H[i,idx[(a,b2)]]+=hb[b,b2]
        r=(a-b)%L
        if r==d or r==L-d: H[i,i]+=V
    return np.linalg.eigvalsh(H)
def fiber(N,K,m,V,d=2,phigauge=True):
    # phi-gauge, equal coins s=+1 hop -1/2 ; w=(w+,w-) basis, r=1..N
    n=2*N; H=np.zeros((n,n),complex)
    c0,s0=np.cos(K/2),np.sin(K/2)
    Bm=np.diag([-c0,1j*s0]); 
    for r in range(1,N+1):
        i=2*(r-1)
        if r%2==0:
            H[i,i+1]+=2*m; H[i+1,i]+=2*m
        if r==d: H[i,i]+=V; H[i+1,i+1]+=V
        if r<N:
            j=2*r
            H[i:i+2,j:j+2]+=Bm
            H[j:j+2,i:i+2]+=Bm.conj().T
    return np.linalg.eigvalsh(H)
if __name__=="__main__":
    L=12;m=0.8;V=-0.9
    full=np.sort(ring_full(L,m,V))
    # sectors
    allf=[]
    for j in range(L):
        K=2*np.pi*j/L
        allf+=list(fiber(L-1,K,m,V))
    # note: j and j+L/2 : K and K+pi ; fiber for K in [0,2pi): check count
    allf=np.sort(allf)
    print(len(full),len(allf))
    print(full[:6]);print(allf[:6])
