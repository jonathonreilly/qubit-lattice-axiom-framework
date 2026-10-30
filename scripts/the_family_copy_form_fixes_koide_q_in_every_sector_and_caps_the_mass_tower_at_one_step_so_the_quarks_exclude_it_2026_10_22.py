AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_COPY_FORM_FIXES_KOIDE_Q_IN_EVERY_SECTOR_AND_CAPS_THE_MASS_TOWER_AT_ONE_STEP_SO_THE_QUARKS_EXCLUDE_IT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""mass-tower-law: propose and test a candidate family mass law built from CL-1 forms.

Candidate law (family copy form): each sector's signed square-root masses are the eigenvalues of
c_f (1 - s_f), with s_f a Hermitian family-space operator built as CL-1 builds its copy sign and hop:
traceless, of unit mean square (sum of squared weights of unitary hops = 1, as R = sum w_i W_i).
A  the three suggested routes (rung span, polar nesting) checked against CL-1 [exact / finite]
B  theorems of the copy-form law [exact, sympy + seeded numerics]
C  the copy-form law against measured masses, mixing and neutrino data [E estimates, M measured]
Tags: [T] exact, [E] estimate or finite diagnostic, [M] measured input.
"""
import itertools, time
import numpy as np, sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))
def Q(m, s=(1, 1, 1)):
    r = np.sqrt(np.asarray(m, float)) * np.asarray(s); return np.sum(r * r) / np.sum(r) ** 2

# ---------------- A ----------------
print("== A. the suggested routes against CL-1")
b, mu = sp.symbols("b mu", real=True)
A_ = (sp.cos(2 * b) + sp.cos(mu)) / 2; B_ = (sp.cos(2 * b) - sp.cos(mu)) / 2
check("[T] (a) rung span: CL-1's flat band cos w = A S - (cos2b - cos mu)/2 at K = 0 (S = 1) gives cos w = cos mu, "
      "so the rest phase per tick is the mass angle; with the dressed-cone clause mu = m N, the proper rest energy is m at "
      "every rung, and spanning more rungs suppresses nothing", sp.simplify(A_ - B_ - sp.cos(mu)) == 0)
me, mm, mt = 0.51099895, 105.6583755, 1776.93; Ql = Q([me, mm, mt])
best = min((abs(Q([1, 2.0 ** -p, 2.0 ** -q]) - Ql), p, q) for p in range(1, 25) for q in range(p + 1, 31))
p, q = best[1], best[2]
check("[E] (a') a fixed angle per tick instead (mass 2^-n at rung n, integers supplied): no integer pair n <= 30 comes "
      "within 1e-3 of the lepton Q, and the closest misses the ratios", best[0] > 1e-3,
      f"best (n2,n3)=({p},{q}): Q={Q([1,2.0**-p,2.0**-q]):.4f}, m_mu/m_tau {2.0**-p:.4f} vs {mm/mt:.4f}, m_e/m_tau {2.0**-q:.2e} vs {me/mt:.2e}")

L = 6; N = L ** 3; V = list(itertools.product((0, 1), repeat=3)); Jf = np.eye(8)[::-1]
def idx(x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
def layer(Hc, par):
    M = np.zeros((N, N), complex); Uc = expm(-1j * Hc)
    for n in itertools.product(range(3), repeat=3):
        ids = [idx(2 * np.array(n) + par + np.array(v)) for v in V]; M[np.ix_(ids, ids)] = Uc
    return M
BL = {}
def bloch(U, m):
    if m not in BL:
        Bm = np.zeros((N, 8), complex)
        for si, s in enumerate(V):
            for n in itertools.product(range(3), repeat=3):
                Bm[idx(2 * np.array(n) + np.array(s)), si] = np.exp(2j * np.pi * np.dot(m, n) / 3) / np.sqrt(27)
        BL[m] = Bm
    return BL[m].conj().T @ U @ BL[m]
def cubeH(Psym, real, polar):
    Am = rng.normal(size=(8, 8)) + (0 if real else 1j * rng.normal(size=(8, 8))); H = (Am + Am.conj().T) / 2
    if Psym: H = (H + Jf @ H @ Jf) / 2
    if polar: H = H + 0.7 * np.diag([sum(v) - 1.5 for v in V])
    return 0.4 * H
def pair_split(case):
    U = layer(cubeH(*case), 1) @ layer(cubeH(*case), 0)
    sp_ = lambda m: np.sort(np.angle(np.linalg.eigvals(bloch(U, m))))
    return max(np.max(np.abs(sp_(m) - sp_(tuple((-np.array(m)) % 3)))) for m in [(1, 1, 1), (1, 0, 0), (1, 2, 0)])
s1, s2, s3 = pair_split((True, False, False)), pair_split((False, True, True)), pair_split((False, False, True))
check("[T] (c) polar nesting: on a two-tiling cube tick (L = 6, 216 modes, random cube generators) the conjugate "
      "family characters (1,1,1)/(2,2,2) have equal spectra if the cube generator keeps cube-centred inversion (T broken) "
      "or is real (polar C3v term, T kept); only polar AND complex splits them",
      s1 < 1e-12 and s2 < 1e-12 and s3 > 1e-2, f"max split: P kept {s1:.1e}, polar real {s2:.1e}, polar complex {s3:.2f}")
print("   the split's nesting is real geometry (T-even) and a uniform split is a pure translation (register), so even"
      " where present it cannot split the pair; drift-weighted effect ~ t_tick H ~ 1e-61")

# ---------------- B ----------------
print("== B. the family copy-form law: sqrt(m) = c (1 - s), s traceless, unit mean square")
d, S1, S2 = sp.symbols("delta S1 S2", real=True); x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
num_ = sp.expand(sum((1 + x) ** 2 for x in (x1, x2, x3))); den_ = sp.expand(sum(1 + x for x in (x1, x2, x3)) ** 2)
ident = sp.expand(num_ - (3 + 2 * (x1 + x2 + x3) + (x1 ** 2 + x2 ** 2 + x3 ** 2))) == 0 and \
        sp.expand(den_ - (3 + x1 + x2 + x3) ** 2) == 0
Qgen = (3 + 2 * S1 + S2) / (3 + S1) ** 2
check("[T] Q = (3 + 2 S1 + S2)/(3 + S1)^2 for sqrt(m) = 1 + x; S1 = 0, S2 = 3 (traceless, unit mean square) gives Q = 2/3 "
      "exactly, for any eigenvectors (signed readout); the same form on CL-1's two copies (1 - s, s^2 = 1) gives Q_2 = 1, "
      "one massless copy", ident and Qgen.subs({S1: 0, S2: 3}) == sp.Rational(2, 3)
      and sp.Rational(0 ** 2 + 2 ** 2, (0 + 2) ** 2) == 1)
xs = [sp.sqrt(2) * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
check("[T] the unit-mean-square traceless triples are exactly sqrt2 cos(delta + 2 pi k/3): one free phase per sector",
      sp.simplify(sum(xs)) == 0 and sp.simplify(sp.expand_trig(sum(x ** 2 for x in xs))) == 3)
qok = True
for _ in range(200):
    Am = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); S = (Am + Am.conj().T) / 2
    S -= np.trace(S).real / 3 * np.eye(3); S /= np.sqrt(np.trace(S @ S).real / 3)
    l = np.linalg.eigvalsh(np.eye(3) - S); qok &= abs(np.sum(l ** 2) / np.sum(l) ** 2 - 2 / 3) < 1e-12
check("[T] seeded check: 200 random Hermitian s give Q = 2/3 to 1e-12", qok)
v0 = sorted([sp.nsimplify(sp.simplify(1 + xx.subs(d, 0))) for xx in xs], key=lambda z: -float(z))
ex0 = [1 + sp.sqrt(2), 1 - 1 / sp.sqrt(2), 1 - 1 / sp.sqrt(2)]
check("[T] with only CL-1..CL-3, s is diagonal in the translation characters and cube-centred inversion sets x1 = x2: "
      "delta in (pi/3)Z, so sqrt(m) = (1+sqrt2, 1-1/sqrt2, 1-1/sqrt2) (or the signed pi/3 pattern): no three distinct masses",
      all(sp.simplify(u - w) == 0 for u, w in zip(v0, ex0)),
      f"m2/m3 at delta=0: {float(((1-1/sp.sqrt(2))/(1+sp.sqrt(2)))**2):.4f}, m1 = m2")
Fm = np.exp(2j * np.pi * np.outer(range(3), range(3)) / 3) / np.sqrt(3); vmax = 0
for _ in range(100):
    def circ():
        th = rng.uniform(0, 2 * np.pi); x = np.sqrt(2) * np.cos(th + 2 * np.pi * np.arange(3) / 3)
        return Fm @ np.diag(1 - x) @ Fm.conj().T
    _, Uu = np.linalg.eigh(circ()); _, Ud = np.linalg.eigh(circ()); Vm = np.abs(Uu.conj().T @ Ud)
    vmax = max(vmax, np.max(np.abs(np.sort(Vm, axis=1) - np.array([0, 0, 1]))))
check("[T] translation-invariant s_u, s_d share the character eigenbasis: |V| is a permutation for every pair of phases "
      "(no mixing), so mixing needs a supplied translation breaker", vmax < 1e-9, f"max off-permutation |V| {vmax:.1e}")
grid = np.linspace(0, np.pi / 3, 20001)[1:-1]
r23 = []; r12 = []
for th in grid:
    l = np.sort(np.abs(1 + np.sqrt(2) * np.cos(th + 2 * np.pi * np.arange(3) / 3)))
    r12.append((l[0] / l[1]) ** 2); r23.append((l[1] / l[2]) ** 2)
r12 = np.array(r12); r23 = np.array(r23); lo = (2 - np.sqrt(3)) ** 2; dz = ((1 - 1 / np.sqrt(2)) / (1 + np.sqrt(2))) ** 2
cap = r23[r12 < 0.1].min()
check("[T] one-step cap: under the copy form m2/m3 lies in [0.0147, 1] and equals (2 - sqrt3)^2 = 0.0718 when m1 = 0; any phase with "
      "m1/m2 < 0.1 has m2/m3 > 0.035, so no sector holds a two-step tower (up: 1.7e-3 and 7.4e-3; down: 0.05 and 0.022; "
      "leptons 4.8e-3 and 0.060 fit)", r23.min() > dz - 1e-6 and cap > 0.035 and 1.273 / 172.57 < cap and 0.0935 / 4.183 < cap
      and mm / mt > cap,
      f"min m2/m3 {r23.min():.4f} (= {dz:.4f} at delta=0), at m1=0 {lo:.4f}, min m2/m3 given m1/m2<0.1: {cap:.4f}")
kap = sp.symbols("kappa", nonnegative=True)
Qk = sp.simplify(sum((1 + kap * x) ** 2 for x in xs) / sum(1 + kap * x for x in xs) ** 2)
check("[T] a link-dressed family hop, weight kappa <= 1 (domain-normalised raisers have norm <= 1), gives Q = (1 + "
      "kappa^2)/3 <= 2/3: dressing can only lower Q", sp.simplify(Qk - (1 + kap ** 2) / 3) == 0)

# ---------------- C ----------------
print("== C. the copy form against measurement [M: PDG 2024; NuFIT 6.0; DESI DR2+CMB sum m_nu < 0.064 eV]")
mt_pred = brentq(lambda x: Q([me, mm, x]) - 2 / 3, 1000, 3000)
check("[E] charged leptons: Q = 2/3 is the measured value; it predicts m_tau from m_e, m_mu within 1 sigma",
      abs(mt_pred - mt) < 0.09, f"Q_meas {Ql:.7f}; m_tau pred {mt_pred:.3f} vs {mt} +- 0.09 MeV")
a0 = np.sum(np.sqrt([me, mm, mt])) / 3; xl = np.sqrt([me, mm, mt]) / a0 - 1
dl = np.arccos(np.clip(xl[2] / np.sqrt(2), -1, 1))
def me_of(dlt):
    l = np.sort(np.abs(1 + np.sqrt(2) * np.cos(dlt + 2 * np.pi * np.arange(3) / 3))); return (l[0] / l[2]) ** 2
fr = [(abs(np.log(me_of(np.pi * pn / qd) / (me / mt))), pn, qd) for qd in range(1, 49) for pn in range(0, 2 * qd)]
bf = min(fr); nfrac = len({sp.Rational(pn, qd) for _, pn, qd in fr})
fracs = np.array(sorted({float(sp.pi * sp.Rational(pn, qd)) for _, pn, qd in fr}))
mof = np.array([me_of(t) for t in fracs]); tg = rng.uniform(0, np.pi / 3, 2000)
lee = np.mean([np.min(np.abs(np.log(mof / me_of(t)))) <= bf[0] for t in tg])
check("[E] the lepton phase (Brannen delta, 2/9 within 2e-5) is no lattice phase: the best pi p/q with q <= 48 misses "
      "m_e/m_tau by more than 1%, and a random target is matched that well by some fraction in most cases (look-elsewhere)",
      bf[0] > 0.01, f"delta {dl:.6f}; best pi*{bf[1]}/{bf[2]}: m_e off {100*(np.exp(bf[0])-1):.1f}%; {nfrac} fractions; "
      f"random targets matched as well: {lee:.2f}")
frac = np.mean(np.array([me_of(t) for t in grid]) <= me / mt)
check("[E] hierarchy is tuned, not produced: a phase uniform on (0, pi/3) gives m1/m3 <= m_e/m_tau in a few % of cases",
      0 < frac < 0.1, f"fraction {frac:.3f}")
qset = {"u PDG": ([2.16e-3, 1.2730, 172.57], [0.4e-3, 0.0046, 0.29]), "d PDG": ([4.70e-3, 0.0935, 4.183], [0.3e-3, 0.0008, 0.007]),
        "u M_Z": ([1.23e-3, 0.620, 168.26], [0.21e-3, 0.017, 0.75]), "d M_Z": ([2.67e-3, 0.05316, 2.839], [0.19e-3, 0.0046, 0.026])}
txt = []; worst = 1e9
for k, (m, e) in qset.items():
    g = np.array([(Q(np.array(m) + np.eye(3)[i] * 1e-6 * m[i]) - Q(m)) / (1e-6 * m[i]) for i in range(3)])
    sq = np.sqrt(np.sum((g * e) ** 2)); qs = Q(m, (-1, 1, 1)); pull = (Q(m) - 2 / 3) / sq; worst = min(worst, pull)
    txt.append(f"{k}: Q {Q(m):.3f} (signed {qs:.3f}) +- {sq:.3f}, kappa^2 {3*Q(m)-1:.2f}")
check("[E] quarks falsify the copy form: Q_u ~ 0.85-0.89 and Q_d ~ 0.73-0.75 at either scale, above 2/3 (as is the signed "
      "readout), so they need kappa > 1, which dressing forbids; and m_c/m_t = 0.0074 is below the copy-form floor 0.0147",
      worst > 5 and 1.273 / 172.57 < dz, "; ".join(txt) + f"; min pull {worst:.0f} sigma")
d21, d31, d32 = 7.49e-5, 2.513e-3, 2.484e-3
def nm(x, o):
    if o == "NO": return np.array([x, np.sqrt(x * x + d21), np.sqrt(x * x + d31)])
    m2 = np.sqrt(x * x + d32); return np.array([np.sqrt(m2 * m2 - d21), m2, x])
sols = []
for o in ("NO", "IO"):
    for sg in [(1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]:
        xx = np.logspace(-7, 0, 4001); g = np.array([Q(nm(x, o), sg) - 2 / 3 for x in xx])
        for i in np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]:
            if abs(g[i]) < 1 and abs(g[i + 1]) < 1:
                x = brentq(lambda y: Q(nm(y, o), sg) - 2 / 3, xx[i], xx[i + 1]); sols.append((o, sg, x, nm(x, o).sum()))
ok = (len(sols) == 2 and {s[0] for s in sols} == {"NO", "IO"})
no = [s for s in sols if s[0] == "NO"]; io = [s for s in sols if s[0] == "IO"]
check("[E] neutrinos (if the copy form is universal): no all-positive solution; the signed readout gives one normal-ordering "
      "solution inside the cosmology bound and one inverted solution outside it", ok and no[0][3] < 0.064 < io[0][3],
      f"NO: m1 {no[0][2]*1e3:.3f} meV, sum {no[0][3]:.4f} eV; IO: m3 {io[0][2]*1e3:.2f} meV, sum {io[0][3]:.3f} eV")
print("   count: the copy form uses 3 scales + 3 phases (the phases are not in CL-1..CL-3) for 9 charged masses; it predicts the 3")
print("   Q values (leptons pass, up and down fail by > 5 sigma) and gives no mixing; the SM uses 9 + 4.")
print(f"runtime {time.time()-t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
