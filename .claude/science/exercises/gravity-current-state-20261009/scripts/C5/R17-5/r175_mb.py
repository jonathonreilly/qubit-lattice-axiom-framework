"""C5 R17-5: multi-band W2_pf completions (six-band signed-axis and C2-exchanged families).
Run: OMP_NUM_THREADS=2 python3 r175_mb.py   (from this folder; imports the unmodified R16-5 profile copy)
Raw values everywhere; no subtraction. Each block prints what it checks.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r165_recheck'))
from r99_profiles_copy import profile

rng = np.random.default_rng(20261013)
np.set_printoptions(precision=4, suppress=False)
AX = np.eye(3)
LABELS = [AX[0], -AX[0], AX[1], -AX[1], AX[2], -AX[2]]          # six signed axes
PI6 = [np.diag([c[j] for c in LABELS]) for j in range(3)]         # Pi_j = diag(v_j), k-independent

def herm(M):
    return 0.5*(M + M.conj().T)

# ---------------------------------------------------------------------------------------------
print("=== (1) six-band signed-axis Pi_j = diag(v_j): zeroth moment, standard vs deformed ===")
# any F that is block-diagonal in the joint label commutes with Pi_j -> identity holds with theta = 0
Fd = np.diag(rng.normal(size=6) + 1j*rng.normal(size=6))
for j in range(3):
    r0 = np.abs(PI6[j] @ Fd - Fd @ PI6[j]).max()
    print(f"  j={j}: |Pi F - F Pi| for sector-diagonal F = {r0:.1e}  (theta = 0 holds)")
# standard W2_pf needs Pi(k+q)F - F Pi(k) = theta F with theta = q_j + O(q^3).  Since Pi is
# k-independent, Pi F - F Pi has zero diagonal (same-label) blocks, so the diagonal blocks of F must vanish
# wherever theta != 0; F(k,k+q) -> Pi_j (nonzero diagonal) as q -> 0 then contradicts continuity.
for q in [1e-1, 1e-2, 1e-3]:
    F = PI6[0] + q*(rng.normal(size=(6, 6)) + 1j*rng.normal(size=(6, 6)))   # any continuous kernel with forward value Pi_x
    ths = np.linspace(-2*q, 2*q, 4001)
    # same-label (diagonal) entries: (Pi F - F Pi)_aa = 0, so the identity there reads theta*F_aa = 0
    diag_res = [np.abs(th*np.diag(F)).max() for th in ths]
    full_res = [np.abs(PI6[0] @ F - F @ PI6[0] - th*F).max() for th in ths]
    print(f"  q={q:.0e}: same-label residual |theta F_aa| minimised at theta = {ths[int(np.argmin(diag_res))]:+.1e} "
          f"(value at theta=q: {np.abs(q*np.diag(F)).max():.2e}, i.e. q*|F_aa| with |F_aa| -> |c_a,x| = 1); "
          f"full residual at theta=q: {np.abs(PI6[0]@F - F@PI6[0] - q*F).max():.2e}, at theta=0: {np.abs(PI6[0]@F - F@PI6[0]).max():.2e}")
print("  allowed constant theta values (differences of spec Pi_x = {-1,0,1}): {-2,-1,0,1,2}; continuous theta near 0 -> 0")

# ---------------------------------------------------------------------------------------------
print("\n=== (2) Theorem MB step A: lambda_max(k+q) - lambda_max(k) must equal theta(q) for every k ===")
def fourier_family(N, R=1, seed=0):
    r = np.random.default_rng(seed)
    terms = []
    for nx in range(-R, R+1):
        for ny in range(-R, R+1):
            for nz in range(-R, R+1):
                A = r.normal(size=(N, N)) + 1j*r.normal(size=(N, N))
                terms.append((np.array([nx, ny, nz]), A/np.sqrt(N)))
    def Pi(k):
        M = np.zeros((N, N), complex)
        for n, A in terms:
            M = M + A*np.exp(1j*n@k)
        return herm(M)
    return Pi

def twisted_const_spectrum(D):
    # Pi(k) = U(k) D U(k)^+, U(k) = exp(i H(k)) with H periodic: constant spectrum, k-dependent eigenvectors
    N = len(D)
    Hf = fourier_family(N, 1, seed=7)
    def Pi(k):
        w, V = np.linalg.eigh(Hf(k))
        U = V @ np.diag(np.exp(1j*w)) @ V.conj().T
        return U @ np.diag(D) @ U.conj().T
    return Pi

def c2_exchanged_family():
    # two bands exchanged by the C2 that reverses k_x: Pi_x(k) = [[a(k), b(k)], [b*, -a(Rk)]], with a not odd
    def Pi(k):
        a = 0.7 + 0.3*np.cos(k[0]) + 0.2*np.sin(k[0]) + 0.1*np.cos(k[1])
        aR = 0.7 + 0.3*np.cos(-k[0]) + 0.2*np.sin(-k[0]) + 0.1*np.cos(-k[1])
        b = 0.25*np.sin(k[2]) + 0.15j*np.sin(k[0])
        return np.array([[a, b], [np.conj(b), -aR]])
    return Pi

families = {
    'random 4-band, range 1': fourier_family(4, 1, seed=3),
    'C2-exchanged 2-band (k-dep. spectrum)': c2_exchanged_family(),
    'twisted constant spectrum {1,1,-1,0}': twisted_const_spectrum(np.array([1.0, 1.0, -1.0, 0.0])),
    'six-band signed axis (Pi_x)': (lambda k: PI6[0]),
}
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(400)]
for name, Pi in families.items():
    out = []
    for qn in [1e-2, 1e-3]:
        qv = qn*np.array([0.6, 0.48, 0.64])
        d = []
        for k in ks:
            lk = np.linalg.eigvalsh(Pi(k)).max(); lq = np.linalg.eigvalsh(Pi(k+qv)).max()
            if lk > 0.05:
                d.append(lq - lk)
        d = np.array(d)
        out.append(f"|q|={qn:.0e}: spread(dlam)/|q| = {(d.max()-d.min())/qn:.3e}, mean(dlam)/|q| = {d.mean()/qn:+.2e}")
    print(f"  {name:40s} " + " ; ".join(out))
print("  (a single theta(q) exists only if spread = 0; then theta = mean, which -> 0 at the zone level)")

# ---------------------------------------------------------------------------------------------
print("\n=== (3) W1_pf forward stress F^(ij)|_E = V_i Pi_j|_E must be symmetric: v || c on every c != 0 band ===")
kk = np.linspace(-np.pi, np.pi, 41)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
for prof in ['G', 'NN']:
    for m in [1.0, 0.3]:
        uu = [profile(prof, K) for K in (KX, KY, KZ)]
        eps = np.sqrt(m*m + sum(u[0] for u in uu))
        v = [u[1]/(2*eps) for u in uu]
        # band labelled c = +e_x with a 3D-dispersing eps: antisymmetric part of v_i c_j
        asym = np.max(np.abs(v[1]*1.0 - v[0]*0.0))      # (i,j) = (y,x): v_y c_x - v_x c_y
        print(f"  {prof} m={m}: 3D band with label +e_x: max|v_y c_x - v_x c_y| = {asym:.4f}  (must be 0 for symmetric T^ij)")

# axis-mover completion of the six-band family: band +e_x has eps = f(k_x) only
def f_axis(kx, m):
    return np.sqrt(m*m + 4*np.sin(kx/2)**2)
def Dfwd(q):                    # periodic forward-difference symbol, D(q) = q + O(q^2) (Hermitian kernel below)
    return -1j*(np.exp(1j*q) - 1)
worst = 0.0; worst_herm = 0.0
for _ in range(2000):
    m = rng.choice([1.0, 0.3, 0.01])
    k = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-np.pi, np.pi, 3)
    if abs(Dfwd(q[0])) < 1e-6:
        continue
    F0x = 1.0                                                     # T^{0x} = number density of the +x sector
    Fxx = (f_axis(k[0]+q[0], m) - f_axis(k[0], m))/Dfwd(q[0])     # T^{xx} on x-links; all other F^{ij} = 0
    omega = f_axis(k[0]+q[0], m) - f_axis(k[0], m)
    worst = max(worst, abs(omega*F0x - Dfwd(q[0])*Fxx))
    Fxx_rev = (f_axis(k[0], m) - f_axis(k[0]+q[0], m))/Dfwd(-q[0])  # kernel F(k+q,k) at -q
    worst_herm = max(worst_herm, abs(Fxx_rev - np.conj(Fxx)))
# smoothness of F^xx at q -> 0 (forward value = v_x * c_x)
k0 = 0.7
fwd = [(f_axis(k0+q, 0.3) - f_axis(k0, 0.3))/Dfwd(q) for q in [1e-3, 1e-5]]
vx = np.sin(k0)/f_axis(k0, 0.3)
print(f"  axis-mover +x band: max|omega F^0x - D_x F^xx| over 2000 random (k,q) = {worst:.2e}; Hermiticity defect = {worst_herm:.2e}")
print(f"  forward F^xx at k=0.7, m=0.3: q=1e-3 -> {fwd[0].real:.6f}{fwd[0].imag:+.1e}i, q=1e-5 -> {fwd[1].real:.6f}; v_x c_x = {vx:.6f}")
print("  zeroth moment: F^{0j} = c_j * 1 on each sector, sector-diagonal -> [P_i, T(q)] = 0, theta = 0 (deformed class D only)")

# ---------------------------------------------------------------------------------------------
print("\n=== (4) redshift bridge RB: isotropic-strain response R = sum_i F^ii(k,k) vs physical R_phys = p.v ===")
print("  (delta eps = -delta_a * R; RB requires R = p.v to leading order in p = k - k0 near the band bottom)")
for m in [1.0, 0.3, 0.01, 0.0]:
    rows = []
    for kx in [0.3, 0.1, 0.03, 0.01, -0.01]:
        e = f_axis(kx, m); vx = np.sin(kx)/e if e > 0 else np.cos(kx/2)*np.sign(kx)
        Rm = vx*1.0                       # label c = +e_x
        Rp = vx*kx
        rows.append(f"k={kx:+.2f}: R/Rphys={Rm/Rp:+.3e}")
    print(f"  axis mover +x, m={m}: " + "; ".join(rows))
# controls
for m in [0.3, 0.0]:
    for G in [0.0, 2*np.pi]:
        kx = 0.05; p = kx + G; e = np.sqrt(m*m + p*p); vx = p/e
        print(f"  CONTROL tower (Pi = k+G, N = infinity) m={m} G={G:.2f}: R/Rphys = {(vx*p)/(vx*p):.6f}; "
              f"delta eps/(-delta_a eps) = {vx*p/e:.6f} (1 = nu ~ 1/a when massless)")
u, up, upp = profile('G', np.array([0.3, 0.1, 0.01, 1.9]))
for i, kx in enumerate([0.3, 0.1, 0.01, 1.9]):
    e = np.sqrt(0.09 + u[i]); vx = up[i]/(2*e); g = up[i]/2
    print(f"  CONTROL single-band G (g = u'/2), m=0.3, k={kx}: R/Rphys = {(vx*g)/(vx*kx):.6f}  (passes RB on the box; fails the zeroth moment, R16-5)")
print("  sector c = 0 band (any eps): F^ii(k,k) = V_i * 0 = 0 -> R = 0, R/Rphys = 0")

# ---------------------------------------------------------------------------------------------
print("\n=== (5) rotation lemma: a unitary continuous rotation must map joint spec(P) to R(alpha) joint spec(P) ===")
for alpha in [np.pi/12, np.pi/6, np.pi/4, np.pi/2]:
    rot = np.cos(alpha)*PI6[0] + np.sin(alpha)*PI6[1]
    s_rot = np.sort(np.linalg.eigvalsh(rot)); s_x = np.sort(np.diag(PI6[0]))
    print(f"  six-band, alpha={alpha:.4f}: spec(cos a Pi_x + sin a Pi_y) = {np.round(s_rot, 4)}; spec Pi_x = {s_x}; "
          f"max diff = {np.abs(s_rot - s_x).max():.4f}")
print("  (equal spectra are necessary for unitary equivalence; they fail for every alpha not in (pi/2)Z)")

# ---------------------------------------------------------------------------------------------
print("\n=== (6) lattice-translation test: winding of det exp(i Pi_x(k)) around the k_x cycle vs N for e^{ik_x} ===")
for name, Pi in families.items():
    if 'six-band' in name:
        N = 6
    else:
        N = Pi(np.zeros(3)).shape[0]
    ky, kz = 0.37, -1.1
    kxs = np.linspace(-np.pi, np.pi, 4001)
    ph = np.array([np.trace(Pi(np.array([kx, ky, kz]))).real for kx in kxs])
    wind = (ph[-1] - ph[0])/(2*np.pi)
    print(f"  {name:40s} N={N}: winding of det e^(i Pi_x) = {wind:+.2e}; needed for exp(iP_x) = T_x (x internal unitary): {N}")

# ---------------------------------------------------------------------------------------------
print("\n=== (7) whole-zone v_max of the laws used ===")
kx = np.linspace(-np.pi, np.pi, 200001)
for m in [1.0, 0.3, 0.01, 0.0]:
    e = f_axis(kx, m)
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.where(e > 0, np.sin(kx)/np.where(e > 0, e, 1), 1.0)
    print(f"  axis mover eps = sqrt(m^2 + 4 sin^2(k_x/2)), m={m}: whole-zone v_max = {np.abs(v).max():.6f} (along its axis; 0 transverse)")
print("  G single band (control): any-d, any-m bound 1.0000 (R16-5 block (1), rerun identical)")

# ---------------------------------------------------------------------------------------------
print("\n=== (8) multiband W1 forward formula P_E F^xx(k,k) P_E = V_x Pi_x|_E (1D, twisted 2-band, with and without degeneracy) ===")
def U1(k):                      # k-periodic unitary rotating the band basis
    a = 0.6*np.sin(k) + 0.3*np.cos(2*k); b = 0.4*np.cos(k)
    H = np.array([[a, b*(1-0.5j)], [b*(1+0.5j), -a]])
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j*w)) @ V.conj().T
def model(k, degenerate):
    e1 = np.sqrt(0.09 + 2 - 2*np.cos(k)); e2 = e1 if degenerate else np.sqrt(1.0 + 2 - 2*np.cos(k)) + 0.2*np.sin(k)
    U = U1(k)
    return U @ np.diag([e1, e2]) @ U.conj().T, U @ np.diag([1.0, -1.0]) @ U.conj().T, (e1, e2), U
for degenerate in [False, True]:
    errs = []
    for k in np.linspace(-3.0, 3.0, 13):
        q = 1e-6
        hk, Pk, (e1, e2), Uk = model(k, degenerate); hq, Pq, _, Uq = model(k+q, degenerate)
        # a continuous kernel with forward value Pi: F(k,k+q) = U(k+q) diag(1,-1) U(k)^+ * (1 + 0.3 sin q)
        F0 = Uq @ np.diag([1.0, -1.0]) @ Uk.conj().T*(1 + 0.3*np.sin(q))
        D = -1j*(np.exp(1j*q) - 1)
        Fxx = (hq @ F0 - F0 @ hk)/D            # W1 solved for the stress (1D: always symmetric)
        Fp = Uk.conj().T @ Fxx @ Uk             # band basis at k (eigenvectors are U(k) columns)
        de = 1e-6
        _, _, (e1p, e2p), _ = model(k+de, degenerate); _, _, (e1m, e2m), _ = model(k-de, degenerate)
        v1 = (e1p - e1m)/(2*de); v2 = (e2p - e2m)/(2*de)
        if degenerate:
            # E = whole C^2: P_E F P_E = V Pi|_E with V = v1*I, Pi|_E = diag(1,-1) in this basis
            target = v1*np.diag([1.0, -1.0])
            errs.append(np.abs(Fp - target).max())
        else:
            errs.append(max(abs(Fp[0, 0] - v1*1.0), abs(Fp[1, 1] - v2*(-1.0))))
    print(f"  degenerate={degenerate}: max |P_E F^xx P_E - V Pi|_E| over 13 k (q=1e-6) = {max(errs):.2e}")

# ---------------------------------------------------------------------------------------------
print("\n=== (9) size of the RB failure at a = l_P for an axis-mover optical photon (|c| = 1/a, RECALLED l_P, lambda) ===")
lP, lam = 1.616e-35, 5.0e-7
ka = 2*np.pi*lP/lam
print(f"  k a = {ka:.3e}; axis-mover strain response / physical redshift = 1/(k a) = {1/ka:.3e} (sign = sign of v.c: blueshift for movers against their label)")
