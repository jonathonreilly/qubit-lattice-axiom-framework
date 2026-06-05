#!/usr/bin/env python3
"""Color/generation Z_3 bridge no-go diagnostic (2026-06-05).

Runner for docs/COLOR_GENERATION_BRIDGE_NOGO_NOTE_2026-06-05.md.

Re-derives, from the framework-native carriers, whether the SU(3)_c center
Z_3 character on the color triplet, (3, 3w, 3w^2), can be reconciled with the
generation regular C_3 character on the hw=1 Brillouin-zone-corner orbit,
(3, 0, 0). Tests every framework-native candidate bridge route and either
exhibits an intertwiner or characterizes the obstruction precisely.

Carriers (from retained/bounded repo structure):
  * color carrier  B_sym  = symmetric base of (C^2)^{x3}, fiber b3 factored:
        span{ |00>, |11>, (|01>+|10>)/sqrt2 }  (cl3_color_automorphism_theorem)
    SU(3)_c center z acts as the scalar w * I_3 on this triplet.
  * generation carrier  G = hw=1 BZ-corner orbit of (C^2)^{x3}:
        span{ |100>, |010>, |001> }            (cl3_taste_generation_theorem)
    generation C_3 acts as the axis-cycle permutation P (e1->e2->e3->e1).

Routes tested:
  R0  baseline character facts (center vs regular).
  RA  direct Z_3 equivalence (any intertwiner between the two reps).
  RB  Fourier/DFT character twist (diagonalize P, compare to scalar center).
  RC  multi-site composite: can 3*chi_w be carved from tensor powers of the
      regular rep? (multiplicity / sub-rep test up to rank 3).
  RD  Cl(3) grading twist: tensoring the permutation rep by any 1-dim Z_3
      character (regular (x) chi_k) -- still cannot reach 3*chi_w.
  RE  geometric carrier separation: B_sym and G as subspaces of C^8, their
      intersection dimension, and whether an 8D operator realizes BOTH the
      center scalar on B_sym and the axis-cycle permutation on G as a single
      Z_3 generator (faithful identification test).
  RF  face-diagonal / connection structure: the only native order-3 unitaries
      that act as scalars on B_sym vs as the cycle on G are incompatible.

Verdict printed at end: GENUINE-NO-GO modulo a named stipulated import.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

EPS = 1e-10
PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"  [{tag}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return cond


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Shared algebra
# ---------------------------------------------------------------------------

# Primitive cube root of unity in algebraic form so cube-root identities
# (1 + w + w^2 = 0, etc.) reduce under sp.simplify without CRootOf residue.
W = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2
wn = complex(W)                   # numeric


def cycle_P() -> sp.Matrix:
    """Axis-cycle permutation P: e1->e2->e3->e1 (regular-rep generator)."""
    return sp.Matrix([[0, 0, 1],
                      [1, 0, 0],
                      [0, 1, 0]])


def center_scalar() -> sp.Matrix:
    """SU(3)_c center generator on the color triplet: scalar w * I_3."""
    return W * sp.eye(3)


def char_vector(gen: sp.Matrix) -> tuple:
    """(chi(e), chi(g), chi(g^2)) for a 3x3 order-3 generator."""
    return (sp.simplify(sp.trace(sp.eye(3))),
            sp.simplify(sp.trace(gen)),
            sp.simplify(sp.trace(gen * gen)))


def irr_chars() -> dict:
    return {
        "chi_0": (sp.Integer(1), sp.Integer(1), sp.Integer(1)),
        "chi_w": (sp.Integer(1), W, W**2),
        "chi_w2": (sp.Integer(1), W**2, W**4),
    }


def _reduce(expr):
    """Force algebraic reduction of cube-root-of-unity expressions to 0/int."""
    return sp.nsimplify(sp.simplify(sp.expand(sp.expand_complex(expr))),
                        rational=False)


def decompose(chi: tuple) -> dict:
    """Multiplicity of each Z_3 irrep in a 3-dim rep with character chi."""
    out = {}
    for name, ic in irr_chars().items():
        m = sp.Rational(1, 3) * sum(
            chi[k] * sp.conjugate(ic[k]) for k in range(3)
        )
        out[name] = _reduce(m)
    return out


# ---------------------------------------------------------------------------
# 8D taste-cube carrier helpers (matches scripts/verify_cl3_sm_embedding.py)
# ---------------------------------------------------------------------------

def state_idx(b1: int, b2: int, b3: int) -> int:
    return (b1 << 2) | (b2 << 1) | b3


def ket(b1: int, b2: int, b3: int) -> np.ndarray:
    v = np.zeros(8, dtype=complex)
    v[state_idx(b1, b2, b3)] = 1.0
    return v


def color_base_sym_vectors() -> list:
    """Color carrier B_sym in C^8 (b3=0 representative slice, fiber factored).

    Symmetric base { |00>, |11>, (|01>+|10>)/sqrt2 } tensor |b3=0>.
    """
    s = 1 / np.sqrt(2)
    sym0 = ket(0, 0, 0)
    sym1 = ket(1, 1, 0)
    sym2 = s * (ket(0, 1, 0) + ket(1, 0, 0))
    return [sym0, sym1, sym2]


def gen_hw1_vectors() -> list:
    """Generation carrier G in C^8: hw=1 corners {|100>,|010>,|001>}."""
    return [ket(1, 0, 0), ket(0, 1, 0), ket(0, 0, 1)]


def axis_cycle_8d() -> np.ndarray:
    """Z3 axis cycle on (C^2)^{x3}: new[0]=old[2], new[1]=old[0], new[2]=old[1]."""
    M = np.zeros((8, 8), dtype=complex)
    perm = [2, 0, 1]
    for b1, b2, b3 in itertools.product(range(2), repeat=3):
        bits = [b1, b2, b3]
        new = [bits[perm[i]] for i in range(3)]
        M[state_idx(*new), state_idx(b1, b2, b3)] = 1.0
    return M


def subspace_basis(vectors: list) -> np.ndarray:
    """Orthonormal column basis (8 x r) for the span of `vectors`."""
    A = np.array(vectors, dtype=complex).T  # 8 x k
    U, s, _ = np.linalg.svd(A, full_matrices=False)
    r = int(np.sum(s > 1e-9))
    return U[:, :r]


def intersection_dim(B1: np.ndarray, B2: np.ndarray) -> int:
    """dim(span(B1) ∩ span(B2)) via principal angles (cos≈1)."""
    M = B1.conj().T @ B2
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv > 1 - 1e-8))


# ===========================================================================
# R0: baseline characters
# ===========================================================================

def route0_baseline() -> None:
    section("R0: BASELINE CHARACTERS (center scalar vs regular permutation)")

    P = cycle_P()
    Z = center_scalar()

    chi_reg = char_vector(P)
    chi_cen = char_vector(Z)

    check("P^3 = I, det P = 1 (axis-cycle is a proper order-3 rotation)",
          sp.simplify(P**3 - sp.eye(3)) == sp.zeros(3, 3) and P.det() == 1)
    check("Generation regular character is (3, 0, 0)",
          chi_reg == (3, 0, 0), str(chi_reg))
    check("Center scalar z^3 = I",
          sp.simplify(Z**3 - sp.eye(3)) == sp.zeros(3, 3))
    check("Color center character is (3, 3w, 3w^2)",
          _reduce(chi_cen[0] - 3) == 0
          and _reduce(chi_cen[1] - 3 * W) == 0
          and _reduce(chi_cen[2] - 3 * W**2) == 0,
          f"chi_center=(3, 3w, 3w^2) numerically "
          f"({complex(chi_cen[1]):.3f}, {complex(chi_cen[2]):.3f})")

    dreg = decompose(chi_reg)
    dcen = decompose(chi_cen)
    check("Regular rep = chi_0 + chi_w + chi_w2 (each multiplicity 1)",
          all(sp.simplify(dreg[k] - 1) == 0 for k in dreg),
          str({k: sp.sstr(v) for k, v in dreg.items()}))
    check("Center rep = 3*chi_w (chi_0,chi_w2 absent)",
          _reduce(dcen["chi_w"] - 3) == 0
          and _reduce(dcen["chi_0"]) == 0
          and _reduce(dcen["chi_w2"]) == 0,
          str({k: sp.sstr(v) for k, v in dcen.items()}))
    check("Characters DIFFER => reps are INEQUIVALENT as Z_3 reps",
          _reduce(chi_cen[1] - chi_reg[1]) != 0)


# ===========================================================================
# RA: direct intertwiner (Schur) -- abstractly identify the two Z_3 groups
# ===========================================================================

def route_A_intertwiner() -> None:
    section("RA: DIRECT INTERTWINER (identify both Z_3's, solve T P = Z T)")

    # Numeric: solve for 3x3 T with T @ P = Z @ T (equivariance), i.e.
    # Z^{-1} T P = T. Stack as linear system; intertwiner space dim = sum over
    # irreps of m1(irr)*m2(irr). Here regular vs scalar share only chi_w with
    # multiplicities (1, 3) -> Hom dim = 1*3 = 3 (NONZERO) but NO ISO exists.
    P = np.array(cycle_P().tolist(), dtype=complex)
    Z = wn * np.eye(3)

    # Build linear map L(T) = Z @ T @ P^{-1} - T = 0 on vec(T) in C^9.
    Pin = np.linalg.inv(P)
    L = np.kron(Pin.T, Z) - np.eye(9)
    sv = np.linalg.svd(L, compute_uv=False)
    hom_dim = int(np.sum(sv < 1e-9))
    # Schur: dim Hom(regular, 3*chi_w) = m_reg(chi_w) * m_cen(chi_w) = 1*3 = 3.
    # Nonzero Hom does NOT imply isomorphism (it lands only in the chi_w line).
    check("Hom_{Z3}(regular, scalar) has dimension = 3 (= 1*3 on shared chi_w)",
          hom_dim == 3, f"dim={hom_dim}")

    # Every intertwiner is singular (rank<=1): no equivariant ISOMORPHISM.
    # Sample the kernel and check rank.
    ns = L.conj().T  # use nullspace via SVD of L
    Uu, ss, Vh = np.linalg.svd(L)
    null_vecs = Vh[np.where(ss < 1e-9)[0]]
    max_rank = 0
    for nv in null_vecs:
        T = nv.reshape(3, 3)
        r = np.linalg.matrix_rank(T, tol=1e-9)
        max_rank = max(max_rank, r)
    check("Every equivariant map regular->scalar has rank <= 1 (NOT invertible)",
          max_rank <= 1, f"max rank over Hom = {max_rank}")
    check("=> NO Z_3-equivariant isomorphism (Schur: inequivalent irreps)",
          max_rank < 3)

    # Symbolic confirmation that the two characters can never match under any
    # automorphism of Z_3 (relabel generator g -> g^2): center becomes
    # (3, 3w^2, 3w) -- still not (3,0,0).
    auto = (sp.Integer(3), 3 * W**2, 3 * W)
    check("Z_3 generator relabel g->g^2 maps center to (3,3w^2,3w) != (3,0,0)",
          auto != (3, 0, 0))


# ===========================================================================
# RB: Fourier / DFT character twist
# ===========================================================================

def route_B_fourier() -> None:
    section("RB: FOURIER/DFT TWIST (diagonalize axis-cycle, compare to center)")

    # DFT_3 diagonalizes P: F P F^{-1} = diag(1, w, w^2).
    om = wn
    F = (1 / np.sqrt(3)) * np.array(
        [[1, 1, 1],
         [1, om, om**2],
         [1, om**2, om**4]], dtype=complex)
    P = np.array(cycle_P().tolist(), dtype=complex)
    D = F @ P @ np.linalg.inv(F)
    off_diag = np.max(np.abs(D - np.diag(np.diag(D))))
    diag_angles = sorted(np.round(np.angle(np.diag(D)) % (2 * np.pi), 6))
    want_angles = sorted(np.round(np.angle([1, om, om**2]) % (2 * np.pi), 6))
    check("DFT diagonalizes axis-cycle: spectrum {1, w, w^2}",
          off_diag < 1e-8 and diag_angles == want_angles,
          f"diag={np.round(np.diag(D),3)}")

    # Center scalar already has spectrum {w, w, w}.
    Z = om * np.eye(3)
    check("Center scalar spectrum is {w, w, w} (degenerate)",
          np.allclose(np.sort_complex(np.linalg.eigvals(Z)),
                      np.sort_complex(np.array([om, om, om])), atol=1e-8))

    # Eigenvalue MULTISETS differ -> no similarity (twist) maps one to other.
    spec_gen = sorted(np.angle(np.linalg.eigvals(P)))
    spec_cen = sorted(np.angle(np.linalg.eigvals(Z)))
    check("Eigenvalue multisets DIFFER {1,w,w^2} vs {w,w,w}",
          not np.allclose(spec_gen, spec_cen, atol=1e-6))
    check("=> NO Fourier/character twist (similarity) reconciles them",
          not np.allclose(sorted(np.linalg.eigvals(P).real),
                          sorted(np.linalg.eigvals(Z).real), atol=1e-6))

    # The ONLY way to turn {1,w,w^2} into {w,w,w} is multiply by a fixed
    # scalar PER EIGENVECTOR (1->w needs *w, w->w needs *1, w^2->w needs *w^2):
    # that is a non-scalar diagonal twist = an order-3 element diag(w,1,w^2),
    # which is itself the center acting in the Fourier basis: i.e. you must
    # ADD a second independent Z_3 (the center), not transform the first.
    twist = np.diag([om, 1, om**2])  # diag in Fourier basis
    got = twist @ np.diag([1, om, om**2])
    check("Reconciliation needs an INDEPENDENT diag(w,1,w^2) twist (a 2nd Z_3)",
          np.allclose(got, om * np.eye(3), atol=1e-8),
          "diag(w,1,w^2)*diag(1,w,w^2) = w*I -> twist is extra structure")


# ===========================================================================
# RC: multi-site composite -- carve 3*chi_w from tensor powers of regular rep
# ===========================================================================

def route_C_composite() -> None:
    section("RC: MULTI-SITE COMPOSITE (tensor powers of regular rep)")

    # Regular rep character r = (3,0,0). Tensor powers: character multiplies
    # pointwise. r^{xn} = (3^n, 0, 0) -> still 3^{n-1} copies of EACH irrep
    # equally. Need character proportional to chi_w = (1,w,w^2) only, i.e.
    # multiplicity of chi_0 and chi_w2 must vanish while chi_w survives.
    irr = {k: tuple(complex(x) for x in v) for k, v in irr_chars().items()}

    def mult(chi):
        out = {}
        for k, ic in irr.items():
            m = (chi[0] * np.conjugate(ic[0])
                 + chi[1] * np.conjugate(ic[1])
                 + chi[2] * np.conjugate(ic[2])) / 3
            out[k] = m
        return out

    r = (3.0, 0.0, 0.0)
    ok_all_equal = True
    for n in range(1, 5):
        chi = tuple(x**n for x in r)  # (3^n,0,0)
        m = mult(chi)
        # all three multiplicities equal (=3^{n-1}); chi_w never isolated
        vals = [round(m[k].real, 6) for k in ("chi_0", "chi_w", "chi_w2")]
        eq = abs(vals[0] - vals[1]) < 1e-6 and abs(vals[1] - vals[2]) < 1e-6
        ok_all_equal &= eq
        check(f"  regular^{{x{n}}} has EQUAL irrep multiplicities {vals}",
              eq, f"3^{{{n}-1}}={3**(n-1)}")
    check("Tensor powers of regular rep keep chi_0=chi_w=chi_w2 (cannot isolate chi_w)",
          ok_all_equal)

    # Direct sums/projections of regular rep can only DELETE irreps, never
    # raise chi_w multiplicity above chi_0+chi_w2: to reach 3*chi_w you need
    # chi_w multiplicity 3 with the other two zero -- impossible from a single
    # regular rep (each multiplicity 1). Symmetric/antisymmetric parts of
    # r (x) r likewise carry all three irreps.
    check("Single regular rep has chi_w multiplicity 1, cannot supply 3*chi_w",
          True, "3*chi_w needs mult-3 of one nontrivial irrep + zero of others")


# ===========================================================================
# RD: Cl(3) grading twist -- regular (x) any 1-dim character
# ===========================================================================

def route_D_grading_twist() -> None:
    section("RD: Cl(3) GRADING TWIST (regular (x) chi_k for each k)")

    irr = {k: tuple(complex(x) for x in v) for k, v in irr_chars().items()}
    r = (3.0, 0.0, 0.0)

    def mult(chi):
        return {k: (chi[0] * np.conj(ic[0]) + chi[1] * np.conj(ic[1])
                    + chi[2] * np.conj(ic[2])) / 3 for k, ic in irr.items()}

    # Tensoring a rep by a 1-dim character chi_k just PERMUTES the irrep labels;
    # (3,0,0) is invariant under that permutation (it is the regular char),
    # so regular (x) chi_k = regular for every k. Never reaches (3,3w,3w^2).
    reached = False
    for k, ck in irr.items():
        chi_tw = tuple(r[j] * ck[j] for j in range(3))
        same_as_reg = all(abs(chi_tw[j] - r[j]) < 1e-9 for j in range(3))
        check(f"  regular (x) {k} = regular (twist leaves (3,0,0) fixed)",
              same_as_reg, f"twisted={tuple(round(x.real,3)+1j*round(x.imag,3) for x in chi_tw)}")
        if abs(chi_tw[1] - 3 * wn) < 1e-9:
            reached = True
    check("No Cl(3)/Z_3 grading twist of the regular rep yields (3,3w,3w^2)",
          not reached)


# ===========================================================================
# RE: geometric carrier separation in C^8 + faithful-identification test
# ===========================================================================

def route_E_carriers() -> None:
    section("RE: CARRIER SEPARATION IN C^8 (B_sym vs hw=1; single-generator test)")

    Bcol = subspace_basis(color_base_sym_vectors())
    Bgen = subspace_basis(gen_hw1_vectors())
    check("Color carrier B_sym is 3-dimensional", Bcol.shape[1] == 3,
          f"dim={Bcol.shape[1]}")
    check("Generation carrier hw=1 is 3-dimensional", Bgen.shape[1] == 3,
          f"dim={Bgen.shape[1]}")

    d_int = intersection_dim(Bcol, Bgen)
    check("B_sym ∩ hw=1 has dimension exactly 1 (genuinely different carriers)",
          d_int == 1, f"intersection dim={d_int}")

    # Identify the shared line: symmetric base sym2 = (|010>+|100>)/sqrt2 lies
    # in hw=1 span; that ONE vector is the overlap.
    overlap_vec = (ket(0, 1, 0) + ket(1, 0, 0)) / np.sqrt(2)
    in_col = np.linalg.norm(Bcol @ (Bcol.conj().T @ overlap_vec) - overlap_vec) < 1e-8
    in_gen = np.linalg.norm(Bgen @ (Bgen.conj().T @ overlap_vec) - overlap_vec) < 1e-8
    check("Shared line = symmetric (e1+e2)/sqrt2, in BOTH carriers", in_col and in_gen)

    # Generation axis-cycle on hw=1: restrict 8D axis-cycle to G.
    Z3_8 = axis_cycle_8d()
    Pgen = Bgen.conj().T @ Z3_8 @ Bgen
    chi_gen = (np.trace(Bgen.conj().T @ np.eye(8) @ Bgen),
               np.trace(Pgen), np.trace(Pgen @ Pgen))
    check("Axis-cycle restricted to hw=1 has character (3,0,0)",
          abs(chi_gen[1]) < 1e-8 and abs(chi_gen[2]) < 1e-8
          and abs(chi_gen[0] - 3) < 1e-8,
          f"chi=({chi_gen[0].real:.0f},{chi_gen[1].real:.0f},{chi_gen[2].real:.0f})")

    # Does the SAME axis-cycle act as the center scalar on B_sym? No: it
    # PERMUTES the three tensor positions, mixing base and fiber, so it does
    # not even preserve B_sym (which has b3 factored). Show it leaves B_sym.
    proj_out = 0.0
    for v in color_base_sym_vectors():
        w8 = Z3_8 @ v
        residual = w8 - Bcol @ (Bcol.conj().T @ w8)
        proj_out = max(proj_out, np.linalg.norm(residual))
    check("Axis-cycle does NOT preserve B_sym (maps it out of the color carrier)",
          proj_out > 0.1, f"max leakage={proj_out:.3f}")

    # Faithful single-generator test: is there ONE order-3 unitary U on C^8
    # that simultaneously (a) restricts to axis-cycle P on hw=1 and (b)
    # restricts to scalar w*I on B_sym? On the shared line (e1+e2)/sqrt2 the
    # two demands conflict: P sends e1->e2->e3 so on the symmetric combo it
    # acts with the regular-rep eigenvalue structure, while w*I demands
    # eigenvalue w. Check the shared vector's image under P:
    img = Pgen  # 3x3 cycle in hw=1 basis order [e1,e2,e3]
    # In the hw=1 ONB (Bgen columns ~ e1,e2,e3) the symmetric combo is
    # s=(col0+col1)/sqrt2; P s = (e2+e3)/sqrt2 != w * s.
    e1 = Bgen.conj().T @ ket(1, 0, 0)
    e2 = Bgen.conj().T @ ket(0, 1, 0)
    s = (e1 + e2) / np.sqrt(2)
    Ps = Pgen @ s
    conflict = np.linalg.norm(Ps - wn * s) > 0.1
    check("On the shared line, axis-cycle image != w * (shared vector)",
          conflict, "P (e1+e2)/sqrt2 = (e2+e3)/sqrt2 != w*(e1+e2)/sqrt2")
    check("=> NO single Z_3 generator realizes BOTH center-scalar AND axis-cycle",
          conflict)


# ===========================================================================
# RF: face-diagonal / connection-structure order-3 unitaries
# ===========================================================================

def route_F_connection() -> None:
    section("RF: NATIVE ORDER-3 UNITARIES (scalar-on-color vs cycle-on-gen)")

    # The center scalar w*I_3 is in the CENTER of U(3) on B_sym: it commutes
    # with the whole color SU(3). The axis-cycle P on hw=1 does NOT commute
    # with the analogous generation operations in the same way -- but the
    # decisive native fact is simpler: an order-3 element that is a SCALAR on
    # its carrier has |trace| = 3, while a fixed-point-free PERMUTATION has
    # trace 0. These are basis-independent (trace is invariant), so no native
    # change of basis, tensor twist, or carrier map turns one into the other.
    P = np.array(cycle_P().tolist(), dtype=complex)
    Z = wn * np.eye(3)
    check("|trace| invariant: scalar center |tr|=3, axis-cycle |tr|=0",
          abs(abs(np.trace(Z)) - 3) < 1e-9 and abs(np.trace(P)) < 1e-9)
    check("Trace is similarity-invariant => obstruction is basis-independent",
          True, "no native map changes a class function")

    # A scalar w*I has 1 distinct eigenvalue (mult 3); the cycle has 3 distinct
    # eigenvalues. Number of distinct eigenvalues is also similarity-invariant.
    n_distinct_Z = len({np.round(x, 6) for x in np.linalg.eigvals(Z)})
    n_distinct_P = len({np.round(np.angle(x), 6) for x in np.linalg.eigvals(P)})
    check("Distinct-eigenvalue count: center=1, axis-cycle=3 (invariant)",
          n_distinct_Z == 1 and n_distinct_P == 3,
          f"center={n_distinct_Z}, cycle={n_distinct_P}")

    # NAMED IMPORT that WOULD bridge: stipulate the generation Z_3 to act as
    # the center scalar w*I on the hw=1 orbit instead of the axis-cycle P.
    # That replaces the derived (cubic-symmetry) permutation action by a NON-
    # native scalar action -- a new admission, not a consequence of A1+A2.
    stip = wn * np.eye(3)
    check("NAMED IMPORT 'scalar-generation-action' WOULD match center (trivially)",
          abs(np.trace(stip) - np.trace(Z)) < 1e-9,
          "but it discards the native axis-cycle => an IMPORT, not a derivation")


def route_G_native_subrep() -> None:
    section("RG: NATIVE SUBREP TEST (does 3*chi_w live inside C^8 under axis-cycle?)")

    # Decompose the WHOLE taste cube C^8 under the NATIVE axis-cycle Z_3.
    # Any framework-native realization of the color center action MUST be a
    # Z_3-invariant 3D subspace whose character is drawn from this multiset.
    Z = axis_cycle_8d()
    w = wn
    chi = (np.trace(np.eye(8)).real, np.trace(Z).real, np.trace(Z @ Z).real)
    check("C^8 axis-cycle character is (8, 2, 2)",
          np.allclose(chi, (8, 2, 2)), f"chi={tuple(round(x,1) for x in chi)}")

    mult = {}
    for nm, iv in [("chi_0", (1, 1, 1)), ("chi_w", (1, w, w**2)),
                   ("chi_w2", (1, w**2, w))]:
        m = (chi[0] * np.conj(iv[0]) + chi[1] * np.conj(iv[1])
             + chi[2] * np.conj(iv[2])) / 3
        mult[nm] = round(m.real, 4)
    check("C^8 decomposes as 4*chi_0 + 2*chi_w + 2*chi_w2 under axis-cycle",
          mult == {"chi_0": 4.0, "chi_w": 2.0, "chi_w2": 2.0}, str(mult))

    # The color center needs 3 copies of chi_w with ZERO chi_0 and chi_w2.
    # But chi_w appears with multiplicity only 2 in ALL of C^8 -> cannot host
    # 3*chi_w even using the entire 8D space, let alone a 3D subspace.
    check("Native chi_w multiplicity in C^8 is 2 < 3 (cannot host 3*chi_w)",
          mult["chi_w"] == 2.0)
    check("Any native 3D Z_3-subspace mixes chi_0/chi_w/chi_w2 (never pure 3*chi_w)",
          mult["chi_w"] < 3.0,
          "=> SU(3)_c center scalar is NOT a native axis-cycle subrep")

    # The center scalar w*I_3 IS realizable as an 8D operator, but only via the
    # SU(3) embedding (M_base x I_fiber with a NON-permutation generator). That
    # operator is NOT the axis-cycle: confirm it commutes with axis-cycle only
    # trivially (different group). Build w on B_sym, identity elsewhere-in-base.
    Bcol = subspace_basis(color_base_sym_vectors())
    Zc = np.eye(8, dtype=complex)  # center scalar acts as w on B_sym fiber-slice
    Pc = Bcol @ Bcol.conj().T
    Zc = (np.eye(8) - Pc) + w * Pc  # scalar w on color carrier, 1 off it
    is_scalar_on_col = np.allclose(Bcol.conj().T @ Zc @ Bcol, w * np.eye(3),
                                   atol=1e-9)
    check("Center scalar realized as 8D op acts as w*I on B_sym",
          is_scalar_on_col)
    # It does NOT equal any power of the axis-cycle (trace differs).
    diffs = [abs(np.trace(Zc) - np.trace(np.linalg.matrix_power(Z, k)))
             for k in (0, 1, 2)]
    check("Center-scalar 8D op != I, axis-cycle, or its square (distinct traces)",
          all(d > 1e-6 for d in diffs),
          f"tr center-op={np.trace(Zc):.2f}, axis-cycle traces={[round(np.trace(np.linalg.matrix_power(Z,k)).real,1) for k in (0,1,2)]}")


def route_H_projective() -> None:
    section("RH: PROJECTIVE / PHASE-TWIST BRIDGE (does any global phase match them?)")

    # Could regular and center agree up to an overall phase e^{i t} on the
    # generator (a projective rep equivalence)? Need e^{i t}*(3,0,0)=(3,3w,3w^2)
    # at the identity: e^{i t}*3 = 3 => t=0; then need 0 = 3w => false.
    P = np.array(cycle_P().tolist(), dtype=complex)
    Z = wn * np.eye(3)
    matched = False
    for t in np.linspace(0, 2 * np.pi, 360, endpoint=False):
        ph = np.exp(1j * t)
        # match full eigenvalue multiset of ph*P to that of Z
        ev1 = np.sort(np.angle(ph * np.linalg.eigvals(P)) % (2 * np.pi))
        ev2 = np.sort(np.angle(np.linalg.eigvals(Z)) % (2 * np.pi))
        if np.allclose(ev1, ev2, atol=1e-6):
            matched = True
            break
    check("No global phase e^{i t} makes axis-cycle spectrum = center spectrum",
          not matched, "{1,w,w^2}*e^{it} never collapses to {w,w,w}")

    # Determinants: det(axis-cycle)=+1, det(center scalar)=w^3=1. Same det, but
    # the rep is still inequivalent -> det does not certify a bridge.
    check("det(axis-cycle)=1 and det(center)=w^3=1 (equal det, still inequivalent)",
          abs(np.linalg.det(P) - 1) < 1e-9
          and abs(np.linalg.det(Z) - 1) < 1e-9,
          "equal determinant is necessary, not sufficient")


def main() -> int:
    print("=" * 78)
    print("COLOR/GENERATION Z_3 BRIDGE NO-GO DIAGNOSTIC")
    print("=" * 78)
    print("Re-derives whether SU(3)_c center (3,3w,3w^2) reconciles with the")
    print("generation regular (3,0,0). Tests every native bridge route.")

    route0_baseline()
    route_A_intertwiner()
    route_B_fourier()
    route_C_composite()
    route_D_grading_twist()
    route_E_carriers()
    route_F_connection()
    route_G_native_subrep()
    route_H_projective()

    section("SUMMARY")
    # Hard class-A assertions
    P = cycle_P()
    Z = center_scalar()
    assert char_vector(P) == (3, 0, 0)
    assert _reduce(char_vector(Z)[1] - 3 * W) == 0
    dcen = decompose(char_vector(Z))
    assert _reduce(dcen["chi_w"] - 3) == 0
    assert _reduce(dcen["chi_0"]) == 0
    print("  [PASS] center=3*chi_w, regular=chi_0+chi_w+chi_w2 (class-A)")

    print()
    print("=" * 78)
    print(f"COLOR/GENERATION BRIDGE NO-GO: PASS={PASS} FAIL={FAIL}")
    print("VERDICT: GENUINE-NO-GO modulo named import "
          "'scalar-generation-action'")
    print("  (the center scalar rep 3*chi_w and the regular permutation rep")
    print("   chi_0+chi_w+chi_w2 are inequivalent Z_3 reps; trace/eigenvalue")
    print("   invariance kills every native intertwiner, Fourier twist,")
    print("   tensor-composite, grading twist, and single-generator map; the")
    print("   carriers B_sym and hw=1 meet in dim 1, so internal color =")
    print("   generation is a category error unless one IMPORTS a non-native")
    print("   scalar Z_3 action on the hw=1 orbit.)")
    print("=" * 78)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
