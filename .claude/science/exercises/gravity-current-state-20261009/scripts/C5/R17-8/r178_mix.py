"""C5 R17-8: mixing, field-dependent and altered constant-shift generators (P-r175a).
Run: OMP_NUM_THREADS=2 python3 r178_mix.py   (imports the unmodified R9-9 profile copy from recheck/R16-5)
Raw values everywhere; nothing subtracted. Each block prints what it checks.
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recheck', 'R16-5'))
from r99_profiles_copy import profile

rng = np.random.default_rng(20261013)

def band3d(name, m):
    """separable cubic band eps^2 = m^2 + sum u(k_i); returns functions eps, v (grad eps), g = u'/2 per axis."""
    def uu(k):
        u, up, upp = profile(name, np.atleast_1d(k))
        return u, up
    def eps(K):
        s = m**2
        for i in range(3):
            s = s + uu(K[..., i])[0]
        return np.sqrt(s)
    def grads(K):
        e = eps(K)
        up = np.stack([uu(K[..., i])[1] for i in range(3)], -1)
        return up/(2*e[..., None]), up/2.0          # v_i = u'_i/(2 eps), g_i = u'_i/2 (R8-2 forward value)
    return eps, grads

SYM = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
def fwd_vec(g, v):
    """coupled components at the forward point: T^{0l} -> g_l, T^{(il)} -> sym(v_i g_l). A = 9."""
    out = [g[..., l] for l in range(3)]
    for (i, l) in SYM:
        out.append(0.5*(v[..., i]*g[..., l] + v[..., l]*g[..., i]))
    return np.stack(out, -1)

# ---------------------------------------------------------------------------------------------
print("=== (1) single band, general finite component mixing: [P_j,T^a(q)] = sum_b M^{ab}(q) T^b(q) ===")
Ks = rng.uniform(-np.pi, np.pi, size=(4000, 3))
for name, m in [("G", 1.0), ("G", 0.3), ("NN", 1.0), ("NN", 0.3), ("L", 0.3)]:
    eps, grads = band3d(name, m)
    v, g = grads(Ks)
    F0 = fwd_vec(g, v)
    rk = np.linalg.matrix_rank(F0, tol=1e-9*np.abs(F0).max())
    line = f"{name} m={m}: rank of forward values (A=9 components) = {rk} -> M(0) = 0 on the coupled space"
    for qn in [1e-1, 1e-2, 1e-3]:
        qv = qn*np.array([1.0, 0.37, -0.21])
        v2, g2 = grads(Ks + qv)
        D = g2[:, 0] - g[:, 0]                       # Delta_q(k) for j = x
        F = 0.5*(fwd_vec(g, v) + fwd_vec(g2, v2))    # a continuous kernel with the right forward value
        nd = len(np.unique(np.round(D/qn, 9)))
        # best unconstrained A x A real mixing matrix for D*F = M F (row-wise least squares)
        lhs = D[:, None]*F
        Msol, *_ = np.linalg.lstsq(F, lhs, rcond=None)
        res = np.linalg.norm(lhs - F@Msol)/np.linalg.norm(lhs)
        line += f"\n   |q|={qn:.0e}: distinct Delta_q(k)/|q| values over 4000 k = {nd} (identity allows <= 9); best 9x9 M: rel. residual = {res:.3f}"
    print(line)
# continuum control: eps = sqrt(m^2+|k|^2) on R^3, g = k (exact crystal momentum without periodicity)
m = 0.3
K = rng.uniform(-1, 1, size=(4000, 3))
for qn in [1e-1, 1e-2, 1e-3]:
    qv = qn*np.array([1.0, 0.37, -0.21])
    e1 = np.sqrt(m**2 + (K**2).sum(1)); e2 = np.sqrt(m**2 + ((K+qv)**2).sum(1))
    v1 = K/e1[:, None]; v2 = (K+qv)/e2[:, None]
    D = (K+qv)[:, 0] - K[:, 0]
    F = 0.5*(fwd_vec(K, v1) + fwd_vec(K+qv, v2))
    lhs = D[:, None]*F
    Msol, *_ = np.linalg.lstsq(F, lhs, rcond=None)
    res = np.linalg.norm(lhs - F@Msol)/np.linalg.norm(lhs)
    print(f"   CONTROL continuum g = k, |q|={qn:.0e}: rel. residual = {res:.1e}; M = q_x*1 recovered to {np.abs(Msol - qv[0]*np.eye(9)).max():.1e}")

# ---------------------------------------------------------------------------------------------
print("\n=== (2) multi-band mixing: reduction lemma and the su(2) ('rotation-like') mixing ===")
# (2a) q=0 identity [Gamma, Phi(w)] = Phi(w M0): Phi maps the mu-generalized eigenspace of M0 into the mu-eigenspace
# of ad_Gamma. Example: M0 = i*eps_j on momentum components -> Pi_j = spin matrices (constant spectrum).
S1 = [np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]), np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]]),
      np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])]                       # spin-1, [S_i,S_j] = i eps S_k
comm = np.abs(S1[0]@S1[1] - S1[1]@S1[0] - 1j*S1[2]).max()
print(f"  spin-1 Pi_j = S_j: |[S_x,S_y] - i S_z| = {comm:.1e}; spec S_x = {np.round(np.linalg.eigvalsh(S1[0]), 12)} (k-independent)")
# W1 (Lemma F): [h, Pi_j] = 0 for all j -> h = eps(k) * 1 on the multiplet (Schur); forward stress V_i Pi_j must be symmetric
for name, mm in [("G", 0.3), ("NN", 1.0)]:
    eps, grads = band3d(name, mm)
    v, g = grads(Ks[:500])
    asym = 0.0
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        for n in range(500):
            asym = max(asym, np.abs(v[n, i]*S1[j] - v[n, j]*S1[i]).max())
    print(f"  {name} m={mm}: spin-1 multiplet, max_k |v_i S_j - v_j S_i| = {asym:.3f} (0 needed for symmetric T^ij -> v = 0: flat band)")
# (2b) multi-shift partner sets: zigzag spectrum {+tri, -tri} with shifts {+q, -q}: partner holds except at a peak
def tri(k):
    return np.abs(-(((-k) + np.pi) % (2*np.pi) - np.pi))
kk = np.linspace(-np.pi, np.pi, 20001)
for qn in [1e-1, 1e-2, 1e-3]:
    viol = np.zeros_like(kk)
    for s in [+1, -1]:
        gam = s*tri(kk)
        cand = np.stack([sp*tri(kk+qn) - mu for sp in [1, -1] for mu in [qn, -qn]], -1)
        viol = np.maximum(viol, np.min(np.abs(cand - gam[:, None]), -1)*(np.abs(gam) > 1e-12))
    i0 = np.argmax(viol)
    print(f"  zigzag {{+tri,-tri}}, shifts {{+q,-q}}, q={qn:.0e}: partner violation max = {viol.max():.2e} (= {viol.max()/qn:.2f} q) at k = {kk[i0]:+.4f} (peak k = +-pi); violation at |k|<2.5: {viol[np.abs(kk) < 2.5].max():.1e}")

# ---------------------------------------------------------------------------------------------
print("\n=== (3) field-dependent generators: Poisson-bracket check of the 'graviton inverse propagator' structure ===")
import sympy as sp
h, p, ar, ai, br, bi = sp.symbols('h p ar ai br bi', real=True)   # graviton mode (h, pi); matter modes a (k), b (k+q)
e1, e2, c, Kq, Y, Z, T0 = sp.symbols('e1 e2 c Kq Y Z T0', real=True)
def PB(f, gg):
    # canonical pairs: (h,p), (ar,ai) and (br,bi) with a = (ar + i ai)/sqrt2: {ar, ai} = 1
    pairs = [(h, p), (ar, ai), (br, bi)]
    return sp.expand(sum(sp.diff(f, x)*sp.diff(gg, y) - sp.diff(f, y)*sp.diff(gg, x) for x, y in pairs))
bil = ar*br + ai*bi          # Re(a* b): a real transition bilinear between the two modes
bil2 = ar*bi - ai*br         # Im(a* b)
Hm = e1*(ar**2 + ai**2)/2 + e2*(br**2 + bi**2)/2
Hg = c*p**2/2 + Kq*h**2/2
Q = h*Y*bil + p*Z*bil2       # field-dependent generator correction (cubic): h-term and pi-term
X = PB(Q, Hm + Hg)
Xp = sp.expand(sp.diff(X, p))      # coefficient of pi (bilinear in matter)
Xh = sp.expand(sp.diff(X, h))
solY = sp.solve(sp.Eq(sp.expand(Xp.coeff(ar*br)), 0), Y)
print(f"  pi-coefficient of {{Q, Hm+Hg}}: {sp.factor(Xp)}")
print(f"  require it = 0  ->  Y = {solY}")
Xh_sub = sp.factor(Xh.subs(Y, solY[0]))
print(f"  h-coefficient after that: {Xh_sub}   (omega = e2 - e1; factor (c*Kq - omega^2)/c * Z = graviton inverse propagator at (omega, q) times Z: zero only for an on-shell graviton)")

# ---------------------------------------------------------------------------------------------
print("\n=== (4) energy-shell (field-dependent) form, single band: t.grad(Pi_x) = t_x for t tangent to the energy surface ===")
# least squares over odd-in-kx, even-in-(ky,kz) trigonometric polynomials Pi_x = sum c_abc sin(a kx) cos(b ky) cos(c kz)
def tangential_lsq(eps_grad, R, n=24):
    g1 = (np.arange(n) + 0.5)*2*np.pi/n - np.pi
    KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
    Kf = np.stack([KX.ravel(), KY.ravel(), KZ.ravel()], -1)
    v = eps_grad(Kf)
    vh = v/np.maximum(np.linalg.norm(v, axis=1, keepdims=True), 1e-14)
    P = np.eye(3)[None] - vh[:, :, None]*vh[:, None, :]
    cols = []
    for a in range(1, R+1):
        for b in range(0, R+1):
            for cc in range(0, R+1):
                gx = a*np.cos(a*Kf[:, 0])*np.cos(b*Kf[:, 1])*np.cos(cc*Kf[:, 2])
                gy = -b*np.sin(a*Kf[:, 0])*np.sin(b*Kf[:, 1])*np.cos(cc*Kf[:, 2])
                gz = -cc*np.sin(a*Kf[:, 0])*np.cos(b*Kf[:, 1])*np.sin(cc*Kf[:, 2])
                G = np.stack([gx, gy, gz], -1)
                cols.append(np.einsum('nij,nj->ni', P, G).ravel())
    A = np.stack(cols, -1)
    rhs = np.einsum('nij,j->ni', P, np.array([1.0, 0, 0])).ravel()
    sol, *_ = np.linalg.lstsq(A, rhs, rcond=None)
    return np.linalg.norm(A@sol - rhs)/np.linalg.norm(rhs), len(cols)
for name, mm in [("NN", 0.3), ("G", 0.3)]:
    eps, grads = band3d(name, mm)
    out = []
    for R in [1, 2, 4, 6]:
        r, nc = tangential_lsq(lambda K: grads(K)[0], R)
        out.append(f"R={R} ({nc} coeffs): {r:.3f}")
    print(f"  {name} m={mm} (cubic): min rel. tangential residual  " + "; ".join(out))
# control: anisotropic band eps = u(kx) + delta*(u(ky)+u(kz)); delta -> 0 is the Reeb-cycle (one-axis) escape
for delta in [1.0, 0.1, 0.01]:
    def vg(K, d=delta):
        up = [profile("NN", K[:, i])[1] for i in range(3)]
        return np.stack([up[0], d*up[1], d*up[2]], -1)
    r, nc = tangential_lsq(vg, 4)
    print(f"  CONTROL NN anisotropy delta={delta}: min rel. tangential residual (R=4) = {r:.3e}")

# no-symmetry check: full real Fourier basis (all sin/cos products) for Pi_x, R = 3
def tangential_lsq_full(eps_grad, R, n=20):
    g1 = (np.arange(n) + 0.5)*2*np.pi/n - np.pi
    KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
    Kf = np.stack([KX.ravel(), KY.ravel(), KZ.ravel()], -1)
    v = eps_grad(Kf)
    vh = v/np.maximum(np.linalg.norm(v, axis=1, keepdims=True), 1e-14)
    P = np.eye(3)[None] - vh[:, :, None]*vh[:, None, :]
    fs = []
    for a in range(0, R+1):
        for fa in ([np.cos, np.sin] if a else [np.cos]):
            for b in range(0, R+1):
                for fb in ([np.cos, np.sin] if b else [np.cos]):
                    for cc in range(0, R+1):
                        for fc in ([np.cos, np.sin] if cc else [np.cos]):
                            if a == b == cc == 0: continue
                            fs.append((a, fa, b, fb, cc, fc))
    def d(f, n_, x):  # derivative of f(n x)
        return n_*np.cos(n_*x) if f is np.sin else -n_*np.sin(n_*x)
    cols = []
    for (a, fa, b, fb, cc, fc) in fs:
        X, Y_, Zc = fa(a*Kf[:, 0]), fb(b*Kf[:, 1]), fc(cc*Kf[:, 2])
        G = np.stack([d(fa, a, Kf[:, 0])*Y_*Zc, X*d(fb, b, Kf[:, 1])*Zc, X*Y_*d(fc, cc, Kf[:, 2])], -1)
        cols.append(np.einsum('nij,nj->ni', P, G).ravel())
    A = np.stack(cols, -1)
    rhs = np.einsum('nij,j->ni', P, np.array([1.0, 0, 0])).ravel()
    sol, *_ = np.linalg.lstsq(A, rhs, rcond=None)
    return np.linalg.norm(A@sol - rhs)/np.linalg.norm(rhs), len(cols)
for name, mm in [("NN", 0.3), ("G", 0.3)]:
    eps, grads = band3d(name, mm)
    r, nc = tangential_lsq_full(lambda K: grads(K)[0], 3)
    print(f"  {name} m={mm}: full Fourier basis (no parity imposed), R=3 ({nc} functions): min rel. tangential residual = {r:.3f}")
