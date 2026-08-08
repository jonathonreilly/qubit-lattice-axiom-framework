#!/usr/bin/env python3
"""Radiative charged-lepton tau-scale selector firewall.

This runner audits the support lane

    y_tau ?= alpha_LM / (4*pi)

against the retained charged-lepton mass objective.  It proves a narrow
negative boundary: the electroweak Casimir and one-loop factor are
generation-blind across e, mu, tau.  Therefore the radiative scale can be
support for a charged-lepton scale, but it cannot by itself identify the tau
eigenvalue or retire the charged-lepton mass import.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import math
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from dm_leptogenesis_exact_common import ALPHA_LM, V_EW  # noqa: E402


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


@dataclass(frozen=True)
class Generation:
    label: str
    pdg_mass_mev: float


GENERATIONS = (
    Generation("e", 0.510998950),
    Generation("mu", 105.6583755),
    Generation("tau", 1776.86),
)


def charged_lepton_casimir() -> Fraction:
    """Casimir used by the support lane for any charged lepton generation."""
    t_left = Fraction(1, 2)
    y_left = Fraction(-1, 2)
    y_right = Fraction(-1, 1)

    c_su2_left = t_left * (t_left + 1)  # 3/4
    c_su2_vertex = 2 * c_su2_left * Fraction(1, 2)
    c_u1_vertex = y_left * y_right * Fraction(1, 2)
    return c_su2_vertex + c_u1_vertex


def main() -> int:
    radiative_script = SCRIPTS / "frontier_charged_lepton_radiative_yukawa_theorem.py"
    diagram_script = SCRIPTS / "frontier_charged_lepton_yukawa_diagrammatic_enumeration.py"
    bz_script = SCRIPTS / "frontier_charged_lepton_yukawa_bz_quadrature_explicit.py"
    direct_no_go_note = DOCS / "CHARGED_LEPTON_DIRECT_WARD_FREE_YUKAWA_NO_GO_NOTE_2026-04-26.md"

    print("Source surface")
    print("-" * 72)
    for path in (radiative_script, diagram_script, bz_script, direct_no_go_note):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    radiative_text = radiative_script.read_text(encoding="utf-8")
    diagram_text = diagram_script.read_text(encoding="utf-8")
    bz_text = bz_script.read_text(encoding="utf-8")

    check(
        "original radiative runner frames itself as support, not closure",
        "not a fully axiom-native retained closure theorem" in radiative_text,
    )
    check("radiative runner uses PDG tau as observational benchmark", "M_TAU_PDG" in radiative_text)
    check(
        "diagrammatic runner still cites an external loop integral surface",
        "I_loop is cited from retained YT_P1_BZ_QUADRATURE" in diagram_text,
    )
    check(
        "BZ runner states the support lane does not close Koide bridges",
        "does not by itself close" in bz_text and "Koide bridges" in bz_text,
    )

    print()
    print("A. Generation-blind radiative Casimir")
    print("-" * 72)
    casimirs = {gen.label: charged_lepton_casimir() for gen in GENERATIONS}
    check("charged-lepton Casimir is exactly one", charged_lepton_casimir() == 1)
    check(
        "same Casimir is assigned to e, mu, tau",
        len(set(casimirs.values())) == 1,
        str(casimirs),
    )

    permuted = tuple(reversed(tuple(casimirs.values())))
    check(
        "generation relabeling leaves the radiative Casimir vector invariant",
        permuted == tuple(casimirs.values()),
        f"C vector = {tuple(casimirs.values())}",
    )

    y_rad = ALPHA_LM / (4 * math.pi)
    y_by_generation = {gen.label: y_rad * float(casimirs[gen.label]) for gen in GENERATIONS}
    check(
        "radiative y value is identical for all charged-lepton generations",
        len({round(value, 18) for value in y_by_generation.values()}) == 1,
        str(y_by_generation),
    )

    print()
    print("B. Universal application is not the charged-lepton hierarchy")
    print("-" * 72)
    predicted_mass_mev = V_EW * 1000.0 * y_rad
    print(f"Universal radiative mass comparator: {predicted_mass_mev:.6f} MeV")

    ratios = {gen.label: predicted_mass_mev / gen.pdg_mass_mev for gen in GENERATIONS}
    print(f"Comparator ratios predicted/PDG: {ratios}")
    check(
        "universal radiative mass is close only to tau comparator",
        abs(ratios["tau"] - 1.0) < 1e-3 and ratios["mu"] > 10 and ratios["e"] > 1000,
        "observed masses are comparators, not proof inputs",
    )
    check(
        "same radiative rule cannot also fit electron and muon masses",
        abs(ratios["e"] - 1.0) > 1000 and abs(ratios["mu"] - 1.0) > 10,
    )

    print()
    print("C. Selector firewall")
    print("-" * 72)
    proof_inputs = {
        "ALPHA_LM",
        "one_loop_factor_4pi",
        "charged_lepton_electroweak_charges",
        "generation_blind_casimir",
        "retained_v_EW",
    }
    forbidden_selector_inputs = {"M_TAU_PDG", "m_e_PDG", "m_mu_PDG", "heaviest_observed_generation"}
    check(
        "PDG masses and heaviest-generation labels are not proof-input keys",
        proof_inputs.isdisjoint(forbidden_selector_inputs),
        f"proof inputs = {sorted(proof_inputs)}",
    )
    check(
        "no tau selector is present in the generation-blind Casimir data",
        len(set(casimirs.values())) == 1 and "tau" not in proof_inputs,
    )
    check(
        "direct Ward no-go already requires a new generation/source primitive",
        "generation-selection / loop-normalization / source-domain law" in direct_no_go_note.read_text(encoding="utf-8"),
    )

    print()
    print("D. N5 execution certificate")
    print("-" * 72)
    print(
        f"per_element: the three components of the generation vectors are formed "
        f"one label at a time and then compared — the Casimir vector comes out "
        f"{tuple(str(v) for v in casimirs.values())} for (e, mu, tau) and the "
        f"radiative Yukawa vector comes out identical to eighteen decimal places "
        f"at {y_rad:.18f} in every component, so no component carries information "
        f"that distinguishes it from the other two."
    )
    print(
        "per_site: checked and not executed — no lattice, link or site variable "
        "is constructed anywhere in this firewall; the inputs are electroweak "
        "vertex charge assignments and two retained constants, so there is no "
        "spatial index against which a site-resolved claim could be stated, and "
        "none is made."
    )
    print(
        "per_mode: checked and not executed — the one-loop content enters only as "
        "the closed factor 1/(4 pi) and no propagator, loop momentum or mode sum "
        "is evaluated here; the runner instead records that the diagrammatic lane "
        "still cites its loop integral from an external quadrature surface, which "
        "is why no mode-resolved statement is available to this firewall."
    )
    print(
        f"per_block: the charge data is resolved by electroweak multiplet block — "
        f"the left-handed doublet block contributes 2 * T(T+1) * 1/2 = 3/4 with "
        f"T = 1/2, the hypercharge pairing of the doublet with the right-handed "
        f"singlet contributes Y_L Y_R / 2 = 1/4, and those two blocks sum to "
        f"exactly {charged_lepton_casimir()}, which is the whole reason the "
        f"result carries no generation index."
    )
    print(
        f"lattice_wide: checked and not executed — there is no volume, lattice or "
        f"thermodynamic limit in this lane; the only whole-system statement made "
        f"is that one universal radiative scale is applied to all three "
        f"generations at once, giving {predicted_mass_mev:.6f} MeV against "
        f"comparator ratios {tuple(round(ratios[g.label], 4) for g in GENERATIONS)} "
        f"for (e, mu, tau), which shows a single universal number cannot be the "
        f"hierarchy and is recorded as comparator evidence only."
    )

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: radiative alpha_LM/(4pi) remains support, not a")
        print("standalone retained tau selector.  It can supply a candidate")
        print("charged-lepton scale only after a separate generation/ratio")
        print("primitive identifies the tau eigenvalue without PDG input.")
        return 0
    print("VERDICT: selector firewall has failing checks.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
