# Symmetric-Point Per-Channel Curvature Scale `m_curv_tree` from V_taste — Structural Theorem over Declared Boundary Inputs, with N_c Tracking

**Date:** 2026-04-14 (originally); 2026-05-03 (review-loop repair);
2026-05-10 (Gap #3 lite — demote `m_H_tree` to `m_curv_tree`); 2026-06-11
(theorem/boundary-input restructure — see changelog below)
**Claim type:** bounded_theorem
**Claim scope:** one load-bearing structural theorem (T1), one declared
definition (D1), one bounded numeric corollary (C1), and a fenced
class-D comparator appendix.
(T1, load-bearing) On the declared minimal-block mean-field surface
(boundary inputs B3/B4), the per-color staggered taste operator
satisfies `D^2 = -4 u_0^2 I`; all `N_taste = 16` taste eigenvalues are
`+/- 2 i u_0` (multiplicity 8 each); `det(D + m) = (m^2 + 4 u_0^2)^8`
per color; hence `V_taste(m) = -(N_taste/2) log(m^2 + 4 u_0^2)`,
`V_taste''(0) = -N_taste/(4 u_0^2)`, per-channel magnitude
`1/(4 u_0^2)`, and every per-color quantity is exactly
N_c-independent. The registered runner recomputes this entire chain
from primitives in exact arithmetic; nothing in T1 is imported as a
formula.
(D1, declared definition) `m_curv_tree^2 := (|V_taste''(0)|/N_taste) v^2
= v^2/(4 u_0^2)`. This is a defined diagnostic scale, NOT an observable
identification.
(C1, bounded corollary) At the declared inputs B1/B2,
`m_curv_tree = v/(2 u_0) = 140.3 GeV`. NOT a Higgs-mass prediction.
**Resolves:** color-factor dispute (does 8/9 enter the Higgs sector?
Answer: no, N_c cancels in the per-channel curvature scale)
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
`scripts/higgs_tree_level_mean_field_runner_2026_05_03.py` — recomputes
T1 from framework primitives (Clifford generators, eta-phase staggered
operator on the 2^4 block, exact characteristic polynomial and
determinants), checks D1/C1 readout algebra with sensitivity and
anti-tuning certificates, and quarantines all PDG comparators in a
terminal class-D section. Deterministic, stdlib-only, < 1 s.
**Non-verifier scripts (different observables; context only):**
`scripts/frontier_higgs_mass_corrected_yt.py` (corrected-y_t RGE route,
119.93 GeV) and `scripts/frontier_higgs_buttazzo_calibration.py`
(full-3-loop calibration, ~125.1 GeV) compute DIFFERENT observables
along different chains and are not verifiers for this note.

## Changelog — why this note was repaired (2026-06-11)

The 2026-05-29 fresh-look record found that the prior surface was
definition-plus-substitution rather than a standalone theorem:
the load-bearing step as then written was the *definition*
`m_curv_tree^2 := curvature x v^2`, the runner hard-coded the canonical
inputs `U_0 = 0.8776`, `V_GEV = 246.22`, `N_TASTE = 16`, and the
one-hop packet did not close the V_taste determinant/eigenvalue
construction. This restructure fixes six defects:

1. **(Critical) Hidden external scale in the headline.** The prior text
   attributed `v = 246.22 GeV` to "the bounded hierarchy formula". That
   was a miscitation: `246.22` is the PDG-observed EW VEV, while the
   hierarchy lane's bounded formula yields `246.282818290129 GeV` under
   its own admissions and is itself only a bounded numerical-match row
   (`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`, file-pointer
   context). Fix: `v` is now boundary input B2, a declared external EW
   VEV scale that this note does not derive, with an insensitivity
   certificate (both candidate values give `140.3` at headline
   precision; spread `0.026%`).
2. **(Critical) Dead one-hop authorities.** The Dependencies section
   cited `TASTE_POLYNOMIAL_NOTE.md`, `DM_AMGM_SATURATION_NOTE.md`, and
   `HIERARCHY_THEOREM.md`, none of which exists on disk; the
   "eigenvalue degeneracy theorem" had no live authority. Fix: the
   runner now recomputes the determinant/eigenvalue content from
   primitives (T1), and the dead citations are removed. The named
   sister derivation lane for the taste count and W(J) form is
   `HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
   (file-pointer context; unaudited, so not a one-hop authority here —
   T1 does not consume it).
3. **(High) Definition presented as the load-bearing step.** Fix:
   theorem/definition/corollary split. T1's load-bearing content is the
   computed operator-to-curvature chain with exact N_c cancellation;
   D1 is explicitly a definition; C1 is the numeric readout.
4. **(High) Runner verified only formula re-evaluation plus prose
   greps.** Fix: the runner constructs the staggered operator and
   computes `D^2 = -4 u_0^2 I`, the characteristic polynomial
   `(lambda^2 + 4)^8`, the exact determinant identity at rational test
   points, the 48x48 color factorization, and the curvature by finite
   difference on `-log det` — the load-bearing residuals are computed,
   not asserted. Falsification legs F1/F2 included; every check tagged
   [A]/[B]/[C]/[D]; no PASS rests on agreement with a PDG number.
5. **(Medium) Boundary condition glossed.** The prior text said "APBC
   in time" while the degenerate `|lambda| = 2 u_0` spectrum requires
   the antiperiodic wrap in ALL four directions of the minimal `L = 2`
   block (momenta `k_mu = +/- pi/2`, the `sin^2 = 1` saturation point).
   Fix: declared in B4; runner falsification leg F1 shows the time-only
   wrap yields a different determinant `(m^2 + u_0^2)^8`.
6. **(Medium) Miscitation and non-load-bearing graph edge.** Step 6
   cited "YT_EW_COLOR_PROJECTION_THEOREM.md, Section 2.2" (no such
   section; the 8/9 content is its Scope/Binding Claim items 1-2), and
   `HIGGS_FROM_LATTICE_NOTE.md` was wired as a load-bearing dependency
   although it is consumed nowhere in T1/D1/C1 (it is comparator-fence
   context for the delegated gap chain). Fix: citation corrected; the
   lattice note is demoted to a backticked file pointer scoped to the
   fenced comparator appendix.

The arithmetic of the prior note was verified correct and is kept:
`u_0 = 0.877681381`, `m_curv_tree = v/(2 u_0) = 140.3 GeV`, exact N_c
cancellation, and the 2026-05-10 demotion (`m_H_tree -> m_curv_tree`,
no Higgs-pole claim) is preserved unchanged.

**Seventh defect (2026-06-11 follow-up, audit-caught).** The
2026-06-11 audit failed this row on a normalization error in the Step
5(c) susceptibility cross-check as restructured above: the displayed
text wrote the FULL per-site susceptibility as `chi = N_c/(4 u_0²)` —
omitting the `N_taste` factor — and then divided by `N_c · N_taste`,
double-dividing by `N_taste`; the resulting per-channel value
`1/(4 u_0² N_taste)` would NOT have reproduced formula [6]. Fix: the
full susceptibility of the color-stacked generating function
`W(m) = N_c · log det(u_0 D + m)` is

    W''(0) = N_c · N_taste / (4 u_0²),

and the per-color per-channel value is `W''(0)/(N_c · N_taste)
= 1/(4 u_0²)`, equal to the Step-4 per-channel curvature magnitude [4]
(W = −N_c · V_taste, so this is the same algebra). Step 5(c) is
corrected accordingly and the runner adds the C10 assertion pair
computing `W''(0)` from the determinant chain by finite difference and
checking both the full and per-color per-channel values.

## What this note is and is NOT (2026-05-10 demotion, retained)

**This note derives** a per-channel symmetric-point curvature scale of
V_taste on the declared mean-field surface:

    m_curv_tree := sqrt(|V_taste''(0)| / N_taste) · v
                 = v / (2 u_0)
                 = 140.3 GeV   (at the declared inputs B1/B2)

`m_curv_tree` is a dimensionful magnitude (mass units) constructed from
the mass²-coefficient of V_taste at the symmetric point m = 0, divided
by the per-taste-channel multiplicity N_taste = 16, and re-expressed at
the declared EW VEV scale v.

**This note does NOT derive the Higgs-mass pole.** The post-EWSB
Higgs-mass pole is the curvature of the FULL effective potential
V_eff_total at the broken-phase minimum φ = v, not the per-channel
curvature of V_taste at the symmetric point m = 0. Per the
Morse/convexity Gap #3 probe (2026-05-10):

- V_taste(m) = -8 log(m² + 4u_0²) is **monotonically decreasing in |m|**;
- V_taste(m) **has no interior minimum** on its own;
- the broken-phase pole emerges only when V_taste is combined with the
  tree-level mass term and the gauge sector to form V_eff_total.

So `m_curv_tree` is structurally a **symmetric-point per-channel
curvature magnitude** (rescaled by the declared VEV scale v), NOT a
broken-phase pole.

**Earlier drafts of this note labeled this quantity `m_H_tree`.** The
first-principles-honest label is `m_curv_tree`. The demotion is a
relabeling and a scope clarification, not a numerical change. This
mirrors PR #951 v3's κ_curv pattern in
`HIGGS_KAPPA_CURV_FROM_VTASTE_SYMMETRIC_POINT_NARROW_THEOREM_NOTE_2026-05-10.md`
(file pointer, not a load-bearing dependency edge: that note is
downstream — it imports this note's V_taste form).

## Declared boundary inputs (B1-B4) and definition D1

T1 is a theorem **over** these declared inputs. None of them is claimed
as derived by this note.

- **B1 (licensed reuse number).** `<P> = 0.5934`, hence
  `u_0 = <P>^(1/4) = 0.877681381`. License: the plaquette authority
  [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  states the canonical value `0.5934` "may still be used by downstream
  notes only as an admitted comparison/reuse number unless a separate
  retained MC certificate or analytic beta=6 closure is supplied." This
  note consumes the value exactly and only under that license. B1
  enters C1 only; T1 carries `u_0` symbolically.
- **B2 (declared external scale).** `v = 246.22 GeV`, the declared
  external EW VEV scale used to express the dimensionless per-channel
  curvature in mass units. This note does not derive `v`. The
  PDG-observed VEV is `246.22 GeV`; the framework hierarchy lane's
  bounded formula yields `246.282818290129 GeV` under its own
  admissions (`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`,
  file-pointer context, not a one-hop authority — that row records the
  formula as a bounded numerical match with named imports). The two
  candidate values differ by `0.026%` and both give
  `m_curv_tree = 140.3 GeV` at headline precision; the runner certifies
  this insensitivity. B2 enters D1/C1 only, never T1.
- **B3 (licensed channel count).** `N_taste = 16` with uniform
  degeneracy at Wilson coefficient `r = 0`. The 16-corner count, the
  Hamming-class multiplicities `(1,4,6,4,1)`, and the staircase
  `W(hw) = 2 r hw` (hence full degeneracy at `r = 0`) are licensed from
  the retained-bounded row
  [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md),
  and the runner recomputes the count and staircase combinatorially.
  The further identification of the Higgs channel as ONE of the 16
  degenerate channels is a declared structural input; its derivation is
  the open target of the effective-N_taste boundary lane
  (`HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`,
  file-pointer context; that note is downstream of this one).
- **B4 (declared surface).** The minimal-block mean-field surface:
  staggered central-difference operator with eta phases
  `eta_mu(x) = (-1)^(x_0 + ... + x_(mu-1))` on the `L = 2` block of
  `Z^3 + t`, antiperiodic wrap in **all four directions** (equivalently
  momenta `k_mu = +/- pi/2` per axis — the `sin^2 = 1` saturation
  point), and mean-field link factorization `U_{ab} -> u_0 delta_{ab}`.
  The mean-field factorization is a declared approximation, not
  derived. The all-four-directions antiperiodic wrap is load-bearing:
  the runner's falsification leg F1 shows that the old "APBC in time
  only" gloss yields `D^2 = -u_0^2 I` and
  `det(D + m) = (m^2 + u_0^2)^8` — a different surface.
- **D1 (declared definition; NOT an input and NOT an observable
  identification).**

      m_curv_tree² := (|V_taste''(0)| / N_taste) · v² = v²/(4 u_0²)

  D1 introduces the symbol `m_curv_tree` for the per-channel
  symmetric-point curvature magnitude expressed in mass units at the
  declared scale B2. It is a diagnostic definition. The theorem content
  of this note is T1; D1 adds a name, and the note says so.

## Theorem T1 (load-bearing; recomputed from primitives by the runner)

Given B3/B4, with `u_0 > 0` carried symbolically and `m` the
taste-singlet mass probe:

1. **Operator.** The per-color staggered operator
   `D = u_0 · Σ_mu eta_mu Γ_mu` on the 16-site block is real
   antisymmetric and satisfies the exact Clifford-square identity
   `D² = -4 u_0² I`. (Runner: exact Fraction matrix arithmetic;
   companion check `(Σ_mu gamma_mu)² = 4 I` on the 4x4 taste block
   built from Pauli tensor products.)
2. **Spectrum.** The characteristic polynomial of `D/u_0` is
   `(λ² + 4)^8`: all `N_taste = 16` taste eigenvalues are `± 2 i u_0`,
   multiplicity 8 each — the uniform `|λ| = 2 u_0` degeneracy. (Runner:
   exact Faddeev-LeVerrier; the coefficients are computed, not
   imported.)
3. **Determinant.** Per color, `det(D + m) = (m² + 4 u_0²)^8`; over
   `N_c` colors at mean field the determinant factorizes as
   `[det_taste(D + m)]^{N_c}`. (Runner: exact at rational test points,
   including the full 48x48 block matrix at `N_c = 3`.)
4. **Potential and curvature.** Defining the per-color taste potential
   `V_taste(m) := -(1/N_c) log det_color(D + m)
   = -(N_taste/2) log(m² + 4 u_0²)`, the symmetric point `m = 0` is an
   extremum with

       V_taste'(0) = 0,
       V_taste''(0) = -N_taste / (4 u_0²) = -4 / u_0²        [T1.a]

   a tachyonic maximum (the instability that drives EWSB once V_taste
   is combined with the rest of V_eff_total). The per-channel curvature
   magnitude is

       |V_taste''(0)| / N_taste = 1 / (4 u_0²)               [T1.b]

   (Runner: finite-difference second derivative of `-log det` against
   the analytic value.)
5. **Exact N_c cancellation.** Every per-color quantity above —
   including [T1.a] and [T1.b] — is exactly independent of `N_c`.
   (Runner: computed from the determinant chain at
   `N_c ∈ {1, 2, 3, 4}`, spread exactly zero; not a symbol-inspection
   claim.)

### Per-step authority table

| Step | Statement | Class | One-hop authority |
| --- | --- | --- | --- |
| S1 | `<P> = 0.5934`, `u_0 = <P>^(1/4)` (C1 only) | licensed boundary input | [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) reuse license (B1) |
| S2 | `N_taste = 16`, `(1,4,6,4,1)` staircase, degeneracy at `r = 0` | licensed boundary input + runner recompute | [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md) (B3) |
| S3 | `D² = -4 u_0² I`; spectrum `± 2 i u_0` x8; `det(D+m) = (m²+4u_0²)^8`; color factorization | (C) first-principles compute on the declared B4 surface | this note + registered runner (exact arithmetic) |
| S4 | `V_taste''(0) = -N_taste/(4u_0²)`; per-channel `1/(4u_0²)`; exact N_c cancellation | (A)/(C) computed from S3 | this note + registered runner |
| S5 | `m_curv_tree := v · sqrt([T1.b]) = v/(2u_0)` | (E) declared definition D1 over B2 | this note (declared; explicitly not an observable identification) |
| S6 | `m_curv_tree = 140.3 GeV` | (A) exact arithmetic over B1/B2 | corollary C1 below |
| S7 | comparison to PDG `m_H = 125.10 GeV` | (D) fenced comparator | comparator appendix only; never load-bearing |

The load-bearing theorem surface is S2-S4. S1 is the licensed boundary
number used by C1, S5 is a declared definition, S6 is corollary C1, and
S7 lives exclusively in the fenced comparator appendix.

## Corollary C1 (bounded numeric readout)

Substituting B1 (`u_0 = 0.877681381`) and B2 (`v = 246.22 GeV`) into D1:

    m_curv_tree = v / (2 u_0) = 246.22 / 1.755362762 = 140.3 GeV
        (zero free parameters GIVEN the declared inputs;
         per-channel symmetric-point curvature scale)

With the hierarchy-lane candidate value `v = 246.2828 GeV` instead:
`m_curv_tree = 140.30 GeV` — the same headline at `0.1 GeV` precision.

**This is NOT a Higgs-mass prediction.** It is the symmetric-point
per-channel curvature magnitude on V_taste, expressed in mass units at
the declared VEV scale. The downstream bounded Higgs route (~125.1 GeV
under its stated admissions, full 3-loop SM RGE from `λ(M_Pl) = 0`) is
tracked in `HIGGS_MASS_DERIVED_NOTE.md` (file-pointer context; that
note does not load-bear on `m_curv_tree` and already cites this one in
its Note↔runner reconciliation section).

## Sensitivity and anti-tuning certificates

This section certifies that C1 is not a numerical match at a tuned
input scale:

- **One knob only, declared.** Given T1, the readout is the
  parameter-free function `m_curv_tree = v / (2 <P>^(1/4))` of the
  declared inputs `(<P>, v)`. Nothing in S2-S4 can be adjusted; `<P>`
  is fixed upstream by the Wilson action at `beta = 6` (consumed here
  under the B1 license), not by any fit to a Higgs-sector number.
- **Analytic sensitivity, declared and verified.**
  `d m_curv_tree / d<P> = -m_curv_tree / (4 <P>) = -59.09 GeV` per unit
  `<P>`: a `1%` shift in `<P>` moves `m_curv_tree` by `0.25%`. The
  runner verifies this against a central finite difference.
- **No admissible tuning to the PDG pole (falsification leg F2).**
  Forcing `v/(2 u_0) = 125.10 GeV` would require `<P> = 0.9379` —
  `+58%` off the licensed `0.5934`, far outside any admissible
  neighborhood. The chain output at the declared inputs is `140.3 GeV`,
  which sits `+12.1%` ABOVE the PDG pole; the note reports that
  separation as a structural fact (see the comparator appendix), not as
  an agreement.
- **B2 insensitivity.** The two candidate `v` values (PDG-observed
  `246.22`; hierarchy-lane bounded `246.2828`) differ by `0.026%`; both
  give `140.3` at headline precision. The headline does not depend on
  which external scale convention is declared.

## Fenced comparator appendix (class D; never load-bearing)

PDG values appear in this note and its runner ONLY in this section and
in the runner's terminal class-D checks. No PASS rests on agreement
with a PDG number.

- **Observed Higgs pole:** `m_H = 125.10 GeV` (PDG). The C1 output
  `140.3 GeV` sits `+12.1%` above it. This separation is the genuine
  structural distance between two different objects — the
  symmetric-point per-channel curvature magnitude on V_taste (this
  note) and the broken-phase pole of V_eff_total (not this note) — and
  is Morse/convexity-forced: V_taste alone has no interior minimum, so
  its symmetric-point curvature has no pole partner on V_taste. The
  +12% magnitude is NOT claimed as a finite missing correction in this
  note; its closure is delegated to the sister chain in Step 7.
- **Observed EW VEV:** `v_obs = 246.22 GeV` (PDG), consumed as the
  declared external scale B2. The hierarchy lane's bounded formula
  value `246.2828 GeV` differs by `+0.0255%` (comparator context only;
  neither value is derived here).
- **Lattice-spacing context:** the lattice Coleman-Weinberg lane
  (`HIGGS_FROM_LATTICE_NOTE.md`, file-pointer context only — demoted
  from a load-bearing graph edge 2026-06-11 because nothing in
  T1/D1/C1 consumes it) reports `m_H/m_W` flowing from `1.85` at
  `a = 1` toward the SM value as `a` decreases; that is delegated
  gap-chain context, not part of this claim surface.

---

## Derivation walk (Steps 1-6; the content T1 packages)

### Step 1: The generating functional

**Framework baseline.** The Quantum axiom supplies the one-qubit /
`Cl(3)` per-site algebra, and the Lattice axiom supplies the `Z^3`
lattice;
staggered Dirac operator D on the minimal `Z^3 + t` block (`L = 2`,
`N_sites = 2^4 = 16`) on the declared B4 surface, gauge group SU(3) at
`beta = 2 N_c / g² = 6`. The matrix dimension is
`N_tot = N_c · N_sites = 48`.

**Eigenvalue degeneracy (computed, T1 items 1-2).** The Clifford-square
identity `D² = -4 u_0² I` on the B4 surface forces all `N_taste = 16`
taste eigenvalues to `|λ| = 2 u_0`, pure imaginary
(`λ_k = ± 2 i u_0`, staggered anti-Hermiticity), multiplicity 8 per
sign per color. Mean-field factorization (`U_{ab} -> u_0 δ_{ab}`, B4)
extends this to all `N_tot = 48` eigenvalues. This is recomputed from
primitives by the runner — it is not an imported theorem (the prior
citations to `TASTE_POLYNOMIAL_NOTE.md` and `DM_AMGM_SATURATION_NOTE.md`
were dead files and have been removed; the named sister derivation lane
is the taste-count/W(J)-form bridge note, file pointer in the
changelog).

The generating functional at mean field:

    W(J) = Σ_{k=1}^{N_tot} (1/2) log(J² + 4 u_0²)
         = (N_tot / 2) · log(J² + 4 u_0²)                   [1]

**N_c tracking:** `N_tot = N_c · N_sites = 3 · 16 = 48`. The factor
N_c is a linear overall multiplier.

### Step 2: Factoring out color

Color and taste factorize at mean field. The full determinant:

    det(D + J) = [det_taste(D + J)]^{N_c}

(runner check: exact 48x48 block determinant at `N_c = 3`). The
taste-sector generating functional (one color copy):

    W_taste(J) = W(J) / N_c = (N_sites / 2) · log(J² + 4 u_0²)

The taste-sector potential on the minimal block (where
`N_sites = N_taste`):

    V_taste(m) = -(N_taste / 2) · log(m² + 4 u_0²)
               = -8 · log(m² + 4 u_0²)                       [2]

**N_c does not appear in [2].** From here on, the derivation is
N_c-independent. The color links contribute only through
`u_0 = <P>^(1/4)`.

### Step 3: Curvature at the symmetric point (Morse/convexity context)

    d V_taste / dm = -N_taste · m / (m² + 4 u_0²) = 0  at m = 0

    d² V_taste / dm² |_{m=0} = -N_taste / (4 u_0²)
                              = -4 / u_0²                    [3]

The negative curvature confirms the symmetric point m = 0 is a local
maximum of V_taste — a tachyonic instability that drives EWSB when
V_taste is combined with the rest of V_eff.

**Morse/convexity context (Gap #3 probe, 2026-05-10).** The full log
potential V_taste(m) = -8 log(m² + 4 u_0²) is **monotonically
decreasing for m > 0**. It has **no interior minimum on V_taste
alone** — and a fortiori no interior CW minimum that could play the
role of a Higgs broken-phase pole. The physical VEV arises from the
interplay of the fermion determinant with the gauge action and the
tree-level mass (the full CW mechanism); the EW scale enters this note
only as the declared external input B2. This is the structural reason
why `m_curv_tree`, derived from the symmetric-point curvature [3]
alone, is NOT a Higgs-mass pole: V_taste's symmetric-point curvature
has no broken-phase partner *on V_taste*; the pole emerges only from
V_eff_total.

### Step 4: The per-channel symmetric-point curvature

The curvature [3] counts ALL N_taste = 16 degenerate taste channels
responding to the mass shift dm. The Higgs is identified (in the
all-channels-degenerate limit; see "Honest scope") with a single
taste-singlet scalar occupying one out of N_taste channels. By the
computed degeneracy (T1 item 2), each taste channel contributes
equally, so the per-channel curvature is:

    |d² V / dm²|_{per channel} = (4 / u_0²) / N_taste
                                = 1 / (4 u_0²)               [4]

Applying definition D1 (the per-channel curvature magnitude rescaled by
the declared scale B2):

    (m_curv_tree / v)² = 4 / (u_0² · N_taste) = 1 / (4 u_0²)

    m_curv_tree / v = 1 / (2 u_0)                            [5]

    m_curv_tree = v / (2 u_0) = 140.3 GeV  (corollary C1)    [6]

Equations [5]-[6] give the **per-channel symmetric-point curvature
scale**. They do NOT give the Higgs-mass pole; per "Honest scope"
below, that identification holds only in a limit where (i)-(iv) are
exact, none of which is true on the canonical framework surface.

**N_c tracking:** N_c divided out at Step 2 (and verified by
computation at `N_c ∈ {1,2,3,4}`). Equation [4] involves only u_0 and
N_taste. The per-channel symmetric-point curvature scale `m_curv_tree`
is N_c-independent.

### Step 5: Status of the readout map (D1 is a definition, not a derivation)

**(a) Dimensional matching (necessary condition only).** The curvature
d²V/dm² is dimensionless (V is dimensionless, m is dimensionless in
lattice units). The ratio m_curv/v is dimensionless and must equal a
function of the dimensionless lattice quantities u_0 and N_taste.
Dimensional analysis ALONE does not pick out the specific combination —
it only constrains it to be dimensionless.

**(b) What D1 actually is.** D1 defines `m_curv_tree²` as the
per-channel symmetric-point curvature magnitude [4] times the declared
external scale v². This is the standard tree-level mean-field
Klein-Gordon curvature readout in the symmetric phase, adopted here BY
DEFINITION. It identifies a structurally clean object derivable from
V_taste plus the declared scale. It is NOT the broken-phase Higgs-mass
pole, and the note does not claim that identification. The Higgs-pole
identification would additionally require:
(i) all N_taste taste channels exactly degenerate with the physical
Higgs (the uniform `N_taste = 16` channel assignment is a declared
structural input, B3);
(ii) gauge corrections to vanish (they do not);
(iii) the EWSB saddle to align with the symmetric-point curvature (it
does not — V_taste alone has no interior minimum, per Step 3);
(iv) V_eff to have a quadratic-only mass coefficient (it does not —
V_taste's logarithmic m⁴ and higher coefficients are non-zero and
contribute to the broken-phase curvature).

**(c) Susceptibility consistency cross-check (not independent;
normalization corrected 2026-06-11).** The scalar susceptibility
counts the mass-shift response of ALL internal DOF — `N_c` colors ×
`N_taste` channels. From the color-stacked generating function
`W(m) = N_c · log det(u_0 D + m) = −N_c · V_taste(m)`, the full
per-site susceptibility is

    W''(0) = N_c · N_taste / (4 u_0²),

and the per-color per-channel value is

    W''(0) / (N_c · N_taste) = 1 / (4 u_0²),

which equals the per-channel curvature magnitude [4] exactly and, after
the D1 v-rescaling, reproduces formula [6]. (The pre-2026-06-11 text
wrote the full susceptibility as `N_c/(4 u_0²)` — omitting `N_taste` —
and then divided by `N_c · N_taste`, double-dividing by `N_taste`; the
displayed per-channel value `1/(4 u_0² N_taste)` would not have
reproduced [6]. The runner now asserts the corrected chain at C10,
computing `W''(0)` from the determinant by finite difference.) This is
a consistency check that reduces to the same algebra (`W = −N_c ·
V_taste`), not an independent derivation; the theorem content remains
T1, and the readout remains definition D1.

> **Note (2026-05-07 cleanup, kept).** A duplicate of paragraph (c)
> appeared in pre-2026-05-03 drafts with the stale phrasing that "the
> correct identification" maps the susceptibility to the physical
> Higgs mass. That paragraph remains removed; the susceptibility
> content is fully covered by the cross-check framing in (c) above.

**Honest scope of Step 5.** The readout map is a declared definition
(D1) applying the tree-level mean-field Klein-Gordon curvature
identification to a defined diagnostic scale. It is correct *as a
definition*. It is **not** a Higgs-mass-pole derivation. The physical
Higgs mass requires (i) dropping the mean-field approximation,
(ii) summing CW + gauge corrections, (iii) RGE running from the lattice
scale to the physical scale, and (iv) the broken-phase pole differing
from the symmetric-point curvature by the genuine structural
separation described above. None of (i)-(iv) is supplied here.

### Step 6: Does the color factor 8/9 enter the Higgs sector?

**No.** Three independent arguments — all about the per-channel
symmetric-point curvature scale `m_curv_tree`, *not* about a
Higgs-mass-pole prediction.

**Argument 1 (factorization, computed).** The taste potential
V_taste [2] is obtained by dividing `V_full = N_c · V_taste` by N_c.
All quantities derived from it are N_c-independent — verified by the
runner from the determinant chain at `N_c ∈ {1,2,3,4}`, spread exactly
zero. The factor `(N_c² - 1)/N_c²` is a quadratic Casimir ratio with no
algebraic pathway into a linear-in-N_c factorization.

**Argument 2 (different operators).** The 8/9 arises in the EW vacuum
polarization, a 2-point function requiring Fierz decomposition in
q-qbar color space: per
[`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
(Scope and Binding Claim items 1-2), `F_adj = (N_c² - 1)/N_c² = 8/9` is
exact SU(3) Fierz/channel-count algebra inside the EW projection family
`K_EW(kappa_EW)`, and that row is a packet-scoped no-go on selecting
`kappa_EW = 0` — i.e., the 8/9 lives in the EW-coupling projection
family, not in scalar-sector 0-point functions. The per-channel
symmetric-point curvature comes from the scalar susceptibility
chi = d²W/dJ², a 0-point function with trivial color structure
`delta_{ab} delta_{ab} = N_c`.

**Argument 3 (ratio invariance).** Even if 8/9 entered m_W through the
EW coupling correction, it would not enter m_curv_tree/m_W: both are
extracted from the same taste-sector potential and any universal color
correction would cancel in their ratio.

### Summary: N_c tracking table

| Quantity | Formula | N_c dependence |
|----------|---------|----------------|
| W(J) | (N_c N_sites / 2) log(J² + 4 u_0²) | proportional to N_c |
| V_taste(m) | -8 log(m² + 4 u_0²) | NONE (N_c divided out) |
| curvature at m=0 | 4 / u_0² | NONE |
| per-channel curvature | 4 / (u_0² N_taste) | NONE |
| m_curv_tree / v | 1 / (2 u_0) | NONE |
| 8/9 factor | (N_c²-1) / N_c² | enters EW couplings ONLY |

## Honest scope (Gap #3 lite, retained)

**Per-channel symmetric-point curvature ≠ broken-phase pole.** This
identity becomes exact only in a limit where (i) all N_taste taste
channels are degenerate with the physical Higgs channel, (ii) gauge
corrections vanish, (iii) the EWSB saddle aligns with the
symmetric-point curvature, and (iv) V_eff has a quadratic-only mass
coefficient near the symmetric point. **None of (i)-(iv) is exactly
true** on the canonical framework surface.

Concretely, for a standard Mexican hat V = -μ²|φ|² + λ|φ|⁴, the
symmetric-point curvature magnitude |V''(0)| = 2μ² and the broken-phase
pole V''(v) = 4λv² = 2μ² coincide only because of the specific
Mexican-hat relation between the v scale and the μ²-λ ratio. For
V_taste — logarithmic, monotonically decreasing in |m|, with **no
interior minimum** — the symmetric-point curvature has no pole partner
on V_taste alone; the pole emerges only from V_eff_total.

The +12% separation reported in the comparator appendix is the genuine
higher-order separation between these two structurally distinct
objects. It is Morse/convexity-forced, not a numerical accident or a
missing finite correction in this note. Closure is delegated to the
sister-authority chain (Step 7); this note provides the symmetric-point
curvature magnitude as the cited input to that chain.

## Step 7: Authority chain for the +12% separation (context inventory)

This step is an audit-compatible authority inventory for the delegated
gap-closure chain. Each row is a pointer; this note does not change any
sibling claim boundary or effective status (the pipeline-derived status
field in the audit ledger). The audit ledger remains the only authority
for current audit and effective status. Nothing in this table is
load-bearing for T1/D1/C1; sister notes are referenced as backticked
file pointers precisely because they are context, not one-hop
authorities for this claim surface.

| Gap correction | Sister authority (context pointer) | Status authority | Closes the gap from / to | Open content |
|---|---|---|---|---|
| 2-loop CW + RGE running | `HIGGS_MASS_DERIVED_NOTE.md` (backticked to avoid the known back-edge through the EW-coupling cluster; that note already cites this one's tree-level formula) + `scripts/frontier_higgs_mass_corrected_yt.py` (corrected-y_t RGE) | audit ledger only | symmetric-point curvature scale → ~119.93 GeV via corrected-y_t at 3L+NNLO | conditional on `y_t` Ward + RGE-transport scaffolding |
| Lattice spacing convergence (`m_H/m_W` flow as `a → 0`) | `HIGGS_FROM_LATTICE_NOTE.md` (backticked; demoted from a load-bearing graph edge 2026-06-11 — consumed nowhere in T1/D1/C1) | audit ledger only | `m_H/m_W = 1.85` at `a=1` → 1.64 at `a=0.5` → 1.558 SM in continuum | continuum-limit theorem surface |
| Wilson-term taste-breaking ((1,4,6,4,1) staircase) | [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md) (also the B3 license); Wilson follow-on notes `HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`, `WILSON_CORRECTED_V_TASTE_TREE_LEVEL_BOUNDED_NOTE_2026-05-08.md`, `WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`, `WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md` are backticked file-pointer context (each cites this note as its load-bearing parent) | audit ledger only | proves the finite staircase identity and bounded leading-order Wilson correction formulas | **still open**: no retained closure of the physical gap; the channel choice, any nonzero Wilson coefficient `r`, and the leading-order comparison to 125.10 GeV remain bounded/noncanonical inputs |
| Buttazzo full-3-loop calibration cross-check | `scripts/frontier_higgs_buttazzo_calibration.py` | (auxiliary calibration) | independent ~125.1 GeV via 3-loop Buttazzo parametric calibration | a different observable along a different chain; not load-bearing for this note |

### What Step 7 records

- The **2026-05-02 status correction audit packet**
  (`HIGGS_MASS_FROM_AXIOM_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md`,
  backticked file pointer) classifies the lattice-curvature →
  physical-(m_H/v)² bridge as a **same-shape obstruction** with cycle 5
  (yt_ew matching M) and cycle 9 (gauge-scalar observable bridge) —
  a member of the lattice → continuum / physical matching cluster
  identified in `AUDIT_BACKLOG_NOTE_2026-05-02.md` §2.3. That cluster
  requires an independent non-perturbative matching theorem before it
  can support a physical-mass closure. This restructure preserves that
  classification: the bridge remains open, which is exactly why D1 is a
  definition and the Higgs pole is a non-claim.
- This note continues to claim only theorem T1 over the declared
  inputs, with the gap closure explicitly delegated.

## Backward-compatibility note (2026-05-10, retained)

Earlier drafts of this note labeled `m_curv_tree` as `m_H_tree`. Sister
bounded-source-surface notes that import this object continue to use
the older label `m_H_tree` for the same numerical quantity
(`v/(2u_0) ≈ 140.3 GeV`); they compute the same thing. Files where this
naming collision is most direct include
`HIGGS_MASS_12PCT_GAP_DECOMPOSITION_BOUNDED_NOTE_2026-05-10_higgsS7.md`,
`HIGGS_MASS_WILSON_CHAIN_PARTIAL_PROGRESS_NOTE_2026-05-10_higgsH1.md`,
`LATTICE_PHYSICAL_MATCHING_THEOREM_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_match.md`,
`WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`,
`WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08.md`,
and `HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`.
Where these notes cite "`m_H_tree` from `HIGGS_MASS_FROM_AXIOM_NOTE`",
read "the symmetric-point per-channel curvature scale `m_curv_tree`
from `HIGGS_MASS_FROM_AXIOM_NOTE` (previously labeled `m_H_tree`)". The
numerical content is unchanged; only the parent label is demoted.

## Explicit non-claims

This note does **not** claim:

- a Higgs-mass-pole prediction or any post-EWSB observable (the
  broken-phase pole belongs to V_eff_total, not V_taste);
- a derivation, MC certification, or analytic closure of
  `<P> = 0.5934` (declared under the upstream reuse license, B1);
- a derivation of the EW VEV `v` (declared external scale, B2; the
  hierarchy lane's bounded formula is context, not authority);
- a derivation of the Higgs-channel selection among the 16 degenerate
  channels (declared structural input, B3; the effective-N_taste
  boundary lane is the open target);
- a derivation of the mean-field factorization (declared approximation,
  B4);
- closure of the +12% separation (delegated, Step 7);
- closure of the lattice → continuum / physical matching obstruction
  (2026-05-02 status-correction packet; preserved);
- any audit outcome or status promotion (status authority is the
  independent audit lane only).

The honest ceiling for this row is bounded: T1 is exact computed
structure over the declared B3/B4 surface, and B1-B4 are real open work
owned by the upstream plaquette, hierarchy, channel-boundary, and
mean-field lanes.

## Dependencies (one-hop, load-bearing)

- [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  — B1 reuse license for `<P> = 0.5934` (consumed at S1/C1 only).
- [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
  — B3 license for `N_taste = 16`, the `(1,4,6,4,1)` staircase, and
  degeneracy at `r = 0` (also recomputed by the runner).
- [`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md)
  — Step 6 Argument 2: `F_adj = 8/9` is exact SU(3) Fierz algebra
  scoped to the EW projection family only.

Context file pointers (backticked throughout; deliberately omitted from
the citation graph as non-load-bearing): `HIGGS_MASS_DERIVED_NOTE.md`,
`HIGGS_FROM_LATTICE_NOTE.md`,
`HIGGS_MASS_FROM_AXIOM_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md`,
`AUDIT_BACKLOG_NOTE_2026-05-02.md`,
`HIGGS_KAPPA_CURV_FROM_VTASTE_SYMMETRIC_POINT_NARROW_THEOREM_NOTE_2026-05-10.md`,
`HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`,
`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`,
`HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`,
and the Wilson follow-on notes listed in Step 7. The prior citations to
`TASTE_POLYNOMIAL_NOTE.md`, `DM_AMGM_SATURATION_NOTE.md`, and
`HIERARCHY_THEOREM.md` were dead files (absent from the repository) and
were removed in the 2026-06-11 restructure; their content (eigenvalue
degeneracy, taste determinant) is recomputed from primitives by the
registered runner, and the VEV input is declared at B2.

## Verification

Run:

```bash
python3 scripts/higgs_tree_level_mean_field_runner_2026_05_03.py
```

Expected result (deterministic, pure Python stdlib, runtime under one
second):

```text
Breakdown: A=6 B=9 C=14 D=2
TOTAL: PASS=31 FAIL=0
```
