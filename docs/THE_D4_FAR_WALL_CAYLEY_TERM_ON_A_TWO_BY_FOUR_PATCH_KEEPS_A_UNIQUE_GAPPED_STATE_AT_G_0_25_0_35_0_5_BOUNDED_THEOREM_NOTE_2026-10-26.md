---
claim_id: the_d4_far_wall_cayley_term_on_a_two_by_four_patch_keeps_a_unique_gapped_state_at_g_0_25_0_35_0_5_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "(1) Exact: with the Z4 twist the wall slice has magnetic translations T_x, T_y (c_r -> w c_{r+e}, w = -i on a wrap) that
commute with the hop and the Cayley term and act as T_A x T_B on the two-chirality register, so (Q, n_A mod 2, K) label
sectors; A <-> B exchange maps Q -> -Q. (2) Finite: the momentum-sector code reproduces the parent 2x2 and 2x3 values
(matvec to 1e-14, gaps to 1e-3). On the 2x4 periodic patch (37.6 M states per momentum sector, Mac mini) the ground state
is unique in (Q, n_A mod 2, K) = (0, 0, 0) at g = 0.25, 0.35, 0.5, with gaps 0.700, 2.900, 5.628 against 0.290, 3.182,
5.599 at 2x3: SURVIVING by the pre-set rule at all three g. At g = 0.25 the trend is non-monotone and the 2x4 gap is below
the free finite-size gap (0.44 x), so g = 0.25 is near the 2D transition. Three width-2 patches only; no thermodynamic claim."
upstream_dependencies:
  - the_d4_far_wall_cayley_term_on_two_plus_one_d_patches_keeps_a_unique_gapped_state_above_a_sharp_transition_near_g_0_25_bounded_theorem_note_2026-10-26
runner: scripts/the_d4_far_wall_cayley_term_on_a_two_by_four_patch_keeps_a_unique_gapped_state_at_g_0_25_0_35_0_5_2026_10_26.py
---

# The D4 far-wall Cayley term on a 2x4 patch keeps a unique gapped state at g = 0.25, 0.35 and 0.5

Runner: runner.py, TOTAL: PASS=22 FAIL=0, 41 s on the laptop, 135 MB peak, 2.7 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (scratch/d4_far_wall_2x4_unique_test_run.py). The criteria were fixed in criteria_pre_run.txt
before any 2x4 eigenvalue was computed. Axioms unchanged; no CL edit; no rule adopted.
Labels: [T] exact, [F] finite live diagnostic, [R] embedded Mac mini result.

## Question
The parent probe (d4-far-wall-2plus1) found 2x2 -> 2x3 gaps of 0.886 -> 0.290 (g = 0.25), 2.557 -> 3.182 (0.35) and
5.639 -> 5.599 (0.5). Its 2x3 GS-sector minimum is 0.017 at g = 0.2435, a sharp transition. Does a third size, 2x4, close
or keep the gap at fixed g?

## A. Model
The model is unchanged: the parent core.py, copied byte for byte. It has the 4-mode register, the Dirac hop
i psi^+ Gamma_k psi' on the (n1, n2) slice with t = 1, the on-site Cayley term g [8 (Omega + Omega^+) - sum s_a s_b], and
psi -> i psi on every wrap. Only the patch size changes.

## B. Symmetry reduction [T]
- At 2x4 the (Q = 0, n_A even) sector has 3.0e8 states, which is 4.8 GB per vector. That is over the 6 GB cap for any Lanczos.
- With the twist, the translations that commute with the hop are magnetic: c_r -> w c_{r+e}, with w = -i on a wrap
  (w = +i fails, by 2.83). Omega gains w^4 = 1, so the Cayley term is invariant. The translations act on each species'
  Fock space separately, so T = T_A x T_B on the Kronecker register.
- Each species' Fock sector is rotated orbit by orbit to a joint T_x, T_y eigenbasis. The cross-species terms
  sum_x O_A,x x O_B,x become (1/N) sum_q Ot_A(q) x Ot_B(q). The occupation terms use a plain Fourier grid; the pair term
  uses a half-shifted grid, because T P_x T^-1 picks up -1 on a wrap. The code checks that each transform moves momentum by
  exactly one label.
- Result: 8 momentum sectors of 3.76e7 states (0.56 GB per vector). A plain three-term Lanczos uses 3 vectors, plus one
  stored ground vector for the deflated e1.
- h_A = h_B, so A <-> B exchange is exact and Q = -1 mirrors Q = +1. At 2x3 and 2x4 the (1,0) and (1,1) momentum spectra
  coincide as sets, which suggests a particle-hole x exchange symmetry. That is observed, not derived.

## C, D. Validation [F]
- At 2x2 the momentum matvec equals the parent matvec mapped through the basis to 1.1e-14, and min over K of e0 equals the
  parent full-sector e0 to 6e-14.
- The live gaps are 0.8861, 2.5573, 5.6393 at 2x2 and 0.2896, 3.1819, 5.5989 at 2x3. They equal the parent values.
- At 2x3 the GS is at K = 0. At g = 0.25 the lowest excitation is in the same (Q, par) sector at a different momentum.

## E. 2x4 [R]
Run on Jonathons-Mac-mini.local, 2026-10-26 16:43 -> 2026-10-27 02:34 EDT, 35,451 s wall time. One worker, one BLAS thread,
nice 10. Peak RSS 3,079 MB against a 6,000 MB self-monitored cap. System memory stayed at 48-53% free and the load stayed
below 4. The run covered 96 sectors (3 g x (Q, par) in {0,1}^2 x 8 K) plus a deflated e1 per g. The Ritz value converged to
1e-8, with ground-vector residual <= 5e-7.

| g | gap 2x2 | gap 2x3 | gap 2x4 | 2x4/2x3 | 2x4/free | E0/site 2x2, 2x3, 2x4 | lowest excitation | class |
|---|---|---|---|---|---|---|---|---|
| 0.25 | 0.886 | 0.290 | 0.700 | 2.41 | 0.44 | -4.216, -4.188, -4.219 | (0,0), K label (4,8) | SURVIVING |
| 0.35 | 2.557 | 3.182 | 2.900 | 0.911 | 1.80 | -5.315, -5.340, -5.342 | (0,0), K label (4,8) | SURVIVING (just) |
| 0.5 | 5.639 | 5.599 | 5.628 | 1.005 | 3.50 | -7.287, -7.296, -7.296 | Q = 1 (4-fold: both parities, 2 K) | SURVIVING |

The free 2x4 gap is 1.608 (2x3: 1.732). At every g the GS sits alone in (0,0,K=0); the in-sector e1 - e0 values are 0.94,
4.95 and 8.56.

## Verdict (pre-set criteria)
- All three g are SURVIVING: the 2x4 gap is >= 0.9 times the 2x3 gap, and the ground state is unique. None is CLOSING.
- For g >= 0.35 the gap is flat in patch size: 2.56/3.18/2.90 and 5.64/5.60/5.63. E0/site is converged to about 3e-3. The gap
  is 1.8 to 3.5 times the free finite-size gap, with no low tower. This is the clean signal: a symmetric, uniquely gapped
  Cayley state on three width-2 patches.
- g = 0.25 passes the rule, but the pass is fragile:
  - The gap is non-monotone (0.886, 0.290, 0.700), and it is below the free finite-size gap. By the parent's own
    "Delta < Delta_free" test it would read CLOSING.
  - The likely reading is that 2x3 sits almost on its own avoided crossing (g_x(2x3) ~ 0.2435), and that g_x drifts with
    patch size. At 2x4, g = 0.25 is on the strong side but close.
  - The 2x4 g_x was not scanned. Each g costs about 3.3 h on the mini.

## What would decide
- A 2x4 GS-sector scan over g in [0.2, 0.3]. Only (0,0) is needed, with K = 0 and K = (4,8): about 10 min per g on the mini.
  It would give the minimum-gap scaling over three sizes and the drift of g_x.
- 3x3 or 4x4 patches are beyond ED. They need DMRG on width-3/4 cylinders or sign-free QMC (the SU(4)-type bilayer
  literature is context only and is not used).

## Smuggling review
- Supplied: the 4-mode register (owner-deferred Qubit bend), the Cayley form and weight, the naive hop t = 1 (doublers
  kept), the Z4 twist, the patch shapes, and g (three values set by the caller; nothing fitted).
- Forced: the magnetic-translation phase w = -i (the only choice that commutes), the momentum labels, Q -> -Q.
- No CL text: this is a finite-size trend on quasi-ladders. Any far-wall CL text should state the coupling as
  "g >= ~0.35 on 2D patches" and not as the chain value.
