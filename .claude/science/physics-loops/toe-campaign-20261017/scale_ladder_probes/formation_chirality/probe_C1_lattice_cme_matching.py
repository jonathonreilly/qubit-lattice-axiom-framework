"""Probe C1 (scale ladder, handedness lane).  Supplied textbook two-band
lattice Weyl model on Z^3 (one qubit-like 2-component mode per site):
  H(k) = sin kx sx + sin ky sy + (cos kz - cos k0 + m(2 - cos kx - cos ky)) sz + lam sin kz * 1
Nodes at (0,0,+-k0) with opposite chirality; lam sin kz is a parity-odd
(inversion-odd) texture that splits node energies by 2 lam sin k0 (a 'mu5').
Put a uniform B along z (Landau gauge, flux 2pi p/q per plaquette), half filling
E_F = 0, and compute the equilibrium current density j_z.
Continuum (IR rung) Weyl EFT with node chemical potentials predicts
   j_z = sum_chi chi mu_chi B / (4 pi^2)  (chiral magnetic effect).
UV (lattice rung) prediction: j_z = 0 exactly (kz periodic).  Decompose the
lattice current into the near-node kz window and the rest of the zone.
Also: chirality of each node from Berry flux (sum must vanish, Nielsen-Ninomiya)."""
import numpy as np
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1.]).astype(complex); I2=np.eye(2)
m,k0,lam = 1.0, np.pi/2, 0.3

def hk(k):
    kx,ky,kz=k
    return np.sin(kx)*sx+np.sin(ky)*sy+(np.cos(kz)-np.cos(k0)+m*(2-np.cos(kx)-np.cos(ky)))*sz+lam*np.sin(kz)*I2

def berry_flux(center, r=0.05, n=40):
    # lower-band Berry flux through small sphere (Fukui-Hatsugai on theta-phi grid)
    th=np.linspace(1e-4,np.pi-1e-4,n); ph=np.linspace(0,2*np.pi,n,endpoint=False)
    U=np.empty((n,n,2),complex)
    for i,t in enumerate(th):
        for j,p in enumerate(ph):
            k=center+r*np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])
            w,v=np.linalg.eigh(hk(k)); U[i,j]=v[:,0]
    F=0
    for i in range(n-1):
        for j in range(n):
            j2=(j+1)%n
            a=np.vdot(U[i,j],U[i+1,j])*np.vdot(U[i+1,j],U[i+1,j2])*np.vdot(U[i+1,j2],U[i,j2])*np.vdot(U[i,j2],U[i,j])
            F+=np.angle(a)
    return F/(2*np.pi)

chis={s: round(berry_flux(np.array([0,0,s*k0])),4) for s in (+1,-1)}
print('node chiralities (lower band Berry flux) at kz=+k0,-k0:', chis, ' sum =', round(sum(chis.values()),6))
Enode={s: lam*np.sin(s*k0) for s in (+1,-1)}
print('node energies:', Enode)

def Hmag(kx,ky,kz,q,p=1):
    B=2*np.pi*p/q; H=np.zeros((2*q,2*q),complex); D=np.zeros((2*q,2*q),complex)
    for x in range(q):
        kyx=ky+B*x
        blk=np.sin(kyx)*sy+(np.cos(kz)-np.cos(k0)+m*(2-np.cos(kyx)))*sz+lam*np.sin(kz)*I2
        H[2*x:2*x+2,2*x:2*x+2]+=blk
        D[2*x:2*x+2,2*x:2*x+2]=-np.sin(kz)*sz+lam*np.cos(kz)*I2   # dH/dkz
        xp=(x+1)%q; ph=np.exp(1j*kx*q) if x==q-1 else 1.0
        hop=(1/(2j))*sx - (m/2)*sz          # coefficient of |x+1><x| part: sin kx sx -> (T - T^dag)/(2i), -m cos kx sz -> -(m/2)(T+T^dag)
        H[2*xp:2*xp+2,2*x:2*x+2]+=hop*ph
        H[2*x:2*x+2,2*xp:2*xp+2]+=(hop*ph).conj().T
    return H,D,B

def current(q, nkx=4, nky=None, nkz=400, window=0.35):
    nky = nky or 2*q
    kxs=np.arange(nkx)*2*np.pi/q/nkx; kys=np.arange(nky)*2*np.pi/nky; kzs=-np.pi+np.arange(nkz)*2*np.pi/nkz
    tot=0.0; near=0.0
    for kz in kzs:
        s=0.0
        for kx in kxs:
            for ky in kys:
                H,D,B=Hmag(kx,ky,kz,q); w,v=np.linalg.eigh(H)
                occ=v[:,w<0]
                s+=np.real(np.einsum('in,ij,jn->',occ.conj(),D,occ))
        s/= (nkx*nky)
        tot+=s
        if min(abs(kz-k0),abs(kz+k0))<window: near+=s
    norm=1.0/(nkz*q)   # j = (1/q) * mean over magnetic-BZ grid (corrected)
    return tot*norm, near*norm, B

for q in (8,12,16,24,32):
    jt,jn,B=current(q)
    cme=sum(chis[s]*(0-Enode[s]) for s in (+1,-1))*B/(4*np.pi**2)
    print(f'ratio near/CME={jn/cme:+.3f}  ', end=''); print(f'q={q:2d} B={B:.4f}: lattice j_total={jt:+.3e}  near-node window={jn:+.3e}  rest={jt-jn:+.3e}  continuum CME (sign conv. Berry flux)={cme:+.3e}')
