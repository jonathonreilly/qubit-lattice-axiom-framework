"""Part 3 exact case analysis.  The unitarity equations (from part3_exact_eqs.py) are polynomial in
c_j and cb_j = conj(c_j).  Any equation that is a single monomial  c_i * cb_j = 0  forces c_i = 0 or
c_j = 0 (cb_j = 0 iff c_j = 0).  We branch recursively on such equations, substituting zeros, until no
monomial equation remains.  Also: an equation  sum_j w_j |c_j|^2 = 0  with all w_j of one sign forces
all those c_j = 0.  Leaves are printed with their surviving variables and remaining equations.
EXACT (symbolic)."""
import sympy as sp, pickle, sys
ci = int(sys.argv[1]) if len(sys.argv) > 1 else 3
dat = pickle.load(open(f"nn_eqs_class{ci}.pkl", "rb"))
names = dat["names"]; nv = len(names)
c = sp.symbols("c0:%d" % nv); cb = sp.symbols("cb0:%d" % nv)
eqs0 = [sp.sympify(e, locals={**{str(x): x for x in c}, **{str(x): x for x in cb}}) for e in dat["eqs"]]

def simplify_sys(zero):
    sub = {c[i]: 0 for i in zero}; sub.update({cb[i]: 0 for i in zero})
    out = set()
    for e in eqs0:
        e2 = sp.expand(e.subs(sub))
        if e2 != 0:
            out.add(e2)
    return out

def forced_zero(e):
    """return list of variable indices forced zero by e, or None; and 'inconsistent' flag"""
    terms = sp.Add.make_args(e)
    # constant nonzero alone -> inconsistent
    if all(t.is_number for t in terms):
        return "INCONSISTENT"
    if len(terms) == 1:
        t = terms[0]
        idxs = []
        for s in t.free_symbols:
            nm = str(s); idxs.append(int(nm[2:]) if nm.startswith("cb") else int(nm[1:]))
        return ("BRANCH", sorted(set(idxs)))
    # sign-definite sum of |c_j|^2 (possibly with constant of the same sign)
    ws = {}
    const = 0
    for t in terms:
        if t.is_number:
            const += t; continue
        co, rest = t.as_coeff_Mul()
        fs = sorted(map(str, rest.free_symbols))
        if len(fs) == 2 and fs[0].startswith("c") and fs[1].startswith("cb") and fs[0][1:] == fs[1][2:] and sp.degree(rest, rest.free_symbols.pop()) == 1:
            ws[int(fs[0][1:])] = co
        else:
            return None
    vals = list(ws.values())
    if all(w > 0 for w in vals) and const >= 0 or all(w < 0 for w in vals) and const <= 0:
        if const != 0:
            return "INCONSISTENT"
        return ("ALLZERO", sorted(ws))
    return None

leaves = []
def recurse(zero, depth=0):
    while True:
        S = simplify_sys(zero)
        changed = False
        branch = None
        for e in sorted(S, key=lambda x: (len(sp.Add.make_args(x)), sp.default_sort_key(x))):
            r = forced_zero(e)
            if r == "INCONSISTENT":
                return
            if r is None: continue
            if r[0] == "ALLZERO":
                zero = zero | set(r[1]); changed = True; break
            if r[0] == "BRANCH":
                if len(r[1]) == 1:
                    zero = zero | set(r[1]); changed = True; break
                branch = r[1]; break
        if changed: continue
        if branch is None:
            key = frozenset(zero)
            if key not in [l[0] for l in leaves]:
                leaves.append((key, S))
            return
        for i in branch:
            recurse(zero | {i}, depth + 1)
        return

recurse(frozenset())
# remove leaves whose zero-set strictly contains another leaf's zero-set? keep all, but report maximal-support ones
print(f"class {ci}: orbit names {names}")
print(f"{len(leaves)} leaves")
for zero, S in sorted(leaves, key=lambda l: len(l[0])):
    alive = [names[i] for i in range(nv) if i not in zero]
    print(f"\nleaf: nonzero-allowed orbits {alive}  ({len(S)} remaining equations)")
    for e in sorted(S, key=sp.default_sort_key):
        print("     ", e)
pickle.dump([(sorted(z), [str(e) for e in S]) for z, S in leaves], open(f"nn_leaves_class{ci}.pkl", "wb"))
