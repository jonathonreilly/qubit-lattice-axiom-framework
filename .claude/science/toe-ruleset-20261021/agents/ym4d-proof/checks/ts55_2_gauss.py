# ts55_2 -- Proposition GT (per-level one-loop terms sum to the running bubble) on toy multiscale Gaussian models.
# Criteria: checks/ts55_2_criteria.md (written before this script). Exact rationals only; moments by independent 1D moments.
from fractions import Fraction as Fr
import random

NP = 6           # plaquette coordinates
LEV = 4          # levels 0..3, 3 = top
CCOL = 3         # colour multiplicity

def dfact(n):    # (n-1)!! for even n, 0 for odd n
    if n % 2: return 0
    r = 1
    for k in range(n - 1, 0, -2): r *= k
    return r

def poly_mul(a, b):
    c = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            c[e] = c.get(e, Fr(0)) + ca * cb
    return c

def expect(p, var, active):
    # E over the variables in `active` (independent centred Gaussians, variances var[k]); others kept symbolic
    out = {}
    for e, c in p.items():
        f = c; ee = list(e)
        for k in active:
            n = e[k]
            if n:
                m = dfact(n)
                if m == 0: f = Fr(0); break
                f *= m * var[k] ** (n // 2)
                ee[k] = 0
        if f != 0:
            out[tuple(ee)] = out.get(tuple(ee), Fr(0)) + f
    return out

def const_of(p, nv):
    return p.get(tuple([0] * nv), Fr(0))

def build_model(seed, uvec):
    rnd = random.Random(seed)
    r = [rnd.choice([2, 3, 4]) for _ in range(LEV)]
    M = [[[rnd.randint(-3, 3) for _ in range(r[i])] for _ in range(NP)] for i in range(LEV)]
    wf = [rnd.randint(0, 4) for _ in range(3)] + [0, 0, 0]
    wg = [0, 0, 0] + [rnd.randint(0, 4) for _ in range(3)]
    if sum(wf) == 0: wf[0] = 1
    if sum(wg) == 0: wg[3] = 1
    return r, M, wf, wg

def analyse(seed, uvec):
    r, M, wf, wg = build_model(seed, uvec)
    nv = sum(r)
    off = [sum(r[:i]) for i in range(LEV)]
    var = []
    for i in range(LEV): var += [Fr(1, 1) / uvec[i]] * r[i]
    # F_p as linear polynomials in Z
    F = []
    for p in range(NP):
        lin = {}
        for i in range(LEV):
            for a in range(r[i]):
                if M[i][p][a]:
                    e = [0] * nv; e[off[i] + a] = 1
                    lin[tuple(e)] = lin.get(tuple(e), Fr(0)) + M[i][p][a]
        F.append(lin)
    def Q(w):
        tot = {}
        for p in range(NP):
            if w[p]:
                sq = poly_mul(F[p], F[p])
                for e, c in sq.items(): tot[e] = tot.get(e, Fr(0)) + w[p] * c
        return tot
    Qf, Qg = Q(wf), Q(wg)
    # X_i := E[Q | F_i], F_i = sigma(Z_i..Z_3): integrate out levels < i
    def cond(Qp, i):
        act = [k for j in range(i) for k in range(off[j], off[j] + r[j])]
        return expect(Qp, var, act)
    allv = list(range(nv))
    per = []
    for i in range(LEV - 1):
        Xi, Yi = cond(Qf, i), cond(Qg, i)
        Xn, Yn = cond(Qf, i + 1), cond(Qg, i + 1)
        val = const_of(expect(poly_mul(Xi, Yi), var, allv), nv) - const_of(expect(poly_mul(Xn, Yn), var, allv), nv)
        per.append(CCOL * val)
    X3, Y3 = cond(Qf, 3), cond(Qg, 3)
    top = CCOL * (const_of(expect(poly_mul(X3, Y3), var, allv), nv)
                  - const_of(expect(X3, var, allv), nv) * const_of(expect(Y3, var, allv), nv))
    # closed forms
    a = []
    for i in range(LEV):
        ai = [[sum(Fr(M[i][p][x] * M[i][q][x]) for x in range(r[i])) / uvec[i] for q in range(NP)] for p in range(NP)]
        a.append(ai)
    A = [[sum(a[i][p][q] for i in range(LEV)) for q in range(NP)] for p in range(NP)]
    def Agt(i):
        return [[sum(a[j][p][q] for j in range(i + 1, LEV)) for q in range(NP)] for p in range(NP)]
    def Age(k):
        return [[sum(a[j][p][q] for j in range(k, LEV)) for q in range(NP)] for p in range(NP)]
    TOTAL = 2 * CCOL * sum(wf[p] * wg[q] * A[p][q] ** 2 for p in range(NP) for q in range(NP))
    Lam, LamWrong = [], []
    for i in range(LEV - 1):
        G = Agt(i)
        Lam.append(CCOL * sum(wf[p] * wg[q] * (4 * G[p][q] * a[i][p][q] + 2 * a[i][p][q] ** 2) for p in range(NP) for q in range(NP)))
        LamWrong.append(CCOL * sum(wf[p] * wg[q] * (2 * G[p][q] * a[i][p][q] + 2 * a[i][p][q] ** 2) for p in range(NP) for q in range(NP)))
    Lam3 = 2 * CCOL * sum(wf[p] * wg[q] * a[3][p][q] ** 2 for p in range(NP) for q in range(NP))
    TREE2 = 2 * CCOL * sum(wf[p] * wg[q] * Age(2)[p][q] ** 2 for p in range(NP) for q in range(NP))
    return dict(per=per, top=top, TOTAL=TOTAL, Lam=Lam, Lam3=Lam3, LamWrong=LamWrong, TREE2=TREE2)

G1 = True; G1F_breaks = 0; G2F_breaks = 0
G3_uind = True; G3_nonzero = 0
lines = []
for seed in range(1, 13):
    uvec = [Fr(9), Fr(7), Fr(5), Fr(4)]          # decreasing toward the top, as asymptotic freedom
    R = analyse(seed, uvec)
    tel = sum(R['per']) + R['top']
    okp = all(R['per'][i] == R['Lam'][i] for i in range(LEV - 1)) and R['top'] == R['Lam3']
    if not (tel == R['TOTAL'] and okp): G1 = False
    if sum(R['LamWrong']) + R['Lam3'] != R['TOTAL']: G1F_breaks += 1
    if sum(R['Lam']) != R['TOTAL']: G2F_breaks += 1
    fine = []
    for u in (Fr(3), Fr(7)):
        Ru = analyse(seed, [u] * LEV)
        fine.append(u * u * (Ru['TOTAL'] - Ru['TREE2']))
    if fine[0] != fine[1]: G3_uind = False
    if fine[0] != 0: G3_nonzero += 1
    lines.append((seed, R['TOTAL'], [str(x) for x in R['per']], str(R['top']), str(fine[0])))
for l in lines:
    print('seed', l[0], 'TOTAL', l[1], 'per', l[2], 'top', l[3], 'u^2*FINE_2', l[4])
print('G1 (brute-force per-level == closed Lambda_i, and sum == TOTAL):', G1)
print('G1-F (4->2) breaks equality in', G1F_breaks, 'of 12')
print('G2-F (drop top) breaks equality in', G2F_breaks, 'of 12')
print('G3 u^2*FINE u-independent:', G3_uind, '; FINE nonzero in', G3_nonzero, 'of 12')
ok = G1 and G1F_breaks >= 10 and G2F_breaks >= 10 and G3_uind and G3_nonzero >= 10
print('VERDICT ts55_2:', 'PASS' if ok else 'FAIL')
