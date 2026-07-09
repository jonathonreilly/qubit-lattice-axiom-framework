# Handoff — wilson-identity-source-dynamics

Campaign 2026-07-08. Owner: Jon. Supervisor: Claude (Fable), workhorse
split with codex workers. Ran the two frontier items named by
mass-identity-and-source: the Wilson-kernel identity test and the
source-field dynamics block.

CAMPAIGN VERDICT: one clean positive (the source-field law block:
classification + forced subtraction + the charge-sector exhibit), one
machinery positive (Wilson engine validated), and one consolidated
disciplined negative (the identity test is closed for the ED
instrument class across BOTH kernels, with the volume wall demonstrated
directly and the tensor-network escape named as the route). The axioms
remain unindicted; no axiom trigger fired at any point.

## PRs in review order (each verifiable by its stated runner command)

1. #5070 block01 (stacked on #5069) — Wilson ED engine + validation.
   `python3 scripts/gauged_wilson_schwinger_ed_engine_2026_07_08.py`
   -> TOTAL PASS (~100s).
2. #5071 block02 (stacked) — static field law classification + forced
   background subtraction + charge-sector Poisson exhibit.
   `python3 scripts/source_field_static_law_classification_2026_07_08.py`
   -> TOTAL LAW-CLASSIFIED (~1s).
3. #5072 block03 (stacked) — Wilson two-band identity test: bounded
   methods negative with the N = 10 volume refutation.
   `python3 scripts/wilson_two_band_identity_own_frame_2026_07_08.py`
   -> TOTAL FAIL TAGGING-FAILED (~31 min; the pre-committed FAIL line
   is the deliverable).

Nothing is landed; the review lane owns landing.

## What the campaign showed (plain language)

- The gravity-field block: within the minimal lawful class of static
  field equations for a potential pulled by energy, Newton's form is
  the unique member with the shift symmetry, and on a finite universe
  a field pulled by TOTAL energy is mathematically inconsistent — it
  must be pulled by energy DIFFERENCES from the average. That
  subtraction is forced by pure solvability, and it is the same shape
  as the cosmological subtraction in real gravity. The framework's own
  electric sector was measured doing exactly all of this for charge:
  external charges create one unit of field between them, compensated
  outside, with the vacuum's screening switching on at strong coupling
  right where theory expects. What generates the analogous field for
  ENERGY remains the open problem — now sharply posed, with candidate
  shapes named.
- The identity test: the Wilson comparator fixed everything it was
  built to fix (both particles rest at zero momentum; the staggered
  zone problem is confirmed as an artifact of that construction), and
  the test got further than ever — four fully valid points with
  identity ratios within 4-25% of the perfect value. Then the
  purpose-built volume check caught it: the best point's ratio moved
  from 1.04 to 2.21 when the ring grew from 8 to 10 sites. Those
  near-perfect numbers were finite-size accidents. Conclusion, now
  backed by two kernels and seven runs: exact diagonalization cannot
  reach the volumes this measurement needs. The right tool is a
  tensor-network (DMRG) engine, where rings of 40-100 sites are
  routine — named as the escape, and a natural future campaign since
  everything else (tags, own-frame protocol, validity discipline)
  ports over unchanged.

## Post-campaign frontier

1. Energy-sector field derivation — THE gravity milestone, unchanged,
   now sharply posed by the source-law note (candidate shapes: an
   emergent collective mode of the record/link sector sourced by
   energy contrasts; a second forced gauge structure from the
   dynamics-form theorem applied to the energy current).
2. DMRG/tensor-network engine for the d=1 comparators — unlocks the
   identity test at converged volumes; the full measurement protocol
   is already built and documented.
3. Exhaustive gauged-sector conserved-density classification
   (pool-restricted leg upgrade) and the transfer-surface version.
4. d=3 lifts; unequal-mass composites; Noether current on larger
   operator classes.

## Resume

Read STATE.yaml. Campaign closed; PRs #5070-#5072 await the review
lane atop the #5061-#5069 stack. Follow-ups start fresh packs.
