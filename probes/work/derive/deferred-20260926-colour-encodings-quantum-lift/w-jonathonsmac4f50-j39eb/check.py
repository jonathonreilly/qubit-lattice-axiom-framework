#!/usr/bin/env python3
"""Two-pair colour encoding: can a positive (or completely positive) evolution reproduce the routed colour rates?
J:derive:deferred-20260926-colour-encodings-quantum-lift:a1   (source: Codex campaign12h_second, DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md)

R  independent reproduction (own code) of the encoding's finite facts: stabilisers 4 and 3, 336 covariance identities,
   positivity by construction, exact rational rank 14 (DomainMatrix over QQ), alternating-character multiplicities 0 and 7,
   the cubic operator transforming by the alternating character.
O  obstruction: on the winding matching (any even N >= 8), with the routed rates (1/2)(k0 + h/2) of #8600 (4), there is a
   density operator Y = X (x) rho_c2 (x) rho_c^(K-2) in the span of encoded states (X = rho_{+e1} - t* rho_{-e1}, t* the double
   smallest root (5509 - 4 sqrt 1896691)/45 of the pencil) and psi in ker Y with <psi| E(L P_Y) |psi> < 0 for every gamma != 0
   and k0 > |gamma| (exact in Q(sqrt 1896691)). Hence no positive linear map Phi_t with Phi_t E = E e^{tL} for small t > 0:
   no CPTP map, no Lindblad generator, reproduces the specified colour rates on this encoding.
"""
import itertools, sys, time
import numpy as np
import sympy as sp
from fractions import Fraction as Fr
from sympy.polys.matrices import DomainMatrix
T0clock = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

# ---------------- the encoding (built from the note's text) ----------------
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3), dtype=int)
        for i in range(3): Rm[i, perm[i]] = signs[i]
        if round(np.linalg.det(Rm)) == 1: rots.append(Rm)
cols = []
for i in range(3):
    for s in (1, -1):
        e = [0, 0, 0]; e[i] = s; cols.append(('A', tuple(e), (0, 0, 0)))
for b in itertools.product((1, -1), repeat=3): cols.append(('B', (0, 0, 0), b))
cidx = {c: i for i, c in enumerate(cols)}
def act(Rm, c): return (c[0], tuple(int(x) for x in Rm @ np.array(c[1])), tuple(int(x) for x in Rm @ np.array(c[2])))
def U(Rm):
    M = np.zeros((4, 4), dtype=np.int64); M[0, 0] = 1; M[1:, 1:] = Rm; return M
def V(Rm): return np.kron(U(Rm), U(Rm))
vA = np.array([(7*i*i + 3*i + 5) % 17 - 8 for i in range(16)], dtype=np.int64)
vB = np.array([(11*i**3 + 4*i + 1) % 19 - 9 for i in range(16)], dtype=np.int64)
a0 = ('A', (1, 0, 0), (0, 0, 0)); b0 = ('B', (0, 0, 0), (1, 1, 1))
HA = [Rm for Rm in rots if act(Rm, a0) == a0]; HB = [Rm for Rm in rots if act(Rm, b0) == b0]
SA = np.eye(16, dtype=np.int64) + sum(V(g) @ np.outer(vA, vA) @ V(g).T for g in HA)
SB = np.eye(16, dtype=np.int64) + sum(V(g) @ np.outer(vB, vB) @ V(g).T for g in HB)
rho_int = [None]*14; trS = [None]*14
for c in cols:
    base, Sm = (a0, SA) if c[0] == 'A' else (b0, SB)
    reps = [Rm for Rm in rots if act(Rm, base) == c]
    mats = {V(g).tobytes(): None for g in reps}
    Ms = [V(g) @ Sm @ V(g).T for g in reps]
    assert all(np.array_equal(Ms[0], M) for M in Ms)            # independent of the transporter
    rho_int[cidx[c]] = Ms[0]; trS[cidx[c]] = int(np.trace(Sm))
evec = [np.array(c[1]) for c in cols]; bvec = [np.array(c[2]) for c in cols]

print("== R reproduction of the encoding's finite facts")
cov = sum(np.array_equal(V(Rm) @ rho_int[cidx[c]] @ V(Rm).T, rho_int[cidx[act(Rm, c)]]) for Rm in rots for c in cols)
check("R1 24 proper rotations, stabilisers of e1 and (1,1,1) of sizes 4 and 3, transporter-independent states, all 336 "
      "covariance identities (integer matrices), trace denominators 1168 and 2125, each S = I + sum of outer products (so rho >= I/Tr S > 0)",
      len(rots) == 24 and len(HA) == 4 and len(HB) == 3 and cov == 336 and sorted(set(trS)) == [1168, 2125], f"{cov} identities")
Mcol = DomainMatrix([[sp.QQ(int(v), trS[k]) for v in rho_int[k].flatten()] for k in range(14)], (14, 256), sp.QQ)
check("R2 exact rational rank of the 14 states in the 256-dim operator space is 14 (DomainMatrix over QQ; injective on the simplex)",
      Mcol.rank() == 14)
# alternating character of O ~ S4: sign of the permutation of the four body diagonals
diags = [np.array(d) for d in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]]
def alt(Rm):
    perm = []
    for d in diags:
        im = Rm @ d
        perm.append(next(i for i, e in enumerate(diags) if np.array_equal(e, im) or np.array_equal(e, -im)))
    inv_ = sum(1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j]); return (-1)**inv_
trV = [int(np.trace(V(Rm))) for Rm in rots]
mH = Fr(sum(alt(Rm)*tr for Rm, tr in zip(rots, trV)), 24); mE = Fr(sum(alt(Rm)*tr*tr for Rm, tr in zip(rots, trV)), 24)
Wc = sp.zeros(16, 16)
for k in range(6, 14): Wc += sp.Rational(int(np.prod(bvec[k])), trS[k])*sp.Matrix(rho_int[k].tolist())
cub_ok = Wc != sp.zeros(16, 16) and all(sp.Matrix(V(Rm).tolist())*Wc*sp.Matrix(V(Rm).T.tolist()) == alt(Rm)*Wc for Rm in rots)
check("R3 alternating-character multiplicity 0 in the 16-dim Hilbert representation and 7 in its operator space; the cubic "
      "operator sum_b b1 b2 b3 rho_b is nonzero and transforms by that character", mH == 0 and mE == 7 and cub_ok,
      f"multiplicities {mH}, {mE}; Frobenius^2 = {sum(v*v for v in Wc)}")

print("== O obstruction to positive dynamics")
D = 1896691
class Q:
    __slots__ = ('x', 'y')
    def __init__(s, x, y=0): s.x = Fr(x); s.y = Fr(y)
    def __add__(s, o): o = o if isinstance(o, Q) else Q(o); return Q(s.x + o.x, s.y + o.y)
    __radd__ = __add__
    def __neg__(s): return Q(-s.x, -s.y)
    def __sub__(s, o): return s + (-(o if isinstance(o, Q) else Q(o)))
    def __mul__(s, o):
        o = o if isinstance(o, Q) else Q(o); return Q(s.x*o.x + D*s.y*o.y, s.x*o.y + s.y*o.x)
    __rmul__ = __mul__
    def inv(s):
        n = s.x*s.x - D*s.y*s.y; return Q(s.x/n, -s.y/n)
    def iszero(s): return s.x == 0 and s.y == 0
    def sign(s):
        if s.y == 0: return (s.x > 0) - (s.x < 0)
        if s.x == 0: return (s.y > 0) - (s.y < 0)
        if (s.x > 0) == (s.y > 0): return 1 if s.x > 0 else -1
        c = s.x*s.x - D*s.y*s.y
        return 0 if c == 0 else ((1 if s.x > 0 else -1) if c > 0 else (1 if s.y > 0 else -1))
    def __float__(s): return float(s.x) + float(s.y)*D**0.5
def nullspace(M):
    M = [row[:] for row in M]; n = len(M); m = len(M[0]); piv = []; r = 0
    for c in range(m):
        pr = next((i for i in range(r, n) if not M[i][c].iszero()), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]; iv = M[r][c].inv(); M[r] = [v*iv for v in M[r]]
        for i in range(n):
            if i != r and not M[i][c].iszero():
                fac = M[i][c]; M[i] = [a - fac*b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == n: break
    basis = []
    for fc in [c for c in range(m) if c not in piv]:
        v = [Q(0)]*m; v[fc] = Q(1)
        for i, pc in enumerate(piv): v[pc] = -M[i][fc]
        basis.append(v)
    return basis
ap = cidx[('A', (1, 0, 0), (0, 0, 0))]; am = cidx[('A', (-1, 0, 0), (0, 0, 0))]
t = sp.symbols('t')
Ai = rho_int[ap]*trS[am]; Bi = rho_int[am]*trS[ap]
vals = [int(DomainMatrix([[sp.ZZ(int(Ai[i, j] - s*Bi[i, j])) for j in range(16)] for i in range(16)], (16, 16), sp.ZZ).det()) for s in range(17)]
Ppol = sp.Poly(sp.interpolate(list(zip(range(17), vals)), t), t)
fl = sp.factor_list(Ppol.as_expr())
facs = {tuple(sp.Poly(f, t).all_coeffs()): m for f, m in fl[1]}
ts = sp.Rational(5509, 45) - sp.Rational(4, 45)*sp.sqrt(D)
others_larger = all(all(r > ts for r in sp.Poly(f, t).real_roots()) for f, m in fl[1] if tuple(sp.Poly(f, t).all_coeffs()) != (45, -11018, 45))
check("O1 det(rho_{+e1} - t rho_{-e1}) = c (t-1)^8 (19t^2-3174t+19)(71t^2-11054t+71)(45t^2-11018t+45)^2 (exact, degree 16); "
      "its smallest root is the double root t* = (5509 - 4 sqrt 1896691)/45 ~ 0.0040843, so X = rho_{+e1} - t* rho_{-e1} >= 0 "
      "(definite pencil, rho_{-e1} > 0) with a two-dimensional kernel",
      Ppol.degree() == 16 and facs.get((1, -1)) == 8 and facs.get((45, -11018, 45)) == 2 and facs.get((19, -3174, 19)) == 1
      and facs.get((71, -11054, 71)) == 1 and others_larger and sp.simplify(45*ts**2 - 11018*ts + 45) == 0, f"t* = {sp.N(ts, 12)}")
tstar = Q(Fr(5509, 45), Fr(-4, 45))
Xq = [[Q(Fr(int(rho_int[ap][i, j]), trS[ap])) - tstar*Fr(int(rho_int[am][i, j]), trS[am]) for j in range(16)] for i in range(16)]
ker = nullspace(Xq); phi = ker[0]
Xphi_zero = all(sum((Xq[i][j]*phi[j] for j in range(16)), Q(0)).iszero() for i in range(16))
trX = Q(1) - tstar
check("O2 exact kernel over Q(sqrt 1896691): dim ker X = 2, X phi = 0 for the first basis vector phi, and Tr X = 1 - t* > 0 "
      "(Y / Tr Y is a density operator)", len(ker) == 2 and Xphi_zero and trX.sign() == 1)
def qf(u, k, v):
    R = rho_int[k]; s = Q(0)
    for i in range(16):
        if u[i].iszero(): continue
        acc = Q(0)
        for j in range(16):
            if R[i, j] != 0 and not v[j].iszero(): acc = acc + v[j]*int(R[i, j])
        s = s + u[i]*acc
    return Q(s.x/trS[k], s.y/trS[k])
def S1(delta, x, y): return Fr(1, 2)*int(np.array(delta) @ (np.cross(evec[x], bvec[y]) + np.cross(evec[y], bvec[x])))
def h1(delta, l, x, y, r): return S1(delta, l, x) + S1(delta, x, r) - S1(delta, l, y) - S1(delta, y, r)
p = {ap: Q(1), am: -tstar}
c_bg, c2, d0 = 1, 7, (0, 1, 0)                   # background colour -e1, pair-2 colour b = (1,1,-1), route direction +e2
zeta = [Q(int(z)) for z in np.random.default_rng(0).integers(-3, 4, size=16)]
f = [qf(phi, k, phi) for k in range(14)]; mm = [qf(phi, k, zeta) for k in range(14)]; nn = [qf(zeta, k, zeta) for k in range(14)]
gco = [f, [2*x for x in mm], nn]
T0 = []; T1 = []
for j in range(3):
    g = gco[j]; s0 = Q(0); s1 = Q(0)
    for a in (ap, am):
        brM = f[c_bg]*f[c_bg]*p[a]*(f[c2]*g[a] - f[a]*g[c2])        # channel (pair 1, d0): pair 1 <-> pair 2, contexts background
        brS = f[c_bg]*p[a]*f[a]*(g[c_bg]*f[c2] - g[c2]*f[c_bg])     # channel (pair 2, d0): pair 2 <-> background, pair 1 = context l
        s0 = s0 + brM + brS
        s1 = s1 + brM*h1(d0, c_bg, a, c2, c_bg) + brS*h1(d0, a, c2, c_bg, c_bg)
    T0.append(s0); T1.append(s1)
check("O3 with chi = phi + s zeta: <psi|E(L P_Y)|psi> / (positive background factor) = (k0/2) T0(s) + (gamma/4) T1(s) with "
      "T0 = s^2 T0_2, T0_2 > 0, T1_0 = 0 and T1_1 != 0 (exact)",
      T0[0].iszero() and T0[1].iszero() and T0[2].sign() == 1 and T1[0].iszero() and T1[1].sign() != 0 and all(x.sign() > 0 for x in f),
      f"T0_2 = {float(T0[2]):.6g}, T1_1 = {float(T1[1]):.6g}, T1_2 = {float(T1[2]):.6g}")
gam, k0 = Fr(1), Fr(11, 10); s_w = Fr(-1, 10000) if T1[1].sign() > 0 else Fr(1, 10000)
tot = (k0/2)*(T0[2]*(s_w*s_w)) + (gam/4)*(T1[1]*s_w + T1[2]*(s_w*s_w))
check("O4 explicit witness gamma = 1, k0 = 11/10, s = -1/10000: <psi|E(L P_Y)|psi> < 0 exactly; for every gamma != 0 and "
      "k0 > |gamma| the choice s = -sign(gamma T1_1) sigma with 0 < sigma < |gamma T1_1|/(2 k0 T0_2 + |gamma T1_2|) is negative",
      tot.sign() == -1, f"value {float(tot):.4g}")
# float cross-check of the two-channel reduction against the whole-lattice channel sum
gamf, k0f = 1.0, 1.1
dirs = [np.array(d) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def Smat(delta): return np.array([[gamf/2*delta @ (np.cross(evec[x], bvec[y]) + np.cross(evec[y], bvec[x])) for y in range(14)] for x in range(14)])
RT = {}
for dd in dirs[1:]:
    Sd = Smat(dd)
    RT[tuple(dd)] = 0.5*(k0f + (Sd[:, :, None, None] + Sd[None, :, None, :] - Sd[:, None, :, None] - Sd[None, None, :, :])/2)
rho_f = [rho_int[k]/trS[k] for k in range(14)]
def lattice_sum(special, background, N):
    spec = set(special); total = 0.0
    def get(site): return special.get(tuple(int(x) % N for x in site), background)
    for u in itertools.product(range(N), repeat=3):
        if sum(u) % 2: continue
        for dd in dirs[1:]:
            a = dd - np.array([1, 0, 0]); fp = [tuple((np.array(u) + k*a) % N) for k in (-1, 0, 1, 2)]
            if len(set(fp)) < 4: raise ValueError('contexts not distinct')
            if not (set(fp) & spec) or (fp[1] not in spec and fp[2] not in spec): continue
            (wl, el), (wu, eu), (ww, ew), (wr, er) = [get(s) for s in fp]
            Wt = np.einsum('i,j,k,l->ijkl', wl, wu, ww, wr)
            val = np.sum(Wt*RT[tuple(dd)]*(np.einsum('i,k,j,l->ijkl', el, eu, ew, er) - np.einsum('i,j,k,l->ijkl', el, eu, ew, er)))
            for s in spec:
                if s not in fp: val *= special[s][0] @ special[s][1]
            total += val
    return total
phif = np.array([float(v) for v in phi]); chif = phif + float(s_w)*np.array([float(v) for v in zeta])
ef = np.array([phif @ r @ phif for r in rho_f]); eg = np.array([chif @ r @ chif for r in rho_f])
pf = np.zeros(14); pf[ap] = 1; pf[am] = -float(tstar)
wb = np.zeros(14); wb[c_bg] = 1; w2 = np.zeros(14); w2[c2] = 1
okL = True; lv = []
for N in (8, 10):
    u0 = (2, 2, 2); u1 = tuple((np.array(u0) + np.array(d0) - np.array([1, 0, 0])) % N)
    L = lattice_sum({u0: (pf, ef), u1: (w2, eg)}, (wb, ef), N); lv.append(L)
    okL &= abs(L - float(tot)) <= 1e-6*abs(float(tot)) and L < 0
check("O5 (float cross-check) the full channel sum over the winding torus, N = 8 and 10, equals the two-channel reduction at the "
      "witness and is negative", okL, f"lattice {lv[0]:.6g}, {lv[1]:.6g}; exact {float(tot):.6g}")

print(f"== done in {time.time()-T0clock:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (an obstruction) - for the faithful two-pair covariant encoding, no positive linear map, hence no "
          "CPTP channel and no Lindblad generator, reproduces the routed colour rates on encoded states over any short time: on "
          "the winding matching (even N >= 8) the density operator Y = X (x) rho_c2 (x) rho_c^(K-2), X = rho_{+e1} - t* rho_{-e1} "
          ">= 0 (t* = (5509 - 4 sqrt 1896691)/45), and psi = phi (x) (phi + s zeta) (x) phi^(K-2) in ker Y give <psi|E(L P_Y)|psi> "
          "= (k0/2) s^2 T0_2 + (gamma/4)(s T1_1 + s^2 T1_2) with T1_1 != 0, negative for small s of the right sign whenever gamma "
          "!= 0 (exact in Q(sqrt 1896691)); gamma = 0 (constant rates) is implemented by the swap Lindbladian. Encoding facts "
          "(covariance, positivity, rank 14, multiplicities 0/7, cubic operator) reproduced independently")
    print("HIT: no positive (in particular no completely positive) evolution reproduces the routed colour rates on the two-pair "
          "faithful encoding; exact PSD encoded witness with a kernel vector on which the transferred generator is negative")
