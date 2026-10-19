"""C4d-05: EXACT range-1 pair-sector theorem (certificate by single-term deduction).

Unknowns: all amplitudes W[sigma, p] of a G-covariant, translation-invariant pair walk at range 1
(p near pair, sigma near pair in box(p); far pairs fixed, phase convention W=1 there).
Constraints (all exact consequences of: U(1), frozen singles, range 1, unitarity; see NOTE):
  (U)  <W p1 | W p2> = 0 for p1 != p2;
  (S)  <W p1 (x) w1 | W p2 (x) w2> = 0 for valid spectator triples (p_i, w_i) [U isometric];
  (Sd) the same with W^dagger [U^dagger isometric, spectator lemma for alpha^-1].
Deduction rule: if, after inserting the zeros already proved, a constraint reduces to
m |x_k|^2 = 0 (m>0 integer), then x_k = 0.
Every deduction is re-verified by an INDEPENDENT implementation (own orbit-keying of amplitudes,
own enumeration of W|p>, own spectator-validity test), which recomputes the witness overlap as a
polynomial in the unknowns and confirms it reduces to m|x_k|^2.
Usage: python3 c4d_05_range1_exact.py [T|O|C1]"""
import sys, itertools, time
from c4d_common import check, total, T, O, cheb, pair, near_rhos, add, sub, rot, ball
import numpy as np
from c4d_quantum import PairWalkSpace, build_constraints
from c4d_solver import moving_mask

gname = sys.argv[1] if len(sys.argv) > 1 else "T"
G = {"T": T, "O": O, "C1": [np.eye(3, dtype=int)]}[gname]
r = 1
t0 = time.time()
S = PairWalkSpace(G, r)
unit, spec = build_constraints(S)
print(f"[{gname}] nvar={S.nvar}  build {time.time()-t0:.1f}s", flush=True)
mv, mult = moving_mask(S)

# ---- deduction with witnesses (builder side) ----
cons = []
for c, t in unit:
    if c == 0:
        cons.append(("U", t))
for kind in ("W", "Wd"):
    for t in spec[kind]:
        cons.append((kind, [(i, j) for _, i, j in t]))
# keep the geometric witness keys: rebuild spectator keys (cheap second pass) for printing/verification
zero, order = set(), []
changed = True
while changed:
    changed = False
    for ci, (kind, t) in enumerate(cons):
        live = [(i, j) for i, j in t if i not in zero and j not in zero]
        if live and all(a == b == live[0][0] for a, b in live):
            k = live[0][0]
            zero.add(k); order.append((k, ci)); changed = True
rest = [k for k in range(S.nvar) if k not in zero]
stay = [k for k, (rho0, s, m) in enumerate(S.var_info) if s == pair((0, 0, 0), rho0)]
print(f"[{gname}] deduced zeros: {len(zero)}; surviving unknowns: {rest}; stay unknowns: {stay}", flush=True)
check(f"[{gname}] every non-stay amplitude is forced to zero (W diagonal)", sorted(rest) == sorted(stay))

# ---- independent re-verification of every deduction ----
# own keying: orbit of (sigma, p) under G x Z^3
def key(sig, p):
    best = None
    for R in G:
        pp = [tuple(int(v) for v in R @ np.array(a)) for a in p]
        ss = [tuple(int(v) for v in R @ np.array(a)) for a in sig]
        m = min(pp)
        k = (tuple(sorted(sub(a, m) for a in pp)), tuple(sorted(sub(a, m) for a in ss)))
        if best is None or k < best:
            best = k
    return best


def near(p):
    a, b = tuple(p)
    return cheb(a, b) <= r


def col(p):
    """own enumeration of W|p> support: near pairs sigma, both sites within r of both sites of p."""
    a, b = tuple(p)
    sites = [s for s in itertools.product(*[range(min(a[i], b[i]) - r, max(a[i], b[i]) + r + 1) for i in range(3)])
             if cheb(s, a) <= r and cheb(s, b) <= r]
    out = []
    for u, v in itertools.combinations(sites, 2):
        if cheb(u, v) <= r:
            out.append(frozenset((u, v)))
    return out


def amp_vec(p, adj):
    """dict sigma -> (key, conj_flag) symbolic amplitude of W|p> or W^dag|p>."""
    if not near(p):
        return {p: None}  # exact 1
    out = {}
    if not adj:
        for s in col(p):
            out[s] = (key(s, p), False)
    else:
        for s in col(p):  # W^dag[s,p] = conj(W[p,s]); p in box(s) <=> s in box(p) at range r
            out[s] = (key(p, s), True)
    return out


def overlap_poly(v1, v2):
    """<v1|v2> as dict {(k1,k2): count} meaning sum count*conj(x_k1) x_k2 (k1/k2 may be 'one')."""
    poly = {}
    for s, a1 in v1.items():
        if s not in v2:
            continue
        a2 = v2[s]
        # conj(a1) * a2 ; a = (key, conjflag) -> value x_key or conj(x_key)
        def lit(a, outer_conj):
            if a is None:
                return ("one",)
            k, cf = a
            return (k, cf ^ outer_conj)
        l1, l2 = lit(a1, True), lit(a2, False)
        # normalise to (conj literal, plain literal) form if possible
        term = tuple(sorted([l1, l2], key=str))
        poly[term] = poly.get(term, 0) + 1
    return poly


def spectator_valid(p, w):
    return w not in p and all(cheb(w, a) > r for a in p)


def with_spec(v, w):
    return {s | {w}: a for s, a in v.items()}


# rebuild witnesses in geometric form for verification
def geometric_constraints():
    geo = []
    for c, t in unit:
        pass
    return geo

# For verification we re-derive, for each deduction, a geometric witness by searching the
# independent enumeration for a constraint that reduces to m|x_k|^2 given the zeros proved before it.
zero_keys = set()
ver_ok = True
key_of_var = {k: key(S.var_info[k][1], pair((0, 0, 0), S.var_info[k][0])) for k in range(S.nvar)}
check(f"[{gname}] independent keying is consistent with the builder's unknowns (bijection)",
      len(set(key_of_var.values())) == S.nvar)


def reduces_to_single(poly, zk):
    live = {}
    for term, cnt in poly.items():
        ks = [l[0] for l in term if l[0] != "one"]
        if any(k in zk for k in ks):
            continue
        if any(l[0] == "one" for l in term):
            return None
        live[term] = cnt
    if len(live) != 1:
        return None
    (term, cnt), = live.items()
    (k1, f1), (k2, f2) = term
    if k1 == k2 and f1 != f2 and cnt > 0:
        return k1
    return None


# geometric witnesses of the builder's deductions, re-evaluated independently
keys = build_constraints.keys
geo = []
for (c, t), kk in zip(unit, keys["U"]):
    if c == 0:
        geo.append(("U",) + kk)
for kind in ("W", "Wd"):
    for kk in keys[kind]:
        geo.append((kind,) + kk)
assert len(geo) == len(cons)
proved, nbad = set(), 0
for k, ci in order:
    wit = geo[ci]
    if wit[0] == "U":
        _, p1, p2 = wit
        ok_geom = near(p1) and near(p2) and p1 != p2
        poly = overlap_poly(amp_vec(p1, False), amp_vec(p2, False))
    else:
        kind, p1, w1, p2, w2 = wit
        adj = kind == "Wd"
        ok_geom = spectator_valid(p1, w1) and spectator_valid(p2, w2) and (p1 | {w1}) != (p2 | {w2})
        poly = overlap_poly(with_spec(amp_vec(p1, adj), w1), with_spec(amp_vec(p2, adj), w2))
    kk = reduces_to_single(poly, proved)
    if not (ok_geom and kk == key_of_var[k]):
        nbad += 1
    else:
        proved.add(kk)
check(f"[{gname}] every deduction re-verified by the independent evaluation of its witness", nbad == 0,
      f"{len(order)} deductions, {nbad} not reproduced")
stay_keys = {key_of_var[k] for k in stay}
check(f"[{gname}] independent route: all amplitudes except the 'stay' ones vanish",
      proved == set(key_of_var.values()) - stay_keys)
for k, ci in order[:4]:
    w = geo[ci]
    print("   e.g. zero of", key_of_var[k], "from", w[0], [sorted(z) if isinstance(z, frozenset) else z for z in w[1:]])
# diagonal W with arbitrary phases solves every constraint (consistency of the conclusion)
rng = np.random.default_rng(3)
x = np.zeros(S.nvar, complex)
for k in stay:
    x[k] = np.exp(1j * rng.uniform(0, 6.28))
from c4d_solver import compile_system, make_fun
fun, _ = make_fun(compile_system(S, unit, spec))
check(f"[{gname}] diagonal W with random phases satisfies all constraints",
      np.max(np.abs(fun(np.concatenate([x.real, x.imag])))) < 1e-12)
total()
