#!/usr/bin/env python3
"""Verify ambient scalar K-blindness and the projective carrier requirement."""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def squash(text: str) -> str:
    return " ".join(text.split())


def is_zero_matrix(mat: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in mat)


def trace_heat_torus(n: int, t: float, power: int) -> complex:
    coords = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
    index = {c: i for i, c in enumerate(coords)}
    size = n**3
    lap = np.zeros((size, size), dtype=float)
    for c, i in index.items():
        lap[i, i] = 6.0
        for axis in range(3):
            for step in (-1, 1):
                cc = list(c)
                cc[axis] = (cc[axis] + step) % n
                lap[i, index[tuple(cc)]] -= 1.0

    perm = np.zeros((size, size), dtype=float)
    for c, i in index.items():
        r = c
        for _ in range(power):
            r = (r[2], r[0], r[1])
        perm[index[r], i] = 1.0

    vals, vecs = np.linalg.eigh(lap)
    heat = (vecs * np.exp(-t * vals)) @ vecs.T
    return np.trace(heat @ perm)


def markdown_targets(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    note_path = docs / "ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md"
    dirac_path = docs / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
    axioms_path = docs / "MINIMAL_AXIOMS_2026-06-29.md"

    note = note_path.read_text(encoding="utf-8")
    dirac = dirac_path.read_text(encoding="utf-8")
    axioms = axioms_path.read_text(encoding="utf-8")
    note_s = squash(note)
    dirac_s = squash(dirac)
    axioms_s = squash(axioms)

    section("PART A - sources and pins")
    check("note exists", note_path.exists())
    check("Dirac dependency exists", dirac_path.exists())
    check("Dirac dependency contains per-site pin", "per-site" in dirac)
    check("Dirac dependency contains proper-cubic pin", "proper cubic rotations" in dirac_s)
    check("Dirac dependency contains claim_scope row", "claim_scope:" in dirac)
    required_scope = (
        "On the adjacency-licensed Q-conserving nearest-neighbor bilinear surface over per-site C^2, "
        "imposing translation and proper-cubic covariance up to local U(1) frame gives exactly two "
        "gauge/scale classes K0 and K1; the K1 branch has the stated site-local absorbing frame "
        "uniqueness, and K0 shows the flux(-1) selector is not forced."
    )
    check("note quotes required ledger claim scope", required_scope in note_s)
    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    check("axioms memo exists", axioms_path.exists())
    check("axioms memo contains Lattice sentence", lattice_sentence in axioms_s)
    check("note quotes Lattice sentence inline", lattice_sentence in note_s)

    section("PART B - T8-1 scalar K-blindness")
    I = sp.I
    R = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    check("cycle matrix has order three", R**3 == sp.eye(3))
    check("R squared is R dagger", R**2 == R.conjugate().T)
    a11, a22, a33, a12, a13, a23 = sp.symbols("a11 a22 a33 a12 a13 a23", real=True)
    b12, b13, b23 = sp.symbols("b12 b13 b23", real=True)
    A = sp.Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]])
    B = sp.Matrix([[0, b12, b13], [-b12, 0, b23], [-b13, -b23, 0]])
    O = A + I * B
    tr1 = sp.trace(O * R)
    tr2 = sp.trace(O * R**2)
    check("generic O is Hermitian", O == O.conjugate().T)
    check("Tr(O R^2) equals conjugate Tr(O R)", sp.simplify(tr2 - sp.conjugate(tr1)) == 0)
    tr1_real = sp.trace(A * R)
    tr2_real = sp.trace(A * R**2)
    check("real symmetric trace is R/R2 equal", sp.simplify(tr1_real - tr2_real) == 0)
    rng = np.random.default_rng(7)
    m = rng.normal(size=(3, 3))
    real_sym = (m + m.T) / 2.0
    rr = np.array(R.tolist(), dtype=float)
    np_gap = np.trace(real_sym @ rr) - np.trace(real_sym @ (rr @ rr))
    check("seeded real-symmetric numpy instance is blind", abs(np_gap) < 1e-12, detail=f"gap={np_gap:.3e}")
    for t in (0.3, 1.0):
        h1 = trace_heat_torus(4, t, 1)
        h2 = trace_heat_torus(4, t, 2)
        check(f"Z_4^3 dense heat trace R/R2 equality at t={t}", abs(h1 - h2) < 1e-9, detail=f"gap={abs(h1-h2):.3e}")

    section("PART C - T8-2 isotypic corollary")
    T0, S = sp.symbols("T0 S", real=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * I / 2
    iso1 = (T0 + sp.conjugate(omega) * S + omega * S) / 3
    iso2 = (T0 + omega * S + sp.conjugate(omega) * S) / 3
    check("I_1 equals I_2 when T1=T2 is real", sp.simplify(iso1 - iso2) == 0)
    z = 1 + I
    iso1_z = (0 + sp.conjugate(omega) * z + omega * sp.conjugate(z)) / 3
    iso2_z = (0 + omega * z + sp.conjugate(omega) * sp.conjugate(z)) / 3
    check("complex T1 discriminator separates isotypes", sp.simplify(iso1_z - iso2_z) != 0)
    check("complex discriminator value is exact", sp.simplify(iso1_z - iso2_z - 2 * sp.sqrt(3) / 3) == 0)

    section("PART D - T8-3 complex-hopping rejector")
    E = lambda i, j: sp.Matrix(3, 3, lambda r, c: 1 if (r, c) == (i, j) else 0)
    phi = sp.Rational(7, 10)
    loop = sp.exp(I * phi) * E(0, 1) + E(1, 2) + E(2, 0)
    O_flux = loop + loop.conjugate().T
    f1 = sp.trace(O_flux * R)
    f2 = sp.trace(O_flux * R**2)
    check("phased loop O is Hermitian", O_flux == O_flux.conjugate().T)
    check("flux trace has nonzero imaginary part", sp.im(f1).is_zero is False, detail=f"Im={sp.im(f1)}")
    check("flux traces remain conjugate-paired", sp.simplify(f2 - sp.conjugate(f1)) == 0)
    check("flux rejector breaks scalar equality", sp.simplify(f1 - f2) != 0)
    flux_i1 = (sp.trace(O_flux) + sp.conjugate(omega) * f1 + omega * f2) / 3
    flux_i2 = (sp.trace(O_flux) + omega * f1 + sp.conjugate(omega) * f2) / 3
    check("flux rejector distinguishes conjugate sectors", sp.simplify(flux_i1 - flux_i2) != 0)

    section("PART E - T8-4 projective spin lift")
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    U = (sp.eye(2) - I * (sx + sy + sz)) / 2
    U_exp = sp.Rational(1, 2) * sp.eye(2) - I * sp.sqrt(3) / 2 * ((sx + sy + sz) / sp.sqrt(3))
    check("closed form equals exp-axis form", sp.simplify(U - U_exp) == sp.zeros(2))
    check("U is unitary", sp.simplify(U * U.conjugate().T - sp.eye(2)) == sp.zeros(2))
    check("U^3 is minus identity", sp.simplify(U**3 + sp.eye(2)) == sp.zeros(2))
    check("Tr U equals one", sp.simplify(sp.trace(U) - 1) == 0)
    check("Tr U^2 equals minus one", sp.simplify(sp.trace(U**2) + 1) == 0)
    check("projective inverse relation U^2=-U^-1", sp.simplify(U**2 + U.inv()) == sp.zeros(2))
    nsigma = (sx + sy + sz) / sp.sqrt(3)
    check("rotation axis is fixed", is_zero_matrix(sp.simplify(U * nsigma * U.conjugate().T - nsigma)))
    check("U sends sigma_x to sigma_y", sp.simplify(U * sx * U.conjugate().T - sy) == sp.zeros(2))
    check("U sends sigma_y to sigma_z", sp.simplify(U * sy * U.conjugate().T - sz) == sp.zeros(2))
    check("U sends sigma_z to sigma_x", sp.simplify(U * sz * U.conjugate().T - sx) == sp.zeros(2))
    p, q, r, s = sp.symbols("p q r s", real=True)
    O_spin = sp.Matrix([[p, q + I * r], [q - I * r, s]])
    spin_expr = sp.trace(O_spin * U**2) + sp.conjugate(sp.trace(O_spin * U))
    check("generic spinor O is Hermitian", O_spin == O_spin.conjugate().T)
    check("spinor sign trace identity holds", sp.simplify(spin_expr) == 0)
    check("unlifted scalar cycle has equal traces", sp.trace(R) == sp.trace(R**2) == 0)
    check("lift traces are unequal", sp.trace(U) != sp.trace(U**2))
    V = (sp.eye(2) - I * sz) / sp.sqrt(2)
    check("wrong C4-type lift fails Z_6 relation", sp.simplify(V**3 + sp.eye(2)) != sp.zeros(2))

    section("PART F - note discipline")
    required_sentences = [
        "the scalar ambient equivariant surface is K-blind: conjugate-sector traces coincide for every real function of the scalar Laplacian",
        "the spin-1/2 lift of the `C3[111]` rotation is projective (`U^3 = -I`), and the double cover natively distinguishes the conjugate sectors",
        "this note names the carrier requirement; it does not derive the phase value",
        "not a terminal no-go",
    ]
    for sentence in required_sentences:
        lines = [line for line in note.splitlines() if sentence in line]
        check(f"required sentence present: {sentence[:42]}", bool(lines))
        check(f"required sentence embedded: {sentence[:42]}", bool(lines) and all(line.strip() != sentence for line in lines))
    for token in ["only route", "last route", "exhausted", "closes the route", "PDG", "new wall"]:
        check(f"forbidden token absent: {token}", token not in note)
    walls = sorted(set(re.findall(r"(?<![A-Z0-9])W_[A-Za-z0-9_]+", note)))
    allowed_walls = ["W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"]
    check("W_ names are whitelisted", all(w in allowed_walls for w in walls), detail=", ".join(walls))
    targets = markdown_targets(note)
    md_targets = [t for t in targets if ".md" in t]
    py_targets = [t for t in targets if ".py" in t]
    check("exactly one markdown dependency target", len(md_targets) == 1 and "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md" in md_targets[0], detail=str(md_targets))
    check("primary runner is the only script link", len(py_targets) == 1 and "acphilambda_ambient_scalar_k_blindness_projective_carrier_2026_07_02.py" in py_targets[0], detail=str(py_targets))
    check("axioms memo is not a markdown target", all("MINIMAL_AXIOMS_2026-06-29.md" not in t for t in targets))
    for ident in [
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01",
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01",
        "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01",
        "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01",
        "ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02",
        "ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02",
        "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02",
    ]:
        check(f"in-flight basename is backticked: {ident[:28]}", f"`{ident}`" in note)
    for token in ["PRESERVE VERBATIM", "MUST BE ABSENT", "Acceptance contract", "ANTI-FABRICATION", "Files to produce", "runner greps", "spec-carrier"]:
        check(f"spec leakage absent: {token}", token not in note)
    check("note declares canonical claim type", "**Type:** bounded_theorem" in note)
    check("note avoids source-side audit verdict", "retained_bounded" not in note and "audited_clean" not in note)
    dependency_line = next((line for line in note.splitlines() if "load-bearing dependency" in line), "")
    check("dependency appears with quoted ledger scope", "claim scope:" in dependency_line and required_scope[:60] in dependency_line)
    for needle in ["N1:", "N2:", "N3:", "N4:", "N5:", "N6:", "N7:", "N8:"]:
        check(f"No-Go gate contains {needle}", needle in note)
    for heading in ["## Verification", "## Non-Claims", "## Routing Consequence"]:
        check(f"note contains {heading}", heading in note)
    check("verification records measured total placeholder or count", "TOTAL: PASS=" in note and "FAIL=0" in note)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
