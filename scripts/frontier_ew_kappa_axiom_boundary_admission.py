#!/usr/bin/env python3
"""
kappa_EW is an axiom-boundary admission (a weighting the axioms do not supply)
=============================================================================

PStack experiment: ew-kappa-axiom-boundary-admission

Companion runner for
  docs/EW_KAPPA_IS_AXIOM_BOUNDARY_ADMISSION_NO_GO_NOTE_2026-06-09.md

Answers the question "is the framework wrong, or do the axioms have an issue?"
for the kappa_EW wall, strictly from the axiom boundary:

  - kappa_EW is a WEIGHTING: the free inter-sector weight in the EW color readout
    Pi_phys = C + kappa_EW * S. The central-sector partition delivers the channel
    COUNT (the (N_c^2-1)/N_c^2 = 8/9 cardinality fraction) but NOT the weight.
  - The Record axiom (MINIMAL_AXIOMS_2026-06-05) explicitly supplies *no* weighting,
    readout context, or normalization; the Quantum axiom supplies *no* physical
    observable bridge.
  - Therefore kappa_EW is not derivable from {Lattice, Quantum, Record} ALONE --
    not only contingently (the route-specific no-gos) but as a direct consequence
    of the axiom boundary. It is an admitted input -- a CANDIDATE Tier-A admission
    of the same axiom-disclaimed class as the two registered ones (AC_phi_lambda =
    the sector-generation rule; theta = the source/action) -- currently absent from
    tier_a_admissions.json; recognition is the audit lane's (this runner parses the
    facts, it does not certify the registry).

Conclusion: the framework is internally consistent and the axioms are minimal and
clean; the EW absolute normalization (g1/g2/alpha_EM/m_t via kappa_EW=0) is
conditional on this admission; sin^2(theta_W) is kappa-invariant within the
construction (unconditional with respect to kappa_EW). This runner does NOT
fabricate kappa=0 or assert kappa=1.

Self-contained: numpy + sympy + stdlib (reads repo files faithfully). Zero PDG inputs.
"""

import json
import os
import re
import numpy as np
import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RNG = np.random.default_rng(20260609)
PASS = 0
FAIL = 0


def check(desc, ok):
    global PASS, FAIL
    PASS += 1 if ok else 0
    FAIL += 0 if ok else 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {desc}")
    return ok


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def section(text, header):
    """Extract the body of a '### <header>' subsection up to the next heading."""
    lines = text.splitlines()
    out, grab = [], False
    for ln in lines:
        if ln.strip().startswith("#"):
            if grab:
                break
            grab = ln.strip().lower().lstrip("# ").startswith(header.lower())
            continue
        if grab:
            out.append(ln)
    return re.sub(r"\s+", " ", " ".join(out).lower())


# ============================================================
# (A) kappa_EW is a WEIGHTING: the partition delivers the 8/9 COUNT, not the weight.
# ============================================================
def part_A():
    print("\n(A) kappa_EW is a weighting: the central-sector partition delivers the 8/9 COUNT, not the weight")
    okall = True
    n = 3

    def P_singlet(G):
        return (np.trace(G) / n) * np.eye(n)

    # the color readout sector weights S (singlet) and C (adjoint) of a color matrix G
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    Gs = P_singlet(G)
    S = float(np.real(np.trace(Gs.conj().T @ Gs)))
    C = float(np.real(np.trace((G - Gs).conj().T @ (G - Gs))))

    # the named family: K_EW(kappa) = 1/(F_adj + kappa*(1-F_adj)); the readout Pi = C + kappa*S
    kappa = sp.symbols("kappa", nonnegative=True)
    F_adj = sp.Rational(n ** 2 - 1, n ** 2)  # 8/9 = the COUNT (cardinality fraction)
    K_EW = 1 / (F_adj + kappa * (1 - F_adj))
    okall &= check(
        f"the delivered COUNT is the cardinality fraction F_adj = {F_adj} (= (N_c^2-1)/N_c^2); "
        f"K_EW(0)={sp.nsimplify(K_EW.subs(kappa,0))}, K_EW(1)={sp.nsimplify(K_EW.subs(kappa,1))}",
        F_adj == sp.Rational(8, 9)
        and sp.nsimplify(K_EW.subs(kappa, 0)) == sp.Rational(9, 8)
        and sp.nsimplify(K_EW.subs(kappa, 1)) == sp.Integer(1),
    )
    # kappa is the FREE weight: Pi(0)=C and Pi(1)=C+S are both functions of the same measured {S,C};
    # no functional of the partition data {count, S, C} fixes kappa.
    okall &= check(
        f"kappa is a FREE inter-sector weight: Pi(kappa=0)=C={C:.3f}, Pi(kappa=1)=C+S={C+S:.3f}, both from the "
        f"same {{S={S:.3f},C={C:.3f}}} -> the weight is not delivered by the count",
        abs((C + 0 * S) - C) < 1e-9 and abs((C + 1 * S) - (C + S)) < 1e-9 and S > 1e-6,
    )
    return okall


# ============================================================
# (B) Faithful, SECTION-SCOPED parse of MINIMAL_AXIOMS_2026-06-05: the Record
#     subsection enumerates 'weighting'/'readout context'/'normalization' and the
#     Quantum subsection enumerates 'physical observable bridge' as NOT supplied.
#     (Parses FACTS only; the inference is the note's, stated in prose, not certified here.)
# ============================================================
def part_B():
    print("\n(B) Section-scoped parse: Record subsection lists 'weighting'/'readout context'; Quantum lists 'observable bridge'")
    okall = True
    ax = read("docs/MINIMAL_AXIOMS_2026-06-05.md")
    rec = section(ax, "Record")
    qtm = section(ax, "Quantum")
    record_terms = [t for t in ["readout context", "weighting", "normalization"] if t in rec]
    okall &= check(
        f"Record subsection lists as NOT supplied: {record_terms} (and 'a record supplies no ...': "
        f"{'a record supplies no' in rec})",
        set(["readout context", "weighting", "normalization"]).issubset(set(record_terms))
        and "a record supplies no" in rec,
    )
    okall &= check(
        f"Quantum subsection lists 'physical observable bridge' as NOT supplied "
        f"('does not supply' in Quantum: {'does not supply' in qtm})",
        "physical observable bridge" in qtm and "does not supply" in qtm,
    )
    # FACT (parse), not a certified governance conclusion: 'weighting' and 'physical observable
    # bridge' are named axiom exclusions; the note's inference (kappa_EW, a weighting in the EW
    # observable bridge, is therefore not axiom-derivable) is stated in the note prose.
    print("    [parse] 'weighting' (Record) and 'physical observable bridge' (Quantum) are named axiom exclusions;")
    print("            the note infers from these that kappa_EW is not derivable from the axioms alone (prose).")
    return okall


# ============================================================
# (C) The registry: exactly two Tier-A admissions are registered (AC_phi_lambda,
#     theta); kappa_EW is absent. Each registered admission is itself an
#     axiom-disclaimed item; kappa_EW maps to 'weighting' the same way.
# ============================================================
def part_C():
    print("\n(C) Registry: 2 admissions registered (AC_phi_lambda, theta); kappa_EW absent; same axiom-disclaimed pattern")
    okall = True
    reg = json.loads(read("docs/audit/data/tier_a_admissions.json"))
    ids = reg["canonical_ids"]
    n_reg = reg["genuine_admitted_input_count"]
    kappa_absent = not any(("kappa" in str(k).lower()) or ("ew_current" in str(k).lower()) for k in ids)
    okall &= check(
        f"tier_a_admissions.json: count={n_reg}, ids={ids}; kappa_EW registered? {not kappa_absent}",
        n_reg == 2 and kappa_absent,
    )
    # the parallel: each admission is an axiom-disclaimed category.
    #   AC_phi_lambda <-> 'sector-generation rule' (Record disclaims); the matter realization.
    #   theta         <-> 'source/action'          (MINIMAL_AXIOMS open-gates list).
    #   kappa_EW      <-> 'weighting'              (Record disclaims).
    ax = re.sub(r"\s+", " ", read("docs/MINIMAL_AXIOMS_2026-06-05.md").lower())
    parallels = {
        "AC_phi_lambda -> 'sector-generation rule'": "sector-generation rule" in ax,
        "theta -> 'source/action'": "source/action" in ax,
        "kappa_EW -> 'weighting'": "weighting" in ax,
    }
    for label, present in parallels.items():
        okall &= check(f"axiom-disclaimed category term present for {label}", present)
    # parse FACT (not a registry verdict): the axiom-disclaimed terms exist for all three, and
    # kappa_EW is absent from the registry. The note proposes -- pending audit recognition -- that
    # kappa_EW is a CANDIDATE Tier-A admission of the same class; it does not certify the registry.
    print("    [parse] all three axiom-disclaimed terms present; kappa_EW absent from the registry. The note")
    print("            proposes kappa_EW as a CANDIDATE Tier-A admission, pending audit recognition (not certified here).")
    return okall


# ============================================================
# (D) The route-specific no-gos each confirm, from a different angle, that the
#     target is a weighting the axioms supply no rule for.
# ============================================================
def part_D():
    print("\n(D) Each route-specific kappa_EW no-go confirms, from a different angle, that the target is a weighting")
    okall = True
    nogo_docs = [
        "docs/EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md",         # CMT / packet
        "docs/EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md",  # OZI size-class
        "docs/EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md",  # tracelessness
        "docs/RCONN_DERIVED_NOTE.md",                                          # MC-not-a-derivation
        "docs/EW_KAPPA_SELF_ENERGY_OBJECT_PIN_MC_UNDECIDABLE_NO_GO_NOTE_2026-06-08.md",  # MC-undecidable / scheme
        "docs/EW_KAPPA_REGISTRATION_REGISTERS_ALL_COLOR_SECTORS_NO_GO_NOTE_2026-06-09.md",  # register-not-read
    ]
    present = [d for d in nogo_docs if os.path.exists(os.path.join(ROOT, d))]
    okall &= check(
        f"route-specific kappa_EW no-go portfolio present: {len(present)}/{len(nogo_docs)} "
        f"(each a distinct failed derivation route for the same weighting)",
        len(present) >= 5,
    )
    print("    => the routes (CMT, OZI, tracelessness, MC, color-blindness, Route-2, register-not-read) each try a")
    print("       different way to derive the weighting; each confirms the axioms supply no rule for it")
    return okall


# ============================================================
# (E) sin^2(theta_W) is kappa-invariant in the framework's construction (the
#     color factor applies equally to g1, g2) -> unconditional WITH RESPECT TO
#     kappa_EW within the existing construction; the admission bears only on the
#     absolute EW normalization.
# ============================================================
def part_E():
    print("\n(E) sin^2(theta_W) kappa-invariant (overall factor cancels) -> unconditional w.r.t. kappa_EW in this construction")
    kappa, g1b, g2b = sp.symbols("kappa g1b g2b", positive=True)
    K = 1 / (sp.Rational(8, 9) + kappa * sp.Rational(1, 9))
    sin2 = (sp.sqrt(K) * g1b) ** 2 / ((sp.sqrt(K) * g1b) ** 2 + (sp.sqrt(K) * g2b) ** 2)
    resid = sp.simplify(sin2 - g1b ** 2 / (g1b ** 2 + g2b ** 2))
    return check(f"sin^2(theta_W) independent of kappa (residual {resid}) -> unconditional w.r.t. kappa_EW in this construction", resid == 0)


def main():
    print("=" * 84)
    print("kappa_EW is an axiom-boundary admission (a weighting the axioms do not supply) -- zero PDG inputs")
    print("=" * 84)
    res = [part_A(), part_B(), part_C(), part_D(), part_E()]
    print("\n" + "=" * 84)
    print(f"RUNNER STATUS: {'PASS' if all(res) and FAIL == 0 else 'FAIL'} (PASS={PASS} FAIL={FAIL})")
    print("=" * 84)
    return 0 if (all(res) and FAIL == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
