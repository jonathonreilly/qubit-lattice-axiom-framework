"""R14-5 (a): the CMC lapse equation of the zero-mode-lapse model in lumpy matter.
   -D^2 N + Qt N = S(t),  <N> = 1,   Qt = K_ij K^ij + (kappa/2)(rho+3p)_nc - Lt(t)
Units c = H = 1 (lengths in c/H). EdS background: theta = 3, kappa*rhobar = 3, Lt = 0 -> Qbar = 3 + 1.5 = 4.5.
Lower bound used (sigma^2 >= 0 dropped): Qt(x) = 3 + 1.5 rho(x)/rhobar  (dust).
Flat 3-metric approximation for the Laplacian (weak field); Part C is a TOY beyond weak field.
A: 3D periodic box, lognormal density with extreme contrast; CG solve; min N, compare with Poisson potential.
B: spherical top-hat Delta = 200 (rel. to critical = background in EdS): N(0)-1 vs Newtonian Phi(0) = -0.75 delta R^2.
C: lapse collapse toy: fixed 'mass' (Q_in R^3 fixed), R -> 0: N(0) -> 0+ (positive by the maximum principle).
D: Yukawa range of the lapse Green's function, l = Qbar^{-1/2}, per era.
"""
import numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spl
rng = np.random.default_rng(14)
print("A. 3D periodic lumpy box")
for L, n, sig in [(0.05, 48, 2.0), (0.05, 48, 3.0), (1.0, 48, 3.0)]:
    h = L/n
    # Gaussian random field with power ~ k^-3 smoothed, then lognormal
    kx = np.fft.fftfreq(n, d=h)*2*np.pi
    KX, KY, KZ = np.meshgrid(kx, kx, kx, indexing='ij'); k2 = KX**2+KY**2+KZ**2; k2[0,0,0] = 1
    amp = 1/np.sqrt(k2**1.5)*np.exp(-k2*(2*h)**2); amp[0,0,0] = 0
    f = np.real(np.fft.ifftn(amp*(rng.normal(size=(n,n,n))+1j*rng.normal(size=(n,n,n)))))
    f = (f - f.mean())/f.std()*sig
    rho = np.exp(f); rho /= rho.mean()                      # rho/rhobar, mean 1
    Q = 3.0 + 1.5*rho
    e = np.ones(n); D1 = sps.diags([e, -2*e, e], [-1, 0, 1], shape=(n, n)).tolil(); D1[0, -1] = 1; D1[-1, 0] = 1
    D1 = D1.tocsr()/h**2; I = sps.identity(n)
    Lap = sps.kron(sps.kron(D1, I), I) + sps.kron(sps.kron(I, D1), I) + sps.kron(sps.kron(I, I), D1)
    A = (-Lap + sps.diags(Q.ravel())).tocsr()
    N1, info = spl.cg(A, np.ones(n**3), rtol=1e-12, maxiter=20000)
    N = N1/N1.mean()
    res = np.linalg.norm(A@N1 - 1)/np.sqrt(n**3)
    # Poisson potential for comparison: lap Phi = 1.5 (rho-1)
    dk = np.fft.fftn(1.5*(rho-1)); lapk = -(2*(np.cos(KX*h)+np.cos(KY*h)+np.cos(KZ*h)-3))/h**2; lapk[0,0,0] = 1
    Phi = np.real(np.fft.ifftn(-dk/lapk)); Phi -= Phi.mean()
    dN = N - 1
    corr = np.corrcoef(dN.ravel(), Phi.ravel())[0, 1]
    print(f"  L={L} c/H, n={n}, sigma_ln={sig}: rho/rhobar in [{rho.min():.2e}, {rho.max():.2e}]; CG info={info}, resid={res:.1e}")
    print(f"     N in [{N.min():.6f}, {N.max():.6f}]  (min N > 0: {N.min() > 0});  rms(N-1) = {dN.std():.3e}; rms(Phi) = {Phi.std():.3e}; corr(dN,Phi) = {corr:.4f}")
print("B. spherical top-hat Delta=200, flat-space radial solution (S = Qbar so N -> 1 far away)")
def tophat(R, Qin, Qo=4.5):
    S = Qo; ki, ko = np.sqrt(Qin), np.sqrt(Qo)
    # inside N = S/Qin + A sinh(ki r)/r ; outside N = 1 + B exp(-ko r)/r ; match N, N' at R
    f_in = lambda r: np.sinh(ki*r)/r; df_in = lambda r: ki*np.cosh(ki*r)/r - np.sinh(ki*r)/r**2
    f_o = lambda r: np.exp(-ko*r)/r; df_o = lambda r: -ko*np.exp(-ko*r)/r - np.exp(-ko*r)/r**2
    M = np.array([[f_in(R), -f_o(R)], [df_in(R), -df_o(R)]]); rhs = np.array([1 - S/Qin, 0.0])
    Acoef, B = np.linalg.solve(M, rhs)
    N0 = S/Qin + Acoef*ki            # sinh(ki r)/r -> ki as r -> 0
    NR = 1 + B*f_o(R)
    return N0, NR
for name, RH in [("cluster R=1.5 Mpc", 1.5/4400), ("galaxy R=0.25 Mpc", 0.25/4400)]:
    delta = 199.0; Qin = 3 + 1.5*(1+delta)
    N0, NR = tophat(RH, Qin)
    print(f"  {name}: RH={RH:.2e}: N(0)-1 = {N0-1:+.4e}; Newtonian Phi(0) = -0.75*delta*R^2 = {-0.75*delta*RH**2:+.4e}; N(R)-1 = {NR-1:+.4e}")
print("C. lapse-collapse TOY (flat 3-metric): fixed mass mu = 1.5*delta*R^3 = 1e-6, R decreasing")
mu = 1e-6
for R in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]:
    delta = mu/(1.5*R**3); Qin = 3 + 1.5*(1+delta)
    N0, NR = tophat(R, Qin)
    print(f"  R={R:.0e}: compactness Q_in R^2 = {Qin*R**2:.2e}: N(0) = {N0:.4e}, N(R) = {NR:.6f}  (positive: {N0 > 0})")
print("D. Yukawa range l = Qbar^-1/2 of the lapse Green's function (instantaneous on the slice)")
for era, Qb in [("radiation", 3 + 3.0), ("EdS matter", 3 + 1.5), ("today, Om=0.3, w=-0.95 smooth DE", 3 + 1.5*(0.3 + 0.7*(1 + 3*(-0.95))))]:
    print(f"  {era}: Qbar = {Qb:.3f} H^2 -> l = {1/np.sqrt(Qb):.3f} c/H")
print("   sufficient positivity: Qt(x) >= kappa*rhobar_nc + (kappa/2)(rho+3p)_nc(x) (Lt = 0); dust/radiation >= 0; smooth DE gives (3/2)(1+w) rho_DE >= 0 iff w >= -1")
w_of_a = lambda a, w0=-0.75, wa=-0.86: w0 + wa*(1 - a)
for a in [1.0, 0.7, 0.5, 0.33]:
    # CPL density ratio and Qt lower bound at the void floor rho_m(x) = 0 (worst case), Om0 = 0.3
    from scipy.integrate import quad
    w0, wa = -0.75, -0.86
    rde = 0.7*a**(-3*(1 + w0 + wa))*np.exp(-3*wa*(1 - a)); rm = 0.3*a**-3
    Qmin = 3*(rm + rde) + 1.5*(0 + rde*(1 + 3*w_of_a(a)))   # theta^2/3 = 3H^2 = 3(rm+rde) with kappa rho in units 3H0^2
    print(f"   DESI-CPL a={a}: w={w_of_a(a):+.3f}, Qt_min(void, rho_m=0)/(3H0^2 units) = {Qmin:.4f} (>0: {Qmin > 0})")
