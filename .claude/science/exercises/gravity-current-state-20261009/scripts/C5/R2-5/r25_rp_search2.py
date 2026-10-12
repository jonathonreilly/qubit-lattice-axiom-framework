"""R2-5 check 7b: as check 7, enumerating only theta-covariant 0/1 kernels (orbits of
(a, b) -> (theta b, theta a)), and separating
  - boundary-only formation: formation steps only out of the boundary slice at t = 0, and
  - bulk formation: a formation step out of a blank slice that can itself occur at t >= 1
    (it has a predecessor in the reachable, continuable set).
Strict permanence = no un-formation step between reachable continuable slices.
Alphabets add theta-even blanks/records to the time-odd companions of check 7.
"""
import itertools, time
import numpy as np

def run(name, vals, theta, is_rec, need_rp=True):
    n = len(vals); idx = range(n)
    pairs = [(a, b) for a in idx for b in idx]
    seen = set(); orbits = []
    for (a, b) in pairs:
        if (a, b) in seen: continue
        o = {(a, b), (theta[b], theta[a])}
        seen |= o; orbits.append(sorted(o))
    cnt = 0; n_rp = 0; boundary_only = 0; bulk = 0; ex_bulk = None; ex_b = None
    t0 = time.time()
    for bits in itertools.product((0, 1), repeat=len(orbits)):
        T = np.zeros((n, n))
        for bit, o in zip(bits, orbits):
            if bit:
                for (a, b) in o: T[a, b] = 1.0
        if need_rp:
            M = T[theta, :]          # M[a', b] = T[theta a', b]
            if not np.allclose(M, M.T): continue
            if np.linalg.eigvalsh(M).min() < -1e-12: continue
        n_rp += 1
        alive = set(idx); changed = True
        while changed:
            changed = False
            for a in list(alive):
                if not any(T[a, b] > 0 for b in alive):
                    alive.discard(a); changed = True
        for b0 in [a for a in idx if not is_rec[a] and a in alive]:
            reach = {b0}; fr = [b0]
            while fr:
                a = fr.pop()
                for b in alive:
                    if T[a, b] > 0 and b not in reach: reach.add(b); fr.append(b)
            unform = any(T[a, b] > 0 and is_rec[a] and not is_rec[b] for a in reach for b in reach)
            if unform: continue
            form_steps = [(a, b) for a in reach for b in reach if T[a, b] > 0 and not is_rec[a] and is_rec[b]]
            if not form_steps: continue
            # can the source blank slice occur at t >= 1?
            occurs_later = lambda a: any(T[c, a] > 0 for c in reach)
            if any(occurs_later(a) for (a, b) in form_steps):
                bulk += 1; ex_bulk = ex_bulk or (T.astype(int).tolist(), vals[b0])
            else:
                boundary_only += 1; ex_b = ex_b or (T.astype(int).tolist(), vals[b0])
    print(f"{name}: orbits={len(orbits)}, {'RP ' if need_rp else ''}laws={n_rp}; (law, boundary) pairs with strict permanence and "
          f"boundary-only formation={boundary_only}, with BULK (ongoing) formation={bulk}  [{time.time()-t0:.1f}s]")
    if ex_bulk: print("    bulk example:", ex_bulk)
    if ex_b and not ex_bulk: print("    boundary-only example:", ex_b)

if __name__ == "__main__":
    run("S1 {b, r} theta trivial", ["b", "r"], [0, 1], [False, True])
    run("S2 {b, U, D}", ["b", "U", "D"], [0, 2, 1], [False, True, True])
    run("S3 {b+, b-, r+, r-}", ["b+", "b-", "r+", "r-"], [1, 0, 3, 2], [False, False, True, True])
    run("S4 {b0, b+, b-, r+, r-}", ["b0", "b+", "b-", "r+", "r-"], [0, 2, 1, 4, 3], [False, False, False, True, True])
    run("S5 {b0, r0, U, D}", ["b0", "r0", "U", "D"], [0, 1, 3, 2], [False, True, True, True])
    run("S6 {b0, r0, b+, b-, r+, r-}", ["b0", "r0", "b+", "b-", "r+", "r-"], [0, 1, 3, 2, 5, 4], [False, True, False, False, True, True])
    print("-- without reflection positivity (theta-covariance only), for comparison --")
    run("S2 {b, U, D} no RP", ["b", "U", "D"], [0, 2, 1], [False, True, True], need_rp=False)
    run("S4 {b0, b+, b-, r+, r-} no RP", ["b0", "b+", "b-", "r+", "r-"], [0, 2, 1, 4, 3], [False, False, False, True, True], need_rp=False)
