"""R5-2 (D): 1+1 analog of LRL (Q = -7 n0^2 + n1^2, Gamma = <eps>, eps = 8+3 sqrt7, quotient = circle of length eta0 = ln eps).
Per-realization Gaussian sums as a function of the observer rapidity u over one full period (exact Haar average):
  T(u)  = sum_{v timelike future} phi_l      (retarded, f_m = 1 on ALL timelike shells)
  Tm(u) = sum_{v timelike future} m phi_l    (f_m = m)
  F(u)  = sum_{all v in L}       phi_l       (non-retarded, all vectors: Poisson => u-independent up to exp(-c l^2))
  S1(u) = shell m = 3 only (single orbit-family reference;  m=1,2 are not timelike: -1,-2 are QRs mod 7? see check)
Also checks the genus fact: timelike shells m (7 not | m) are exactly those with (m/7) = -1."""
import numpy as np
eta0 = np.log(8 + 3*np.sqrt(7))
def legendre7(m): r = m % 7; return 0 if r == 0 else (1 if r in (1, 2, 4) else -1)
# genus check on enumerated vectors
N = 1100
n0 = np.arange(-N, N+1); n1 = np.arange(-N, N+1)
A0, A1 = np.meshgrid(n0, n1, indexing='ij'); A0 = A0.ravel(); A1 = A1.ravel()
Q = -7*A0.astype(np.int64)**2 + A1.astype(np.int64)**2
ok = True
small = (np.abs(A0) < 120) & (np.abs(A1) < 320)
Qs = Q[small]
for q in np.unique(np.abs(Qs[(Qs != 0) & (np.abs(Qs) < 400)])):
    if q % 7 == 0: continue
    signs = set(np.sign(Qs[np.abs(Qs) == q]).tolist())
    pred = {-1} if legendre7(int(q)) == -1 else {1}
    if signs != pred: ok = False; print("genus check fails at", q, signs)
print("genus check (|Q|<400, 7 not| Q): sign(Q) = (|Q|/7) for every represented |Q|:", ok)
P0 = np.sqrt(7.0)*A0; P1 = A1.astype(float)
tl = (Q < 0) & (A0 > 0)
m = -Q
us = np.linspace(-eta0/2, eta0/2, 64, endpoint=False)
print(f"eta0 = {eta0:.6f}; frames = 64 rapidities over one period (exact Haar average on the circle)")
print("   l    sd_u[T]       sd_u[Tm]      sd_u[F]       sd_u[shell m=3]   mean T        (reach check)")
for l in (2, 3, 4, 6, 8, 11, 15, 20, 27, 36):
    if 7*l > N*np.exp(-eta0/2): break
    vals = {k: [] for k in ('T', 'Tm', 'F', 'S3')}
    for u in us:
        # observer frame: boost by -u ; |B v|_E^2 = cosh(2u)(x0^2+x1^2) - 2 sinh(2u) x0 x1
        r2 = np.cosh(2*u)*(P0*P0 + P1*P1) - 2*np.sinh(2*u)*P0*P1
        w = np.exp(-r2/(2*l*l))
        vals['F'].append(w.sum()); vals['T'].append(w[tl].sum()); vals['Tm'].append((w*m)[tl].sum())
        vals['S3'].append(w[tl & (m == 3)].sum())
    # reach: minimal observer norm of boundary points
    rb = np.sqrt(np.min(np.cosh(2*us)[:, None]*0 + 1))  # placeholder
    edge = np.exp(-(N*np.exp(-eta0/2))**2/(2*l*l))
    print(f"  {l:4d}  {np.std(vals['T']):.4e}   {np.std(vals['Tm']):.4e}   {np.std(vals['F']):.4e}   {np.std(vals['S3']):.4e}       {np.mean(vals['T']):.6e}   edge weight {edge:.1e}")
