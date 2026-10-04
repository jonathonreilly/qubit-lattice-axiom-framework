# Lane 3 — Quark Masses Retention

**Date:** 2026-04-26
**Status:** ACCEPTED CRITICAL OPEN SCIENCE LANE on `main`; no theorem or claim
promotion
**Science priority:** HIGHEST. CKM closing in α_s + rationals does NOT satisfy
"quark masses derived."
**Approachability:** Tier B-C (4–8 months for full closure; first sub-targets
landable in 4–8 weeks)
**Primary closure targets:** retained `m_u`, `m_d`, `m_s`, `m_c`, and `m_b`
from framework-native amplitudes and threshold-local retention.
**First parallel-worker target:** separate the bounded companion matches from
actual load-bearing theorem targets, then attack one up-type and one down-type
sub-target.
**Non-claim boundary:** the top mass is retained; the remaining five quark
masses are not.


## Landing correction to the comparator (2026-10-04)

The common-scale diagnostic uses four-loop mass/coupling running with
explicit **two-loop** bottom-threshold coupling and strange-mass matching:
`m_s^(4)(mb) = [1 + (89/432)(alpha_s^(5)(mb)/pi)^2] m_s^(5)(mb)`.
It is a mixed-truncation diagnostic, not a fully matched four-loop prediction;
three-loop decoupling and truncation/systematic uncertainties remain open.
The earlier precise numbers below omitted strange-mass matching and are
superseded by the corrected runner. The mismatch remains about 19%.
The quoted PDG-2024 quark-mass errors are **90% confidence halfwidths**;
combining them with the 68% coupling error in quadrature measures sensitivity,
not a one-sigma significance or a joint statistical rejection. Any “16 sigma”
reading below is withdrawn. Ratio scale invariance applies to a common,
fixed-flavour, mass-independent QCD theory. The SM example only checks its
sampled scales in a supplied truncated one-loop flow (fixed tau Yukawa,
imported initial data, no threshold matching); it supplies no all-scale bound.
Mixed-scale root fits are restricted to the bracket `[1.3,8] GeV`; a root below
that bracket is not evaluated without charm matching.
Source for decoupling conventions: [RunDec, Eqs. 20 and 28](https://arxiv.org/pdf/hep-ph/0004189).
No framework coefficient, exponent or scale is derived by this comparison.

## Corrigendum (2026-09-30)

**What was wrong.** Sections 1 and 2 count the down-type "threshold-local
self-scale" matches (`m_s/m_b = 0.02239`, `+0.2%`; `m_d/m_b`, `+3.5%`) as
sub-percent bounded-companion results, and Section 2 says "perturbative QCD
shifts give Δp ~ 0.01". Those comparators divide a mass at 2 GeV by the bottom
mass at its own mass. The ratio of two MS-bar masses at one energy is
energy-independent, so the scale-consistent test is at one common scale. With
four-loop QCD running and PDG 2024 inputs (`m_s(2 GeV) = 93.5(8) MeV`,
`m_b(m_b) = 4.183(7) GeV`, `alpha_s(M_Z) = 0.1180(9)`), `m_s(m_b)/m_b(m_b) = 0.018878`
and the bridge prediction misses by `+18.6% +- 1.2%` (about 16 sigma with PDG
errors, atlas `|V_cb|` taken as exact; `+16.9%` to `+20.4%` across standard input
sets; `+20.6%` from lattice mass ratios with no running); `m_d/m_b` misses by
`+22.5%`. The exponent that fits the common-scale `m_s/m_b` is `0.7975`, not `5/6`
(a shift of `0.036`, not `0.01`, and no running can supply it: the RG-invariant
ratio does not run), and it stays `0.79` to `0.80` up to the Planck scale under
one-loop Standard-Model running.

**Corrected planning input.** Target 3A should not be read as "prove the
non-perturbative dynamics that closes a small residual". The bridge as written
(exponent `5/6`, prefactor `1`) has no scale-consistent numerical support; on the
RG-invariant ratio it would need a prefactor `1.15` or an exponent `0.80`. The
`+0.2%` is a mixed-scale convention coincidence (it needs the strange mass quoted
at `1.99 GeV`). `m_d/m_s`, a ratio of two masses at 2 GeV, keeps its `+3.3%`.

**What still stands.** Every non-claim and firewall statement of this lane, and
the exact identity `C_F - T_F = 5/6`. The status of this note is unchanged by
this corrigendum; audit status remains with the independent audit lane. Full
table and evidence: `CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`
(Corrigendum).

## 2026-04-27 Dependency Firewall

The [Quark Lane 3 bounded-companion retention firewall](../../QUARK_LANE3_BOUNDED_COMPANION_RETENTION_FIREWALL_NOTE_2026-04-27.md)
records the current no-go boundary for this lane. The top mass is retained,
but CKM closure, bounded down-type ratios, and bounded up-type extensions do
not by themselves retain `m_u`, `m_d`, `m_s`, `m_c`, or `m_b`.

The firewall blocks any five-mass closure unless a branch supplies theorem-core
down-type bridges and scale selection, a retained up-type partition or scalar
amplitude law, and a species-differentiated Yukawa Ward or equivalent absolute
scale primitive for non-top quarks.

## 1. Missing-science framing

The CKM atlas/axiom package closes many mixing identities, but the framework
still needs direct answers to:

> "Wait — what about m_u, m_d, m_s, m_c, m_b? You closed CKM without using
> quark masses, but where are the quark masses themselves?"

The answer in the current package is "bounded companion" — meaning the
threshold-local self-scale comparison gives sub-percent matches but the
comparison uses PDG values, not framework-derived ones. The 5/6 = C_F − T_F
exponent for V_cb is a structural identity but its non-perturbative proof at
lattice scale remains open. The up-type sector has a candidate scalar law
shortlist (7/9, √(3/5), atan(√5)−√5/6, ...) but no derivation principle picks
one.

**Result: 5 of 6 quark masses are effectively pinned to PDG values via the
bounded companion lane. This is a central missing-science issue for
the framework's TOE claim after Koide.** Closing CKM structurally without
closing the quark mass values themselves is a partial result, not a full
flavor-sector closure.

## 2. Current state of repo content

### Retained

- m_t (pole) = 172.57 GeV at 0.07% (2-loop) — the only retained quark mass
- y_t(M_Pl)/g_s(M_Pl) = 1/√6 (exact lattice-scale Ward identity)
- Full CKM structural closure (every entry + B_s + Thales + NLO γ̄ + Jarlskog NLO
  + barred apex/circumradius/orthocenter — all in α_s and rationals)

### Bounded companion

- Down-type CKM-dual mass-ratio lane:
  - m_d/m_s = 0.05165 (+3.3% from threshold-local self-scale comparator)
  - m_s/m_b = 0.02239 (+0.2%)
  - m_d/m_b = 0.001156 (+3.5%)
- Up-type bounded extension with one interior partition (f_12, f_23)
- 5/6 bridge (V_cb = (m_s/m_b)^(5/6)) — perturbative QCD shifts give Δp ~ 0.01,
  full shift requires non-perturbative dynamics at g=1
- Up-type amplitude scalar law shortlist:
  - 7/9 (strongest small-rational refit)
  - √(3/5) (strongest small-radical anchored)
  - atan(√5) − √5/6 (best one-step native projector/support law)
  - √(5/6) · (1 − 1/√42) (best anchored projector law)
- Quark taste-staircase support
- (Approximately 10 structural support notes in
  [QUARK_MASS_RATIO_NOTE_2026-04-18.md](../../QUARK_MASS_RATIO_NOTE_2026-04-18.md))

### Absent

- Direct retention of m_d, m_s, m_b, m_u, m_c (only ratios bounded;
  absolute scales would chain off m_t retained)
- Full non-perturbative proof of the 5/6 exponent
- Up-type scalar amplitude law (which of the shortlist candidates is correct)
- Generation-stratified Yukawa Ward identities (analog of y_t Ward for u, d,
  s, c, b)

## 3. Derivation targets

### 3A. Down-type 5/6 exponent NP proof

**Target:** prove the V_cb = (m_s/m_b)^(5/6) bridge non-perturbatively at the
lattice scale, beyond perturbative QCD shifts.

**Existing scaffolding:**
- C_F − T_F = 4/3 − 1/2 = 5/6 (exact group-theory rationals)
- Lattice anomalous dimension support (L=4-12 noisy; needs L≥16)
- Taste-staircase support landed 2026-04-25

**Approachability:** Tier B-C. Substantial NP-QCD work but the structural
target is sharp.

### 3B. Up-type amplitude scalar law derivation

**Target:** identify which of the shortlist candidates (or a new clean form)
is the correct up-type amplitude scalar law that closes m_u/m_c retention.

**Existing scaffolding:**
- The candidate shortlist itself
- The widened native-affine-support no-go (rules out one-step affine-projector
  laws)
- Up-amplitude candidate scan + restricted native-expression scan

**Approachability:** Tier B (4–8 weeks). Small candidate set; structural
grammar well-mapped.

### 3C. Generation-stratified Yukawa Ward identities

**Target:** derive y_d/y_t, y_s/y_t, y_b/y_t, y_u/y_t, y_c/y_t as Ward-identity
ratios analogous to the retained y_t(M_Pl)/g_s(M_Pl) = 1/√6.

**Existing scaffolding:**
- The y_t Ward derivation (template)
- The hw=1 triplet structure with 3 generations explicitly
- Generation-color and EW A4 bridges (recent landing 4cc6d474)

**Approachability:** Tier B. Extends existing retained Ward content.

### 3D. Absolute quark-mass scales via m_t retained

**Target:** chain absolute mass scales for all 5 down-type and up-type quarks
off the retained m_t = 172.57 GeV.

**What the framework needs:** generation-stratified Ward (3C) + retained mass
ratios (3A + 3B) → absolute masses by simple chain.

**Approachability:** Tier A-B. Automatic once 3A, 3B, 3C land.

### 3E. CKM-mass cross-validation

**Target:** verify the now-retained quark masses correctly reproduce the
already-retained CKM atlas/axiom structural identities.

**Approachability:** Tier A. Internal consistency check after 3A-3D.

## 4. Existing scaffolding to build on

- [QUARK_MASS_RATIO_NOTE_2026-04-18.md](../../QUARK_MASS_RATIO_NOTE_2026-04-18.md)
- [QUARK_MASS_RATIO_FULL_SOLVE_NOTE_2026-04-18.md](../../QUARK_MASS_RATIO_FULL_SOLVE_NOTE_2026-04-18.md)
- [QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md](../../QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md)
- [DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md](../../DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md)
- [YT_WARD_IDENTITY_DERIVATION_THEOREM.md](../../YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
- The full retained CKM atlas/axiom package
- Generation-color and EW A4 bridges on current `main`
- α_LM geometric-mean identity

## 5. Recommended attack approach

**Phase 1 (parallel):**

1. **3B: Up-type amplitude law.** Small candidate shortlist; weeks of focused
   work could land. Tier B.
2. **3C: Generation-stratified Yukawa Ward.** Template (y_t Ward) is retained;
   lift to other generations. Tier B.

**Phase 2 (after Phase 1):**

3. **3A: Down-type 5/6 NP proof.** Substantial; benefits from the taste-staircase
   support already landed. Tier B-C.
4. **3D: Absolute scales via m_t.** Automatic after Phase 1. Tier A.

**Phase 3:**

5. **3E: CKM-mass cross-validation.** Internal consistency check. Tier A.

## 6. Out of scope / will not claim

- This lane does NOT propose to derive m_t separately (already retained).
- This lane does NOT propose to address heavy-quark expansions (HQET, NRQCD)
  in initial scope.
- This lane does NOT address quark mass running at all scales — focus is
  retained values at canonical lattice / threshold scales.

## 7. Cross-references

- Depends on: Koide closure (for the Q-side of the cross-sector V_cb bridge,
  which provides additional constraint on quark masses via Q_ℓ · α_s² = 4|V_cb|²)
- Enables: Lane 1 (hadron masses depend on quark masses; Lane 1 now
  identifies combined `m_u + m_d` retention as the shortest quark-mass
  dependency for the GMOR pion route)
- Enables: Lane 4 (neutrino sector consistency checks via flavor-universal
  Yukawa structure)
- Cross-validates: existing CKM atlas/axiom package (CKM was closed without
  quark inputs; closing quark masses retention provides independent verification)

## 8. Reviewer questions

1. Should up-type amplitude law (3B) be the entry point, or down-type 5/6
   proof (3A)?
2. Is the generation-stratified Yukawa Ward identity (3C) approach the right
   route, or is there a cleaner taste-staircase route?
3. What precision target should "retained" mean for quark mass ratios —
   sub-percent? PDG precision?
4. Should the 5/6 NP proof be considered a single theorem target or a
   research program with multiple sub-theorems?
