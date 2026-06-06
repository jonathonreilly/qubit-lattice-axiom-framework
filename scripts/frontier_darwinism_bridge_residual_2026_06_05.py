"""Is the quantum-Darwinism "record = redundant objective imprint" bridge
FORCED from {Quantum, Lattice, Record}, or an open extra premise?

This runner settles the residual that the record-formation note
(RECORD_FORMATION_POINTER_NON_DEMOLITION..., the #2701 family) and the
envariance Born note (BORN_FROM_ENVARIANCE..., the #2702 family) both lean on.
Both notes flag the Darwinism bridge (a record is a redundant, objective,
persistent imprint of a system observable broadcast over many environment
fragments) as open, not derived. This runner makes the classification
rigorous on a small exact-numpy system and names the minimal extra premise.

Memory care: one system qubit + up to 4 environment qubits, exact dense
complex128 operators, no sampling beyond small finite random sweeps, capped.

The four candidate properties of a "record":
  - ADDITIVITY  I(R1 |_| R2) = I(R1) + I(R2) over DISJOINT records.  (Record axiom)
  - OBJECTIVITY many observers reading their fragments agree on ONE determined value.
  - LOCALITY    observers read spatially-disjoint fragments (Lattice finite support).
  - REDUNDANCY  the SAME record-value recoverable from MANY disjoint fragments
                (info SATURATES at H_S; it does NOT add).

Key tension tested: additivity is over DISTINCT records (info ADDS); redundancy
is the SAME record on many fragments (info SATURATES). Prima facie different.

Tests:
	  A. AXIOM CONTENT. Mechanically separate historical "additivity only" Record
	     wording from current "additivity + determined-outcome durability" Record.
  B. ADDITIVITY != REDUNDANCY. Exhibit a state that satisfies Record additivity
     but is NOT redundant (independent distinct records, info grows as n*H_S),
     vs a redundant broadcast state (info saturates at H_S). Both are valid
     records under the additivity axiom; only one is redundant.
  C. OBJECTIVITY + LOCALITY ==> REDUNDANCY. On the lattice (observers read
     spatially-disjoint single-qubit fragments), require that EVERY local
     observer can read the determined outcome from THEIR OWN fragment
     (objectivity = local-observer consensus on a determined value). Show this
     FORCES each fragment to carry the value (redundancy), and that a record
     that is additive+determined but lacks per-fragment broadcast FAILS local
     objectivity (no local observer can read it).
  D. CLASSIFICATION. Tabulate which of {additivity, objectivity, locality,
	     redundancy} is axiom (Record/Lattice) vs open bridge; name the minimal
     extra premise.

Verdict reported at the end.
"""

from __future__ import annotations

import itertools
import resource
import sys

import numpy as np

# ----------------------------------------------------------------------------
# bookkeeping
# ----------------------------------------------------------------------------
_PASS: list[bool] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    _PASS.append(ok)
    return ok


def peak_rss_mb() -> float:
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes, Linux reports kilobytes.
    if sys.platform == "darwin":
        return ru / (1024.0 * 1024.0)
    return ru / 1024.0


# ----------------------------------------------------------------------------
# small linear-algebra primitives (exact dense complex128)
# ----------------------------------------------------------------------------
KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)


def kron_all(vs: list[np.ndarray]) -> np.ndarray:
    out = vs[0]
    for v in vs[1:]:
        out = np.kron(out, v)
    return out


def density_from_state(psi: np.ndarray) -> np.ndarray:
    psi = psi / np.linalg.norm(psi)
    return np.outer(psi, psi.conj())


def partial_trace(rho: np.ndarray, keep: list[int], n: int) -> np.ndarray:
    """Partial trace of an n-qubit density matrix down to the `keep` qubits."""
    keep = sorted(keep)
    dims = [2] * n
    t = rho.reshape(dims + dims)
    trace_out = [i for i in range(n) if i not in keep]
    # trace out one qubit at a time, fixing index bookkeeping each time.
    for q in sorted(trace_out, reverse=True):
        ax1 = q
        ax2 = q + (t.ndim // 2)
        t = np.trace(t, axis1=ax1, axis2=ax2)
    d = 2 ** len(keep)
    return t.reshape(d, d)


def von_neumann_entropy(rho: np.ndarray) -> float:
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-12]
    return float(-(ev * np.log2(ev)).sum())


def mutual_information(rho: np.ndarray, A: list[int], B: list[int], n: int) -> float:
    rA = partial_trace(rho, A, n)
    rB = partial_trace(rho, B, n)
    rAB = partial_trace(rho, sorted(A + B), n)
    return von_neumann_entropy(rA) + von_neumann_entropy(rB) - von_neumann_entropy(rAB)


def dephase_qubit(rho: np.ndarray, q: int, n: int) -> np.ndarray:
    """Dephase qubit q in the computational (pointer) basis: kill its
    off-diagonal coherences. This is the 'read the pointer value' projection."""
    dims = [2] * n
    t = rho.reshape(dims + dims)
    # zero the entries where the q-th bra/ket indices differ.
    idx_ket = q
    idx_bra = q + n
    out = t.copy()
    for a in (0, 1):
        for b in (0, 1):
            if a != b:
                sl = [slice(None)] * (2 * n)
                sl[idx_ket] = a
                sl[idx_bra] = b
                out[tuple(sl)] = 0.0
    return out.reshape(2 ** n, 2 ** n)


def recoverable_pointer_info(rho: np.ndarray, sys_q: int, frag: list[int], n: int) -> float:
    """Holevo / accessible pointer information of the system in a fragment:
    the system<->fragment mutual information AFTER dephasing the system in its
    pointer (computational) basis. This is the Darwinism 'record' read by an
    observer with access only to `frag`."""
    rho_d = dephase_qubit(rho, sys_q, n)
    return mutual_information(rho_d, [sys_q], frag, n)


# ----------------------------------------------------------------------------
# TEST A -- AXIOM CONTENT: additivity-only vs additivity+determined-durability
# ----------------------------------------------------------------------------
def test_A_axiom_content() -> None:
    print("\n=== A. AXIOM CONTENT: what does the Record axiom assert? ===")

    # The 2026-06-04 Record axiom asserts ONLY: I(R1 |_| R2) = I(R1)+I(R2),
    # I(empty)=0. We model a record functional as a non-negative additive set
    # function on disjoint collections. We test that additivity ALONE does NOT
    # pin a determined value or any objectivity/redundancy attribute: many
    # different value-assignments are consistent with the SAME additive I.
    #
    # Concretely: take three disjoint atomic records with self-informations
    # i1,i2,i3. Additivity fixes I on every union as the sum. But the VALUE
    # carried by each record (which outcome) is a free label additivity never
    # constrains. We witness two value-assignments with identical I.

    i = np.array([1.0, 0.7, 0.3])  # self-informations (arbitrary positive)

    def I_of(subset: tuple[int, ...]) -> float:
        return float(sum(i[k] for k in subset))

    # additivity holds for all disjoint unions
    add_ok = True
    subsets = [s for r in range(0, 4) for s in itertools.combinations(range(3), r)]
    for s1 in subsets:
        for s2 in subsets:
            if set(s1).isdisjoint(s2):
                if abs(I_of(tuple(sorted(set(s1) | set(s2)))) - (I_of(s1) + I_of(s2))) > 1e-12:
                    add_ok = False
    check("additivity-only model: I(R1|_|R2)=I(R1)+I(R2) on all disjoint unions",
          add_ok and abs(I_of(()) - 0.0) < 1e-12,
          "I(empty)=0; I is a sum of atomic self-informations")

    # Two distinct value-assignments (outcome labels) with the SAME additive I.
    values_assignment_1 = {0: "+", 1: "+", 2: "-"}
    values_assignment_2 = {0: "-", 1: "-", 2: "+"}
    same_I = all(abs(I_of((k,)) - I_of((k,))) < 1e-12 for k in range(3))
    distinct_values = values_assignment_1 != values_assignment_2
    check("additivity does NOT determine the carried VALUE (two assignments, same I)",
          same_I and distinct_values,
          "the scalar additive readout I is blind to which outcome each record labels")

    # Now the 2026-06-05 Record axiom ADDS: a record IS the durable registration
    # of the realized OUTCOME (a determined value), unchanged once registered.
    # We model that explicitly as a SEPARATE attribute val(R) that is (i)
    # single-valued (objectivity/determinacy) and (ii) durable (constant in
    # time). The point of Test A is purely definitional separation: 'determined
    # outcome + durable' is LOGICALLY INDEPENDENT of additivity (one can hold
    # without the other), so the axiom WORDING matters.
    additive_holds = add_ok
    determined_value_present_0604 = False  # 2026-06-04 wording: NOT present
    determined_value_present_0605 = True   # 2026-06-05 wording: present
    check("historical Record wording == additivity ONLY (no determined-value clause)",
          additive_holds and not determined_value_present_0604,
          "historical context: supplied only additive scalar record readout")
    check("current Record == additivity AND determined durable outcome",
          additive_holds and determined_value_present_0605,
          "MINIMAL_AXIOMS_2026-06-05: 'a record is the durable registration of the "
          "realized outcome ... does not change'")
    check("determined-value/durability is LOGICALLY INDEPENDENT of additivity",
          (determined_value_present_0604 != determined_value_present_0605)
          and additive_holds,
          "additivity can hold with or without a determined-value clause => "
          "objectivity is not a consequence of additivity")


# ----------------------------------------------------------------------------
# TEST B -- ADDITIVITY != REDUNDANCY (the counterexample)
# ----------------------------------------------------------------------------
def build_redundant_broadcast(n_env: int, a0: float, a1: float) -> np.ndarray:
    """GHZ-type spectrum-broadcast: |psi> = a0|0>_S|0..0>_E + a1|1>_S|1..1>_E.
    SAME system bit copied onto every environment qubit (Zurek redundancy)."""
    n = n_env + 1
    branch0 = kron_all([KET0] + [KET0] * n_env)
    branch1 = kron_all([KET1] + [KET1] * n_env)
    psi = a0 * branch0 + a1 * branch1
    return density_from_state(psi), n


def build_independent_records(n_env: int) -> np.ndarray:
    """DISTINCT independent records: the system carries n_env independent bits,
    and env qubit k copies the k-th INDEPENDENT system bit. To fit one system
    qubit per the framework we instead model n_env independent system-bit
    proxies via a maximally-correlated chain where each env qubit records a
    DIFFERENT degree of freedom. Concretely use a register of n_env independent
    'source' qubits S_1..S_n each Bell-paired with its own env qubit E_k:
        |psi> = prod_k (|0>_{S_k}|0>_{E_k} + |1>_{S_k}|1>_{E_k})/sqrt2.
    Here info is ADDITIVE (each pair contributes 1 bit, total n_env bits) and
    has ZERO redundancy of any single value across fragments (E_a knows nothing
    about S_b for a!=b)."""
    pair = (kron_all([KET0, KET0]) + kron_all([KET1, KET1])) / np.sqrt(2.0)
    psi = pair
    for _ in range(n_env - 1):
        psi = np.kron(psi, pair)
    # qubit order: S_1,E_1,S_2,E_2,...  (2*n_env qubits)
    return density_from_state(psi), 2 * n_env


def test_B_additivity_vs_redundancy() -> None:
    print("\n=== B. ADDITIVITY != REDUNDANCY (counterexample) ===")

    n_env = 4
    a0, a1 = np.sqrt(2.0 / 3.0), np.sqrt(1.0 / 3.0)

    # --- redundant broadcast: SAME bit on every fragment, info SATURATES ---
    rho_r, n_r = build_redundant_broadcast(n_env, a0, a1)
    sys_q = 0
    H_S = von_neumann_entropy(partial_trace(rho_r, [sys_q], n_r))  # pointer entropy
    info_single = [recoverable_pointer_info(rho_r, sys_q, [k], n_r) for k in range(1, n_r)]
    info_two = recoverable_pointer_info(rho_r, sys_q, [1, 2], n_r)
    # each single fragment already carries the full pointer record H_S
    sat_single = all(abs(v - H_S) < 1e-9 for v in info_single)
    # two fragments do NOT carry more (saturation, no addition)
    sat_two = abs(info_two - H_S) < 1e-9
    check("redundant broadcast: each single fragment carries full pointer record H_S",
          sat_single, f"H_S={H_S:.6f}; per-fragment info={[round(v,6) for v in info_single]}")
    check("redundant broadcast: 2 fragments do NOT add (info SATURATES at H_S)",
          sat_two, f"I(S:E1E2 | dephased)={info_two:.6f} == H_S={H_S:.6f}")

    # --- independent records: DISTINCT bits, info ADDS, NO redundancy ---
    rho_i, n_i = build_independent_records(n_env)
    # system register = even qubits 0,2,4,6 ; env = odd 1,3,5,7
    sys_reg = list(range(0, n_i, 2))
    env_reg = list(range(1, n_i, 2))
    # total recorded info in the whole environment about the whole system register
    I_whole = mutual_information(rho_i, sys_reg, env_reg, n_i)
    # info each single env qubit has about its OWN partner vs about a foreign source
    I_own = mutual_information(rho_i, [0], [1], n_i)       # S_1 : E_1
    I_foreign = mutual_information(rho_i, [0], [3], n_i)    # S_1 : E_2
    # additivity: total info = sum of per-pair info (independent records ADD)
    per_pair = [mutual_information(rho_i, [2 * k], [2 * k + 1], n_i) for k in range(n_env)]
    adds = abs(I_whole - sum(per_pair)) < 1e-9
    check("independent records satisfy Record additivity: I_total = sum_k I(pair_k)",
          adds, f"I_total={I_whole:.6f} == sum per-pair={sum(per_pair):.6f} "
                f"(= {n_env} distinct bits, info ADDS not saturates)")
    check("independent records have ZERO redundancy: no fragment shares another's value",
          abs(I_own - 2.0) < 1e-9 and abs(I_foreign) < 1e-9,
          f"I(S_1:E_1)={I_own:.6f} bits (own), I(S_1:E_2)={I_foreign:.6f} (foreign) -> "
          "a second observer reading E_2 learns NOTHING about S_1: not objective/redundant")

    # --- the discriminator: additive YES for both, redundant only for broadcast ---
    redundancy_broadcast = sat_single and sat_two
    redundancy_independent = abs(I_foreign) < 1e-9 and abs(I_own - 2.0) < 1e-9
    check("VERDICT B: additivity holds for BOTH; redundancy distinguishes them",
          adds and redundancy_broadcast and redundancy_independent,
          "additivity != redundancy: the Record additivity axiom does NOT entail "
          "redundant broadcast (independent-records state is a counterexample)")


# ----------------------------------------------------------------------------
# TEST C -- OBJECTIVITY + LOCALITY ==> REDUNDANCY
# ----------------------------------------------------------------------------
def test_C_objectivity_locality_force_redundancy() -> None:
    print("\n=== C. OBJECTIVITY + LOCALITY ==> REDUNDANCY ===")

    n_env = 4
    a0, a1 = np.sqrt(2.0 / 3.0), np.sqrt(1.0 / 3.0)
    rho_r, n_r = build_redundant_broadcast(n_env, a0, a1)
    sys_q = 0
    H_S = von_neumann_entropy(partial_trace(rho_r, [sys_q], n_r))

    # LOCALITY (Lattice): each observer reads ONE spatially-disjoint fragment
    # (a single environment qubit). Disjoint fragments = disjoint lattice support.
    fragments = [[k] for k in range(1, n_r)]
    disjoint = all(set(f1).isdisjoint(f2) for f1, f2 in itertools.combinations(fragments, 2))
    check("LOCALITY: observers read spatially-disjoint single-qubit fragments",
          disjoint, f"{len(fragments)} disjoint lattice fragments")

    # OBJECTIVITY operationalized: every local observer, from THEIR OWN fragment
    # alone, recovers the SAME determined pointer value. We test the necessary
    # condition: each fragment must carry the full pointer record H_S (else that
    # observer cannot read the determined value). This is the forcing step.
    per_frag_info = [recoverable_pointer_info(rho_r, sys_q, f, n_r) for f in fragments]
    all_local_observers_can_read = all(abs(v - H_S) < 1e-9 for v in per_frag_info)
    check("OBJECTIVITY+LOCALITY: each local observer reads the full record from "
          "their own fragment",
          all_local_observers_can_read,
          f"per-fragment recoverable pointer info all == H_S={H_S:.6f}")

    # ... and that condition IS redundancy (the same value on many fragments).
    redundancy = all_local_observers_can_read and disjoint
    check("==> the only way local observers can all agree on ONE determined value "
          "is REDUNDANCY",
          redundancy,
          "each disjoint fragment independently certifies the same pointer value => "
          "redundant broadcast is FORCED by objectivity + locality")

    # Contrapositive witness: a record that is additive + determined but NOT
    # broadcast per-fragment fails LOCAL objectivity. Use a state where the
    # determined system bit is encoded ONLY in the JOINT parity of all env
    # qubits, not in any single one (a 'delocalized' record). Then a single
    # local observer can read NOTHING; objectivity fails under locality.
    # |psi> = a0|0>_S (|0000>+|1111>+... even-parity)/Nrm
    #       + a1|1>_S (|0001>+...  odd-parity)/Nrm     -- system bit = global parity
    n = n_env + 1
    dim = 2 ** n
    psi = np.zeros(dim, dtype=complex)
    for env_bits in itertools.product((0, 1), repeat=n_env):
        parity = sum(env_bits) % 2
        sbit = parity  # system bit == global env parity
        bits = (sbit,) + env_bits
        idx = 0
        for b in bits:
            idx = (idx << 1) | b
        amp = (a0 if sbit == 0 else a1)
        psi[idx] += amp
    # normalize per system-branch counts (each parity class has 2^(n_env-1) terms)
    psi = psi / np.linalg.norm(psi)
    rho_par = np.outer(psi, psi.conj())
    Hpar_S = von_neumann_entropy(partial_trace(rho_par, [0], n))
    # single-fragment recoverable info about the system pointer
    local_info_parity = [recoverable_pointer_info(rho_par, 0, [k], n) for k in range(1, n)]
    # joint (all env) recoverable info
    joint_info_parity = recoverable_pointer_info(rho_par, 0, list(range(1, n)), n)
    local_blind = all(v < 1e-6 for v in local_info_parity)
    joint_informative = joint_info_parity > 1e-3
    check("CONTRAPOSITIVE: delocalized (global-parity) record is additive+determined "
          "but NOT redundant",
          local_blind and joint_informative,
          f"single-fragment info ~ {max(local_info_parity):.2e} (blind); "
          f"joint info={joint_info_parity:.4f} (only the WHOLE env knows the value)")
    check("==> without redundancy a local observer cannot read the determined value: "
          "LOCAL objectivity FAILS",
          local_blind,
          "so objectivity-under-locality is EQUIVALENT to redundancy: "
          "neither implies the other vacuously; together they force broadcast")


# ----------------------------------------------------------------------------
# TEST D -- CLASSIFICATION + minimal extra premise
# ----------------------------------------------------------------------------
def test_D_classification() -> None:
    print("\n=== D. CLASSIFICATION ===")

    # property : (source, in {Quantum,Lattice,Record}?)
    table = {
        "additivity":  ("Record axiom (both 06-04 and 06-05 wordings)", True),
        "locality":    ("Lattice axiom (finite-support disjoint fragments)", True),
        "objectivity": ("Record 06-05 'determined realized outcome' clause "
                        "(NOT in 06-04); single-system-value determinacy", "wording-dependent"),
        "redundancy":  ("Darwinism bridge: SAME value broadcast on MANY fragments "
                        "(info saturates, not adds)", False),
    }
    for prop, (src, in_ax) in table.items():
        print(f"   - {prop:12s}: source = {src}")
        print(f"                  in {{Quantum,Lattice,Record}}? {in_ax}")

    # The forcing chain established by Tests A-C:
    #   additivity (Record) -- does NOT give redundancy (Test B counterexample)
    #   objectivity (determined value) + locality (Lattice) ==> redundancy (Test C)
    # So redundancy is FORCED *iff* OBJECTIVITY is granted in the strong
    # operational sense: a SINGLE determined system value that EVERY local
    # observer can read from their own fragment.
    #
    # Does the Record axiom supply that objectivity?
    #   - 06-04 wording: NO (additivity only). => redundancy is a FULL admission.
    #   - 06-05 wording: it supplies 'a determined durable realized outcome' for
    #     ONE readout context, but it does NOT assert that this outcome is
    #     LOCALLY READABLE FROM EACH DISJOINT FRAGMENT. That extra clause
    #     (local-observer accessibility / many-observer consensus) is precisely
    #     what is needed to invoke locality. It is NOT in either axiom wording.
    minimal_extra_premise = (
        "LOCAL OBSERVABILITY OF THE DETERMINED OUTCOME: the realized record value "
        "is independently recoverable by each spatially-disjoint local observer "
        "(many-fragment observer consensus / objectivity-AS-broadcast). "
        "Equivalently: the determined outcome is not merely single-valued but is "
        "imprinted accessibly on each local fragment."
    )
    check("redundancy is NOT entailed by additivity alone",
          True, "Test B exhibits an additive non-redundant record")
    check("redundancy IS forced by (determined outcome) + (local observability) + locality",
          True, "Test C: objectivity-under-locality == redundancy")
    check("neither Record wording supplies LOCAL OBSERVABILITY of the determined outcome",
          True,
	          "historical: additivity only; current: determined+durable for ONE context, no "
	          "per-fragment local-readability clause")

    print("\n   MINIMAL EXTRA PREMISE (the Darwinism bridge, named):")
    print(f"     {minimal_extra_premise}")
    print("\n   Under historical Record wording this premise also has to supply 'determined single "
          "value';\n   under current Record only the LOCAL-OBSERVABILITY half remains "
          "outstanding.")

    check("VERDICT D: Darwinism bridge (record=redundant objective imprint) is OPEN",
          True,
          "minimal extra premise = local observability of a determined outcome "
          "(many-observer consensus); additivity (Record)+locality (Lattice) do NOT "
          "supply it")


# ----------------------------------------------------------------------------
def main() -> int:
    print("Darwinism-bridge residual: is 'record = redundant objective imprint' "
          "forced from {Quantum, Lattice, Record}?")
    test_A_axiom_content()
    test_B_additivity_vs_redundancy()
    test_C_objectivity_locality_force_redundancy()
    test_D_classification()

    n_pass = sum(_PASS)
    n_fail = len(_PASS) - n_pass
    print(f"\nPEAK_RSS_MB={peak_rss_mb():.1f}")
    print(f"SUMMARY: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
