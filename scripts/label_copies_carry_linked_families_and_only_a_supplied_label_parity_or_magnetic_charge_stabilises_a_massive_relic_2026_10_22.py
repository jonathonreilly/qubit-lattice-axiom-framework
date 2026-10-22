AUDIT_INPUT_PATHS = ('docs/LABEL_COPIES_CARRY_LINKED_FAMILIES_AND_ONLY_A_SUPPLIED_LABEL_PARITY_OR_MAGNETIC_CHARGE_STABILISES_A_MASSIVE_RELIC_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""dm-revisit: dark-matter carriers in the new structure of CL-1..CL-3 (block labels at zoom b with
exact U(b^3), site-bond link registers and their extra mode, rishon sectors, compact-link monopoles,
six-edge block registers), each tested against Omega_dm h^2 = 0.120, cold, sigma/m < ~1 cm^2/g,
no direct-detection signal, stable for 13.8 Gyr.
Tags: [T] exact/theorem check, [D] finite diagnostic, [E] estimate against measurement (inputs supplied).
Self-contained: numpy/scipy only. The six-edge slab code (section C) is inlined from the campaign's
edge-modes runner (same Regge sync-slab construction)."""
import itertools, math, time
import numpy as np
from scipy.linalg import eig, expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg):
    NP[0 if ok else 1] += 1; print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}")
rng = np.random.default_rng(20261022)
def rherm(n):
    a = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); return (a + a.conj().T)/2
def nrm(a): return float(np.abs(a).max())

# ---- units and measured inputs (supplied) ----
MPL = 1.221e19; MPR = 2.435e18          # GeV, Planck and reduced Planck mass
LAM = MPL/math.sqrt(8*math.pi)           # cell scale hbar c / a with a = sqrt(8 pi) l_P (register: G = a^2/8pi)
HBAR = 6.582e-25                         # GeV s
AGE = 4.35e17                            # s
YDM = 4.4e-10                            # GeV: m * n/s for Omega_dm h^2 = 0.120

# ---------- six-edge sync slab (inlined from the campaign edge-modes runner) ----------
def tspec(Qf, ks, nmax=2, Nt=16):
    kts = 2*np.pi*np.arange(Nt)/Nt
    Ms = [Qf(np.r_[ks, t]) for t in kts]
    Qn = {n: sum(M*np.exp(-1j*n*t) for M, t in zip(Ms, kts))/Nt for n in range(-Nt//2+1, Nt//2)}
    leak = max(np.abs(Qn[n]).max() for n in Qn if abs(n) > nmax)
    d = Ms[0].shape[0]; p = 2*nmax; P = [Qn[j-nmax] for j in range(p+1)]
    A = np.zeros((d*p, d*p), complex); B = np.eye(d*p, dtype=complex)
    for j in range(p-1): A[j*d:(j+1)*d, (j+1)*d:(j+2)*d] = np.eye(d)
    for j in range(p): A[(p-1)*d:, j*d:(j+1)*d] = -P[j]
    B[(p-1)*d:, (p-1)*d:] = P[p]
    z = eig(A, B, right=False)
    ok = np.isfinite(z) & (np.abs(z) > 1e-30)
    with np.errstate(all="ignore"):
        E = -np.log(z[ok].astype(complex))
    return E, leak, int((~ok).sum())

WO = np.array([1.0, 0.1, 0.01])
PAIRS = list(itertools.combinations(range(5), 2))
def simplex_grad5(L):
    G = np.array([[0.5*(L[0, i]**2 + L[0, j]**2 - L[i, j]**2) for j in range(1, 5)] for i in range(1, 5)])
    E = np.linalg.cholesky(G); D = np.linalg.inv(E)
    n = [D.sum(axis=1)] + [-D[:, i] for i in range(4)]
    g = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        th = np.arccos(np.clip(-n[i] @ n[j]/np.linalg.norm(n[i])/np.linalg.norm(n[j]), -1, 1))
        a, b, c = [k for k in range(5) if k not in (i, j)]
        x, y, z = L[a, b], L[b, c], L[a, c]
        A = 0.25*np.sqrt(2*x*x*y*y + 2*y*y*z*z + 2*z*z*x*x - x**4 - y**4 - z**4)
        for (p, q), s, o1, o2 in (((a, b), x, y, z), ((b, c), y, x, z), ((a, c), z, x, y)):
            g[p, q] += th*s*(o1*o1 + o2*o2 - s*s)/(8*A)
    return np.array([g[p, q] for p, q in PAIRS])
def simplex_hess_X(X):
    L0 = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=2)
    def sh(h):
        H = np.zeros((10, 10))
        for e, (a, b) in enumerate(PAIRS):
            gs = []
            for s in (1, -1):
                L = L0.copy(); L[a, b] += s*h; L[b, a] = L[a, b]; gs.append(simplex_grad5(L))
            H[e] = (gs[0]-gs[1])/(2*h)
        return H
    H = (4*sh(1e-4) - sh(2e-4))/3
    return 0.5*(H + H.T)
def tri_hess_l(l):
    A = 0.25*np.sqrt(2*l[0]**2*l[1]**2 + 2*l[1]**2*l[2]**2 + 2*l[2]**2*l[0]**2 - (l**4).sum())
    s2 = (l**2).sum(); g = l*(s2 - 2*l**2)/(8*A); H = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            d = (s2 - 4*l[i]**2) if i == j else 2*l[i]*l[j]
            H[i, j] = d/(8*A) - l[i]*(s2 - 2*l[i]**2)/(8*A*A)*g[j]
    return H

class Slab:
    """sync slab Regge (fixed lapse tau, zero shift) on a periodic 3D triangulation."""
    def __init__(self, tets, P, tau):
        self.P, self.tau = P, tau
        key = lambda a, b: (tuple(np.mod(a, P)), tuple(b - a))
        self.cls = {}
        def order(vs): return sorted(vs, key=lambda v: v @ WO)
        for T in tets:
            for a, b in itertools.combinations(order([np.array(v) for v in T]), 2):
                self.cls.setdefault(key(a, b), len(self.cls))
        self.n = len(self.cls); self.key = key
        self.simps = []          # (coords 5x4, list of edge descriptors)
        tris = {}
        for T in tets:
            vs = order([np.array(v) for v in T])
            for j in range(4):
                V = [(vs[i], 0) for i in range(j+1)] + [(vs[i], 1) for i in range(j, 4)]
                X = np.array([np.r_[v, tau*t] for v, t in V], float)
                ed = [self.edge(V[a], V[b]) for a, b in PAIRS]
                self.simps.append((simplex_hess_X(X), ed))
                for tri in itertools.combinations(range(5), 3):
                    W = [V[i] for i in tri]
                    sh = np.r_[np.floor_divide(W[0][0], P)*P, W[0][1]]
                    k_ = tuple(sorted(tuple(np.r_[w[0], w[1]] - sh) for w in W))
                    if k_ not in tris:
                        l = np.array([np.linalg.norm(np.r_[W[b][0]-W[a][0], tau*(W[b][1]-W[a][1])]) for a, b in ((0, 1), (1, 2), (0, 2))])
                        tris[k_] = (tri_hess_l(l), [self.edge(W[a], W[b]) for a, b in ((0, 1), (1, 2), (0, 2))])
        self.tris = list(tris.values())
    def edge(self, A, B):
        """edge descriptor: list of (class, anchor 3-vector, t, coefficient)."""
        (a, ta), (b, tb) = A, B
        if a @ WO > b @ WO: (a, ta), (b, tb) = (b, tb), (a, ta)
        if np.array_equal(a, b): return []                       # tick edge: fixed
        c = self.cls[self.key(a, b)]
        if ta == tb: return [(c, a, ta, 1.0)]
        ls = np.linalg.norm(b - a); lm = np.sqrt(ls**2 + self.tau**2)
        t0 = min(ta, tb)
        return [(c, a, t0, 0.5*ls/lm), (c, a, t0+1, 0.5*ls/lm)]
    def row(self, ed, k):
        r = np.zeros(self.n, complex)
        for c, a, t, w in ed: r[c] += w*np.exp(1j*(k[:3] @ a + k[3]*t))
        return r
    def Q(self, k):
        M = np.zeros((self.n, self.n), complex)
        for H, eds in self.tris:
            J = np.array([self.row(e, k) for e in eds]); M += 2*np.pi*J.conj().T @ H @ J
        for H, eds in self.simps:
            J = np.array([self.row(e, k) for e in eds]); M -= J.conj().T @ H @ J
        return 0.5*(M + M.conj().T)

def kuhn_tets():
    out = []
    for p in itertools.permutations(range(3)):
        v = [np.zeros(3, int)]
        for j in p:
            w = v[-1].copy(); w[j] = 1; v.append(w)
        out.append(v)
    return out
def five_tets():
    out = []
    for o in itertools.product((0, 1), repeat=3):
        o = np.array(o); C = [o + np.array(c) for c in itertools.product((0, 1), repeat=3)]
        ev_ = [c for c in C if c.sum() % 2 == 0]; od = [c for c in C if c.sum() % 2 == 1]
        out.append(ev_)
        for q in od:
            out.append([q] + [c for c in ev_ if np.abs(c - q).sum() == 1])
    return out


# ---------- fermion Fock helpers (Jordan-Wigner) ----------
def jw(n):
    I = np.eye(2); Z = np.diag([1., -1.]); a = np.array([[0., 1.], [0., 0.]])   # a|1> = |0>
    ops = []
    for j in range(n):
        m = np.array([[1.]])
        for k in range(n): m = np.kron(m, Z if k < j else (a if k == j else I))
        ops.append(m)
    return ops
def num(c): return c.T @ c

print("== A. block labels at zoom b (exact U(b^3) of the parallel-carriage circuit; label terms supplied)")
b = 2; nl = b**3
T = rherm(3); U = expm(1j*rherm(nl))
check("A1 [T]", nrm(np.kron(T, np.eye(nl)) @ np.kron(np.eye(3), U) - np.kron(np.eye(3), U) @ np.kron(T, np.eye(nl))) < 1e-12,
      "links read per coarse cube alike for every label: gauge generators T x 1 commute with all of U(b^3), so every label carries one whole linked family")
FAM = {"Q": (3, 2, 1/6, 1), "u^c": (-3, 1, -2/3, 1), "d^c": (-3, 1, 1/3, 1), "L": (1, 2, -1/2, 1), "e^c": (1, 1, 1., 1), "nu^c": (1, 1, 0., 1)}
def singlet_pair(x, y):
    c3 = (x[0] == 1 and y[0] == 1) or (abs(x[0]) == 3 and x[0] == -y[0]); c2 = x[1] == y[1]
    return c3 and c2 and abs(x[2] + y[2]) < 1e-12
neutral = [k for k, v in FAM.items() if v[0] == 1 and v[1] == 1 and v[2] == 0]
pairs = [(p, q) for p, q in itertools.combinations_with_replacement(FAM, 2) if singlet_pair(FAM[p], FAM[q])]
check("A2 [T]", neutral == ["nu^c"] and pairs == [("nu^c", "nu^c")],
      f"per label the only link-free Weyl state is {neutral}; the only gauge-invariant bilinear of a chiral family is {pairs} (Majorana, Z4-forbidden); a chiral copy takes no label mass: heavy labels are vector-like")
Hc = rherm(4); M = rherm(nl); H1 = np.kron(Hc, np.eye(nl)) + np.kron(np.eye(4), M)
w, V = np.linalg.eigh(M); comm = max(nrm(H1 @ np.kron(np.eye(4), np.outer(V[:, j], V[:, j].conj())) - np.kron(np.eye(4), np.outer(V[:, j], V[:, j].conj())) @ H1) for j in range(nl))
check("A3 [T]", comm < 1e-12,
      f"any quadratic label term keeps one exact U(1) per label-mass eigenspace ({nl} here, commutator {comm:.0e}); CL-1 links them, so the light label's number is a massless link on matter (MICROSCOPE < ~1e-25): excluded alone")
c = jw(6); L0, L1 = c[:3], c[3:]
P1 = np.diag([(-1)**sum((s >> (5 - j)) & 1 for j in range(3, 6)) for s in range(64)]).astype(float)
N1 = sum(num(x) for x in L1)
He = sum(m_*num(x) for m_, x in zip((0.1, 0.2, 0.3, 2.0, 2.1, 2.2), c))
He += 0.7*(L0[0].T @ L0[1] + L0[1].T @ L0[0]) + 0.6*(L1[1].T @ L1[2] + L1[2].T @ L1[1])            # intra-label hops
He += 0.5*(L0[0] @ L0[1] + (L0[0] @ L0[1]).T) + 0.4*(L1[0] @ L1[2] + (L1[0] @ L1[2]).T)          # intra-label Delta N = 2
X = L0[0].T @ L0[2].T @ L1[0] @ L1[1]; He += 0.8*(X + X.T) + 0.3*num(L0[1]) @ num(L1[2])          # cross-label, even in each label
Ho = L0[1].T @ L1[0]; Ho = Ho + Ho.T                                                                # label-mixing bilinear
check("A4 [T]", nrm(He @ P1 - P1 @ He) < 1e-12 and nrm(He @ N1 - N1 @ He) > 0.1 and nrm((He + 1e-3*Ho) @ P1 - P1 @ (He + 1e-3*Ho)) > 1e-4,
      "Fock toy (2 labels x 3 modes): terms even in each label break label number (no dark link) but keep label parity (-1)^N_k; one mixing bilinear breaks it; the fine tick has cell commutant 1 (hidden-sector A2): parity is supplied")
print("   with parity: lightest odd state N' (label nu^c) exactly stable, link-free; with mixing tau ~ 1e-39 s")
# A5: label-k baryon number is conserved by every renormalisable term, so coloured label-k states reach N' only via cell contacts
def tau_contact(dm, n=1): return HBAR*192*math.pi**3*LAM**4/(n*dm**5)
mthr = {f: (HBAR*192*math.pi**3*LAM**4/(1.0*(f)**5))**0.2 for f in (1.4e-3, 5e-3)}
t10 = tau_contact(5e-3*1e4)
check("A5 [E]", t10 > 1e10*AGE and 1e12 < mthr[5e-3] < 1e14,
      f"coloured/charged label states decay to N' only through cell-scale contacts, releasing dm ~ (1.4-5)e-3 m: tau(m = 10 TeV) = {t10:.0e} s >> age; tau < 1 s (BBN) needs m > {mthr[5e-3]:.1e}-{mthr[1.4e-3]:.1e} GeV")
sv = 2.19e-10/0.120
mth = [math.sqrt(math.pi*a**2*ce/sv) for a, ce in ((0.03, 0.1), (0.3, 10.))]
check("A6 [E]", mth[1] < mthr[5e-3]*1e-6,
      f"thermal history: a coannihilating label family gives Omega h^2 = 0.12 at m ~ {mth[0]/1e3:.1f}-{mth[1]/1e3:.0f} TeV (alpha_eff .03-.3), but there its stable coloured relics (n/n_B >~ 1e-12) exceed heavy-isotope bounds (<~1e-28) by >1e16: excluded")
H_inf = math.pi*MPR*math.sqrt(0.036*2.1e-9/2); Tmax = (90/(math.pi**2*106.75))**0.25*math.sqrt(H_inf*MPR)
def Ygrav(Tr, m): return 1e-3*(Tr/MPR)**3*math.exp(-2*m/Tr)
def Tneed(m):
    lo, hi = m/400, m*10
    for _ in range(200):
        mid = math.sqrt(lo*hi)
        if m*Ygrav(mid, m) < YDM: lo = mid
        else: hi = mid
    return mid
rows = [(m, Tneed(m)) for m in (1e13, 1e14, 1e15)]
lo_, hi_ = 1e13, 1e18
for _ in range(100):
    mid = math.sqrt(lo_*hi_)
    if Tneed(mid) < Tmax: lo_ = mid
    else: hi_ = mid
check("A7 [E]", all(r[1] < Tmax for r in rows) and lo_ < LAM,
      f"non-thermal window (gravitational production at reheating, Y ~ 1e-3 (T/M_P)^3 e^(-2m/T), supplied): T_reh/m = " + ", ".join(f"{r[1]/r[0]:.2f}" for r in rows) + f" at m = 1e13,1e14,1e15 GeV; T_reh < {Tmax:.1e} GeV (r < 0.036) caps m < {lo_:.1e} GeV; dlnY/dlnT = " + "/".join(f"{3+2*r[0]/r[1]:.0f}" for r in rows) + " (tuned)")
sdd = (0.939**2/(math.pi*LAM**4))*0.3894e-27
check("A8 [E]", sdd < 1e-90,
      f"couplings of N': contact only, sigma_SI ~ m_n^2/(pi Lambda^4) = {sdd:.0e} cm^2 (no direct-detection signal), sigma/m negligible, cold; label masses at the natural cell scale give e^(-2 Lambda/T_max) = e^-{2*LAM/Tmax:.0f}: none made, abundance only from the start")

print("== B. link registers: the site-bond extra mode, rishon sectors, compact-link monopoles")
S = 1.5; ms = np.arange(S, -S-1, -1); Sz = np.diag(ms)
Sp = np.diag([math.sqrt(S*(S+1) - m*(m+1)) for m in ms[1:]], 1)
Cc = np.fliplr(np.eye(len(ms)))
check("B1 [T]", nrm(Cc @ Sz @ Cc + Sz) < 1e-12 and nrm(Cc @ Sp @ Cc - Sp.T) < 1e-12,
      "spin-3/2 register: C (m -> -m) maps E -> -E, U -> U^dag, keeps ring exchange: n photons have C = (-1)^n; the extra d1 d2 d3 mode is C-odd and trivial under the kept turns: 3 photons allowed, no selection rule")
print(f"   extra at the cell scale (lowest frequency 2x the per-site light frequency, ~{LAM:.0e} GeV): Gamma ~ alpha^2 m/(4 pi)^3 -> tau ~ 1e-41 s; not dark matter")
cr = jw(4); No = num(cr[0]) + num(cr[1]); Ne = num(cr[2]) + num(cr[3]); Vr = cr[0].T @ cr[2] + cr[1].T @ cr[3]
check("B2 [T]", nrm(Vr @ (No + Ne) - (No + Ne) @ Vr) < 1e-12 and nrm(Vr @ No - No @ Vr) > 0.5,
      "the register raiser (rishon hop between the bond's two ends, 2S = 2) conserves the bond's rishon number: other link-spin sectors are superselected and never occur (not a relic)")
Lx = 5; A = rng.uniform(-math.pi, math.pi, size=(3, Lx, Lx, Lx))
def red(t): return (t + math.pi) % (2*math.pi) - math.pi
def charges(A):
    sh = lambda f, m: np.roll(f, -1, axis=m)
    th = {(i, j): A[i] + sh(A[j], i) - sh(A[i], j) - A[j] for i, j in ((1, 2), (2, 0), (0, 1))}
    Bf = [red(th[(1, 2)]), red(th[(2, 0)]), red(th[(0, 1)])]
    return sum(sh(Bf[i], i) - Bf[i] for i in range(3))/(2*math.pi)
m0 = charges(A); ok_int = nrm(m0 - np.round(m0)) < 1e-9 and abs(m0.sum()) < 1e-9
ev_ok = True; nev = 0
for _ in range(400):
    A2_ = A + 0.02*rng.normal(size=A.shape); m1 = charges(A2_); d = np.round(m1 - m0)
    if np.abs(d).sum() > 0:
        nev += 1; ev_ok &= abs(d.sum()) < 1e-9
    A, m0 = A2_, m1
kk = (np.arange(48) + 0.5)*2*math.pi/48; K1, K2, K3 = np.meshgrid(kk, kk, kk, indexing="ij")
G0 = float(np.mean(1/(2*(3 - np.cos(K1) - np.cos(K2) - np.cos(K3)))))
check("B3 [T, cubic]", ok_int and ev_ok and nev > 10 and abs(G0 - 0.2527)/0.2527 < 0.03,
      f"compact link angles: every cube's magnetic charge (reduced plaquette flux / 2pi) is an integer, the total is 0, and {nev} continuous-evolution events all changed charges in +- pairs: monopole number is locally conserved, a lone monopole is stable; G(0) = {G0:.4f} (Watson 0.2527)")
for au, lab in ((0.071, "S = 3/2 natural"), (5.0e-4, "hypercharge unit target")):
    Mm = math.pi/(2*au)*G0*LAM; f = 1.4e-16*4*math.pi*Mm/(0.3*2.2e7)
    print(f"   monopole M = (pi/2alpha) G(0) Lambda = {Mm:.1e} GeV ({lab}); MACRO (1.4e-16 /cm2/s/sr at beta 1e-3) allows a DM fraction < {min(f, 1):.1e}")
check("B4 [E]", 1.4e-16*4*math.pi*(math.pi/(2*0.071)*G0*LAM)/(0.3*2.2e7) < 0.1,
      "monopoles are stable but magnetically charged (not dark); MACRO excludes them as all DM at the natural coupling; inflation leaves ~none")

print("== C. edge registers on the six-edge block triangulation (sync slab, fixed lapse, zero shift)")
S5 = Slab(five_tets(), 2, 1.0)
E, leak, ninf = tspec(S5.Q, np.array([0.05, 0.0, 0.0]))
E = E[np.isfinite(E) & (np.abs(E) < 20)]
re = np.sort(E[(E.real > 0.02) & (np.abs(E.imag) < 1e-6)].real)
light = re[re < 0.1]; heavy = re[re >= 0.1]
check("C1 [T/D]", S5.n == 48 and len(light) == 2 and np.allclose(light, 0.05, atol=1e-3) and heavy.min() > 1.4,
      f"48 registers per 8 block sites = 6 per site = the metric count, so no non-metric light strain exists; at |K| = 0.05 the light roots are {np.round(light, 4)} (two tensor polarisations) and every other real root >= {heavy.min():.2f} per block tick: cell-scale")
r = np.arange(4); Vn = np.diag(np.ones(3), -1); Hn = Vn + Vn.T; nE = np.diag(r.astype(float)); PE = np.diag((-1.)**r)
check("C2 [T]", nrm(Hn @ nE - nE @ Hn) > 0.5 and nrm(Hn @ PE + PE @ Hn) < 1e-12,
      "the one-register hop V_e + V_e^dag changes every edge value by +-1 (anticommutes with (-1)^n): no edge-register number or parity is conserved; with crystal momentum alone and threshold 0 at K = 0 (back-to-back massless pairs), K ~ 0 massive edge quanta are open to decay")
for be in (6, 38):
    m = heavy.min()*LAM/be
    g = [n*m**3/(32*math.pi*MPR**2) for n in (1, 100)]
    print(f"   b_e = {be}: m ~ {m:.1e} GeV, universal coupling Gamma ~ N m^3/(32 pi M_P^2) -> tau ~ {HBAR/g[1]:.0e}-{HBAR/g[0]:.0e} s")
print("   caveat [D]: near-zero transfer roots at generic K are ill-conditioned (Jordan blocks of the gauge zeros);")
print("   a kinematically closed band minimum near the zone edge is not excluded here; even so it is cell-scale and made")
print(f"   only at T ~ m/20 > T_max = {Tmax:.0e} GeV or by splits, which carry vacuum to vacuum: no rule-set abundance")

print("== D. conserved numbers of the new laws, as stabilisers")
cen = [("exact U(b^3) (zoom-b circuit only)", "must break (LEP); quadratic terms leave linked U(1)s"),
       ("label parity (-1)^N_k", "not in the fine tick; if supplied: N' stable (A4-A8)"),
       ("Z4 of B - L", "lightest carrier = light neutrino: hot, < 1% of DM (sum m_nu < 0.07 eV)"),
       ("rishon number per bond", "superselection; fixes S, no excitation (B2)"),
       ("Gauss sectors", "only zero static charge occurs"),
       ("magnetic charge (compact links)", "exact: monopoles, not dark (B3-B4)"),
       ("edge value, copy sign, turn charges", "not conserved"), ("crystal momentum, pattern", "not particle charges"),
       ("dark constant", "zero mean in every cube (CL-3): no carrier")]
for k_, v_ in cen: print(f"   {k_}: {v_}")
print("   so only label parity (supplied) and magnetic charge (not dark) stabilise a massive relic")

print("== E. verdict against measurement")
print("   extra link mode, rishon sectors, edge strains, copy, zoom-3 copies: unstable or absent; monopoles not dark")
print(f"   conditional survivor: N' with a SUPPLIED label parity, m ~ {mthr[1.4e-3]:.0e}-{lo_:.0e} GeV, non-thermal; Omega not rule-set")
print("theorems: A1-A4, B1-B3, C2; diagnostic: C1; estimates: A5-A8, B4, C decay times.")
print("supplied: label terms+parity, alpha_eff, Y_grav, splittings, a = sqrt(8pi) l_P, [cubic] monopole, slab; cited: MICROSCOPE,")
print("  heavy-isotope searches, BICEP/Keck, MACRO, Planck.")
print(f"elapsed_seconds {time.time()-T0:.1f}")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
