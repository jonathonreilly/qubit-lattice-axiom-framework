# LEE-1 pre-registration

Written 2026-10-18T21:16Z, before any family member is evaluated. The
readings are the ones fixed in ../TESTS.md (LEE-1); nothing here changes them.

## What was read before writing this

- docs/MINIMAL_AXIOMS_2026-06-29.md (full), PRIMITIVE_REGISTRY_CHECK.md,
  SCALE_REFERENCE_PRIMITIVE_NOTE.md, derivation_obligations.json (three
  obligations, none on the hierarchy).
- origin/main docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md in full,
  including the 2026-09-30 corrigendum, the 2026-10-04 reproduction boundary,
  the F1-F4 anti-tuning certificates.
- origin/main greps: no HIERARCHY_PLAQUETTE_* file exists; matter-inclusive
  plaquette numbers on main live only in the honest-status corrigendum
  (spot check + campaign HMC). Numerology guards exist (B4 attachment
  enumeration, DELTA0 probes) but are qualitative. No quantitative
  look-elsewhere count of the v formula was found on main.

**Known before registration (not new):** the input values for part (ii) and
their v-shifts in the corrigendum (1 taste -4.1 %, 2 tastes -4.7..-7.6 %,
4 tastes -13 %, point estimate 0.59369 -> -0.195 %). Part (i) has not been
evaluated for any member.

## Fixed constants

- M_Pl (B2) = 1.2209e19 GeV; reduced M_Pl = M_Pl / sqrt(8 pi).
- v_obs = 246.22 GeV (the honest-status note's comparator).
- <P> = 0.5934 (B1), u0 = <P>^(1/4), alpha_bare = 1/(4 pi),
  alpha_LM = alpha_bare/u0, alpha_s(v) = alpha_bare/u0^2 (main's canonical
  surface, CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE).
- Match size of the candidate: delta0 = v_cand/v_obs - 1 (about +2.55e-4,
  from the note). "10x its own size" means a shift of 10*|delta0|.

## Part (i): the family (decision family F0)

Members are M_Pl * p * c^k.

- **r-set R (17 values).** Small rationals p/q with p, q in {1,2,3,4} in
  lowest terms: {1, 2, 3, 4, 1/2, 1/3, 1/4, 2/3, 3/2, 3/4, 4/3}; eta/zeta
  ratios of the 7/8 kind, 1 - 2^(1-s) for s = 2..6: {1/2, 3/4, 7/8, 15/16,
  31/32}; and their inverses {2, 4/3, 8/7, 16/15, 32/31}. Union = 17 values.
- **Prefactors p = r^(1/n)**, n in {1, 2, 4}, deduplicated by value
  (relative tolerance 1e-12).
- **c-set C (10 values).** Base: alpha_bare, alpha_LM, alpha_s(v), u0, <P>.
  Reduced variants: alpha/(4 pi) for the three couplings (the loop-reduced
  form g^2/(16 pi^2); main's canonical surface lists alpha_LM/(4 pi)); and
  1 - u0, 1 - <P> for the two lattice numbers (their small-deviation forms).
- **k = 1..32.**
- Members are counted as (p, c, k) triples. Distinct-value counts are also
  reported (P^k = u0^(4k) collisions).

Robustness families (reported, not used for the reading):
- F_core: C = the 5 base values only.
- F_uniform: C = each of the 5 base values times {1, 1/pi, 1/(4 pi)} (15).
- F0x2: F0 with both M_Pl conventions (doubles the members).

## Part (i) statistics

1. **N_hit(0.03 %)** = members with |m/v_obs - 1| <= 3e-4; **N_hit(1 %)** with
   1e-2. **p_hit = N_hit / N** (the registered statistic).
2. **p_global (supplementary, the look-elsewhere probability).** For a target
   v' drawn log-uniformly from [v_obs/10, 10 v_obs], the probability that the
   family has at least one member within the window of v'. Computed two ways:
   exact union of intervals in ln v', and Monte Carlo with 2e5 random targets.
   Reported at windows 3e-4, 1e-2 and |delta0|. Also the expected number of
   members per random target.
3. List every hit and the rank of the candidate among them.

**Property stated before the run (to be checked by the script).** In one
column (fixed p, c) the members' ln values are spaced by |ln c|. The smallest
|ln c| in every family above is |ln u0| ~ 0.13, larger than the full 1 %
window width 2 ln(1.01) ~ 0.02. So a column holds at most one hit, N_hit <=
N/32, and **p_hit <= 1/32 < 0.05 for every target**. The first clause of
LEE-COINCIDENCE cannot fire for this family shape, and p_hit <= 1e-3 holds
whenever N_hit <= N/1000. This is why p_global is also reported: p_hit is a
member fraction, not a chance-coincidence probability.

## Part (ii): inputs

Recompute v_cand = M_Pl (7/8)^(1/4) (alpha_bare/<P>^(1/4))^16 directly and via
dln v/dln<P> = -4 (both shown). Inputs:

| id | input | source on main | class |
|---|---|---|---|
| P0 | 0.5934 +/- 5e-5 (licence half-step) | PLAQUETTE_SELF_CONSISTENCY, honest-status B1 | baseline |
| P1 | 0.5934 +/- 0.0006 | YT_ZERO_IMPORT_CHAIN_NOTE table | EJ (stated uncertainty) |
| P2 | 0.59369(2) | April production ensembles (corrigendum (2)) | EJ |
| P3 | 0.59372(4) | wall-campaign heatbath, code outside repo | reported only |
| M1 | 0.5934 + 0.0062(2), 1 taste | corrigendum (1), reweighted 4^4 | EJ |
| M2 | 0.5934 + 0.0119(11) / + 0.0072(25), 2 tastes | corrigendum (1) | EJ (main's taste census reads 2 tastes) |
| M4 | 0.5934 + 0.0212(11) HMC / +0.026 linear, 4 tastes | corrigendum (1) | EJ (one unrooted staggered field) |
| M8, M16 | 193, 163 GeV as reported | corrigendum (1) | reported only (not supported by main's counts) |
| Q | 0.5973(6) on 4^4 | CONFINEMENT_STRING_TENSION_NOTE | reported only (finite volume) |
| G-full | M_Pl = 1.2209e19 | B2 | baseline |
| G-red | M_Pl/sqrt(8 pi) | convention | see rule below |

EJ = equally justified, counted for the reading. Matter-inclusive values count
as EJ because the formula's own determinant carries fermion modes and main's
corrigendum calls the pure-gauge measure an unlabelled premise.

**M_Pl rule.** The approved scale-reference primitive declares a^-1 = M_Pl and
states that it supplies no dimensionless content and leaves a/l_P = 1
underived. Primary rule: the reduced convention is NOT counted as EJ for the
robustness clause (the primitive fixes the ruler), but IS counted as a trial
factor (F0x2) in p_global. The reading under the alternative rule is also
stated.

## Reading map (fixed in TESTS.md)

- COINCIDENCE if p_hit(0.03 %) >= 0.05, or any EJ input shifts v_cand by more
  than 10 |delta0|.
- SIGNIFICANT if p_hit(0.03 %) <= 1e-3 and every EJ input keeps v_cand within
  1 % of v_obs.
- OPEN otherwise.
EJ inputs are applied at their central values; their stated 1-sigma ranges
are reported beside them.

## Limits stated in advance

- The family is one shape (prefactor x power). Other shapes (sums,
  exponentials, other exponents tied to 2^d) are forking paths not counted
  here, so p_global is a lower bound on the real look-elsewhere freedom.
- The matter-inclusive shifts are small-lattice, reweighted or HMC numbers
  from main; they are not re-run here.
