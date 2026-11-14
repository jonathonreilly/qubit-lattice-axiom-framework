"""sa55_hm: exact checks behind SRCAN55.md Lemma SA-TC (criteria: sa55_hm_criteria.md, written first).
Plain python, fractions only. No floats in any verdict. Prints to stdout only."""
from fractions import Fraction as Fr
import itertools, random, math

ok_all = True
def report(name, cond):
    global ok_all
    print(f"{name}: {'PASS' if cond else 'FAIL'}")
    if not cond:
        ok_all = False

# ---------------- C1: polarisation identity ----------------
def random_symmetric_form(p, seed):
    rng = random.Random(seed)
    # symmetric p-linear form on Q^p given by coefficients on sorted index tuples
    coeff = {}
    for idx in itertools.combinations_with_replacement(range(p), p):
        coeff[idx] = Fr(rng.randint(-9, 9))
    def T(vectors):  # vectors: list of p vectors (lists of Fractions), multilinear evaluation
        total = Fr(0)
        for idx in itertools.product(range(p), repeat=p):
            c = coeff[tuple(sorted(idx))]
            if c == 0:
                continue
            prod = c
            for k in range(p):
                prod *= vectors[k][idx[k]]
                if prod == 0:
                    break
            total += prod
        return total
    return T

def unit(p, i):
    return [Fr(1) if j == i else Fr(0) for j in range(p)]

c1_ok = True
ctrl_fires_all = True
for p in range(1, 6):
    ctrl_fired_this_p = False
    for s in range(3):
        T = random_symmetric_form(p, seed=1000 * p + s)
        lhs = T([unit(p, i) for i in range(p)])
        acc = Fr(0)
        for eps in itertools.product([1, -1], repeat=p):
            v = [Fr(e) for e in eps]
            sign = 1
            for e in eps:
                sign *= e
            acc += sign * T([v] * p)
        rhs = acc / (2 ** p * math.factorial(p))
        rhs_wrong = acc / (2 ** p)
        if lhs != rhs:
            c1_ok = False
            print(f"  C1 mismatch p={p} seed={s}: lhs={lhs} rhs={rhs}")
        if lhs != rhs_wrong:
            ctrl_fired_this_p = True
    if p >= 2 and not ctrl_fired_this_p:
        ctrl_fires_all = False
    print(f"  C1 p={p}: identity {'holds' if c1_ok else 'FAILS'} on 3 forms; control fired at this p: {ctrl_fired_this_p}")
report("C1 polarisation identity (15 forms)", c1_ok)
report("C1-ctrl (missing p!) fires for every p>=2", ctrl_fires_all)

# ---------------- C2: omega_hm(1/2) rigorous enclosure ----------------
def atan_bracket(x, nterms):
    """alternating series sum_{k>=0} (-1)^k x^(2k+1)/(2k+1), 0<x<1: consecutive partial sums bracket the value"""
    s_prev = Fr(0)
    s = Fr(0)
    for k in range(nterms):
        s_prev = s
        s += Fr((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
    lo, hi = min(s, s_prev), max(s, s_prev)
    return lo, hi

a5 = atan_bracket(Fr(1, 5), 30)
a239 = atan_bracket(Fr(1, 239), 10)
pi_lo = 16 * a5[0] - 4 * a239[1]
pi_hi = 16 * a5[1] - 4 * a239[0]
assert pi_lo < pi_hi

def omega_enclosure(r, nterms=60):
    A_lo, A_hi = atan_bracket(r, nterms)
    q_lo = 4 * A_lo / pi_hi
    q_hi = 4 * A_hi / pi_lo
    return 1 - q_hi, 1 - q_lo

def dec_out(x, digits, up):
    scale = 10 ** digits
    n = x * scale
    fl = n.numerator // n.denominator
    if up and fl * n.denominator != n.numerator:
        fl += 1
    return f"{Fr(fl, scale).numerator}/{scale}" if False else f"{fl}e-{digits}"

w_lo, w_hi = omega_enclosure(Fr(1, 2))
print(f"  pi in [{dec_out(pi_lo, 12, False)}, {dec_out(pi_hi, 12, True)}] (x1e-12, outward)")
print(f"  omega_hm(1/2) in [{dec_out(w_lo, 9, False)}, {dec_out(w_hi, 9, True)}] (x1e-9, outward)")
c2 = (w_lo >= Fr(4096, 10000)) and (w_hi <= Fr(4098, 10000)) and (w_hi - w_lo < Fr(1, 10 ** 6))
report("C2 omega_hm(1/2) in [0.4096,0.4098], width<1e-6", c2)
report("C2-ctrl (claim omega_hm(1/2)>=1/2 rejected)", w_hi < Fr(1, 2))
for rr in (Fr(1, 4), Fr(1, 10)):
    lo, hi = omega_enclosure(rr)
    print(f"  [info] omega_hm({rr}) in [{dec_out(lo, 9, False)}, {dec_out(hi, 9, True)}] (x1e-9, outward)")

# ---------------- C3: argument identity and monotonicity ----------------
us = [Fr(1, 7), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(1), Fr(3, 2), Fr(2), Fr(3), Fr(7)]
c3 = True
ctrl3_fired = False
for r in (Fr(1, 2), Fr(1, 4), Fr(1, 10)):
    best = None
    best_u = None
    for u in us:
        c = (1 - u * u) / (1 + u * u)
        s = 2 * u / (1 + u * u)
        assert c * c + s * s == 1
        tr, ti = r * c, r * s                     # tau = tr + i ti
        nr, ni = 1 + tr, ti                       # numerator 1 + tau
        dr, di = 1 - tr, -ti                      # denominator 1 - tau
        den = dr * dr + di * di                   # |1 - tau|^2
        wr = (nr * dr + ni * di) / den            # Re((1+tau)/(1-tau))
        wi = (ni * dr - nr * di) / den            # Im(...)
        a_ok = (wr == (1 - r * r) / den) and (wi == 2 * r * s / den)
        b_ok = wr > 0
        if not (a_ok and b_ok):
            c3 = False
            print(f"  C3 fail r={r} u={u}: wr={wr} wi={wi}")
        ratio = wi / wr
        if ratio != 2 * r * s / (1 + r * r):
            ctrl3_fired = True
        if best is None or ratio > best:
            best, best_u = ratio, u
    c_ok = (best_u == 1) and (best == 2 * r / (1 - r * r))
    if not c_ok:
        c3 = False
    print(f"  C3 r={r}: max Im/Re over samples at u={best_u}, value {best} (=2r/(1-r^2): {best == 2*r/(1-r*r)})")
report("C3 argument identity, Re>0, max at theta=pi/2 (27 samples)", c3)
report("C3-ctrl (wrong 2r sin/(1+r^2) rejected)", ctrl3_fired)

print("VERDICT:", "PASS" if ok_all else "FAIL")
