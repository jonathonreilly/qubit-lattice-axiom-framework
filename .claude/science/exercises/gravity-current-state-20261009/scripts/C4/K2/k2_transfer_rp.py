"""K2 part 3: transfer matrix / reflection positivity at xi = 1 on Z^4.

(a) Scalar: Euclidean nearest-neighbour time action -> one-step transfer matrix eigenvalue
    lambda = e^{-E}, cosh E = 1 + (s^2+m^2)/2 : always in (0,1]  (positive at xi = 1).
    Real-time leapfrog with the same stencil at tau = a: lambda + 1/lambda = 2 - (s^2+m^2):
    |lambda|max = 5 + 2 sqrt 6 = 9.899 at the zone corner s^2 = 12 (K7a's 9.9).
(b) Graviton (staggered FP, K7a): temporal gauge h_{4mu} = 0 is reachable exactly for s_4 != 0;
    the remaining 6x6 form is s_4^2 W + V(q). W (DeWitt, lambda=1) is indefinite (trace mode).
    Constraints (h_{4mu} rows) cut the 6 components to the 2 spatial-TT ones, where the form is
    (s_4^2 + q^2)/4 per polarisation -> nearest-neighbour Gaussian in time -> positive transfer
    matrix with 4 sinh^2(E/2) = q^2. The unreduced temporal-gauge propagator has a wrong-sign
    (ghost-like) piece in the trace sector: the Euclidean conformal-factor problem.
"""
import numpy as np, sympy as sp

print("== (a) scalar at xi = 1 ==")
for s2 in [0.0, 1.0, 4.0, 8.0, 12.0]:
    m2 = 0.0
    c = 1 + (s2 + m2) / 2
    lamE = c - np.sqrt(c * c - 1)            # e^{-E}
    # leapfrog: lambda^2 - (2 - s2) lambda + 1 = 0
    b = 2 - (s2 + m2)
    roots = np.roots([1, -b, 1])
    print(f"s^2={s2:5.1f}: Euclidean transfer eigenvalue e^-E = {lamE:.6f} (>0);  leapfrog tau=a |lambda|max = {np.abs(roots).max():.4f}")
print("leapfrog corner value 5+2*sqrt(6) =", 5 + 2 * np.sqrt(6), " (K7a: 9.9). Stable leapfrog needs tau^2 * 12 <= 4.")

print("\n== (b) staggered linearized graviton, temporal gauge ==")
s = sp.symbols('s0:4', real=True)
D = 4
pairs = [(m, n) for m in range(D) for n in range(m, D)]
H = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f"h{min(m,n)}{max(m,n)}"))
hv = [sp.Symbol(f"h{m}{n}") for (m, n) in pairs]
s2 = sum(si**2 for si in s)
hs = H * sp.Matrix(s); shs = (sp.Matrix(s).T * H * sp.Matrix(s))[0]; tr = H.trace()
Q = sp.Rational(1, 4) * (s2 * sum(H[m, n]**2 for m in range(D) for n in range(D)) - 2 * (hs.T * hs)[0]
                         + 2 * shs * tr - s2 * tr**2)
sp_idx = [i for i, (m, n) in enumerate(pairs) if m < 3 and n < 3]        # spatial h_ij (time = index 3)
t_idx = [i for i, (m, n) in enumerate(pairs) if n == 3]                 # h_{i4}, h_44
K = sp.hessian(Q, hv) / 2
Kss = K.extract(sp_idx, sp_idx)
W = sp.simplify(Kss.diff(s[3], 2) / 2)
G6 = np.diag([1.0 if pairs[i][0] == pairs[i][1] else 2.0 for i in sp_idx])   # h:h metric
Wn = np.array(W, dtype=float)
print("kinetic (s_4^2) form W on h_ij, generalized eigenvalues in the h:h metric:",
      np.round(np.sort(np.linalg.eigvals(np.linalg.solve(G6, Wn)).real), 6))
rng = np.random.default_rng(3)
for trial in range(3):
    q = rng.normal(size=3)
    subs = {s[0]: q[0], s[1]: q[1], s[2]: q[2]}
    q2 = float(np.sum(q * q))
    # spatial TT basis for momentum q: e1,e2 perpendicular to q; TT tensors e1e2+e2e1, e1e1-e2e2
    qh = q / np.linalg.norm(q)
    e1 = np.cross(qh, [1.0, 0.3, -0.2]); e1 /= np.linalg.norm(e1); e2 = np.cross(qh, e1)
    def vec(M):  # symmetric 3x3 -> components in sp_idx order (h_ij with i<=j)
        return np.array([M[pairs[i][0], pairs[i][1]] for i in sp_idx])
    TT = np.array([vec(np.outer(e1, e2) + np.outer(e2, e1)), vec(np.outer(e1, e1) - np.outer(e2, e2))]).T
    for s4 in [0.0, 0.7, 1.9]:
        sub = dict(subs); sub[s[3]] = s4
        Kn = np.array(Kss.subs(sub), dtype=float)
        KTT = TT.T @ Kn @ TT
        MTT = TT.T @ G6 @ TT
        ratio = np.linalg.eigvals(np.linalg.solve(MTT, KTT)).real
        # constraint rows: d Q / d h_{4mu} at h_{4mu}=0, as linear maps on h_ij
        Kts = np.array(K.extract(t_idx, sp_idx).subs(sub), dtype=float)
        cons_on_TT = np.abs(Kts @ TT).max()
        rank_c = np.linalg.matrix_rank(Kts, tol=1e-10)
        if trial == 0:
            print(f"q={np.round(q,3)}, s4={s4}: TT block / (h:h) = {np.round(ratio,10)}  vs (s4^2+q^2)/4 = {(s4**2+q2)/4:.10f};"
                  f" constraints vanish on TT: {cons_on_TT:.1e}; rank of constraint rows = {rank_c}")
# kernel of the constraint rows at generic s4 != 0 = spatial TT (2-dim)?
q = np.array([0.4, -1.3, 0.8]); sub = {s[0]: q[0], s[1]: q[1], s[2]: q[2], s[3]: 0.9}
Kts = np.array(K.extract(t_idx, sp_idx).subs(sub), dtype=float)
u, sv, vt = np.linalg.svd(Kts)
print("constraint rows (4x6) singular values:", np.round(sv, 6), "-> kernel dim", 6 - np.sum(sv > 1e-10))

print("\n-- unreduced temporal-gauge propagator: poles in x = s_4^2 and residue signs --")
x = sp.symbols('x', real=True)
q = [sp.Rational(3, 5), sp.Rational(-4, 5), sp.Rational(1, 2)]
sub = {s[0]: q[0], s[1]: q[1], s[2]: q[2]}
Kx = Kss.subs(sub).subs(s[3]**2, x).subs(s[3], sp.sqrt(x))
detK = sp.factor(sp.simplify(Kx.det()))
print("det K_temporal(x = s_4^2) =", detK)
q2 = sum(qi**2 for qi in q)
print("q^2 =", q2)
# residues of the propagator in the trace direction (h_ij = delta_ij a) and TT direction
Ginv = sp.simplify(Kx.inv())
tr_vec = sp.Matrix([1 if pairs[i][0] == pairs[i][1] else 0 for i in sp_idx])
g_tr = sp.simplify((tr_vec.T * Ginv * tr_vec)[0])
print("trace-trace propagator  G_tr(x) =", sp.factor(g_tr))
print("  (a pole at x = -q^2 with residue of the opposite sign to the TT pole, or no pole + polynomial/1/x")
print("   pieces = non-propagating constraint modes; see report)")
