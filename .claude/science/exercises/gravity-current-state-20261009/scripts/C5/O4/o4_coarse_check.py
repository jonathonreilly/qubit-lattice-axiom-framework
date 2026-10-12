# Check: sum over cubic cells (size L) of L^3 * <dPhi>_cell^2, dPhi = 1/|x-a|-1/|x-b|, |a-b|=d<<L,
# vs far-field estimate (4 pi/3) d^2 / L. Units G m = 1.
import numpy as np
def cell_avg(center, L, pts, n=8):
    g,w=np.polynomial.legendre.leggauss(n); g=g*L/2; w=w/2
    X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); W=(w[:,None,None]*w[None,:,None]*w[None,None,:])
    out=[]
    for p in pts:
        r=np.sqrt((center[0]+X-p[0])**2+(center[1]+Y-p[1])**2+(center[2]+Z-p[2])**2)
        out.append(np.sum(W/r))
    return out[0]-out[1]
def total(L,d,off,R=40,nnear=3):
    a=np.array(off)+np.array([d/2,0,0]); b=np.array(off)-np.array([d/2,0,0])
    s=0.0
    rng=range(-R,R+1)
    for i in rng:
        for j in rng:
            for k in rng:
                c=np.array([i*L,j*L,k*L])
                if max(abs(i),abs(j),abs(k))<=nnear:
                    n=24 if max(abs(i),abs(j),abs(k))<=1 else 10
                    v=cell_avg(c,L,[a,b],n)
                else:
                    v=1/np.linalg.norm(c-a)-1/np.linalg.norm(c-b)
                s+=L**3*v*v
    # tail beyond R*L: dipole d cos/r^2 -> (4pi/3) d^2 / (R L)
    s+= (4*np.pi/3)*d**2/((R+0.5)*L)
    return s
for d in [0.01,0.05]:
    for off in [(0.0,0.0,0.0),(0.23,0.11,0.07),(0.45,0.3,0.0)]:
        L=1.0
        t=total(L,d,off,R=25)
        print(f"d={d}, offset={off}: sum={t:.4e}, (4pi/3)d^2/L={(4*np.pi/3)*d**2/L:.4e}, ratio={t/((4*np.pi/3)*d**2/L):.3f}")
