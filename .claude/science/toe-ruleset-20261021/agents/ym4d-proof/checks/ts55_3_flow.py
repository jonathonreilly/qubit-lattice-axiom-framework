# ts55_3 -- Lemma SUM / Lemma AF-cmp (TSE55 sections 3.3-3.4) on synthetic sequences obeying the pairwise flow bracket.
# Criteria: checks/ts55_3_criteria.md (written before this script). Exact rationals only.
from fractions import Fraction as Fr
import random, math

L = 3; K = 60; GAM2 = Fr(1)          # gamma^{-2} = 1, so gamma^2 = 1
PARAMS = [(Fr(1, 4), Fr(1), Fr(1, 2)), (Fr(1, 2), Fr(3, 2), Fr(1)), (Fr(1), Fr(1), Fr(0))]
KS = list(range(0, 56, 5))

def ceil_fr(x):
    return -((-x.numerator) // x.denominator)

def make_sequences(bm, bp, RF, rnd):
    uK = 1 + RF + Fr(1, 3)
    seqs = []
    # slowest / fastest
    for b in (bm, bp):
        seqs.append(('slow' if b == bm else 'fast', [uK + b * (K - j) for j in range(K + 1)]))
    for t in range(40):
        deltas = [bm + (bp - bm) * Fr(rnd.randint(0, 12), 12) for _ in range(K)]
        e = [Fr(rnd.randint(-6, 6), 12) * RF for _ in range(K)] + [Fr(0)]
        u = [uK + sum(deltas[j:K]) + e[j] for j in range(K + 1)]
        seqs.append(('rand%d' % t, u))
    return uK, seqs

def bracket_ok(u, bm, bp, RF):
    for j in range(K + 1):
        for n in range(j, K + 1):
            d = u[j] - u[n]
            if not (bm * (n - j) - RF <= d <= bp * (n - j) + RF):
                return False
    return all(x >= 1 / GAM2 for x in u)

def T_s(s, uK, bp, RF):
    best = Fr(0)
    c0 = ceil_fr((uK / 2 - RF) / bp)
    for c in range(c0, c0 + 200):
        right = 2 * (RF + bp * c)
        if right < uK:
            continue
        val = right ** s * Fr(1, L ** (8 * c)) if c >= 0 else right ** s * L ** (-8 * c)
        best = max(best, val)
    return best

def V_const(uK, bp, RF):
    q = Fr(1, L ** 4)
    best = Fr(0)
    c0 = ceil_fr((uK / 2 - RF) / bp)
    for c in range(c0, c0 + 200):
        right = 2 * (RF + bp * c)
        if right < uK:
            continue
        pw = Fr(1, L ** (4 * c)) if c >= 0 else Fr(L ** (-4 * c))
        val = right * (bp * c + RF + bp / (1 - q)) * pw / (1 - q)
        best = max(best, val)
    return best

rnd = random.Random(20261029)
S1 = True; S2 = True; S3 = True; S1F = None; S2F = None
nseq = 0; nchecked = 0; s3_trunc = 6
report = []
for (bm, bp, RF) in PARAMS:
    uK, seqs = make_sequences(bm, bp, RF, rnd)
    q8 = Fr(1, L ** 8); q4 = Fr(1, L ** 4)
    Cco = {s: (Fr(2) ** s) / (1 - q8) + GAM2 ** s * T_s(s, uK, bp, RF) / (1 - q8) for s in (2, 3)}
    Ccmp = 2 * (bp * q4 / (1 - q4) ** 2 + RF / (1 - q4)) + GAM2 * V_const(uK, bp, RF)
    omega = {n: Fr(L ** (4 * n), 2 ** (L ** n)) for n in range(1, s3_trunc + 1)}
    Cfine = 2 * sum((bp * n + RF) * omega[n] for n in omega)
    report.append(('params', str(bm), str(bp), str(RF), 'C_co(2)=%s' % float(Cco[2]), 'C_co(3)=%s' % float(Cco[3]),
                   'C_cmp=%s' % float(Ccmp)))
    for name, u in seqs:
        if not bracket_ok(u, bm, bp, RF):
            continue
        nseq += 1
        for k in KS:
            uk = u[k]
            if uk < 2 * RF + 2:
                continue
            nchecked += 1
            for s in (2, 3):
                lhs = sum(Fr(1) / u[k + n] ** s * Fr(1, L ** (8 * n)) for n in range(0, K - k + 1))
                if lhs > Cco[s] / uk ** s:
                    S1 = False; report.append(('S1 violated', name, k, s))
            lhs2 = sum(abs(Fr(1) / u[k + n] - Fr(1) / uk) * Fr(1, L ** (4 * n)) for n in range(0, K - k + 1))
            if lhs2 > Ccmp / uk ** 2:
                S2 = False; report.append(('S2 violated', name, k))
            lhs3 = sum(abs(Fr(1) / u[k - n] - Fr(1) / uk) * omega[n] for n in range(1, min(k, s3_trunc) + 1))
            if lhs3 > Cfine / uk ** 2:
                S3 = False; report.append(('S3 violated', name, k))
        if name == 'slow' and (bm, bp, RF) == PARAMS[0]:
            u0 = u[0]
            S1F = u0 ** 2 * sum(Fr(1) / u[n] ** 2 for n in range(0, K + 1))
            S2F = u0 ** 2 * sum(abs(Fr(1) / u[n] - Fr(1) / u0) for n in range(0, K + 1))
            S2F_thr = 10 * Ccmp
for r in report:
    print(r)
print('admissible sequences used:', nseq, '; (sequence, k) pairs checked:', nchecked)
print('S1 (coarse sum with canonical weights, s=2,3):', S1)
print('S1-F value u_0^2*sum u_n^-2 (no canonical weight), must exceed 10:', float(S1F))
print('S2 (AF comparison, coarse side):', S2)
print('S2-F value u_0^2*sum|1/u_n-1/u_0| (no weight):', float(S2F), ' threshold 10*C_cmp =', float(S2F_thr))
print('S3 (fine side, termwise, truncated at n <= %d):' % s3_trunc, S3)
ok = S1 and S2 and S3 and S1F > 10 and S2F > S2F_thr
print('VERDICT ts55_3:', 'PASS' if ok else 'FAIL')
