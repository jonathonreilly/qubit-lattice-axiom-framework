"""A48 Q2: lemma F under the looser reading (one qubit per place).

Claim (EXACT, proof in report): for every looser action whose group law holds on the turns about
the charge's vertex v, and every hop set in lemma F's class covariant under it,
  theta(d, -d, e) = s(t_d, C t_d) = product over places x on the e-axis of s(A_x, M_x A_x),
with M_x = C2 action at x.  Swapped pairs always give +1.  A fixed place gives -1 only when M_x is a
half-turn about an axis at 45 deg to the Pauli A_x.  The quarter turn N_x (N_x^2 = M_x) then maps
A_x off the Pauli axes, and so does the 120-deg turn at v; the half-turn about d pairs the other
fixed places so their signs cancel.

Checks:
 (a) fixed-place lemma: all 24 Clifford N with N^4 = 1; rational-axis non-Clifford N with
     N^4 in {1, half-turn}; control: involutions M alone (C2 only) DO give -1.
 (b) vertex-qubit census for every homomorphism rho_v: Gamma -> Clifford rotations, Gamma in
     {O, T, D2, {1,C2z}}, with A45's link decorations and Gauss-parity switching.
 (c) far-place census: places v +- 2e_a (vertex places on the axes), induced looser actions,
     for Gamma = O and T; control Gamma = {1, C2z}.
 (d) dense 7-qubit Levin-Wen junction phases: random looser O-actions (all four classes, random
     Clifford frames) with covariant dressings; control: the D2 escape found in (b).
"""
import itertools, signal
import numpy as np
from collections import Counter
from a48lib import *
import a48lib
PT = [[a48lib.ptype(k, t) for t in range(4)] for k in range(24)]
def ptype(k, t):
    return PT[k][t]

signal.alarm(280)
rng = np.random.default_rng(4802)

# ---------- (a) fixed-place lemma ----------
print("(a) fixed-place lemma")
bad = 0; tot = 0
for k in range(24):
    if order(k) in (1, 2, 4):
        k2 = MUL[k][k]
        for a in (1, 2, 3):
            tot += 1
            bad += anti(a, ptype(k2, a))
print("   Clifford quarter-turn actions N (N^4 = 1), Pauli a: N^2 a anticommutes with a in %d of %d cases" % (bad, tot))
ctrl = [(k, a) for k in range(24) if order(k) == 2 for a in (1, 2, 3) if anti(a, ptype(k, a))]
print("   control, half-turn alone (M^2 = 1): M a anticommutes with a in %d cases (M = face-diagonal half-turns: %d distinct)"
      % (len(ctrl), len(set(k for k, _ in ctrl))))
# non-Clifford: N = R(n, psi), n rational, psi with N^4 = 1 (psi = 90, 270) or N^4 = half-turn (psi = 45+90j)
axes_n = [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=3) if any(v)]
def is_axis(v, tol=1e-9):
    return np.sum(np.abs(np.abs(v) - 1) < tol) == 1 and np.sum(np.abs(v) < tol) == 2
nviol = 0; nadm = 0; nchk = 0
for n in axes_n:
    for psi in [np.pi / 2, 3 * np.pi / 2, np.pi / 4, 3 * np.pi / 4, 5 * np.pi / 4, 7 * np.pi / 4]:
        N = rot_axis_angle(n, psi)
        N4 = np.linalg.matrix_power(N, 4)
        quarter = np.linalg.norm(N4 - np.eye(3)) < 1e-9
        half = np.linalg.norm(N4 - rot_axis_angle(n, np.pi)) < 1e-9
        for a in range(3):
            e = np.eye(3)[a]
            nchk += 1
            Na, N2a = N @ e, N @ N @ e
            if is_axis(Na) and is_axis(N2a):
                nadm += 1
                if abs(np.dot(N2a, e)) < 1e-9:
                    nviol += 1
print("   non-Clifford N (124 rational axes x 6 angles x 3 Paulis = %d): a, Na, N^2a all Pauli in %d cases; N^2a perpendicular to a in %d" % (nchk, nadm, nviol))

# ---------- (b) vertex-qubit census ----------
print("(b) vertex qubit + six links, every looser action rho_v of Gamma on the vertex qubit")
GENS = {'O (24 turns)': [C4[2], C3d], 'T (12 even turns)': [C2[2], C3d],
        'D2 (3 axis half-turns)': [C2[0], C2[2]], '{1, C2z}': [C2[2]]}
def hop_orbits(grp):
    seen = set(); orbs = []
    for i in range(6):
        if i in seen:
            continue
        orb = sorted(set(PERM[g][i] for g in grp)); seen |= set(orb); orbs.append(orb)
    return orbs
def v_assignments(grp, rho):
    """all rho-covariant Pauli types p(i) at the vertex qubit."""
    orbs = hop_orbits(grp); choices = []
    for orb in orbs:
        i0 = orb[0]; stab = [g for g in grp if PERM[g][i0] == i0]
        ok = []
        for t in range(4):
            if all(ptype(rho[h], t) == t for h in stab):
                p = {}
                good = True
                for g in grp:
                    j = PERM[g][i0]; tj = ptype(rho[g], t)
                    if j in p and p[j] != tj:
                        good = False; break
                    p[j] = tj
                if good:
                    ok.append(p)
        choices.append(ok)
    out = []
    for combo in itertools.product(*choices):
        p = {}
        for d in combo:
            p.update(d)
        out.append(tuple(p[i] for i in range(6)))
    return out
def emat_from_types(p):
    return [[anti(p[i], p[j]) for j in range(6)] for i in range(6)]
census = {}
d2_escape = None
for gname, grp in GROUPS.items():
    H = homs(grp, GENS[gname])
    n_assign = 0; n_nontriv = 0; n_ferm = 0; cls = Counter()
    for rho in H:
        for p in v_assignments(grp, rho):
            n_assign += 1; n_nontriv += int(any(p))
            rows, nv, dvar, yvar, cvar = link_system(grp, 'fermion', e=emat_from_types(p))
            if gf2_consistent(rows):
                n_ferm += 1
                cls[tuple(int(np.trace(ROT[rho[g]])) for g in GENS[gname])] += 1
                if gname == '{1, C2z}' and d2_escape is None:
                    sol = gf2_solve(rows, nv)
                    d2_escape = (rho, p, sol, dvar, yvar, cvar)
    # bosonic sanity: exact action, trivial dressing must be consistent
    print("   %-24s homs %3d | covariant vertex assignments %4d (nonzero %4d) | fermion-consistent %d %s"
          % (gname, len(H), n_assign, n_nontriv, n_ferm, dict(cls) if cls else ''))

# ---------- (c) far places on the axes ----------
print("(c) far vertex places v +- 2e_a (all six), induced looser actions, vertex qubit and links included")
def far_e_sets(grp, gname, sigmas_per_orbit):
    """sigmas_per_orbit: dict orbit_rep -> hom dict on its stabilizer.  One hop orbit assumed."""
    # far-place orbits and coset reps
    orbs = hop_orbits(grp)          # same permutation action on the six far places
    rep_of = {}; coset = {}
    for orb in orbs:
        k0 = orb[0]
        for k in orb:
            rep_of[k] = k0
            coset[k] = next(g for g in grp if PERM[g][k0] == k)
    def A(g, k):
        gk = PERM[g][k]; k0 = rep_of[k]
        h = MUL[MUL[INV[coset[gk]]][g]][coset[k]]
        return sigmas_per_orbit[k0][h]
    hops = hop_orbits(grp)
    assert len(hops) == 1
    i0 = 0; stab = [g for g in grp if PERM[g][i0] == i0]
    es = set()
    for q0 in itertools.product(range(4), repeat=6):
        ok = all(q0[PERM[h][k]] == ptype(A(h, k), q0[k]) for h in stab for k in range(6))
        if not ok:
            continue
        q = {}
        good = True
        for g in grp:
            i = PERM[g][i0]
            for k in range(6):
                key_ = (i, PERM[g][k]); val = ptype(A(g, k), q0[k])
                if key_ in q and q[key_] != val:
                    good = False; break
                q[key_] = val
            if not good:
                break
        if not good:
            continue
        e = tuple(tuple(sum(anti(q[(i, k)], q[(j, k)]) for k in range(6)) % 2 for j in range(6)) for i in range(6))
        es.add(e)
    return es
for gname in ['O (24 turns)', 'T (12 even turns)']:
    grp = GROUPS[gname]
    orbs = hop_orbits(grp); k0 = orbs[0][0]
    stab = [g for g in grp if PERM[g][k0] == k0]
    gens_stab = [g for g in stab if g != ID]
    Hst = homs(stab, gens_stab)
    all_e = set()
    for sig in Hst:
        all_e |= far_e_sets(grp, gname, {k0: sig})
    # vertex assignments under every rho_v
    Hv = homs(grp, GENS[gname])
    ev = set()
    for rho in Hv:
        for p in v_assignments(grp, rho):
            ev.add(tuple(tuple(r) for r in emat_from_types(p)))
    nf = 0
    for e1 in all_e:
        for e2 in ev:
            e = [[(e1[i][j] + e2[i][j]) % 2 for j in range(6)] for i in range(6)]
            rows, *_ = link_system(grp, 'fermion', e=e)
            nf += int(gf2_consistent(rows))
    print("   %-20s far-place stabilizer homs %d | distinct far sign patterns %d | vertex patterns %d | fermion-consistent combos %d"
          % (gname, len(Hst), len(all_e), len(ev), nf))
# control {1, C2z}: factors of hops +-x, +-y only at the C2z-fixed far places v +- 2e_z
grp = GROUPS['{1, C2z}']; g2 = C2[2]
invol = [k for k in range(24) if order(k) in (1, 2)]
n_try = 0; n_ok = 0; example = None
for sp, sm in itertools.product(invol, invol):     # C2z action at v+2e_z and at v-2e_z
    for qx in itertools.product(range(4), repeat=2):
        for qy in itertools.product(range(4), repeat=2):
            # factors at (far +z, far -z): hop +x: qx, hop -x: images; hop +y: qy, hop -y: images
            fac = {0: qx, 1: (ptype(sp, qx[0]), ptype(sm, qx[1])),
                   2: qy, 3: (ptype(sp, qy[0]), ptype(sm, qy[1])), 4: (0, 0), 5: (0, 0)}
            e = [[(anti(fac[i][0], fac[j][0]) + anti(fac[i][1], fac[j][1])) % 2 for j in range(6)] for i in range(6)]
            rows, *_ = link_system(grp, 'fermion', e=e)
            n_try += 1
            if gf2_consistent(rows):
                n_ok += 1
                if example is None:
                    example = (sp, sm, qx, qy)
print("   control {1, C2z} (no quarter turn, no pairing): fermion-consistent in %d of %d choices" % (n_ok, n_try))
if example:
    print("      e.g. C2z at v+2e_z: %s, at v-2e_z: %s; hop +x carries (%s, %s), hop +y carries (%s, %s) there"
          % (ROT[example[0]].tolist(), ROT[example[1]].tolist(), 'IXYZ'[example[2][0]], 'IXYZ'[example[2][1]],
             'IXYZ'[example[3][0]], 'IXYZ'[example[3][1]]))
# pairing check under D2: hop +x factors at the C2z-fixed far places v+-2e_z, induced action
grp = GROUPS['D2 (3 axis half-turns)']
k0 = 4                                   # far place +z
stab = [g for g in grp if PERM[g][k0] == k0]
cos = {4: ID, 5: C2[0]}                  # C2x maps +z -> -z
nz = 0; ntot = 0
for sg in homs(stab, [g for g in stab if g != ID]):
    def A(g, k):
        gk = PERM[g][k]; h = MUL[MUL[INV[cos[gk]]][g]][cos[k]]; return sg[h]
    for qp in range(4):
        qm = ptype(A(C2[0], 4), qp)                     # C2x fixes hop +x: factor at -z is the image
        if ptype(A(C2[0], 5), qm) != qp:
            continue
        ntot += 1
        contrib = (anti(qp, ptype(A(C2[2], 4), qp)) + anti(qm, ptype(A(C2[2], 5), qm))) % 2
        nz += contrib
print("   D2 pairing check (hop +x, far places v+-2e_z, every induced looser action): net C2z sign -1 in %d of %d cases" % (nz, ntot))

# ---------- (d) dense Levin-Wen junction phases, 7 qubits (vertex + six links) ----------
print("(d) dense 7-qubit junction phases")
NQ = 7   # qubit 0 = vertex, 1..6 = links in DIRS order
def beta_ops(ops, g, rho_U):
    """looser action of turn g: links soldered-exact (twists on links only rotate about their own
    field axis, which cannot change commutation signs), vertex by rho_U[g]."""
    new = [None] * NQ
    Ug = su2_of_rot(ROT[g])
    new[0] = rho_U[g] @ ops[0] @ rho_U[g].conj().T
    for i in range(6):
        new[1 + PERM[g][i]] = Ug @ ops[1 + i] @ Ug.conj().T
    return new
def all_triples_phases(T):
    ph = {}
    for tri in itertools.combinations(range(6), 3):
        c, res = tjunction_phase(T[tri[0]], T[tri[1]], T[tri[2]])
        ph[tri] = (np.round(c, 6), res)
    return ph
Ogrp = GROUPS['O (24 turns)']
Hv = homs(Ogrp, GENS['O (24 turns)'])
def cls_of(rho):
    t4 = int(np.trace(ROT[rho[C4[2]]])); t3 = int(np.trace(ROT[rho[C3d]]))
    return {(3, 3): 'trivial', (-1, 3): 'sign twist', (-1, 0): 'axis', (1, 0): 'soldered'}[(t4, t3)]
coset_x = {PERM[g][0]: g for g in Ogrp}
summary = Counter(); worst_cov = 0.0; tj_phases = Counter()
for trial in range(48):
    rho = Hv[rng.integers(len(Hv))]
    rho_U = {g: su2_of_rot(ROT[rho[g]]) for g in Ogrp}
    ps = [p for p in v_assignments(Ogrp, rho)]
    p = ps[rng.integers(len(ps))]
    # t_{+x}: raise on link +x; decoration on -x link: b2; on the four perpendicular links: b1 (C4x-invariant)
    b1, b2 = rng.integers(2), rng.integers(2)
    ops = [PAUL[p[0]]] + [None] * 6
    for i in range(6):
        if i == 0:
            ops[1 + i] = raise_out(0)
        elif i == 1:
            ops[1 + i] = PAUL[AXIS[i] + 1] if b2 else I2
        else:
            ops[1 + i] = PAUL[AXIS[i] + 1] if b1 else I2
    T = {}
    for i, g in coset_x.items():
        T[i] = kron_list(beta_ops(ops, g, rho_U))
    # covariance residual over all 24 turns (up to phase and Gauss parity B_v)
    Bv = kron_list([I2] + [PAUL[AXIS[i] + 1] for i in range(6)])
    for g in Ogrp:
        for i, gi_ in coset_x.items():
            img = kron_list(beta_ops(beta_ops(ops, gi_, rho_U), g, rho_U))
            tgt = T[PERM[g][i]]
            best = min(np.linalg.norm(img - (np.vdot(t, img) / np.vdot(t, t)) * t) / np.linalg.norm(img)
                       for t in (tgt, tgt @ Bv))
            worst_cov = max(worst_cov, best)
    ph = all_triples_phases(T)
    for tri, (c, res) in ph.items():
        kind = 'T-junction' if any(AXIS[a] == AXIS[b] for a, b in itertools.combinations(tri, 2)) else 'corner'
        tj_phases[(kind, complex(c))] += 1
    summary[cls_of(rho)] += 1
print("   48 random looser O-actions on the vertex qubit (classes %s), random covariant dressings:" % dict(summary))
print("   covariance residual (max over 24 turns x 6 hops, up to phase and B_v): %.1e" % worst_cov)
print("   junction phases seen: %s" % {k: v for k, v in sorted(tj_phases.items(), key=lambda z: (z[0][0], z[0][1].real))})
# control: the D2 escape
if d2_escape is not None:
    rho, p, sol, dvar, yvar, cvar = d2_escape
    grp = GROUPS['{1, C2z}']
    rho_U = {g: su2_of_rot(ROT[rho[g]]) for g in grp}
    T = {}
    for i in range(6):
        ops = [PAUL[p[i]]] + [None] * 6
        for j in range(6):
            if j == i:
                ops[1 + j] = raise_out(j)
            else:
                ops[1 + j] = PAUL[AXIS[j] + 1] if sol[dvar[(i, j)]] else I2
        T[i] = kron_list(ops)
    Bv = kron_list([I2] + [PAUL[AXIS[i] + 1] for i in range(6)])
    worst = 0.0
    for g in grp:
        for i in range(6):
            ops = [PAUL[p[i]]] + [raise_out(j) if j == i else (PAUL[AXIS[j] + 1] if sol[dvar[(i, j)]] else I2) for j in range(6)]
            img = kron_list(beta_ops(ops, g, rho_U)); tgt = T[PERM[g][i]]
            best = min(np.linalg.norm(img - (np.vdot(t, img) / np.vdot(t, t)) * t) / np.linalg.norm(img) for t in (tgt, tgt @ Bv))
            worst = max(worst, best)
    ph = all_triples_phases(T)
    print("   control {1, C2z} escape (vertex qubit): C2z acts on the vertex qubit by %s; vertex Paulis %s"
          % (ROT[rho[C2[2]]].tolist(), ''.join('IXYZ'[t] for t in p)))
    print("      {1, C2z} covariance residual %.1e; junction phases over all 20 triples: %s"
          % (worst, Counter(complex(c) for c, r in ph.values())))
    # does any looser quarter turn or 120-deg turn extend it?  (C4z must map hop +x to +y)
    ext4 = [k for k in range(24) if order(k) in (1, 2, 4) and MUL[k][k] == rho[C2[2]]
            and ptype(k, p[0]) == p[2]]
    ext3 = [k for k in range(24) if order(k) in (1, 3) and ptype(k, p[0]) == p[2] and ptype(k, p[2]) == p[4]]
    print("      Clifford vertex actions for C4z squaring to rho(C2z) and mapping p(+x) to p(+y): %d; "
          "for C3(111) mapping p(+x)->p(+y)->p(+z): %d" % (len(ext4), len(ext3)))
print("done")
