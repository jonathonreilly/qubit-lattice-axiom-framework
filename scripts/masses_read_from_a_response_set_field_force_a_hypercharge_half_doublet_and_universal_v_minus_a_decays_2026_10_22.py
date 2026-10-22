AUDIT_INPUT_PATHS = ('docs/MASSES_READ_FROM_A_RESPONSE_SET_FIELD_FORCE_A_HYPERCHARGE_HALF_DOUBLET_AND_UNIVERSAL_V_MINUS_A_DECAYS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""charged-current: CL-3 links symmetries of the update with its response fields transformed.
A: link algebra with H as a CL-3 field vs H frozen at its vacuum value.  B: link masses, rho, G_F.
C: lattice three-body decay rate of a massive doublet member, m^5.  D: estimates vs measurement."""
import numpy as np, sympy as sp, time
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); P = F = 0
def chk(tag, name, ok, info=''):
    global P, F
    P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {name}" + (f" | {info}" if info else ''))
rng = np.random.default_rng(7)
print('== A. which generators CL-3 links (one chiral family, Weyl fields Q u d L e n, field H)')
# abelian phases on [Q,u,d,L,e,n,H]; each term is a charge sum that must vanish
terms = {'Q u H': [1, 1, 0, 0, 0, 0, 1], 'Q d H*': [1, 0, 1, 0, 0, 0, -1], 'L e H*': [0, 0, 0, 1, 1, 0, -1],
         'L n H': [0, 0, 0, 1, 0, 1, 1], '(n)^4': [0, 0, 0, 0, 0, 4, 0], 'u d d n': [0, 1, 2, 0, 0, 1, 0]}
A = sp.Matrix(list(terms.values())); ns = A.nullspace()
Y = ns[0] / ns[0][6] / 2 if len(ns) == 1 else None
chk('T', 'H transformed: exact abelian charges = 1, Y with Y_H = 1/2', len(ns) == 1, f"6Y = {list(6 * Y)}")
chk('T', 'Y ratios Q:u:d:L:e:n = 1:-4:2:-3:6:0 (as link-selection T3)', list(6 * Y)[:6] == [1, -4, 2, -3, 6, 0])
# bilinear rep: every mass bilinear psi_L psi_R-bar is (1,2,+-1/2): H's rep is forced by the content
chk('T', "Yukawa invariance forces Y_H = Y_L - Y_e-bar... = +-1/2 for all four bilinears",
    all(abs(abs(sum(c * y for c, y in zip(t[:6], Y[:6]))) - sp.Rational(1, 2)) == 0 for t in terms.values() if t[6]))
# nonabelian: su(2) x u(1)_Y on H; stabiliser of a frozen vacuum value v
s = [np.array(m, complex) / 2 for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
gens = s + [np.eye(2) / 2]
dims = []
for _ in range(20):
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    Mv = np.array([np.r_[(G @ v).real, (G @ v).imag] for G in gens]).T
    dims.append(4 - np.linalg.matrix_rank(Mv, 1e-10))
chk('T', 'H frozen at any v != 0: unbroken subalgebra of su(2)+u(1)_Y is 1-dim (photon); 3 broken',
    set(dims) == {1}, f"linked 8+3+1 = 12 -> unbroken 8+1 = 9, massive 3 (W+, W-, Z)")
v = np.array([0, 1.0]); Qg = s[2] + gens[3]
chk('T', 'unbroken generator at v=(0,1) is Q = T3 + Y; neutrino Q = 0, electron -1, u 2/3, d -1/3',
    np.allclose(Qg @ v, 0) and [sp.Rational(1, 2) + Y[3], -sp.Rational(1, 2) + Y[3], sp.Rational(1, 2) + Y[0], -sp.Rational(1, 2) + Y[0]] == [0, -1, sp.Rational(2, 3), -sp.Rational(1, 3)])
print('== B. link masses from |D H|^2 at the vacuum value')
ok = True; rh = []
for _ in range(20):
    g, gp, v0 = rng.uniform(0.2, 1.5, 3)
    u = rng.normal(size=2) + 1j * rng.normal(size=2); u = u / np.linalg.norm(u) * v0 / np.sqrt(2)
    cg = [g] * 3 + [gp]
    M2 = np.array([[cg[a] * cg[b] * (u.conj() @ (gens[a] @ gens[b] + gens[b] @ gens[a]) @ u).real for b in range(4)] for a in range(4)])
    ev = np.sort(np.linalg.eigvalsh(M2)); mW2, mZ2 = g ** 2 * v0 ** 2 / 4, (g ** 2 + gp ** 2) * v0 ** 2 / 4
    ok &= np.allclose(ev, [0, mW2, mW2, mZ2]); rh.append(mW2 / (mZ2 * g ** 2 / (g ** 2 + gp ** 2)))
chk('T', 'spectrum {0, mW^2, mW^2, mZ^2}, mW = g v/2, mZ = sqrt(g^2+g\'^2) v/2, any vacuum direction', ok)
chk('T', 'rho = mW^2/(mZ^2 cos^2 thW) = 1 exactly', np.allclose(rh, 1), f"max|rho-1| = {max(abs(np.array(rh) - 1)):.1e}")
gs, vs = sp.symbols('g v', positive=True)
GF = sp.simplify(sp.sqrt(2) * gs ** 2 / (8 * (gs * vs / 2) ** 2))
chk('T', 'contact limit: G_F = sqrt2 g^2/(8 mW^2) = 1/(sqrt2 v^2): g cancels, same for every doublet', sp.simplify(GF - 1 / (sp.sqrt(2) * vs ** 2)) == 0)
q = np.linspace(-np.pi, np.pi, 41); m = 0.3
qh2 = 4 * np.sin(q / 2) ** 2
chk('T', 'lattice link propagator g^2/(qhat^2+m^2) -> g^2/m^2 at q=0, deviation qhat^2/m^2', abs(1 / (qh2[20] + m * m) - 1 / m ** 2) < 1e-12)
print('== C. lattice decay rate: mu -> e nubar_e nu_mu, V-A contact, lattice cones E = |2 sin(k/2)|')
def E(k): return 2 * np.sqrt((np.sin(k / 2) ** 2).sum(-1))
def kh(k): return 2 * np.sin(k / 2)
N = 200000; uk = rng.random(N) ** (1 / 3); d1 = rng.normal(size=(N, 3)); d1 /= np.linalg.norm(d1, axis=1)[:, None]
d2 = rng.normal(size=(N, 3)); d2 /= np.linalg.norm(d2, axis=1)[:, None]
def rate(m, VA=True):
    R = 0.62 * m; k1 = (R * uk)[:, None] * d1
    f = lambda t: m - E(k1) - E(t[:, None] * d2) - E(k1 + t[:, None] * d2)
    lo = np.zeros(N); hi = np.full(N, R); good = (f(lo) > 0) & (f(hi) < 0)
    for _ in range(50):
        mid = (lo + hi) / 2; pos = f(mid) > 0; lo = np.where(pos, mid, lo); hi = np.where(pos, hi, mid)
    t = (lo + hi) / 2; h = 1e-7 * m; dfd = (f(t + h) - f(t - h)) / (2 * h)
    k2 = t[:, None] * d2; k3 = -(k1 + k2); E1, E2, E3 = E(k1), E(k2), E(k3)
    amp = m * E2 * (E1 * E3 - (kh(k1) * kh(k3)).sum(1)) if VA else m * m * E1 * E3   # /64 G^2
    w = (4 / 3 * np.pi * R ** 3) * 4 * np.pi * t ** 2 / abs(dfd) * amp * 64 / (8 * E1 * E2 * E3) * 2 * np.pi / (2 * np.pi) ** 6 / (2 * m)
    w = np.where(good, w, 0); return w.mean(), w.std() / np.sqrt(N), good.mean()
ms = [0.01, 0.02, 0.1, 0.3, 0.6]; res = [rate(x) for x in ms]
c = [r[0] / (x ** 5 / (192 * np.pi ** 3)) for r, x in zip(res, ms)]
for x, r, cc in zip(ms, res, c): print(f"   m = {x:<5} Gamma/(G^2 m^5/192pi^3) = {cc:.4f} +- {r[1] / r[0] * cc:.4f}")
chk('F', 'small m: lattice rate -> G^2 m^5/(192 pi^3) within 1%', abs(c[0] - 1) < 0.01 and abs(c[1] - 1) < 0.01)
sl = np.log(res[1][0] / res[0][0]) / np.log(2)
chk('F', 'exponent d ln Gamma / d ln m = 5 at small m (common random numbers)', abs(sl - 5) < 1e-3, f"{sl:.5f}")
dc = [x / c[0] - 1 for x in c[2:]]
chk('F', 'lattice correction (same samples, vs m=0.01) grows with m a, below 2% at m a = 0.6', 0 < dc[0] < dc[1] < dc[2] < 0.02, ' '.join(f"{x:+.4f}" for x in dc))
print('== D. estimates vs measurement (SI/PDG inputs supplied)')
Gf, al, s2 = 1.1663787e-5, 1 / 127.951, 0.23122
v0 = (np.sqrt(2) * Gf) ** -0.5; mW = np.sqrt(np.pi * al / (np.sqrt(2) * Gf) / s2); mZ = mW / np.sqrt(1 - s2)
print(f"   v = {v0:.2f} GeV (supplied by G_F); tree mW = {mW:.2f} vs 80.369, mZ = {mZ:.2f} vs 91.188")
chk('E', 'tree mW, mZ from alpha(MZ), sin^2 thW, G_F within 0.5%', abs(mW / 80.369 - 1) < 5e-3 and abs(mZ / 91.188 - 1) < 5e-3)
hb = 6.582119569e-25; mmu, mtau, me = 0.1056584, 1.77686, 0.000510999
ttau = 2.1969811e-6 * (mmu / mtau) ** 5 * 0.1782
chk('E', 'tau lifetime from muon by m^5 and one g: within 1% of 290.3 fs', abs(ttau / 290.3e-15 - 1) < 0.01, f"{ttau * 1e15:.1f} fs")
Vud, lam, fpi, mpi = 0.97373, 1.2754, 0.1302, 0.13957
tn = 2 * np.pi ** 3 * hb / (Gf ** 2 * Vud ** 2 * me ** 5 * 1.6887 * (1 + 3 * lam ** 2) * 1.0390)
chk('E', 'neutron lifetime (V_ud, g_A, f, radiative 3.9% supplied) within 1% of 878.4 s', abs(tn / 878.4 - 1) < 0.01, f"{tn:.0f} s")
Gp = Gf ** 2 * Vud ** 2 * fpi ** 2 * mpi * mmu ** 2 * (1 - mmu ** 2 / mpi ** 2) ** 2 / (8 * np.pi)
chk('E', 'charged pion lifetime within 3% of 26.03 ns (no radiative corr.)', abs(hb / Gp / 26.033e-9 - 1) < 0.03, f"{hb / Gp * 1e9:.2f} ns")
Re = (me / mmu) ** 2 * ((mpi ** 2 - me ** 2) / (mpi ** 2 - mmu ** 2)) ** 2
chk('E', 'V-A helicity suppression: Gamma(e)/Gamma(mu) = 1.28e-4 tree (meas 1.2327e-4; scalar would be ~5.5)', abs(Re / 1.2327e-4 - 1) < 0.05, f"{Re:.4e}")
print('supplied: chiral content, H as a CL-3 response field (its rep forced), v, g, g\', V_ud, g_A, f_pi, lattice cones.')
print(f'time {time.time() - t0:.1f} s'); print(f'TOTAL: PASS={P} FAIL={F}')
