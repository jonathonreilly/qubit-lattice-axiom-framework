#!/usr/bin/env python3
"""Bell values of record laws: records-only formation stays at 2, the dynamics
clause reaches 2 sqrt 2 and no further.

Formation reading (supplied, as in the landed formation notes): each record is
a function of the records already formed at its neighbours and of fresh local
randomness. Two wings A and B each form an outcome record after a setting
record. The CHSH value is |E00 + E01 + E10 - E11| over the four setting pairs.

Checks:

A. The 16 deterministic response pairs give CHSH values of magnitude 2 at most,
   and 2 is attained.
B. Records-only formation, settings formed with no parents and neither setting
   an ancestor of the other wing's outcome: on three window templates with
   random kernels (binary and ternary contents) the joint odds decompose as a
   mixture over the common ancestry of products of one-wing odds, and the CHSH
   magnitude never exceeds 2.
C. Scope: a formation path from one wing's setting to the other wing's outcome
   (through a record whose content carries the setting) reaches 4 exactly.
D. Scope: the static reading, conditioning a five-site binary chain on its
   two end records, reaches an exact rational CHSH value above 2 sqrt 2.
E. Dynamics clause (supplied, the supplied companion construction) with records as fields and the
   trace rule (supplied, the supplied companion construction): the antiferromagnetic Heisenberg bond
   of an isolated pair has the singlet as ground state; antipodal menus give
   E = -a.b and CHSH = 2 sqrt 2 exactly; random states and menus never exceed
   2 sqrt 2 (Tsirelson; B^2 = 4 - [A0, A1] (x) [B0, B1]).
F. Sequential formation reproduces the joint odds: A records first by the trace
   rule on the pair state; B, then isolated in the field of A's record with
   its other records cancelling, records by its ground-state law.

The dynamics clause, the trace rule and the menus are supplied, not adopted.
Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from fractions import Fraction as Fr

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np
import sympy as sp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


def chsh_from_E(E):
    """Largest |CHSH| over the four relabellings of which setting pair is negated."""
    vals = [E[0][0] + E[0][1] + E[1][0] - E[1][1], E[0][0] + E[0][1] - E[1][0] + E[1][1],
            E[0][0] - E[0][1] + E[1][0] + E[1][1], -E[0][0] + E[0][1] + E[1][0] + E[1][1]]
    return max(abs(v) for v in vals)


rng = np.random.default_rng(20260924)

# ------------------------------------------------------------ A: LHV vertices
print("A. deterministic response pairs")
vals = []
for fa in itertools.product((1, -1), repeat=2):
    for fb in itertools.product((1, -1), repeat=2):
        E = [[fa[s] * fb[t] for t in range(2)] for s in range(2)]
        vals.append(chsh_from_E(E))
check("the 16 deterministic response pairs have |CHSH| <= 2, attained", max(vals) == 2 and min(vals) == 2,
      f"values {sorted(set(vals))}")


# ------------------------------------------------ B: records-only formation
print("B. records-only formation windows")


def random_kernel(n_parent_states, k):
    """A conditional law on k contents for each parent configuration."""
    K = rng.dirichlet(np.ones(k) * rng.uniform(0.2, 2.0), size=n_parent_states)
    return K


def formation_joint(template, k):
    """Exact joint law by the formation chain rule, and the common-ancestry mixture.

    Templates (source records form first, each from its formed neighbour; then
    outcomes a <- (sA, one source record), b <- (sB, another)):
      chain:   w1 -> w2 -> w3 ; a <- (sA, w1) ; b <- (sB, w3) ; common ancestry {w1}
      fork:    w0 -> w1, w0 -> w2 ; a <- (sA, w1) ; b <- (sB, w2) ; common ancestry {w0}
      shared:  w1 ; a <- (sA, w1) ; b <- (sB, w1) ; common ancestry {w1}
    Outcomes are binary; source contents take k values. The joint E is summed over
    every record of the window; the mixture sums over the common ancestry alone,
    with each wing's exclusive ancestors integrated out on that wing.
    """
    Ka = random_kernel(2 * k, 2)   # a given (sA, its source neighbour)
    Kb = random_kernel(2 * k, 2)   # b given (sB, its source neighbour)
    ea = lambda sA, w: Ka[sA * k + w][0] - Ka[sA * k + w][1]
    eb = lambda sB, w: Kb[sB * k + w][0] - Kb[sB * k + w][1]
    E = [[0.0, 0.0], [0.0, 0.0]]
    E_mix = [[0.0, 0.0], [0.0, 0.0]]
    if template == "chain":
        p1 = rng.dirichlet(np.ones(k)); K2 = random_kernel(k, k); K3 = random_kernel(k, k)
        for sA in range(2):
            for sB in range(2):
                for w1, w2, w3, a, b in itertools.product(range(k), range(k), range(k), range(2), range(2)):
                    E[sA][sB] += (p1[w1] * K2[w1, w2] * K3[w2, w3] * Ka[sA * k + w1][a] * Kb[sB * k + w3][b]
                                  * (1 - 2 * a) * (1 - 2 * b))
                for w1 in range(k):
                    eb_marg = sum(K2[w1, w2] * K3[w2, w3] * eb(sB, w3) for w2 in range(k) for w3 in range(k))
                    E_mix[sA][sB] += p1[w1] * ea(sA, w1) * eb_marg
    elif template == "fork":
        p0 = rng.dirichlet(np.ones(k)); K1 = random_kernel(k, k); K2 = random_kernel(k, k)
        for sA in range(2):
            for sB in range(2):
                for w0, w1, w2, a, b in itertools.product(range(k), range(k), range(k), range(2), range(2)):
                    E[sA][sB] += (p0[w0] * K1[w0, w1] * K2[w0, w2] * Ka[sA * k + w1][a] * Kb[sB * k + w2][b]
                                  * (1 - 2 * a) * (1 - 2 * b))
                for w0 in range(k):
                    ea_marg = sum(K1[w0, w1] * ea(sA, w1) for w1 in range(k))
                    eb_marg = sum(K2[w0, w2] * eb(sB, w2) for w2 in range(k))
                    E_mix[sA][sB] += p0[w0] * ea_marg * eb_marg
    else:
        p1 = rng.dirichlet(np.ones(k))
        for sA in range(2):
            for sB in range(2):
                for w1, a, b in itertools.product(range(k), range(2), range(2)):
                    E[sA][sB] += p1[w1] * Ka[sA * k + w1][a] * Kb[sB * k + w1][b] * (1 - 2 * a) * (1 - 2 * b)
                for w1 in range(k):
                    E_mix[sA][sB] += p1[w1] * ea(sA, w1) * eb(sB, w1)
    dev = max(abs(E[s][t] - E_mix[s][t]) for s in range(2) for t in range(2))
    return chsh_from_E(E), dev


worst, worst_dev, n = 0.0, 0.0, 0
for template in ("chain", "fork", "shared"):
    for k in (2, 3):
        for _ in range(1500):
            v, d = formation_joint(template, k)
            worst = max(worst, v)
            worst_dev = max(worst_dev, d)
            n += 1
check("records-only formation: the chain-rule joint equals the mixture over the common ancestry alone",
      worst_dev < 1e-12, f"{n} random kernels on three templates; max deviation {worst_dev:.1e}")
check("records-only formation: |CHSH| never exceeds 2", worst <= 2 + 1e-12, f"largest value {worst:.6f}")

# --------------------------------------------------------- C: cross-wing path
print("C. scope: a formation path across the wings")
# a's record content carries (a, sA): four letters; b <- (sB, a's record) with b = a xor (sA and sB)
E = [[Fr(0)] * 2 for _ in range(2)]
for sA in range(2):
    for sB in range(2):
        tot = Fr(0)
        for a in range(2):                      # a fair coin at A
            b = a ^ (sA & sB)
            tot += Fr(1, 2) * (1 - 2 * a) * (1 - 2 * b)
        E[sA][sB] = tot
v = chsh_from_E(E)
check("a record carrying the setting across the wings gives CHSH 4 exactly", v == 4, f"E = {[[str(x) for x in r] for r in E]}")

check("cross-wing PR-box has unbiased operational marginals",
      all(sum((a ^ (u & v)) == b for a in range(2)) == 1
          for u, v, b in itertools.product(range(2), repeat=3)))

# ------------------------------------------------------- D: static reading
print("D. scope: the static reading conditioned on its end records")
eps = Fr(1, 100)
bits = (0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0)
Wt = [[[(Fr(1) if bits[4 * kk + 2 * i + j] else eps) for j in range(2)] for i in range(2)] for kk in range(4)]
E = [[Fr(0)] * 2 for _ in range(2)]
for sA in range(2):
    for sB in range(2):
        tot, corr = Fr(0), Fr(0)
        for A, C, B in itertools.product(range(2), repeat=3):
            w = Wt[0][sA][A] * Wt[1][A][C] * Wt[2][C][B] * Wt[3][B][sB]
            tot += w
            corr += w * (1 - 2 * A) * (1 - 2 * B)
        E[sA][sB] = corr / tot
v = chsh_from_E(E)
check("a five-site chain law conditioned on its end records exceeds 2 sqrt 2 (exact rational)",
      v == Fr(2981272129803, 1020712070201) and v * v > 8, f"CHSH = {v} = {float(v):.6f} > 2.828427")

# --------------------------------------------------- E: the dynamics clause
print("E. the dynamics clause on an isolated pair")
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
I2 = np.eye(2, dtype=complex)


def sdot(v):
    return sum(v[k] * S[k] for k in range(3))


def proj(q):
    return 0.5 * (I2 + sdot(q))


# exact: ground state of J s.s (J > 0) is the singlet
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
HH = sp.kronecker_product(sx, sx) + sp.kronecker_product(sy, sy) + sp.kronecker_product(sz, sz)
singlet = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
ev = HH.eigenvals()
gs_ok = (HH * singlet - (-3) * singlet).applyfunc(sp.simplify) == sp.zeros(4, 1) and min(ev) == -3 and ev[-3] == 1
th = sp.symbols("theta_a theta_b", real=True)
a_vec = sp.Matrix([sp.sin(th[0]), 0, sp.cos(th[0])])
b_vec = sp.Matrix([sp.sin(th[1]), 0, sp.cos(th[1])])
Aop = a_vec[0] * sx + a_vec[2] * sz
Bop = b_vec[0] * sx + b_vec[2] * sz
Eab = sp.simplify((singlet.H * sp.kronecker_product(Aop, Bop) * singlet)[0])
corr_ok = sp.simplify(Eab + sp.cos(th[0] - th[1])) == 0
check("antiferromagnetic Heisenberg pair: unique ground state is the singlet, E(a, b) = -a.b",
      gs_ok and corr_ok, f"E = {sp.simplify(Eab)}")


def E_singlet(t_a, t_b):
    return -sp.cos(t_a - t_b)


angles_a = (0, sp.pi / 2)
angles_b = (sp.pi / 4, -sp.pi / 4)
Es = [[E_singlet(angles_a[s], angles_b[t]) for t in range(2)] for s in range(2)]
val = sp.nsimplify(sp.simplify(abs(Es[0][0] + Es[0][1] + Es[1][0] - Es[1][1])))
check("standard antipodal menus give CHSH = 2 sqrt 2 exactly", sp.simplify(val - 2 * sp.sqrt(2)) == 0, f"CHSH = {val}")

best, idt = 0.0, 0.0
for _ in range(20000):
    psi = rng.normal(size=4) + 1j * rng.normal(size=4)
    psi /= np.linalg.norm(psi)
    ms = [rng.normal(size=3) for _ in range(4)]
    ms = [m / np.linalg.norm(m) for m in ms]
    A0, A1, B0, B1 = (sdot(m) for m in ms)
    Bell = np.kron(A0, B0) + np.kron(A0, B1) + np.kron(A1, B0) - np.kron(A1, B1)
    best = max(best, abs(np.real(psi.conj() @ Bell @ psi)))
    idt = max(idt, np.abs(Bell @ Bell - (4 * np.eye(4) - np.kron(A0 @ A1 - A1 @ A0, B0 @ B1 - B1 @ B0))).max())
check("no state and no antipodal menus exceed 2 sqrt 2 (Tsirelson)", best <= 2 * np.sqrt(2) + 1e-12 and idt < 1e-12,
      f"20000 random draws: largest {best:.6f}; B^2 identity max {idt:.1e}")

# ------------------------------------------------ F: sequential formation
print("F. sequential formation with records as fields")
J = 1.0
psi = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
worst = 0.0
for _ in range(200):
    pa, pb = rng.normal(size=3), rng.normal(size=3)
    pa, pb = pa / np.linalg.norm(pa), pb / np.linalg.norm(pb)
    for sa in (1, -1):
        # A records +-pa by the trace rule on the pair state
        PA = np.kron(proj(sa * pa), I2)
        prob_a = np.real(psi.conj() @ PA @ psi)
        post = PA @ psi
        post /= np.linalg.norm(post)
        rho_b_cond = np.einsum('ij,ik->jk', post.reshape(2, 2), post.reshape(2, 2).conj())
        # B isolated: field J * (A's content) with its other records cancelling; ground state
        hB = J * sa * pa
        evals, V = np.linalg.eigh(sdot(hB))
        gsB = np.outer(V[:, 0], V[:, 0].conj())
        for sb in (1, -1):
            seq = prob_a * np.real(np.trace(proj(sb * pb) @ gsB))
            joint = np.real(psi.conj() @ np.kron(proj(sa * pa), proj(sb * pb)) @ psi)
            worst = max(worst, abs(seq - joint), np.abs(rho_b_cond - gsB).max())
check("A first by the trace rule, then B by its isolated ground-state law, reproduces the singlet odds",
      worst < 1e-12, f"200 random menu pairs; max deviation {worst:.1e}")

print('per_element: Deterministic local binary responses and PR-box marginals are tested.')
print('per_site: Single-wing response kernels and conditioned record probabilities are tested.')
print('per_mode: checked and not executed — no propagating-mode Bell claim is made.')
print('per_block: Finite classical windows and the supplied two-qubit CHSH operator are tested.')
print('lattice_wide: checked and not executed — no unrestricted lattice formation theorem is certified.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
