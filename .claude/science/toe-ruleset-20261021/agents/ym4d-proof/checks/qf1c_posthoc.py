#!/usr/bin/env python3
# qf1c_posthoc.py -- [POST-HOC] two secondary readings quoted in QFIX.md sections 3.3 and 12.4.
# NO pre-registered verdict attaches to this file; it exists because I quoted two hand-computed
# numbers and must either confirm or correct them.  Exact Decimal, no lock.
from decimal import Decimal as D, getcontext
getcontext().prec = 50
def dpow(x, y): return (D(y) * D(x).ln()).exp()
c_s = D("411.9229708842423061"); c_g = D("5699.632830341894211")
F = D("175.8"); R0 = D(64); S6 = D(6).sqrt(); m = 19615
def B(mm, n=400):
    t = D(0)
    for i in range(n):
        p = D(2)**(i+1)
        if p-1 > 1: t += D(mm)/p*(p-1).ln()
    return t.exp()
B8 = B(8)
def c_theta(q):
    th = D(4)/D(q); a = D(1)/(D(1)-th)
    return (D(1)-th)*dpow(D(4)*th, th/(D(1)-th)), a
def C_S1(q, mm, cs):
    ct, a = c_theta(q)
    return ((ct*dpow(D(27)*cs, a) + D(4096)*c_g)/(D(1)-D(1)/D(4)-D(1)/(D(4)*D(mm))))**D("0.5")
def Chat(q, NS, cs):
    ct, a = c_theta(q)
    ac = (D(1)+S6)*C_S1(q, m, cs)/D(m)
    t1 = dpow(D(36)*cs*D(NS), a)/2
    t3 = D(288)*(c_g + D(18)*(D(NS)*cs*dpow(R0, D(-2)+D(8)/D(q)) + D(1)/(D(36)*D(m))))
    return t1 + ac*ac/2 + t3
def CT(q, NS, cs): return S6*F*B8*Chat(q, NS, cs)
print("[POST-HOC] reading 1 -- (H2)'s worth, |N_S| = 3 (M-sharp) vs 486 (M-ct), P-max, m = 19615")
for q in [12, 100, 10**6]:
    lo, hi = CT(q, 3, c_s), CT(q, 486, c_s)
    print(f"  q = {q:>8}: C_T(|N|=3) = {lo:.5E}  C_T(|N|=486) = {hi:.5E}  ratio = {hi/lo:9.3f}"
          f"  = {D(hi/lo).log10():.3f} decades of C_T  ({2*D(hi/lo).log10():.3f} of eps_1^cut)")
print()
print("[POST-HOC] reading 2 -- room in c_s: EPSSTAR l.608's floor c_s >= 319.2 against c_s = 411.92297")
for q in [12, 32, 100, 10**6]:
    hi, lo = CT(q, 3, c_s), CT(q, 3, D("319.2"))
    print(f"  q = {q:>8}: C_T(c_s=411.9) = {hi:.5E}   C_T(c_s=319.2) = {lo:.5E}"
          f"   room = {D(hi/lo).log10():.4f} decades of C_T")
