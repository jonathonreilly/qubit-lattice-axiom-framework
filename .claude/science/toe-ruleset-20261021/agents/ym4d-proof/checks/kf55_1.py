# kf55_1 -- exact checks for KFACTOR_O55.md (criteria: checks/kf55_1_criteria.md, written before this file).
# Exact Fraction / int arithmetic only. No floats in any verdict (floats appear only in printed approximations).
from fractions import Fraction as F
from itertools import product

out = []
def say(s=""):
    out.append(s); print(s)

# ---------------- rigorous enclosures ----------------
def e_enclosure(N=30):
    s, fact = F(0), 1
    for n in range(N + 1):
        if n > 0: fact *= n
        s += F(1, fact)
    tail = F(2, fact * (N + 1))          # sum_{n>N} 1/n! <= 2/(N+1)!
    return s, s + tail

def ln3_enclosure(N=60):
    # ln 3 = 2 atanh(1/2) = 2 sum_{j>=0} (1/2)^{2j+1}/(2j+1); tail after j=N bounded by geometric series
    x = F(1, 2); s = F(0)
    for j in range(N + 1):
        s += x ** (2 * j + 1) / (2 * j + 1)
    tail = x ** (2 * N + 3) / (2 * N + 3) / (1 - x * x)
    return 2 * s, 2 * (s + tail)

# ---------------- Part A ----------------
d, L = 4, 3
Cf = 1 + F(2 * d) / (1 - F(1, L ** 3))
eL, eU = e_enclosure()
A1 = (Cf == F(121, 13)) and (Cf * eL >= F(2530, 100)) and (Cf * eU <= F(2531, 100))
say(f"A1: C_f = {Cf} (={float(Cf):.6f}); C_f*e in [{float(Cf*eL):.6f}, {float(Cf*eU):.6f}] -> {'PASS' if A1 else 'FAIL'}")

lnL, lnU = ln3_enclosure()
alpha = F(1, 4)
pattern_ok, undecided = True, []
for k in range(2, 10001):
    # theta* = 1/((k-1) ln3);  theta* > alpha  <=>  (k-1) ln3 < 4 ;  theta* < alpha <=> (k-1) ln3 > 4
    lo, hi = (k - 1) * lnL, (k - 1) * lnU
    if hi < 1 / alpha:   above = True
    elif lo > 1 / alpha: above = False
    else:
        undecided.append(k); continue
    expect_above = k <= 4
    if above != expect_above:
        pattern_ok = False
A2 = pattern_ok and not undecided
say(f"A2: ln3 in [{float(lnL):.12f}, {float(lnU):.12f}]; theta*>1/4 exactly for k<=4, <1/4 for 5<=k<=10000; "
    f"undecided={undecided[:5]} -> {'PASS' if A2 else 'FAIL'}")

# ---------------- Part B ----------------
kminus = F(1)
kplus_set = [F(1), F(2), F(4)]
eta_set = [F(1, 10), F(1, 100), F(1, 1000)]
As_set = [F(1), F(10), F(100)]
Aj_set = [F(1), F(10), F(100)]
Lth_set = [F(4, 3), F(2), F(5, 2)]
cB = F(1)
KMAX = 400

B1 = B2 = B3 = B4 = True
worst_B2 = None
ctrl_min_N, ctrl_min_S = None, None
for kp, eta, As, Aj, Lth in product(kplus_set, eta_set, As_set, Aj_set, Lth_set):
    kh = kp / kminus
    AB = cB * kp * L ** 2
    # B1: algebra TR-1 => TR-2
    for m in range(0, KMAX + 1):
        Lm2 = F(1, L ** (2 * m))
        T = (Lm2 * As * eta ** 2 + Lm2 * (kp * eta + As * eta ** 2 + m * Aj * eta ** 2)) / kminus
        P = cB * kp * L ** (m + 2) * eta * T
        claim = AB * eta ** 2 * kh * F(1, L ** m) * (1 + (2 * As + m * Aj) * eta / kp)
        if P != claim:
            B1 = False
    # per-level normalized row bounds a_m
    a = [min(F(1), kh * F(1, L ** m) * (1 + (2 * As + m * Aj) * eta / kp)) for m in range(0, KMAX + 1)]
    if a[0] != 1:
        B4 = False
    # M = max_m m r^m, r = Lth/L
    r = Lth / L
    seq = [m * r ** m for m in range(0, 3001)]
    M = max(seq)
    imax = seq.index(M)
    if not (imax < 1500 and all(seq[i] >= seq[i + 1] for i in range(1500, 3000))):
        B2 = False
    BPc = Lth * kh * (1 + 2 * As * eta / kp + (Aj * eta / kp) * M)
    BS = kh * (F(L, L - 1) * (1 + 2 * As * eta / kp) + F(L, (L - 1) ** 2) * (Aj * eta / kp))
    for k in range(2, KMAX + 1):
        Nk = max(Lth ** (k - l) * a[k - 1 - l] for l in range(1, k))
        Sk = sum(a[k - 1 - l] for l in range(1, k))
        if Nk > BPc or Sk > BS:
            B2 = False
            worst_B2 = (kp, eta, As, Aj, Lth, k)
        if k == KMAX:
            Nold, Sold = Lth ** (k - 1), F(k - 1)
            rN, rS = Nold / Nk, Sold / Sk
            ctrl_min_N = rN if ctrl_min_N is None else min(ctrl_min_N, rN)
            ctrl_min_S = rS if ctrl_min_S is None else min(ctrl_min_S, rS)
            if not (rN >= 10 and rS >= 10):
                B3 = False

say(f"B1 (TR-1 => TR-2 exact algebra, m<=400, 243 combos): {'PASS' if B1 else 'FAIL'}")
say(f"B2 (N_k <= B_Pc and S_k <= B_S for 2<=k<=400, all combos): {'PASS' if B2 else 'FAIL'}"
    + ("" if worst_B2 is None else f"  first failure at {worst_B2}"))
say(f"B3 (control at k=400: old/new >= 10): {'PASS' if B3 else 'FAIL'}; min old/new class-norm ratio = "
    f"{float(ctrl_min_N):.3e}, min old/new sum ratio = {float(ctrl_min_S):.3e}")
say(f"B4 (a_0 = 1: no gain claimed at the top level): {'PASS' if B4 else 'FAIL'}")

# illustrative printout (not a verdict): one combination
kp, eta, As, Aj, Lth = F(2), F(1, 100), F(10), F(10), F(2)
kh = kp
a = [min(F(1), kh * F(1, L ** m) * (1 + (2 * As + m * Aj) * eta / kp)) for m in range(0, 41)]
say("illustration (kappa_hat=2, eta=1/100, A_s=A_j=10, L^theta=2): a_m for m=0..8 = "
    + ", ".join(f"{float(x):.4f}" for x in a[:9]))
for k in (5, 10, 20, 40):
    Nk = max(Lth ** (k - l) * a[k - 1 - l] for l in range(1, k))
    Sk = sum(a[k - 1 - l] for l in range(1, k))
    say(f"  k={k}: new class norm {float(Nk):.4f} vs old {float(Lth**(k-1)):.1f}; new sum {float(Sk):.4f} vs old {k-1}")

overall = all([A1, A2, B1, B2, B3, B4])
say(f"OVERALL: {'PASS' if overall else 'FAIL'}")
