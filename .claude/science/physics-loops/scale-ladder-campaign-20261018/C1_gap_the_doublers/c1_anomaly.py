#!/usr/bin/env python3
"""C1 part 2: anomaly bookkeeping for the eight Weyl nodes of the eight-node step (number-conserving route).

Exact integer/mod-2 bookkeeping from the computed chiralities (c1lib / first-order degenerate PT):
 A1  rotation orbits of the nodes: {k*}, {-k*}, A = {k*+pi e_i}, B = {-k*+pi e_i}; chiralities (+1, -1, -1 x3, +1 x3).
 A2  translations act on the node doublet at K by the phase e^{-iK.e} (checked on the L = 4 torus); composed with the U(1)
     rotation e^{+i k*.e N} this is the IR "taste" Z2^3: node k* + pi n -> (-1)^{n.e}.
 A3  for every rotation-invariant union S of orbits: net chirality (U(1)^3, U(1)-grav^2), the Weyl dipole
     b_S = sum chi_K K mod 2pi (mixed U(1)-translation / anomalous-Hall vector), and the U(1)^2-Z2^(i) counts
     sum_{n_i odd} chi mod 2.  Only S = all eight (and S = empty) has all of them zero.
 A4  pairing bookkeeping: for Q = 0 every BdG point K carries Weyl charge chi_K - chi_{-K} = +-2 (cannot be gapped by
     any small pairing); for Q = pi p, p in {0,1}^3, the partner of node n is n + p + (1,1,1) and the pair is gappable
     iff the chiralities are equal, i.e. iff |p| is odd; only Q = 0 and Q = R = pi(1,1,1) are rotation invariant.
"""
import itertools
from c1lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

chi = {}
for nm, k in NODES.items():
    a, B = weyl_data(k, level(k, np.pi / 2)); chi[nm] = int(np.sign(np.linalg.det(B)))
nvec = {nm: np.array(NVEC[nm]) for nm in NODES}
# ---- A1 orbits ----
def orbit(nm):
    k = NODES[nm]; out = set()
    for g in ROT:
        im = gk(g, k)
        out |= {m for m, kk in NODES.items() if same_k(im, kk)}
    return frozenset(out)
orbits = sorted({orbit(nm) for nm in NODES}, key=lambda o: (len(o), sorted(o)))
print("orbits:", [sorted(o) for o in orbits])
ok = len(orbits) == 4 and all(len({chi[m] for m in o}) == 1 for o in orbits)
check("A1 four rotation orbits {k*}, {-k*}, A, B with constant chirality on each; chi(k* + pi n) = (-1)^|n| chi(k*)", ok and
      all(chi[nm] == (-1) ** int(nvec[nm].sum()) * chi['k*'] for nm in NODES), str({nm: chi[nm] for nm in NODES}))

# ---- A2 translation action on node states (L = 4 torus, real space) ----
ok = True
for nm, k in NODES.items():
    Qm = level(k, np.pi / 2)
    psi = Bloch(-k) @ Qm[:, 0]     # real-space form of an eigenvector of the chk-convention Bloch matrix at k (blocks use e^{ik.sh})
    for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        Tm = opmat_from(*trans[TV.index(t)])
        ph = np.vdot(psi, Tm @ psi)
        ok &= np.isclose(ph, np.exp(1j * np.dot(k, t))) and np.isclose(ph / np.exp(1j * np.dot(kst, t)), (-1) ** int(nvec[nm] @ np.array(t)))
check("A2 (convention check) unit translations act on each node doublet by e^{iK.e} (chk momentum convention); removing the common "
      "U(1) phase e^{ik*.e} leaves the taste sign (-1)^{n.e}: T_e e^{-ik*.e N} acts in the IR as Z2^3", ok)

# ---- A3 bookkeeping per symmetric subset ----
names = list(NODES)
def book(S):
    S = list(S); nchi = sum(chi[m] for m in S)
    b = sum(chi[m] * NODES[m] for m in S) if S else np.zeros(3)
    bmod = np.round(np.mod(b, 2 * np.pi) / np.pi, 6) % 2
    z2 = tuple(int(sum(chi[m] for m in S if nvec[m][i] % 2 == 1)) % 2 for i in range(3))
    return nchi, bmod, z2
rows = []
for r in range(0, 5):
    for combo in itertools.combinations(range(4), r):
        S = set().union(*[orbits[i] for i in combo]) if combo else set()
        nchi, bmod, z2 = book(S)
        lab = "+".join(sorted('{k*}' if o == {'k*'} else '{-k*}' if o == {'-k*'} else ('A' if 'k*+pi ex' in o else 'B') for o in [orbits[i] for i in combo])) or 'empty'
        rows.append((lab, len(S), nchi, bmod, z2))
print(f"{'subset':16s} {'#':>2s} {'sum chi':>7s}  {'b/pi mod 2':>14s}  U(1)^2-Z2^(x,y,z) mod 2")
for lab, n, nchi, bmod, z2 in rows:
    print(f"{lab:16s} {n:2d} {nchi:7d}  {str(bmod.tolist()):>14s}  {z2}")
free = [lab for lab, n, nchi, bmod, z2 in rows if nchi == 0 and np.allclose(bmod, 0) and z2 == (0, 0, 0)]
check("A3 among rotation-invariant node subsets only 'empty' and 'all eight' have zero net chirality, zero Weyl dipole mod 2pi and zero "
      "U(1)^2-Z2 counts; the six doublers (A+B) and the pair {+-k*} each carry b = pi(1,1,1) mod 2pi (Z2 counts (1,1,1))",
      sorted(free) == sorted(['empty', 'A+B+{-k*}+{k*}']) and
      any(lab == 'A+B' and nchi == 0 and np.allclose(bmod, 1) and z2 == (1, 1, 1) for lab, n, nchi, bmod, z2 in rows) and
      any(lab == '{-k*}+{k*}' and nchi == 0 and np.allclose(bmod, 1) and z2 == (1, 1, 1) for lab, n, nchi, bmod, z2 in rows),
      f"anomaly-free symmetric subsets: {free}")
# representative independence of b for net-chirality-zero sets
S = [m for m in NODES if '+pi' in m]
b1 = sum(chi[m] * NODES[m] for m in S); b2 = sum(chi[m] * (NODES[m] + 2 * np.pi * np.array(rng_v)) for m, rng_v in zip(S, itertools.cycle([(1, 0, 0), (0, -1, 1), (2, 0, 0)])))
check("A3b for a zero-net-chirality set b mod 2pi Z^3 is independent of the momentum representatives (shift test)",
      np.allclose(np.exp(1j * (b1 - b2)), 1))

# ---- A4 pairing bookkeeping ----
bdg_q0 = {nm: chi[nm] - chi[[m for m, kk in NODES.items() if same_k(kk, -NODES[nm])][0]] for nm in NODES}
check("A4a Q = 0 pairing: BdG Weyl charge chi_K - chi_{-K} = +-2 at every node (K and -K have opposite chirality), so no small "
      "Q = 0 pairing gaps any node, doubler or not", all(abs(v) == 2 for v in bdg_q0.values()), str(bdg_q0))
tab = []
ok = True
for p in itertools.product((0, 1), repeat=3):
    p = np.array(p); Q = np.pi * p
    rotinv = all(same_k(g['M'] @ Q, Q) for g in ROT)
    pairs = []
    for nm in NODES:
        partner = [m for m, kk in NODES.items() if same_k(kk, Q - NODES[nm])]
        ok &= len(partner) == 1
        pairs.append(chi[nm] == chi[partner[0]])
    gappable = all(pairs); never = not any(pairs)
    ok &= (gappable if p.sum() % 2 == 1 else never)
    tab.append((p.tolist(), rotinv, 'all pairs equal-chirality (gappable)' if gappable else 'all pairs opposite (protected)'))
for row in tab: print("   Q/pi =", row[0], " rotation-invariant:", row[1], " ", row[2])
check("A4b Q = pi p maps every node to a node; pairs are equal-chirality (gappable) iff |p| odd; rotation-invariant Q: only 0 (protected) "
      "and R = pi(1,1,1) (intra-node, gappable)", ok and [r[0] for r in tab if r[1]] == [[0, 0, 0], [1, 1, 1]])

# ---- A5 which nodes the B7 twisted odd tori see ----
# B7 T5: on an odd-L torus with twist theta = +-k* (psi(w + L n) = e^{i theta.n} psi(w)) the allowed momenta obey L k = theta mod 2pi.
seen = {}
for Lt in (1, 3, 5, 7, 9, 11):
    for tn, th in (('k*', kst), ('-k*', -kst)):
        for sgn in (1, -1):    # both momentum-sign conventions (chk blocks use e^{ik.sh}; real-space Bloch vector is e^{-ik.v})
            seen[(Lt, tn, sgn)] = sorted(nm for nm, k in NODES.items() if same_k(sgn * Lt * k, th))
for kk, v in seen.items(): print(f"   L={kk[0]:2d} theta={kk[1]:3s} sign={kk[2]:+d}: nodes in the twisted momentum set: {v}")
check("A5 on every odd twisted torus of B7 (theta = +-k*) the allowed momenta contain exactly one of +-k* and none of the six doublers: "
      "B7's exact odd-N degeneracy and its conditional LSM are carried by the +-k* doublets, not by the doublers",
      all(len(v) == 1 and v[0] in ('k*', '-k*') for v in seen.values()))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
