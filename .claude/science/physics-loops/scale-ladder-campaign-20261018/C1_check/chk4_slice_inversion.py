#!/usr/bin/env python3
"""C1 check, extras:
 L1  slice bookkeeping (free-fermion, exact given integer slice invariants): for each rotation-invariant node subset S, can
     an integer slice invariant nu_z(k_z) (gap at the node quasi-energy on slices k_z != node planes) with jumps chi at the
     node planes be compatible with an axis-C2 perpendicular to z (orientation-reversing on the slice: nu -> -nu, affine
     k_z -> -k_z + theta_z)?  Only subsets with zero jumps everywhere pass.
 L2  lift-(in)dependence: rephasing a lift by c(g) with c^2 = A2 swaps the labels A1 <-> A2 for BOTH chi and det, so the
     rule "allowed iff chi|G_K = det_K" is lift-independent while the label "det = A2" is a convention of the real lift.
 I1  O_h channels (improper lifts included, characters base x parity): A2g/A2u allow the singlet at all eight with
     |m_K| = |m_-K|; A1g/A1u forbid it at all eight.
"""
from cklib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(9)
chi = {}
for n, K in NODES.items():
    a, B = weyl_B(K, node_doublet(n)); chi[n] = int(np.sign(np.linalg.det(B)))
orbits = {'k*': [(0, 0, 0)], '-k*': [(1, 1, 1)], 'A': [n for n in DOUB if sum(n) == 1], 'B': [n for n in DOUB if sum(n) == 2]}
c2x = find_el(np.diag([1, -1, -1])); thz = (gk(c2x, np.zeros(3)))[2]
print(f"   C2x affine shift theta_z = {thz/np.pi:.0f} pi")
def slice_ok(S, axis=2, c2=c2x):
    planes = {}
    for n in S:
        z = round(float(wrap(NODES[n][axis])) / (np.pi / 2)); planes[z] = planes.get(z, 0) + chi[n]
    # intervals: I0 = (-pi/2, pi/2), I1 = (pi/2, 3pi/2); nu(I0) = a, nu(I1) = a - J where J = jump at +pi/2 (= -jump at -pi/2 if consistent)
    J = planes.get(1, 0); Jm = planes.get(-1, 0)
    if J + Jm != 0: return False, planes      # net chirality on the slice family must vanish for a periodic nu
    th = round(float(wrap(gk(c2, np.zeros(3))[axis])) / np.pi) % 2
    for a in range(-5, 6):
        nu0, nu1 = a, a - J
        if th == 0 and nu0 == -nu0 and nu1 == -nu1: return True, planes
        if th == 1 and nu1 == -nu0: return True, planes
    return False, planes
res = {}
for r in range(5):
    for combo in itertools.combinations(orbits, r):
        S = [n for o in combo for n in orbits[o]]
        ok, planes = slice_ok(S); res['+'.join(combo) or 'empty'] = ok
        print(f"   {('+'.join(combo) or 'empty'):14s} jumps at k_z=+-pi/2: {planes}  C2x-compatible integer nu: {ok}")
check("L1 with an axis C2 (orientation-reversing on slices) the configurations '{+-k*} only' and 'doublers only' admit NO integer slice "
      "invariant; 'all eight' (and 'empty') do: a free-fermion, Floquet-compatible (given slice invariants) version of the dipole "
      "obstruction, using only C2x", not res['k*+-k*'] and not res['A+B'] and res['k*+-k*+A+B'] and res['empty'])

# ---------------- L2 ----------------
cph = {g: (1j if A2[g] == -1 else 1.0) for g in PROPER}                  # c(g)^2 = A2(g)
Up = {g: cph[g] * UF[g] for g in PROPER}
okc = all(np.allclose(Up[g] @ W(k) @ Up[g].conj().T, W(gk(g, k))) for g in PROPER for k in rng.uniform(-np.pi, np.pi, (2, 3)))
D = node_doublet((0, 0, 0)); st = stab(NODES[(1, 0, 0)]); Dd = node_doublet((1, 0, 0))
det_new = all(abs(np.linalg.det(D.conj().T @ Up[g] @ D) - 1) < 1e-9 for g in PROPER) and \
          all(abs(np.linalg.det(Dd.conj().T @ Up[g] @ Dd) - 1) < 1e-9 for g in st)
# the A2 (old-lift) channel is the A1 channel of the new lift: U' A U'^T = c^2 U A U^T = A2 * A2 * A = A
VA2 = onsite_channel(A2)
ch_new = all(np.allclose(Up[g] @ X @ Up[g].T, X) for g in PROPER for X in VA2)
check("L2 rephased lifts U'_g = c(g) U_g (c^2 = A2) are equally symmetries of the step; with them det = A1 at +-k* and the doublers and the "
      "old A2 channel is the new A1 channel: the all-or-nothing rule is lift-independent, the labels A1/A2 (and 'undressed') are lift conventions",
      okc and det_new and ch_new)

# ---------------- I1: O_h ----------------
IMP = list(range(24, 48))
def proper_part(g): return find_el(-OH[g]) if g >= 24 else g
okall = True; info = []
DQ = {n: node_doublet(n) for n in NODES}
neg_node = {n: tuple((1 - x) % 2 for x in n) for n in NODES}
for base in ('A1', 'A2'):
    for par in ('g', 'u'):
        chiO = {g: (A2[proper_part(g)] if base == 'A2' else 1) * (1 if (g < 24 or par == 'g') else -1) for g in range(48)}
        V = onsite_channel(chiO, idx=list(range(48)))
        if not V: info.append(f"{base}{par}: dim 0"); continue
        A = sum((rng.normal() + 1j * rng.normal()) * X for X in V)
        m = {n: abs(singlet(DQ[n], 2 * A)) for n in NODES}
        eq = all(abs(m[n] - m[neg_node[n]]) < 1e-9 for n in NODES)
        if base == 'A2': okall &= min(m.values()) > 1e-4 and eq
        else: okall &= max(m.values()) < 1e-11
        info.append(f"{base}{par}: dim {len(V)}, |m| in [{min(m.values()):.1e}, {max(m.values()):.1e}], |m_K|=|m_-K| {eq}")
print("   O_h channels:", "; ".join(info))
inv = find_el(-np.eye(3, dtype=int)); print(f"   inversion affine shift: {gk(inv, np.zeros(3))/np.pi} pi (maps K -> -K)")
check("I1 O_h channels: A2g/A2u allow the singlet at all eight with |m_K| = |m_-K|; A1g/A1u forbid it at all eight (or are empty)", okall)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
