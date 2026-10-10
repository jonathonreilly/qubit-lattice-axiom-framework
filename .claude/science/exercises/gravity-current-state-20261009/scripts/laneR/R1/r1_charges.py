# R1 check: any compactly supported change of a symmetric tensor field E on Z^3 changes
#  - scalar (fracton) charge rho = D_i D_j E_ij by zero total charge AND zero total dipole;
#  - vector charge rho_j = D_i E_ij by zero total vector charge AND zero angular charge sum x x rho.
# A record forming at one site adds +1 at one site (net monopole), so record count cannot be such a Gauss charge.
import numpy as np
rng=np.random.default_rng(5); L=16
def D(f,i):  # forward difference, open box (field zero outside)
    g=np.zeros_like(f); sl=[slice(None)]*3; sl2=[slice(None)]*3
    sl[i]=slice(0,L-1); sl2[i]=slice(1,L); g[tuple(sl)]=f[tuple(sl2)]-f[tuple(sl)]; g[tuple([slice(None)]*i+[slice(L-1,L)])]=-f[tuple([slice(None)]*i+[slice(L-1,L)])]
    return g
def Db(f,i):  # backward difference
    g=np.zeros_like(f); sl=[slice(None)]*3; sl2=[slice(None)]*3
    sl[i]=slice(1,L); sl2[i]=slice(0,L-1); g[tuple(sl)]=f[tuple(sl)]-f[tuple(sl2)]; g[tuple([slice(None)]*i+[slice(0,1)])]=f[tuple([slice(None)]*i+[slice(0,1)])]
    return g
X=np.indices((L,L,L)).astype(float)
for trial in range(3):
    E=np.zeros((3,3,L,L,L)); c=rng.integers(5,10,3)
    blk=rng.integers(-3,4,(3,3,3,3,3)); blk=blk+blk.transpose(1,0,2,3,4)
    E[:,:,c[0]:c[0]+3,c[1]:c[1]+3,c[2]:c[2]+3]=blk
    rho_s=sum(D(Db(E[i,j],i),j) for i in range(3) for j in range(3))
    rho_v=np.array([sum(Db(E[i,j],i) for i in range(3)) for j in range(3)])
    mono_s=rho_s.sum(); dip_s=[(X[k]*rho_s).sum() for k in range(3)]
    mono_v=rho_v.sum(axis=(1,2,3)); ang=[(X[a]*rho_v[b]-X[b]*rho_v[a]).sum() for a,b in [(0,1),(1,2),(0,2)]]
    print('trial',trial,'scalar: net',mono_s,'dipole',np.round(dip_s,9),'| vector: net',mono_v,'angular',np.round(ang,9))
print('one record formed at a site: net count +1 (monopole), dipole += x: not reachable by any compact E change')
