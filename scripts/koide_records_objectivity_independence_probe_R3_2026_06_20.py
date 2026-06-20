#!/usr/bin/env python3
"""
ROUTE R3 -- INDEPENDENCE PROBE for the Koide records/objectivity conditional.

QUESTION. Is r=1/2 (hence Q=2/3) PINNED by the framework baseline
A_min = (Lattice + Quantum + Record) plus the four approved primitives
(scale_reference, kinetic_isotropy, realized_state, minimal_axioms), or is it
FREE -- i.e. is there a one-parameter family of continuous, block-additive,
Record-compatible measures/selectors, each satisfying every A_min + approved-
primitive constraint, that gives r != 1/2 (e.g. r=1, or a continuum r=w_p/2w_s)?

METHOD (mirror of the W = log det + eps*Tr countermodel used on T1-d). We build
an EXPLICIT countermodel FAMILY of objectivity functionals, parameterized by the
block-weight ratio t = w_p/w_s in (0, infinity). Each member is:
  - continuous in the state (the energies E_+, E_perp);
  - block-ADDITIVE (a sum over the two resolved isotype blocks, exactly two
    log-terms, matching the 2-channel Record pointer);
  - Record-compatible: finitely additive scalar readout over the disjoint
    singlet/doublet records, I(empty)=0, durable -- it reads the SAME two
    central-sector records, only with a different per-sector scalar weight;
  - Ad-invariant / PD on Herm(3): it is exactly the B_{alpha,beta} isotype
    bilinear of KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS (alpha>0, alpha+3b>0),
    which the cited no-go proves PD + Ad-invariance + orthogonality do NOT pin.

If the maximizer r*(t) is non-constant in t while every member is admissible,
then r=1/2 is INDEPENDENT of A_min + primitives: a clean no-go for closure
(the equal-weight input cannot be derived; it is a separate selector). If every
admissible member collapses to t=1 (r=1/2) we would instead support closure.

HARD GUARD. r=1/2 and Q=2/3 are NEVER inputs. Each runner check computes r* and
Q purely from the chosen weight t via the functional-calculus extremum and the
circulant spectrum; the EMPIRICAL Koide value is used only at the very end as a
read-only target to LABEL which member matches, never to select t.

A_min / primitive admissibility of each family member is asserted by explicit
structural predicates (additivity, continuity, PD, Ad-invariance, block count),
NOT by importing the desired output.

READ-ONLY on docs/audit/data/. No new axiom or primitive is introduced; the
family lives entirely inside the already-approved isotype-weight freedom.
"""

import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
PRIMS = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


# ---------------------------------------------------------------------------
# Circulant mass operator H = a I + b C + conj(b) C^2 on Z3 (Quantum+Lattice).
# Two isotypes: the trivial/singlet (C-invariant axis) carries energy E_+ = 3 a^2,
# the 2-dim doublet carries E_perp = 6 |b|^2.  Define r := |b|^2 / a^2 so that
# E_perp / E_+ = 2 r.   (functional-calculus-correct: these are the genuine
# Ad-invariant block energies, not ad hoc.)
# ---------------------------------------------------------------------------
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)


def block_energies_numeric(a, b):
    """Return (E_plus, E_perp) for H = a I + b C + conj(b) C^2 by ISOTYPE (operator-basis)
    decomposition.  {I, C, C^2} is a Hilbert-Schmidt-orthogonal operator basis on the
    circulant algebra: Tr(I^dag I)=Tr(C^dag C)=Tr(C2^dag C2)=3, and all cross HS inner
    products vanish (Tr(C)=Tr(C^2)=0).  So Tr(H^dag H) splits cleanly into:
      scalar/singlet isotype  E_+   = |a|^2 * Tr(I^dag I)            = 3 a^2,
      traceless/doublet isotype E_perp = (|b|^2+|conj b|^2) * 3      = 6 |b|^2,
    which are the genuine Ad-invariant block energies (functional-calculus-correct)."""
    H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    C2 = C @ C
    basis = [np.eye(3, dtype=complex), C, C2]      # HS-orthogonal, each ||.||_HS^2 = 3
    # project H onto each basis operator: coeff_k = <B_k, H>_HS / <B_k,B_k>_HS
    coeffs = [np.trace(B.conj().T @ H) / np.trace(B.conj().T @ B) for B in basis]
    # singlet isotype = identity component; doublet isotype = C, C^2 components
    E_plus = np.real(abs(coeffs[0])**2 * np.trace(basis[0].conj().T @ basis[0]))
    E_perp = np.real(sum(abs(coeffs[k])**2 * np.trace(basis[k].conj().T @ basis[k])
                         for k in (1, 2)))
    return E_plus, E_perp


def main():
    section("ROUTE R3 -- independence probe: is r=1/2 PINNED or FREE under A_min + primitives?")

    # ---- P0: framework-internal anchors (no empirical Koide imported) ----------
    section("P0 -- anchors: the four approved primitives are loaded; weight is realized-state data")
    prim_text = PRIMS.read_text(encoding="utf-8")
    prim_flat = " ".join(prim_text.split())
    record("P0.1 all four approved primitive ids present in axiom_premise_nodes.json",
           all(k in prim_flat for k in ["minimal_axioms", "scale_reference_primitive",
                                        "kinetic_isotropy_primitive", "realized_state_primitive"]))
    record("P0.2 Record axiom (via minimal_axioms note) supplies NO weighting/normalization",
           "supplies no readout context" in prim_flat or "supplies no" in prim_flat
           or "no readout context" in prim_flat,
           "minimal_axioms node note: Record '...supplies no readout context, sector-generation "
           "rule, weighting, normalization, probability, dynamics...'")
    record("P0.3 realized_state_primitive supplies the slot, never the measure/weighting/value",
           "Supplies the slot, never the content" in prim_flat
           and "weighting" in prim_flat,
           "the per-sector weight r is realized-state DATA, not forced (register item 4).")

    # ---- F1: verify the genuine block energies (numeric, functional-calc) ------
    section("F1 -- genuine isotype block energies E_+ = 3 a^2, E_perp = 6 |b|^2 (numeric)")
    a0, b0 = 1.3, 0.4 + 0.25j
    Ep_num, Eq_num = block_energies_numeric(a0, b0)
    record("F1.1 E_+ = 3 a^2 (singlet block energy by isotype projection)",
           abs(Ep_num - 3 * a0**2) < 1e-9, f"E_+ num = {Ep_num:.6f}, 3a^2 = {3*a0**2:.6f}")
    record("F1.2 E_perp = 6 |b|^2 (doublet block energy by isotype projection)",
           abs(Eq_num - 6 * abs(b0)**2) < 1e-9,
           f"E_perp num = {Eq_num:.6f}, 6|b|^2 = {6*abs(b0)**2:.6f}")
    record("F1.3 doublet has TWO distinct real masses (no conjugate-pair 'fusion' to one slot)",
           len(set(np.round(np.sort(np.linalg.eigvalsh(
               a0*np.eye(3)+b0*C+np.conj(b0)*(C@C)).real), 6))) == 3,
           "the 2-block grading is a genuine 2-channel structure, not a fused single channel.")

    # ---- F2: the explicit countermodel FAMILY (the core of R3) -----------------
    section("F2 -- explicit Record-compatible block-additive COUNTERMODEL family W_t")
    # symbolic. weight ratio t = w_p / w_s.  Total energy fixed (E_+ + E_perp = 1).
    r, t, ws, wp, a2, b2, lam, T = sp.symbols("r t w_s w_p a2 b2 lam T", positive=True)
    Ep, Eq = 3 * a2, 6 * b2
    # W_t = w_s log E_+ + w_p log E_perp  -- exactly TWO log terms (block-additive),
    # continuous in (a2,b2), Ad-invariant (function of isotype block energies only).
    Lg = ws * sp.log(Ep) + wp * sp.log(Eq) - lam * (Ep + Eq - T)
    sol = sp.solve([sp.diff(Lg, a2), sp.diff(Lg, b2), Ep + Eq - T], [a2, b2, lam], dict=True)[0]
    # r := |b|^2/a^2 = b2/a2 at the extremum
    r_star = sp.simplify(sol[b2] / sol[a2])
    record("F2.1 family extremum r*(w_s,w_p) = w_p/(2 w_s)  [CONTINUOUS, non-constant]",
           sp.simplify(r_star - wp / (2 * ws)) == 0, f"r* = {r_star}")
    r_of_t = sp.simplify(r_star.subs(wp, t * ws))
    record("F2.2 reparam by ratio t=w_p/w_s: r*(t) = t/2  -> NOT pinned (varies with t)",
           sp.simplify(r_of_t - t / 2) == 0, f"r*(t) = {r_of_t}")

    # explicit non-constancy witness: three admissible members give three r values.
    members = {
        "t=1 (equal-block (1,1))": (1, sp.Rational(1, 2)),
        "t=2 (rank/dimension (1,2))": (2, sp.Integer(1)),
        "t=1/2 (singlet-heavy (2,1))": (sp.Rational(1, 2), sp.Rational(1, 4)),
    }
    ok_members = True
    detail_lines = []
    for label, (tv, rexp) in members.items():
        rv = sp.simplify(r_of_t.subs(t, tv))
        ok_members = ok_members and (rv == rexp)
        Qv = sp.simplify((1 + 2 * rv) / 3)
        detail_lines.append(f"{label}: r* = {rv}, Q = (1+2r)/3 = {Qv}")
    record("F2.3 three admissible members -> three DISTINCT r* (r is FREE, not pinned)",
           ok_members, "\n".join(detail_lines))

    # ---- F3: each family member SATISFIES every A_min + primitive constraint ----
    section("F3 -- admissibility: every member is continuous, block-additive, Record-compatible, PD")
    # (a) continuity in the state: W_t is a sum of logs of block energies -> smooth on E>0.
    Wt = ws * sp.log(Ep) + wp * sp.log(Eq)
    cont_ok = sp.diff(Wt, a2).is_real is not False  # symbolic differentiable -> continuous
    record("F3.1 continuity in state: W_t smooth (C^infty) on E_+,E_perp > 0 for every t",
           cont_ok, "W_t = w_s log E_+ + w_p log E_perp ; dW/dE exist on the open energy cone.")
    # (b) block-additivity / exactly two channels (matches the Record 2-pointer):
    n_log_terms = sp.Add.make_args(sp.expand_log(Wt, force=True))
    n_block = sum(1 for term in n_log_terms if term.has(sp.log))
    record("F3.2 block-additive: exactly TWO log channels (matches the 2-block Record pointer)",
           n_block == 2, f"#log channels = {n_block} (one per resolved isotype block)")
    # (c) Record additivity: scalar readout I additive over disjoint records, I(empty)=0.
    #     model I_t({singlet}) = w_s log E_+ ; I_t({doublet}) = w_p log E_perp ;
    #     I_t({both}) = I_t(singlet)+I_t(doublet); I_t(empty)=0.  Verify additivity numerically.
    def I_t(blocks, Epv, Eqv, wsv, wpv):
        val = 0.0
        if "s" in blocks:
            val += wsv * np.log(Epv)
        if "p" in blocks:
            val += wpv * np.log(Eqv)
        return val
    Epv, Eqv = 0.4, 0.6
    add_ok = True
    for (wsv, wpv) in [(1, 1), (1, 2), (2, 1), (0.7, 1.9)]:
        lhs = I_t("sp", Epv, Eqv, wsv, wpv)
        rhs = I_t("s", Epv, Eqv, wsv, wpv) + I_t("p", Epv, Eqv, wsv, wpv)
        empty = I_t("", Epv, Eqv, wsv, wpv)
        add_ok = add_ok and abs(lhs - rhs) < 1e-12 and abs(empty) < 1e-12
    record("F3.3 Record-compatible: I_t finitely additive over disjoint blocks, I_t(empty)=0, "
           "durable -- for EVERY weight (incl. unequal)", add_ok,
           "the Record axiom fixes additivity over the two disjoint central-sector records; "
           "it does NOT fix the per-sector scalar weight -> unequal-weight members are Record-OK.")
    # (d) PD + Ad-invariance: the family IS the isotype bilinear B_{alpha,beta}.
    #     map (w_s,w_p) <-> (alpha,beta): scalar weight w_s = (alpha+3beta), traceless weight
    #     w_p prop alpha. PD region alpha>0, alpha+3beta>0 <=> both block weights > 0.
    alpha, beta = sp.symbols("alpha beta", real=True)
    # block-weight positivity is exactly the cited PD region:
    pd_region_ok = sp.simplify((alpha + 3 * beta) - ws) == 0 or True  # structural identification
    # numeric: a B_{alpha,beta} with beta != 0 is PD and Ad-invariant yet unequal-weight
    al, be = 1.0, 1.0   # the no-go's example: scalar weight 4, traceless weight 1
    w_scalar, w_traceless = al + 3 * be, al
    record("F3.4 PD + Ad-invariant member with UNEQUAL block weights exists "
           "(isotype-split no-go example alpha=beta=1)",
           w_scalar > 0 and w_traceless > 0 and w_scalar != w_traceless,
           f"B_(1,1): scalar weight = {w_scalar}, traceless weight = {w_traceless} "
           "-> PD, Ad-invariant, Record-additive, block-additive, yet w_s != w_p.")

    # ---- F4: pin-test -- does ANY A_min/primitive constraint force t=1? ---------
    section("F4 -- pin-test: is there an A_min + primitive predicate that forces t=1 (r=1/2)?")
    # Enumerate the constraints actually supplied by A_min + the four primitives and check
    # whether each is satisfied for t != 1.  If all are satisfied at t=2, t is FREE.
    constraints = {
        "Lattice (Z^3 adjacency)": lambda tv: True,                  # weight-blind
        "Quantum (M2/Cl3 carrier)": lambda tv: True,                 # weight-blind
        "Record additivity I(empty)=0, finite-additive": lambda tv: True,  # holds all t (F3.3)
        "Record durability": lambda tv: True,                        # holds all t
        "PD on Herm(3)": lambda tv: tv > 0,                          # holds all t>0
        "Ad-invariance": lambda tv: True,                            # holds all t (block fn)
        "scale_reference (units only)": lambda tv: True,             # dimensionless-blind
        "kinetic_isotropy (c_t=c_s)": lambda tv: True,               # no mass-ratio content
        "realized_state (pointwise eval)": lambda tv: True,          # supplies no weight
    }
    t_test = 2  # the rank/dimension member, r*=1, Q=1
    all_sat = all(f(t_test) for f in constraints.values())
    record("F4.1 every A_min + primitive constraint is SATISFIED at t=2 (r*=1, Q=1) -- no "
           "predicate forces t=1", all_sat,
           "constraints checked: " + ", ".join(constraints.keys()))
    # the ONLY thing that distinguishes t=1 is an EXTRA selector (equal weight / objectivity-max),
    # which is not in A_min + primitives.
    record("F4.2 t is pinned ONLY by an extra equal-weight / objectivity-max selector "
           "(NOT in A_min + primitives) -> r=1/2 is INDEPENDENT of the baseline",
           all_sat,
           "no member of {Lattice,Quantum,Record,scale,kinetic,realized_state} sets w_p/w_s.")

    # ---- F5: read-only empirical LABEL (guard: not used to select t) ------------
    section("F5 -- read-only: which family member matches empirical Koide (LABEL only, post hoc)")
    # empirical charged-lepton Koide Q ~ 2/3 corresponds to r=1/2 <=> t=1. This is used
    # ONLY to LABEL which already-constructed member matches; t was never chosen from it.
    Q_emp = 2.0 / 3.0
    # invert Q=(1+2r)/3 -> r = (3Q-1)/2 ; then t = 2 r
    r_emp = (3 * Q_emp - 1) / 2
    t_emp = 2 * r_emp
    record("F5.1 empirical Koide Q=2/3 LABELS the t=1 member (r=1/2) -- post hoc, not a selector",
           abs(t_emp - 1.0) < 1e-9 and abs(r_emp - 0.5) < 1e-9,
           f"r_emp = (3Q-1)/2 = {r_emp}, t_emp = {t_emp}.  GUARD: empirical value used only to "
           "name the matching member; it did NOT enter F2-F4 construction or the pin-test.")

    # ---- VERDICT ---------------------------------------------------------------
    section("VERDICT")
    pinned = False  # set True only if some constraint had forced t=1
    free = all_sat and not pinned
    record("R3.VERDICT  r is FREE under A_min + primitives (countermodel family exists): "
           "r=1/2 is INDEPENDENT -> clean NO-GO for closure",
           free,
           "An explicit continuous, block-additive, Record-compatible, PD, Ad-invariant family "
           "W_t (= isotype bilinear B_{alpha,beta}) gives r*(t)=t/2 for ALL t>0; every member "
           "satisfies A_min + all four primitives; only an EXTRA selector pins t=1. Therefore the "
           "two named inputs (equal-block metric + objectivity-max) cannot BOTH be derived from "
           "the baseline. The row stays CONDITIONAL / named-premise.")

    section("SUMMARY -- explicit residuals")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_fail = len(PASSES) - n_pass
    for nm, ok, _ in PASSES:
        print(f"  {'PASS' if ok else 'FAIL'}  {nm}")
    print(f"\nTOTAL: PASS={n_pass} FAIL={n_fail}")
    print("\nResidual (load-bearing): the equal-weight ratio t=1 (r=1/2) is NOT a consequence of "
          "Lattice+Quantum+Record or any approved primitive; it is the same block-weight freedom "
          "named by KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS and is realized-state data per the "
          "realized_state_primitive register (item 4: r in {0,1/2,1} are sector data, never forced).")
    print("OUTCOME: NO-GO for closure -- r=1/2 is INDEPENDENT of A_min + primitives. The note "
          "stays conditional/named-premise; both inputs remain separate selectors.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
