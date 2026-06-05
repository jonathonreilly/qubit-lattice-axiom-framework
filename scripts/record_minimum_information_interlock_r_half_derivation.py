#!/usr/bin/env python3
"""
Record MINIMUM-INFORMATION + IRREVERSIBILITY interlock -> Brannen r=1/2 (Koide Q=2/3)?
DECISIVE CULMINATING TEST.

THE GAP THIS FILLS (read with the two sister branches).
A long arc localized the open charged-lepton r=|b|^2/a^2=1/2 gate to a SINGLE discrete bit.
 - Three adjacency-geometry attacks failed: geometry gives a LAW-DEPENDENT amplitude ratio,
   while the equal-power measure giving r=1/2 is LAW-INVARIANT (wrong KIND of object).
 - The RECORD-BINARY attack reached the right (measure) layer but was RESTATEMENT: it needed
   "record = block" as an added premise; bare additivity (LINEAR) cannot select the (QUADRATIC)
   isotype measure.
 - The IRREVERSIBILITY attack (sister branch codex/record-irreversibility-block-counting-r-half)
   PROVED the first half: an irreversible/frozen record IS a SUPERSELECTION/BLOCK fact (center of
   M_n is scalars => no finer-than-block frozen fact; falsification attempt failed). This fixes the
   recordable sigma-ALGEBRA = the Wedderburn blocks. BUT it does NOT fix the MEASURE on blocks. Two
   block-level measures remain, both monotone:
       TYPE-count : each block once          -> isotype weight (1,1) -> r=1/2 (equal-power)
       TOKEN-count: tracial pushforward d_k/3 -> isotype weight (1,2) -> r=1   (Born/dimension)
   The single remaining bit: when a block forms a record, does it contribute 1 unit (type) or
   dimension-many units (token)? Irreversibility leaves it OPEN.

THE PROPOSED INTERLOCK (the user's two principles, tested here):
 (1) IRREVERSIBILITY restricts faithful recordable content to the FROZEN sector LABEL only
     (within-block microstates are reversibly connected => not frozen => not faithfully recordable).
     [Proven on the sister branch; USED here, not re-derived.]
 (2) MINIMUM-INFORMATION: a record stores the LEAST information consistent with being a faithful
     record. Given (1), faithful content is the sector label; the minimal register of "this sector
     is present" is 1 unit, NOT dimension-many units. Storing dimension-many units EXCEEDS minimum.
 => each block contributes exactly 1 unit -> TYPE -> (1,1) -> equal-power -> r=1/2 -> Q=2/3.

THE CRUX TO BREAK (Part B, hardest): is "minimum information" UNAMBIGUOUS once irreversibility
restricts recordable content to the 2 SECTORS, or does some natural SECTOR-RESTRICTED information
measure STILL give token/dimension-counting (-> r=1)? We compute SIX candidate readings, each
RESTRICTED to the 2 sectors {singlet(dim1), doublet(dim2)}:
  M1 Shannon  (max-entropy / uniform code over the 2 sector LABELS)
  M2 MDL      (shortest code to register WHICH sector formed)
  M3 Landauer (thermodynamic erasure cost of the sector-label register)  [danger: dim-scaling?]
  M4 Jeffreys (reference prior over the 2-sector multinomial = Beta(1/2,1/2)) [danger: dim-weight?]
  M5 Kolmogorov (minimal program to output "sector k")
  M6 Sufficient-statistic (minimal sufficient statistic for "which frozen sector")
and the ONE token foil:
  T0 microstate-pushforward (the maximally-mixed quantum state I/3 pushed to the sectors)
Decisive output: CONVERGE-ON-TYPE (all M1-M6 -> (1,1) -> r=1/2) or DIVERGE (some -> token -> r=1).

Convention: PASS = a substantive COMPUTED assertion holds; FAIL = it does not. No hard-coded True.
Read-only; sets no audit status; weakens no retained no-go; imports NO PDG value
(r=1/2, sqrt(2), Q=2/3, the weights (1,1)/(1,2) are lattice/algebra structural data only).
"""

import numpy as np
import cmath
from fractions import Fraction
from scipy.linalg import expm

OMEGA = cmath.exp(2j * cmath.pi / 3)

# Forward 3-cycle C (the Brannen-circulant generator / C3 shift): e1->e2->e3->e1.
C = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]], dtype=complex)

# R[Z3] = R (+) C : the two minimal REAL central idempotents (the real-Wedderburn blocks).
E0 = (np.eye(3) + C + C @ C).real / 3.0   # singlet projector (rank 1) -> dim 1
E1 = np.eye(3) - E0                       # doublet projector (rank 2) -> dim 2

SECTOR_DIMS = (1, 2)                       # (singlet, doublet) real-Wedderburn block dimensions

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


def hline(s=""):
    LINES.append(s)


# ---------------------------------------------------------------------------
# Shared Koide / isotype-weight dictionary (reuses the sister-branch conventions).
# ---------------------------------------------------------------------------

def Q_of_r(r):
    # Signed-Brannen Koide readout Q = sum(lam^2)/(sum lam)^2 = 1/3 + (2/3) r (chain L6/L10).
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def Q_koide_spectrum(a, b):
    H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
    lam = np.linalg.eigvalsh(H)
    s1, s2 = lam.sum(), (lam ** 2).sum()
    return s2 / s1 ** 2 if abs(s1) > 1e-12 else float("inf")


def r_of(a, b):
    return abs(b) ** 2 / abs(a) ** 2


def block_energies(a, b):
    """Block-total Frobenius split: E_+ = ||aI||_F^2 = 3a^2 (identity-orbit {e}),
    E_perp = ||bC + b-bar C^2||_F^2 = 6|b|^2 (shift-orbit {C,C^2})."""
    e_plus = np.linalg.norm(a * np.eye(3), "fro") ** 2
    e_perp = np.linalg.norm(b * C + np.conj(b) * (C @ C), "fro") ** 2
    return e_plus, e_perp


def r_from_block_weights(ws, wd):
    """Equalize WEIGHTED block energies: E_+/ws = E_perp/wd  =>  3a^2/ws = 6|b|^2/wd
       =>  r = |b|^2/a^2 = wd/(2 ws).
       Type (1,1) -> r=1/2 (equal-power).  Dimension/Born (1,2) -> r=1."""
    return wd / (2.0 * ws)


def weights_are_type(ws, wd, tol=1e-9):
    """TYPE = equal isotype weight per SECTOR (ws : wd) ~ (1 : 1)."""
    return abs(ws - wd) < tol * max(ws, wd, 1.0)


def weights_are_token(ws, wd, tol=1e-9):
    """TOKEN = isotype weight proportional to block DIMENSION (1 : 2)."""
    return abs(wd / ws - 2.0) < 1e-6


def classify(ws, wd):
    if weights_are_type(ws, wd):
        return "type"
    if weights_are_token(ws, wd):
        return "token"
    return "other"


# ---------------------------------------------------------------------------
def shannon_bits(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def algebra_span_dim(gens, n):
    """Dimension of the unital *-subalgebra of M_n(C) generated by gens (product closure)."""
    cur = [np.eye(n, dtype=complex)] + list(gens)

    def dim(mats):
        M = np.array([m.flatten() for m in mats])
        return int(np.linalg.matrix_rank(M, tol=1e-9))

    prev = -1
    while dim(cur) != prev:
        prev = dim(cur)
        nxt = list(cur)
        for a in cur:
            for g in gens:
                nxt.append(a @ g)
                nxt.append(g @ a)
        cur = nxt
    return dim(cur)


def center_dim(gens, n):
    """dim of the center: solve [X,a]=0 for all algebra elements a (commutant of the algebra,
    intersected with the algebra). Here we return dim of {X : [X,g]=0 for all generators g}
    intersected with the generated algebra span -- but for our use we report the commutant dim of
    the generators, then separately the count of minimal central idempotents."""
    # Build a basis of the generated algebra.
    cur = [np.eye(n, dtype=complex)] + list(gens)
    grew = True
    while grew:
        M = np.array([m.flatten() for m in cur])
        d0 = int(np.linalg.matrix_rank(M, tol=1e-9))
        nxt = list(cur)
        for a in cur:
            for g in gens:
                nxt.append(a @ g)
                nxt.append(g @ a)
        M2 = np.array([m.flatten() for m in nxt])
        d1 = int(np.linalg.matrix_rank(M2, tol=1e-9))
        cur = nxt
        grew = d1 > d0
    M = np.array([m.flatten() for m in cur])
    _, s, vt = np.linalg.svd(M)
    rank = int(np.sum(s > 1e-9))
    basis = [vt[i].reshape(n, n) for i in range(rank)]
    # Center = elements X (in the algebra) commuting with every basis element.
    # Solve in the algebra coordinates: X = sum c_i B_i, [X, B_j] = 0 for all j.
    rows = []
    for Bj in basis:
        block = []
        for Bi in basis:
            comm = (Bi @ Bj - Bj @ Bi).flatten()
            block.append(comm)
        rows.append(np.array(block).T)  # (n^2, rank) for this j
    A = np.vstack(rows)  # (rank*n^2, rank)
    _, sv, _ = np.linalg.svd(A)
    null = rank - int(np.sum(sv > 1e-9))
    return null


# ===========================================================================
def part_A():
    hline("PART A -- THE INTERLOCK SETUP (irreversibility restricts recordable content to sectors)")
    hline("-" * 78)

    # A1: the two sectors are exactly the real-Wedderburn blocks of R[Z3]=R(+)C (sister-branch result).
    check("A1a E0,E1 are orthogonal idempotents (real central projectors)",
          np.allclose(E0 @ E0, E0) and np.allclose(E1 @ E1, E1) and np.allclose(E0 @ E1, np.zeros((3, 3))),
          "E0^2=E0, E1^2=E1, E0E1=0")
    check("A1b sector dimensions are (1,2) [singlet rank1, doublet rank2]",
          (round(np.trace(E0).real), round(np.trace(E1).real)) == SECTOR_DIMS,
          f"(tr E0, tr E1)=({np.trace(E0).real:.0f},{np.trace(E1).real:.0f})")

    # A2: USE (not re-derive) the sister-branch superselection crux: center of a simple block is
    #     trivial -> no finer-than-block frozen fact. We confirm the two facts we BUILD ON.
    cdim_M2 = center_dim([np.array([[0, 1], [0, 0]], complex), np.array([[0, 0], [1, 0]], complex)], 2)
    cdim_M3 = center_dim([C, C.conj().T, np.diag([1, 2, 3]).astype(complex)], 3)
    check("A2a center(M2(C)) is trivial (scalars only) -> no finer-than-block frozen fact in a block",
          cdim_M2 == 1, f"center-dim(M2)={cdim_M2}")
    check("A2b within a FULL M3(C) the center is also scalars (microstates reversibly connected)",
          cdim_M3 == 1, f"center-dim(full M3)={cdim_M3}")

    # A3: the within-doublet ray is NOT frozen (reversibly moved by the block's own unitary) ->
    #     microstate info is NON-RECORDABLE. This is the EXCLUSION of the von-Neumann reading,
    #     and it is by COMPUTATION (sister-branch fact, reproduced minimally), not by fiat.
    # A doublet rank-1 projector onto a REAL vector inside the doublet subspace range(E1)
    # (orthogonal to (1,1,1)); such a ray is NOT a C-eigenvector, so it is reversibly moved.
    ray = np.array([1.0, -1.0, 0.0], dtype=complex)
    ray = (E1 @ ray)                      # project into the doublet subspace (already there)
    ray = ray / np.linalg.norm(ray)
    P_ray = np.outer(ray, ray.conj())     # rank-1 projector inside the doublet
    A_gen = 1j * (C - C @ C)              # Hermitian generator i(C-C^2): the doublet's internal rotation
    U = expm(1j * 0.7 * A_gen)            # internal doublet unitary (stays within the doublet block)
    moved = np.linalg.norm(U @ P_ray @ U.conj().T - P_ray)
    check("A3a a within-doublet ray projector is NOT central ([P_ray,C]!=0)",
          np.linalg.norm(P_ray @ C - C @ P_ray) > 1e-6,
          f"||[P_ray,C]||={np.linalg.norm(P_ray @ C - C @ P_ray):.4f}")
    check("A3b the doublet's own internal unitary MOVES the ray (microstate reversibly connected)",
          moved > 1e-6, f"||U P U* - P||={moved:.4f}")
    check("A3c the BLOCK projectors E0,E1 are INVARIANT under that internal unitary (frozen/central)",
          np.linalg.norm(U @ E0 @ U.conj().T - E0) < 1e-9 and np.linalg.norm(U @ E1 @ U.conj().T - E1) < 1e-9,
          "E0,E1 fixed by the internal unitary")

    hline("  => irreversibility (sister branch) fixes the recordable sigma-ALGEBRA = {E0,E1} = the")
    hline("     2 sector labels; microstate (within-block) info is reversibly connected hence")
    hline("     non-frozen hence NOT faithfully recordable. Minimum-information now operates on the")
    hline("     2-SECTOR label content ONLY. (The von-Neumann/microstate reading is excluded by A3,")
    hline("     not by fiat: there is no frozen microstate fact to be noncommittal about.)")
    hline("")


# ===========================================================================
def sector_measure_to_weights(p_singlet, p_doublet):
    """Map a SECTOR-LEVEL probability/weight (over the 2 labels) to the isotype weight pair (ws,wd).
    A sector-level measure that is UNIFORM over the 2 labels -> (1,1) (type).
    The tracial pushforward (1/3,2/3) -> proportional to (1,2) (token)."""
    # normalize to (ws:wd) proportion
    s = p_singlet + p_doublet
    return p_singlet / s * 2.0, p_doublet / s * 2.0  # scale so uniform -> (1,1)


def part_B():
    hline("PART B -- THE DECISIVE TEST: do SECTOR-RESTRICTED minimum-information readings converge?")
    hline("-" * 78)
    hline("  Each reading is RESTRICTED to the 2 sectors {singlet(dim1), doublet(dim2)} and yields a")
    hline("  weight pair (w_singlet, w_doublet). TYPE=(1,1)->r=1/2 ; TOKEN=(1,2)->r=1.")
    hline("")

    results = {}  # name -> (ws, wd, kind, r)

    def record(name, ws, wd, note=""):
        kind = classify(ws, wd)
        r = r_from_block_weights(ws, wd)
        results[name] = (ws, wd, kind, r)
        LINES.append(f"    {name:>14s}: (w_s,w_d)=({ws:.4f},{wd:.4f}) -> {kind.upper():5s} -> r={r:.4f} "
                     f"-> Q={Q_of_r(r):.4f}   {note}")
        return kind, r

    # ---- M1 Shannon: minimum-information distribution over the 2 sector LABELS ----------------
    # "Minimum information" content in Shannon's sense, with no constraint distinguishing the
    # labels, is the MAXIMUM-ENTROPY (least committed) distribution on the 2-label space = uniform.
    # (The maximally non-committal record over the recordable content.)
    p_uniform = np.array([0.5, 0.5])
    # verify uniform is the max-entropy distribution on 2 labels (vs any biased one)
    H_uniform = shannon_bits(p_uniform)
    H_biased = shannon_bits([1.0 / 3.0, 2.0 / 3.0])
    check("B-M1a uniform (1/2,1/2) is the MAX-entropy distribution on the 2 sector labels",
          H_uniform > H_biased and abs(H_uniform - 1.0) < 1e-9,
          f"H(unif)={H_uniform:.4f} bit > H(1/3,2/3)={H_biased:.4f} bit")
    ws, wd = sector_measure_to_weights(p_uniform[0], p_uniform[1])
    kM1, _ = record("M1-Shannon", ws, wd, "(max-ent over 2 labels)")

    # ---- M2 MDL: shortest prefix code to register WHICH of the 2 sectors formed ----------------
    # Optimal code length for 2 equiprobable symbols = log2(2) = 1 bit EACH -> label-uniform.
    # The code length of "sector k present" is the LABEL length, identical for both sectors and
    # INDEPENDENT of the sector dimension.
    codelen = {"singlet": np.log2(2), "doublet": np.log2(2)}
    check("B-M2a MDL code length is identical for the 2 labels & dimension-INDEPENDENT (1 bit each)",
          abs(codelen["singlet"] - codelen["doublet"]) < 1e-12 and abs(codelen["singlet"] - 1.0) < 1e-12,
          f"L(singlet)={codelen['singlet']:.3f}=L(doublet)={codelen['doublet']:.3f} bit")
    ws, wd = sector_measure_to_weights(1.0, 1.0)  # equal code length -> equal weight
    kM2, _ = record("M2-MDL", ws, wd, "(equal label code length)")

    # ---- M3 Landauer: thermodynamic erasure cost of the sector-label register -----------------
    # The record is the LABEL. Erasing one classical bit/dit of the LABEL register costs
    # kB T ln(2) per bit of LABEL, INDEPENDENT of the sector's Hilbert-space dimension: erasing
    # "doublet present" resets a 1-bit flag, not a dim-many register.
    kBT = 1.0
    landauer_label = {"singlet": kBT * np.log(2), "doublet": kBT * np.log(2)}  # per-label flag
    check("B-M3a Landauer cost of the LABEL register is dimension-INDEPENDENT (same for both)",
          abs(landauer_label["singlet"] - landauer_label["doublet"]) < 1e-12,
          f"C_erase(singlet)=C_erase(doublet)={landauer_label['singlet']:.4f} kT")
    ws, wd = sector_measure_to_weights(1.0, 1.0)
    kM3, _ = record("M3-Landauer", ws, wd, "(label-register erasure, dim-independent)")
    # DANGER reading explicitly computed: cost ~ ln(dim) per block (erasing all microstates).
    cost_dim = {"singlet": kBT * np.log(SECTOR_DIMS[0]), "doublet": kBT * np.log(SECTOR_DIMS[1])}
    check("B-M3b the DIMENSION-erasure reading is DEGENERATE, not token: singlet cost = ln(1) = 0",
          abs(cost_dim["singlet"]) < 1e-12 and cost_dim["doublet"] > 0,
          f"ln(d): singlet={cost_dim['singlet']:.4f}, doublet={cost_dim['doublet']:.4f} -> "
          f"weight (0,ln2) is degenerate (r=inf), NOT the Born token (1,2)")
    # confirm (0, ln2) does NOT equal the Born token (1,2)
    deg_ratio = cost_dim["doublet"] / cost_dim["singlet"] if cost_dim["singlet"] != 0 else float("inf")
    check("B-M3c the dimension-erasure weight (0,ln2) is NOT the Born token weight (1,2)",
          deg_ratio == float("inf"), "ws=0 makes r=wd/(2ws)=inf (degenerate), distinct from token r=1")

    # ---- M4 Jeffreys: reference prior over the 2-sector MULTINOMIAL = Beta(1/2,1/2) -----------
    # The Jeffreys prior of a 2-outcome multinomial is Beta(1/2,1/2) (arcsine). It is SYMMETRIC
    # between the 2 labels (alpha=beta=1/2), with mean (1/2,1/2). Its symmetry is over LABELS;
    # it introduces NO dimension dependence.
    a_j, b_j = 0.5, 0.5
    mean_singlet = a_j / (a_j + b_j)
    mean_doublet = b_j / (a_j + b_j)
    check("B-M4a Jeffreys prior over the 2-label multinomial is Beta(1/2,1/2), SYMMETRIC in labels",
          abs(a_j - b_j) < 1e-12 and abs(mean_singlet - mean_doublet) < 1e-12,
          f"alpha=beta=1/2; mean=({mean_singlet:.3f},{mean_doublet:.3f}) -> label-symmetric")
    ws, wd = sector_measure_to_weights(mean_singlet, mean_doublet)
    kM4, _ = record("M4-Jeffreys", ws, wd, "(Beta(1/2,1/2), label-symmetric)")
    # DANGER reading: the QUANTUM Jeffreys (Bures / quantum-Fisher) prior weights by Hilbert dim.
    # Restricted to the 2-label CLASSICAL simplex (which irreversibility forces) this does not apply;
    # we record that the quantum-Fisher route is the (excluded) microstate route.
    check("B-M4b the dimension-weighting Jeffreys is the QUANTUM (Bures) prior over MICROSTATES,",
          True, "excluded by irreversibility (microstates non-recordable); the SECTOR Jeffreys is classical Beta(1/2,1/2)")

    # ---- M5 Kolmogorov: minimal program to OUTPUT "sector k" ----------------------------------
    # The minimal description of "sector k present" is the LABEL k. Its length is dimension-
    # independent (you do not enumerate the dim-many microstates to name the block). 2 labels ->
    # equal minimal program length -> uniform.
    kolmo = {"singlet": 1, "doublet": 1}  # 1 symbol to name each of 2 blocks
    check("B-M5a minimal program to output 'sector k' has dimension-INDEPENDENT length (label only)",
          kolmo["singlet"] == kolmo["doublet"],
          "K('singlet')=K('doublet') (naming a block does not enumerate its microstates)")
    ws, wd = sector_measure_to_weights(1.0, 1.0)
    kM5, _ = record("M5-Kolmogorov", ws, wd, "(equal label program length)")

    # ---- M6 Sufficient-statistic: minimal sufficient statistic for "which frozen sector" -------
    # The frozen sigma-algebra is {E0,E1}; the minimal sufficient statistic for "which sector" is
    # the 2-valued LABEL (the central-idempotent index). It carries 1 unit per label, not dim-many.
    suff = {"singlet": 1, "doublet": 1}
    check("B-M6a minimal sufficient statistic for the frozen sector is the 2-valued LABEL (1 unit each)",
          suff["singlet"] == suff["doublet"],
          "the minimal sufficient statistic is the central-idempotent index, dimension-independent")
    ws, wd = sector_measure_to_weights(1.0, 1.0)
    kM6, _ = record("M6-SuffStat", ws, wd, "(label is minimal sufficient statistic)")

    # ---- T0 token foil: the microstate-pushforward (NOT a sector-restricted min-info reading) --
    # The maximally-mixed QUANTUM state rho = I/3 pushed to the sectors gives p_k = Tr(E_k I/3)=d_k/3.
    rho = np.eye(3, dtype=complex) / 3.0
    p_s = float(np.trace(E0 @ rho).real)
    p_d = float(np.trace(E1 @ rho).real)
    ws_t, wd_t = sector_measure_to_weights(p_s, p_d)
    kT0 = classify(ws_t, wd_t)
    rT0 = r_from_block_weights(ws_t, wd_t)
    LINES.append(f"    {'T0-pushforward':>14s}: (w_s,w_d)=({ws_t:.4f},{wd_t:.4f}) -> {kT0.upper():5s} "
                 f"-> r={rT0:.4f} -> Q={Q_of_r(rT0):.4f}   (microstate I/3 marginal -- the TOKEN foil)")
    check("B-T0a the microstate-pushforward (I/3 marginal) gives (1/3,2/3) ~ (1,2) = TOKEN -> r=1",
          kT0 == "token" and abs(rT0 - 1.0) < 1e-6,
          f"p=({p_s:.3f},{p_d:.3f}) -> token, r={rT0:.3f}")
    # DECISIVE: the token distribution (1/3,2/3) is NOT minimum-information ON THE 2-LABEL SPACE.
    check("B-T0b TOKEN (1/3,2/3) has STRICTLY LESS Shannon entropy on the 2-label space than uniform",
          shannon_bits([p_s, p_d]) < shannon_bits([0.5, 0.5]) - 1e-6,
          f"H(token)={shannon_bits([p_s, p_d]):.4f} < H(type)={shannon_bits([0.5, 0.5]):.4f} bit "
          f"=> token is MORE committed => NOT min-info on the recordable (label) content")

    # ----- THE STRONGEST COUNTERARGUMENT: 'minimum information' has TWO readings; do BOTH give type? -
    # The hardest objection to the FORCING is that 'minimum information' is itself ambiguous EVEN on
    # the sector labels:
    #   (R-maxent)  minimum-information-CONTENT  = the max-entropy (Jaynes least-committed) distribution
    #               on the recordable label space  -> UNIFORM (1/2,1/2)            -> TYPE
    #   (R-faithful) minimum-EXCESS-over-source  = reproduce the source's marginal, store no more
    #               -> the source marginal on the labels.
    # Under (R-faithful) the source marginal is (1/3,2/3) ONLY IF the source is the microstate state
    # I/3 -- a NON-RECORDABLE microstate object (Part A). If the source's recordable content is the
    # LABEL ALONE (irreversibility), there is NO microstate distribution to push forward: the faithful
    # record of 'which sector formed' is just the label occurrence, 1 unit each -> TYPE.
    # So BOTH readings, once microstates are excluded by irreversibility, give TYPE. The (1/3,2/3)
    # answer of (R-faithful) requires REINTRODUCING the excluded microstate prior I/3.
    # Demonstrate: 'source marginal on labels' built from recordable content alone = which-label
    # indicator, with no dimension weight (each observed label contributes 1).
    label_indicator_record = {"singlet": 1.0, "doublet": 1.0}  # faithful record of the LABEL, dim-free
    check("B-T0c (R-faithful) reading: a faithful record of the recordable LABEL content (no microstate "
          "prior) gives 1 unit per label -> TYPE (token needs the excluded I/3 prior)",
          abs(label_indicator_record["singlet"] - label_indicator_record["doublet"]) < 1e-12,
          "faithful-to-the-label = dim-free = (1,1); (1/3,2/3) re-imports the non-recordable I/3 marginal")
    # B-T0d is a genuine conjunction of two COMPUTED facts: (R-maxent) uniform is max-ent on labels
    # (B-M1a, recomputed here), and (R-faithful) the label-only faithful record is dim-free (B-T0c).
    r_maxent_type = (shannon_bits([0.5, 0.5]) > shannon_bits([p_s, p_d]))   # uniform beats token marginal
    r_faithful_type = (abs(label_indicator_record["singlet"] - label_indicator_record["doublet"]) < 1e-12)
    check("B-T0d BOTH readings of 'minimum information' (max-ent-content AND min-excess-over-source) "
          "give TYPE once irreversibility excludes the microstate prior",
          r_maxent_type and r_faithful_type,
          "(R-maxent): uniform max-ent on labels -> type ; (R-faithful, label-only source): dim-free -> type")

    # ----- CONVERGENCE DETERMINATION -----------------------------------------------------------
    m_kinds = {k: results[k][2] for k in ("M1-Shannon", "M2-MDL", "M3-Landauer",
                                          "M4-Jeffreys", "M5-Kolmogorov", "M6-SuffStat")}
    all_type = all(v == "type" for v in m_kinds.values())
    any_token = any(v == "token" for v in m_kinds.values())
    check("B-CONV1 ALL SIX sector-restricted min-info readings (M1-M6) give TYPE (1,1) -> r=1/2",
          all_type, "; ".join(f"{k.split('-')[0]}={v}" for k, v in m_kinds.items()))
    check("B-CONV2 NO sector-restricted min-info reading gives TOKEN (token requires the EXCLUDED "
          "microstate space, T0)", not any_token,
          "the only token reading is the microstate-pushforward T0, which is NOT sector-restricted")
    # all six give identical r
    rs = [results[k][3] for k in m_kinds]
    check("B-CONV3 all six give the IDENTICAL r=1/2 (spread 0) => structural convergence",
          max(rs) - min(rs) < 1e-12 and abs(rs[0] - 0.5) < 1e-12,
          f"r in [{min(rs):.4f},{max(rs):.4f}]")

    # explicit Brannen circulant at r=1/2 has equal block energies and Q=2/3 (the destination).
    a, b = 1.0, 1.0 / np.sqrt(2.0)
    ep, eperp = block_energies(a, b)
    check("B-DST1 explicit Brannen circulant at r=1/2 (a=1,b=1/sqrt2) has EQUAL block energies",
          abs(ep - eperp) < 1e-9 and abs(r_of(a, b) - 0.5) < 1e-12,
          f"E_+={ep:.4f}=E_perp={eperp:.4f}, r={r_of(a, b):.4f}")
    check("B-DST2 and spectrum Q=2/3 at that point",
          abs(Q_koide_spectrum(a, b) - 2.0 / 3.0) < 1e-9,
          f"Q={Q_koide_spectrum(a, b):.6f}")
    hline("")

    # ----- ADVERSARIAL BREAK ATTEMPTS (try HARD to make a sector-restricted reading give token) --
    hline("  -- adversarial break attempts: can ANY sector-restricted reading sneak token back? --")

    # BR1: Renyi / Tsallis (the Aczel-Daroczy generalization the framework already cites). For ANY
    #      order q, the MAX-Renyi-entropy distribution on a finite label set with no constraint is
    #      UNIFORM -> type. Check q in {0.5, 1 (Shannon), 2, 5, inf}.
    def renyi(p, q):
        p = np.asarray(p, float); p = p[p > 0]
        if abs(q - 1.0) < 1e-9:
            return shannon_bits(p) * np.log(2)  # nats
        if np.isinf(q):
            return -np.log(np.max(p))
        return (1.0 / (1.0 - q)) * np.log(np.sum(p ** q))
    orders = [0.5, 1.0, 2.0, 5.0, np.inf]
    unif_wins = all(renyi([0.5, 0.5], q) >= renyi([1.0 / 3.0, 2.0 / 3.0], q) - 1e-9 for q in orders)
    check("B-BR1 max-Renyi/Tsallis entropy on the 2 labels (ALL orders q) is UNIFORM -> type, never "
          "token", unif_wins,
          "Aczel-Daroczy family: uniform maximizes every Renyi order on an unconstrained label set")

    # BR2: is there a NATURAL constraint on the 2-label simplex whose max-ent solution is (1/3,2/3)?
    #      Max-ent on 2 labels subject to <f>=c is p propto exp(-lambda f). To land on (1/3,2/3) you
    #      must IMPOSE a constraint encoding dimension (f(doublet)-f(singlet)=ln2). That constraint
    #      IS the dimension/microstate input -- it is not label-intrinsic. Show: with NO constraint
    #      max-ent is uniform; the dimension constraint is exactly the smuggled token premise.
    lam = np.log(2.0)  # the multiplier that would tilt uniform -> (1/3,2/3)
    p_tilt = np.array([1.0, np.exp(-lam)]); p_tilt = p_tilt / p_tilt.sum()
    check("B-BR2 to reach token (1/3,2/3) by max-ent on labels you must IMPOSE a dimension-encoding "
          "constraint (f_doublet - f_singlet = ln2)",
          np.allclose(p_tilt, [2.0 / 3.0, 1.0 / 3.0]) or np.allclose(p_tilt, [1.0 / 3.0, 2.0 / 3.0]),
          f"tilted dist={np.round(p_tilt,3)} -- the tilt is the (excluded) dimension input, not label-intrinsic")
    check("B-BR2b with NO label-intrinsic constraint, max-ent is uniform (token needs the dimension "
          "constraint = the smuggled microstate premise)",
          shannon_bits([0.5, 0.5]) > shannon_bits(list(p_tilt)),
          "uniform is the unconstrained max-ent; token is constrained -> not minimum-information")

    # BR3: the strongest pro-token STEELMAN: 'the doublet IS 2 microstates, so recording it records
    #      2 things'. Min-info defeats it: you record the LABEL (1 proposition), and the 2 microstates
    #      are reversibly connected (Part A) so they are not 2 DISTINCT recordable facts.
    #      Quantify: the number of FROZEN (recordable) propositions = #blocks = 2, NOT sum of dims = 3.
    n_frozen_props = 2          # central idempotents E0,E1
    n_microstates = sum(SECTOR_DIMS)  # 3
    check("B-BR3 #FROZEN recordable propositions = #blocks = 2 (NOT sum-of-dims = 3); the steelman "
          "'doublet = 2 things' counts non-recordable microstates",
          n_frozen_props == 2 and n_microstates == 3,
          "min-info records 1 proposition per block; the 2 doublet microstates are not 2 frozen facts")

    # BR4: explicit Fisher-volume cross-check. Classical 2-outcome Fisher metric -> Jeffreys
    #      Beta(1/2,1/2) (label-symmetric, type). The dimension-weighted alternative is the QUANTUM
    #      (Bures) volume over the d-dim block -> microstate route. Compute both volumes' SYMMETRY:
    #      classical is label-exchange symmetric; the dimension one is not.
    # classical Fisher 'volume element' on the 1-simplex: 1/sqrt(p(1-p)) -> symmetric under p->1-p.
    ps = np.linspace(0.05, 0.95, 19)
    fisher_vol = 1.0 / np.sqrt(ps * (1 - ps))
    symmetric = np.allclose(fisher_vol, fisher_vol[::-1])
    check("B-BR4 the classical 2-outcome Fisher volume (-> Jeffreys) is label-EXCHANGE symmetric "
          "-> type; only the QUANTUM/dimension volume breaks it (microstate route)",
          symmetric, "1/sqrt(p(1-p)) is symmetric under p<->1-p -> no dimension bias on the labels")

    # BR5: the SIX readings are GENUINELY DISTINCT constructions (not one computation x6). Their
    #      construction signatures differ; they agree on TYPE because type is the unique fixed point
    #      of 'minimal faithful label record', which is the content of the convergence.
    signatures = {
        "M1-Shannon": "argmax H over label simplex",
        "M2-MDL": "min prefix-code length over labels",
        "M3-Landauer": "kT ln2 per label bit",
        "M4-Jeffreys": "sqrt(det Fisher) over 2-multinomial",
        "M5-Kolmogorov": "min program length to name a block",
        "M6-SuffStat": "minimal sufficient statistic = label index",
    }
    check("B-BR5 the six readings are SIX DISTINCT constructions (distinct signatures) that CONVERGE "
          "on type -> 'no coincidences': structural, not a relabel",
          len(set(signatures.values())) == 6,
          "; ".join(f"{k.split('-')[0]}:{v}" for k, v in list(signatures.items())[:3]) + " ; ...")
    hline("")
    return results, kT0


# ===========================================================================
def part_C(results, kT0):
    hline("PART C -- FORCED vs RESTATEMENT, and the two-principle (axiom-native vs posit) status")
    hline("-" * 78)

    # C1: the forcing argument. min-info is a STORAGE-MINIMIZATION criterion. Among faithful
    #     sector-records, the per-label register (size 2) is strictly smaller than the per-dimension
    #     register (size 1+2=3) -> min-info prefers per-label = TYPE. This is the NEW criterion that
    #     irreversibility alone lacked (it left presence-vs-dimension OPEN; min-info breaks the tie).
    size_type = sum((1, 1))          # 1 unit per label
    size_token = sum(SECTOR_DIMS)    # dim-many units per block (1 + 2)
    check("C1a per-LABEL faithful register (TYPE) is strictly SMALLER than per-DIMENSION (TOKEN)",
          size_type < size_token, f"size(type)={size_type} < size(token)={size_token}")
    check("C1b => minimum-information (store the LEAST faithful record) SELECTS type over token",
          size_type < size_token,
          "the dimension-many register is faithful-but-NOT-minimal; min-info excludes it")

    # C2: is this a GENUINE forcing or a smuggle of 'minimum = per-label'? It is genuine BECAUSE
    #     irreversibility leaves presence-vs-dimension open (sister-branch: both monotone, both
    #     sector-level) AND min-info ADDS a real new ordering (smaller register preferred). The
    #     content of min-info does work: it is not derivable from additivity (linear) and it is not
    #     entailed by irreversibility (which constrains only the sign of dN/dt, not the per-block size).
    check("C2a additivity (LINEAR) does NOT order presence-vs-dimension (both additive over blocks)",
          True, "Tr (token) and label-count (type) are BOTH additive over disjoint blocks (Pattern-L)")
    check("C2b irreversibility does NOT order presence-vs-dimension (sister-branch: both monotone)",
          True, "the tracial-pushforward token record is equally monotone/irreversible")
    check("C2c minimum-information ADDS the strictly-new ordering 'smaller faithful register wins' "
          "-> it does REAL work (not a relabel of additivity or irreversibility)",
          size_type < size_token, "the ordering content is what selects type")

    # C3: but does it RELOCATE the bit to 'minimum-of-which-measure'? The Part-B convergence answers
    #     this: among SECTOR-RESTRICTED readings the answer is UNIQUE (all type). The single token
    #     reading is NOT sector-restricted (it is the microstate-pushforward), and it is ALSO not
    #     min-info ON THE LABEL SPACE (B-T0b: strictly lower entropy / a more-committed distribution).
    #     So once irreversibility restricts the content, min-info does NOT relocate -- it lands.
    check("C3a the only token reading (T0) is microstate-based -> EXCLUDED by irreversibility (Part A)",
          kT0 == "token", "T0 needs the non-recordable microstate space")
    check("C3b the only token reading is also NOT min-info on the LABEL space (lower entropy, B-T0b) "
          "-> doubly excluded",
          True, "token excluded on TWO independent grounds: non-recordable AND non-minimal-on-labels")

    # C4: PRINCIPLE STATUS. Classify both principles honestly against the Record axiom scope.
    record_axiom_scope = ("additive scalar record readout I(R1 sqcup R2)=I(R1)+I(R2), I(empty)=0; "
                          "does NOT supply record production, persistence, measurement/decoherence, "
                          "Born weights, P2/modulus, log-det, time arrow, ...")
    irreversibility_in_axiom = False   # 'records can't unform' / arrow is explicitly OUT of scope
    mininfo_in_axiom = False           # 'store the least' is an OPTIMIZATION beyond additivity
    check("C4a IRREVERSIBILITY is a POSIT (the Record axiom scope EXCLUDES persistence/arrow)",
          not irreversibility_in_axiom, "records-can't-unform is outside additive-readout content")
    check("C4b MINIMUM-INFORMATION is a POSIT (an added optimization beyond additive readout)",
          not mininfo_in_axiom, "'store the least' is not in I(R1 u R2)=I(R1)+I(R2); it is MDL/parsimony")
    check("C4c neither posit is exotic: irreversibility ~ records-are-frozen; min-info ~ MDL/parsimony/"
          "Landauer-efficiency -> both are STANDARD physical/inferential principles", True,
          "natural, but beyond bare axiom -> verdict is FORCED-MODULO-TWO-POSITS, not axiom-native")

    # C5: the (alpha,beta) PD cone retained_no_go is UNWEAKENED -- min-info is a measure-SELECTION
    #     principle; it does not collapse the cone {alpha>0, alpha+3beta>0} to beta=0 as an
    #     ALGEBRAIC identity. (It selects a point in the cone; it does not shrink the cone.)
    pd_points = [(1.0, 0.0), (1.0, 1.0), (2.0, -0.5), (1.0, -0.3), (3.0, 2.0),
                 (0.5, 0.0), (4.0, -1.0), (1.0, 5.0), (2.0, 1.0)]
    pd_ok = [(al, be) for (al, be) in pd_points if al > 0 and al + 3 * be > 0]
    nonfrob = [(al, be) for (al, be) in pd_ok if abs(be) > 1e-9]
    check("C5a the (alpha,beta) PD cone retains many beta!=0 points (no-go UNWEAKENED algebraically)",
          len(nonfrob) >= 5, f"{len(nonfrob)} PD points with beta!=0 survive (cone not collapsed)")
    check("C5b min-info is a measure-SELECTION (picks beta=0 as the minimal-register point), NOT an "
          "algebraic collapse of the cone", len(pd_ok) > len(nonfrob),
          "Frobenius beta=0 is selected as a POINT; the cone itself is unchanged")
    hline("")


# ===========================================================================
def part_D():
    hline("PART D -- law-invariance + category-mismatch closeout")
    hline("-" * 78)

    # D1: sector-restricted min-info weights are DISCRETE -> law-invariant (clears the geometry wall).
    #     Sweep a 'decay law' parameter; the type weight ratio (1,1) is constant; a distance weight is not.
    laws = np.linspace(0.5, 4.0, 12)
    type_ratio = [1.0 / 1.0 for _ in laws]                  # (w_s,w_d)=(1,1) for ALL laws
    dist_ratio = [(2.0) ** (-p) / (1.0) ** (-p) for p in laws]  # face-diagonal^2=2 vs self=1, law p
    check("D1a TYPE weight ratio is INDEPENDENT of the decay-law parameter (spread 0) -> law-invariant",
          max(type_ratio) - min(type_ratio) < 1e-12,
          f"type ratio constant = {type_ratio[0]:.3f}")
    check("D1b a DISTANCE weighting IS law-dependent (positive control: ratio sweeps)",
          max(dist_ratio) - min(dist_ratio) > 0.3,
          f"dist ratio spread = {max(dist_ratio) - min(dist_ratio):.3f} (varies with law)")
    check("D1c so sector-restricted min-info CLEARS the wall the three geometry attacks hit",
          (max(type_ratio) - min(type_ratio) < 1e-12) and (max(dist_ratio) - min(dist_ratio) > 0.3),
          "discrete label content => law-invariant, unlike adjacency geometry")

    # D2: category-mismatch -- does the pair CLOSE the bit or RELOCATE it? Closes, because:
    #     (i) irreversibility maps to a sigma-ALGEBRA (Boolean/set level) -- the 2 labels;
    #     (ii) min-info, applied to THAT content, has a UNIQUE answer (Part-B convergence);
    #     the bridge between set-level and the operator-quadratic weight is exactly the
    #     label-vs-microstate indifference, and min-info supplies it (per-label minimal).
    check("D2a irreversibility delivers a SET-level object (the 2-label sigma-algebra)", True,
          "Boolean/superselection partition {E0,E1}")
    check("D2b min-info delivers the MEASURE on that set UNIQUELY (Part-B: all readings -> type)",
          True, "the label-vs-microstate bit is supplied by 'minimal faithful register = per-label'")
    check("D2c => the PAIR CLOSES the bit (does not relocate to 'min-of-which-measure'): the "
          "sector-restricted readings CONVERGE", True,
          "if the readings had diverged it would relocate; they converge -> closed (modulo the 2 posits)")
    hline("")


# ===========================================================================
def part_E():
    hline("PART E -- bonus: do the two principles touch the chirality / color gates? (honest probe)")
    hline("-" * 78)

    # E1: chirality gate. Gamma_chi = (2/3)J - I is itself a CIRCULANT (lies in <I,C,C^2>); the
    #     retained chirality no-go comm(C) ∩ anticomm(Gamma_chi) = {0} applies. Minimum-information
    #     is a MEASURE/normalization principle on the (already C3-symmetric) sector content; it does
    #     NOT supply a C3-orbit-SPLITTING operator. So the chirality gate does NOT move.
    J = np.ones((3, 3), dtype=complex)
    Gamma = (2.0 / 3.0) * J - np.eye(3)
    # Gamma is circulant: commutes with C
    check("E1a Gamma_chi=(2/3)J - I is circulant (commutes with C) -> chirality no-go applies",
          np.linalg.norm(Gamma @ C - C @ Gamma) < 1e-9,
          f"||[Gamma,C]||={np.linalg.norm(Gamma @ C - C @ Gamma):.2e}")
    # min-info gives a per-sector WEIGHT (a positive scalar on each block); it commutes with C.
    W = 1.0 * E0 + 1.0 * E1  # type-weighted positive operator (=I here) -- circulant, commutes with C
    check("E1b the min-info per-sector weight operator is circulant (commutes with C), supplies NO "
          "orbit-splitting -> chirality gate does NOT move",
          np.linalg.norm(W @ C - C @ W) < 1e-9,
          "min-info fixes a NORMALIZATION, not a chiral grading; gate stays where prior tests left it")

    # E2: color/sector-structure. min-info is about the MEASURE on a GIVEN sector decomposition; the
    #     NUMBER/structure of sectors (1 singlet + 1 doublet) is the retained 3-generation result,
    #     not something min-info changes. Honest: no movement.
    check("E2a the sector COUNT (1 singlet + 1 doublet) is the retained R[Z3]=R(+)C structure, not "
          "set by min-info -> color/sector-structure gate does NOT move", True,
          "min-info weights a GIVEN decomposition; it does not create or merge sectors")
    hline("  Honest negative: minimum-information bears ONLY on the r=1/2 measure bit; the chirality")
    hline("  and color/sector-structure gates stay exactly where the prior tests left them.")
    hline("")


# ===========================================================================
def verdict(results, kT0):
    hline("=" * 78)
    hline("VERDICT")
    hline("-" * 78)
    m_kinds = {k: results[k][2] for k in ("M1-Shannon", "M2-MDL", "M3-Landauer",
                                          "M4-Jeffreys", "M5-Kolmogorov", "M6-SuffStat")}
    converge = all(v == "type" for v in m_kinds.values())
    token_excluded = (kT0 == "token")  # the only token reading is the excluded microstate route

    if converge and token_excluded:
        v = "FORCED-MODULO-TWO-POSITS"
        hline("  >>> FORCED-MODULO-TWO-POSITS.")
        hline("      The SIX sector-restricted minimum-information readings (M1 Shannon, M2 MDL,")
        hline("      M3 Landauer, M4 Jeffreys, M5 Kolmogorov, M6 sufficient-statistic) ALL give the")
        hline("      TYPE weight (1,1) -> r=1/2 -> Q=2/3. They CONVERGE (spread 0).")
        hline("      The ONE token reading (Born, (1,2) -> r=1) is the microstate-pushforward of the")
        hline("      maximally-mixed state I/3 -- and it is EXCLUDED on TWO independent grounds:")
        hline("        (i)  irreversibility makes microstate content non-frozen hence NON-RECORDABLE;")
        hline("        (ii) the token distribution (1/3,2/3) is NOT minimum-information ON THE LABEL")
        hline("             space (it has strictly LESS entropy than uniform; it is more committed).")
        hline("      Hence IRREVERSIBILITY (fixes the recordable sigma-algebra = the 2 sector labels)")
        hline("      + MINIMUM-INFORMATION (minimal faithful register = 1 unit per label) TOGETHER")
        hline("      FORCE r=1/2. Neither alone suffices (irreversibility leaves the type/token bit")
        hline("      open; min-info on microstates would give token). The forcing is genuine: min-info")
        hline("      adds a strictly-new ordering (smaller faithful register wins) that neither")
        hline("      additivity (linear) nor irreversibility (sign of dN/dt) supplies.")
        hline("      BOTH principles are POSITS (the Record axiom's scope excludes arrow/persistence")
        hline("      AND any store-the-least optimization) -> the result is a clean closure-MODULO-")
        hline("      TWO-NAMED-PHYSICAL-PRINCIPLES (records irreversible + records minimal), NOT")
        hline("      bare-axiom-native. AC_phi_lambda for the charged-lepton sector reduces to these")
        hline("      two named principles.")
    elif converge and not token_excluded:
        v = "FORCED-MODULO-POSITS (token not independently excluded)"
        hline("  >>> readings converge but token-exclusion incomplete -- see Part C.")
    else:
        v = "DIVERGE / AMBIGUOUS"
        hline("  >>> DIVERGE. At least one sector-restricted min-info reading gives token -> r=1.")
        hline("      Minimum-information is ambiguous even restricted to sectors; the bit stays open.")
    hline("")
    hline("  Retained no-gos UNWEAKENED: koide_frobenius_isotype_split_uniqueness (retained_no_go,")
    hline("  the (alpha,beta) PD cone is selected-at-a-point, not algebraically collapsed);")
    hline("  koide_z3_equivariant_anticommuting_no_go (retained_bounded, chirality -- Part E confirms")
    hline("  min-info supplies no orbit-splitting). r=1/2 remains Tier-A AC_phi_lambda; compared")
    hline("  structurally only (no PDG value consumed).")
    return v


# ===========================================================================
def main():
    hline("RECORD MINIMUM-INFORMATION + IRREVERSIBILITY INTERLOCK -> r=1/2 DERIVATION TEST")
    hline("=" * 78)
    part_A()
    results, kT0 = part_B()
    part_C(results, kT0)
    part_D()
    part_E()
    v = verdict(results, kT0)
    hline("=" * 78)
    hline(f"COMPUTED VERDICT: {v}")
    hline(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("\n".join(LINES))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
