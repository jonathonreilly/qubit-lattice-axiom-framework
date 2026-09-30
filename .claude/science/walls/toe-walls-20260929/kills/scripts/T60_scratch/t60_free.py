"""T60 tests A1, A2(free), A3, A4, A6 on the free walker sea. Numbers only.
Units: hop = 1 with E(k) = |sin k| at ell = 1, which the scale primitive makes 1 = M_Pl (E_P).
Run: python3 t60_free.py > t60_free_output.txt
"""
import numpy as np, itertools, math

np.set_printoptions(linewidth=140)

# ---------- constants (SI / GeV) ----------
lP = 1.616255e-35            # m
hbar_c_eV_m = 1.973269804e-7 # eV m
MPl_eV = 1.220890e28         # eV  (non-reduced)
rho_ratio_obs = 1.1e-123     # the wall's own rho_Lambda / rho_Planck (checked below)
# check the ratio from Planck-2018-like inputs
G = 6.67430e-11; c = 2.99792458e8; hbar = 1.054571817e-34
H0 = 67.4e3/3.0856775814913673e22
OmL = 0.685
rho_c = 3*H0**2/(8*np.pi*G)            # kg/m^3
rho_L_J = OmL*rho_c*c**2               # J/m^3
rho_P_J = c**7/(hbar*G**2)             # J/m^3
print("A0 rho_Lambda/rho_P from H0=67.4, OmL=0.685: %.3e (wall quotes 1.1e-123)" % (rho_L_J/rho_P_J))

# ---------- A1: log-det per cell ----------
def logdet_cell(m, N=40):
    P = (np.arange(N)+0.5)*2*np.pi/N
    s2 = np.sin(P/2)**2
    tot = 0.0
    # 4D sum of sin^2 via broadcasting in chunks
    S = (s2[:,None,None,None]+s2[None,:,None,None]+s2[None,None,:,None]+s2[None,None,None,:])
    return -np.mean(np.log(m*m+S))
print("\nA1 log-det per cell eps_vac = -<log(m^2 + sum sin^2(P/2))>_BZ (N=40^4)")
for m in (0.3,0.7,1.0):
    print("   m=%.1f  eps_vac = %.4f   (June note: -0.667,-0.866,-1.068)" % (m, logdet_cell(m)))

def I3_grid(N):
    k = (np.arange(N)+0.5)*2*np.pi/N
    s2 = np.sin(k)**2
    acc = 0.0
    for i in range(N):
        a = s2[i] + s2[:,None] + s2[None,:]
        acc += np.sqrt(a).sum()
    return acc/N**3
print("\nA1 I(inf) = <|s|>_BZ (3D), midpoint grids")
for N in (64,128,256):
    print("   N=%d  I=%.6f" % (N, I3_grid(N)))
I_inf = I3_grid(256)
I4 = (3+3*np.sqrt(2)+np.sqrt(3))/8
print("   probe 6 quotes E_0 = -1.19380; T03 cost per record 2<|s|> = 2.387602 -> 2*I_inf = %.6f" % (2*I_inf))
print("   I(4^3) closed form (3+3sqrt2+sqrt3)/8 = %.6f" % I4)

# real-space 4^3 diagonalisation of sigma.sin(k) walk
def walker_H(L, ell=1.0, mass=0.0):
    N = L**3
    idx = lambda x,y,z: ((x%L)*L+(y%L))*L+(z%L)
    sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]],complex), np.array([[1,0],[0,-1]],complex)]
    H = np.zeros((2*N,2*N),complex)
    for x,y,z in itertools.product(range(L),repeat=3):
        i = idx(x,y,z)
        for j,(dx,dy,dz) in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
            jn = idx(x+dx,y+dy,z+dz)
            # (sigma_j/(2i)) (S_j - S_j^dag): amplitude to hop forward and backward
            blk = sig[j]/(2j)
            H[2*i:2*i+2, 2*jn:2*jn+2] += blk
            H[2*jn:2*jn+2, 2*i:2*i+2] += blk.conj().T
    return H/ell
H = walker_H(4)
ev = np.linalg.eigvalsh(H)
print("   real-space 4^3: sum of negative eigenvalues / N = %.6f (closed form -%.6f)" % (ev[ev<0].sum()/64, I4))

# ---------- A2 (free): equation of state by finite difference ----------
def Esea(L, ell):
    e = np.linalg.eigvalsh(walker_H(L,ell))
    return e[e<0].sum()          # total, N=L^3 sites
L=4; N=L**3; h=1e-3
E0 = Esea(L,1.0); Ep = Esea(L,1+h); Em = Esea(L,1-h)
dE_dl = (Ep-Em)/(2*h)
dV_dl = 3*N*1.0**2
p = -dE_dl/dV_dl; rho = E0/N
print("\nA2 free massless sea on 4^3: rho=%.6f  p=%.6f  p/rho=%.6f (prediction 1/3)" % (rho,p,p/rho))

# massive staggered block: E = sqrt(mu^2 + s^2/ell^2), average over 4^3 zone points
def mass_sea_per_site(mu, ell, L=4):
    k = 2*np.pi*np.arange(L)/L
    s2 = np.sin(k)**2
    S = s2[:,None,None]+s2[None,:,None]+s2[None,None,:]
    return -np.mean(np.sqrt(mu**2 + S/ell**2))
for mu in (0.0, 0.3, 1.0, 3.0):
    e0 = mass_sea_per_site(mu,1.0)
    de = (mass_sea_per_site(mu,1+h)-mass_sea_per_site(mu,1-h))/(2*h)
    p = -de/3.0
    print("   massive mu=%.1f: rho=%.6f p/rho=%.6f (in [0,1/3])" % (mu, e0, p/e0 if mu>0 else p/e0))

# ---------- A3 dilution bounds ----------
print("\nA3 dilution bounds (I=%.4f)" % I_inf)
ell_need = (I_inf/rho_ratio_obs)**0.25
print("   (a) stretch: ell_needed = %.3e l_P = %.3e m  (LHC reach 1e-19 m; gravity tests 5.2e-5 m)" % (ell_need, ell_need*lP))
print("       mismatch in length vs 1e-19 m: %.1f decades" % np.log10(ell_need*lP/1e-19))
for a_m, lab in ((1e-19,"a=1e-19 m (~2 TeV lattice)"),(1e-18,"a=1e-18 m"),(1e-15,"a=1e-15 m")):
    E_lat_eV = hbar_c_eV_m/a_m
    rho = I_inf*(E_lat_eV/MPl_eV)**4
    print("   (b) coarse lattice %s: E_lat=%.3e eV, |rho_sea|/rho_P = %.2e  (target 1.1e-123: %.1f decades too big)" % (lab, E_lat_eV, rho, np.log10(rho/rho_ratio_obs)))
Rc = 4.4e26/lP
V_obs = 4/3*np.pi*Rc**3
print("   (c) empty-born growth: sea energy fixed; need volume ratio %.1e; sites in comoving observable volume ~ %.1e (R=%.2e l_P)" % (I_inf/rho_ratio_obs, V_obs, Rc))
print("       => margin %.1f decades if the initial patch is O(1) cells" % (np.log10(V_obs) - np.log10(I_inf/rho_ratio_obs)))

# ---------- A4 records-only (pinched) source ----------
print("\nA4 records-only (pinched) source: sea residual r(m) = -(m^2/2) <1/sqrt(m^2 + s^2)>")
# verify the KS real-space formula against the 09-04 note: 12^3, m=1 -> -0.200917464424
def KS_M(L):
    N=L**3
    idx=lambda x,y,z:((x%L)*L+(y%L))*L+(z%L)
    M=np.zeros((N,N))
    for x,y,z in itertools.product(range(L),repeat=3):
        i=idx(x,y,z)
        eta=[1,(-1)**x,(-1)**(x+y)]
        for j,(dx,dy,dz) in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
            jn=idx(x+dx,y+dy,z+dz)
            M[i,jn]+=eta[j]/2; M[jn,i]+=eta[j]/2
    return M
M12=KS_M(12); lam=np.linalg.eigvalsh(M12)
r12=-(1.0/2)*np.mean(1/np.sqrt(lam**2+1.0))
print("   12^3 real space, walker units (hop 1/2, E=|sin k|), m=1: r_v = %.9f" % r12)
lam2=2*lam   # the 09-04 note's KS matrix has hop amplitude 1 (E^2 = m^2 + sum(2-2cos p)), i.e. 2x ours
r12n=-(1.0/2)*np.mean(1/np.sqrt(lam2**2+1.0))
print("   12^3 real space, note's units (hop 1), m=1: r_v = %.9f   (09-04 note: -0.200917464424)" % r12n)
# momentum-space J(m) on a large grid: symbol <1/sqrt(m^2+sum sin^2 k)>
def J3(m,N=192):
    k=(np.arange(N)+0.5)*2*np.pi/N; s2=np.sin(k)**2
    acc=0.0
    for i in range(N):
        a=s2[i]+s2[:,None]+s2[None,:]
        acc+=(1/np.sqrt(m*m+a)).sum()
    return acc/N**3
print("   momentum-space check J(1)=%.6f -> r=%.6f (infinite lattice)" % (J3(1.0), -0.5*J3(1.0)))
J0=J3(1e-9,N=192)
print("   J(0)=<1/|s|> = %.4f  (converges; small-m: r ~ -(m^2/2)*J0)" % J0)
species = {"top (173 GeV)":173e9, "electron":0.511e6, "heaviest neutrino ~0.05 eV":0.05}
for name,m_eV in species.items():
    m=m_eV/MPl_eV
    res=0.5*m*m*J0
    print("   %-28s m/M_Pl=%.2e  |residual|/rho_P = %.2e  -> %.1f decades above 1.1e-123" % (name, m, res, np.log10(res/rho_ratio_obs)))
# pinched weight of a massless / massive eigenpacket (6^3)
L=6; M6=KS_M(L); N=L**3
Gam=np.diag([(-1)**(x+y+z) for x,y,z in itertools.product(range(L),repeat=3)]).astype(float)
for m in (0.0,0.5):
    Hm=M6+m*Gam
    w,v=np.linalg.eigh(Hm)
    pos=np.where(w>1e-9)[0]
    j=pos[len(pos)//2]; psi=v[:,j]; E=w[j]
    full=psi@Hm@psi
    pinched=np.sum(np.diag(Hm)*psi**2)
    print("   packet at E=%.4f m=%.1f: <H>=%.4f, <D(H)>=%.4f, retained=%.4f (pred m^2/E^2=%.4f)" % (E,m,full,pinched,pinched/full,(m/E)**2))
# scale-free counting residual: d eps/d log ell = -2 mu^2 < 1/(mu^2 + sum sin^2(P/2)) > , 4D
def J4(mu,N=40):
    P=(np.arange(N)+0.5)*2*np.pi/N; s2=np.sin(P/2)**2
    S=(s2[:,None,None,None]+s2[None,:,None,None]+s2[None,None,:,None]+s2[None,None,None,:])
    return np.mean(1/(mu*mu+S))
print("   scale-free (lapse-tied) reading: overall-scale response per cell = 2 mu^2 J4(mu); J4(1e-3)=%.3f" % J4(1e-3))

# ---------- A6 no equilibrium ----------
print("\nA6 stationary point of total energy per site E(ell)=m0 + e_sea(ell)?")
ells = np.linspace(0.2,50,2000)
for mu in (0.0,0.01,0.3,1.0):
    Es = np.array([mass_sea_per_site(mu,l) for l in ells])
    dE = np.gradient(Es, ells)
    print("   mu=%.2f: min dE/dell = %.3e, max = %.3e  (sign change? %s)" % (mu, dE.min(), dE.max(), bool((dE.min()<0)and(dE.max()>0))))
