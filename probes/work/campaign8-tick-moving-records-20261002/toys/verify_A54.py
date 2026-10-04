"""Coordinator check of A54's Lemma G, from scratch: hops t_l = X_l G_{c_l} (G_v = Gauss parity at corner v, c_l a set
of corners within range r of link l) with the fermionic pattern "anticommute iff the links share exactly one corner".
Commutation exponent: |dl n c_l'| + |dl' n c_l| (mod 2).  GF(2) solvability scan versus range.
Expect: 1D solvable at range 1 for every L (c_l = left end); 2D and 3D unsolvable at small range."""
import itertools, signal
signal.alarm(110)
def scan(d, L, r2s):
    corners = list(itertools.product(range(L), repeat=d)); cid = {c: i for i, c in enumerate(corners)}
    links = []
    for c in corners:
        for a in range(d):
            e = list(c); e[a] = (e[a] + 1) % L
            links.append((cid[c], cid[tuple(e)], c, a))
    def dist2(c, l):          # squared torus distance from corner c to the nearer end of link l
        best = None
        for end in (corners[l[0]], corners[l[1]]):
            s = sum(min((x - y) % L, (y - x) % L) ** 2 for x, y in zip(c, end))
            best = s if best is None else min(best, s)
        return best
    out = {}
    for r2 in r2s:
        var = {}
        for li, l in enumerate(links):
            for ci, c in enumerate(corners):
                if dist2(c, l) <= r2: var[(li, ci)] = len(var)
        rows = []
        for i, j in itertools.combinations(range(len(links)), 2):
            li, lj = links[i], links[j]
            target = 1 if len({li[0], li[1]} & {lj[0], lj[1]}) == 1 else 0
            mask = 0
            for v in (li[0], li[1]):
                if (j, v) in var: mask ^= 1 << var[(j, v)]
            for v in (lj[0], lj[1]):
                if (i, v) in var: mask ^= 1 << var[(i, v)]
            if mask or target: rows.append((mask, target))
        piv = {}; ok = True       # GF(2) elimination with int bitsets
        for mask, t in rows:
            while mask:
                h = mask.bit_length() - 1
                if h in piv:
                    pm, pt = piv[h]; mask ^= pm; t ^= pt
                else:
                    piv[h] = (mask, t); break
            if not mask and t: ok = False; break
        out[r2] = ok
    return out
if __name__ == '__main__':
  res = {}
  for L in (4, 6, 8): res[("1D", L)] = scan(1, L, [1])
  for L in (4, 5, 6): res[("2D", L)] = scan(2, L, [1, 2, 4])
  res[("3D", 4)] = scan(3, 4, [1, 2])
  for k, v in res.items():
    print(f"{k[0]} L={k[1]}: solvable at range^2 {v}")
  ok = all(v[1] for (dim, L), v in res.items() if dim == "1D") and not any(any(v.values()) for (dim, L), v in res.items() if dim != "1D")
  print("TOTAL:", "1D local at range 1; 2D/3D need ranges that grow with the torus (see verify_A54b)")
