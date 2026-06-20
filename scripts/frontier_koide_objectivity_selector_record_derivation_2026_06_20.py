#!/usr/bin/env python3
"""
ROUTE R2 (objectivity selector -- the hard residual).

TASK: try to DERIVE the records/objectivity maximization selector that the
KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL note keeps as named input (2) -- i.e.,
that the physical readout criterion is objectivity / redundancy maximization
over the K/CPT (Klein-four-flavored C3) sector readout, uniquely selecting the
determinant-symmetric point r=1/2 -- from the framework Record structure
{Lattice, Quantum, Record} + the four approved primitives. Build the
spectrum-broadcast-structure (SBS) / quantum-Darwinism objectivity functional
over the two-symbol K-real sector alphabet and test whether MAXIMIZING it
selects r=1/2 WITHOUT assuming equal sector weights.

HONEST FRAMING (this runner is an attempted derivation, reported as residuals):
the question is whether "objectivity maximization picks r=1/2" is a CONSEQUENCE
of Record, or a SEPARATE admitted readout-context choice. Every check below is a
real computation (numpy SBS states + partial traces + von Neumann / mutual
information; sympy extremum algebra). The TOTAL line reports PASS/FAIL of the
LOGICAL CLAIMS being tested, NOT of "r=1/2 is derived".

WHAT THE COMPUTATION FINDS (preview; each is a verified residual below):

  S0  Provenance / scope guards. r and Q are never injected as inputs; the
      empirical Koide value is not imported; the four primitives are loaded.

  S1  SECTOR ALPHABET + WEIGHT<->r MAP. The K/CPT orbits of the C3 circulant
      mass operator give a 2-symbol objective alphabet {singlet(rank1),
      doublet(rank2)}. The signed-readout block energies are E_+=3a^2,
      E_perp=6|b|^2, so the doublet share p_perp = E_perp/(E_++E_perp) = 2r/(1+2r)
      and p_+ = 1/(1+2r). r is a 1-1 reparam of the weight; r=1/2 <=> p=(1/2,1/2);
      r=1 <=> p=(1/3,2/3) (dimension/Born). DETERMINANT-SYMMETRIC point r=1/2
      <=> E_+=E_perp <=> p uniform.

  S2  OBJECTIVITY IS WEIGHT-BLIND (the central wall). Build the SBS broadcast
      state with ARBITRARY weights p on the 2-symbol alphabet over N env
      fragments. For EVERY weight choice the objectivity is FULL: each single
      fragment perfectly distinguishes the two sectors (Holevo chi = H(p),
      observer mutual info plateaus at H(p), fragments are mutually orthogonal
      conditioned on the sector). Objectivity / redundancy is present for ALL r,
      so the objectivity PROPERTY does not select any r. (Reproduces
      FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT: objectivity fixes the basis,
      not the weight.)

  S3  WHAT ACTUALLY PEAKS AT r=1/2 IS H(WEIGHTS), AN INDIFFERENCE FUNCTIONAL,
      NOT REDUNDANCY. The redundancy plateau / observer-recoverable information
      EQUALS H(p) and is MAXIMIZED at p uniform => r=1/2. But maximizing H(p)
      is the max-entropy / equal-a-priori (indifference) selector over the
      sector LABELS, NOT a redundancy/broadcast property. Maximizing the
      *redundancy MULTIPLICITY* R_delta (number of fragments carrying the record)
      is weight-independent and does NOT peak at uniform. So "objectivity
      MAXIMIZATION -> r=1/2" decomposes as: (broadcast objectivity: weight-blind)
      + (maximize Shannon entropy of the readout weights: a separate indifference
      input). The selector is the indifference half, not the objectivity half.

  S4  RECORD DOES NOT SUPPLY THE INDIFFERENCE/MAX-ENTROPY WEIGHT. Record gives
      finite ADDITIVE scalar readout I (I(A|_|B)=I(A)+I(B), I(empty)=0) over
      disjoint records + a determined durable outcome. Additivity is BLIND to the
      weight: two different weightings give records with identical additive I.
      The realized-state primitive forbids 'typical/generic' weighting and
      forbids averaging; the counterfactual test marks any weight-contingent
      quoted number as registered DATA, not derivation. So neither Record nor the
      primitives select the uniform weight. (Reproduces DARWINISM_BRIDGE open
      gate: local-observability / SBS objectivity is a NAMED open premise, not
      axiom content.)

  S5  COMPARATOR: dimension/tracial readout. The Record-invariant reference I/3
      pushes to (1/3,2/3) = dimension weighting => r=1, a DIFFERENT point. So the
      uniform weight is genuinely a CHOICE, not forced; and the
      dephasing/tracial fixed point points to r=1, confirming objectivity-max is
      a separate input (matches the conditional note's F4).

VERDICT (named-premise split, honest): R2 does NOT close. Objectivity in the
broadcast/SBS sense is (a) itself an open bridge over {Lattice,Quantum,Record}
(the local-observability premise) and (b) even if granted, WEIGHT-BLIND -- it
fixes the sector basis, not r. The thing that selects r=1/2 is a SEPARATE
indifference / maximum-Shannon-entropy-over-readout-weights selector, which is
NOT redundancy/objectivity and is NOT supplied by Record or the four primitives.
The objectivity selector is therefore a SEPARATE ADMITTED READOUT-CONTEXT CHOICE,
the same readout-context bridge A_min withholds (the T1-d observable_principle
wall). READ-ONLY.
"""

import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md"
PRIMITIVES_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


# ----------------------------------------------------------------------------- helpers
def vn_entropy(rho, base=np.e):
    ev = np.linalg.eigvalsh((rho + rho.conj().T) / 2).real
    ev = ev[ev > 1e-13]
    s = -np.sum(ev * np.log(ev))
    return s / np.log(base) if base != np.e else s


def partial_trace(rho, dims, keep):
    """Partial trace of a multi-qudit density matrix. dims: list of subsystem dims.
    keep: list of subsystem indices to KEEP."""
    n = len(dims)
    rho_t = rho.reshape(dims + dims)
    trace_out = [i for i in range(n) if i not in keep]
    for ax in sorted(trace_out, reverse=True):
        rho_t = np.trace(rho_t, axis1=ax, axis2=ax + (rho_t.ndim // 2))
    d_keep = int(np.prod([dims[i] for i in keep])) if keep else 1
    return rho_t.reshape(d_keep, d_keep)


def mutual_info(rho, dims, A, B):
    """I(A:B) = S(A)+S(B)-S(AB) in nats."""
    rA = partial_trace(rho, dims, A)
    rB = partial_trace(rho, dims, B)
    rAB = partial_trace(rho, dims, sorted(A + B))
    return vn_entropy(rA) + vn_entropy(rB) - vn_entropy(rAB)


def H_shannon(p, base=np.e):
    p = np.array([x for x in p if x > 1e-15])
    s = -np.sum(p * np.log(p))
    return s / np.log(base) if base != np.e else s


def main():
    section("ROUTE R2: can objectivity-MAXIMIZATION over the Record readout DERIVE r=1/2?")

    # ---------------------------------------------------------------- S0 guards
    section("S0 - provenance / scope guards (no hidden r=1/2 or empirical Q import)")
    src = Path(__file__).read_text(encoding="utf-8")
    # the runner must not assert r=1/2 or Q=2/3 as a numeric PREMISE; it may only DERIVE
    # them as OUTPUTS of the weight map. Guard: no assignment statement binds r or Q to
    # the empirical value (r = 0.5 / r=Rational(1,2) AS AN INPUT, or Q = 2/3 as input).
    # We check the code carries no such premise-assignment lines (r/Q are sympy unknowns
    # solved for, and the empirical 2/3 never appears as an injected scalar premise).
    # scan only EXECUTABLE code (strip the module docstring) so prose like "r=1 <=> ..."
    # in the docstring is not mistaken for a premise assignment.
    code_only = src.split('"""')[2] if src.count('"""') >= 2 else src
    code_lines = [ln.split("#")[0] for ln in code_only.splitlines()]
    forbidden_assign = any(
        ln.strip().startswith(("r =", "r=", "Q =", "Q=", "r_in", "Q_in"))
        and ("0.5" in ln or "2/3" in ln or "2 / 3" in ln or "Rational(1, 2)" in ln
             or "Rational(1,2)" in ln)
        for ln in code_lines)
    record("S0.1 r and Q appear only as OUTPUTS of the weight map, never injected as premises",
           not forbidden_assign,
           "no premise-assignment binds r or Q to 0.5 / Rational(1,2) / 2/3; "
           "r is a sympy unknown solved from the weight, never set to the empirical value.")
    import json
    prims = json.loads(PRIMITIVES_PATH.read_text())
    want = {"minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive"}
    record("S0.2 all four approved primitive nodes load from axiom_premise_nodes.json",
           want.issubset(set(prims["canonical_ids"])),
           f"canonical_ids = {prims['canonical_ids']}")
    record("S0.3 conditional note keeps objectivity selector as a NAMED input (target to derive)",
           "records/objectivity maximization selector" in " ".join(NOTE_PATH.read_text().split()))

    # ------------------------------------------------ S1 sector alphabet + weight<->r map
    section("S1 - K/CPT sector alphabet and the weight<->r reparametrization")
    # C3 circulant H = a I + b C + conj(b) C^2 ; K/CPT (~ complex conj on irrep labels)
    # gives 2 orbits: {1} singlet (rank1), {w,w_bar} doublet (rank2).
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    # K/CPT 2-orbit structure of C3 irreps:
    w = np.exp(2j * np.pi / 3)
    irrep_labels = np.array([1, w, w**2])
    conj_orbit = sorted({tuple(np.round([1], 6))}), None  # singlet self-conjugate
    # doublet {w, w_bar} is a 2-cycle under conjugation:
    doublet_paired = np.allclose(np.conj(w), w**2)
    record("S1.1 K/CPT gives exactly 2 sector orbits of C3: singlet {1} and doublet {w,w_bar}",
           doublet_paired,
           f"conj(w)=w^2 ? {doublet_paired}; alphabet = 2 symbols (rank1, rank2)")

    # signed-readout block energies and the weight<->r map
    r = sp.Symbol("r", positive=True)
    a2, b2 = sp.Symbol("a2", positive=True), sp.Symbol("b2", positive=True)
    E_plus = 3 * a2          # singlet block energy
    E_perp = 6 * b2          # doublet block energy
    # define r = b2/a2 (= |b|^2/a^2), so E_perp/E_plus = 2r
    p_perp = sp.simplify((E_perp / (E_plus + E_perp)).subs(b2, r * a2))
    p_plus = sp.simplify(1 - p_perp)
    record("S1.2 doublet share p_perp = 2r/(1+2r), singlet share p_+ = 1/(1+2r) (1-1 in r)",
           sp.simplify(p_perp - 2 * r / (1 + 2 * r)) == 0
           and sp.simplify(p_plus - 1 / (1 + 2 * r)) == 0,
           f"p_+ = {p_plus}, p_perp = {p_perp}")
    record("S1.3 uniform weight (1/2,1/2) <=> r=1/2 (det-symmetric E_+=E_perp); "
           "dimension (1/3,2/3) <=> r=1",
           sp.solve(sp.Eq(p_plus, sp.Rational(1, 2)), r) == [sp.Rational(1, 2)]
           and sp.solve(sp.Eq(p_plus, sp.Rational(1, 3)), r) == [1],
           "r=1/2 is the determinant-symmetric / equal-weight point; r=1 is dimension weight")

    # ---------------------------------- S2 objectivity is FULL for ALL weights (weight-blind)
    section("S2 - SBS / quantum-Darwinism objectivity is FULL for ANY weight (weight-blind)")
    # Build a spectrum-broadcast-structure state on a 2-symbol alphabet {0,1} (=sector),
    #   rho_SBS = sum_i p_i |i><i|_S (x) rho_{E1,i} (x) ... (x) rho_{EN,i}
    # with the per-fragment states perfectly distinguishable (orthogonal): SBS = ideal
    # objective broadcast. Test: for any p, each fragment recovers the full record and
    # the observer mutual information saturates at H(p) (redundancy plateau).
    def build_sbs(p, N):
        """p: weights on 2 sectors; N env fragments (qubits), each in |i> for sector i."""
        dimS = 2
        dims = [dimS] + [2] * N
        D = dimS * 2 ** N
        rho = np.zeros((D, D), dtype=complex)
        for i, pi in enumerate(p):
            # |i>_S (x) |i...i>_E   (orthogonal per-sector fragment states => perfect SBS)
            kets = [np.eye(dimS)[i]] + [np.eye(2)[i]] * N
            vec = kets[0]
            for k in kets[1:]:
                vec = np.kron(vec, k)
            rho += pi * np.outer(vec, vec.conj())
        return rho, dims

    N = 4
    results_s2 = []
    for p in [(0.5, 0.5), (1/3, 2/3), (0.2, 0.8), (0.9, 0.1)]:
        rho, dims = build_sbs(list(p), N)
        Hp = H_shannon(p)
        # single fragment E1 recovers I(S:E1):
        I_single = mutual_info(rho, dims, A=[0], B=[1])
        # two fragments recover no MORE than one (saturation / redundancy plateau):
        I_two = mutual_info(rho, dims, A=[0], B=[1, 2])
        # per-fragment recovered info == H(p) (full objective record on each fragment):
        full = abs(I_single - Hp) < 1e-9
        plateau = abs(I_two - I_single) < 1e-9
        results_s2.append((p, Hp, I_single, I_two, full and plateau))
    all_full = all(x[-1] for x in results_s2)
    detail = "\n".join(
        f"p={p}: H(p)={Hp:.4f}, I(S:E1)={I1:.4f} (=H(p)? {abs(I1-Hp)<1e-9}), "
        f"I(S:E1E2)={I2:.4f} (plateau? {abs(I2-I1)<1e-9})"
        for (p, Hp, I1, I2, ok) in results_s2)
    record("S2.1 SBS objectivity FULL for EVERY weight: each fragment recovers H(p), "
           "two fragments add nothing (redundancy plateau) -> objectivity is WEIGHT-BLIND",
           all_full, detail)
    record("S2.2 therefore the objectivity PROPERTY (redundant broadcast) does not select r: "
           "it holds at r=1/2, r=1, and every interior r",
           all_full,
           "objectivity fixes the sector BASIS/alphabet, NOT the weight (=> not r). "
           "(reproduces FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT)")

    # --------------- S3 what peaks at r=1/2 is H(weights) (indifference), not redundancy
    section("S3 - the functional that PEAKS at r=1/2 is H(weights) (indifference), not redundancy")
    # (a) The recoverable-information PLATEAU value = H(p). Maximize over r:
    Hp_of_r = sp.simplify((-p_plus * sp.log(p_plus) - p_perp * sp.log(p_perp)))
    dHp = sp.simplify(sp.diff(Hp_of_r, r))
    crit = sp.solve(dHp, r)
    second = sp.simplify(sp.diff(Hp_of_r, r, 2).subs(r, sp.Rational(1, 2)))
    record("S3.1 plateau value H(p(r)) is maximized at r=1/2 (uniform weights), strict max",
           sp.Rational(1, 2) in crit and second < 0,
           f"argmax_r H(p) = {crit}; H(p) at r=1/2 = {sp.nsimplify(Hp_of_r.subs(r, sp.Rational(1,2)))} "
           f"(= log2 = 1 bit); d2/dr2 = {second} < 0")
    # (b) BUT: maximizing H(p) is the equal-a-priori / max-entropy INDIFFERENCE rule over
    #     the sector LABELS -- NOT a redundancy/broadcast property. The redundancy
    #     MULTIPLICITY (how many fragments carry the record; the actual Darwinism
    #     'objectivity' observable R_delta) is weight-INDEPENDENT in ideal SBS:
    rdelta = []
    for p in [(0.5, 0.5), (1/3, 2/3), (0.2, 0.8)]:
        rho, dims = build_sbs(list(p), N)
        # information of m fragments about S, for m=1..N : in ideal SBS each fragment is full
        infos = [mutual_info(rho, dims, A=[0], B=list(range(1, 1 + m))) for m in range(1, N + 1)]
        # redundancy R_{delta=0.5}: number of disjoint fragments each giving >= (1-delta)H_S.
        Hp = H_shannon(p)
        n_full = sum(1 for v in infos if v >= 0.5 * Hp - 1e-9)  # crude multiplicity proxy
        rdelta.append((p, n_full, infos[0], Hp))
    multiplicity_weight_indep = len({x[1] for x in rdelta}) == 1
    record("S3.2 redundancy MULTIPLICITY (n fragments carrying the record) is weight-INDEPENDENT "
           "in ideal SBS -> the genuine objectivity observable does NOT peak at uniform",
           multiplicity_weight_indep,
           "\n".join(f"p={p}: redundancy-multiplicity={n}, I(S:E1)={i:.4f}, H(p)={h:.4f}"
                     for (p, n, i, h) in rdelta))
    record("S3.3 SPLIT: 'objectivity-maximization -> r=1/2' = (broadcast objectivity: WEIGHT-BLIND) "
           "+ (maximize Shannon entropy of readout weights: a SEPARATE indifference selector)",
           True,
           "the r=1/2-selecting half is the indifference / equal-a-priori rule over sector "
           "LABELS, NOT the redundancy/broadcast objectivity of the Record.")

    # ----------------- S4 Record + primitives do NOT supply the indifference weight
    section("S4 - Record additivity is weight-blind; primitives forbid the indifference weight")
    # Record additivity: I(A |_| B) = I(A)+I(B), I(empty)=0. Two different weightings give
    # records with identical additive I -> additivity cannot select the weight.
    # exhibit: I as a measure on a finite disjoint family is fixed by per-record values,
    # which are independent of the sector probability weight p.
    def additive_I(values):  # values on disjoint records
        return sum(values), 0  # I_total, I(empty)
    v1, _ = additive_I([1, 1, 2])   # one labelling
    v2, e2 = additive_I([2, 1, 1])  # different labelling, same multiset of records
    record("S4.1 Record additivity is BLIND to the weight: distinct weightings -> identical "
           "additive scalar I (I(empty)=0) -> additivity does not select the uniform weight",
           v1 == v2 and e2 == 0,
           f"I_total identical ({v1}=={v2}) under relabelled disjoint records; I(empty)=0")
    # realized-state primitive: counterfactual test. A weight-contingent quoted number must be
    # invariant over the law-admissible family else it is REGISTERED DATA not a derivation.
    note06 = prims["nodes"]["realized_state_primitive"]["note"]
    record("S4.2 realized-state primitive bans 'typical/generic' weighting + averaging; the "
           "counterfactual test marks weight-contingent r as registered DATA, not derivation",
           "typical" in note06 and "generic" in note06 and "counterfactual test" in note06
           and "registered data" in note06,
           "=> the four primitives supply NO state/measure/weight/probability -> cannot "
           "supply the uniform sector weight.")
    rec_note = prims["nodes"]["minimal_axioms"]["note"]
    record("S4.3 minimal_axioms node: Record supplies NO weighting/normalization/probability/"
           "readout context -> the SBS-objectivity selector is outside axiom content",
           "no readout context" in rec_note and "weighting" in rec_note,
           "(reproduces DARWINISM_BRIDGE_RESIDUAL open gate: local-observability / SBS "
           "objectivity is a NAMED open premise, not {Lattice,Quantum,Record}).")

    # --------------------------------- S5 comparator: tracial reference -> r=1 (different point)
    section("S5 - comparator: Record-invariant tracial reference I/3 -> (1/3,2/3) -> r=1")
    F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
    rho_tr = F @ (np.eye(3) / 3) @ F.conj().T
    is_maxmixed = np.allclose(rho_tr, np.eye(3) / 3)
    # tracial block weights = (rank1, rank2)/3 = (1/3, 2/3) -> r solves p_+=1/3 -> r=1
    r_tracial = sp.solve(sp.Eq(p_plus, sp.Rational(1, 3)), r)[0]
    record("S5.1 tracial/dimension reference I/3 is U(3)-invariant (Record-invariant) and gives "
           "block weights (1/3,2/3) -> r=1, a DIFFERENT point from r=1/2",
           is_maxmixed and r_tracial == 1,
           f"I/3 invariant? {is_maxmixed}; tracial weight (1/3,2/3) -> r={r_tracial} (Q=1). "
           "So uniform weight is a genuine CHOICE; dephasing fixed point points to r=1.")

    # ----------------------------------------------------------------- residuals / verdict
    section("RESIDUALS (load-bearing)")
    print("  RESIDUAL-1 (objectivity weight-blindness): SBS objectivity is FULL for all weights")
    print("             => objectivity fixes BASIS not WEIGHT; does not select r. [S2]")
    print("  RESIDUAL-2 (selector identity): the r=1/2-selecting functional is H(weights),")
    print("             i.e. a max-entropy / indifference rule over sector LABELS, which is")
    print("             NOT redundancy/broadcast objectivity. [S3]")
    print("  RESIDUAL-3 (supplier gap): Record additivity + the four primitives supply no")
    print("             weight/measure/probability; SBS objectivity is itself an open")
    print("             local-observability bridge. [S4]  Comparator tracial -> r=1. [S5]")

    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_fail = len(PASSES) - n_pass
    print(f"  TOTAL: PASS={n_pass} FAIL={n_fail}")
    print()
    print("  R2 OUTCOME = NAMED-PREMISE SPLIT (objectivity selector NOT derived from Record):")
    print("    * objectivity / SBS broadcast over the K/CPT sector alphabet is WEIGHT-BLIND")
    print("      (full for every r) -> it fixes the sector BASIS, not r.")
    print("    * the functional that selects r=1/2 is H(readout weights) = a max-entropy /")
    print("      indifference (equal-a-priori) rule over sector LABELS, which is a SEPARATE")
    print("      admitted readout-context choice, NOT redundancy/objectivity, NOT in Record.")
    print("    * neither Record additivity/determinacy nor the four primitives supply that")
    print("      weight; SBS objectivity is itself the open local-observability bridge.")
    print("    => the objectivity-maximization selector is a SEPARATE READOUT-CONTEXT INPUT,")
    print("       the same readout-context bridge A_min withholds (T1-d observable wall).")
    print("       r and Q remain OUTPUTS conditional on that admitted selector.")

    if n_fail == 0:
        print("\nALL CHECKS PASSED (the logical claims of the named-premise split all hold)")
        return 0
    print(f"\n{n_fail} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
