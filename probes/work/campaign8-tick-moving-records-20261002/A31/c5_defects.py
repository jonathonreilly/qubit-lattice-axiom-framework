"""A31 c5: can a single defect of A20's two covariant calm stabilizer vacua move at all?

Star state: S_x = prod_a s^a_{x+e_a} s^a_{x-e_a} = +1 for all x.  Face state: F_x = prod over the 12
face-diagonal neighbours x+d of s^{perp(d)}_{x+d} = +1.  A Pauli s^b_y flips the stars/faces it
anticommutes with. Over F2, local operators create exactly the span of single-site flip patterns.
A single defect moves by v iff the two-defect pattern {x, x+v} lies in that span (on a 6^3 torus).
"""
import signal, itertools, numpy as np
signal.alarm(55)
L = 6
sites = list(itertools.product(range(L), repeat=3)); idx = {s:i for i,s in enumerate(sites)}; N = len(sites)
E = [np.array(e) for e in [(1,0,0),(0,1,0),(0,0,1)]]
def sh(s, v): return tuple(int((s[i]+v[i]) % L) for i in range(3))
def star_pattern(y, b):
    out = set()
    for a in range(3):
        if a == b: continue
        for sg in (1,-1): out.add(idx[sh(y, sg*E[a])])
    return out
def face_pattern(y, b):
    out = set()
    for a in range(3):
        if a == b: continue
        for s1 in (1,-1):
            for s2 in (1,-1):
                d = s1*E[b] + s2*E[a]; out.add(idx[sh(y, -d)])
    return out
def span_basis(cols):
    # Gaussian elimination over F2 on bit-packed rows (python ints); returns pivot dict
    piv = {}
    for c in cols:
        v = 0
        for i in c: v ^= (1 << i)
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    return piv
def in_span(piv, pattern):
    v = 0
    for i in pattern: v ^= (1 << i)
    while v:
        h = v.bit_length() - 1
        if h not in piv: return False
        v ^= piv[h]
    return True
cands = {'e_x': (1,0,0), '2e_x': (2,0,0), 'e_x+e_y': (1,1,0), '2e_x+2e_y': (2,2,0), 'e_x+e_y+e_z': (1,1,1),
         '2(e_x+e_y+e_z)': (2,2,2), 'e_x+2e_y': (1,2,0), '3e_x': (3,0,0)}
for name, pat in [('star', star_pattern), ('face', face_pattern)]:
    cols = [pat(y, b) for y in sites for b in range(3)]
    piv = span_basis(cols)
    print(f"{name} state on {L}^3: rank of flip patterns {len(piv)} of {N}; weights of single-site patterns {sorted(set(len(c) for c in cols))}")
    origin = idx[(0,0,0)]
    res = {k: in_span(piv, {origin, idx[sh((0,0,0), v)]}) for k, v in cands.items()}
    print("   two-defect pattern {x, x+v} creatable by a local operator (single defect hops by v):",
          "; ".join(f"{k}: {'yes' if r else 'no'}" for k, r in res.items()))
    single = in_span(piv, {origin})
    print(f"   single defect creatable alone: {'yes' if single else 'no'}")
# all displacements on the 6^3 torus, and the rank deficit (stabilizer dependencies) versus size
for name, pat in [('star', star_pattern), ('face', face_pattern)]:
    cols = [pat(y, b) for y in sites for b in range(3)]
    piv = span_basis(cols); origin = idx[(0,0,0)]
    mob = [s for s in sites if s != (0,0,0) and in_span(piv, {origin, idx[s]})]
    print(f"{name}: displacements v (of {N-1}) for which a lone defect can be moved by ANY Pauli operator: {len(mob)}")
for Ls in (4, 6, 8):
    L = Ls; sites = list(itertools.product(range(L), repeat=3)); idx = {s:i for i,s in enumerate(sites)}; N = len(sites)
    out = []
    for name, pat in [('star', star_pattern), ('face', face_pattern)]:
        piv = span_basis([pat(y, b) for y in sites for b in range(3)]); out.append(f"{name} N-rank={N-len(piv)}")
    print(f"L={L}: " + ", ".join(out) + "  (growth with L => sub-extensive ground-space degeneracy, fracton-like)")
