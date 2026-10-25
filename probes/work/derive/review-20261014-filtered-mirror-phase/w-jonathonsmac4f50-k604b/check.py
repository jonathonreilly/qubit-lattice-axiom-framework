#!/usr/bin/env python3
"""check.py for J:derive:review-20261014-filtered-mirror-phase:a1  (same-family, unrefereed).

Self-contained.  numpy, scipy, sympy only.  Gaussian-integer matrices are held in numpy complex128 with entries
that are small integers (all products stay far below 2**53, so the arithmetic is exact); every filter/overlap
statement uses fractions.Fraction.  One line per check: PASS or FAIL.

Sections
  A  source hashes (the four named objects, copies kept in ./src)
  B  explicit Spin(10) 16 / Clifford encoding of the quartic (the repo's SPIN10 note conventions)
  C  X2's B^a = 2 * (note's B_a); Spin(10) and spin-SU(2) invariance (coefficient level)
  D  light-mode commutator: general lemma + coefficient-slice test on the 256-mode 3D L=2 carrier
  E  light-mode commutator in a genuine CAR (Fock) engine with the actual 16-index tensors (64-mode cell)
  F  exact overlap kernel of the filters; exact-zero => no independent-site limit (lemma + numbers)
  G  number-conserving member sum B^dagger B: exact non-singlet minimum multiplet (atom)
  H  mean-field channel (BdG) re-derivation and susceptibility ratios (reproduction of K1's B1)
"""
import hashlib, itertools, os, sys, time
from fractions import Fraction as Fr
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()
npass = nfail = 0
HITS = []


def rep(ok, msg):
    global npass, nfail
    if ok:
        npass += 1
    else:
        nfail += 1
    print(("PASS " if ok else "FAIL ") + msg)
    sys.stdout.flush()


# ============================================================================ A. hashes
SRC = {
    "combos_X2_COMBO_REPORT.md": "3b5e095d96a3fa16fb8b8c3b9adc6cf560f9a167db481132719efac6bc5b9438",
    "kills_K1_KILL_REPORT.md": "31113b4b7c78e2b1d8bed2a42d4a6140ca6de154d414393d3ce11d4f2c233f6f",
    "routes_F1_ROUTE_REPORT.md": "e799854cc30793c9fadd9c1437d7e2a64f807c60c14ff90512abfc3646c212dd",
    "combos_X1_COMBO_REPORT.md": "0f2aa85353eabd52d0820e20ee31cec23cddd44f14ff1b0a7d9caabead861a1f",
}
for name, h in SRC.items():
    p = os.path.join(HERE, "src", name)
    try:
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
    except OSError:
        got = "missing"
    rep(got == h, f"A: source copy {name} sha256 matches the task's value ({got[:12]})")

# ============================================================================ B. Clifford / 16 encoding
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)


def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms:
        out = np.kron(out, m)
    return out


def ZP(n):
    return [Z] * n


gam = []
for k in range(5):
    gam.append(kron(*([I2] * k + [X] + ZP(4 - k))))
    gam.append(kron(*([I2] * k + [Y] + ZP(4 - k))))
Cmat = kron(Y, X, Y, X, Y)
chir = kron(*ZP(5))
plus = [i for i in range(32) if np.real(chir[i, i]) > 0]
assert len(plus) == 16 and plus == [i for i in range(32) if bin(i).count("1") % 2 == 0]


def is_int(A):
    return np.all(np.abs(A.real - np.round(A.real)) == 0) and np.all(np.abs(A.imag - np.round(A.imag)) == 0)


ok = all(np.array_equal(gam[a] @ gam[b] + gam[b] @ gam[a], 2 * (a == b) * np.eye(32)) for a in range(10) for b in range(10))
rep(ok, "B: ten 32x32 Gamma matrices (SPIN10 note convention) satisfy {Ga,Gb}=2 delta_ab exactly")
Tgen = {}   # T_ab = i G_a G_b restricted to + chirality (t_ab = T_ab/2)
for a in range(10):
    for b in range(a + 1, 10):
        T = 1j * gam[a] @ gam[b]
        Tgen[(a, b)] = T[np.ix_(plus, plus)]
S = sum(T @ T for T in Tgen.values())
rep(np.array_equal(S, 45 * np.eye(16)) and len(Tgen) == 45,
    "B: sum_{a<b} t_ab^2 = 45/4 on the 16 (45 generators), exact")
M = []
for a in range(10):
    CG = Cmat @ gam[a]
    Ma = CG[np.ix_(plus, plus)]
    M.append(Ma)
rep(all(np.array_equal(m, m.T) and is_int(m) for m in M) and all(np.count_nonzero(m) == 16 for m in M),
    "B: M_a=(C Gamma_a)|_+ are symmetric 16x16 Gaussian-integer monomial matrices (16 nonzeros each)")
bad = 0
for (a, b), T in Tgen.items():
    for c in range(10):
        lhs = T.T @ M[c] + M[c] @ T                 # = 2*(t^T M + M t)
        rhs = 2j * ((a == c) * M[b] - (b == c) * M[a])
        bad += (not np.array_equal(lhs, rhs))
rep(bad == 0, "B: vector identity t_ab^T M_c + M_c t_ab = i(d_ac M_b - d_bc M_a) for all 45x10 (a,b,c), exact")

# Omega = sum_a B_a B_a with B_a = sum M_a[al,be] u_al v_be ; modes: u_al -> al, v_be -> 16+be
def normal_order(ops):
    ops = list(ops); sign = 1
    for i in range(1, len(ops)):            # insertion sort with anticommutation
        j = i
        while j > 0 and ops[j - 1] > ops[j]:
            ops[j - 1], ops[j] = ops[j], ops[j - 1]; sign = -sign; j -= 1
    if len(set(ops)) < len(ops):
        return 0, None
    return sign, tuple(ops)


Bterms = []
for a in range(10):
    Bterms.append([(M[a][al, be], al, 16 + be) for al in range(16) for be in range(16) if M[a][al, be] != 0])
Om = {}
for a in range(10):
    for (c1, i1, j1) in Bterms[a]:
        for (c2, i2, j2) in Bterms[a]:
            s, key = normal_order([i1, j1, i2, j2])
            if s:
                Om[key] = Om.get(key, 0) + s * c1 * c2
Om = {k: v for k, v in Om.items() if v != 0}
# ordered monomial u_al u_ga v_be v_de (al<ga, be<de) => sorted tuple (al,ga,16+be,16+de)
rep(len(Om) == 240, f"B: Omega=sum B_a B_a has {len(Om)} nonzero ordered coefficients (note: 240)")
v = Om.get((0, 1, 30, 31), 0)
rep(v == 8, f"B: coefficient at (u0,u1,v14,v15) = {v} (note: +8)")

# ============================================================================ C. X2 normalisation, invariances
eps = np.array([[0, 1], [-1, 0]], complex)          # i sigma_y
# B^X2_a = sum (eps)_{st} M[al,be] psi_{s al} psi_{t be};  modes (s,al): s=0 -> u, s=1 -> v
K = np.kron(eps, M[0])                              # coefficient matrix on 32 modes (s,alpha) ordered s-major
# operator sum_{mn} K[m,n] psi_m psi_n = sum_{m<n} (K[m,n]-K[n,m]) psi_m psi_n
Kas = K - K.T
Bnote = np.zeros((32, 32), complex)
for (c, i, j) in Bterms[0]:
    Bnote[i, j] += c; Bnote[j, i] -= c              # c psi_i psi_j -> antisymmetric coefficient c on (i,j), -c on (j,i)
rep(np.array_equal(Kas, 2 * Bnote), "C: X2's B^a = psi^T(i sigma_y x C Gamma^a)psi equals 2 x (SPIN10 note's B_a) as an operator (factor 2 normalisation), exact")
# spin-SU(2) singlet: sigma^T eps + eps sigma = 0 for sigma_x,y,z
rep(all(np.array_equal(s.T @ eps + eps @ s, np.zeros((2, 2))) for s in (X, Y, Z)),
    "C: eps=i sigma_y is an SU(2) singlet coupling (sigma^T eps + eps sigma = 0), so each B_a is a spin singlet (rotation lift)")

# ============================================================================ D. light-mode commutator, coefficient level
C3 = list(itertools.product((0, 1), repeat=3))
hw = lambda c: sum(c)
fNN = lambda c: hw(c) - 1                           # (1 - sum cos)/2 at a corner = hw - 1  (integers)
fF1 = lambda c: {0: 1, 1: 0, 2: 1, 3: 1}[hw(c)]     # F1 filter at corners (exact values, checked in F below)
fone = lambda c: 1
rep([fNN(c) for c in C3 if hw(c) == 1] == [0, 0, 0] and [fF1(c) for c in C3 if hw(c) == 1] == [0, 0, 0]
    and all(fNN(c) != 0 and fF1(c) != 0 for c in C3 if hw(c) != 1),
    "D: both filters vanish exactly at the three hw1 corners and nowhere else among the 8 corners (integer values)")
mode = lambda c, s, al: (C3.index(c) * 2 + s) * 16 + al      # 256 modes on the 3D L=2 torus
for fname, f in (("f_NN", fNN), ("f_F1", fF1), ("control f=1", fone)):
    light_rows_zero = True; mirror_rows_nonzero = True; maxlight = 0
    for x in C3:
        g = np.array([f(c) * (-1) ** (np.dot(c, x) % 2) for c in C3], dtype=complex)
        for a in range(10):
            Kx = np.kron(np.outer(g, g), np.kron(eps, M[a]))     # 256x256: B_a(x)=sum K[m,n] psi_m psi_n (unnormalised F)
            assert np.array_equal(Kx, -Kx.T)
            for c in C3:
                rows = Kx[mode(c, 0, 0): mode(c, 1, 15) + 1, :]
                z = not np.any(rows)
                if hw(c) == 1:
                    light_rows_zero &= z
                else:
                    mirror_rows_nonzero &= (not z) if f(c) != 0 else z
    if fname == "control f=1":
        rep(not light_rows_zero, f"D: {fname}: light-corner rows of the B_a(x) coefficient matrices are NOT zero (control has power)")
    else:
        rep(light_rows_zero and mirror_rows_nonzero,
            f"D: {fname}: for all 8 x 10 operators B_a(x) on the 256-mode carrier the hw1 rows/columns vanish exactly (96 modes) "
            f"=> [B_a(x),psi_m]=[B_a(x)^dag,psi_m]=0, hence every word in the B's commutes with psi_m; mirror rows nonzero")

# ============================================================================ E. CAR engine, 64-mode two-corner cell
def sgn_below(m, i):
    return -1 if (bin(m & ((1 << i) - 1)).count("1") & 1) else 1


def ann(i, st):
    out = {}
    for m, c in st.items():
        if (m >> i) & 1:
            k = m ^ (1 << i)
            out[k] = out.get(k, 0) + c * sgn_below(m, i)
    return out


def cre(i, st):
    out = {}
    for m, c in st.items():
        if not (m >> i) & 1:
            k = m | (1 << i)
            out[k] = out.get(k, 0) + c * sgn_below(m, i)
    return out


def addto(a, b, s=1):
    for k, c in b.items():
        a[k] = a.get(k, 0) + s * c
    return a


def clean(a):
    return {k: c for k, c in a.items() if c != 0}


# 1D L=2 torus, corners l (index 0, p=0) and mu (index 1, p=pi); modes id = c*32 + s*16 + alpha  (64 modes)
def build_B(f, a, x):
    """B_a(x) = sum_{al,be} 2 M[al,be] psi_S(x,u,al) psi_S(x,v,be), psi_S(x,s,al)=sum_c f_c (-1)^{c x} psi(c,s,al)."""
    terms = {}
    for al in range(16):
        for be in range(16):
            m = M[a][al, be]
            if m == 0:
                continue
            for c1 in (0, 1):
                for c2 in (0, 1):
                    w = 2 * m * f[c1] * f[c2] * (-1) ** ((c1 + c2) * x)
                    if w != 0:
                        key = (c1 * 32 + 0 * 16 + al, c2 * 32 + 1 * 16 + be)
                        terms[key] = terms.get(key, 0) + w
    return [(w, i, j) for (i, j), w in terms.items() if w != 0]


def applyB(terms, st):
    out = {}
    for w, i, j in terms:
        addto(out, {k: w * c for k, c in ann(i, ann(j, st)).items()})
    return out


def applyBd(terms, st):                              # (w psi_i psi_j)^dag = conj(w) psi_j^dag psi_i^dag
    out = {}
    for w, i, j in terms:
        addto(out, {k: np.conj(w) * c for k, c in cre(j, cre(i, st)).items()})
    return out


def make_H(f):
    Bs = [build_B(f, a, x) for x in (0, 1) for a in range(10)]
    def H(st):
        out = {}
        for T in Bs:
            Bv = applyB(T, st)
            addto(out, applyBd(T, Bv))                       # + B^dag B
            addto(out, applyB(T, Bv), 0.5)                   # + 1/2 B B
            addto(out, applyBd(T, applyBd(T, st)), 0.5)      # + 1/2 B^dag B^dag
        return clean(out)
    return H


rng = np.random.default_rng(20261014)
def rand_state():
    st = {0: 1.0 + 0j}                                          # vacuum component
    modes = rng.choice(64, size=6, replace=False)
    for m in modes:
        st[1 << int(m)] = complex(int(rng.integers(1, 4)), int(rng.integers(-2, 3)))
    for _ in range(3):
        pr = rng.choice(64, size=2, replace=False)
        st[(1 << int(pr[0])) | (1 << int(pr[1]))] = complex(int(rng.integers(1, 4)), int(rng.integers(-2, 3)))
    return st


def comm_norm(H, m, v):
    a = H(ann(m, v)); b = ann(m, H(v))
    return max([abs(c) for c in clean(addto(dict(a), b, -1)).values()] + [0.0])


v = rand_state()
Hl = make_H([0, 1]); Hc = make_H([1, 1])
light = [int(i) for i in rng.choice(32, size=5, replace=False)]            # corner l modes (ids 0..31)
mirror = [32 + int(i) for i in rng.choice(32, size=5, replace=False)]      # corner mu modes (ids 32..63)
# make sure v has support on each tested mode so the commutator is not vacuous
for m in light + mirror:
    v[1 << m] = v.get(1 << m, 0) + 1.0
cl = [comm_norm(Hl, m, v) for m in light]
cm = [comm_norm(Hl, m, v) for m in mirror]
cc = [comm_norm(Hc, m, v) for m in light]
rep(max(cl) == 0.0, f"E: filtered (f_l=0,f_mu=1) actual-Spin(10) quartic H=sum(B^dag B + 1/2 BB + 1/2 B^dag B^dag): "
                    f"max|[H,psi_light]| = {max(cl):.1e} on 5 light modes, random N<=2 state (exact zero)")
rep(min(cm) > 0.5, f"E: same H: min|[H,psi_mirror]| = {min(cm):.2f} > 0 (the commutator is not vacuously zero)")
rep(min(cc) > 0.5, f"E: unfiltered control f=1: min|[H,psi_(corner l)]| = {min(cc):.2f} > 0")

# ============================================================================ F. exact overlap kernels
def pmul(p, q):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            k = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
            out[k] = out.get(k, 0) + ca * cb
    return {k: c for k, c in out.items() if c != 0}


def padd(p, q, s=1):
    out = dict(p)
    for k, c in q.items():
        out[k] = out.get(k, 0) + s * c
    return {k: c for k, c in out.items() if c != 0}


def axis(a, d):
    k = [0, 0, 0]; k[a] = d; return tuple(k)


ONE = {(0, 0, 0): Fr(1)}
def sin2(a):  # sin^2(p_a/2) = 1/2 - (z+1/z)/4
    return {(0, 0, 0): Fr(1, 2), axis(a, 1): Fr(-1, 4), axis(a, -1): Fr(-1, 4)}
def cos2(a):
    return {(0, 0, 0): Fr(1, 2), axis(a, 1): Fr(1, 4), axis(a, -1): Fr(1, 4)}
fF1p = ONE
for mu in range(3):
    t = sin2(mu)
    for nu in range(3):
        if nu != mu:
            t = pmul(t, cos2(nu))
    fF1p = padd(fF1p, t, -1)
fNNp = {(0, 0, 0): Fr(1, 2)}
for a in range(3):
    fNNp[axis(a, 1)] = Fr(-1, 4); fNNp[axis(a, -1)] = Fr(-1, 4)


def evalcorner(p, c):
    return sum(co * (-1) ** (sum(k[i] * c[i] for i in range(3)) % 2) for k, co in p.items())


rep([evalcorner(fF1p, c) for c in C3] == [fF1(c) for c in C3] and [evalcorner(fNNp, c) for c in C3] == [fNN(c) for c in C3],
    "F: real-space coefficient dictionaries of f_F1 (27-site cube) and f_NN (7-site star) reproduce the corner values used in D/E exactly")
rep(len(fF1p) == 27 and len(fNNp) == 7, "F: supports are 27 and 7 sites")


def kernel(p):
    K = {}
    for a, ca in p.items():
        for b, cb in p.items():
            r = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
            K[r] = K.get(r, 0) + ca * cb
    return {k: c for k, c in K.items() if c != 0}


for name, p, support, maxnb, agg in (("f_NN", fNNp, 25, Fr(2, 5), None), ("f_F1", fF1p, 125, None, None)):
    Kp = kernel(p)
    K0 = Kp[(0, 0, 0)]
    S2 = sum(c * c for r, c in Kp.items() if r != (0, 0, 0))
    mx = max(abs(c) for r, c in Kp.items() if r != (0, 0, 0))
    Nr = len(Kp) - 1
    ratio2 = S2 / (K0 * K0)
    if name == "f_NN":
        rep(K0 == Fr(5, 8) and mx / K0 == Fr(2, 5) and ratio2 == Fr(3, 2) and len(Kp) == 25,
            f"F: f_NN exact: K(0)=5/8, max_(r!=0)|K|/K(0)=2/5, aggregate^2 = sum_(r!=0)K^2/K(0)^2 = {ratio2} (=3/2), support 25")
    else:
        rep(len(Kp) == 125 and abs(float(mx / K0) - 0.1850) < 5e-4 and abs(float(ratio2) ** 0.5 - 0.6338) < 5e-4,
            f"F: f_F1 exact: support {len(Kp)}, max|K|/K(0)={float(mx/K0):.4f}, aggregate={float(ratio2)**0.5:.4f} (K1's FFT values 0.1850, 0.6338)")
    # lemma: exact zero at p0=(pi,0,0)  =>  K(0) = -sum_{r!=0} K(r) (-1)^{r_x}  <=  sum|K| <= sqrt(Nr * S2)
    kz = sum(c * (-1) ** (r[0] % 2) for r, c in Kp.items())
    rep(kz == 0 and ratio2 >= Fr(1, Nr),
        f"F: {name}: |f|^2 has an exact zero at (pi,0,0) (kernel transform {kz}); aggregate^2 = {float(ratio2):.4f} >= 1/N_r = 1/{Nr} as the lemma demands")
# uniqueness of the A1g star filter with the hw1 zero:  a + b*sum cos p ; hw1: a + b(-1+1+1) = a + b
import sympy as sp
_a, _b = sp.symbols("a b")
_sol = sp.solve(sp.Eq(_a + _b * (sp.cos(sp.pi) + sp.cos(0) + sp.cos(0)), 0), _a)
rep(_sol == [-_b], "F: A1g nearest-neighbour-star filters a+b*sum cos p_a vanish at (pi,0,0) iff a=-b, i.e. the star filter is f_NN up to scale (unique)")

# optimisation over range-1 A1g filters with zeros at hw1 (numerical, not certified global)
from scipy.optimize import minimize
shells = {0: [(0, 0, 0)], 1: [k for k in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, k)) == 1],
          2: [k for k in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, k)) == 2],
          3: [k for k in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, k)) == 3]}
def fam(c):
    p = {}
    for s, ks in shells.items():
        for k in ks:
            p[k] = float(c[s])
    return p
def corner_val(p, cc):
    return sum(v * (-1) ** (sum(k[i] * cc[i] for i in range(3)) % 2) for k, v in p.items())
def agg2(c):
    p = fam(c)
    # exact-in-floats autocorrelation
    K = {}
    for a, ca in p.items():
        for b, cb in p.items():
            r = (b[0] - a[0], b[1] - a[1], b[2] - a[2]); K[r] = K.get(r, 0.0) + ca * cb
    K0 = K[(0, 0, 0)]
    return sum(v * v for r, v in K.items() if r != (0, 0, 0)) / K0 ** 2
# constraint f(hw1)=0 linear: solve for c0 given c1..c3
def c_from(z):
    c = np.zeros(4); c[1:] = z
    e = [1, 0, 0]
    tmp = corner_val(fam(c), (1, 0, 0))                 # value with c0=0
    c[0] = -tmp                                         # shell-0 contributes +c0 at every corner
    return c
def zero_other_corner_penalty(c):
    p = fam(c)
    vals = [abs(corner_val(p, cc)) for cc in C3 if hw(cc) != 1]
    return min(vals)
best = None
r2 = np.random.default_rng(3)
for trial in range(40):
    z0 = r2.normal(size=3)
    res = minimize(lambda z: agg2(c_from(z)) + (1e3 if zero_other_corner_penalty(c_from(z)) < 1e-3 * np.abs(c_from(z)).max() else 0.0),
                   z0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-14, "maxiter": 4000})
    if best is None or res.fun < best.fun:
        best = res
cb = c_from(best.x)
print(f"   info: min aggregate^2 over range-1 A1g filters with hw1 zeros (40 starts): {best.fun:.4f} "
      f"(f_F1: {float(kernel(fF1p)[(0,0,0)]) and float(sum(c*c for r,c in kernel(fF1p).items() if r!=(0,0,0))/kernel(fF1p)[(0,0,0)]**2):.4f}); coefficients (shell 0..3, scale-free) = {np.round(cb/np.abs(cb).max(),4).tolist()}")
fF1_agg2 = float(sum(c * c for r, c in kernel(fF1p).items() if r != (0, 0, 0)) / kernel(fF1p)[(0, 0, 0)] ** 2)
rep(best.fun > 1.0 / 124 and best.fun <= fF1_agg2 + 1e-9,
    f"F: numerical search (40 Nelder-Mead starts, not a certified global minimum) over range-1 A1g filters with the hw1 zeros finds aggregate^2 = {best.fun:.4f} "
    f"(aggregate {best.fun**0.5:.3f}), between the lemma bound 1/124 and f_F1's {fF1_agg2:.4f}")
gg = np.linspace(-np.pi, np.pi, 31)
PP = np.array(list(itertools.product(gg, repeat=3)))
fv = sum(cb[s_] * np.cos(PP @ np.array(k, float)) for s_, ks in shells.items() for k in ks)
dist = np.min([np.linalg.norm(((PP - np.pi * np.array(h_) + np.pi) % (2 * np.pi)) - np.pi, axis=1) for h_ in ((1, 0, 0), (0, 1, 0), (0, 0, 1))], axis=0)
fv = fv / fv.max()
rep(fv.min() > -1e-9 and np.abs(fv[dist > 0.3]).min() > 1e-2,
    f"F: that optimised filter (normalised to max 1) is >= 0 on a 31^3 grid with no zero beyond 0.3 of the hw1 corners (min {np.abs(fv[dist > 0.3]).min():.3f}); it is a competitor, not a different mechanism")
# RHN-contract illustration: a translation-invariant, number-conserving on-site term (chemical potential m) gaps the walker by moving the nodes
# off the Fermi level (max |sin p| = sqrt 3): bands m +- |sin p| do not cross 0 once |m| > sqrt 3
_gp = np.linspace(-np.pi, np.pi, 61)
_s2 = np.sin(_gp)[:, None, None] ** 2 + np.sin(_gp)[None, :, None] ** 2 + np.sin(_gp)[None, None, :] ** 2
_mx = np.sqrt(_s2.max())
rep(abs(_mx - np.sqrt(3)) < 1e-12 and (2.0 - _mx) > 0.26,
    "F: max|sin p| = sqrt 3 on the grid (at (pi/2)^3); so walker + on-site chemical potential m=2 (keeps all shifts and number) has bands m +- |sin p| "
    "bounded away from 0 by >= 2-sqrt3: gapped with the nodes moved off the Fermi level, i.e. 'nu_R forced' is conditional on the node-preserving contract")

# ============================================================================ G. number-conserving member: non-singlet minimum multiplet
# Q_+ = sum_a B_a^dag B_a >= 0.  Fully-u-filled state |Psi_up> has no v: B_a|Psi_up> = 0.  (checked on the 32-mode operator algebra)
def mode_u(al): return al
def mode_v(al): return 16 + al
full_up = sum(1 << mode_u(al) for al in range(16))
Bs0 = [Bterms[a] for a in range(10)]
st = {full_up: 1.0 + 0j}
z = all(not clean(applyB([(2 * w, i, j) for (w, i, j) in Bs0[a]], st)) for a in range(10))
rep(z, "G: B_a |all 16 u-modes filled> = 0 for all 10 a (explicit actual M_a): Q_+ |Psi_up> = 0, and Q_+ >= 0 => E_min(N=16)=0")
# S_- = sum_al v_al^dag u_al ; check [S_-, B_a]=0 on a random N=3 state and that S_-^k |Psi_up> != 0 for k=0..16
def Sminus(st):
    out = {}
    for al in range(16):
        addto(out, cre(mode_v(al), ann(mode_u(al), st)))
    return clean(out)
cur = {full_up: 1.0 + 0j}; norms = []
for k in range(17):
    norms.append(sum(abs(c) ** 2 for c in cur.values()))
    cur = Sminus(cur)
rep(all(n > 0 for n in norms) and not cur,
    "G: S_-^k |Psi_up> != 0 for k=0..16 and S_-^17|Psi_up>=0: an S=8 multiplet of 17 states (N=16)")
Bfull = [[(2 * w, i, j) for (w, i, j) in Bs0[a]] for a in range(10)]
rs = np.random.default_rng(5)
stt = {}
for _ in range(6):
    ids = rs.choice(32, size=3, replace=False)
    stt[sum(1 << int(i) for i in ids)] = complex(int(rs.integers(1, 4)), int(rs.integers(-2, 3)))
okc = True
for a in range(10):
    lhs = clean(addto(applyB(Bfull[a], Sminus(stt)), Sminus(applyB(Bfull[a], stt)), -1))
    okc &= not lhs
rep(okc, "G: [S_-, B_a] = 0 on a random 3-particle state for all a (B_a is a spin singlet; Q_+ commutes with S_-)")
# so every state S_-^k|Psi_up> has Q_+ = 0; and for N<16 the same holds with N u-modes filled.
Nmax = 16
# full family: B_a^dag also kills the all-u-filled state (u^dag blocked), so |Psi_up> is an exact E=0 eigenstate of ANY member a*sum B^dag B + lam*sum(BB + B^dag B^dag)
zd = all(not clean(applyBd(Bfull[a], {full_up: 1.0 + 0j})) for a in range(10))
rep(zd, "G: B_a^dag |all 16 u-modes filled> = 0 as well, so |Psi_up> (and its S=8 multiplet) is an exact zero-energy eigenstate of every member a*B^dag B + lam*(BB + B^dag B^dag); "
        "for lam != 0 whether E=0 is the ground energy is NOT decided (Q is then indefinite)")
def Splus(st):
    out = {}
    for al in range(16):
        addto(out, cre(mode_u(al), ann(mode_v(al), st)))
    return clean(out)
okc2 = all(not clean(addto(applyB(Bfull[a], Splus(stt)), Splus(applyB(Bfull[a], stt)), -1)) for a in range(10))
rep(okc2, "G: [S_+, B_a] = 0 on the same random state for all a (so [S_pm, B_a^dag] = 0 too)")
allN = True
for N in range(1, 17):
    cur = {sum(1 << mode_u(al) for al in range(N)): 1.0 + 0j}
    sizes = []
    for k in range(N + 2):
        sizes.append(sum(abs(c) ** 2 for c in cur.values()))
        zero_Q = all(not clean(applyB(Bfull[a], cur)) for a in range(10))
        allN &= zero_Q
        cur = Sminus(cur)
    allN &= all(s_ > 0 for s_ in sizes[:N + 1]) and sizes[N + 1] == 0
rep(allN, "G: for every N=1..16, the N states S_-^k|N u-modes filled> (k=0..N, spin N/2, dimension N+1) are all annihilated by every B_a: "
          "Q_+ has an exact E=0 minimum multiplet of dimension N+1 in sector N (N>16 by particle-hole), containing non-singlets")

# ============================================================================ H. BdG re-derivation and susceptibility ratios
import sympy as sp
sx, sy, sz = sp.symbols("sx sy sz", real=True)
phi = sp.symbols("phi", positive=True)
S1 = sp.Matrix([[0, 1], [1, 0]]); S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); S3 = sp.Matrix([[1, 0], [0, -1]])
h = sx * S1 + sy * S2 + sz * S3
hm = (-sx) * S1 + (-sy) * S2 + (-sz) * S3                     # h(-k)
D = phi * sp.I * S2                                           # singlet pairing iσ_y
Hbdg = sp.Matrix(sp.BlockMatrix([[h, D], [D.H, -hm.T]]))
lam = sp.symbols("lam")
cp = sp.factor(sp.simplify((Hbdg - lam * sp.eye(4)).det()))
target = sp.expand((lam ** 2 - (sx ** 2 + sy ** 2 + sz ** 2 + phi ** 2)) ** 2)
rep(sp.simplify(sp.expand(cp) - target) == 0,
    "H: BdG spectrum of walker h(k)=sigma.sin k with singlet pairing phi*i sigma_y is E=+-sqrt(|sin k|^2+phi^2), each doubly degenerate (K1's B1 dispersion), exact")


def bz_avg(fun, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    acc = 0.0
    for kx in k:
        p = np.stack(np.meshgrid(np.array([kx]), k, k, indexing="ij"))
        acc += fun(p).sum()
    return acc / N ** 3


def f_F1n(p):
    s2 = np.sin(p / 2) ** 2; c2 = np.cos(p / 2) ** 2
    return 1 - (s2[0] * c2[1] * c2[2] + s2[1] * c2[0] * c2[2] + s2[2] * c2[0] * c2[1])
def f_NNn(p): return (1 - np.cos(p[0]) - np.cos(p[1]) - np.cos(p[2])) / 2
Nq = 80
Ic = bz_avg(lambda p: 1.0 / np.sqrt((np.sin(p) ** 2).sum(0)), Nq)
IF = bz_avg(lambda p: f_F1n(p) ** 4 / np.sqrt((np.sin(p) ** 2).sum(0)), Nq)
IN = bz_avg(lambda p: f_NNn(p) ** 4 / np.sqrt((np.sin(p) ** 2).sum(0)), Nq)
rep(abs(Ic / IF - 3.244) < 0.03 and abs(Ic / IN - 0.873) < 0.01,
    f"H: reproduction of K1 B1 onset ratios g_c(filter)/g_c(control)=I[1]/I[f]: f_F1 {Ic/IF:.3f} (K1 3.244), f_NN {Ic/IN:.3f} (K1 0.873) at N={Nq}")
ten = [(3, 1, Fr(-1, 3)), (3, 1, Fr(1, 3)), (1, 2, Fr(1, 2)), (1, 2, Fr(-1, 2))]
rep(sum(a * b for a, b, _ in ten) == 10 and not any(a == 1 and b == 1 and y == 0 for a, b, y in ten),
    "H: the 10-vector of Spin(10) contains no G_SM singlet (so any B^a condensate breaks G_SM), exact")

# ============================================================================ summary
print(f"   info: runtime {time.time()-t0:.1f}s")
HIT = ("HIT: scoped counterexample and lemma, filtered Spin(10) quartic: (i) the number-conserving member sum_{x,a} B_a(x)^dag B_a(x) has, in every "
       "particle-number sector, an exact zero-energy minimum multiplet of maximal spin (non-singlet), so that member alone never gives a unique symmetric "
       "ground space; (ii) any filter with an exact zero has non-orthonormal psi_S(x) (aggregate overlap^2 >= 1/N_r; f_NN exactly 3/2); neither statement "
       "touches the BB+h.c. mixture or the thermodynamic limit")
if nfail == 0:
    print(HIT)
print(f"TOTAL: PASS={npass} FAIL={nfail}")
print("SUMMARY: The X2 Spin(10) quartic is the SPIN10 note's B_a with a factor 2, its light-mode commutator vanishes exactly (coefficient and CAR level) for any "
      "polynomial in the filtered field, the number-conserving member has an exact non-singlet zero-energy multiplet, and every exactly-zero filter lacks an independent-site limit; "
      "existence of a symmetric gapped mirror phase is not advanced.")
sys.exit(0 if nfail == 0 else 1)
