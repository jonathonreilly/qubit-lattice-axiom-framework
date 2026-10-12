"""R2-5 check 1: Lemma T / T' on column (1+0 spatial) laws.

(a) Exhaust every time-reflection-symmetric HARD column law of window range r (r = 3, 4)
    on {0 = blank, 1 = locked}: allowed-window sets closed under reversal.
    Half-line t = 0..T with s_0 = 0 (low-record boundary), free top, uniform weight on
    allowed columns.  For each law record:
      form_bulk : expected number of formation steps (0 -> 1) with t+1 <= T/2
      unform_bulk: expected number of un-formation steps (1 -> 0) with t+1 <= T/2
      rec_mid   : P(record present at t = T/2)
    Lemma T' (finite range, column-local): no law has form_bulk > 0 and unform_bulk == 0.
(b) Positive (soft) symmetric laws: random symmetric 2x2 pair weights + on-site weights.
    The half-line kernel is the Doob h-transform K(a,b) = T(a,b) psi(b) / (lam psi(a));
    check detailed balance pi(a)K(a,b) = pi(b)K(b,a) with pi = psi^2, and that
    K(1->0) = 0 forces K(0->1) = 0.
Exact rational arithmetic for (a) via Fractions on counts (integers).
"""
import itertools
from fractions import Fraction
import numpy as np

def windows(r):
    return list(itertools.product((0, 1), repeat=r))

def reversal_classes(r):
    seen, classes = set(), []
    for w in windows(r):
        if w in seen:
            continue
        rw = tuple(reversed(w))
        cls = tuple(sorted({w, rw}))
        seen.update(cls)
        classes.append(cls)
    return classes

def analyse(allowed, r, T):
    # states: last (r-1) symbols; boundary: s_0 = 0 and we pad the past with 0 (blank past)
    # so the first windows are (0,...,0,s_1,...).  Pre-boundary blanks are part of the boundary.
    allowed = set(allowed)
    k = r - 1
    states = list(itertools.product((0, 1), repeat=k))
    idx = {s: i for i, s in enumerate(states)}
    n = len(states)
    # forward counts: number of allowed prefixes ending in state s at time t
    fwd = [dict() for _ in range(T + 1)]
    fwd[0] = {tuple([0] * k): 1}
    for t in range(1, T + 1):
        nxt = {}
        for s, c in fwd[t - 1].items():
            for b in (0, 1):
                w = s + (b,)
                if w in allowed:
                    ns = w[1:]
                    nxt[ns] = nxt.get(ns, 0) + c
        fwd[t] = nxt
    # backward counts: number of allowed completions from state s at time t to T (free top)
    bwd = [dict() for _ in range(T + 1)]
    bwd[T] = {s: 1 for s in states}
    for t in range(T - 1, -1, -1):
        cur = {}
        for s in states:
            tot = 0
            for b in (0, 1):
                w = s + (b,)
                if w in allowed:
                    tot += bwd[t + 1].get(w[1:], 0)
            cur[s] = tot
        bwd[t] = cur
    Z = sum(c * bwd[0].get(s, 0) for s, c in fwd[0].items())
    if Z == 0:
        return None
    half = T // 2
    form = Fraction(0)
    unform = Fraction(0)
    for t in range(0, half):
        for s, c in fwd[t].items():
            for b in (0, 1):
                w = s + (b,)
                if w in allowed:
                    cnt = c * bwd[t + 1].get(w[1:], 0)
                    if cnt == 0:
                        continue
                    a = s[-1]
                    if a == 0 and b == 1:
                        form += Fraction(cnt, Z)
                    if a == 1 and b == 0:
                        unform += Fraction(cnt, Z)
    recmid = Fraction(sum(c * bwd[half].get(s, 0) for s, c in fwd[half].items() if s[-1] == 1), Z)
    return form, unform, recmid

def part_a():
    out = []
    for r, T in ((3, 40), (4, 40)):
        classes = reversal_classes(r)
        n_specs = 0
        n_form = 0
        n_bad = 0
        strict_ok = []
        for mask in range(1 << len(classes)):
            allowed = set()
            for i, cls in enumerate(classes):
                if mask >> i & 1:
                    allowed.update(cls)
            res = analyse(allowed, r, T)
            if res is None:
                continue
            n_specs += 1
            form, unform, recmid = res
            if form > 0:
                n_form += 1
                if unform == 0:
                    n_bad += 1
                    strict_ok.append(sorted(allowed))
        out.append((r, T, len(classes), n_specs, n_form, n_bad))
        print(f"range r={r}, T={T}: reversal classes={len(classes)}, laws with an allowed column={n_specs}, "
              f"laws with bulk formation (t<=T/2)={n_form}, of which bulk un-formation probability 0: {n_bad}")
        for a in strict_ok[:5]:
            print("   counterexample allowed windows:", a)
    return out

def part_b(trials=2000, seed=1):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(trials):
        A = rng.uniform(0.0, 2.0, size=(2, 2))
        W = (A + A.T) / 2  # symmetric time-bond weight (theta-symmetric)
        h = rng.uniform(0.01, 3.0, size=2)
        D = np.diag(np.sqrt(h))
        Tm = D @ W @ D
        lam, vec = np.linalg.eigh(Tm)
        psi = np.abs(vec[:, -1]); l0 = lam[-1]
        K = Tm * psi[None, :] / (l0 * psi[:, None])
        pi = psi ** 2
        db = np.max(np.abs(pi[:, None] * K - (pi[:, None] * K).T))
        worst = max(worst, db, abs(K.sum(1) - 1).max())
    print(f"(b) soft symmetric 2-state laws, {trials} random draws: max |detailed-balance defect|, |row-sum-1| = {worst:.2e}")
    # zero un-forming forces zero formation
    W = np.array([[1.0, 0.0], [0.0, 1.0]])
    for hb in (0.5, 2.0):
        D = np.diag(np.sqrt([1.0, hb]))
        Tm = D @ W @ D
        lam, vec = np.linalg.eigh(Tm)
        print(f"    W(1,0)=W(0,1)=0, on-site ratio {hb}: transfer matrix is diagonal -> K(0->1) = 0 (no formation); eig = {lam}")

if __name__ == "__main__":
    print("== Lemma T' exhaust (hard, column-local, theta-symmetric) ==")
    part_a()
    print("== Lemma T for soft laws (reversible half-line kernel) ==")
    part_b()
