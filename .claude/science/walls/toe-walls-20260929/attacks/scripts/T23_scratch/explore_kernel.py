import numpy as np, itertools
L=4
idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
N=L**3
D=np.zeros((N,N))
for x,y,z in itertools.product(range(L),repeat=3):
    eta=[1,(-1)**x,(-1)**(x+y)]
    for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
        i=idx(x,y,z); jp=idx(x+e[0],y+e[1],z+e[2]); jm=idx(x-e[0],y-e[1],z-e[2])
        D[i,jp]+=eta[mu]/2; D[i,jm]-=eta[mu]/2
print("antisym", np.allclose(D,-D.T))
u,s,vt=np.linalg.svd(D)
print("rank",(s>1e-9).sum(),"kernel dim",(s<1e-9).sum())
K=vt[s<1e-9].T
# characterise: support structure
P=K@K.T
print("proj diag range",P.diagonal().min(),P.diagonal().max())

# search corner waves v_c(x) = (-1)^{c.x} * xi(x), xi = (-1)^{q(x)}, q quadratic form over Z2 in bits of x mod 2
pts=list(itertools.product(range(L),repeat=3))
def vec(f):
    v=np.zeros(N)
    for p in pts: v[idx(*p)]=f(*p)
    return v
found=[]
for coeffs in itertools.product([0,1],repeat=6):
    a12,a13,a23,l1,l2,l3=coeffs
    def xi(x,y,z):
        b=[x%2,y%2,z%2]
        q=a12*b[0]*b[1]+a13*b[0]*b[2]+a23*b[1]*b[2]+l1*b[0]+l2*b[1]+l3*b[2]
        return (-1)**q
    v=vec(xi)
    r=np.linalg.norm(v-P@v)
    if r<1e-9: found.append(coeffs)
print("xi candidates in kernel:",found)
