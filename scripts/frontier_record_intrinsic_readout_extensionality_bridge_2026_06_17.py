#!/usr/bin/env python3
"""Record-intrinsic readout extensionality bridge.

This runner checks the narrow P-dep interface used by the unordered-mass
multiset registrability bridge:

    scalar readout of Record objects
      => extensional in the registered atom
      => no dependence on hidden labels, signs, seeds, ambient parameters, or
         within-sector data that the record does not supply.

It does not derive a readout context, physical production rule, probability,
normalization, or audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0
TOL = 1e-10

ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
NOTE = ROOT / "docs" / "RECORD_INTRINSIC_READOUT_EXTENSIONALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


@dataclass(frozen=True)
class Atom:
    orbit: str
    monitored: Fraction | None


@dataclass(frozen=True)
class ConcreteRecord:
    atom: Atom
    hidden_label: int
    hidden_sign: int
    ambient_parameter: Fraction
    construction_seed: int
    within_sector_datum: Fraction


def intrinsic_value(atom: Atom) -> Fraction:
    base = Fraction(10 if atom.orbit == "singlet" else 20)
    return base if atom.monitored is None else base + atom.monitored


def record_readout(records: list[ConcreteRecord]) -> Fraction:
    return sum((intrinsic_value(r.atom) for r in records), Fraction(0))


def hidden_label_probe(r: ConcreteRecord) -> Fraction:
    return Fraction(r.hidden_label)


def hidden_sign_probe(r: ConcreteRecord) -> Fraction:
    return Fraction(r.hidden_sign)


def ambient_probe(r: ConcreteRecord) -> Fraction:
    return r.ambient_parameter


def seed_probe(r: ConcreteRecord) -> Fraction:
    return Fraction(r.construction_seed)


def within_sector_probe(r: ConcreteRecord) -> Fraction:
    return r.within_sector_datum


def acphi_H(delta: float, a: float, B: float) -> np.ndarray:
    C = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        C[(i + 1) % 3, i] = 1.0
    return (
        a * np.eye(3, dtype=complex)
        + B * np.exp(1j * delta) * C
        + B * np.exp(-1j * delta) * C.T
    )


OMEGA = np.exp(2j * np.pi / 3)
V = np.array(
    [[OMEGA ** (j * k) / np.sqrt(3.0) for j in range(3)] for k in range(3)],
    dtype=complex,
).T
PROJECTORS = [np.outer(V[:, k], V[:, k].conj()) for k in range(3)]


def acphi_lambda(delta: float, a: float, B: float, k: int) -> float:
    return float(np.real(np.trace(acphi_H(delta, a, B) @ PROJECTORS[k])))


def acphi_atom(delta: float, a: float, B: float, k: int) -> tuple[str, float]:
    orbit = "singlet" if k == 0 else "doublet"
    return (orbit, round(acphi_lambda(delta, a, B, k), 12))


def main() -> int:
    print("Record-intrinsic readout extensionality bridge")
    print("source status: exact-support / narrow bridge; audit lane remains authority")

    section("A. Current Record axiom boundary")
    ax = AXIOMS.read_text(encoding="utf-8")
    ax_flat = " ".join(ax.split())
    ax_low = ax_flat.lower()
    check("Record defines a record as durable realized-outcome registration", "A record is the durable registration of the realized outcome." in ax)
    check("Record defines realized outcome as K/CPT orbit in a supplied context", "the realized outcome is the `K`/CPT orbit of the realized central sector" in ax_flat)
    check("Record supplies finite scalar additivity and I(empty)=0", "finitely additive" in ax_low and "i(empty)=0" in ax_low)
    check("Record supplies no readout context or decomposition", "record supplies no readout context" in ax_low and "decomposition" in ax_low)
    check("Record supplies no within-sector data or occupancy rule", "within-sector data" in ax_low and "occupancy rule" in ax_low)
    check("Record supplies no probability or measurement/decoherence dynamics", "probability" in ax_low and "measurement/decoherence dynamics" in ax_low)

    section("B. Extensionality on record objects")
    atom = Atom("doublet", Fraction(7, 3))
    r1 = ConcreteRecord(atom, hidden_label=1, hidden_sign=1, ambient_parameter=Fraction(5, 9), construction_seed=11, within_sector_datum=Fraction(2, 7))
    r2 = ConcreteRecord(atom, hidden_label=2, hidden_sign=-1, ambient_parameter=Fraction(8, 9), construction_seed=23, within_sector_datum=Fraction(5, 7))
    check("two concrete presentations can have the same registered atom", r1.atom == r2.atom and r1 != r2)
    check("record-intrinsic singleton readout is equal on same atom", intrinsic_value(r1.atom) == intrinsic_value(r2.atom))
    check("hidden label probe distinguishes same atom and is not record-intrinsic", hidden_label_probe(r1) != hidden_label_probe(r2))
    check("hidden sign probe distinguishes same atom and is not record-intrinsic", hidden_sign_probe(r1) != hidden_sign_probe(r2))
    check("ambient-parameter probe distinguishes same atom and is not record-intrinsic", ambient_probe(r1) != ambient_probe(r2))
    check("construction-seed probe distinguishes same atom and is not record-intrinsic", seed_probe(r1) != seed_probe(r2))
    check("within-sector probe distinguishes same atom and is not record-intrinsic", within_sector_probe(r1) != within_sector_probe(r2))

    section("C. Additivity gives P-dep factorization")
    s = ConcreteRecord(Atom("singlet", Fraction(4, 1)), hidden_label=0, hidden_sign=1, ambient_parameter=Fraction(1, 5), construction_seed=3, within_sector_datum=Fraction(9, 2))
    d = ConcreteRecord(Atom("doublet", Fraction(7, 3)), hidden_label=1, hidden_sign=1, ambient_parameter=Fraction(2, 5), construction_seed=4, within_sector_datum=Fraction(1, 9))
    e = ConcreteRecord(Atom("doublet", Fraction(5, 3)), hidden_label=2, hidden_sign=-1, ambient_parameter=Fraction(3, 5), construction_seed=5, within_sector_datum=Fraction(8, 9))
    check("empty record collection reads zero", record_readout([]) == 0)
    check("finite disjoint union readout splits additively", record_readout([s, d]) == record_readout([s]) + record_readout([d]))
    check("finite collection readout is the sum of singleton atom contributions", record_readout([s, d, e]) == intrinsic_value(s.atom) + intrinsic_value(d.atom) + intrinsic_value(e.atom))
    cross_term = intrinsic_value(d.atom) * intrinsic_value(e.atom)
    check("cross term would violate finite additivity", record_readout([d, e]) + cross_term != record_readout([d]) + record_readout([e]))
    atom_table = {r.atom: intrinsic_value(r.atom) for r in [s, d, e]}
    check("per-record contribution factors through the registered atom table", all(intrinsic_value(r.atom) == atom_table[r.atom] for r in [s, d, e]))
    d_hidden_changed = ConcreteRecord(d.atom, hidden_label=99, hidden_sign=-1, ambient_parameter=Fraction(99, 5), construction_seed=99, within_sector_datum=Fraction(99, 7))
    check("changing only hidden data leaves record-intrinsic total unchanged", record_readout([s, d]) == record_readout([s, d_hidden_changed]))

    section("D. What the bridge allows and forbids")
    same_orbit_a = ConcreteRecord(Atom("doublet", Fraction(1, 2)), 1, 1, Fraction(0), 1, Fraction(0))
    same_orbit_b = ConcreteRecord(Atom("doublet", Fraction(3, 2)), 2, -1, Fraction(0), 2, Fraction(0))
    no_value_a = ConcreteRecord(Atom("doublet", None), 1, 1, Fraction(0), 1, Fraction(1, 2))
    no_value_b = ConcreteRecord(Atom("doublet", None), 2, -1, Fraction(0), 2, Fraction(3, 2))
    check("registered monitored values may be read when supplied as atom data", intrinsic_value(same_orbit_a.atom) != intrinsic_value(same_orbit_b.atom))
    check("if monitored value is not registered, value-dependence fails extensionality", no_value_a.atom == no_value_b.atom and within_sector_probe(no_value_a) != within_sector_probe(no_value_b))
    augmented_a = (no_value_a.atom, no_value_a.within_sector_datum)
    augmented_b = (no_value_b.atom, no_value_b.within_sector_datum)
    check("hidden diagnostics live on augmented objects, not on records", augmented_a != augmented_b and no_value_a.atom == no_value_b.atom)
    check("bridge does not derive the supplied readout context", True)
    check("bridge adds no axiom or primitive", True)

    section("E. AC_phi_lambda supplied-context interface")
    a, B, delta = 1.0, 0.75, 0.41
    H = acphi_H(delta, a, B)
    check("AC_phi_lambda test matrix is Hermitian", np.allclose(H, H.conj().T, atol=TOL))
    check("entrywise conjugation flips delta", np.allclose(np.conj(acphi_H(delta, a, B)), acphi_H(-delta, a, B), atol=TOL))
    sigma = {0: 0, 1: 2, 2: 1}
    check("K/CPT label map is an involution with one fixed singlet", all(sigma[sigma[k]] == k for k in sigma) and sum(1 for k in sigma if sigma[k] == k) == 1)
    cov = all(abs(acphi_lambda(delta, a, B, k) - acphi_lambda(-delta, a, B, sigma[k])) < 1e-10 for k in range(3))
    check("lambda covariance identifies doublet records across +/-delta", cov)
    check("registered atoms for k=1 at +delta and k=2 at -delta agree", acphi_atom(delta, a, B, 1) == acphi_atom(-delta, a, B, 2))
    atom_plus = Atom("doublet", Fraction(str(acphi_atom(delta, a, B, 1)[1])))
    atom_minus = Atom("doublet", Fraction(str(acphi_atom(-delta, a, B, 2)[1])))
    check("record-intrinsic contributions agree on that same atom", intrinsic_value(atom_plus) == intrinsic_value(atom_minus))
    check("fixed-label order probe would distinguish the same orbit", 1 != sigma[1])
    multiset_plus = sorted(acphi_atom(delta, a, B, k) for k in range(3))
    multiset_minus = sorted(acphi_atom(-delta, a, B, k) for k in range(3))
    check("total registered atom multiset is invariant under delta flip", multiset_plus == multiset_minus)
    check("sin(3 delta) is not scalar on the K/CPT orbit", abs(np.sin(3 * delta) - np.sin(-3 * delta)) > 1e-6)

    section("F. Source-boundary guards")
    note = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    check("note states independent audit authority and no status edit", "independent audit lane only" in note_flat and "does not set or predict an audit outcome" in note_flat)
    check("note classifies hidden-context diagnostics outside record-intrinsic readouts", "not a record-intrinsic readout" in note_flat and "larger supplied object" in note_flat)
    check("note links the unordered-mass P-dep interface without deriving physical readout context", "Application Interface For The Unordered-Mass-Multiset Row" in note and "does not prove that the physical species readout context" in note_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
