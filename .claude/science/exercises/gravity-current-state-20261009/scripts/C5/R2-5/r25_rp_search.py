"""R2-5 check 7: exhaustive search, single-site column laws (transfer matrix T over one site's
values), time reflection theta acting on values, bond-reflection positivity (twisted kernel
M(a', b) = T(theta a', b) symmetric PSD), theta-covariance T(a, b) = T(theta b, theta a).
Question: is there a law and a blank boundary value such that, in the half-line process
(slices reachable from the boundary AND continuable forever), a record forms and no record
ever un-forms?
Alphabets:
  S1 = {blank, rec} theta trivial (scalar record);
  S2 = {blank, U, D} theta: U <-> D (oriented record, the route-P2 label);
  S3 = {b+, b-, r+, r-} theta: + <-> - (scalar record bit with a time-odd companion p).
All 0/1 kernels are enumerated (hard laws); soft laws reduce to these supports.
"""
import itertools
import numpy as np

def search(vals, theta, is_rec):
    n = len(vals)
    idx = list(range(n))
    found = []; n_rp = 0
    for bits in itertools.product((0, 1), repeat=n * n):
        T = np.array(bits, dtype=float).reshape(n, n)
        # theta-covariance
        ok = all(T[a, b] == T[theta[b], theta[a]] for a in idx for b in idx)
        if not ok: continue
        M = np.array([[T[theta[ap], b] for b in idx] for ap in idx])
        if not np.allclose(M, M.T): continue
        if np.linalg.eigvalsh(M).min() < -1e-12: continue
        n_rp += 1
        # continuable set: slices with an infinite forward path (iterate removal of dead ends)
        alive = set(idx)
        changed = True
        while changed:
            changed = False
            for a in list(alive):
                if not any(T[a, b] > 0 and b in alive for b in alive):
                    alive.discard(a); changed = True
        for b0 in [a for a in idx if not is_rec[a]]:
            if b0 not in alive: continue
            reach = {b0}; frontier = [b0]
            while frontier:
                a = frontier.pop()
                for b in alive:
                    if T[a, b] > 0 and b not in reach:
                        reach.add(b); frontier.append(b)
            form = any(T[a, b] > 0 and not is_rec[a] and is_rec[b] for a in reach for b in reach)
            unform = any(T[a, b] > 0 and is_rec[a] and not is_rec[b] for a in reach for b in reach)
            if form and not unform:
                found.append((T.astype(int).tolist(), vals[b0]))
    return n_rp, found

if __name__ == "__main__":
    cases = [
        ("S1 scalar", ["blank", "rec"], [0, 1], [False, True]),
        ("S2 oriented label", ["blank", "U", "D"], [0, 2, 1], [False, True, True]),
        ("S3 scalar bit + time-odd p", ["b+", "b-", "r+", "r-"], [1, 0, 3, 2], [False, False, True, True]),
    ]
    for name, vals, theta, is_rec in cases:
        n_rp, found = search(vals, theta, is_rec)
        print(f"{name}: theta-covariant RP hard laws = {n_rp}; laws with formation and strict permanence = {len(found)}")
        for T, b0 in found[:6]:
            print(f"    example: boundary {b0}, T = {T}")
