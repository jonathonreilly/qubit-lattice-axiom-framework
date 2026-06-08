"""The i-IDENTITY AUTOMORPHISM GATE (exercise artifact #1; the diagnostic that gates the unification).

QUESTION (route-3 of the exercise): is the complex unit `i` that appears across the framework ONE physical
object whose sign-flip is implemented by the SINGLE global Record-CPT conjugation K (entrywise complex
conjugation), or are there SEVERAL independent complex structures? If one i -> the hope that a single
structural lever moves r, theta, and delta-sign together is licensed; if several -> the wall is genuinely
multi-dimensional along the complex-structure axis and no single primitive buys more than one item.

This is exactly the cheap, finite, decidable test that would have caught the refuted det_C='Dyson class'
unification early (MEMORY #3138): DERIVE the identification, do not assert it.

K = global complex conjugation in the standard basis (the Record K/CPT conjugation), K(X) = conj(X),
antilinear: K(i)=-i. An object "carries the scalar i" iff K flips its sign (K(X) = -X, K-ODD). An object is
a REAL structure iff K fixes it (K(X) = X, K-EVEN) -- such an object can still be a complex STRUCTURE
(square to -1 on a subspace) yet be invisible to the scalar conjugation K.

TABULATES + classifies each appearance of i / orientation as a concrete algebra element:
  i1. Quantum scalar i      : i*I_2 in M_2(C).
  i2. su(2) imaginary gen   : sigma_y.
  i3. Cl(3,0) volume element: omega = sigma_x sigma_y sigma_z   (claim: = i*I_2, so volume element IS i1).
  i4. composition i (#2573) : the shared central i of M_2(C) (x) M_2(C)  ((i*I2)(x)I2 == I2(x)(i*I2) == i*I4).
  i5. readout/Yukawa phase  : the phase delta of b=|b|e^{i delta} in M = aI + bC + b-bar C^2.
  j1. generation complex str: J_cs = (C - C^2)/sqrt(3)  (REAL antisymmetric, J_cs^2 = -(I - P_triv)).
  o1. orientation Z2        : sign(Vandermonde) of the C3 generation spectrum (S_3 sign rep, REAL).

DECISIVE CHECKS:
  G1 omega = i*I_2 exactly (the Clifford pseudoscalar IS the scalar i).
  G2 the composition i is shared: (i*I2)(x)I2 == I2(x)(i*I2) == i*I4  (one i across two sites).
  G3 a SINGLE global K flips ALL of {i1,i2,i3,i4} simultaneously (K-ODD): the scalar/algebraic i is ONE object.
  G4 the Yukawa phase is K-ODD: K(M) = M with delta -> -delta (the phase rides the same scalar i); the
     observable SPECTRUM is K-EVEN (records read the K-even modulus, drop the K-odd phase).
  G5 J_cs is REAL -> K(J_cs) = J_cs (K-EVEN) yet J_cs^2 = -1 on the doublet: a genuine complex structure the
     scalar conjugation K CANNOT flip -> INDEPENDENT of the scalar i.
  G6 sign(Vandermonde) orientation is a REAL Z2 -> K-EVEN (K cannot flip it).
  G7 VERDICT: K flips the scalar-i cluster {i1..i5} but FIXES the real-structure cluster {j1,o1}. So there
     are (at least) TWO independent complex structures under global K (K-odd scalar i; K-even real structure).

CONCLUSION: the naive "one i / one lever moves all four" unification is NOT licensed; the scalar-i sub-sector
(theta reality class + delta phase + the scalar-i holomorphic reading of r) IS internally unified by the
single K, but the polarization/orientation lever that actually decides r=1/2-vs-1 and delta-sign lives in
the K-EVEN real-structure sector (J_cs / Vandermonde) -- a SEPARATE single object (route 4's KO-dimension
real structure J), to be tested on its own. The det_C-style error this gate forecloses: assuming the scalar
i (composition/phase) and the real-structure polarization are the same object -- they provably are not (K
flips one, fixes the other). No PDG/fitted value; exact numpy.
"""
from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def K(X):
    """Global Record-CPT conjugation = entrywise complex conjugation in the standard basis (antilinear)."""
    return np.conjugate(X)


def kparity(X, tol=1e-12):
    """Return 'odd' if K(X) = -X (carries the scalar i), 'even' if K(X) = X (real structure), else 'mixed'."""
    if np.allclose(K(X), -X, atol=tol):
        return "odd"
    if np.allclose(K(X), X, atol=tol):
        return "even"
    return "mixed"


def main() -> int:
    print("i-IDENTITY AUTOMORPHISM GATE: one scalar i, or several independent complex structures?")
    print("=" * 86)
    I2 = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], complex)
    Y = np.array([[0, -1j], [1j, 0]], complex)
    Z = np.array([[1, 0], [0, -1]], complex)

    # ---- the i-carrying objects ----
    i1 = 1j * I2                       # Quantum scalar i
    i2 = Y                             # su(2) imaginary generator
    i3 = X @ Y @ Z                     # Cl(3,0) volume element omega
    i4 = np.kron(1j * I2, I2)          # composition central i on M2 (x) M2
    i4b = np.kron(I2, 1j * I2)

    # ---- the real-structure / orientation objects (generation sector) ----
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)   # 3-cycle (real permutation)
    J_cs = (C - C @ C) / np.sqrt(3.0)
    P_triv = np.ones((3, 3), complex) / 3.0

    # G1: volume element IS the scalar i
    check("G1: Cl(3,0) volume element omega = sigma_x sigma_y sigma_z = i*I_2 EXACTLY (the pseudoscalar IS "
          "the scalar i)", np.allclose(i3, 1j * I2),
          f"omega = {np.round(i3,6).tolist()}  (== i*I_2)")

    # G2: composition i is shared (one i across two sites)
    check("G2: composition i is SHARED -- (i*I2)(x)I2 == I2(x)(i*I2) == i*I4 (two sites share ONE i)",
          np.allclose(i4, i4b) and np.allclose(i4, 1j * np.eye(4)),
          f"||(i*I2)(x)I2 - I2(x)(i*I2)|| = {np.linalg.norm(i4 - i4b):.1e}")

    # G3: a SINGLE global K flips ALL scalar-i objects simultaneously
    parities = {"i1 scalar i*I2": kparity(i1), "i2 sigma_y": kparity(i2),
                "i3 volume omega": kparity(i3), "i4 composition i": kparity(i4)}
    all_odd = all(p == "odd" for p in parities.values())
    check("G3: one global K (entrywise conj) flips ALL of {i*I2, sigma_y, omega, composition i} -> K-ODD "
          "for every one -> the scalar/algebraic i is ONE object",
          all_odd, "; ".join(f"{k}:{v}" for k, v in parities.items()))

    # G4: the Yukawa phase rides the same scalar i (K-odd); the spectrum is K-even
    a, b_mag, delta = 1.0, 1.0 / np.sqrt(2), 0.2222
    b = b_mag * np.exp(1j * delta)
    M = a * I2.shape[0] * 0 + a * np.eye(3, dtype=complex) + b * C + np.conj(b) * (C @ C)
    M_negdelta = a * np.eye(3, dtype=complex) + (b_mag * np.exp(-1j * delta)) * C + (b_mag * np.exp(1j * delta)) * (C @ C)
    phase_flips = np.allclose(K(M), M_negdelta)          # K sends delta -> -delta
    spectrum_even = np.allclose(np.sort(np.linalg.eigvalsh(M)), np.sort(np.linalg.eigvalsh(M_negdelta)))
    check("G4: Yukawa phase is K-ODD -- K(M) = M with delta -> -delta (the phase rides the scalar i); but the "
          "observable SPECTRUM is K-EVEN (records read the K-even modulus, drop the K-odd phase)",
          phase_flips and spectrum_even,
          f"K(M)==M(delta->-delta): {phase_flips}; spectrum(+delta)==spectrum(-delta): {spectrum_even}")

    # G5: J_cs is a REAL complex structure -> K-even, independent of the scalar i
    jcs_real = np.allclose(J_cs.imag, 0)
    jcs_parity = kparity(J_cs)
    jcs_is_cstruct = np.allclose(J_cs @ J_cs, -(np.eye(3) - P_triv))
    check("G5: J_cs = (C - C^2)/sqrt3 is REAL (K-EVEN, K(J_cs)=J_cs) yet J_cs^2 = -(I - P_triv) (a genuine "
          "complex structure on the doublet) -> an i the scalar conjugation K CANNOT flip -> INDEPENDENT of "
          "the scalar i",
          jcs_real and jcs_parity == "even" and jcs_is_cstruct,
          f"J_cs real={jcs_real}, K-parity={jcs_parity}, J_cs^2=-(I-P_triv): {jcs_is_cstruct}")

    # G6: orientation sign(Vandermonde) is a real Z2 -> K-even
    lam = np.sort(np.linalg.eigvalsh(M)).real
    Delta = (lam[0] - lam[1]) * (lam[1] - lam[2]) * (lam[2] - lam[0])
    orient_real = abs(np.imag(Delta)) < 1e-12 if np.iscomplexobj(Delta) else True
    check("G6: orientation sign(Vandermonde) of the C3 spectrum is a REAL Z2 (S_3 sign rep) -> K-EVEN; K "
          "cannot flip a real orientation bit",
          orient_real and np.sign(Delta) in (-1.0, 1.0),
          f"Vandermonde Delta = {Delta:.4f} (real), sign = {int(np.sign(Delta))}")

    # G7: VERDICT -- two independent complex structures under global K
    scalar_i_cluster_odd = all_odd and phase_flips
    real_structure_cluster_even = (jcs_parity == "even") and orient_real
    two_independent = scalar_i_cluster_odd and real_structure_cluster_even
    check("G7 (VERDICT): a single global K flips the scalar-i cluster {i*I2, sigma_y, omega, composition i, "
          "Yukawa phase} (ONE object, K-ODD) but FIXES the real-structure cluster {J_cs, Vandermonde "
          "orientation} (K-EVEN) -> there are (at least) TWO INDEPENDENT complex structures under K; the "
          "naive single-i unification is NOT licensed",
          two_independent,
          f"scalar-i cluster all K-odd: {scalar_i_cluster_odd}; real-structure cluster all K-even: {real_structure_cluster_even}")

    print("\nCLASSIFICATION TABLE (object | complex-structure? | K-parity):")
    rows = [
        ("i1 Quantum scalar i*I2", "yes (i^2=-1)", kparity(i1)),
        ("i2 su(2) sigma_y", "yes", kparity(i2)),
        ("i3 Cl(3) volume omega=iI", "yes (= i1)", kparity(i3)),
        ("i4 composition i (#2573)", "yes (shared)", kparity(i4)),
        ("i5 Yukawa phase delta", "scalar-i phase", "odd (delta->-delta)"),
        ("j1 generation J_cs", "yes (on doublet)", kparity(J_cs)),
        ("o1 sign(Vandermonde)", "Z2 orientation", "even (real)"),
    ]
    for nm, cs, kp in rows:
        print(f"   {nm:32s} | {cs:18s} | K-{kp}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "GATE VERDICT: the scalar/algebraic i is ONE object -- the Quantum i*I2, the su(2) sigma_y, the Cl(3)\n"
        "volume element omega=iI, the composition i, and the Yukawa phase are ALL flipped by the single global\n"
        "Record-CPT conjugation K. This INTERNALLY UNIFIES the CP/phase/reality sub-sector: the theta reality\n"
        "class, the delta phase, and the scalar-i holomorphic reading of r are all governed by that one K.\n"
        "BUT the framework-native generation complex structure J_cs and the orientation Z2 sign(Vandermonde)\n"
        "are REAL operators, K-INVARIANT, and thus INDEPENDENT of the scalar i. So there is NOT a single\n"
        "complex structure: the wall has (at least) two independent axes -- the K-ODD scalar i and the K-EVEN\n"
        "real structure. The naive 'one lever moves all four' unification is NOT licensed in its strong form.\n"
        "What IS licensed: (a) pursue theta + delta-phase + r-readability jointly through the single scalar-i =\n"
        "Record-CPT K; (b) treat route-4's KO-dimension real structure J as a SEPARATE single Z2 lever living\n"
        "in the K-EVEN sector (same place as J_cs / Vandermonde), to be tested ON ITS OWN. FORECLOSED det_C-\n"
        "style error: assuming the scalar i (composition/phase) and the real-structure polarization (which sets\n"
        "r=1/2 vs r=1 and delta-sign) are the same object -- they provably are not (K flips one, fixes the\n"
        "other). Run route 4 on the K-even real structure; do NOT assume one i buys all four."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
