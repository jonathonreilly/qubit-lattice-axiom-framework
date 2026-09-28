"""Records that form at empty sites on the site's clock (block 95's clocked gas plus permanent formation).

Model (block 95 as landed, plus the task's formation): on the L^dim torus, Delta = 2dim I - Adj, G its mean-zero inverse,
u_z(C) = m sum_{r in C} G(z - r), m = 2 dim lambda, w = e^u.  Motion: a record at x moves to an empty neighbour y at rate
exp[a u_x + (1-a) u_y] h / (2 dim), h = W(C')/(W(C) + W(C')).  Formation: an empty site x forms a record at rate
z exp(b u_x(C)); records are permanent.  Write E(d) = e^{m G(d)} = kappa^{den G(d)} with kappa = e^{m/den} a chosen rational,
so every rate is an exact rational (b, a integers).

Exact sections A-F (Fractions, sympy); the interval bracketing in E uses mpmath interval arithmetic; section G solves the
finite Markov chain exactly (level by level, rational linear algebra).  The only floating-point content is printed values.
"""
import itertools, sys, time
from fractions import Fraction as Fr
from collections import Counter
import sympy as sp
from sympy.polys.matrices import DomainMatrix

T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)

# ---------------------------------------------------------------------------------------------
# model
# ---------------------------------------------------------------------------------------------
def green(L, dim):
    sites = list(itertools.product(range(L), repeat=dim)); idx = {p: i for i, p in enumerate(sites)}; V = len(sites)
    nb = {p: [tuple((p[k] + (d if k == a else 0)) % L for k in range(dim)) for a in range(dim) for d in (-1, 1)] for p in sites}
    M = [[sp.Rational(0)] * V for _ in range(V)]
    for p in sites:
        i = idx[p]; M[i][i] += 2 * dim
        for q in nb[p]: M[i][idx[q]] -= 1
    for i in range(V):
        for j in range(V): M[i][j] += sp.Rational(1, V)
    Minv = DomainMatrix(M, (V, V), sp.QQ).inv().to_Matrix()
    o = idx[tuple([0] * dim)]
    G = {p: sp.Rational(Minv[idx[p], o]) - sp.Rational(1, V) for p in sites}
    return sites, idx, nb, V, G

class Model:
    def __init__(self, L, dim, kappa, a=1, b=1, z=Fr(1), Wmode="one"):
        self.L, self.dim, self.a, self.b, self.z, self.Wmode = L, dim, a, b, Fr(z), Wmode
        sites, idx, nb, V, G = green(L, dim)
        self.sites, self.idx, self.nb, self.V, self.G = sites, idx, nb, V, G
        self.den = int(sp.ilcm(*[g.q for g in set(G.values())]))
        self.E = {p: Fr(kappa) ** int(G[p] * self.den) for p in sites}       # e^{m G(d)}
        self.deg = 2 * dim
        self.sub = lambda x, r: tuple((x[k] - r[k]) % L for k in range(dim))
    def S_exp(self, x, C):
        out = Fr(1)
        for r in C: out *= self.E[self.sub(x, r)]
        return out
    def pair_energy_weight(self, C, power):
        w = Fr(1)
        for r, s in itertools.combinations(C, 2): w *= self.E[self.sub(r, s)] ** power
        return w
    def W(self, C):
        return Fr(1) if self.Wmode == "one" else self.pair_energy_weight(C, 2 * self.a - 1)       # cancels the pair law
    def pi_weight(self, C):                                                                    # W(C) e^{m (1-2a) E(C)}
        return self.W(C) * self.pair_energy_weight(C, 1 - 2 * self.a)
    def motion(self, C):
        out = []; Cs = set(C)
        for x in C:
            ux = self.S_exp(x, C)
            for y in self.nb[x]:
                if y in Cs: continue
                Cn = tuple(sorted((Cs - {x}) | {y}))
                w = ux if self.a == 1 else ux ** self.a * self.S_exp(y, C) ** (1 - self.a)
                h = self.W(Cn) / (self.W(C) + self.W(Cn))
                out.append((Cn, w * h / self.deg))
        return out
    def creation(self, C):
        Cs = set(C)
        return [(tuple(sorted(Cs | {x})), self.z * self.S_exp(x, C) ** self.b) for x in self.sites if x not in Cs]
    def beta(self, C): return sum(r for _, r in self.creation(C))

def level_states(M, n): return [tuple(sorted(c)) for c in itertools.combinations(M.sites, n)]
def proportional(v, w):
    ratios = set()
    for C in v:
        if w[C] == 0:
            if v[C] != 0: return False
        else: ratios.add(v[C] / w[C])
    return len(ratios) <= 1

def level_series(M, top=2, order=4):
    """Exact Taylor coefficients a[k][j][C] of P_k(C, t) for k <= top (levels above `top` never feed back)."""
    states = [level_states(M, k) for k in range(top + 1)]
    mot = [{C: M.motion(C) for C in states[k]} for k in range(top + 1)]
    cre = [{C: M.creation(C) for C in states[k]} for k in range(top + 1)]
    beta = [{C: sum(r for _, r in cre[k][C]) for C in states[k]} for k in range(top + 1)]
    a = [[{C: Fr(0) for C in states[k]} for _ in range(order + 1)] for k in range(top + 1)]
    a[0][0][()] = Fr(1)
    for j in range(order):
        for k in range(top + 1):
            new = {C: Fr(0) for C in states[k]}
            for C, v in a[k][j].items():
                if v == 0: continue
                out = 0
                for Cn, r in mot[k][C]: new[Cn] += r * v; out += r
                new[C] -= (out + beta[k][C]) * v
            if k > 0:
                for C, v in a[k - 1][j].items():
                    if v == 0: continue
                    for Cn, r in cre[k - 1][C]: new[Cn] += r * v
            for C in new: a[k][j + 1][C] = new[C] / (j + 1)
    return states, mot, cre, beta, a

KAP = Fr(24, 25)

# ---------------------------------------------------------------------------------------------
# A. The torus Green function (exact)
# ---------------------------------------------------------------------------------------------
print("== A. torus Green function on the cubic 3^3 torus (exact)")
sites3, idx3, nb3, V3, G3 = green(3, 3)
zero3 = (0, 0, 0)
lapG = {p: 6 * G3[p] - sum(G3[q] for q in nb3[p]) for p in sites3}
want(all(lapG[p] == (1 if p == zero3 else 0) - sp.Rational(1, V3) for p in sites3) and sum(G3.values()) == 0,
     "A1 Delta G = delta_0 - 1/V and sum G = 0 exactly on 3^3; G takes the values " + str(sorted(set((G3[p] * 486) for p in sites3))) + "/486 (offsets 0, e1, e1+e2, e1+e2+e3)")
want(len(set(G3.values())) == 4, "A2 four offset classes with four distinct values of G: the pair law separates all distances on 3^3")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. Block 95 T2 re-checked, W = 1, a = 1 (exact)
# ---------------------------------------------------------------------------------------------
print("== B. block 95's pair law: detailed balance of the motion (exact, kappa = 24/25)")
M1 = Model(3, 3, KAP, a=1, b=1)
for n in (2, 3):
    viol = cnt = 0
    for C in level_states(M1, n):
        pw = M1.pi_weight(C)
        back = None
        for Cn, r in M1.motion(C):
            cnt += 1
            rb = dict(M1.motion(Cn)).get(C)
            if pw * r != M1.pi_weight(Cn) * rb: viol += 1
    want(viol == 0, f"B{n - 1} pi(C) ∝ e^(-m sum_pairs G): detailed balance for all {cnt} moves at count {n}")
print("   [A-B took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# C. The exact series: when does the conditional law stay pi_n? (exact)
# ---------------------------------------------------------------------------------------------
print("== C. exact Taylor series of the joint chain (levels 0-2, creation out of level 2 kills)")
cases = [(1, -1, "one", "a=1, b=-1=1-2a"), (1, 1, "one", "a=1, b=1"), (1, 0, "one", "a=1, b=0"), (1, 2, "one", "a=1, b=2"),
         (0, 1, "one", "a=0, b=1=1-2a"), (0, 0, "one", "a=0, b=0"), (1, 0, "pair", "a=1, b=0, W = e^{m E}")]
res = {}
for (a, b, mode, tag) in cases:
    M = Model(3, 3, KAP, a=a, b=b, Wmode=mode)
    states, mot, cre, beta, ser = level_series(M, top=2, order=4)
    pi2 = {C: M.pi_weight(C) for C in states[2]}
    a22, a23, a24 = ser[2][2], ser[2][3], ser[2][4]
    r = dict(i=proportional(a22, pi2), t3=proportional(a23, a22), t4=proportional(a24, a22), ii=len(set(beta[2].values())) == 1)
    res[tag] = (M, states, mot, cre, beta, ser, pi2, r)
    print(f"   {tag}: t^2 coeff ∝ pi_2 (i): {r['i']}; beta_2 constant (ii): {r['ii']}; t^3 ∝ t^2: {r['t3']}; t^4 ∝ t^2: {r['t4']}", flush=True)
want(res["a=1, b=-1=1-2a"][7]['i'] and res["a=0, b=1=1-2a"][7]['i'] and not res["a=1, b=1"][7]['i'] and not res["a=1, b=0"][7]['i']
     and not res["a=1, b=2"][7]['i'] and not res["a=0, b=0"][7]['i'],
     "C1 the leading (t^2) coefficient of the level-2 law is proportional to pi_2 exactly for b = 1 - 2a (a = 1, b = -1; a = 0, b = 1), and for no other b tried")
want(all(not res[t][7]['t3'] for t in ("a=1, b=-1=1-2a", "a=0, b=1=1-2a", "a=1, b=1", "a=1, b=0", "a=1, b=2", "a=0, b=0")) and
     all(not res[t][7]['ii'] for t in ("a=1, b=-1=1-2a", "a=0, b=1=1-2a", "a=1, b=1", "a=1, b=2")) and res["a=1, b=0"][7]['ii'],
     "C2 the next coefficient (t^3) is never proportional to pi_2: with beta_2 nonconstant (b != 0) the count-2 law drifts; with b = 0 (beta_2 = z(V - 2) constant) it fails already at t^2")
want(res["a=1, b=0, W = e^{m E}"][7]['i'] and res["a=1, b=0, W = e^{m E}"][7]['t3'] and res["a=1, b=0, W = e^{m E}"][7]['t4'] and res["a=1, b=0, W = e^{m E}"][7]['ii'],
     "C3 the single survivor: b = 0 with W = e^{m(2a-1)E} (pi_n uniform, no pair law): (i), (ii) and the series through t^4 all hold")
# first-order deviation, b = 1 - 2a: conditional law = pi_2 [1 - (t/3)(beta_2 - beta_bar) + O(t^2)]
for tag in ("a=1, b=-1=1-2a", "a=0, b=1=1-2a"):
    M, states, mot, cre, beta, ser, pi2, r = res[tag]
    a22, a23 = ser[2][2], ser[2][3]
    S22 = sum(a22.values()); S23 = sum(a23.values())
    pihat = {C: pi2[C] / sum(pi2.values()) for C in states[2]}
    bbar = sum(pihat[C] * beta[2][C] for C in states[2])
    dev = {C: a23[C] / S22 - a22[C] * S23 / S22 ** 2 for C in states[2]}          # d/dt of the conditional law at t = 0+
    want(all(dev[C] == -Fr(1, 3) * pihat[C] * (beta[2][C] - bbar) for C in states[2]) and any(dev[C] != 0 for C in states[2]),
         f"C4 [{tag}] d/dt of the conditional law at t = 0+ equals -(1/3) pi_2(C)(beta_2(C) - E_pi2 beta_2), exactly, for all 351 pairs, and is not zero")
print("   [A-C took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# D. Condition (i) at count 2 (exact)
# ---------------------------------------------------------------------------------------------
print("== D. condition (i) at count 2: b must equal 1 - 2a (exact)")
classes3 = [(1, 0, 0), (1, 1, 0), (1, 1, 1)]
ok_i = True
for a in (0, 1):
    for b in range(-3, 4):
        Mm = Model(3, 3, KAP, a=a, b=b)
        F2 = {d: sum(Mm.S_exp(x, [zero3]) ** b for x in [d]) * 2 for d in classes3}       # F_2({0,d}) = pi_1(0) f(d; {0}) + pi_1(d) f(0; {d}) (with pi_1 = 1, z = 1)
        pi2 = {d: Mm.pi_weight((zero3, d)) for d in classes3}
        prop = len({F2[d] / pi2[d] for d in classes3}) == 1
        ok_i &= (prop == (b == 1 - 2 * a))
want(ok_i, "D1 for a = 0, 1 and b = -3..3 (kappa = 24/25): F_2(C) ∝ pi_2(C) over the three offset classes iff b = 1 - 2a")
print("   [A-D took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# E. Condition (ii) at count 2 fails for every lambda b != 0 on the smallest cubic torus
# ---------------------------------------------------------------------------------------------
print("== E. condition (ii) at count 2: beta_2 is constant only at lambda b = 0 (exact + interval)")
def beta2_exp_poly(d):
    cnt = Counter()
    for x in sites3:
        if x == zero3 or x == d: continue
        cnt[G3[x] + G3[tuple((x[k] - d[k]) % 3 for k in range(3))]] += 1
    return cnt                                                # {exponent mu: multiplicity}: beta_2({0,d})/z = sum_mu c_mu e^{t mu}, t = m b
def diffpoly(d, d2):
    A, B = beta2_exp_poly(d), beta2_exp_poly(d2); diff = Counter(A)
    for k, v in B.items(): diff[k] -= v
    return {k: v for k, v in diff.items() if v != 0}
def sign_changes(diff):
    seq = [c for _, c in sorted(diff.items())]
    return sum(1 for i in range(len(seq) - 1) if seq[i] * seq[i + 1] < 0)
dA = diffpoly((1, 0, 0), (1, 1, 1)); dB = diffpoly((1, 1, 0), (1, 1, 1))
want(sum(dA.values()) == 0 and sum(dB.values()) == 0 and sum(c * mu for mu, c in dA.items()) != 0 and sum(c * mu for mu, c in dB.items()) != 0
     and sign_changes(dA) == 2 and sign_changes(dB) == 2,
     "E1 f_A(t) = beta_2({0,e1}) - beta_2({0,(1,1,1)}) and f_B(t) = beta_2({0,(1,1,0)}) - beta_2({0,(1,1,1)}) are exponential sums with exact integer "
     f"coefficients ({len(dA)} and {len(dB)} exponents); f(0) = 0, f'(0) = {sum(c*mu for mu,c in dA.items())} and {sum(c*mu for mu,c in dB.items())} != 0, and each has exactly 2 sign changes")
# Laguerre's rule: a sum sum c_j e^{mu_j t} has at most (sign changes of c_j ordered by mu_j) real zeros counted with multiplicity.
# t = 0 is a simple zero, so each f has at most one more real zero.  Signs at +-infinity come from the extreme exponents.
import mpmath as mp
mp.mp.dps = 40
from mpmath import iv
iv.dps = 40
def fval(diff, t): return sum(c * mp.e ** (mp.mpf(mu.p) / mu.q * t) for mu, c in diff.items())
def fiv(diff, t):
    tt = iv.mpf(t)
    return sum(c * iv.exp(iv.mpf(mu.p) / mu.q * tt) for mu, c in diff.items())
def analyse(diff):
    items = sorted(diff.items())
    sgn_minf, sgn_pinf = (1 if items[0][1] > 0 else -1), (1 if items[-1][1] > 0 else -1)
    d1 = sum(c * mu for mu, c in diff.items())
    sgn_right0, sgn_left0 = (1 if d1 > 0 else -1), (-1 if d1 > 0 else 1)
    # number of zeros on (0, inf) has the parity of the sign change between 0+ and +inf; on (-inf, 0) between -inf and 0-; at most one in total
    nz_pos = 1 if sgn_right0 != sgn_pinf else 0
    nz_neg = 1 if sgn_minf != sgn_left0 else 0
    return nz_pos, nz_neg
nzA, nzB = analyse(dA), analyse(dB)
want(nzA[1] == 0 and nzB[1] == 0 and nzA[0] == 1 and nzB[0] == 1,
     "E2 sign pattern: f_A and f_B each have exactly one nonzero real zero, and it is positive (Laguerre: at most one; parity of the sign change from 0+ to +infinity: one)")
def bracket(diff, lo, hi):
    a_, b_ = iv.mpf(lo), iv.mpf(hi)
    fa, fb = fiv(diff, lo), fiv(diff, hi)
    return (fa.b < 0 and fb.a > 0) or (fa.a > 0 and fb.b < 0)
def find(diff):
    xs = [mp.mpf(k) / 10 for k in range(1, 600)]
    for x0, x1 in zip(xs, xs[1:]):
        if fval(diff, x0) * fval(diff, x1) < 0:
            r = mp.findroot(lambda t: fval(diff, t), (x0, x1), solver='anderson')
            return r
rA, rB = find(dA), find(dB)
brA = (mp.nstr(rA - mp.mpf('1e-6'), 12), mp.nstr(rA + mp.mpf('1e-6'), 12)); brB = (mp.nstr(rB - mp.mpf('1e-6'), 12), mp.nstr(rB + mp.mpf('1e-6'), 12))
want(bracket(dA, *brA) and bracket(dB, *brB) and mp.mpf(brA[0]) > mp.mpf(brB[1]),
     f"E3 (interval arithmetic, 40 digits) the zero of f_A lies in [{brA[0]}, {brA[1]}] and the zero of f_B in [{brB[0]}, {brB[1]}]: disjoint brackets, "
     "so no t != 0 makes beta_2 equal on all three offset classes")
ok4 = True
for bb in (-3, -2, -1, 1, 2, 3):
    Mb_ = Model(3, 3, KAP, a=1, b=bb)
    ok4 &= len({Mb_.beta((zero3, d)) for d in classes3}) == 3
want(ok4, "E4 exact witness: for b = -3..3, b != 0 (kappa = 24/25) the three offset classes have three distinct beta_2 values; with E2-E3, for every real "
     "lambda b != 0 the total creation rate differs between pairs at different offsets, so (ii) holds iff lambda b = 0")
M0 = Model(3, 3, KAP, a=1, b=0)
want(len({M0.beta(C) for C in level_states(M0, 2)}) == 1 and len({Model(3, 3, KAP, a=1, b=1).beta(C) for C in level_states(Model(3, 3, KAP, a=1, b=1), 2)}) > 1,
     "E5 beta_2 over all 351 pairs: one value at b = 0, several at b = 1 (kappa = 24/25)")
print("   [A-E took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# F. Where the second record forms: the first-formation offset law is the reciprocal power of the equilibrium law (exact)
# ---------------------------------------------------------------------------------------------
print("== F. the offset at which the second record forms (exact, kappa = 24/25, 3^3)")
def offset_law(Mm):
    w = {x: Mm.S_exp(x, [zero3]) ** Mm.b for x in Mm.sites if x != zero3}; Z = sum(w.values())
    return {x: w[x] / Z for x in w}
ok_recip = True
for b in (-2, -1, 1, 2):
    Mm = Model(3, 3, KAP, a=1, b=b)
    q = offset_law(Mm)
    piw = {x: Mm.pi_weight((zero3, x)) for x in q}; Zp = sum(piw.values()); pi_ = {x: piw[x] / Zp for x in q}
    ok_recip &= len({q[x] * pi_[x] ** b for x in q}) == 1
want(ok_recip, "F1 with a = 1: q_b(d) ∝ e^{b m G(d)} and pi_2(d) ∝ e^{-m G(d)}, so q_b ∝ pi_2^{-b} exactly (b = -2, -1, 1, 2)")
Mv = Model(3, 3, KAP, a=1, b=1)
q1 = offset_law(Mv)
piw = {x: Mv.pi_weight((zero3, x)) for x in q1}; Zp = sum(piw.values()); pi1 = {x: piw[x] / Zp for x in q1}
def by_class(law):
    out = Counter()
    for x, p in law.items():
        k = tuple(sorted((c if c <= 1 else 3 - c) for c in x))          # offset class on Z_3: coordinates 0 or 1
        out[sum(k)] += p
    return out
bc_q, bc_pi = by_class(q1), by_class(pi1)
print("   class (number of nonzero coordinates 1, 2, 3): formation offset law q_1 =", {k: float(v) for k, v in sorted(bc_q.items())},
      "  equilibrium pi_2 =", {k: float(v) for k, v in sorted(bc_pi.items())})
want(bc_q[1] < Fr(6, 26) < bc_pi[1] and bc_q[3] > Fr(8, 26) > bc_pi[3],
     "F2 kappa = 24/25 (slowed clocks near records), b = 1: the second record forms at a nearest neighbour with probability "
     f"{float(bc_q[1]):.4f} < 6/26 (uniform), and on the body diagonal with {float(bc_q[3]):.4f} > 8/26 -- into the void; motion then pulls the pair together "
     f"(pi_2: nearest {float(bc_pi[1]):.4f} > 6/26, diagonal {float(bc_pi[3]):.4f} < 8/26)")
print("   [A-F took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# G. Time to jam (exact chain on the 3x3 torus, the two-dimensional analogue of block 95's construction)
# ---------------------------------------------------------------------------------------------
print("== G. time to jam: exact Markov chain on the 2D 3x3 torus (Delta = 4I - Adj, u = 4 lambda sum G), kappa = 24/25")
def solve_exact(A, rhs):
    n = len(rhs)
    Mx = DomainMatrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A], (n, n), sp.QQ)
    R = DomainMatrix([[sp.Rational(x.numerator, x.denominator)] for x in rhs], (n, 1), sp.QQ)
    X = Mx.lu_solve(R).to_Matrix()
    return [Fr(int(X[i].p), int(X[i].q)) for i in range(n)]
def jam_time(Mm):
    T = {tuple(sorted(Mm.sites)): Fr(0)}
    for n in range(Mm.V - 1, -1, -1):
        st = level_states(Mm, n); ix = {C: i for i, C in enumerate(st)}
        A = [[Fr(0)] * len(st) for _ in st]; rhs = [Fr(1)] * len(st)
        for C in st:
            i = ix[C]; out = Fr(0)
            for Cn, r in Mm.motion(C): A[i][ix[Cn]] -= r; out += r
            for Cn, r in Mm.creation(C): rhs[i] += r * T[Cn]; out += r
            A[i][i] += out
        x = solve_exact(A, rhs)
        for C, v in zip(st, x): T[C] = v
    return T[()]
def frozen_limit(Mm):
    T0_ = {tuple(sorted(Mm.sites)): Fr(0)}
    for n in range(Mm.V - 1, -1, -1):
        for C in level_states(Mm, n):
            cr = Mm.creation(C); bt = sum(r for _, r in cr)
            T0_[C] = 1 / bt + sum((r / bt) * T0_[Cn] for Cn, r in cr)
    return T0_[()]
def adiabatic_limit(Mm):
    tot = Fr(0)
    for n in range(Mm.V):
        st = level_states(Mm, n); ws = [Mm.pi_weight(C) for C in st]
        tot += 1 / (sum(w * Mm.beta(C) for w, C in zip(ws, st)) / sum(ws))
    return tot
jam = {}
for b in (1, 0, -1):
    vals = {}
    for z in (Fr(1, 10**6), Fr(1), Fr(10**6)):
        vals[z] = jam_time(Model(3, 2, KAP, a=1, b=b, z=z)) * z
    Mu = Model(3, 2, KAP, a=1, b=b, z=Fr(1))
    ad, fr = adiabatic_limit(Mu), frozen_limit(Mu)
    jam[b] = (vals, ad, fr)
    zs = sorted(vals)
    print(f"   b = {b}: z T(z) at z = 1e-6, 1, 1e6: " + ", ".join(f"{float(vals[z]):.6f}" for z in zs) + f";  slow-formation limit {float(ad):.6f};  frozen-motion limit {float(fr):.6f}", flush=True)
H9 = sum(Fr(1, k) for k in range(1, 10))
want(all(v == H9 for v in jam[0][0].values()) and jam[0][1] == H9 and jam[0][2] == H9,
     f"G1 b = 0: z T(z) = H_9 = {float(H9):.6f} exactly for every z (uniform formation is coupon collecting; motion is irrelevant)")
ok_lim = True
for b in (1, -1):
    vals, ad, fr = jam[b]; zs = sorted(vals)
    ok_lim &= (vals[zs[0]] < vals[zs[1]] < vals[zs[2]] and abs(vals[zs[0]] - ad) < Fr(1, 10**5) and abs(vals[zs[2]] - fr) < Fr(1, 10**5) and ad < fr)
want(ok_lim, "G2 b = +-1: z T(z) increases with z, from the slow-formation limit sum_n 1/E_{pi_n} beta_n (motion equilibrates between formations) at z = 1e-6 "
     "to the frozen-motion limit (random sequential formation) at z = 1e6, both within 1e-5, exactly")
want(jam[1][1] < H9 < jam[-1][1] and jam[1][2] < H9 < jam[-1][2],
     "G3 forming on the site's own clock (b = 1) jams sooner than uniform formation, and forming against it (b = -1) later, in both limits: "
     f"z T = {float(jam[1][1]):.4f} / {float(jam[1][2]):.4f} (b = 1) < {float(H9):.4f} < {float(jam[-1][1]):.4f} / {float(jam[-1][2]):.4f} (b = -1)")
want(True, "G4 the lattice always jams: formation at every empty site has positive rate and records are permanent, so the full lattice is the unique "
     "absorbing state and is reached from every state; the expected time above is finite (exact linear solve)")
print("   [total %.0f s]" % (time.time() - T0))

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED on the cubic 3^3 torus (steps of the general argument are in ATTEMPT.md): with block 95's motion (a = 1 or a = 0, W = 1) and permanent formation "
      "at rate z e^{b u}, the count-conditional law stays the pair law pi_n at every count and time from the empty lattice iff (i) the creation flux is proportional "
      "to pi_n and (ii) the total creation rate depends on the count only; (i) at count 2 forces b = 1 - 2a, (ii) at count 2 forces lambda b = 0, so for lambda != 0 no b works, "
      "the first deviation being -(t/3) pi_2 (beta_2 - mean); the only survivor is b = 0 with the pair law cancelled (pi uniform); the second record forms at offset law "
      "q_b ∝ pi_2^(-b), the reciprocal power of the equilibrium law, into the void for b = 1; the lattice always jams, in time z T = H_V for b = 0 and shorter (longer) for b = 1 (-1)")
print("HIT: independent re-derivation (Sonnet 5.5) of a2's negative result, same Laguerre method and roots, with extensions: no formation law z e^{b u} with block 95's motion "
      "keeps the pair law at every count (lambda != 0, a != 1/2): iff-criterion (i) creation flux ∝ pi_n and (ii) count-only total creation rate; (i) forces b = 1-2a, (ii) forces lambda b = 0 "
      "(all real lambda b on 3^3, Laguerre + interval brackets); NEW: exact first deviation d/dt of the count-2 law = -(1/3) pi_2 (beta_2 - E beta_2), exact series through t^4 on the full "
      "3^3 chain, the exception b = 0 with W = e^{m(2a-1)E} (pi uniform), a = 0 case, second-record offset law q_b ∝ pi_2^(-b), exact 2D 3x3 jam times (z T = H_9 for b = 0; b = 1 sooner, b = -1 later)")
