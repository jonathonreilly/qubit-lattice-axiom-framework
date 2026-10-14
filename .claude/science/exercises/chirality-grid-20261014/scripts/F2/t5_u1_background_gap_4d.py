"""T5: min |eig H_W| (Wilson M=1, r=1) in Gaussian weak-coupling U(1) backgrounds on 6^4."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
rng = np.random.default_rng(20261014)
L = 6; V = L**4
s1 = np.array([[0,1],[1,0]],complex); s2 = np.array([[0,-1j],[1j,0]],complex); s3 = np.array([[1,0],[0,-1]],complex); I2=np.eye(2)
# chiral basis: gamma_k = [[0, -i s_k],[i s_k, 0]], gamma_4 = [[0,1],[1,0]], gamma5 = diag(1,-1)
Z = np.zeros((2,2))
gam = [np.block([[Z, -1j*s],[1j*s, Z]]) for s in (s1,s2,s3)] + [np.block([[Z, I2],[I2, Z]])]
g5 = np.block([[I2, Z],[Z, -I2]])
for a in range(4):
    for b in range(4):
        assert np.allclose(gam[a]@gam[b]+gam[b]@gam[a], 2*(a==b)*np.eye(4))
    assert np.allclose(gam[a]@g5+g5@gam[a], 0)
coords = np.array(np.unravel_index(np.arange(V), (L,)*4)).T
def site(c): return np.ravel_multi_index(tuple(np.mod(c, L).T), (L,)*4)
def gauge_angles(g):
    k = 2*np.pi*np.fft.fftfreq(L)
    K = np.meshgrid(k,k,k,k, indexing='ij')
    phat2 = sum(4*np.sin(kk/2)**2 for kk in K)
    th = []
    for mu in range(4):
        noise = rng.normal(size=(L,)*4) + 1j*rng.normal(size=(L,)*4)
        amp = np.zeros_like(phat2); amp[phat2>0] = 1/np.sqrt(phat2[phat2>0])
        A = np.real(np.fft.ifftn(noise*amp))*np.sqrt(V)/np.sqrt(2)*np.sqrt(2)
        th.append(g*A.reshape(-1))
    return th
def HW(th, M=1.0, r=1.0):
    rows=[]; cols=[]; vals=[]
    def add(i,j,blk):
        for a in range(4):
            for b in range(4):
                if blk[a,b]!=0: rows.append(4*i+a); cols.append(4*j+b); vals.append(blk[a,b])
    for x in range(V):
        add(x,x,(4*r-M)*np.eye(4))
        for mu in range(4):
            e = np.zeros(4,int); e[mu]=1
            y = site(coords[x]+e)
            u = np.exp(1j*th[mu][x])
            add(x,y,-0.5*(r*np.eye(4)-gam[mu])*u)
            add(y,x,-0.5*(r*np.eye(4)+gam[mu])*np.conj(u))
    D = sp.csr_matrix((vals,(rows,cols)),shape=(4*V,4*V))
    G5 = sp.kron(sp.eye(V), sp.csr_matrix(g5))
    return (G5@D).tocsc()
for g in (0.0, 0.5, 0.65):
    lm = []
    ncfg = 1 if g == 0 else 8
    for c in range(ncfg):
        th = gauge_angles(g) if g>0 else [np.zeros(V)]*4
        H = HW(th)
        assert abs(H - H.getH()).max() < 1e-12
        w = sla.eigsh(H, k=6, sigma=0.0, which='LM', return_eigenvectors=False)
        wmax = sla.eigsh(H, k=1, which='LM', return_eigenvectors=False)
        lm.append((np.min(np.abs(w)), np.max(np.abs(wmax))))
        plaq = None
    lmins = [a for a,b in lm]; lmaxs=[b for a,b in lm]
    print(f"g={g}: lam_min over cfgs = {np.round(lmins,4)}  min={min(lmins):.4f}  lam_max~{max(lmaxs):.3f}  kappa_min={min(lmins)/max(lmaxs):.4f}")
