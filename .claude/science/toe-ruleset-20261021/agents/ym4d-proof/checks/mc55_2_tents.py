# mc55_2 -- exact polynomial checks of the quintic-tent facts used in MINCB55 Lemma GI_j.
# Criteria: checks/mc55_2_criteria.md (written before this script). Exact rationals only.
from fractions import Fraction as F
from itertools import product

def norm(p):
    p = [F(c) for c in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p
def add(p, q):
    n = max(len(p), len(q)); return norm([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])
def scal(a, p): return norm([F(a) * c for c in p])
def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return norm(r)
def der(p): return norm([i * p[i] for i in range(1, len(p))] or [0])
def ev(p, t): return sum(F(c) * F(t) ** i for i, c in enumerate(p))
def compose_1mt(p):  # p(1 - t)
    r = [F(0)]; base = [F(1)]; one_m_t = [F(1), F(-1)]
    for c in p:
        r = add(r, scal(c, base)); base = mul(base, one_m_t)
    return r
def polymod(p, m):  # remainder of p modulo monic-normalised m
    p = norm(p); m = norm(m); lead = m[-1]
    while len(p) >= len(m) and not (len(p) == 1 and p[0] == 0):
        c = p[-1] / lead; shift = len(p) - len(m)
        p = add(p, scal(-c, [F(0)] * shift + m))
    return p

s5 = norm([1, 0, 0, -10, 15, -6])
s3 = norm([1, 0, -3, 2])
res = []
def gate(name, cond):
    res.append((name, bool(cond))); return bool(cond)

def T1(s): return add(s, compose_1mt(s)) == [F(1)]
def T2(s):
    d1, d2 = der(s), der(der(s))
    return ev(s, 0) == 1 and ev(s, 1) == 0 and ev(d1, 0) == 0 and ev(d2, 0) == 0 and ev(d1, 1) == 0 and ev(d2, 1) == 0

ok = True
ok &= gate('T1 s5(t)+s5(1-t)==1', T1(s5))
ok &= gate('T2 C2 gluing at 0 and 1', T2(s5))
d1 = der(s5); d2 = der(d1); d3 = der(d2); d4 = der(d3)
t = [F(0), F(1)]; omt = [F(1), F(-1)]
ok &= gate("T3 s5' == -30 t^2 (1-t)^2", d1 == scal(-30, mul(mul(t, t), mul(omt, omt))))
# T4: 15/8 - 30 t^2(1-t)^2 == 30 (t-1/2)^2 (1/4 + t(1-t)) and |s5'(1/2)| = 15/8
lhs = add([F(15, 8)], scal(-30, mul(mul(t, t), mul(omt, omt))))
tmh = [F(-1, 2), F(1)]
rhs = scal(30, mul(mul(tmh, tmh), add([F(1, 4)], mul(t, omt))))
ok &= gate("T4 identity 15/8-|s5'| = 30(t-1/2)^2(1/4+t(1-t)) and |s5'(1/2)|=15/8", lhs == rhs and abs(ev(d1, F(1, 2))) == F(15, 8))
# T5: s5'' squared modulo 6t^2-6t+1 is a constant c; check c < (289/50)^2 and s5''(0)=s5''(1)=0; and s5''' == -60(6t^2-6t+1)
mq = norm([1, -6, 6])
rem = polymod(mul(d2, d2), mq)
c_ok = len(rem) == 1
c = rem[0] if c_ok else None
ok &= gate("T5 s5''' == -60 (6t^2-6t+1)", d3 == scal(-60, mq))
ok &= gate(f"T5 (s5'')^2 mod (6t^2-6t+1) is the constant {c} < (289/50)^2 = {F(289,50)**2}; s5''(0)=s5''(1)=0",
           c_ok and c < F(289, 50) ** 2 and ev(d2, 0) == 0 and ev(d2, 1) == 0)
# T6: |s5'''| at 0, 1/2, 1 is 60, 30, 60; s5'''' has single root 1/2
ok &= gate("T6 |s5'''|(0,1/2,1) = (60,30,60), s5'''' root at 1/2 only",
           [abs(ev(d3, x)) for x in (0, F(1, 2), 1)] == [60, 30, 60] and len(d4) == 2 and -d4[0] / d4[1] == F(1, 2))
# T7: tent chi(z) = s5(|z|) for |z|<1, 0 otherwise
def chi(z):
    z = abs(F(z)); return ev(s5, z) if z < 1 else F(0)
ok &= gate("T7 chi(0)=1, chi(n)=0 for 1<=|n|<=5, chi(t)+chi(t-1)=1 on a grid of [0,1]",
           chi(0) == 1 and all(chi(n) == 0 for n in list(range(1, 6)) + list(range(-5, 0)))
           and all(chi(F(i, 97)) + chi(F(i, 97) - 1) == 1 for i in range(0, 98)))
# T8: blend constant
sup = {0: F(1), 1: F(15, 8), 2: F(289, 50), 3: F(60)}
best = F(0)
for beta in product(range(4), repeat=4):
    if sum(beta) <= 3 and sum(beta) >= 1:
        pr = F(1)
        for b in beta:
            pr *= sup[b]
        best = max(best, pr)
ok &= gate(f"T8 max_|beta|<=3 prod sup|w^(beta_nu)| == 60 (got {best}); C_blend = 2^4*60*4 = {16*60*4}", best == 60)
# Control: s3 must satisfy T1 but FAIL T2
c_T1 = T1(s3); c_T2 = T2(s3)
control_fired = c_T1 and (not c_T2)
for name, v in res:
    print(('PASS ' if v else 'FAIL ') + name)
print(f"CONTROL s3: T1 {'holds' if c_T1 else 'fails'}, T2 {'holds (control did NOT fire)' if c_T2 else 'FAILS (control fired)'}; s3''(1) = {ev(der(der(s3)),1)}")
print(f"VERDICT mc55_2: {'PASS' if (ok and control_fired) else 'FAIL'}")
