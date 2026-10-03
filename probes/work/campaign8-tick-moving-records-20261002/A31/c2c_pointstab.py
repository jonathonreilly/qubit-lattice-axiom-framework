"""A31 c2c: point stabilizers of pi-flux sign patterns (4^3 torus, no periodicity assumed).
(7a) patterns invariant under the face-diagonal half turn about site 0 [(x,y,z)->(y,x,-z)]: can every
     plaquette touching site 0 carry flux pi?  (proof in the report: no)
(7b) bond orbits under all 24 rotations about site 0 (no translations): any pi-flux pattern among the
     orbit-constant patterns?
(7c) under the tetrahedral subgroup T about site 0 (12 rotations): pi-flux patterns exist?"""
import signal, itertools, numpy as np
signal.alarm(55)
exec(open('c2_patterns.py').read().split('# (1) orbits under G_s')[0])
def orbits(group):
    orb = -np.ones(len(bonds), int); k = 0
    for i in range(len(bonds)):
        if orb[i] >= 0: continue
        stack = [i]; orb[i] = k
        while stack:
            j = stack.pop()
            for M,t in group:
                jj = bond_image(M,t,bonds[j])
                if orb[jj] < 0: orb[jj] = k; stack.append(jj)
        k += 1
    return orb, k
# plaquettes touching site 0
s0 = sidx[(0,0,0)]
touch = [p for p in range(len(plaq)) if any(s0 in (sidx[bonds[b][0]], sidx[add(bonds[b][0], E[bonds[b][1]])]) for b in plaq[p])]
C2d = np.array([[0,1,0],[1,0,0],[0,0,-1]])
orbA, kA = orbits([(np.eye(3,dtype=int),(0,0,0)), (C2d,(0,0,0))])
# solve: is there an orbit-constant sign pattern with flux -1 on all plaquettes touching 0 that are mapped to themselves?
selfmapped = []
for p in touch:
    imgs = sorted(bond_image(C2d,(0,0,0),bonds[b]) for b in plaq[p])
    if imgs == sorted(plaq[p]): selfmapped.append(p)
print(f"(7a) plaquettes at site 0 mapped to themselves by the face-diagonal half turn: {len(selfmapped)}; "
      f"their flux for every invariant pattern: ", end="")
vals = set()
for p in selfmapped:
    o = [orbA[b] for b in plaq[p]]
    # each orbit appears an even number of times in the plaquette => product of signs is +1 for every pattern
    from collections import Counter
    vals.add(all(c % 2 == 0 for c in Counter(o).values()))
print("always +1" if vals == {True} else "can be -1")
for name, group in [('O (24)', [(M,(0,0,0)) for M in rots]),
                    ('T (12)', [(M,(0,0,0)) for M in rots if (np.abs(M) == np.abs(M).T).all() == False or np.array_equal(np.abs(M), np.eye(3,dtype=int))])]:
    orb, k = orbits(group)
    cnt = 0
    if k <= 22:
        for signs in itertools.product([1,-1], repeat=k):
            eta = np.array([signs[o] for o in orb])
            if np.all(fluxes(eta) == -1): cnt += 1
        print(f"(7{'b' if name.startswith('O') else 'c'}) group {name}: {len(group)} elements, {k} bond orbits, pi-flux patterns: {cnt}")
    else:
        print(f"    group {name}: {k} orbits (too many to enumerate)")
