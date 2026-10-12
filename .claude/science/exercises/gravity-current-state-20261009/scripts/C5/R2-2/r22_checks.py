"""R2-2 checks (C5 round 2): Lemma N-Q algebra, the needle theorem behind P-L, and the
Lorentz-random lattice (LRL) counterexample to the *strong* (in-band) form of P-L.
Sections:
 1. N-Q step 1: A=P+Q with spec in {0,1,2} forces [P,Q]=0 (algebraic identity), and the
    counterexample A=2P, B=2Q (theta=pi/3): integer spectra, integer sum, non-commuting.
 2. integer variance bound Var X >= theta(1-theta).
 3. 1+1 LRL from the Z[sqrt2] lattice: discrete boost symmetry, no null vectors, |x^2|>=1/sqrt2...,
    Euclidean hard core in every frame, Lorentz invariance in law (Monte Carlo), Bragg gap |q^2|>=c.
 4. needle theorem illustration on the 1+1 LRL: Var N(needle) >= 1/4, timelike Bragg share -> 0.
 5. 3+1: anisotropic form Q7=-7x0^2+x1^2+x2^2+x3^2 (no rational null vectors), integral boosts of
    unbounded rapidity, Bragg gap; contrast with isotropic Z^4 (null vectors, null Bragg peaks).
"""
import itertools, numpy as np, sympy as sp
rng = np.random.default_rng(20261012)
print("=" * 78)
print("(1) N-Q step 1: two-projection lemma")
P, Q = sp.symbols('P Q', commutative=False)
A = P + Q
expr = sp.expand(A**3 - 3*A**2 + 2*A)
# reduce with P^2=P, Q^2=Q
def red(e):
    e = sp.expand(e)
    for _ in range(6):
        e = sp.expand(e.subs({P**3: P, Q**3: Q}).subs({P**2: P, Q**2: Q}))
    return e
print("  A(A-1)(A-2) with P^2=P,Q^2=Q  =", red(expr))
print("  so spec(P+Q) in {0,1,2}  =>  PQP+QPQ = PQ+QP  =>  (PQP)^2=PQP  =>  |QP-PQP|^2=PQP-(PQP)^2=0  =>  QP=PQP=PQ")
for n, k in [(4, 2), (6, 3), (8, 3)]:
    X = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Uq, _ = np.linalg.qr(X)
    Y = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Vq, _ = np.linalg.qr(Y)
    Pm = Uq[:, :k] @ Uq[:, :k].conj().T; Qm = Vq[:, :k] @ Vq[:, :k].conj().T
    ev = np.linalg.eigvalsh(Pm + Qm)
    print(f"  random n={n},k={k}: ||[P,Q]||={np.linalg.norm(Pm@Qm-Qm@Pm):.3f}, max dist(spec(P+Q),Z)={np.max(np.abs(ev-np.round(ev))):.3f}")
th = np.pi/3
Pm = np.array([[1, 0], [0, 0.]]); v = np.array([np.cos(th), np.sin(th)]); Qm = np.outer(v, v)
Am, Bm = 2*Pm, 2*Qm
print("  counterexample (drop N5): A=2P, B=2Q, theta=pi/3: spec A =", np.round(np.linalg.eigvalsh(Am), 12),
      " spec B =", np.round(np.linalg.eigvalsh(Bm), 12), " spec(A+B) =", np.round(np.linalg.eigvalsh(Am+Bm), 12),
      " ||[A,B]|| =", round(float(np.linalg.norm(Am@Bm-Bm@Am)), 6))
print("=" * 78)
print("(2) integer variance bound: Var X >= theta(1-theta), theta = frac(EX)")
worst = 1e9
for _ in range(20000):
    m = rng.integers(2, 7); p = rng.dirichlet(np.ones(m)); xs = np.arange(m) + rng.integers(0, 3)
    mu = p @ xs; var = p @ xs**2 - mu**2; t = mu - np.floor(mu)
    worst = min(worst, var - t*(1-t))
print("  min over 20000 random integer laws of Var - theta(1-theta) =", f"{worst:.3e}", "(>=0)")

print("=" * 78)
print("(3) 1+1 Lorentz-random lattice (LRL) from Z[sqrt2]")
r2 = np.sqrt(2.0)
s = 2**-0.25                    # (u,v) = s(a+b r2, a-b r2), u=t+x, v=t-x; density 1
def basis_tx(eta):
    # columns: images of (a,b)=(1,0),(0,1) in (t,x) after boost (u,v)->(e^eta u, e^-eta v)
    cols = []
    for a, b in [(1, 0), (0, 1)]:
        u = s*np.exp(eta)*(a + b*r2); v = s*np.exp(-eta)*(a - b*r2)
        cols.append([(u+v)/2, (u-v)/2])
    return np.array(cols).T
eta0 = np.log(3 + 2*r2)
B0 = basis_tx(0.0); Bp = basis_tx(eta0)
M = np.linalg.solve(B0, Bp)
print(f"  covolume = {abs(np.linalg.det(B0)):.12f} (density 1);  eta0 = ln(3+2sqrt2) = {eta0:.6f}")
print("  B_eta0 L in L coordinates (must be an integer unimodular matrix):\n", np.round(M, 10))
ab = np.array([(a, b) for a in range(-40, 41) for b in range(-40, 41) if (a, b) != (0, 0)])
minkx2 = -(s**2)*(ab[:, 0]**2 - 2*ab[:, 1]**2)          # x^2 = -t^2+x^2 = -uv
print(f"  min |x^2| over nonzero lattice vectors (|a|,|b|<=40) = {np.min(np.abs(minkx2)):.6f} = s^2 = 1/sqrt2 -> no null vectors")
mind = []
for eta in np.linspace(-6, 6, 241):
    X = (basis_tx(eta) @ ab.T).T
    mind.append(np.min(np.linalg.norm(X, axis=1)))
print(f"  Euclidean min distance of B_eta L over eta in [-6,6]: min = {min(mind):.4f} (bound sqrt|x^2| >= {s:.4f})")
# dual (Bragg) lattice, Euclidean pairing; q^2 = -q_t^2 + q_x^2
def bragg(eta, R=60):
    Bs = 2*np.pi*np.linalg.inv(basis_tx(eta)).T
    mn = np.array([(m, n) for m in range(-R, R+1) for n in range(-R, R+1) if (m, n) != (0, 0)])
    return (Bs @ mn.T).T
G = bragg(0.0)
q2 = -G[:, 0]**2 + G[:, 1]**2
print(f"  Bragg gap: min |q^2| over nonzero Bragg vectors = {np.min(np.abs(q2)):.6f}  (= (2pi)^2/sqrt2 = {(2*np.pi)**2/r2:.6f})")
print("  -> ensemble Bartlett spectrum vanishes on {0<|q^2|<c}: spacelike AND timelike neighbourhood of the light cone")

def sample_pts(eta, shift, half=12, R=40):
    B = basis_tx(eta)
    mn = np.array([(m, n) for m in range(-R, R+1) for n in range(-R, R+1)])
    X = (B @ (mn + shift).T).T
    return X[(np.abs(X[:, 0]) < half) & (np.abs(X[:, 1]) < half)]
def lrl_sample():
    eta = rng.uniform(0, eta0); shift = rng.uniform(0, 1, 2)
    # recentre so points cover the window: shift in lattice coords
    return eta, shift
def count_in(X, W):
    return np.sum(W(X))
def boost(chi):
    return np.array([[np.cosh(chi), np.sinh(chi)], [np.sinh(chi), np.cosh(chi)]])
print("  Lorentz invariance in law (MC, 4000 samples): N(W) for unit square W vs boosted windows")
for chi in [0.0, 0.7, 2.5]:
    Linv = np.linalg.inv(boost(chi))
    W = lambda X: np.all(np.abs((Linv @ X.T).T) < 0.5, axis=1)     # X in Lambda W  <=> Lambda^-1 X in W
    cnts = []
    for _ in range(4000):
        eta, sh = lrl_sample()
        B = basis_tx(eta)
        # enumerate lattice points near the boosted window: use lattice coords range from window corners
        corners = (boost(chi) @ np.array([[.5, .5], [.5, -.5], [-.5, .5], [-.5, -.5]]).T).T
        lc = np.linalg.solve(B, corners.T).T
        lo = np.floor(lc.min(0)) - 2; hi = np.ceil(lc.max(0)) + 2
        mm = np.array([(m, n) for m in range(int(lo[0]), int(hi[0])+1) for n in range(int(lo[1]), int(hi[1])+1)])
        X = (B @ (mm + sh).T).T
        cnts.append(int(np.sum(W(X))))
    cnts = np.array(cnts)
    pk = [np.mean(cnts == k) for k in range(4)]
    print(f"    chi={chi:3.1f}: mean={cnts.mean():.4f}  var={cnts.var():.4f}  P(N=0..3)={np.round(pk,3)}")

print("=" * 78)
print("(4) needle theorem on the 1+1 LRL: needle [−T/2,T/2]x[−w/2,w/2], T*w=1/2 (mean 1/2)")
for T in [1, 4, 16, 64, 256]:
    w = 0.5/T
    vars_, tl_share = [], []
    for _ in range(300):
        eta = rng.uniform(0, eta0)
        B = basis_tx(eta)
        # exact variance over shifts: Var = sum_{G!=0} |1hat_W(G)|^2 (density 1), truncated
        Bs = 2*np.pi*np.linalg.inv(B).T
        Rm = 400
        mn = np.array(np.meshgrid(np.arange(-Rm, Rm+1), np.arange(-Rm, Rm+1))).reshape(2, -1).T
        mn = mn[np.any(mn != 0, axis=1)]
        Gs = (Bs @ mn.T).T
        f = (T*np.sinc(Gs[:, 0]*T/(2*np.pi)) * w*np.sinc(Gs[:, 1]*w/(2*np.pi)))**2
        tl = (-Gs[:, 0]**2 + Gs[:, 1]**2) < 0
        tot = f.sum(); vars_.append(tot); tl_share.append(f[tl].sum()/tot)
    print(f"  T={T:4d}: <Var>_trunc = {np.mean(vars_):.4f} (>= 1/4 required; truncated sum, a lower estimate)   timelike-Bragg share = {np.mean(tl_share):.2e}")
# MC exact variance check at T=16
T = 16; w = 0.5/T; cnts = []
for _ in range(20000):
    eta = rng.uniform(0, eta0); sh = rng.uniform(0, 1, 2); B = basis_tx(eta)
    corners = np.array([[T/2, w/2], [T/2, -w/2], [-T/2, w/2], [-T/2, -w/2]])
    lc = np.linalg.solve(B, corners.T).T; lo = np.floor(lc.min(0)) - 2; hi = np.ceil(lc.max(0)) + 2
    mm = np.array([(m, n) for m in range(int(lo[0]), int(hi[0])+1) for n in range(int(lo[1]), int(hi[1])+1)])
    X = (B @ (mm + sh).T).T
    cnts.append(int(np.sum((np.abs(X[:, 0]) < T/2) & (np.abs(X[:, 1]) < w/2))))
cnts = np.array(cnts)
print(f"  MC exact (T=16, 20000): mean={cnts.mean():.4f}, Var={cnts.var():.4f} (>=0.25), P(N=0,1,2)={[round(float(np.mean(cnts==k)),3) for k in range(3)]}")

print("=" * 78)
print("(5) 3+1 arithmetic lattices")
J7 = np.diag([-7, 1, 1, 1])
def refl(r, J):
    Qr = r @ J @ r
    return np.eye(4, dtype=int) - (2*np.outer(r, r @ J)) // Qr if np.all((2*np.outer(r, r @ J)) % Qr == 0) else None
rs = [np.array(v) for v in [(0, 1, 0, 0), (1, 3, 0, 0), (1, 2, 2, 1), (0, 0, 1, 0), (0, 1, -1, 0)]]
R = {tuple(r): refl(r, J7) for r in rs}
for r, M in R.items():
    print(f"  r={r}: Q7(r)={np.array(r)@J7@np.array(r)}, integral reflection: {M is not None and np.array_equal(M.T@J7@M, J7)}")
g = R[(1, 3, 0, 0)] @ R[(0, 1, 0, 0)]
D = np.diag([np.sqrt(7), 1, 1, 1])
greal = D @ g @ np.linalg.inv(D)
print("  gamma = s_(1,3,0,0) s_(0,1,0,0) =\n", g)
print(f"  preserves Q7: {np.array_equal(g.T@J7@g, J7)}, det={round(np.linalg.det(g))}, orthochronous g00>0: {g[0,0]>0}, cosh(rapidity)={greal[0,0]:.4f}")
gp = np.eye(4, dtype=np.int64)
for k in range(1, 5):
    gp = gp @ g
    print(f"    gamma^{k}: cosh(rapidity) = {(D@gp@np.linalg.inv(D))[0,0]:.4e}")
# anisotropy over Q: no nonzero n with Q7(n)=0 in a box, and mod-8 argument
Nb = 25
rngb = np.arange(-Nb, Nb+1)
n1, n2, n3 = np.meshgrid(rngb, rngb, rngb, indexing='ij')
S3 = (n1**2 + n2**2 + n3**2).ravel()
hit = [n0 for n0 in range(0, Nb+1) if np.any(S3 == 7*n0*n0) and not (n0 == 0)]
print(f"  Q7 null vectors with |n_i|<={Nb}: n0 values with 7 n0^2 = sum of 3 squares: {hit} (expect none; Legendre: 7*4^k(8m+7) form)")
print(f"  min |Q7(n)| over nonzero n in box = {min(abs(-7*n0*n0 + int(v)) for n0 in range(0, 6) for v in np.unique(S3)[:400] if not (n0 == 0 and v == 0))}")
# dual form 7*Q7^* (y) = -y0^2 + 7(y1^2+y2^2+y3^2); Bragg q^2 = (2pi)^2 Q7^*(y)
hitd = [y0 for y0 in range(1, 7*Nb) if np.any(7*S3 == y0*y0)]
print(f"  dual null vectors with |y_i|<={Nb}: {hitd} (expect none) -> Bragg gap |q^2| >= (2pi)^2/7 in units where L7 = diag(sqrt7,1,1,1)Z^4")
# isotropic Z^4 contrast
J1 = np.diag([-1, 1, 1, 1])
print("  isotropic Z^4: (1,1,0,0) null:", (np.array([1, 1, 0, 0])@J1@np.array([1, 1, 0, 0])) == 0,
      "; Pythagorean null directions -> null Bragg peaks; Gamma_Z non-cocompact (cusp)")
# cusp estimate for Z^4-based LRL: P(shortest null vector has Euclidean length < eps) ~ eps^2 (Siegel-type bound)
print("  Z^4-LRL: E#(null lattice vectors with |x|<eps) = c*sum_k k^-2 * lambda_0(B_eps) ~ eps^2 (lambda_0 = d^3x/|x|): 'in-band' null Bragg needs eps ~ omega*a")
print("done")
