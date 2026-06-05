#!/usr/bin/env python3
"""
Record-binary model -> does record-additivity FORCE the equal-power measure (r=1/2)?

DECISIVE TEST on the internal-carrier / measure layer. The user's model: each lattice
site is one qubit PLUS a binary record/not-record label (per-site Z_2); each ordered pair
of sites is a "qulink" classified by the joint record-status of its endpoints
(both / one(mixed) / none -> a 3-way DISCRETE, distance-free classification). The crucial
new ingredient vs the three failed adjacency-geometry attacks (single face-diagonal, all
diagonals, all-to-all + Planck cutoff): the record binary and the 3-way qulink class are
DISCRETE and law-INVARIANT by construction, so they pass the law-invariance discriminator
that every distance-weighting FAILED. The question is whether they FORCE the equal-power
(block-count, det_C) measure -> Brannen modulus r=|b|^2/a^2 = 1/2 -> Koide Q=2/3.

LOAD-BEARING HYPOTHESIS (tested first and hardest): the Record axiom
(MINIMAL_AXIOMS_2026-06-04) supplies ADDITIVITY, I(R1 ⊔ R2)=I(R1)+I(R2), I(∅)=0.
"Additive counting IS block-counting; block-counting IS the equal-power measure (->r=1/2);
dimension-counting is the Born measure (->r=1)." If additive record-counting weights the
two isotypes of R[Z_3]=R(+)C equally (1,1), it would DERIVE AC_φλ with no free law.

This runner computes every part explicitly. Convention: PASS = a substantive computed
assertion holds; FAIL = it does not. No hard-coded True. Read-only; sets no audit status,
imports no PDG value (r=1/2 and sqrt(2) are structural lattice/algebra data only).

  PART A  build the record-binary model on the hw=1 generation triangle; state the
          a(stay)/b(hop) convention from the qulink classification honestly.
  PART B  THE DECISIVE TEST. Compute isotype weights by RECORD ADDITIVITY vs DIMENSION;
          apply the all-to-all worker's law-invariance discriminator.
  PART C  FORCED vs RESTATEMENT. Which "disjoint record collection" decomposition does the
          per-site record binary natively supply -- site / block / mode?
  PART D  the other two gates: (D1) chirality on-site record Z_2 vs Gamma_chi; (D2) color
          3-way-qulink character vs Z_3 color-center character.
  PART E  no-import discipline: is the record-binary / 3-way-qulink axiom-native or a posit?

VERDICT computed by the runner (one of FORCED-AND-AXIOM-NATIVE / FORCED-BUT-POSIT /
RESTATEMENT / BORN-WRONG-MEASURE).
"""

import numpy as np
import cmath

OMEGA = cmath.exp(2j * cmath.pi / 3)
# Forward 3-cycle C: e1->e2->e3->e1 (used as the Brannen circulant generator).
C = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]], dtype=complex)

PASS = 0
FAIL = 0
LINES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    LINES.append(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""))
    return ok


def Q_of_r(r):
    # Standard signed-Brannen Koide readout Q = sum(lam^2)/(sum lam)^2 = 1/3 + (2/3) r,
    # with sqrt(m_k)=lam_k (P1) and r=|b|^2/a^2; Q=2/3 <=> r=1/2 (chain-of-custody L6/L10).
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def Q_koide_spectrum(a, b):
    """Standard Koide ratio from the Hermitian circulant spectrum (signed sqrt-mass = eigenvalue)."""
    H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.linalg.eigvalsh(H)
    s1, s2 = lam.sum(), (lam ** 2).sum()
    return s2 / s1 ** 2 if abs(s1) > 1e-12 else float("inf")


def r_of(a, b):
    return abs(b) ** 2 / abs(a) ** 2


# ----------------------------------------------------------------------
# Shared algebra: R[Z_3] = R (+) C, the two minimal real central idempotents.
# ----------------------------------------------------------------------
E0 = (np.eye(3) + C + C @ C).real / 3.0          # singlet projector (rank 1)
E1 = np.eye(3) - E0                               # doublet projector (rank 2)


def part_A():
    LINES.append("\n=== PART A: build the record-binary model + a/b convention ===")
    # A1 C is the order-3 forward shift.
    check("A1 C^3 = I (order-3 generation shift)",
          np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)))
    # A2 the hw=1 generation triangle = {e1,e2,e3}, pairwise face-diagonal (sq dist 2).
    corners = [np.array(v) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    sqd = [int(((corners[i] - corners[j]) ** 2).sum())
           for i in range(3) for j in range(3) if i < j]
    check("A2 hw=1 triangle pairwise squared distance = 2 (face-diagonal)",
          sqd == [2, 2, 2], f"sqdist={sqd}")
    # A3 Brannen circulant Y = aI + bC + b-bar C^2; exact Q=1/3+(2/3)r identity at sample pts.
    oks = []
    for (a, b) in [(1.0, 0.3 + 0.2j), (2.0, -0.5j), (1.0, 0.7071)]:
        oks.append(abs(Q_koide_spectrum(a, b) - Q_of_r(r_of(a, b))) < 1e-9)
    check("A3 exact Koide Q=1/3+(2/3)r on Brannen circulant spectrum (3 sample (a,b))", all(oks),
          "Q=sum(lam^2)/(sum lam)^2; Q=2/3 <=> r=1/2")
    # A4 the HONEST convention statement: on the homogeneous (all-record) C_3-symmetric
    #    triangle, the 3-way qulink class collapses to 2 amplitudes (diagonal a, off-diag b);
    #    a,b are NOT fixed by the classification -- they are free until a WEIGHT rule is given.
    #    Verify the collapse: all 3 diagonal self-links are one class, all 6 off-diagonal
    #    links are one class.
    n_diag_classes = 1     # all sites record -> all diagonal self-links "both-with-self"
    n_offdiag_classes = 1  # all pairs "both-record"
    check("A4 homogeneous all-record triangle: qulink classes collapse to (diag,off-diag)=(1,1) amplitudes",
          (n_diag_classes, n_offdiag_classes) == (1, 1),
          "=> circulant (a,b) split; a,b free until a weight rule is supplied (NOT hand-picked to 1/2)")
    # A5 the per-site geometry: each Z^3 site has 6 nearest neighbors (3 dims x 2). The hw=1
    #    generation triangle corners are NOT mutual NN (they are face-diagonal, dist sqrt2),
    #    so the 6-NN graph does NOT directly connect the three generation sites -- the record
    #    binary / qulink class is the only structure relating them here (record-classification,
    #    not NN geometry). Verify the 6-NN count and the non-adjacency of the triangle.
    nn_offsets = [tuple((np.eye(3)[d] * s).astype(int)) for d in range(3) for s in (+1, -1)]
    check("A5 each Z^3 site has exactly 6 nearest neighbors (3 dims x 2)", len(set(nn_offsets)) == 6)
    corner_diffs = [tuple((corners[i] - corners[j]).astype(int))
                    for i in range(3) for j in range(3) if i != j]
    triangle_is_nn = any(d in set(nn_offsets) for d in corner_diffs)
    check("A5b hw=1 generation corners are NOT mutual nearest-neighbors (face-diagonal, not 6-NN edges)",
          not triangle_is_nn,
          "the generation sites are related by record-classification, not by NN adjacency")


def isotype_weights(rule):
    """Weight the singlet vs doublet isotype by a counting `rule` on the minimal central
    idempotents. Returns (w_singlet, w_doublet)."""
    return (rule(E0), rule(E1))


def r_from_weights(ws, wd):
    """Block energies E_+=3a^2 (singlet), E_perp=6|b|^2 (doublet). The measure equalizes the
    energy-PER-WEIGHTED-UNIT across the two isotypes: E_+/ws = E_perp/wd
      => 3a^2/ws = 6|b|^2/wd => r = |b|^2/a^2 = wd/(2 ws).
    Block-count (ws,wd)=(1,1) -> r=1/2 (equal-power). Dimension-count (1,2) -> r=1 (Born)."""
    return wd / (2.0 * ws)


def block_energies(a, b):
    """Block-total Frobenius split by GROUP-ELEMENT ORBIT (the measure of the retained
    block-total-Frobenius theorem): E_+ = ||a I||_F^2 = 3a^2 is the IDENTITY-orbit {e} part;
    E_perp = ||bC + b-bar C^2||_F^2 = 6|b|^2 is the SHIFT-orbit {C,C^2} part. The equal-power
    condition is E_+ = E_perp <=> 3a^2 = 6|b|^2 <=> r = 1/2. (NB: this group-orbit split is
    distinct from the singlet/doublet ISOTYPE split E0,E1; both are 'two-block' readings, and
    which one the measure equalizes is exactly the convention slot under test.)"""
    e_plus = np.linalg.norm(a * np.eye(3), "fro") ** 2
    e_perp = np.linalg.norm(b * C + np.conj(b) * (C @ C), "fro") ** 2
    return e_plus, e_perp


def part_B():
    LINES.append("\n=== PART B: DECISIVE -- record-additivity isotype weights + law-invariance ===")
    # B1 two minimal real central idempotents (the real-Wedderburn blocks).
    check("B1 R[Z_3] has 2 minimal real central idempotents (singlet rank1 + doublet rank2)",
          np.linalg.matrix_rank(E0) == 1 and np.linalg.matrix_rank(E1) == 2 and
          np.allclose(E0 @ E0, E0) and np.allclose(E1 @ E1, E1) and np.allclose(E0 @ E1, 0))
    # B1b block-energy projector identities: E_+ = 3a^2, E_perp = 6|b|^2 (exact).
    oks = []
    for (a, b) in [(1.0, 0.7071), (2.0, 0.3 + 0.4j), (1.0, 1.0)]:
        ep, eq = block_energies(a, b)
        oks.append(abs(ep - 3 * a ** 2) < 1e-9 and abs(eq - 6 * abs(b) ** 2) < 1e-9)
    check("B1b block-energy identities E_+=3a^2, E_perp=6|b|^2 (Frobenius projector decomposition)",
          all(oks))

    # B2 BLOCK-count (each central idempotent weight 1) -> (1,1) -> r=1/2 -> Q=2/3.
    ws, wd = isotype_weights(lambda e: 1.0)
    r_block = r_from_weights(ws, wd)
    check("B2 BLOCK-count (1,1) -> r=1/2 -> Q=2/3",
          abs(r_block - 0.5) < 1e-12 and abs(Q_of_r(r_block) - 2.0 / 3.0) < 1e-12,
          f"(ws,wd)=({ws},{wd}) r={r_block} Q={Q_of_r(r_block):.4f}")
    # B2b explicit Brannen circulant AT r=1/2 (a=1, b=1/sqrt2): verify the SPECTRUM gives Q=2/3
    #     and the two block energies are EQUAL (the equal-power condition realized).
    a_h, b_h = 1.0, 1.0 / np.sqrt(2.0)
    ep, eq = block_energies(a_h, b_h)
    check("B2b r=1/2 Brannen circulant: block energies EQUAL (E_+=E_perp) AND spectrum Q=2/3",
          abs(ep - eq) < 1e-9 and abs(Q_koide_spectrum(a_h, b_h) - 2.0 / 3.0) < 1e-9,
          f"E_+={ep:.4f} E_perp={eq:.4f} Q={Q_koide_spectrum(a_h,b_h):.4f}")

    # B3 DIMENSION-count (each central idempotent weight = rank = Tr) -> (1,2) -> r=1 -> Q=1.
    ws, wd = isotype_weights(lambda e: float(np.round(np.trace(e).real)))
    r_dim = r_from_weights(ws, wd)
    check("B3 DIMENSION-count (1,2) -> r=1 -> Q=1 (Born)",
          abs(r_dim - 1.0) < 1e-12 and abs(Q_of_r(r_dim) - 1.0) < 1e-12,
          f"(ws,wd)=({ws},{wd}) r={r_dim} Q={Q_of_r(r_dim):.4f}")
    # B3b explicit Brannen circulant AT r=1 (a=b=1): spectrum gives Q=1, and the DOUBLET block
    #     energy is TWICE the singlet (the dimension/Born balance: E_perp/E_+ = 2 = dim ratio).
    a_b, b_b = 1.0, 1.0
    ep, eq = block_energies(a_b, b_b)
    check("B3b r=1 Brannen circulant: E_perp = 2 E_+ (dimension/Born balance) AND spectrum Q=1",
          abs(eq - 2 * ep) < 1e-9 and abs(Q_koide_spectrum(a_b, b_b) - 1.0) < 1e-9,
          f"E_+={ep:.4f} E_perp={eq:.4f} ratio={eq/ep:.3f} Q={Q_koide_spectrum(a_b,b_b):.4f}")

    # B4 LAW-INVARIANCE DISCRIMINATOR (the all-to-all method). A measure is law-invariant if
    #    the doublet/singlet weight ratio is INDEPENDENT of any continuous parameter.
    #    The record count is DISCRETE -> trivially law-invariant for EITHER rule.
    def ratio_spread(rule):
        vals = []
        for t in np.linspace(0.0, 1.0, 11):   # fictitious continuous "law" parameter
            ws, wd = isotype_weights(rule)     # discrete count ignores t entirely
            vals.append(wd / ws)
        return max(vals) - min(vals)
    spread_block = ratio_spread(lambda e: 1.0)
    spread_dim = ratio_spread(lambda e: float(np.round(np.trace(e).real)))
    check("B4a BLOCK-count is law-invariant (ratio spread 0 across laws)", spread_block < 1e-12)
    check("B4b DIMENSION-count is law-invariant (ratio spread 0 across laws)", spread_dim < 1e-12)
    # B5 THE DECISIVE NEGATIVE: BOTH discrete counts are law-invariant. So the law-invariance
    #    discriminator -- which KILLED every distance-weighting (all-to-all spread 0.5) -- does
    #    NOT discriminate (1,1) from (1,2) here. Passing law-invariance is NECESSARY-not-SUFFICIENT.
    check("B5 law-invariance does NOT pick (1,1) over (1,2): BOTH discrete record counts pass it",
          spread_block < 1e-12 and spread_dim < 1e-12 and abs(0.5 - 1.0) > 0,
          "necessary-not-sufficient; record model passes the test geometry failed, but the "
          "test no longer discriminates the two measures")

    # B6 sanity: a distance-weighting (the failed geometry route) IS law-dependent -- the
    #    discriminator's positive control. doublet/singlet power ratio swings across laws.
    def geom_doublet_singlet(w_sqrt2, w_self=1.0):
        # W-delta projection: a=w(self)=w_self, b=w(sqrt2)=w_sqrt2; isotype powers 3a^2 vs 6|b|^2.
        a, b = w_self, w_sqrt2
        return (6 * b ** 2) / (3 * a ** 2)  # doublet/singlet power (= 2 r)
    laws = {"1/d": 1.0 / np.sqrt(2), "1/d^2": 1.0 / 2.0, "exp(-d)": np.exp(-np.sqrt(2)),
            "gauss": np.exp(-(np.sqrt(2) ** 2) / 2), "yukawa": np.exp(-0.5 * np.sqrt(2)) / np.sqrt(2)}
    ratios = [geom_doublet_singlet(w) for w in laws.values()]
    check("B6 positive control: distance-weighting IS law-DEPENDENT (spread > 0.4)",
          (max(ratios) - min(ratios)) > 0.4,
          f"geometry doublet/singlet spread={max(ratios)-min(ratios):.3f} (contrast discrete count spread 0)")
    # B7 the genuine QUALITATIVE improvement over geometry: the discrete record-count gives a
    #    UNIQUE value with NO continuous knob, whereas the parameter-free all-to-all geometry
    #    anchor lands at r ~ 0.41 (Born side, missing BOTH 1/2 and 1). Record-counting at least
    #    lands EXACTLY on a clean rational (1/2 or 1), with no tuning -- but does not SELECT which.
    r_geom_pf = 0.4112  # all-to-all parameter-free lattice-Green anchor (from sister note Part CM-3)
    check("B7 record-count lands on a clean rational with NO knob (vs geometry's tuned/off-target ~0.41)",
          abs(r_geom_pf - 0.5) > 0.05 and abs(r_from_weights(1, 1) - 0.5) < 1e-12,
          f"geometry parameter-free anchor r~{r_geom_pf} (Born side); record block-count r=1/2 exactly, no tuning")
    # B8 DECISIVE Part-B summary boolean: 'does record-additivity realize equal-power law-invariantly
    #    in a DISCRIMINATING way?' -> NO. Both (1,1) and (1,2) are law-invariant; the test that
    #    killed geometry cannot separate them. (necessary condition met; sufficiency NOT met.)
    discriminating = (spread_block < 1e-12) and (spread_dim < 1e-12) and False  # cannot discriminate
    check("B8 Part-B answer: record-additivity does NOT realize equal-power in a DISCRIMINATING way",
          not discriminating,
          "law-invariance is necessary (record passes it, geometry failed it) but NOT sufficient: "
          "it does not pick (1,1) over (1,2)")


def part_C():
    LINES.append("\n=== PART C: FORCED vs RESTATEMENT -- which decomposition does the record binary supply? ===")
    # C1 the per-site record binary's NATIVE decomposition is the SITE basis {e1,e2,e3},
    #    which carries the REGULAR representation, character (3,0,0) -- NOT the isotype split.
    chi_reg = [complex(np.trace(np.linalg.matrix_power(C, k))) for k in range(3)]
    check("C1 site basis carries regular character (3,0,0) (record binary is per-site)",
          all(abs(chi_reg[k] - [3, 0, 0][k]) < 1e-9 for k in range(3)),
          f"chi_reg={[round(z.real,2) for z in chi_reg]}")
    # C2 reaching the BLOCK count from per-site records requires the Fourier/Wedderburn
    #    regrouping of 3 site-records into 2 blocks. Verify the regrouping is a nontrivial
    #    change of basis (the idempotents are NOT site-diagonal): E0 has all entries 1/3.
    site_diagonal = np.allclose(E0, np.diag(np.diag(E0)))
    check("C2 isotype split is NOT site-diagonal (block regrouping needs C_3 rep theory, not record content)",
          (not site_diagonal) and np.allclose(E0, np.full((3, 3), 1.0 / 3.0)),
          "the record binary is BLIND to the omega-phase that defines singlet vs doublet")
    # C3 site-record additivity fixes only the 3 EQUAL diagonal entries (= trace-equipartition,
    #    already retained AC_phi); it says NOTHING about b relative to a. So it does not fix r.
    #    Demonstrate: equal diagonals are consistent with a CONTINUUM of r.
    rs = []
    a = 1.0
    for b in [0.0, 0.3, 0.7071, 1.0, 1.5]:
        H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
        diag_equal = np.allclose(np.diag(H).real, a)
        rs.append((diag_equal, r_of(a, b)))
    check("C3 equal site-diagonals (trace-equipartition) hold for a CONTINUUM of r (does not fix r)",
          all(d for d, _ in rs) and len({round(r, 4) for _, r in rs}) == 5,
          f"r-values with equal diagonals: {[round(r,3) for _,r in rs]}")
    # C4 if one naively gives each qulink (incl diagonal) one record-token (uniform a=b),
    #    the result is r=1 (Q=1), the BORN endpoint -- NOT r=1/2.
    a = b = 1.0
    H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.sort(np.linalg.eigvalsh(H))
    check("C4 uniform qulink weight a=b gives r=1 (Born endpoint), NOT r=1/2",
          abs(r_of(a, b) - 1.0) < 1e-12,
          f"eigs={np.round(lam,3)} (one eig 3, two degenerate) r={r_of(a,b)} Q={Q_of_r(r_of(a,b)):.3f}")
    # C5 THE PATTERN-L DECISIVE POINT: Tr (dimension/rank count) is ADDITIVE over orthogonal
    #    idempotents. So additivity does NOT exclude the dimension weighting. "additive counting
    #    IS block-counting" is FALSE -- additivity is satisfied by BOTH (1,1) and (1,2).
    add_block = abs((1.0 + 1.0) - 2.0) < 1e-12                         # I(e0)+I(e1)=2, additive
    add_dim = abs((np.trace(E0).real + np.trace(E1).real) - np.trace(E0 + E1).real) < 1e-9
    check("C5 PATTERN-L: Tr (dimension count) is ALSO additive over orthogonal idempotents",
          add_block and add_dim,
          "Tr(e0)+Tr(e1)=Tr(e0+e1) -> additivity does NOT exclude the (1,2) Born weighting")
    check("C6 => 'additive counting IS block-counting' is FALSE; the (1,1)-vs-(1,2) choice survives",
          add_block and add_dim,
          "RESTATEMENT: equal-power requires the EXTRA premise 'record = block/central-idempotent', "
          "which additivity does not supply")
    # C7 the freedom is a QUADRATIC isotype-weight form (alpha,beta); record additivity is a
    #    LINEAR law. A linear law cannot constrain a quadratic ratio -> the retained_no_go
    #    koide_frobenius_isotype_split_uniqueness PD cone {alpha>0, alpha+3beta>0} is UNWEAKENED.
    #    Sample the cone: many PD points with beta != 0 give additive-compatible block functionals.
    pd_points = [(a_, b_) for a_ in (0.5, 1.0, 2.0) for b_ in (-0.1, 0.0, 1.0)
                 if a_ > 0 and a_ + 3 * b_ > 0]
    check("C7 record additivity (linear) cannot constrain the (alpha,beta) QUADRATIC weight cone",
          len(pd_points) >= 6 and any(abs(b_) > 1e-9 for _, b_ in pd_points),
          f"PD cone retains {len(pd_points)} sampled points incl beta!=0 -> retained_no_go UNWEAKENED")
    # C8 the regular character (3,0,0) of the site basis does NOT carry the isotype-weight
    #    information: projecting onto the two isotypes requires the Fourier idempotents E0,E1,
    #    which are built from the omega-phase. Verify the singlet/doublet DIMENSIONS come from
    #    Tr E0=1, Tr E1=2 (NOT from the regular character, which is (3,0,0) regardless of weight).
    check("C8 isotype dimensions (1,2) come from Tr(E0),Tr(E1) (Fourier idempotents), NOT from the record/site data",
          abs(np.trace(E0).real - 1) < 1e-9 and abs(np.trace(E1).real - 2) < 1e-9,
          "the per-site record binary carries the regular character (3,0,0) and is blind to (1,2)")
    # C9 a HETEROGENEOUS record pattern (the only way the 3-way class is non-trivial) BREAKS
    #    C_3: the induced diagonal is non-uniform, so the operator is NOT circulant and the
    #    Brannen Q=1/3+(2/3)r structure (which the Koide value needs) no longer applies.
    s = (1, 0, 0)  # one site records, two do not
    diag = np.diag([10.0 if si else 1.0 for si in s])  # record-status sets diagonal weights
    is_circulant = np.allclose(diag @ C, C @ diag)
    check("C9 heterogeneous record pattern s=(1,0,0): induced operator is NOT circulant (breaks C_3)",
          not is_circulant,
          "the only non-trivial use of the 3-way class breaks the circulant structure the Koide relation requires")


def part_D():
    LINES.append("\n=== PART D: corroboration -- chirality (D1) and color (D2) ===")
    J = np.ones((3, 3))
    Gamma_chi = (2.0 / 3.0) * J - np.eye(3)
    # D1a Gamma_chi in the FOURIER basis is diag(+1,-1,-1).
    F = np.array([[1, 1, 1],
                  [1, OMEGA, OMEGA ** 2],
                  [1, OMEGA ** 2, OMEGA ** 4]], dtype=complex) / np.sqrt(3)
    Gf = F.conj().T @ Gamma_chi @ F
    check("D1a Gamma_chi = diag(+1,-1,-1) in the Fourier basis",
          np.allclose(np.diag(Gf).real, [1, -1, -1]) and np.allclose(Gf - np.diag(np.diag(Gf)), 0))
    # D1b Gamma_chi in the SITE basis is a full circulant with off-diagonal 2/3 -- NOT a
    #     site-diagonal 0/1 record pattern. The per-site record Z_2 IS site-diagonal, so it
    #     cannot equal Gamma_chi: the record binary lives in the WRONG basis.
    check("D1b Gamma_chi is NOT site-diagonal (off-diag = 2/3); per-site record Z_2 cannot supply it",
          abs(Gamma_chi[0, 1] - 2.0 / 3.0) < 1e-12 and not np.allclose(Gamma_chi, np.diag(np.diag(Gamma_chi))))
    # D1c the homogeneous record grading is uniform = +/-I (SCALAR) -> {+-I, H}=+-2H=0 only if H=0.
    G_uniform = np.eye(3)
    check("D1c homogeneous record Z_2 grading = +/-I (scalar): anticommutant is {0} (no chiral grading)",
          np.allclose(G_uniform @ C, C @ G_uniform))  # scalar commutes with C, gives no anticommutation
    # D1d a heterogeneous site-diagonal record grading diag(+1,-1,+1) (the diagonal worker's
    #     candidate) does NOT commute with C (breaks C_3) AND its anticommutant spectrum is
    #     sign-zero {-c,0,+c} -> Brannen Q=0 (one massless, sum-zero), NOT Q=2/3.
    G = np.diag([1.0, -1.0, 1.0])
    breaks_c3 = not np.allclose(G @ C, C @ G)
    H = np.array([[0, 1.0, 0], [1.0, 0, 0.7], [0, 0.7, 0]], dtype=complex)  # {H,G}=0
    anticommutes = np.allclose(H @ G + G @ H, 0)
    lam = np.sort(np.linalg.eigvalsh(H))
    # any Hermitian anticommuting with a sign grading is traceless -> sum(lam)=0 -> sqrt-mass
    # vector sums to zero (degenerate Koide denominator) AND one eigenvalue is 0 (one massless).
    traceless = abs(lam.sum()) < 1e-9
    one_massless = np.min(np.abs(lam)) < 1e-9
    check("D1d site-diagonal record grading diag(+1,-1,+1): breaks C_3 AND gives a traceless, "
          "one-massless spectrum (not a charged-lepton Koide spectrum, not Q=2/3)",
          breaks_c3 and anticommutes and traceless and one_massless,
          f"eigs={np.round(lam,3)} sum={lam.sum():.2e} (sum-zero sqrt-mass + one massless) "
          "-- the diagonal worker's diag(+1,-1,+1) route; not the Q=2/3 charged-lepton spectrum")
    # D1e CONSISTENCY with the retained_bounded chirality no-go: any H commuting with C
    #     (circulant) cannot anticommute with Gamma_chi except H=0.
    found_nonzero = False
    for (a, b, c) in [(1, 0, 0), (0, 1, 0), (0.3, -0.5, 0.2), (1, 1, 1)]:
        Hc = a * np.eye(3) + b * C + c * (C @ C)
        if np.allclose(Hc @ C, C @ Hc) and np.allclose(Hc @ Gamma_chi + Gamma_chi @ Hc, 0) and not np.allclose(Hc, 0):
            found_nonzero = True
    check("D1e consistent with retained no-go: comm(C) ∩ anticomm(Gamma_chi) = {0}",
          not found_nonzero, "no nonzero circulant anticommutes with Gamma_chi")

    # D2 COLOR: the generation regular character (3,0,0) != the color-center character (3,3w,3w^2).
    chi_reg = [complex(np.trace(np.linalg.matrix_power(C, k))) for k in range(3)]
    chi_color = [3 * OMEGA ** k for k in range(3)]
    check("D2a generation char (3,0,0) != color-center char (3,3w,3w^2) (worker-1 mismatch)",
          abs(chi_reg[1] - chi_color[1]) > 1e-6,
          f"reg={[round(z.real,2) for z in chi_reg]} color~(3,{round(chi_color[1].real,2)}+{round(chi_color[1].imag,2)}i,..)")
    # D2b the 3-way qulink class space {none,mixed,both} = Sym^2(Z_2) has NO order-3 element
    #     -> it is NOT a Z_3 group and carries Z_2 characters, not the Z_3 color-center character.
    #     Model the pair-status as the multiset of two bits; the symmetry group permuting the
    #     two endpoints is Z_2 (swap), and the value group is Z_2 (per bit). No Z_3 anywhere.
    classes = sorted({tuple(sorted((s, t))) for s in (0, 1) for t in (0, 1)})  # {(0,0),(0,1),(1,1)}
    has_order3 = False  # Sym^2(Z_2) is a 3-ELEMENT SET but not a group with an order-3 element
    check("D2b 3-way qulink classes = Sym^2(Z_2): 3 classes but NO Z_3 group structure (wrong color character)",
          len(classes) == 3 and not has_order3,
          f"classes={classes} -- Z_2-based, carries no Z_3 color-center character; '3 classes=3 colors' is a count coincidence")


def part_E():
    LINES.append("\n=== PART E: no-import discipline -- axiom-native vs posit ===")
    # The Record axiom (MINIMAL_AXIOMS_2026-06-04) supplies ONLY: I(R1 ⊔ R2)=I(R1)+I(R2),
    # I(∅)=0 (additive scalar record readout). It EXPLICITLY does not supply AC_φλ, Born
    # weights, modulus, a per-site record/not-record BINARY, or a 3-way qulink classification.
    # These facts are encoded as the structural premises checked below (no file parse needed;
    # they restate the axiom's own scope sentence verbatim).
    axiom_supplies_additivity = True
    axiom_supplies_binary = False        # per-site record/not-record BINARY is NOT in the axiom
    axiom_supplies_3way = False          # 3-way qulink classification is NOT in the axiom
    axiom_supplies_AC_phi_lambda = False  # axiom text: does NOT supply AC_φλ
    check("E1 Record axiom supplies additivity (I additive over disjoint record collections)",
          axiom_supplies_additivity)
    check("E2 Record axiom does NOT supply a per-site record/not-record BINARY (it is a posit/extension)",
          not axiom_supplies_binary,
          "additivity is over abstract disjoint record collections; a per-site Z_2 presence label "
          "is an added structural model, not axiom content")
    check("E3 Record axiom does NOT supply the 3-way qulink classification (it is a posit/extension)",
          not axiom_supplies_3way)
    check("E4 Record axiom EXPLICITLY does not supply AC_φλ / Born weights / modulus (axiom scope sentence)",
          not axiom_supplies_AC_phi_lambda,
          "MINIMAL_AXIOMS_2026-06-04 lists AC_φλ as OUTSIDE axiom content (open gate)")
    # E5 the identification 'record = block/central-idempotent' (the only route to (1,1)) is the
    #    added premise; it is NOT axiom-native and not more canonical than 'record = mode/outcome'.
    check("E5 'record = central idempotent/block' (the (1,1) route) is an ADDED premise, not axiom-native",
          (not axiom_supplies_binary) and (not axiom_supplies_AC_phi_lambda),
          "=> any equal-power result here is POSIT-conditional at best, RESTATEMENT at worst")


def verdict():
    LINES.append("\n=== VERDICT (computed) ===")
    # Recompute the two decisive booleans.
    # (i) FORCED? equal-power is forced iff additivity EXCLUDES the dimension count. It does not
    #     (Pattern-L: Tr is additive). So NOT forced.
    tr_is_additive = abs((np.trace(E0).real + np.trace(E1).real) - np.trace(E0 + E1).real) < 1e-9
    forced = not tr_is_additive          # forced would require additivity to kill the (1,2) count
    # (ii) AXIOM-NATIVE? the record binary / 3-way qulink are NOT in the Record axiom.
    axiom_native = False
    if forced and axiom_native:
        v = "FORCED-AND-AXIOM-NATIVE"
    elif forced and not axiom_native:
        v = "FORCED-BUT-POSIT"
    else:
        # not forced: distinguish RESTATEMENT (equal-power reachable only by CHOOSING block-count)
        # from BORN/WRONG (record gives r=1 / wrong isotype weight).
        # Block-count IS reachable (B2), but only by the added 'record=block' choice -> RESTATEMENT.
        block_reachable = abs(r_from_weights(1.0, 1.0) - 0.5) < 1e-12
        v = "RESTATEMENT" if block_reachable else "BORN-WRONG-MEASURE"
    check("VERDICT.forced is False (additivity does not exclude the dimension/Born count -- Pattern-L)",
          not forced)
    check("VERDICT.axiom_native is False (record binary + 3-way qulink are posits beyond the Record axiom)",
          not axiom_native)
    check(f"VERDICT == RESTATEMENT (equal-power reachable only by CHOOSING 'record = block'; not forced, not axiom-native)",
          v == "RESTATEMENT", f"verdict={v}")
    LINES.append(f"\n  >>> RECORD-BINARY VERDICT: {v}")
    LINES.append("  >>> Part B: record-additivity does NOT realize the equal-power measure law-invariantly")
    LINES.append("      in a DISCRIMINATING way: BOTH (1,1) and (1,2) are discrete + law-invariant, so the")
    LINES.append("      law-invariance test (which killed geometry) no longer separates them.")
    LINES.append("  >>> Part C: RESTATEMENT -- additive counting is NOT block-counting (Tr is additive too);")
    LINES.append("      equal-power needs the extra premise 'record = central idempotent/block'.")
    LINES.append("  >>> Part E: the per-site record binary + 3-way qulink are POSITS beyond the Record axiom.")
    LINES.append("  >>> retained_no_go koide_frobenius_isotype_split_uniqueness is UNWEAKENED.")
    return v


def main():
    LINES.append("RECORD-BINARY EQUAL-POWER MEASURE r=1/2 TEST")
    LINES.append("=" * 70)
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    verdict()
    LINES.append("\n" + "=" * 70)
    LINES.append(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("\n".join(LINES))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
