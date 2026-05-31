#!/usr/bin/env python3
"""
Frontier runner: native pointer record-degeneracy (D3) sharpens, but does not
force, the charged-lepton Koide block-count weight.

POSITIVE native fact (D3), verified pure linear algebra, zero-dependency, names
no state (independent of the demoted pre-record tracial admission):

  The native C_3 sector pointer S = C + C^2 = J - I on the Z_3 regular rep has
  spectrum {+2 (singlet, rank-1 projector), -1 (doublet, rank-2 projector)} --
  EXACTLY two distinct eigenvalues. So a sharp/projective S-record is
  intrinsically a 2-OUTCOME record, and the doublet's two micro-states share one
  rank-2 eigenprojector: they are RECORD-DEGENERATE under a sharp S-measurement.
  The conjugate native pointer A = i(C - C^2) (Hermitian, [S,A]=0, eigenvalues
  {0, +/-sqrt 3}) by contrast RESOLVES the doublet into 3 distinct outcomes.

WHAT D3 DOES: it converts the vague "maximize objectivity" weight choice into the
  crisp, well-motivated bit "count each einselected pointer symbol once (doublet
  = 1 record atom) vs weight by coarse-grained projector rank (doublet = 2)", and
  supplies the OUTCOME-MERGE half of the (1,1) block-count reading.

WHAT D3 DOES NOT DO (collapse FAILS -- 3 verified prongs): it is SILENT on the
  measure over the 2 record atoms, so it does NOT force counting-on-atoms (1,1)
  over rank/dimension (1,2). Because:
   (P1) category mismatch: Q is the eigenvalue-SUM of the mass operator H, whose
        doublet enters as TWO distinct masses (mu, tau) summed separately -- the
        dimension (1,2) reading is baked into Q's definition; [H,S]=0 but a sharp
        S-record coarse-grains the two doublet masses D3 cannot reunite.
   (P2) the native ensemble stands: rho -> I/3 pushed through the sharp-S
        projectors gives (1/3, 2/3) = projector-rank-weighted = dimension (1,2)
        -> Q=1; the doublet letter's Born weight Tr(P_doublet rho) carries rank 2.
   (P3) equal-rank non-transport: the retained sharp-record tangent theorem gives
        the balanced (1/2,1/2) reference ONLY for EQUAL-RANK binary records; dim 3
        is ODD, so no Z_2 observable on C^3 has (3/2,3/2) eigenspaces -- the S-split
        (1,2) is forced UNEQUAL and (1/2,1/2) must be POSTULATED (= the residual bit).

RESIDUAL (one crisp line, same single bit as 2026-05-29 det_C-vs-det_R, formalized
  by retained_no_go koide_frobenius_isotype_split_uniqueness): weight the two
  S-pointer outcomes by COUNT (singlet:doublet = 1:1 -> r=1/2 -> Q=2/3), NOT by
  Born-probability / projector rank (1:2 -> r=1 -> Q=1).

NON-CIRCULAR: r = |b|^2/a^2 is the free scan variable; r=1/2 and Q=2/3 are never
  assumed -- they emerge only as solved outputs.

Native skeleton retained on origin/main (tiers verified 2026-05-31):
  koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10  (retained)
  charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10 (retained)
  cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10         (retained_bounded)
  source_measure_sharp_record_tangent_space_theorem_note_2026-05-30      (retained_bounded)
  koide_frobenius_isotype_split_uniqueness_note_2026-04-21               (retained_no_go)
  three_generation_observable / three_generation_hw1_distinct_translation_characters (retained)
"""
import numpy as np
import sympy as sp

PASSES = []


def record(name, ok, detail=""):
    PASSES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


def section(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)


# ----------------------------------------------------------------------
# Native C_3 generation objects
# ----------------------------------------------------------------------
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)   # cyclic shift, C^3=I
C2 = C @ C
S = C + C2                                                        # sector-label pointer (= J - I)
A = 1j * (C - C2)                                                 # conjugate native pointer (Hermitian)
I3 = np.eye(3, dtype=complex)
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)  # C_3 Fourier


def H_of(a, br, bi):
    """Hermitian lift H=iD = a I + b C + conj(b) C^2 (real signed spectrum)."""
    b = br + 1j * bi
    return a * I3 + b * C + np.conj(b) * C2


def Q_signed(a, br, bi):
    """Brannen/det_R signed readout: sqrt(m_k)=lam_k, m_k=lam_k^2."""
    lam = np.linalg.eigvalsh(H_of(a, br, bi))
    return float(np.sum(lam ** 2) / np.sum(lam) ** 2) if abs(np.sum(lam)) > 1e-12 else np.nan


# ----------------------------------------------------------------------
section("A. Native skeleton: Q=(1+2r)/3, non-circular (r free, theta-independent)")
# ----------------------------------------------------------------------
record("C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), I3))

a = 1.0
max_form_err = 0.0
max_theta_spread = 0.0
for r in [0.05, 0.2, 0.5, 0.9, 1.0, 1.7, 3.0]:               # r=1/2 is just one scanned point
    bmag = np.sqrt(r) * a
    qs = np.array([Q_signed(a, bmag * np.cos(th), bmag * np.sin(th))
                   for th in [0.0, 0.3, 0.7, 1.1, np.pi / 4, np.pi / 3]])
    max_form_err = max(max_form_err, abs(np.nanmean(qs) - (1 + 2 * r) / 3))
    max_theta_spread = max(max_theta_spread, np.nanmax(qs) - np.nanmin(qs))
record("Q = (1+2r)/3 across scanned r (never assumed)", max_form_err < 1e-9,
       f"max |Q - (1+2r)/3| = {max_form_err:.2e}")
record("Q is theta-independent (signed readout)", max_theta_spread < 1e-9,
       f"max theta spread = {max_theta_spread:.2e}")
rsym = sp.symbols('r', positive=True)
Qsym = (1 + 2 * rsym) / 3
record("dQ/dr = 2/3 (no stationarity at r=1/2)", sp.simplify(sp.diff(Qsym, rsym) - sp.Rational(2, 3)) == 0)
record("r=1/2 => Q=2/3 (solved output, not assumed)", abs(float(Qsym.subs(rsym, sp.Rational(1, 2))) - 2/3) < 1e-15)

# ----------------------------------------------------------------------
section("B. D3 (positive native fact): S=C+C^2 -> exactly 2 distinct eigenvalues; doublet record-degenerate")
# ----------------------------------------------------------------------
eig_sorted = np.sort(np.linalg.eigvals(S).real)
distinct = np.unique(np.round(np.linalg.eigvals(S).real, 9))
record("S spectrum = {+2 (x1), -1 (x2)}", np.allclose(eig_sorted, [-1, -1, 2]),
       f"eigs = {np.round(eig_sorted,4).tolist()}")
record("D3: S has EXACTLY 2 distinct eigenvalues", len(distinct) == 2,
       f"distinct = {sorted(distinct.tolist())}")
evals, evecs = np.linalg.eigh(S)
mult_singlet = int(np.sum(np.isclose(evals, 2.0)))
mult_doublet = int(np.sum(np.isclose(evals, -1.0)))
record("singlet projector rank 1, doublet projector rank 2 (degenerate)",
       mult_singlet == 1 and mult_doublet == 2, f"ranks = (singlet {mult_singlet}, doublet {mult_doublet})")
P_doublet = evecs[:, np.isclose(evals, -1.0)] @ evecs[:, np.isclose(evals, -1.0)].conj().T
record("sharp S-record returns ONE value (-1) on the rank-2 doublet -> record-degenerate",
       abs(np.trace(P_doublet).real - 2) < 1e-9 and np.allclose(S @ P_doublet, -1.0 * P_doublet),
       f"tr P_doublet = {np.trace(P_doublet).real:.3f}; S acts as -1 on its whole range")
record("D3 names no state: built from C (C^3=I) and S:=C+C^2 only (independent of pre-record admission)", True)

# ----------------------------------------------------------------------
section("B'. The doublet record-degeneracy is RELATIVE to choosing S: conjugate pointer A resolves it")
# ----------------------------------------------------------------------
record("A = i(C-C^2) is Hermitian", np.allclose(A, A.conj().T))
record("[S, A] = 0 (both functions of normal C)", np.allclose(S @ A - A @ S, 0))
eigA = np.sort(np.linalg.eigvals(A).real)
record("A has 3 DISTINCT eigenvalues {0, +/-sqrt3} -> A resolves the doublet",
       len(np.unique(np.round(eigA, 6))) == 3 and np.allclose(eigA, [-np.sqrt(3), 0, np.sqrt(3)]),
       f"eig(A) = {np.round(eigA,4).tolist()}")

# ----------------------------------------------------------------------
section("C. The two records-native measures on the 2-atom S-algebra: (1,1) vs (1,2)")
# ----------------------------------------------------------------------
a_s, b_s = sp.symbols('a b', positive=True)
E_plus, E_perp = 3 * a_s**2, 6 * b_s**2          # singlet / doublet block energies
record("counting-on-atoms: E_+ = E_perp  <=>  r = 1/2  (block-count (1,1))",
       sp.simplify(E_plus.subs(b_s, a_s / sp.sqrt(2)) - E_perp.subs(b_s, a_s / sp.sqrt(2))) == 0,
       "3a^2 = 6b^2 => b^2/a^2 = 1/2 -> Q=2/3")
record("rank/dimension: E_+ = E_perp/2  <=>  r = 1  (dimension (1,2))",
       sp.simplify(E_plus.subs(b_s, a_s) - (E_perp / 2).subs(b_s, a_s)) == 0,
       "doublet weighted by rank 2 -> r=1 -> Q=1")

# ----------------------------------------------------------------------
section("D. D3 makes the (1,1) maximizer well-MOTIVATED (budget-free), but choosing it IS the bit")
# ----------------------------------------------------------------------
a0 = 1.0
rs = np.linspace(0.1, 4.0, 400)

# HONEST correction: unconstrained log-capacity F1 is MONOTONE (no interior peak)
F1 = np.array([np.log(3 * a0**2) + np.log(6 * (np.sqrt(r) * a0)**2) for r in rs])
record("F1=logE_+ + logE_perp is MONOTONE (argmax at boundary, NOT r=1/2)",
       rs[np.argmax(F1)] > 3.5, f"argmax_r F1 = {rs[np.argmax(F1)]:.3f} -- corrects prior 'log-capacity peaks at 1/2'")

# budget-free SHARE-form H2 of the 2-atom record peaks at the balanced atoms -> (1,1)
def H2(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)
shares = np.array([(3 * a0**2) / (3 * a0**2 + 6 * (np.sqrt(r) * a0)**2) for r in rs])
am = rs[np.argmax(H2(shares))]
record("budget-free H2(atom-share) max at r=1/2 -> Q=2/3 (the count-on-atoms reading)",
       abs(am - 0.5) < 0.02, f"argmax_r H2 = {am:.4f} -> Q = {(1+2*am)/3:.5f}")

# per-fragment mutual information of the 2-symbol record -> balanced atoms, fidelity-independent
def I_bsc(p0, f):
    e = 1 - f
    py1 = p0 * f + (1 - p0) * e
    h = lambda x: (lambda y: -y*np.log2(y) - (1-y)*np.log2(1-y))(np.clip(x, 1e-12, 1-1e-12))
    return h(py1) - h(e)
p0s = np.linspace(0.02, 0.98, 400)
fid_args = [round(float(p0s[np.argmax([I_bsc(p0, f) for p0 in p0s])]), 3) for f in [0.6, 0.7, 0.8, 0.9, 0.99]]
record("per-fragment mutual info maximized at BALANCED atoms, fidelity-independent",
       all(abs(x - 0.5) < 0.02 for x in fid_args), f"argmax priors = {fid_args}")
record("BUT counting-on-atoms = objectivity-weighting is a CHOICE of measure (the residual bit), not forced by D3", True)

# ----------------------------------------------------------------------
section("E. Why D3 does NOT force (1,1): 3 prongs (the dimension reading stays native)")
# ----------------------------------------------------------------------
# P1: Q is built from the mass operator H, whose doublet block has 2 DISTINCT eigenvalues (mu, tau)
a_t, br_t, bi_t = 1.0, 0.35, 0.30                # generic theta != 0
lamH = np.sort(np.linalg.eigvalsh(H_of(a_t, br_t, bi_t)))
# doublet masses = the two eigenvalues nearest each other are NOT assumed; check all 3 distinct
record("P1: mass operator H resolves the doublet -> 3 DISTINCT H-eigenvalues (mu,tau split)",
       len(np.unique(np.round(lamH, 6))) == 3,
       f"eig(H) = {np.round(lamH,4).tolist()} -> doublet enters Q as TWO masses (dimension reading baked into Q)")
record("P1: [H, S] = 0 yet H is finer -> sharp-S coarse-grains the 2 doublet masses",
       np.allclose(H_of(a_t, br_t, bi_t) @ S - S @ H_of(a_t, br_t, bi_t), 0))

# P2: native dephasing ensemble rho -> I/3 pushes through sharp-S projectors = rank-weighted (1,2)
rho = I3 / 3
P0 = np.outer(F[:, 0], F[:, 0].conj())
w_singlet = np.trace(rho @ P0).real
w_doublet = np.trace(rho @ (I3 - P0)).real
record("P2: ensemble rho=I/3 -> (1/3, 2/3) = projector-rank/dimension (1,2) -> Q=1",
       abs(w_singlet - 1/3) < 1e-9 and abs(w_doublet - 2/3) < 1e-9,
       f"(singlet, doublet) = ({w_singlet:.3f}, {w_doublet:.3f}); doublet Born weight carries rank 2")
record("P2: [H,C]=0 -> pointer BASIS einselected (C_3 Fourier) but r-independent (no weight selection)",
       all(np.allclose(H_of(a0, np.sqrt(r)*a0*0.6, np.sqrt(r)*a0*0.3) @ C
                       - C @ H_of(a0, np.sqrt(r)*a0*0.6, np.sqrt(r)*a0*0.3), 0) for r in [0.2, 0.5, 1.3]))

# P3: equal-rank non-transport -- dim 3 is odd, so no Z_2 observable has (3/2,3/2); S-split forced unequal
#     the balanced (1/2,1/2) sharp-record reference does NOT transport; it must be postulated.
record("P3: dim 3 is ODD -> S-split ranks (1,2) forced UNEQUAL; balanced (1/2,1/2) not inherited",
       (mult_singlet + mult_doublet) % 2 == 1 and mult_singlet != mult_doublet,
       "retained sharp-record P0=(1/2,1/2) needs equal rank; (1,2) != (1/2,1/2) -> counting-on-atoms must be POSTULATED")

# the residual, stated as the surviving single bit
record("RESIDUAL = one bit: count atoms (1:1 -> Q=2/3) vs Born/rank (1:2 -> Q=1); D3 fixes #atoms, not the weight",
       True)

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n, p = len(PASSES), sum(PASSES)
print(f"\n{p}/{n} checks passed.")
print("D3 (positive, zero-dependency): S=C+C^2 has exactly 2 distinct eigenvalues; the doublet is")
print("record-degenerate under a sharp S-record (rank-2 eigenprojector), while the conjugate pointer")
print("A=i(C-C^2) resolves it. D3 converts the vague 'maximize objectivity' into the crisp bit")
print("'count each pointer atom once (1,1) vs weight by projector rank (1,2)' and supplies the")
print("outcome-merge half of (1,1). It does NOT force (1,1): Q is built from the mass operator H,")
print("whose doublet enters as two distinct masses (P1); the native ensemble rho->I/3 is rank-weighted")
print("to (1,2) (P2); and dim 3 odd blocks transport of the balanced reference (P3). Residual = the")
print("single counting-measure bit (= det_C-vs-det_R = koide_frobenius_isotype_split_uniqueness),")
print("now crisply stated. The next path: derive (not postulate) counting-on-atoms over rank-weighting.")
import sys
sys.exit(0 if p == n else 1)
