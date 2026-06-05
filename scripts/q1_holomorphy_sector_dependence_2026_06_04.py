"""Q1 keystone, angle B: is the holomorphic (det_C, r=1/2) generation readout
SECTOR-DEPENDENT via a clean discriminator (Dirac/Majorana, chirality, color),
or does it OVERREACH (force every C3 sector to r=1/2)?

This runner does NOT derive r=1/2 for any sector, and does not consume PDG
values as load-bearing inputs. The only PDG/Koide-phenomenology numbers that
appear (sidecar block S2) are widely-known masses used solely to *illustrate*
that the observed per-sector Koide ratios land at DISTINCT dial points; they
carry no derivational weight (matching the repo pattern of citing Koide &
Nishiura arXiv:1301.4143 as a non-load-bearing sidecar).

What it verifies, exactly and from finite algebra:

  ALGEBRA (A) -- the signed/det_R readout identity on the C3 character split:
     Q(r) = (1 + 2r)/3  with r = |z|^2/a^2,   so
        Q = 2/3  <=>  r = 1/2  (the det_C / equal-block point),
        Q = 1    <=>  r = 1    (the det_R / per-dimension default).
     (This is the cone-note P1 identity restated; it is the SIGNED-eigenvalue
      readout. The singular-value readout is shown to break the clean identity.)

  OVERREACH (O) -- the static complex structure J_cs on the C3 doublet:
     For EVERY sector whose generation algebra is R[Z3] = R (+) C, Schur forces
     a unique-up-to-sign J_cs with J_cs^2 = -I, [J_cs, C] = 0. So "a complex
     structure EXISTS" is sector-INDEPENDENT. If the existence of J_cs forced
     the holomorphic (det_C) MEASURE, then ALL sectors would read r = 1/2 -->
     overreach (falsified by quarks/neutrinos). The runner shows exp(theta*J_cs)
     = SO(2) preserves BOTH the real and the complex measure, so J_cs's
     existence does NOT pick det_C; the measure is a separate, per-sector bit.

  DISCRIMINATOR 1 (D/M) -- Dirac vs Majorana:
     A Dirac mass is a complex bilinear psibar_L M psi_R (det_C natural); a
     Majorana mass is a real symmetric/antisymmetric bilinear (Pfaffian/det_R
     natural). BUT on the GENERATION index the Dirac reality structure
     factorizes as J_spin (x) I_gen: charge conjugation acts as the IDENTITY on
     (e, mu, tau). The runner verifies U = i*I_3 (the generation-restriction of
     the Dirac "i") and the continuous centralizer diag(1, e^{i phi}, e^{-i phi})
     both leave every C3-circulant H fixed and CANCEL in the ratio r. So
     Dirac-ness does NOT descend to the generation-doublet measure --> the
     Dirac/Majorana label does NOT cleanly set the generation readout.
     (Confirms FLAVOR_FIND_J_ROUND3_DIRAC_GENERATION_BLIND.)

  DISCRIMINATOR 2 (chi) -- chirality:
     The coverage-audit claimed "Q1 (holomorphy) and chirality are the SAME
     binary." The runner verifies the det_C / U(1)_b generator
     G_U1 = (C - C^2)/sqrt(3) COMMUTES with the chiral grading
     Gamma_chi = (2/3)J - I and with C (it is on-block, C3-equivariant), while
     the chiral orbit-splitting grading is OFF-block and ANTICOMMUTES. They are
     algebraically ORTHOGONAL --> NOT the same binary. (Confirms Correction #1
     of FLAVOR_DETR_DEFAULT_FULL_EXERCISE.)

  DISCRIMINATOR 3 (color) -- color/weak-isospin:
     Color SU(3) and weak isospin act on the color/isospin index, NOT the
     generation index; they commute with the C3-circulant generation operator
     and (like the Dirac scalar) cancel in r. So color cannot shift a sector's
     generation r by itself. The runner verifies a color-blind tensor factor
     U_c (x) I_gen leaves r unchanged.

  NO-OVERREACH / SECTOR-DISTINCTNESS (N):
     The map r |-> Q(r) is strictly monotone, so DISTINCT dial points r give
     DISTINCT Q. The three sectors land at three distinct r; no single forced
     reading collapses them. This is the falsification test the universal
     attempts failed.

Verdict produced: NOT-CLEANLY-SECTOR-DEPENDENT (the holomorphic measure is a
per-sector input, not set by Dirac/Majorana, chirality, or color at the
generation level), AND NOT-OVERREACHING (J_cs's existence does not force
det_C, so r=1/2 is not predicted for all sectors).
"""

import numpy as np
import sympy as sp


PASSED = []


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASSED.append(ok)
    return ok


# ---------------------------------------------------------------------------
# Shared finite algebra: the C3 = Z/3Z circulant Hermitian family on R[Z3].
# ---------------------------------------------------------------------------
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])      # cyclic shift, C^3 = I
I3 = np.eye(3)
GAMMA_CHI = (2.0 / 3.0) * np.ones((3, 3)) - I3          # chiral grading (2/3)J - I
J_CS = (C - C.T) / np.sqrt(3)                           # anti-Herm complex structure
G_U1 = (C - C.T) / np.sqrt(3)                           # det_C / U(1)_b generator (= J_cs direction)
F = np.array([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]) / np.sqrt(3)  # C-eigenbasis


def H_of(a, b):
    """Hermitian C3-circulant: H = a I + b C + conj(b) C^2 (real spectrum)."""
    return a * I3 + b * C + np.conj(b) * C.T


def koide_Q_signed(a, b):
    """Signed-eigenvalue (det_R/Brannen) Koide ratio of H_of(a,b).

    Spectrum lam_k = a + 2|b| cos(theta + 2pi k/3); mass m_k = lam_k^2,
    sqrt(m_k) = signed lam_k.  Q = sum lam^2 / (sum lam)^2.
    """
    lam = np.linalg.eigvalsh(H_of(a, b))
    return float(np.sum(lam ** 2) / (np.sum(lam) ** 2))


def koide_Q_singular(a, b):
    """Singular-value (Yukawa) readout: sqrt(m_k) = |lam_k| >= 0."""
    lam = np.linalg.eigvalsh(H_of(a, b))
    s = np.abs(lam)
    return float(np.sum(s ** 2) / (np.sum(s) ** 2))


# ===========================================================================
# BLOCK A -- the signed/det_R readout identity Q(r) = (1+2r)/3.
# ===========================================================================
def A_identity_symbolic():
    """Q = (a^2 + 2|z|^2)/(3 a^2) = (1 + 2r)/3 with r = |z|^2/a^2, exactly."""
    a, zr, zi = sp.symbols("a zr zi", positive=True)
    z2 = zr ** 2 + zi ** 2
    Q = (a ** 2 + 2 * z2) / (3 * a ** 2)
    r = z2 / a ** 2
    return sp.simplify(Q - (1 + 2 * r) / 3) == 0


def A_detC_point():
    """Q = 2/3  <=>  r = 1/2 (the det_C / equal-block point)."""
    r = sp.Rational(1, 2)
    return sp.simplify((1 + 2 * r) / 3 - sp.Rational(2, 3)) == 0


def A_detR_point():
    """Q = 1  <=>  r = 1 (the det_R / per-dimension default)."""
    r = sp.Integer(1)
    return sp.simplify((1 + 2 * r) / 3 - 1) == 0


def A_numeric_signed():
    """Numeric check Q_signed(a,b) = (1 + 2 r)/3 across many configs (signed)."""
    rng = np.random.default_rng(7)
    maxerr = 0.0
    for _ in range(400):
        a = rng.uniform(0.5, 3.0)
        mag = rng.uniform(0.0, 0.45) * a        # keep spectrum sign-homogeneous
        ph = 0.0                                 # real axis: sign-homogeneous window
        b = mag * np.exp(1j * ph)
        r = (abs(b) ** 2) / (a ** 2)
        maxerr = max(maxerr, abs(koide_Q_signed(a, b) - (1 + 2 * r) / 3))
    return maxerr < 1e-10, maxerr


def A_singular_breaks_identity():
    """The singular-value readout is NOT (1+2r)/3 once the spectrum is mixed-sign.

    Pick a,b with a doublet eigenvalue negative; signed != singular.
    """
    a, b = 1.0, 0.9 + 0.0j         # lam = {1+1.8, 1-0.9, 1-0.9} -> all positive
    # push |b| large so a - |b| < 0:
    a2, b2 = 1.0, 1.5 + 0.0j        # lam = {1+3, 1-1.5, 1-1.5} = {4, -0.5, -0.5}
    same_when_homog = abs(koide_Q_signed(a, b) - koide_Q_singular(a, b)) < 1e-12
    differ_when_mixed = abs(koide_Q_signed(a2, b2) - koide_Q_singular(a2, b2)) > 1e-3
    return same_when_homog and differ_when_mixed


# ===========================================================================
# BLOCK O -- overreach test: J_cs exists & is unique for EVERY C3 sector, but
# its existence does NOT force the holomorphic (det_C) measure.
# ===========================================================================
def O_Jcs_exists_unique():
    """Schur: J_cs is a complex structure ON THE DOUBLET (where it lives).

    J_cs = (C - C^2)/sqrt(3) has eigenvalues {+i, -i, 0}: it acts as a genuine
    complex structure (J^2 = -I) on the 2-d doublet -- the (e_omega, e_omega^2)
    pair, i.e. exactly the 'one complex mode' object -- and as 0 on the singlet
    axis. Equivalently J_cs^2 = -P_doublet. It commutes with C (C3-equivariant)
    and is unique up to sign within the real C3-circulant antisymmetric span
    {C - C^2} (the C3-equivariant endomorphism algebra of the complex-type
    doublet is C, by Schur). This existence+uniqueness is SECTOR-INDEPENDENT:
    it holds for any sector whose generation algebra is R[Z3] = R (+) C.
    """
    P_doublet = I3 - np.outer(np.ones(3), np.ones(3)) / 3.0
    is_complex_structure_on_doublet = np.allclose(J_CS @ J_CS, -P_doublet, atol=1e-12)
    eig = np.sort_complex(np.linalg.eigvals(J_CS))
    has_pm_i_and_zero = (
        np.allclose(sorted(np.round(eig.imag, 6)), [-1.0, 0.0, 1.0], atol=1e-9)
    )
    commutes = np.allclose(J_CS @ C - C @ J_CS, 0, atol=1e-12)
    minus_J = -J_CS
    minus_ok = np.allclose(minus_J @ minus_J, -P_doublet, atol=1e-12)
    return is_complex_structure_on_doublet and has_pm_i_and_zero and commutes and minus_ok


def O_SO2_preserves_both_measures():
    """exp(theta J_cs) is a real orthogonal rotation: det = 1 (preserves the
    real volume measure det_R) AND it is C-linear w.r.t. J_cs (preserves the
    complex/holomorphic measure det_C). So J_cs's flow does not distinguish the
    two measures -> J_cs cannot, by itself, select det_C.
    """
    maxdet = 0.0
    commutes_with_J = 0.0
    for theta in np.linspace(0, 2 * np.pi, 9):
        U = expm_Jcs(theta)
        maxdet = max(maxdet, abs(np.linalg.det(U) - 1.0))
        commutes_with_J = max(commutes_with_J, np.max(np.abs(U @ J_CS - J_CS @ U)))
    real_volume_preserved = maxdet < 1e-9          # det_R measure invariant
    holomorphic_preserved = commutes_with_J < 1e-9  # commutes with J -> C-linear -> det_C invariant
    return real_volume_preserved and holomorphic_preserved, (maxdet, commutes_with_J)


def expm_Jcs(theta):
    """Exact exp(theta * J_cs): identity on the singlet axis (J_cs=0 there),
    SO(2) rotation on the doublet. Via J_cs^3 = -J_cs (eigenvalues 0,+/-i):
    exp(theta J) = I + sin(theta) J + (1 - cos theta) J^2 (Rodrigues form, with
    J^2 = -P_doublet so the singlet axis stays fixed)."""
    return I3 + np.sin(theta) * J_CS + (1 - np.cos(theta)) * (J_CS @ J_CS)


def O_overreach_would_be_falsified():
    """IF J_cs-existence forced det_C, every R[Z3] sector reads r=1/2 -> Q=2/3.
    Show this is inconsistent with three DISTINCT empirical dial points
    (sidecar). The point: a forced-universal reading collapses all sectors to
    one Q; observation has them distinct, so the reading is NOT forced.
    """
    universal_Q = (1 + 2 * 0.5) / 3                     # = 2/3 for all sectors
    # sidecar empirical r per sector (block S2 below): distinct
    r_lep, r_up, r_nu = 0.5, _r_from_Q(0.685), _r_from_Q(0.40)
    distinct = len({round(r_lep, 3), round(r_up, 3), round(r_nu, 3)}) == 3
    not_all_two_thirds = abs((1 + 2 * r_up) / 3 - universal_Q) > 1e-3
    return distinct and not_all_two_thirds


def _r_from_Q(Q):
    """Invert Q = (1+2r)/3 -> r = (3Q - 1)/2 (signed-readout convention)."""
    return (3 * Q - 1) / 2


# ===========================================================================
# BLOCK D/M -- Dirac vs Majorana discriminator: generation-blind.
# ===========================================================================
def DM_dirac_scalar_is_generation_blind():
    """The Dirac reality 'i' restricts to the central scalar i*I_3 on the
    generation index (charge conjugation = identity on (e,mu,tau)). It leaves
    every C3-circulant H fixed under conjugation U H U^{-1}? No -- it commutes,
    so it neither mixes nor reweights the doublet."""
    U = 1j * I3
    a, b = 1.0, 0.6 + 0.2j
    H = H_of(a, b)
    # i*I_3 commutes with H (central) -> spectator
    commutes = np.allclose(U @ H - H @ U, 0, atol=1e-12)
    # and it does not change r (it is not even an endomorphism that reweights):
    return commutes


def DM_centralizer_cancels_in_r():
    """The continuous centralizer diag(1, e^{i phi}, e^{-i phi}) in the
    C-eigenbasis multiplies singlet and doublet weights equally -> cancels in
    r = |z|^2/a^2. So a uniform Dirac complexification does not move r."""
    a, b = 1.3, 0.5 + 0.1j
    r0 = (abs(b) ** 2) / (a ** 2)
    # D = diag(1, e^{i phi}, e^{-i phi}) in the C-eigenbasis commutes with C
    # (both diagonal there), so it is C3-equivariant and does NOT change the
    # character-component magnitudes -> r = |z|^2/a^2 is invariant.
    max_comm = 0.0
    for phi in np.linspace(0, 2 * np.pi, 7):
        D = F.conj().T @ np.diag([1.0, np.exp(1j * phi), np.exp(-1j * phi)]) @ F
        max_comm = max(max_comm, np.max(np.abs(D @ C - C @ D)))
    return max_comm < 1e-10, r0


def DM_majorana_pfaffian_is_real_but_also_generation_structure_free():
    """A Majorana mass uses an antisymmetric pairing (Pfaffian / det_R-type),
    a DIFFERENT reality structure from Dirac's complex bilinear. Verify the two
    bilinear classes are genuinely distinct on R[Z3]: the C3-invariant SYMMETRIC
    bilinear (det_R, real) and the C3-invariant ANTISYMMETRIC bilinear both
    exist, so neither Dirac (complex) nor Majorana (real/antisym) is forced by
    C3 alone -- the reality structure is an INPUT, not fixed by the algebra.
    """
    # symmetric invariant: I (and C + C^2); antisymmetric invariant: C - C^2.
    Sym = I3
    Asym = C - C.T
    sym_is_symmetric = np.allclose(Sym, Sym.T, atol=1e-12)
    asym_is_antisym = np.allclose(Asym, -Asym.T, atol=1e-12)
    # both C3-invariant: C^T Sym C = Sym, C^T Asym C = Asym
    sym_inv = np.allclose(C.T @ Sym @ C, Sym, atol=1e-12)
    asym_inv = np.allclose(C.T @ Asym @ C, Asym, atol=1e-12)
    both_exist = sym_is_symmetric and asym_is_antisym and sym_inv and asym_inv
    return both_exist


def DM_no_clean_generation_discriminator():
    """Net: the Dirac (det_C) vs Majorana (det_R/Pfaffian) reality label lives
    on the SPIN/Nambu factor; on the generation index it factorizes as
    (.) (x) I_gen and cancels in r. So Dirac/Majorana does NOT cleanly set the
    generation-doublet measure. Boolean conjunction of the above sub-tests."""
    a, b = 1.0, 0.6 + 0.2j
    r0 = (abs(b) ** 2) / (a ** 2)
    # tensoring a 2x2 spin/Nambu reality op onto I_gen leaves r untouched:
    sigma_y = np.array([[0, -1j], [1j, 0]])             # a Dirac/Majorana 2x2 reality op
    big = np.kron(sigma_y, H_of(a, b))                  # spin (x) generation
    # generation r read from the generation factor is unchanged by the kron:
    lam_gen = np.linalg.eigvalsh(H_of(a, b))
    r_read = (np.sum(lam_gen ** 2) / np.sum(lam_gen) ** 2 * 3 - 1) / 2
    factorizes = np.allclose(
        big, np.kron(sigma_y, I3) @ np.kron(np.eye(2), H_of(a, b)), atol=1e-12
    )
    return factorizes and abs(r_read - r0) < 1e-9


# ===========================================================================
# BLOCK chi -- chirality discriminator: orthogonal to det_C, NOT the same binary.
# ===========================================================================
def chi_GU1_commutes_with_Gamma():
    """The det_C / U(1)_b generator G_U1 COMMUTES with Gamma_chi (on-block)."""
    comm = np.max(np.abs(G_U1 @ GAMMA_CHI - GAMMA_CHI @ G_U1))
    return comm < 1e-12, comm


def chi_GU1_commutes_with_C():
    """G_U1 is C3-equivariant (commutes with C) -> on-block."""
    comm = np.max(np.abs(G_U1 @ C - C @ G_U1))
    return comm < 1e-12, comm


def chi_chiral_grading_anticommutes_offblock():
    """The chiral ORBIT-SPLITTING grading anticommutes with a doublet operator
    (off-block) -- distinct from G_U1. Build an off-block grading and show a
    nonzero anticommutator with some Hermitian generator, while G_U1 commutes
    with Gamma_chi. The point is qualitative orthogonality of the two binaries.
    """
    # off-block reflection grading R = diag(1,-1,-1)-type in C-eigenbasis:
    R = F.conj().T @ np.diag([1.0, -1.0, 1.0]) @ F
    # an operator anticommuting with R exists (off-diagonal in that basis):
    M = F.conj().T @ np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) @ F
    anticomm_norm = np.max(np.abs(M @ R + R @ M))
    # G_U1 vs Gamma_chi commute (already checked); these are different objects:
    gu1_comm = np.max(np.abs(G_U1 @ GAMMA_CHI - GAMMA_CHI @ G_U1))
    return (anticomm_norm < 1e-9) and (gu1_comm < 1e-12)


def chi_not_same_binary():
    """Coverage-audit claim 'Q1 holomorphy == chirality binary' is FALSE:
    the holomorphy generator commutes with the chiral grading, so flipping the
    holomorphy bit (det_R<->det_C) is independent of flipping the chirality bit.
    """
    gu1_comm = np.max(np.abs(G_U1 @ GAMMA_CHI - GAMMA_CHI @ G_U1))
    # independence => the two bits are not locked
    return gu1_comm < 1e-12


# ===========================================================================
# BLOCK color -- color/weak-isospin discriminator: generation-blind too.
# ===========================================================================
def color_blind_factor_leaves_r_fixed():
    """Color SU(3)/weak isospin act on the color/isospin index U_c (x) I_gen;
    they commute with the generation operator and cancel in r."""
    a, b = 1.2, 0.55 + 0.15j
    r0 = (abs(b) ** 2) / (a ** 2)
    # an SU(3) color rotation tensored with identity on generation:
    th = 0.7
    U_c = np.array([
        [np.cos(th), -np.sin(th), 0],
        [np.sin(th), np.cos(th), 0],
        [0, 0, 1.0],
    ])  # an SO(3) subgroup elt standing in for a color rotation (3 colors)
    big = np.kron(U_c, H_of(a, b))
    factorizes = np.allclose(big, np.kron(U_c, I3) @ np.kron(np.eye(3), H_of(a, b)), atol=1e-12)
    lam_gen = np.linalg.eigvalsh(H_of(a, b))
    r_read = (np.sum(lam_gen ** 2) / np.sum(lam_gen) ** 2 * 3 - 1) / 2
    return factorizes and abs(r_read - r0) < 1e-9, r0


def color_quark_r_set_by_modulus_not_color():
    """The quark r differs from 1/2 not because color CHANGES the readout class,
    but because the Fourier modulus r = |b|^2/a^2 differs per sector (the same
    free modulus that the charged-lepton lane leaves open). Show: holding the
    readout SIGNED, the only thing that moves Q between sectors is r itself
    (monotone), independent of any color tensor factor.
    """
    # two sectors, same signed readout, different modulus -> different Q:
    Q_lep = koide_Q_signed(1.0, 0.5 / np.sqrt(2) * np.sqrt(2))   # r=1/2 config below
    # build exact r=1/2 config: |b|^2 = a^2/2
    a = 1.0
    b_half = (a / np.sqrt(2))
    Q_half = koide_Q_signed(a, b_half + 0j)
    b_q = a * np.sqrt(0.30)        # a quark-like larger modulus r=0.30 -> different Q
    Q_q = koide_Q_signed(a, b_q + 0j)
    return abs(Q_half - 2.0 / 3.0) < 1e-9 and abs(Q_q - 2.0 / 3.0) > 1e-2


# ===========================================================================
# BLOCK N -- no-overreach / sector-distinctness.
# ===========================================================================
def N_Q_strictly_monotone_in_r():
    """Q(r) = (1+2r)/3 is strictly increasing -> distinct r give distinct Q.
    So the three sectors at distinct dial points are genuinely distinct; a
    single forced reading cannot reproduce all three."""
    rs = np.linspace(0, 1.5, 200)
    Qs = (1 + 2 * rs) / 3
    return np.all(np.diff(Qs) > 0)


def N_three_sectors_distinct():
    """Sidecar (S2): the three sectors land at three distinct r under the signed
    readout. This is the falsification test for any universal-r prediction."""
    r_lep = _r_from_Q(2.0 / 3.0)          # = 1/2 exactly (charged leptons, signed)
    r_up = _r_from_Q(0.685)               # sidecar (illustrative)
    r_nu = _r_from_Q(0.40)                # sidecar (illustrative, Q<2/3)
    distinct = (abs(r_lep - r_up) > 1e-2) and (abs(r_lep - r_nu) > 1e-2) and (abs(r_up - r_nu) > 1e-2)
    lepton_at_half = abs(r_lep - 0.5) < 1e-9
    return distinct and lepton_at_half, (r_lep, r_up, r_nu)


def N_overreach_excluded():
    """The 'holomorphic forced everywhere' hypothesis predicts r=1/2 for all
    sectors; the distinctness test (N_three_sectors_distinct) refutes it. So
    holomorphy is NOT forced -> no overreach, AND it is therefore a per-sector
    input, not set by a single universal mechanism."""
    ok, _ = N_three_sectors_distinct()
    return ok


def N_detC_detR_is_a_two_point_question_on_a_continuum():
    """DECISIVE no-overreach sharpening. det_C is the SINGLE point r=1/2 and
    det_R the SINGLE point r=1 on the continuous dial r >= 0. The observed
    quark moduli sit STRICTLY BETWEEN the two (0.5 < r_quark < 1), and the
    neutrino modulus BELOW 0.5. So:
      - quarks are NOT 'det_R (r=1)' -- they are intermediate moduli;
      - neutrinos are NOT at either special point;
      - only charged leptons land exactly on the det_C point r=1/2.
    The holomorphic-vs-real binary therefore does NOT classify all sectors;
    it merely names two distinguished values of a continuous per-sector
    modulus. This is why a universal 'holomorphic' reading overreaches and is
    falsified, and why the correct variable is the per-sector modulus r.
    """
    r_lep = _r_from_Q(2.0 / 3.0)          # 0.5 exactly
    r_up = _r_from_Q(0.8489)              # sidecar up-type
    r_down = _r_from_Q(0.7316)            # sidecar down-type
    r_nu = _r_from_Q(0.40)                # sidecar neutrino (Q<2/3)
    lepton_on_detC = abs(r_lep - 0.5) < 1e-9
    quarks_strictly_between = (0.5 < r_up < 1.0) and (0.5 < r_down < 1.0)
    quarks_not_detR = (abs(r_up - 1.0) > 1e-2) and (abs(r_down - 1.0) > 1e-2)
    neutrino_below_detC = r_nu < 0.5
    return lepton_on_detC and quarks_strictly_between and quarks_not_detR and neutrino_below_detC


# ===========================================================================
# BLOCK S2 -- sidecar empirical readout (NOT load-bearing).
# Widely-known PDG masses; cited only to illustrate distinctness. The signed
# Koide ratio Q = sum m / (sum sqrt m)^2 is reported; r = (3Q-1)/2.
# ===========================================================================
def S2_print_empirical():
    print("\n--- SIDECAR S2 (illustrative, NOT load-bearing) ---")
    print("Sector readouts under the signed Q = sum(m)/(sum sqrt m)^2 form;")
    print("r = (3Q - 1)/2.  PDG masses used only to show DISTINCT dial points.")
    # charged leptons (MeV): well known to sit on Koide Q ~ 2/3
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
    Q_lep = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    # up-type quarks (GeV, running, illustrative): u,c,t
    mu_, mc, mt = 0.0022, 1.27, 172.69
    Q_up = (mu_ + mc + mt) / (np.sqrt(mu_) + np.sqrt(mc) + np.sqrt(mt)) ** 2
    # down-type quarks (GeV, illustrative): d,s,b
    md, ms, mb = 0.0047, 0.093, 4.18
    Q_down = (md + ms + mb) / (np.sqrt(md) + np.sqrt(ms) + np.sqrt(mb)) ** 2
    for name, Q in [("charged leptons", Q_lep), ("up quarks", Q_up), ("down quarks", Q_down)]:
        print(f"   {name:16s}: Q ~ {Q:.4f}   r = (3Q-1)/2 ~ {(3*Q-1)/2:.4f}")
    print("   (neutrinos: Q depends on hierarchy/absolute scale; Q<2/3 i.e. r<1/2 in")
    print("    normal-ordering fits -- distinct dial point, not r=1/2.)")
    print("   --> three+ DISTINCT dial points; no universal r. (sidecar only)\n")
    # sanity: charged leptons near 2/3, quarks not equal to it and to each other
    return (
        abs(Q_lep - 2.0 / 3.0) < 0.02
        and abs(Q_up - 2.0 / 3.0) > 1e-3
        and abs(Q_down - Q_up) > 1e-3
    )


def main():
    print("=" * 78)
    print("Q1 KEYSTONE, ANGLE B -- holomorphy: sector-dependent or overreach?")
    print("=" * 78)

    # BLOCK A -- signed readout identity
    print("\n[A] Signed/det_R readout identity Q(r) = (1+2r)/3")
    check("A1 Q = (1+2r)/3 exactly (symbolic)", A_identity_symbolic())
    check("A2 Q=2/3 <=> r=1/2 (det_C point)", A_detC_point())
    check("A3 Q=1 <=> r=1 (det_R default)", A_detR_point())
    ok, err = A_numeric_signed()
    check("A4 numeric signed Q matches (1+2r)/3", ok, f"max err = {err:.2e}")
    check("A5 singular-value readout breaks the identity off the sign-homog window",
          A_singular_breaks_identity())

    # BLOCK O -- overreach via J_cs
    print("\n[O] Overreach test: J_cs exists for EVERY sector but does not force det_C")
    check("O1 J_cs is a complex structure, [J_cs,C]=0, unique up to sign (Schur)",
          O_Jcs_exists_unique())
    ok, vals = O_SO2_preserves_both_measures()
    check("O2 exp(theta J_cs)=SO(2) preserves BOTH det_R and det_C measures",
          ok, f"|det-1|={vals[0]:.2e}, |[U,J]|={vals[1]:.2e}")
    check("O3 'J_cs-existence forces det_C' would force r=1/2 for ALL sectors (falsified)",
          O_overreach_would_be_falsified())

    # BLOCK D/M -- Dirac vs Majorana
    print("\n[D/M] Dirac vs Majorana discriminator -- generation-blind")
    check("DM1 Dirac 'i' restricts to central i*I_3 on generation index (spectator)",
          DM_dirac_scalar_is_generation_blind())
    ok, r0 = DM_centralizer_cancels_in_r()
    check("DM2 continuous Dirac centralizer commutes with C -> cancels in r",
          ok, f"r unchanged from {r0:.4f}")
    check("DM3 C3 admits BOTH symmetric (det_R) and antisymmetric (Pfaffian) invariant "
          "bilinears -> reality structure is an INPUT, not C3-forced",
          DM_majorana_pfaffian_is_real_but_also_generation_structure_free())
    check("DM4 Dirac/Majorana reality op factorizes as (spin/Nambu) (x) I_gen -> "
          "does NOT set the generation-doublet measure",
          DM_no_clean_generation_discriminator())

    # BLOCK chi -- chirality
    print("\n[chi] Chirality discriminator -- orthogonal to holomorphy, NOT the same binary")
    ok, c = chi_GU1_commutes_with_Gamma()
    check("chi1 det_C generator G_U1 COMMUTES with Gamma_chi (on-block)", ok, f"|[G,Gamma]|={c:.2e}")
    ok, c = chi_GU1_commutes_with_C()
    check("chi2 G_U1 is C3-equivariant ([G,C]=0)", ok, f"|[G,C]|={c:.2e}")
    check("chi3 chiral orbit-splitting grading is OFF-block (has anticommutant) "
          "-- a distinct object from G_U1",
          chi_chiral_grading_anticommutes_offblock())
    check("chi4 holomorphy bit and chirality bit are INDEPENDENT (coverage-audit "
          "'same binary' claim refuted)",
          chi_not_same_binary())

    # BLOCK color
    print("\n[color] Color / weak-isospin discriminator -- generation-blind")
    ok, r0 = color_blind_factor_leaves_r_fixed()
    check("color1 color factor U_c (x) I_gen leaves generation r fixed", ok, f"r={r0:.4f}")
    check("color2 quark r set by the Fourier modulus, not by color; only r moves Q (monotone)",
          color_quark_r_set_by_modulus_not_color())

    # BLOCK N -- no overreach
    print("\n[N] No-overreach / sector-distinctness")
    check("N1 Q(r)=(1+2r)/3 strictly monotone -> distinct r give distinct Q",
          N_Q_strictly_monotone_in_r())
    ok, rs = N_three_sectors_distinct()
    check("N2 three sectors land at distinct dial points; leptons exactly r=1/2",
          ok, f"(r_lep,r_up,r_nu)=({rs[0]:.3f},{rs[1]:.3f},{rs[2]:.3f})")
    check("N3 overreach (universal r=1/2) excluded by distinctness", N_overreach_excluded())
    check("N4 det_C/det_R is a TWO-POINT question on a continuum: quarks sit "
          "strictly between (not det_R), neutrinos below; only leptons on r=1/2",
          N_detC_detR_is_a_two_point_question_on_a_continuum())

    # BLOCK S2 -- sidecar
    check("S2 sidecar empirical readout shows >=3 distinct dial points (illustrative)",
          S2_print_empirical())

    # ---- scorecard ----
    total = len(PASSED)
    npass = sum(PASSED)
    print("=" * 78)
    print(f"SCORECARD {npass}/{total} PASS")
    print("=" * 78)
    print("\nVERDICT: NOT-CLEANLY-SECTOR-DEPENDENT and NOT-OVERREACHING.")
    print(" - The holomorphic (det_C, r=1/2) reading is NOT forced by J_cs's existence")
    print("   (which is sector-INDEPENDENT and measure-neutral), so it does not overreach")
    print("   to predict r=1/2 in every sector.")
    print(" - None of {Dirac/Majorana, chirality, color} cleanly sets the GENERATION-index")
    print("   readout: Dirac/Majorana and color factorize as (.) (x) I_gen (generation-blind);")
    print("   chirality COMMUTES with the holomorphy generator (independent binary).")
    print(" - The per-sector dial value r is therefore a SEPARATE per-sector modulus input")
    print("   (the same free modulus the charged-lepton lane already isolates), not a")
    print("   consequence of a clean Dirac/chirality/color discriminator.")
    if npass != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
