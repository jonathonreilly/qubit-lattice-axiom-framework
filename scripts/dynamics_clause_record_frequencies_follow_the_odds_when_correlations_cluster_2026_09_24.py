#!/usr/bin/env python3
"""Record frequencies follow the one-shot odds when the averaged connected correlation vanishes.

Supplied and not adopted: the dynamics clause of the supplied companion construction and the trace rule
(the supplied companion construction). Records form at n unrecorded sites from a joint state rho; site
i uses the antipodal menu {+p_i, -p_i}. The landed IID/typicality firewall
(docs/RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md) showed that one-step odds
do not fix frequencies: a sequence law is needed. Under the trace rule the
sequence law is the joint trace rule on rho.

Checks:

A. The joint law of the n records is the same for every formation order
   (sequential collapse by commuting single-site projectors), and the
   frequency F of +p outcomes has exactly
   E F = (1/n) sum_i (1 + <p_i.s_i>)/2,
   Var F = (1/4n^2) sum_ij (<(p_i.s_i)(p_j.s_j)> - <p_i.s_i><p_j.s_j>)
   (random 6-qubit states and menus).
B. The firewall's two laws are trace-rule laws of states: the product state
   with odds (2/3, 1/3) gives the IID count law (1/9, 4/9, 4/9) and the cat
   state sqrt(2/3)|00> + sqrt(1/3)|11> gives the locked law (1/3, 0, 2/3); on
   n sites the product's variance is 2/(9n) and the cat's stays 2/9.
C. A clustering example from the clause: in the ground state of the gapped
   Kitaev staircase tube (12 sites, the supplied companion construction's compass point), the spin
   correlation <s^a_i s^b_j> vanishes unless i = j or (i, j) is a bond of
   type a = b; a finite z-menu variance is computed; no all-size scaling is tested.
D. The clause's degenerate ground spaces hold both kinds: the ferromagnetic
   Heisenberg ground multiplet on a 6-site ring contains the cat
   (|up...up> + |down...down>)/sqrt 2, whose z-menu frequency is 0 or 1
   (variance 1/4), and the product state along x, whose z-menu frequency
   concentrates (variance 1/(4n)), with the same one-shot odds 1/2.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_RECORD_FREQUENCIES_FOLLOW_THE_ONE_SHOT_ODDS_EXACTLY_WHEN_CORRELATIONS_CLUSTER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
I2 = np.eye(2, dtype=complex)


def sdot(v):
    return sum(v[k] * S[k] for k in range(3))


def proj(q):
    return 0.5 * (I2 + sdot(q))


def op(n, placed):
    return reduce(np.kron, [placed.get(k, I2) for k in range(n)])


def unit(v):
    return v / np.linalg.norm(v)


# ------------------------------------------------------ A: the variance identity
print("A. the joint law and the variance identity")
n = 6
worst_order, worst_mom = 0.0, 0.0
for trial in range(5):
    psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n)
    psi /= np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    menus = [unit(rng.normal(size=3)) for _ in range(n)]
    Pp = [op(n, {i: proj(menus[i])}) for i in range(n)]
    Pm = [op(n, {i: proj(-menus[i])}) for i in range(n)]
    # joint law by the product of projectors (any order: they commute)
    joint = {}
    for outs in itertools.product((1, -1), repeat=n):
        P = reduce(np.matmul, [Pp[i] if outs[i] == 1 else Pm[i] for i in range(n)])
        joint[outs] = np.real(np.trace(P @ rho))
    # sequential collapse in a random order reproduces it
    order = rng.permutation(n)
    for outs in list(joint)[:16]:
        r = rho.copy()
        prob = 1.0
        for i in order:
            P = Pp[i] if outs[i] == 1 else Pm[i]
            pr = np.real(np.trace(P @ r))
            prob *= pr
            r = P @ r @ P / pr if pr > 1e-15 else r
        worst_order = max(worst_order, abs(prob - joint[outs]))
    # moments of F
    EF = sum(pr * sum(1 for o in outs if o == 1) / n for outs, pr in joint.items())
    VF = sum(pr * (sum(1 for o in outs if o == 1) / n) ** 2 for outs, pr in joint.items()) - EF ** 2
    X = [op(n, {i: sdot(menus[i])}) for i in range(n)]
    m = [np.real(np.trace(X[i] @ rho)) for i in range(n)]
    EF_formula = sum((1 + m[i]) / 2 for i in range(n)) / n
    C = [[np.real(np.trace(X[i] @ X[j] @ rho)) - m[i] * m[j] for j in range(n)] for i in range(n)]
    VF_formula = sum(C[i][j] for i in range(n) for j in range(n)) / (4 * n * n)
    worst_mom = max(worst_mom, abs(EF - EF_formula), abs(VF - VF_formula))
check("the joint law is order-independent and E F, Var F obey the exact identities",
      worst_order < 1e-12 and worst_mom < 1e-12, f"5 random 6-qubit states; order {worst_order:.1e}, moments {worst_mom:.1e}")

# ---------------------------------------------------- B: the firewall's two laws
print("B. the firewall's two laws as states")
a0, a1 = np.sqrt(2 / 3), np.sqrt(1 / 3)
prod2 = np.kron([a0, a1], [a0, a1])
cat2 = a0 * np.array([1, 0, 0, 0]) + a1 * np.array([0, 0, 0, 1])


def count_law(state, nq):
    probs = np.abs(state) ** 2
    law = [0.0] * (nq + 1)
    for idx, p in enumerate(probs):
        zeros = nq - bin(idx).count("1")
        law[zeros] += p
    return law


ip = count_law(prod2, 2)      # Pr(N0 = 0, 1, 2)
lk = count_law(cat2, 2)
want_ip = [1 / 9, 4 / 9, 4 / 9]
want_lk = [1 / 3, 0.0, 2 / 3]
marg_ok = abs(sum(p for i, p in enumerate(np.abs(cat2) ** 2) if (i >> 1) == 0) - 2 / 3) < 1e-12
check("product state gives the IID law (1/9, 4/9, 4/9); the cat gives the locked law (1/3, 0, 2/3)",
      np.allclose(ip, want_ip) and np.allclose(lk, want_lk) and marg_ok,
      f"product {np.round(ip, 6).tolist()}, cat {np.round(lk, 6).tolist()}; same one-record odds 2/3")
vals, ok_b = [], True
for nq in (4, 8, 12):
    prodn = reduce(np.kron, [np.array([a0, a1])] * nq)
    catn = np.zeros(2 ** nq)
    catn[0], catn[-1] = a0, a1
    res = []
    for st in (prodn, catn):
        law = count_law(st, nq)             # law of the number of zeros
        ef = sum(k * p for k, p in enumerate(law)) / nq
        vf = sum((k / nq) ** 2 * p for k, p in enumerate(law)) - ef ** 2
        res.append((ef, vf))
    ok_b &= abs(res[0][0] - 2 / 3) < 1e-12 and abs(res[1][0] - 2 / 3) < 1e-12
    ok_b &= abs(res[0][1] - 2 / (9 * nq)) < 1e-12 and abs(res[1][1] - 2 / 9) < 1e-12
    vals.append((nq, res[0][1], res[1][1]))
check("from the n-site states: the product's frequency variance is 2/(9n), the cat's stays 2/9, same mean 2/3",
      ok_b, "; ".join(f"n = {a}: {b:.5f}, {c:.5f}" for a, b, c in vals))

# --------------------------------------------- C: the gapped Kitaev tube clusters
print("C. clustering in the gapped Kitaev staircase tube")
N = 3
sites = {}
for z in range(N):
    for x in (0, 1):
        for r in (0, 1):
            sites[(x, r, z)] = len(sites)
nq = len(sites)
bonds = []
for z in range(N):
    bonds.append((sites[(0, 0, z)], sites[(1, 0, z)], 0))
    bonds.append((sites[(0, 1, z)], sites[(1, 1, z)], 0))
    for x in (0, 1):
        bonds.append((sites[(x, 0, z)], sites[(x, 1, z)], 1))
        bonds.append((sites[(x, 0, z)], sites[(x, 1, (z + 1) % N)], 2))
import scipy.sparse as sps
import scipy.sparse.linalg as spla

SSp = [sps.csr_matrix(m) for m in S]
I2p = sps.identity(2, dtype=complex, format="csr")


def sop(nqq, placed):
    return reduce(lambda A, B: sps.kron(A, B, format="csr"), [placed.get(k, I2p) for k in range(nqq)])


def apply_pauli(vec, nqq, i, a):
    t = vec.reshape([2] * nqq)
    t = np.moveaxis(np.tensordot(S[a], t, axes=([1], [i])), 0, i)
    return t.reshape(-1)


H = sum(sop(nq, {j: SSp[a], k: SSp[a]}) for (j, k, a) in bonds)
ev, V = spla.eigsh(H, k=4, which="SA", v0=np.random.default_rng(9052).normal(size=H.shape[0]), tol=1e-12)
assert np.max(np.linalg.norm(H @ V - V * ev, axis=0)) < 1e-9
order = np.argsort(ev)
ev, V = ev[order], V[:, order]
gs = V[:, 0]
degenerate = ev[1] - ev[0] < 1e-9
bondset = {(min(j, k), max(j, k), a) for (j, k, a) in bonds}
viol, nonzero_bonds = 0.0, 0
for i in range(nq):
    for a in range(3):
        vi = apply_pauli(gs, nq, i, a)
        for j in range(nq):
            if i == j:
                continue
            for b in range(3):
                val = np.real(np.vdot(gs, apply_pauli(vi, nq, j, b)))
                allowed = a == b and (min(i, j), max(i, j), a) in bondset
                if allowed:
                    nonzero_bonds += abs(val) > 1e-6
                else:
                    viol = max(viol, abs(val))
means = max(abs(np.real(np.vdot(gs, apply_pauli(gs, nq, i, a)))) for i in range(nq) for a in range(3))
Cz = sum(np.real(np.vdot(gs, apply_pauli(apply_pauli(gs, nq, j, 2), nq, i, 2))) for i in range(nq) for j in range(nq))
VFz = Cz / (4 * nq * nq)
check("tube ground state: <s^a_i s^b_j> = 0 unless (i,j) is a bond of type a = b; <s_i> = 0",
      (not degenerate) and viol < 1e-9 and means < 1e-9 and nonzero_bonds > 0,
      f"largest forbidden correlation {viol:.1e}; {nonzero_bonds // 2} nonzero bond correlations; gap {ev[1] - ev[0]:.4f}")
check("z-menu frequency variance on the tube is (n + 2 sum_zbonds <s^z s^z> )/(4 n^2), finite n=12 diagnostic",
      VFz < 1.0 / (4*nq) and abs(VFz - (nq + 2*sum(np.vdot(gs, apply_pauli(apply_pauli(gs,nq,j,2),nq,i,2)).real for i,j,a in bonds if a==2))/(4*nq*nq)) < 1e-10, f"n = {nq}: Var F = {VFz:.5f} (1/(4n) = {1 / (4 * nq):.5f})")

# ------------------------------------------ D: cats in the ferromagnetic multiplet
print("D. the ferromagnetic ground multiplet holds cats and products")
nr = 6
Hf = -sum(op(nr, {i: S[a], (i + 1) % nr: S[a]}) for i in range(nr) for a in range(3))
evf, Vf = np.linalg.eigh(Hf)
g0 = evf[0]
Pg = sum(np.outer(Vf[:, k], Vf[:, k].conj()) for k in range(len(evf)) if abs(evf[k] - g0) < 1e-9)
up = np.zeros(2 ** nr)
up[0] = 1
dn = np.zeros(2 ** nr)
dn[-1] = 1
cat = (up + dn) / np.sqrt(2)
plus = reduce(np.kron, [np.array([1, 1]) / np.sqrt(2)] * nr)
in_cat = abs(np.real(cat @ Pg @ cat) - 1) < 1e-12
in_plus = abs(np.real(plus.conj() @ Pg @ plus) - 1) < 1e-12


def freq_var_z(state, nqq):
    probs = np.abs(state) ** 2
    Fs = [bin(i).count("1") / nqq for i in range(2 ** nqq)]
    ef = sum(p * f for p, f in zip(probs, Fs))
    return sum(p * f * f for p, f in zip(probs, Fs)) - ef ** 2, ef


vc, ec = freq_var_z(cat, nr)
vp, ep = freq_var_z(plus, nr)
check("the multiplet contains the cat (Var F = 1/4) and the x-product (Var F = 1/(4n)), both with odds 1/2",
      in_cat and in_plus and abs(vc - 0.25) < 1e-12 and abs(vp - 1 / (4 * nr)) < 1e-12 and abs(ec - 0.5) < 1e-12
      and abs(ep - 0.5) < 1e-12, f"degeneracy {int(round(np.real(np.trace(Pg))))}; Var {vc:.4f} and {vp:.4f}")

print('per_element: Single-site projectors and connected-correlation identities are tested.')
print('per_site: Record marginals and their contribution to frequency variance are tested.')
print('per_mode: checked and not executed — no infinite-volume spectral gap is computed.')
print('per_block: Finite product, cat, labelled-graph and ferromagnetic-ring states are tested.')
print('lattice_wide: checked and not executed — uniform clustering is imported conditionally, not numerically proved.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
