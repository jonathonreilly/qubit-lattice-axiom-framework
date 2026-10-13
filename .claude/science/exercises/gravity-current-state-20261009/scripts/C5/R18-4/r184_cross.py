"""C5 R18-4: W15 crossing-band checks (Theorem W across band crossings).
Run: OMP_NUM_THREADS=2 python3 r184_cross.py > r184_cross.out
Raw values everywhere; nothing subtracted. Every block prints what it checks.
Blocks:
 (1) Lemma S0: at a conical crossing the commuting momentum symbol is scalar on the degenerate space
     (limit directions of d-hat are non-collinear; pi_+ - pi_- -> 0 at the crossing).
 (2) Energy-shell tangential identity t.grad(pi_x) = t_x (C = 1) on crossing bands:
     X_B (Weyl pair, tilted Weyl pair, PT nodal loop), ansatz pi_+ = A + B|d| (A, B trig polynomials,
     = eigenvalue of every analytic Pi = a + b h); X_A (folded band, branch on the double cover).
 (3) Controls: non-periodic pi_x = k_x admitted (tower-like) -> residual 0; one-axis anisotropy -> residual -> 0.
 (4) H-RB at a conical (massless) extremum: solve grad(phi).(C p + f1 phi) = phi for (C, f1) on tilted /
     anisotropic cones; report the solution space and min over it of sigma_min(C) (rank C = 3 iff > 0).
"""
import itertools
import numpy as np

rng = np.random.default_rng(18_4)


# ------------------------------------------------------------------ helpers
def fourier_basis(K, R, scale=(1.0, 1.0, 1.0)):
    """Real Fourier basis (cos, sin of n.(scale*k)), |n_i| <= R, n in a half-space; returns values and gradients."""
    s = np.array(scale)
    ns = [n for n in itertools.product(range(-R, R + 1), repeat=3) if n > (0, 0, 0)]
    vals = [np.ones(len(K))]
    grads = [np.zeros((len(K), 3))]
    for n in ns:
        nv = np.array(n) * s
        ph = K @ nv
        c, si = np.cos(ph), np.sin(ph)
        vals.append(c); grads.append(-si[:, None] * nv[None, :])
        vals.append(si); grads.append(c[:, None] * nv[None, :])
    return np.array(vals).T, np.transpose(np.array(grads), (1, 0, 2))  # (Npts, M), (Npts, M, 3)


def tangential_lsq(V, cols_grad, target_dir=np.array([1.0, 0.0, 0.0]), extra=None):
    """min || P_perp (sum_c a_c grad_c - e_x) || / || P_perp e_x ||  over coefficients a.
    cols_grad: (Npts, M, 3). V: velocities (Npts, 3)."""
    vh = V / np.linalg.norm(V, axis=1)[:, None]
    P = np.eye(3)[None, :, :] - vh[:, :, None] * vh[:, None, :]
    G = np.einsum('pij,pmj->pmi', P, cols_grad)  # (Npts, M, 3)
    if extra is not None:
        G = np.concatenate([G, np.einsum('pij,pmj->pmi', P, extra)], axis=1)
    b = np.einsum('pij,j->pi', P, target_dir)
    Amat = np.transpose(G, (0, 2, 1)).reshape(-1, G.shape[1])
    bv = b.reshape(-1)
    coef, *_ = np.linalg.lstsq(Amat, bv, rcond=None)
    res = np.linalg.norm(Amat @ coef - bv) / np.linalg.norm(bv)
    return res, coef


def model_d(name, K, delta=1.0, m=2.0):
    kx, ky, kz = K[:, 0], K[:, 1], K[:, 2]
    z = np.zeros_like(kx)
    if name == 'weyl':  # d = (sin kx, d sin ky, m - cos kx - d(cos ky + cos kz)); Weyl points at (0,0,+-pi/2) for m=2,d=1
        d = np.stack([np.sin(kx), delta * np.sin(ky), m - np.cos(kx) - delta * (np.cos(ky) + np.cos(kz))], 1)
        J = np.zeros((len(K), 3, 3))
        J[:, 0, 0] = np.cos(kx)
        J[:, 1, 1] = delta * np.cos(ky)
        J[:, 2, 0] = np.sin(kx); J[:, 2, 1] = delta * np.sin(ky); J[:, 2, 2] = delta * np.sin(kz)
        return d, J
    if name == 'nodal':  # PT-symmetric (real) d = (m - sum cos, 0, sin kz); nodal loop cos kx + cos ky = m-1 at kz = 0
        d = np.stack([m - np.cos(kx) - np.cos(ky) - np.cos(kz), z, np.sin(kz)], 1)
        J = np.zeros((len(K), 3, 3))
        J[:, 0, 0] = np.sin(kx); J[:, 0, 1] = np.sin(ky); J[:, 0, 2] = np.sin(kz)
        J[:, 2, 2] = np.cos(kz)
        return d, J
    raise ValueError(name)


def tilt_f(name, K):
    kx, ky, kz = K[:, 0], K[:, 1], K[:, 2]
    if name == 'none':
        return np.zeros(len(K)), np.zeros((len(K), 3))
    if name == 'tilt':  # f = 0.3 sin kz + 0.2 sin kx  (tilts both Weyl cones; type I)
        f = 0.3 * np.sin(kz) + 0.2 * np.sin(kx)
        g = np.stack([0.2 * np.cos(kx), 0 * kx, 0.3 * np.cos(kz)], 1)
        return f, g
    raise ValueError(name)


print("=== (1) Lemma S0: at a conical crossing a commuting continuous Pi is scalar on the degenerate space ===")
for name, x0, plane in [('weyl', np.array([0, 0, np.pi / 2]), None), ('nodal', None, None)]:
    if name == 'weyl':
        th = rng.uniform(0, np.pi, 4000); ph = rng.uniform(0, 2 * np.pi, 4000)
        u = np.stack([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)], 1)
        K = x0[None, :] + 1e-6 * u
    else:  # nodal loop point: kz = 0, cos kx + cos ky = 1 with kx = ky = pi/3 ; transverse plane spanned by (1,1,0)/sqrt2 and z
        x0 = np.array([np.pi / 3, np.pi / 3, 0.0])
        a = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
        n1 = np.array([1, 1, 0]) / np.sqrt(2); n2 = np.array([0, 0, 1.0])
        K = x0[None, :] + 1e-6 * (np.cos(a)[:, None] * n1[None, :] + np.sin(a)[:, None] * n2[None, :])
    d, _ = model_d(name, K)
    dh = d / np.linalg.norm(d, axis=1)[:, None]
    sv = np.linalg.svd(dh, compute_uv=False)
    print(f"  {name}: |d(x0)| = {np.linalg.norm(model_d(name, x0[None, :])[0]):.1e}; singular values of the limit-direction set of d-hat "
          f"(rank >= 2 => non-collinear => b(x0) = 0): {np.round(sv, 4)}")
    # commuting analytic Pi = alpha + lambda(k) d.sigma, pi_+- = alpha +- lambda |d| -> alpha at x0
    lam = 1.0 + 0.5 * np.cos(K[:, 0]) + 0.3 * np.sin(K[:, 2])
    alpha = 0.7 * np.sin(K[:, 0]) + 0.2
    pp = alpha + lam * np.linalg.norm(d, axis=1); pm = alpha - lam * np.linalg.norm(d, axis=1)
    print(f"     example Pi = alpha + lambda d.sigma: max |pi_+ - pi_-| on the 1e-6 sphere/circle = {np.max(np.abs(pp - pm)):.2e}")

print("\n=== (2) energy-shell tangential identity on crossing bands, C = 1:  min || P_perp(grad pi_x - e_x) || / || P_perp e_x || ===")
Npts = 7000
K = rng.uniform(-np.pi, np.pi, (Npts, 3))
for name, tilt in [('weyl', 'none'), ('weyl', 'tilt'), ('nodal', 'none')]:
    d, J = model_d(name, K)
    nd = np.linalg.norm(d, axis=1)
    f, gf = tilt_f(tilt, K)
    gnd = np.einsum('pi,pij->pj', d / nd[:, None], J)  # grad |d|
    V = gf + gnd  # upper band velocity
    keep = (nd > 0.05) & (np.linalg.norm(V, axis=1) > 1e-3)
    out = []
    for R in (1, 2, 3):
        vals, grads = fourier_basis(K[keep], R)
        # pi = A + B|d| : grad = grad A + |d| grad B + B grad|d|
        gB = nd[keep][:, None, None] * grads + vals[:, :, None] * gnd[keep][:, None, :]
        cols = np.concatenate([grads[:, 1:, :], gB], axis=1)
        res, _ = tangential_lsq(V[keep], cols)
        out.append(f"R={R} ({cols.shape[1]} fns): {res:.3f}")
    print(f"  X_B {name:5s} tilt={tilt:4s} upper band (sorted, Lipschitz at X), pi_+ = A + B|d| :  " + "; ".join(out)
          + f"   [{keep.sum()} pts, |d|>0.05]")
# X_A: folded band -- two bands exchanged under kx -> kx + 2 pi; analytic branch lives on the cover kx in [0, 4 pi)
Kc = np.column_stack([rng.uniform(-2 * np.pi, 2 * np.pi, Npts), rng.uniform(-np.pi, np.pi, (Npts, 2))])
for lab, eps_grad in [('folded NN eps=-cos(kx/2)-cos ky-cos kz', lambda Q: np.stack([0.5 * np.sin(Q[:, 0] / 2), np.sin(Q[:, 1]), np.sin(Q[:, 2])], 1))]:
    V = eps_grad(Kc)
    keep = np.linalg.norm(V, axis=1) > 1e-3
    out = []
    for R in (1, 2, 3):
        vals, grads = fourier_basis(Kc[keep], R, scale=(0.5, 1.0, 1.0))
        res, _ = tangential_lsq(V[keep], grads[:, 1:, :])
        out.append(f"R={R} ({grads.shape[1]-1} fns): {res:.3f}")
    print(f"  X_A {lab} (branch on the double cover, periods 4pi x 2pi x 2pi): " + "; ".join(out))
# the same folded model seen as two sorted bands on T^3: check the sorted band's pi jumps at the face (why branches are used)

print("\n=== (3) controls (same observable) ===")
d, J = model_d('weyl', K)
nd = np.linalg.norm(d, axis=1); gnd = np.einsum('pi,pij->pj', d / nd[:, None], J)
keep = (nd > 0.05) & (np.linalg.norm(gnd, axis=1) > 1e-3)
vals, grads = fourier_basis(K[keep], 2)
gB = nd[keep][:, None, None] * grads + vals[:, :, None] * gnd[keep][:, None, :]
cols = np.concatenate([grads[:, 1:, :], gB], axis=1)
lin = np.zeros((keep.sum(), 1, 3)); lin[:, 0, 0] = 1.0  # grad of the non-periodic k_x (tower / continuum momentum)
res, coef = tangential_lsq(gnd[keep], cols, extra=lin)
print(f"  CONTROL weyl, R=2 basis + non-periodic k_x admitted: residual = {res:.2e} (coefficient of k_x = {coef[-1]:.6f})")
for delta in (1.0, 0.1, 0.01):
    d, J = model_d('weyl', K, delta=delta, m=1.0 + 2 * delta)
    nd = np.linalg.norm(d, axis=1); gnd = np.einsum('pi,pij->pj', d / nd[:, None], J)
    keep = (nd > 0.05 * max(delta, 0.2)) & (np.linalg.norm(gnd, axis=1) > 1e-4)
    vals, grads = fourier_basis(K[keep], 2)
    gB = nd[keep][:, None, None] * grads + vals[:, :, None] * gnd[keep][:, None, :]
    cols = np.concatenate([grads[:, 1:, :], gB], axis=1)
    # one-axis: target is the y-identity (level sets nearly planes ky = const carry x,z windings)
    res_y, _ = tangential_lsq(gnd[keep], cols, target_dir=np.array([0.0, 1.0, 0.0]))
    res_x, _ = tangential_lsq(gnd[keep], cols)
    print(f"  CONTROL one-axis weyl delta={delta}: residual x-identity = {res_x:.3e}; y-identity = {res_y:.3e}")

print("\n=== (4) H-RB at a conical extremum: grad phi(p).(C p + f1 phi(p)) = phi(p) for all p; solution space and min sigma_min(C) ===")
def cone(G, w):
    L = np.linalg.cholesky(G)
    def phi(P):
        return np.sqrt(np.einsum('pi,ij,pj->p', P, G, P)) + P @ w
    def gphi(P):
        r = np.sqrt(np.einsum('pi,ij,pj->p', P, G, P))
        return (P @ G) / r[:, None] + w[None, :]
    return phi, gphi
P = rng.normal(size=(3000, 3))
cases = [('isotropic', np.eye(3), np.zeros(3)),
         ('tilted |w|=0.5', np.eye(3), np.array([0.0, 0.0, 0.5])),
         ('tilted |w|=0.9 oblique', np.eye(3), np.array([0.5, -0.4, 0.6])),
         ('anisotropic + tilt', np.array([[1.0, 0.3, 0.0], [0.3, 0.5, 0.1], [0.0, 0.1, 2.0]]), np.array([0.2, 0.3, -0.1]))]
for lab, G, w in cases:
    phi, gphi = cone(G, w)
    ph, gp = phi(P), gphi(P)
    assert np.all(ph > 0)
    # unknowns: C (9, row-major C_ab), f1 (3);  equation: sum_ab gp_a C_ab p_b + ph * gp . f1 = ph
    A = np.concatenate([np.einsum('pa,pb->pab', gp, P).reshape(len(P), 9), ph[:, None] * gp], 1)
    sol, *_ = np.linalg.lstsq(A, ph, rcond=None)
    resid = np.linalg.norm(A @ sol - ph) / np.linalg.norm(ph)
    U, S, Vt = np.linalg.svd(A, full_matrices=True)
    null = Vt[np.sum(S > 1e-9 * S[0]):]  # null-space basis (directions in (C,f1) space)
    # minimise sigma_min(C) over the affine solution space by random search + local polish
    best = np.inf
    for trial in range(4000):
        t = rng.normal(size=len(null)) * rng.choice([0.1, 1.0, 10.0, 100.0])
        x = sol + t @ null if len(null) else sol
        best = min(best, np.linalg.svd(x[:9].reshape(3, 3), compute_uv=False)[-1])
    C0 = sol[:9].reshape(3, 3)
    print(f"  {lab:24s}: residual {resid:.1e}; null-space dim {len(null)}; particular C sym part eigs {np.round(np.linalg.eigvalsh((C0 + C0.T) / 2), 4)}; "
          f"min sigma_min(C) over sampled solution space = {best:.4f}")
print("  (rank C = 3 on the whole solution space iff min sigma_min > 0; the analytic argument gives this exactly, see report)")

print("\n=== (5) whole-zone v_max of the test laws (round-16 rule; lattice units, both sorted bands) ===")
Kg = rng.uniform(-np.pi, np.pi, (200000, 3))
for name, tilt in [('weyl', 'none'), ('weyl', 'tilt'), ('nodal', 'none')]:
    d, J = model_d(name, Kg); nd = np.linalg.norm(d, axis=1); f, gf = tilt_f(tilt, Kg)
    gnd = np.einsum('pi,pij->pj', d / nd[:, None], J)
    vp = np.linalg.norm(gf + gnd, axis=1).max(); vm = np.linalg.norm(gf - gnd, axis=1).max()
    print(f"  {name} tilt={tilt}: v_max upper = {vp:.4f}, lower = {vm:.4f}")
Kc2 = np.column_stack([rng.uniform(-2 * np.pi, 2 * np.pi, 200000), rng.uniform(-np.pi, np.pi, (200000, 2))])
vf = np.linalg.norm(np.stack([0.5 * np.sin(Kc2[:, 0] / 2), np.sin(Kc2[:, 1]), np.sin(Kc2[:, 2])], 1), axis=1).max()
print(f"  folded NN (branch on the cover; in the folded lattice's own units): v_max = {vf:.4f}")
print("  No gauge-field symbol is introduced: the graviton enters only through theta = C q + O(q^2) (R9-9's v_max not recomputed).")

print("\n=== (6) continuous multi-shift mixing (title hole), SPECTRAL level only: partner relation along a line ===")
print("  test: every nonzero eigenvalue g of Pi(t) with |g| > eps has g + s in spec Pi(t+q) for some s in Sigma0(q) (forward direction checked);")
print("  AND (local-affine step, vR17-8:15) the increment of every eigenvalue that is separated on [t-q, t+q] lies in Sigma0(q)")
def tri(t):  # slope +1 through 0, turning points at +-pi/2 (values +-pi/2), period 2 pi
    t = (t + np.pi) % (2 * np.pi) - np.pi
    return np.where(np.abs(t) <= np.pi / 2, t, np.sign(t) * np.pi - t)
def spec_A(t):  # R17-8's zigzag pair {+tri, -tri} rescaled: turning points separated from every other value
    return np.array([tri(t), -tri(t)])
def spec_B(t):  # candidate: tri plus constant spectator branches +-pi/2 that it touches at its turning points
    return np.array([tri(t), np.pi / 2 + 0 * t, -np.pi / 2 + 0 * t])
def worst(specf, q, sig, eps=1e-9, sep=None):
    ts = np.linspace(-np.pi, np.pi, 20001)
    bad = 0.0
    for t in ts:
        a, b = specf(t), specf(t + q)
        for g in a:
            if abs(g) > eps:
                bad = max(bad, min(abs(g + s - x) for s in sig for x in b))
        if sep is not None:  # local-affine step: separated eigenvalues must move by an element of Sigma0
            for i, g in enumerate(a):
                others = np.delete(a, i)
                if abs(g) > 10 * abs(q) and np.all(np.abs(others - g) > 10 * abs(q)):
                    gb = b[i]
                    bad = max(bad, min(abs(gb - g - s) for s in sig))
    return bad
for q in (1e-2, 1e-3):
    sig = [q, -q, 0.0]
    print(f"  q={q:.0e}: zigzag {{+tri,-tri}} (R17-8 control): worst defect / q = {worst(spec_A, q, sig, sep=True)/q:.3f};"
          f"   touching candidate {{tri, +pi/2, -pi/2}}: worst defect / q = {worst(spec_B, q, sig, sep=True)/q:.3f}")
print("  (defect/q ~ 1 = fails; ~0 = passes the SPECTRAL relation. Passing is necessary only: the intertwiner identity (*),")
print("   W1 symmetric stress and the redshift test are NOT checked here.)")

print("\n=== (7) orientation monodromy of the line field span(d) around a conical point in a transverse slice (Lemma X2) ===")
print("  track a continuous unit field n || d along a small circle (sign chosen for continuity, through sign-flip zeros);")
print("  monodromy = n(2pi).n(0) (+1 trivial, -1 branched cover). Also count the sign-flip crossings.")
def monodromy(dfun, r=1e-2, M=200000):
    th = np.linspace(0, 2 * np.pi, M + 1) + 1e-7  # avoid exact zeros on symmetric axes
    x, y = r * np.cos(th), r * np.sin(th)
    d = dfun(x, y)
    nd = np.linalg.norm(d, axis=1)
    dh = d / np.maximum(nd, 1e-300)[:, None]
    n = dh[0].copy(); flips = 0; prev_sign = 1
    for i in range(1, M + 1):
        c = dh[i] if np.dot(dh[i], n) >= 0 else -dh[i]
        s = 1 if np.dot(dh[i], c) > 0 else -1
        if s != prev_sign: flips += 1
        prev_sign = s; n = c
    return float(np.dot(n, dh[0])), flips
examples = {
    "d=(x^2, xy, 0)            [A-line x=0 through a conical point]": lambda x, y: np.stack([x**2, x*y, 0*x], 1),
    "d=((y^2-x^3)x,(y^2-x^3)y,0) [cusp A-curve through a conical pt]": lambda x, y: np.stack([(y**2-x**3)*x, (y**2-x**3)*y, 0*x], 1),
    "d=(x(x-y)(x+2y), x y (x-y), y^3) [mixed, cubic]": lambda x, y: np.stack([x*(x-y)*(x+2*y), x*y*(x-y), y**3], 1),
    "d=(x y, x^2 - y^2, x^3)   [conical only]": lambda x, y: np.stack([x*y, x**2-y**2, x**3], 1),
    "d=(x, y, 0)               [Weyl-like line, conical only]": lambda x, y: np.stack([x, y, 0*x], 1),
}
for lab, f in examples.items():
    mono, fl = monodromy(f)
    print(f"  {lab}: monodromy {mono:+.6f}; sign-flip crossings {fl}")
rngm = np.random.default_rng(7)
worst = 1.0; nflip = []
for trial in range(40):  # random cubic d sharing a common linear factor (forces an A-curve through the conical point)
    a = rngm.normal(size=(3, 6))
    L = rngm.normal(size=2)
    def f(x, y, a=a, L=L):
        mon = np.stack([x**2, x*y, y**2, x**3, x*x*y, y**3], 1)
        lin = L[0] * x + L[1] * y
        return (mon @ a.T) * lin[:, None]
    mono, fl = monodromy(f, r=1e-3, M=40000)
    worst = min(worst, mono); nflip.append(fl)
print(f"  40 random laws d = (linear form) x (random quadratic+cubic vector): min monodromy {worst:+.6f}; flip counts {sorted(set(nflip))}")
mono, fl = monodromy(lambda x, y: np.stack([y, np.sqrt(x**2 + y**2) - x, 0 * x], 1))
print(f"  CONTROL (NOT analytic: d = (y, r - x, 0), zero set = one half-line): monodromy {mono:+.6f}; sign-flip crossings {fl}"
      "  -> the tracker detects a branched (odd) case when one exists")
