# sc55_tel.py -- exact check of the telescoping conditional-covariance identity (SRCCD55 Proposition B).
# Criteria: sc55_tel_criteria.md (written first). Exact rational arithmetic only (fractions.Fraction).
import itertools, random
from fractions import Fraction as Fr

SIZES = (4, 3, 3, 2)          # |S_0|, |S_1|, |S_2|, |S_3|;  K = 3
K = len(SIZES) - 1

def rand_pos(rng):
    return Fr(rng.randint(1, 9))

def normalise(row):
    s = sum(row)
    return [x / s for x in row]

def make_chain(rng, markov=True):
    w0 = [rand_pos(rng) for _ in range(SIZES[0])]
    kern = []
    for i in range(K):
        if markov:
            # K_i(u_{i+1} | u_i): a stochastic matrix indexed [u_i][u_{i+1}]
            kern.append({(ui,): normalise([rand_pos(rng) for _ in range(SIZES[i + 1])])
                         for ui in range(SIZES[i])})
        else:
            # non-Markov: K_i depends on (u_i, u_{i-1}, ..., u_0)
            kern.append({hist: normalise([rand_pos(rng) for _ in range(SIZES[i + 1])])
                         for hist in itertools.product(*[range(SIZES[j]) for j in range(i, -1, -1)])})
    return w0, kern

def joint(w0, kern, markov=True):
    p = {}
    for cfg in itertools.product(*[range(n) for n in SIZES]):
        val = w0[cfg[0]]
        for i in range(K):
            key = (cfg[i],) if markov else tuple(cfg[j] for j in range(i, -1, -1))
            val *= kern[i][key][cfg[i + 1]]
        p[cfg] = val
    Z = sum(p.values())
    return {c: v / Z for c, v in p.items()}

def cond_exp(p, f, given_idx):
    """E[f(cfg) | cfg[j] for j in given_idx] as a dict keyed by the tuple of given values."""
    num, den = {}, {}
    for c, pc in p.items():
        key = tuple(c[j] for j in given_idx)
        num[key] = num.get(key, Fr(0)) + pc * f(c)
        den[key] = den.get(key, Fr(0)) + pc
    return {k: num[k] / den[k] for k in num}

def lhs(p, G, H):
    eG = cond_exp(p, lambda c: G[c[0]], (K,))
    eH = cond_exp(p, lambda c: H[c[0]], (K,))
    eGH = cond_exp(p, lambda c: G[c[0]] * H[c[0]], (K,))
    return {k: eGH[k] - eG[k] * eH[k] for k in eGH}

def rhs(p, G, H, form="markov", drop0=False):
    total = {}
    for i in range(K):
        if drop0 and i == 0:
            continue
        if form == "markov":
            gi_idx = (i,)
        else:  # tail sigma-algebra U_i, ..., U_K
            gi_idx = tuple(range(i, K + 1))
        Gi = cond_exp(p, lambda c: G[c[0]], gi_idx)
        Hi = cond_exp(p, lambda c: H[c[0]], gi_idx)
        gi = lambda c: Gi[tuple(c[j] for j in gi_idx)]
        hi = lambda c: Hi[tuple(c[j] for j in gi_idx)]
        nxt_idx = (i + 1,) if form == "markov" else tuple(range(i + 1, K + 1))
        eg = cond_exp(p, gi, nxt_idx)
        eh = cond_exp(p, hi, nxt_idx)
        egh = cond_exp(p, lambda c: gi(c) * hi(c), nxt_idx)
        covfn = lambda c: egh[tuple(c[j] for j in nxt_idx)] - eg[tuple(c[j] for j in nxt_idx)] * eh[tuple(c[j] for j in nxt_idx)]
        term = cond_exp(p, covfn, (K,))
        for k, v in term.items():
            total[k] = total.get(k, Fr(0)) + v
    return total

def markov_property_holds(p, G):
    for i in range(1, K + 1):
        a = cond_exp(p, lambda c: G[c[0]], tuple(range(i, K + 1)))
        b = cond_exp(p, lambda c: G[c[0]], (i,))
        for key, val in a.items():
            if val != b[(key[0],)]:
                return False
    return True

rng = random.Random(20261029)
T1 = T2 = True; T1_count = 0; C2_fired = False
for t in range(25):
    w0, kern = make_chain(rng, markov=True)
    p = joint(w0, kern, markov=True)
    G = [Fr(rng.randint(-9, 9)) for _ in range(SIZES[0])]
    H = [Fr(rng.randint(-9, 9)) for _ in range(SIZES[0])]
    L = lhs(p, G, H); R = rhs(p, G, H, "markov")
    for k in L:
        if L[k] == R[k]:
            T1_count += 1
        else:
            T1 = False
    if not markov_property_holds(p, G):
        T2 = False
    R0 = rhs(p, G, H, "markov", drop0=True)
    if any(L[k] != R0[k] for k in L):
        C2_fired = True

C1_fired = False; C1b = True; C1b_count = 0
for t in range(25):
    w0, kern = make_chain(rng, markov=False)
    p = joint(w0, kern, markov=False)
    G = [Fr(rng.randint(-9, 9)) for _ in range(SIZES[0])]
    H = [Fr(rng.randint(-9, 9)) for _ in range(SIZES[0])]
    L = lhs(p, G, H)
    Rm = rhs(p, G, H, "markov")
    Rt = rhs(p, G, H, "tail")
    if any(L[k] != Rm[k] for k in L):
        C1_fired = True
    for k in L:
        if L[k] == Rt[k]:
            C1b_count += 1
        else:
            C1b = False

print("T1 identity (Markov chains): exact equalities %d / 50 -> %s" % (T1_count, "PASS" if T1 and T1_count == 50 else "FAIL"))
print("T2 Markov property E[G|U_i..U_K] = E[G|U_i]: %s" % ("PASS" if T2 else "FAIL"))
print("C1 control (non-Markov chains, Markov-form RHS must differ somewhere): %s" % ("FIRED" if C1_fired else "DID NOT FIRE"))
print("C1b general tail-sigma-algebra form in non-Markov chains: exact equalities %d / 50 -> %s" % (C1b_count, "HOLDS" if C1b and C1b_count == 50 else "FAILS"))
print("C2 control (drop i=0 term must break identity somewhere): %s" % ("FIRED" if C2_fired else "DID NOT FIRE"))
ok = T1 and T1_count == 50 and T2 and C1_fired and C1b and C1b_count == 50 and C2_fired
print("VERDICT:", "PASS" if ok else "FAIL")
