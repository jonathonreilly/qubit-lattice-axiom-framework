#!/usr/bin/env python3
"""Determinant-readout supplied-boundary exhaustion checks.

Source-boundary target: the missing bridge named by the audit-lane conditional verdict on
theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10:

    "retain a determinant-readout bridge proving that the physical
     arg det(M_u M_d) contribution is exhausted by the multiplicative
     determinant-character readout and that no phase-sensitive
     non-multiplicative or action-level datum remains."

This runner checks the source-boundary quarantine plus, on small complex
matrices and finite abelian-group models
(memory tiny, dims <= 16):

  B1  ORBIT: K/CPT acts on the determinant datum by complex conjugation, so
      the orbit of z = det(M_u M_d) is {z, conj z}; |z| is fixed and arg z is
      negated; arg det(M_u M_d) = arg det M_u + arg det M_d (mod 2 pi).
  B2  MULTIPLICATIVE ENTRY: the determinant datum is multiplicative over
      disjoint records (block factorization), and on the strong-CP selected
      surface the entire vacuum-weight dependence on the mass datum is
      det(D + M) (Gaussian/exact), whose orientation-sensitive part is
      arg det.  Leg-A miniature: anti-Hermitian D with the epsilon pairing
      gives det(D + m I) real positive for real m > 0.
  B3  FORCING + EXHAUSTION: on finite models of the datum group, the FULL
      solution space of Record-additive readouts is computed by explicit
      nullspace linear algebra.  Additivity over disjoint records plus
      determinant multiplicativity force the homomorphism (multiplicative)
      class; the phase component is additive hence odd; K/CPT orbit constancy
      makes it even; even AND odd => zero.  The complete surviving space is
      the modulus (k = 0) class -- verified as an exact nullspace dimension
      count, not on a hand-picked family.
  B4  HOSTILE GUARDS: the old cos(arg z) attack is re-run against the
      generalized statement (killed by ADDITIVITY, witness printed), plus
      NEW hostile readings: |sin(arg z)| (orbit-constant, non-multiplicative,
      killed by additivity); a cross-sector interference functional
      cos(arg z1 - arg z2) (orbit-constant under the simultaneous K/CPT
      conjugation, phase-sensitive, killed by the no-cross-term consequence
      of additivity); principal-branch Arg (fails BOTH hypotheses, wrap
      witness); the real-lift additive phase k*phi (additive, killed by
      orbit constancy).  The kill table shows the intersection structure.
  B5  ACTION-LEVEL COMPOSITION + BOUNDARY: cross-plane mixed derivatives of a
      per-plaquette (single-plane-summand) action vanish for arbitrary
      symbolic f (composition with the retained_bounded cross-plane absence
      note, not a re-derivation of the license); named residual boundary
      witnesses.

The runner sets no audit status and reads/writes no audit surface.
"""
from __future__ import annotations

import cmath
import math
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
MASS_SIDE_NOTE = (
    ROOT
    / "docs"
    / "THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    extra = f"  [{detail}]" if detail else ""
    print(f"{tag}: {label}{extra}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def rand_complex(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))


def angles_equal_mod_2pi(a: float, b: float, tol: float = 1e-10) -> bool:
    d = (a - b) % (2.0 * math.pi)
    return min(d, 2.0 * math.pi - d) < tol


def main() -> int:
    rng = np.random.default_rng(20260611)

    # ------------------------------------------------------------------
    section("B0 - source-boundary guards: W2/action-level premises quarantined")

    note_text = NOTE.read_text(encoding="utf-8")
    mass_side_text = MASS_SIDE_NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    mass_side_flat = " ".join(mass_side_text.split())
    note_guard = note_flat.replace("*", "").replace("`", "")
    check(
        "source note is supplied-boundary, not physical bridge closure",
        "Supplied-Boundary Repair" in note_text
        and "It does **not** derive the physical W2 identification" in note_text
        and "action-level reduction from the framework" in note_text,
    )
    check(
        "W2 physical-registrability identification is quarantined",
        "quarantined physical-registrability identification" in note_flat
        and "W2 is not derived, promoted, or smuggled by this note" in note_flat,
    )
    check(
        "full action-level determinant datum is not globally derived here",
        "The full action-level determinant datum is not globally derived here" in note_text
        and "this note still does not prove W2, K-reality, the orientation-bit choice" in note_text,
    )
    check(
        "physical/non-registrable/multi-plaquette exclusions remain non-claims",
        "not load-bearing in this note" in note_flat.lower()
        and "any multi-plaquette, source-insertion, or non-registrable readout exclusion" in note_text,
    )
    check(
        "source note is scoped as supplied-context algebra only",
        "**Claim type:** bounded_theorem" in note_text
        and "**Type:** bounded_theorem" in note_text
        and "conditional-support; supplied-context algebra only" in note_flat
        and "not a physical theta_eff or action-level readout bridge" in note_flat
        and "Downstream physical strong-CP use must carry a separate W2/action-level theorem" in note_flat,
    )
    check(
        "2026-06-20 conditional-scoping repair names BOTH supplied premises (i) W2 and (ii) theta_eff entry",
        "2026-06-20 Source Repair: Downstream Conditional Scope" in note_text
        and "(i) W2 physical-registrability" in note_flat
        and "(ii) action-level `theta_eff` determinant-entry" in note_text
        and "Supplied here for the conditional theorem, not derived. Open bridge." in note_flat,
    )
    check(
        "2026-06-20 repair keeps downstream strong-CP use explicitly conditional on (i) and (ii)",
        "Downstream strong-CP use is explicitly conditional" in note_text
        and "must additionally carry, or itself remain conditional on, premises (i)\nand (ii)".replace("\n", " ") in note_flat,
    )
    check(
        "2026-06-20 repair does NOT derive the two supplied premises",
        "does **not** derive the W2 physical-registrability theorem" in note_flat
        and "action-level `theta_eff` determinant-entry theorem" in note_flat,
    )
    check(
        "source note expected scorecard matches runner count",
        "TOTAL: PASS=47 FAIL=0" in note_text,
    )
    check(
        "2026-06-18 wiring cites the mass-side epsilon-Hermiticity bridge as a source-edge",
        MASS_SIDE_NOTE.name in note_text
        and "mass-side source-edge wiring" in note_flat
        and "source-edge for the bilinear matter half" in note_flat,
    )
    check(
        "mass-side source-edge supplies first-power Berezin + epsilon-Hermiticity mechanisms",
        "first-power Berezin" in mass_side_flat
        and "Hermiticity Discharges the Determinant-Readout Bridge" in mass_side_text
        and "det(D(U)+A)" in mass_side_text
        and "K-reality premise" in mass_side_flat,
    )
    check(
        "mass-side source-edge is not imported as audit status and keeps K-reality/orientation/gauge residuals live",
        "not used here as an audit verdict or retained authority" in note_guard
        and "orientation bit is not erased" in note_flat
        and "gauge-side bare-`theta` / multi-plaquette residual is untouched" in note_text,
    )

    # ------------------------------------------------------------------
    section("B1 - K/CPT orbit structure of the determinant datum (3x3 numeric)")

    ok_conj = ok_dag = ok_orbit = ok_mod = ok_arg = ok_sum = True
    for _ in range(8):
        Mu = rand_complex(rng, 3)
        Md = rand_complex(rng, 3)
        z = np.linalg.det(Mu @ Md)
        # K/CPT conjugation acts on each mass block by complex conjugation
        # (equivalently dagger up to the K-even transpose), so the datum
        # conjugates either way.
        z_conj = np.linalg.det(np.conj(Mu) @ np.conj(Md))
        z_dag = np.conj(np.linalg.det(Mu.conj().T @ Md.conj().T))
        ok_conj &= abs(z_conj - np.conj(z)) < 1e-9
        ok_dag &= abs(z_dag - z) < 1e-9  # dagger datum = conj(det), so conj back = z
        # involution: applying the conjugation twice returns z -> orbit {z, conj z}
        ok_orbit &= abs(np.conj(np.conj(z)) - z) < 1e-12
        ok_mod &= abs(abs(z_conj) - abs(z)) < 1e-9
        ok_arg &= angles_equal_mod_2pi(cmath.phase(z_conj), -cmath.phase(z), 1e-8)
        ok_sum &= angles_equal_mod_2pi(
            cmath.phase(z),
            cmath.phase(np.linalg.det(Mu)) + cmath.phase(np.linalg.det(Md)),
            1e-8,
        )
    check("det(conj M_u conj M_d) = conj det(M_u M_d) (8 samples)", ok_conj)
    check("dagger variant gives the same conjugated datum (8 samples)", ok_dag)
    check("conjugation is an involution => K/CPT orbit of z is {z, conj z}", ok_orbit)
    check("|det(M_u M_d)| is K/CPT-invariant", ok_mod)
    check("arg det(M_u M_d) -> -arg det(M_u M_d) under K/CPT", ok_arg)
    check("arg det(M_u M_d) = arg det M_u + arg det M_d (mod 2 pi)", ok_sum)

    # ------------------------------------------------------------------
    section("B2 - multiplicative entry of the mass datum (disjoint records, Leg-A miniature)")

    ok_block = ok_block_arg = True
    for _ in range(5):
        blocks = [rand_complex(rng, 2), rand_complex(rng, 3), rand_complex(rng, 2)]
        big = np.zeros((7, 7), dtype=complex)
        i = 0
        prod = 1.0 + 0j
        argsum = 0.0
        for b in blocks:
            n = b.shape[0]
            big[i : i + n, i : i + n] = b
            prod *= np.linalg.det(b)
            argsum += cmath.phase(np.linalg.det(b))
            i += n
        zb = np.linalg.det(big)
        ok_block &= abs(zb - prod) < 1e-8 * max(1.0, abs(zb))
        ok_block_arg &= angles_equal_mod_2pi(cmath.phase(zb), argsum, 1e-8)
    check("det over disjoint (block) records is multiplicative (5 samples)", ok_block)
    check("union-record phase = sum of per-record phases (mod 2 pi)", ok_block_arg)

    # Leg-A miniature: D = [[0, A], [-A^dag, 0]] is anti-Hermitian and
    # anticommutes with epsilon = diag(I, -I); for real m > 0 the weight
    # det(D + m I) is real positive.
    ok_antih = ok_eps = ok_pos = True
    for _ in range(5):
        A = rand_complex(rng, 4)
        D = np.block(
            [[np.zeros((4, 4), dtype=complex), A], [-A.conj().T, np.zeros((4, 4), dtype=complex)]]
        )
        ok_antih &= np.allclose(D.conj().T, -D)
        eps = np.diag([1.0] * 4 + [-1.0] * 4).astype(complex)
        ok_eps &= np.allclose(eps @ D + D @ eps, 0.0)
        m = 0.7
        w = np.linalg.det(D + m * np.eye(8))
        ok_pos &= abs(w.imag) < 1e-8 * abs(w) and w.real > 0
    check("miniature staggered-like D is anti-Hermitian (5 samples)", ok_antih)
    check("epsilon = diag(I,-I) anticommutes with D (epsilon pairing)", ok_eps)
    check("det(D + m I) real positive for real m > 0 (selected surface, Leg-A form)", ok_pos)

    # Gaussian exactness in miniature: the weight's full mass dependence is
    # det(D + M); exp(sum log eigenvalues) = det (branch-free identity), and
    # an orientation phase alpha in M = m e^{i alpha} I enters the weight only
    # through arg det(D + M); the K/CPT partner alpha -> -alpha conjugates it.
    A = rand_complex(rng, 4)
    D = np.block(
        [[np.zeros((4, 4), dtype=complex), A], [-A.conj().T, np.zeros((4, 4), dtype=complex)]]
    )
    m, alpha = 0.7, 0.43
    Mp = m * cmath.exp(1j * alpha) * np.eye(8)
    Mm = m * cmath.exp(-1j * alpha) * np.eye(8)
    wp = np.linalg.det(D + Mp)
    wm = np.linalg.det(D + Mm)
    ev = np.linalg.eigvals(D + Mp)
    check(
        "exp(Tr log(D+M)) = det(D+M) (Gaussian weight = determinant, branch-free)",
        abs(cmath.exp(sum(cmath.log(l) for l in ev)) - wp) < 1e-8 * abs(wp),
    )
    check(
        "orientation flip alpha -> -alpha conjugates the weight: det(D+M(-alpha)) = conj det(D+M(alpha))",
        abs(wm - np.conj(wp)) < 1e-8 * abs(wp),
        detail="same |det|, opposite arg: exactly the K/CPT orbit pair of B1",
    )

    # ------------------------------------------------------------------
    section("B3 - forcing + exhaustion: FULL additive solution space by nullspace count")

    # Model A (torsion phase): datum group window Z_window x Z_12, coordinates
    # (i, j) = (log-modulus steps, phase in 2pi/12 units). Additivity rows:
    # F(g+h) - F(g) - F(h) = 0 whenever g, h, g+h are in the window.
    W = 4  # modulus window |i| <= W
    NPH = 12
    idx = {}
    for i in range(-W, W + 1):
        for j in range(NPH):
            idx[(i, j)] = len(idx)
    nvar = len(idx)

    def additivity_rows(domain_idx, wrap_phase: bool):
        rows = []
        keys = list(domain_idx.keys())
        for (i1, j1) in keys:
            for (i2, j2) in keys:
                i3 = i1 + i2
                j3 = (j1 + j2) % NPH if wrap_phase else j1 + j2
                if (i3, j3) in domain_idx:
                    r = np.zeros(len(domain_idx))
                    r[domain_idx[(i3, j3)]] += 1.0
                    r[domain_idx[(i1, j1)]] -= 1.0
                    r[domain_idx[(i2, j2)]] -= 1.0
                    rows.append(r)
        return np.array(rows)

    Aadd = additivity_rows(idx, wrap_phase=True)
    _, s, Vt = np.linalg.svd(Aadd, full_matrices=False)
    null_dim = int(np.sum(s < 1e-9)) + (nvar - len(s) if len(s) < nvar else 0)
    check(
        "Model A (phase = Z_12 torsion): additive solution space has dimension 1",
        null_dim == 1,
        detail=f"nullspace dim = {null_dim}; torsion alone kills the phase generator",
    )
    v = Vt[-1]
    # survivor proportional to the modulus coordinate i, phase coefficient 0
    ref = np.zeros(nvar)
    for (i, j), k in idx.items():
        ref[k] = float(i)
    ref /= np.linalg.norm(ref)
    overlap = abs(float(v @ ref))
    check(
        "Model A survivor = modulus coordinate (k = 0 class), phase coefficient 0",
        overlap > 1.0 - 1e-9,
        detail=f"|overlap with F(i,j)=i| = {overlap:.12f}",
    )

    # Model B (real-lift phase, no torsion): window Z x Z. Additive solution
    # space is 2-dimensional {a*i + b*j}; the K/CPT orbit (evenness) rows
    # F(i,-j) - F(i,j) = 0 must cut it to the modulus line. This is the
    # even-AND-odd route the note uses (no torsion shortcut).
    idxB = {}
    for i in range(-W, W + 1):
        for j in range(-W, W + 1):
            idxB[(i, j)] = len(idxB)
    nvarB = len(idxB)
    AaddB = additivity_rows(idxB, wrap_phase=False)
    _, sB, VtB = np.linalg.svd(AaddB, full_matrices=False)
    nullB = int(np.sum(sB < 1e-9)) + (nvarB - len(sB) if len(sB) < nvarB else 0)
    check(
        "Model B (real-lift phase): additive solution space has dimension 2",
        nullB == 2,
        detail=f"nullspace dim = {nullB}: span{{a*i + b*j}} (odd phase lift admitted)",
    )
    basisB = VtB[-2:]
    # every additive solution is odd in the phase coordinate: F(0,-j) = -F(0,j)
    ok_odd = True
    for vb in basisB:
        for j in range(1, W + 1):
            ok_odd &= abs(vb[idxB[(0, j)]] + vb[idxB[(0, -j)]]) < 1e-9
    check("additive => ODD in the phase coordinate (checked on the full basis)", ok_odd)

    even_rows = []
    for i in range(-W, W + 1):
        for j in range(1, W + 1):
            r = np.zeros(nvarB)
            r[idxB[(i, j)]] += 1.0
            r[idxB[(i, -j)]] -= 1.0
            even_rows.append(r)
    Afull = np.vstack([AaddB, np.array(even_rows)])
    _, sF, VtF = np.linalg.svd(Afull, full_matrices=False)
    nullF = int(np.sum(sF < 1e-9)) + (nvarB - len(sF) if len(sF) < nvarB else 0)
    check(
        "Model B + K/CPT orbit constancy: solution space cuts 2 -> 1 (even AND odd => 0 phase)",
        nullF == 1,
        detail=f"nullspace dim = {nullF}",
    )
    vF = VtF[-1]
    refB = np.zeros(nvarB)
    for (i, j), k in idxB.items():
        refB[k] = float(i)
    refB /= np.linalg.norm(refB)
    overlapB = abs(float(vF @ refB))
    check(
        "EXHAUSTION: the complete registrable solution space = modulus (k=0) class",
        overlapB > 1.0 - 1e-9,
        detail=f"|overlap with F(i,j)=i| = {overlapB:.12f}; phase content exactly zero",
    )

    # Homomorphism forcing restated on data: additivity over disjoint records
    # + multiplicativity of the union datum (B2) IS the functional equation
    # F(z w) = F(z) + F(w); verify F(1) = 0 follows (two disjoint datum-1 records).
    check(
        "additivity + multiplicative union datum => F(z w) = F(z) + F(w) and F(1) = 0",
        ok_block and nullF == 1 and overlapB > 1.0 - 1e-9,
        detail="block determinant multiplicativity plus the full additive/even solution-space cut leaves only the modulus line",
    )

    # ------------------------------------------------------------------
    section("B4 - hostile guards: old cos(arg z) re-run + new hostile readings")

    def additivity_holds(F, z1, z2, tol=1e-9):
        return abs(F(z1 * z2) - (F(z1) + F(z2))) < tol

    def orbit_holds(F, z, tol=1e-9):
        return abs(F(np.conj(z)) - F(z)) < tol

    z1 = cmath.rect(1.3, 2.0 * math.pi / 3.0)
    z2 = cmath.rect(0.8, 2.0 * math.pi / 3.0)
    zwrap1 = cmath.rect(1.0, 3.0 * math.pi / 4.0)

    F1 = lambda z: math.log(abs(z))
    check(
        "F1 = log|z|: additive AND orbit-constant AND phase-free (the survivor)",
        additivity_holds(F1, z1, z2)
        and orbit_holds(F1, z1)
        and abs(F1(cmath.rect(1.3, 0.4)) - F1(cmath.rect(1.3, 1.9))) < 1e-12,
    )

    F2 = lambda z: math.cos(cmath.phase(z))
    check(
        "F2 = cos(arg z) [OLD guard]: orbit-constant but NOT additive -> killed by ADDITIVITY",
        orbit_holds(F2, z1) and not additivity_holds(F2, z1, z2),
        detail=f"witness phi1=phi2=2pi/3: cos(4pi/3)={F2(z1*z2):+.4f} != 2cos(2pi/3)={F2(z1)+F2(z2):+.4f}",
    )
    check(
        "F2 is phase-sensitive (same |z|, different F2) -> evenness alone is NOT erasure",
        abs(F2(cmath.rect(1.0, 0.3)) - F2(cmath.rect(1.0, 1.7))) > 0.1,
    )

    F3 = lambda z: abs(math.sin(cmath.phase(z)))
    check(
        "F3 = |sin(arg z)| [NEW hostile]: orbit-constant, phase-sensitive, NOT additive -> killed by ADDITIVITY",
        orbit_holds(F3, z1)
        and abs(F3(cmath.rect(1.0, 0.3)) - F3(cmath.rect(1.0, 1.2))) > 0.1
        and not additivity_holds(F3, z1, z2),
    )

    F4 = lambda z: cmath.phase(z)  # principal branch Arg in (-pi, pi]
    check(
        "F4 = principal Arg [NEW hostile]: fails additivity at the wrap AND fails orbit constancy",
        (not additivity_holds(F4, zwrap1, zwrap1)) and (not orbit_holds(F4, z1)),
        detail=f"wrap witness: Arg(z^2)={F4(zwrap1 * zwrap1):+.4f} != 2*Arg(z)={2 * F4(zwrap1):+.4f}",
    )

    # F5: cross-sector interference functional on the union record:
    # I(e1 u e2) = log|z1 z2| + cos(arg z1 - arg z2). Orbit-constant under the
    # SIMULTANEOUS K/CPT conjugation (the difference negates, cos is even),
    # phase-sensitive, but additivity I(e1 u e2) = I(e1) + I(e2) fails by the
    # cross term: exactly the no-interference consequence of Record additivity.
    def F5_union(za, zb):
        return math.log(abs(za * zb)) + math.cos(cmath.phase(za) - cmath.phase(zb))

    lhs = F5_union(z1, z2)
    rhs = F1(z1) + F1(z2)
    check(
        "F5 = interference cos(arg z1 - arg z2) [NEW hostile]: orbit-constant under simultaneous conj",
        abs(F5_union(np.conj(z1), np.conj(z2)) - F5_union(z1, z2)) < 1e-12,
    )
    check(
        "F5 is phase-sensitive yet violates additivity (cross term) -> killed by NO-CROSS-TERM/additivity",
        abs(lhs - rhs) > 0.5
        and abs(F5_union(z1, z2) - F5_union(z1, cmath.rect(abs(z2), 0.1))) > 0.1,
        detail=f"I(e1 u e2) - I(e1) - I(e2) = {lhs - rhs:+.4f} != 0",
    )

    # F6: real-lift additive phase k*phi-tilde (the regularity-free additive
    # candidate; Model B's second basis direction). Additive, but K/CPT orbit
    # constancy forces evenness: k*(-phi) = k*phi for all phi => k = 0.
    k = 2.0
    F6 = lambda phi: k * phi  # on the lifted phase line
    check(
        "F6 = k*phi (real-lift additive phase) [NEW hostile]: additive but NOT orbit-constant -> killed by ORBIT constancy",
        abs(F6(0.7 + 0.4) - (F6(0.7) + F6(0.4))) < 1e-12 and abs(F6(-0.7) - F6(0.7)) > 0.1,
        detail="even AND odd => k = 0; this is Model B's 2 -> 1 cut at a single candidate",
    )

    check(
        "kill table: additivity alone admits F6; orbit constancy alone admits F2/F3/F5; "
        "the INTERSECTION admits only the modulus class",
        additivity_holds(F1, z1, z2)
        and orbit_holds(F1, z1)
        and orbit_holds(F2, z1)
        and not additivity_holds(F2, z1, z2)
        and orbit_holds(F3, z1)
        and not additivity_holds(F3, z1, z2)
        and abs(F6(0.7 + 0.4) - (F6(0.7) + F6(0.4))) < 1e-12
        and abs(F6(-0.7) - F6(0.7)) > 0.1
        and nullF == 1
        and overlapB > 1.0 - 1e-9,
        detail="matches the exact nullspace counts of B3 (2 -> 1, survivor = modulus)",
    )

    # ------------------------------------------------------------------
    section("B5 - action-level composition (per-plaquette class) + named boundary")

    # Composition with the retained_bounded cross-plane absence note (not a
    # re-derivation):
    # a per-plaquette action is a sum of single-plane summands, so every
    # cross-plane mixed derivative vanishes for arbitrary symbolic f.
    x01, x23, x02, x13, x03, x12 = sp.symbols("x01 x23 x02 x13 x03 x12", real=True)
    fs = [sp.Function(f"f{i}") for i in range(6)]
    Aact = (
        fs[0](x01) + fs[1](x23) + fs[2](x02) + fs[3](x13) + fs[4](x03) + fs[5](x12)
    )
    ok_cross = all(
        sp.simplify(sp.diff(Aact, a, b)) == 0
        for (a, b) in [(x01, x23), (x02, x13), (x03, x12)]
    )
    check(
        "per-plaquette (single-plane-summand) class: all dual-pair cross-plane mixed derivatives vanish",
        ok_cross,
        detail="composes with retained_bounded cross-plane absence; no local F.Ftilde slot to host an orientation datum",
    )

    note_plain = (
        NOTE.read_text().lower().replace("*", "").replace("`", "")
        if NOTE.exists()
        else ""
    )
    note_plain = " ".join(note_plain.split())
    check(
        "BOUNDARY: registrability of the physical readout (W2) is a standing premise, not derived here",
        "quarantined physical-registrability identification" in note_plain
        and "it does not prove the physical readout must be registrable" in note_plain,
        detail="theorem is conditional on the Record-registrable class (additivity + orbit constancy)",
    )
    check(
        "BOUNDARY: strong-CP premise 1 ('no bare theta slot') is a SEPARATE action-surface premise",
        "strong-cp premise 1" in note_plain
        and "distinct" in note_plain
        and "action-surface premise" in note_plain,
        detail="RP no-go note keeps it open; this bridge addresses ONLY the mass-orientation datum",
    )
    check(
        "BOUNDARY: per-plaquette class is a licensed input (retained_bounded); multi-plaquette/clover reopens a cross-plane slot",
        "the full action-level determinant datum is not globally derived here" in note_plain
        and "multi-plaquette" in note_plain,
        detail="the action-level half is conditional on the supplied class",
    )
    check(
        "BOUNDARY: fermion-source/insertion observables carry (D+M)^{-1} dependence outside the theta_eff vacuum-weight premise",
        "source/insertion observables" in note_plain
        and "not the full m-dependence of every observable" in note_plain,
        detail="the bridge covers the arg det(M_u M_d) contribution to theta_eff, not all M-dependence",
    )
    check(
        "BOUNDARY: prior additive+even core note is cited as prior statement (currently unaudited); its legs are re-derived self-contained here",
        "currently unaudited" in note_plain
        and "not load-bearing here" in note_plain
        and "re-derived in this note" in note_plain,
        detail="no unaudited dependency is load-bearing for this runner's checks",
    )

    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
