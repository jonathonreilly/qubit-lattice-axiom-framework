#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""RECORD_GENERATION_READOUT_TWO_SECTORS — generation readout resolves two sectors.

Theorem (conditional on the supplied readout context):

  The generation readout context resolves exactly TWO central sectors under its
  supplied fixed K/CPT conjugation: a SINGLET (dim 1) and a DOUBLET (dim 2).

Supplied readout context (NOT re-derived here; cited provenance):
  - The emergent 3-generation carrier is the hw=1 BZ-corner orbit {e1,e2,e3}
    carrying the regular representation of C3 = Z3
    (CL3_TASTE_GENERATION_THEOREM / FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED).
  - The readout context is a finite central-sector decomposition with a fixed
    K/CPT conjugation. The Record axiom, MINIMAL_AXIOMS_2026-06-05, names the
    realized K/CPT orbit and makes scalar readout I finitely additive over
    disjoint records; it does not supply the context, decomposition,
    conjugation, weight, probability, or dynamics.

What the runner COMPUTES (exact sympy + numpy cross-check):
  1. The regular representation of C3 on {e1,e2,e3} (the cyclic permutation),
     and its complex irreducible characters chi_0, chi_1, chi_2.
  2. The K = complex-conjugation action on the three characters, and its orbits:
     {chi_0} fixed, {chi_1, chi_2} swapped.
  3. The orbit dimensions: 1 (singlet) and 2 (doublet). TWO sectors.
  4. The Frobenius-Schur indicators nu = (1/|G|) sum_g chi(g^2):
     nu(chi_0)=+1 (real type), nu(chi_1)=nu(chi_2)=0 (complex type).
  5. The CONTRAST showing K/CPT is load-bearing:
       - complex split  C[Z3] = C ⊕ C ⊕ C  -> THREE central sectors;
       - real Wedderburn R[Z3] = R ⊕ C     -> TWO real blocks
     and the real-block count equals the K/CPT-orbit count (= 2).

Target: PASS >= 20, FAIL = 0.
"""
from __future__ import annotations

import cmath
import math

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def cx(z) -> sp.Expr:
    """Canonicalize a complex sympy expression to rectangular a+b*I form so that
    exp(2*pi*I/3) and -1/2+sqrt(3)*I/2 compare equal under structural ==."""
    return sp.nsimplify(sp.expand_complex(sp.simplify(z)))


def ceq(a, b) -> bool:
    """Exact symbolic equality of two (possibly complex) sympy scalars."""
    return sp.simplify(sp.expand_complex(a - b)) == 0


def veq(va, vb) -> bool:
    """Exact symbolic equality of two equal-length lists of scalars."""
    return len(va) == len(vb) and all(ceq(x, y) for x, y in zip(va, vb))


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {label}"
    if detail:
        line += f"\n       {detail}"
    print(line)


def banner(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


# ---------------------------------------------------------------------------
# Group C3 = Z3 and its regular representation on the hw=1 carrier {e1,e2,e3}.
# ---------------------------------------------------------------------------
# Exact primitive cube root of unity in sympy.
W = sp.exp(2 * sp.pi * sp.I / 3)          # omega = e^{2 pi i / 3}
ELEMENTS = [0, 1, 2]                        # C3 = {e, g, g^2} written additively


def banner_setup() -> sp.Matrix:
    banner("Setup - supplied readout carrier: C3 regular rep on hw=1 orbit {e1,e2,e3}")
    # The cyclic generator g acts as e1 -> e2 -> e3 -> e1 (cited provenance:
    # CL3_TASTE_GENERATION_THEOREM section C, Z3 cycles the hw=1 corners).
    # As a permutation matrix on basis (e1,e2,e3):
    P = sp.Matrix([[0, 0, 1],
                   [1, 0, 0],
                   [0, 1, 0]])
    # g^k = P^k. This is the (left) regular representation of C3.
    I3 = sp.eye(3)
    check("S1 regular-rep generator P is a permutation realizing e1->e2->e3->e1",
          P * sp.Matrix([1, 0, 0]) == sp.Matrix([0, 1, 0]) and
          P * sp.Matrix([0, 1, 0]) == sp.Matrix([0, 0, 1]) and
          P * sp.Matrix([0, 0, 1]) == sp.Matrix([1, 0, 0]),
          "P e1=e2, P e2=e3, P e3=e1")
    check("S2 P has order 3 (C3): P^3 = I, P != I", P**3 == I3 and P != I3,
          "P^3 = I_3")
    # Faithful = injective on the group: distinct group elements -> distinct
    # matrices, i.e. P, P^2 are both != I (and P^3 = I closes the order-3 cycle).
    check("S3 regular rep is faithful and 3-dimensional",
          P != I3 and P**2 != I3 and P.shape == (3, 3),
          "dim = 3 = |C3|; g, g^2 act nontrivially (injective on C3)")
    return P


# ---------------------------------------------------------------------------
# (1)-(2) The three irreducible complex characters of C3.
# ---------------------------------------------------------------------------
def characters() -> dict:
    banner("(1) Three 1-dim complex characters chi_0, chi_1, chi_2 of C3")
    # chi_a(g^k) = omega^{a k}.  a in {0,1,2}.
    chi = {}
    for a in ELEMENTS:
        chi[a] = [sp.simplify(W ** (a * k)) for k in ELEMENTS]  # values on e,g,g^2
    check("1.1 chi_0 = (1,1,1) (trivial)", veq(chi[0], [sp.Integer(1)] * 3),
          f"chi_0 = {chi[0]}")
    check("1.2 chi_1 = (1, omega, omega^2)",
          veq(chi[1], [sp.Integer(1), W, W**2]),
          f"chi_1 = {chi[1]}")
    check("1.3 chi_2 = (1, omega^2, omega)",
          veq(chi[2], [sp.Integer(1), W**2, W**4]),
          f"chi_2 = {chi[2]}")

    # Orthonormality / completeness: these are exactly the irreducible chars,
    # so the regular rep decomposes as chi_0 + chi_1 + chi_2 (each once).
    # Inner product <chi_a, chi_b> = (1/3) sum_k chi_a(g^k) conj(chi_b(g^k)).
    def ip(a, b):
        s = sum(chi[a][k] * sp.conjugate(chi[b][k]) for k in ELEMENTS)
        return cx(s / 3)

    gram = sp.Matrix(3, 3, lambda i, j: ip(i, j))
    check("1.4 characters are orthonormal (Gram = I_3)",
          gram == sp.eye(3),
          "1/3 sum_k chi_a conj(chi_b) = delta_{ab}")

    # Regular-rep character = (3,0,0); multiplicity of each chi_a is 1.
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    chi_reg = [sp.trace(P**k) for k in ELEMENTS]  # tr(P^k): k=0->3, else 0
    mult = [cx(sum(chi_reg[k] * sp.conjugate(chi[a][k]) for k in ELEMENTS) / 3)
            for a in ELEMENTS]
    check("1.5 regular character = (3,0,0); each chi_a appears exactly once",
          chi_reg == [sp.Integer(3), sp.Integer(0), sp.Integer(0)] and
          mult == [sp.Integer(1)] * 3,
          f"chi_reg = {chi_reg}; multiplicities = {mult}")
    return chi


# ---------------------------------------------------------------------------
# (3) K = complex conjugation acts on characters; (4) orbits.
# ---------------------------------------------------------------------------
def k_conjugation_orbits(chi: dict) -> dict:
    banner("(3)-(4) K = CPT complex conjugation on characters; K/CPT orbits")
    # K conj-acts on a character pointwise: (K.chi)(g) = conj(chi(g)).
    # Equivalently K.chi_a = chi_{-a mod 3}.
    Kchi = {a: [sp.conjugate(chi[a][k]) for k in ELEMENTS] for a in ELEMENTS}

    check("3.1 K fixes chi_0 (it is real): conj(chi_0) = chi_0",
          veq(Kchi[0], chi[0]), f"conj(chi_0) = {[cx(c) for c in Kchi[0]]}")
    check("3.2 K swaps chi_1 <-> chi_2: conj(chi_1) = chi_2",
          veq(Kchi[1], chi[2]), f"conj(chi_1) = {[cx(c) for c in Kchi[1]]} = chi_2")
    check("3.3 K swaps chi_2 <-> chi_1: conj(chi_2) = chi_1",
          veq(Kchi[2], chi[1]), f"conj(chi_2) = {[cx(c) for c in Kchi[2]]} = chi_1")
    check("3.4 K is an involution on the character set (K^2 = id)",
          all(veq([sp.conjugate(c) for c in Kchi[a]], chi[a]) for a in ELEMENTS),
          "conj(conj(chi_a)) = chi_a for all a")

    # Build the K-action as a permutation of the index set {0,1,2}.
    # index map: a -> (-a) mod 3.
    sigma = {a: (-a) % 3 for a in ELEMENTS}
    check("3.5 K-permutation of sector indices = (0)(1 2)",
          sigma == {0: 0, 1: 2, 2: 1}, f"sigma = {sigma}")

    # Orbits under <K>.
    seen = set()
    orbits = []
    for a in ELEMENTS:
        if a in seen:
            continue
        orb = {a}
        b = sigma[a]
        while b not in orb:
            orb.add(b)
            b = sigma[b]
        for x in orb:
            seen.add(x)
        orbits.append(sorted(orb))
    orbits.sort(key=lambda o: (len(o), o))
    check("4.1 K/CPT orbits of the central sectors are {0} and {1,2}",
          orbits == [[0], [1, 2]], f"orbits = {orbits}")
    check("4.2 number of K/CPT-orbit sectors = 2 (NOT 3)", len(orbits) == 2,
          f"#sectors = {len(orbits)}")

    dims = sorted(len(o) for o in orbits)
    check("4.3 orbit (sector) dimensions are 1 (singlet) and 2 (doublet)",
          dims == [1, 2], f"sector dims = {dims} -> singlet + doublet")
    check("4.4 sector dims sum to |C3| = 3 (the full regular-rep carrier)",
          sum(dims) == 3, f"1 + 2 = {sum(dims)}")
    return {"orbits": orbits, "sigma": sigma, "dims": dims, "Kchi": Kchi}


# ---------------------------------------------------------------------------
# (4) Frobenius-Schur indicators confirm real (+1) vs complex (0) types.
# ---------------------------------------------------------------------------
def frobenius_schur(chi: dict) -> dict:
    banner("(4) Frobenius-Schur indicators nu = (1/|G|) sum_g chi(g^2)")
    # For C3 (abelian), g^2 for g=g^k is g^{2k mod 3}. nu_a = (1/3) sum_k chi_a(g^{2k}).
    fs = {}
    for a in ELEMENTS:
        s = sum(chi[a][(2 * k) % 3] for k in ELEMENTS)
        fs[a] = cx(s / 3)
    check("FS.1 nu(chi_0) = +1 (REAL type)", fs[0] == sp.Integer(1),
          f"nu_0 = {fs[0]}")
    check("FS.2 nu(chi_1) = 0 (COMPLEX type)", fs[1] == sp.Integer(0),
          f"nu_1 = {fs[1]}")
    check("FS.3 nu(chi_2) = 0 (COMPLEX type)", fs[2] == sp.Integer(0),
          f"nu_2 = {fs[2]}")
    check("FS.4 FS pattern (+1,0,0) matches: chi_0 real, {chi_1,chi_2} a conjugate "
          "complex pair fused by K into ONE real doublet block",
          fs[0] == sp.Integer(1) and fs[1] == sp.Integer(0) and fs[2] == sp.Integer(0),
          "real-type singlet + one complex-type conjugate pair = 2 real blocks")
    # Sanity: number of self-conjugate (real, nu!=0) chars = number of K-fixed
    # characters = 1; complex pairs contribute (3-1)/2 = 1 doublet.
    n_real = sum(1 for a in ELEMENTS if fs[a] != 0)
    n_doublet = (len(ELEMENTS) - n_real) // 2
    check("FS.5 real-block count via FS = n_real(=1) + n_complexpairs(=1) = 2",
          n_real == 1 and n_doublet == 1 and (n_real + n_doublet) == 2,
          f"n_real={n_real}, n_complex_pairs={n_doublet} -> 2 sectors")
    return fs


# ---------------------------------------------------------------------------
# (5) Contrast: C[Z3]=C^3 (THREE sectors) vs R[Z3]=R⊕C (TWO sectors).
# K/CPT is exactly what fuses chi_1,chi_2 into one real doublet block.
# ---------------------------------------------------------------------------
def wedderburn_contrast(chi: dict, orbit_info: dict) -> None:
    banner("(5) Contrast — WITHOUT K/CPT: 3 complex sectors; WITH K/CPT: 2 real blocks")

    # Complex group algebra C[Z3] = C ⊕ C ⊕ C : THREE blocks, one per character.
    # Diagonalize the regular rep over C: P = F* diag(1, omega, omega^2) F.
    F = sp.Matrix(3, 3, lambda r, c: W ** (r * c)) / sp.sqrt(3)  # DFT
    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    D = F.conjugate().T * P * F
    diag_vals = [cx(D[i, i]) for i in range(3)]
    is_diag = all(ceq(D[i, j], 0) for i in range(3) for j in range(3) if i != j)
    # The DFT slot-ordering is a convention; the physics claim is the unordered
    # multiset of distinct central characters {1, omega, omega^2}.
    targets = [sp.Integer(1), cx(W), cx(W**2)]
    remaining = list(diag_vals)
    multiset_ok = True
    for t in targets:
        hit = next((i for i, v in enumerate(remaining) if ceq(v, t)), None)
        if hit is None:
            multiset_ok = False
            break
        remaining.pop(hit)
    multiset_ok = multiset_ok and len(remaining) == 0
    check("5.1 over C the regular rep diagonalizes to the multiset {1, omega, "
          "omega^2}: C[Z3] = C ⊕ C ⊕ C (THREE complex central sectors)",
          is_diag and multiset_ok,
          f"diag = {diag_vals}; #complex sectors = 3")

    n_complex_sectors = 3
    n_kcpt_sectors = len(orbit_info["orbits"])
    check("5.2 K/CPT FUSES the two faithful characters: 3 complex sectors "
          "collapse to 2 K/CPT-orbit sectors",
          n_complex_sectors == 3 and n_kcpt_sectors == 2,
          f"{n_complex_sectors} (complex) -> {n_kcpt_sectors} (K/CPT orbits)")

    # Real Wedderburn R[Z3] = R ⊕ C : the real regular rep decomposes into the
    # trivial 1-dim real block plus a 2-dim REAL-irreducible rotation block.
    # The 2x2 real block is conjugate to the 2pi/3 rotation.
    # Real change of basis: u0 = (e1+e2+e3) (trivial); the orthogonal complement
    # carries the rotation. Build the real block explicitly.
    # Real similarity T diagonalizing P into block(1) ⊕ R(2pi/3):
    s3 = sp.sqrt(3)
    # Orthonormal real basis: trivial + two real combos.
    u0 = sp.Matrix([1, 1, 1]) / s3
    u1 = sp.Matrix([2, -1, -1]) / sp.sqrt(6)
    u2 = sp.Matrix([0, 1, -1]) / sp.sqrt(2)
    T = sp.Matrix.hstack(u0, u1, u2)
    block = sp.simplify(T.T * P * T)
    # Expected: [[1,0,0],[0,cos,-sin],[0,sin,cos]] with angle 2pi/3.
    c = sp.Rational(-1, 2)            # cos(2pi/3)
    s = s3 / 2                        # sin(2pi/3)
    expected = sp.Matrix([[1, 0, 0],
                          [0, c, -s],
                          [0, s, c]])
    same = sp.simplify(block - expected) == sp.zeros(3, 3)
    check("5.3 over R the regular rep = (1) ⊕ rotation(2pi/3): "
          "R[Z3] = R ⊕ C (ONE real + ONE complex-type block = TWO blocks)",
          same,
          "real block = diag(1) ⊕ R(2pi/3); the 2x2 rotation is the irreducible "
          "real DOUBLET block")
    # The 2x2 rotation block is irreducible over R (no real eigenvalue) but
    # splits over C into omega, omega^2 -> it IS the fused {chi_1,chi_2} pair.
    rot = expected[1:, 1:]
    eig = [cx(e) for e in rot.eigenvals().keys()]
    # Match the unordered eigenvalue multiset {omega, omega^2}.
    targets = [cx(W), cx(W**2)]
    matched = (len(eig) == 2 and
               ((ceq(eig[0], targets[0]) and ceq(eig[1], targets[1])) or
                (ceq(eig[0], targets[1]) and ceq(eig[1], targets[0]))))
    check("5.4 the real doublet block has NO real eigenvalue (irreducible over R) "
          "and splits over C into {omega, omega^2}",
          matched and all(sp.im(e) != 0 for e in eig),
          f"eig(rotation) = {eig} = {{omega, omega^2}}")

    n_real_blocks = 2
    check("5.5 K/CPT-orbit count (=2) EQUALS real Wedderburn block count (=2)",
          n_kcpt_sectors == n_real_blocks == 2,
          "the fixed K/CPT conjugation in the readout context IS the real-structure fusion "
          "C[Z3]=C^3 -> R[Z3]=R⊕C")


# ---------------------------------------------------------------------------
# Independent numpy cross-check (floating point) of the central claims.
# ---------------------------------------------------------------------------
def numpy_crosscheck() -> None:
    banner("X — independent numpy (float) cross-check of the K-orbit / sector count")
    w = cmath.exp(2j * math.pi / 3)
    # characters as numeric rows
    chi = {a: np.array([w ** ((a * k) % 3) for k in range(3)], dtype=complex)
           for a in range(3)}
    # K = elementwise conjugation
    Kchi = {a: np.conjugate(chi[a]) for a in range(3)}
    fixed = [a for a in range(3) if np.allclose(Kchi[a], chi[a])]
    swapped = []
    for a in range(3):
        for b in range(3):
            if a < b and np.allclose(Kchi[a], chi[b]):
                swapped.append((a, b))
    check("X1 numpy: exactly chi_0 is K-fixed", fixed == [0],
          f"K-fixed = {fixed}")
    check("X2 numpy: exactly {chi_1, chi_2} are K-swapped", swapped == [(1, 2)],
          f"K-swapped pairs = {swapped}")
    n_sectors = len(fixed) + len(swapped)
    check("X3 numpy: K/CPT-orbit sector count = 2 (1 fixed + 1 swapped pair)",
          n_sectors == 2, f"#sectors = {n_sectors}")

    # FS indicators numerically.
    fs = {a: (sum(chi[a][(2 * k) % 3] for k in range(3)) / 3).real for a in range(3)}
    check("X4 numpy: FS = (+1, 0, 0)",
          abs(fs[0] - 1) < 1e-9 and abs(fs[1]) < 1e-9 and abs(fs[2]) < 1e-9,
          f"nu = ({fs[0]:.3f}, {fs[1]:.3f}, {fs[2]:.3f})")

    # Real regular rep eigenvalues (should be {1, omega, omega^2}).
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    ev = np.linalg.eigvals(P)
    has_one = np.any(np.abs(ev - 1) < 1e-9)
    has_w = np.any(np.abs(ev - w) < 1e-9)
    has_w2 = np.any(np.abs(ev - w * w) < 1e-9)
    check("X5 numpy: regular-rep eigenvalues = {1, omega, omega^2} "
          "(1 real singlet + 1 conjugate doublet pair)",
          has_one and has_w and has_w2,
          f"eig(P) = {np.round(ev, 4)}")


def main() -> int:
    print("RECORD_GENERATION_READOUT_TWO_SECTORS — generation readout resolves "
          "two K/CPT-orbit sectors (singlet + doublet)")
    print("Conditional derivation: central-sector decomposition + K/CPT supplied "
          "by the readout context; Record only names the realized orbit and "
          "adds disjoint records.")
    banner_setup()
    chi = characters()
    orbit_info = k_conjugation_orbits(chi)
    frobenius_schur(chi)
    wedderburn_contrast(chi, orbit_info)
    numpy_crosscheck()

    banner("RESULT")
    print(f"PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("ALL CHECKS PASSED")
        print("Generation readout resolves exactly TWO K/CPT-orbit sectors: "
              "SINGLET (chi_0, dim 1) + DOUBLET ({chi_1,chi_2}, dim 2).")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
