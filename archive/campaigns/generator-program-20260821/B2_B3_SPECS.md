# B2 / B3 Spec Skeletons (frozen 2026-08-21; a fresh session executes)

## B2 (block 172) — the redesigned census

Prerequisite: B1 declared record alphabet A and class map
{Pi_a}; B1's weight-profile/frequency-profile table.

1. CONTROLS FIRST: (a) the uniform-profile check — if the induced
   profile on the chosen fixture is uniform, STOP and move to a
   non-uniform fixture (counting = weighting there; zero collisions
   would be an artifact); (b) the half-support scope as the
   trivially-colliding control (memo §5).
2. THE REFINEMENT (GLEASON-SHAPED) CENSUS: for refinement families
   of a fixed record (coarse-grainings A -> A' with |A| >= 3),
   test ADDITIVITY of the weight across refinements, exactly. This
   carries theorem-power; the profile-collision census alone does
   not (zero-collision is not basis-robust — the enlarged-basis
   precedent).
3. THE PROFILE-COLLISION CENSUS (the memo's original): distinct
   weight profiles vs identical record-frequency profiles, exact
   rationals, full-quotient scope. Exit on first collision;
   reproduce at one more fixture size; the collision IS the memo
   to the owner's bar (do not widen scope before the bar).
4. THE EQUIVARIANCE FIXED-POINT (existence, not uniqueness): is
   the normalized slice-Gram weight a stationary measure of the
   record-extension map, and unique among candidates in the
   displayed class? Attacks what the census cannot.
5. The p != 1 family dies to one exact coarse-graining triple
   (sign of (w1+w2)^p - w1^p - w2^p); pin |A| >= 3 in advance.
   Count-proportional dies by blindness transfer (its profile is
   carrier-blind; if the candidate's profile moves between
   sigma = 1/5 and 3/5, no counting run is needed).

Supervised block (owner-bar adjacent). Full verification chain:
disjoint checker spec'd to refute, 15-mutation sweep, N5 fence.

## B3 (block 173) — the R1-R3 joint test

The c679 Record/Born harness deformed through the gravity lane's
positive region. Pins: ../hygiene-20260821/GENERATOR_PROGRAM_PINS.md
(origin/main 38109c451a; merge commit 946617e7c4; note + runner +
independent-check blobs recorded). Predictions (panel 4, standing):
R1 pass / R2 pass / R3 Gram-fails-no-verdict-flip; falsifier = any
verdict flip. Merge-acceptance criteria carry the anti-shim
standard: any derived inter-record channel must be shear-dependent
or it is physics-empty by our own theorem. Codex-suitable
(bounded-read: the two harness scripts + the boundary note + B1's
findings file ONLY); pool unlocks Aug 22 12:35.

## Landing discipline (both)

Branch stacked per the standing chain (B1 lands first as block 171
on #7146's branch); five-pin refresh; N5-prefix fence adoption
(single-line literal guard); baseline exit 0; --deep; sweep 15/15
via mutation_sweep.py; SWEEP-GATED + MAIN-GATED commit; PR stacked.
The landing session must re-freeze pins itself — trust nothing
from this session's memory except these files.

## B2 amendments from the block-171 checker (mandatory)

- Read the CORRECTED profile table b171_profile_table_v2.py (in
  THIS directory, copied from the draft worker's output; the
  session scratchpad does not survive) — the original NULL_FIXTURES
  entry
  is REFUTED (checker C6/L2: x-homogeneity gives x-period-2, not
  uniformity; W5/W6/W7 non-uniform on both claimed null carriers).
  The uniform-profile control CANNOT be skipped.
- The site-alphabet profile-collision census is ANSWERED: collisions
  exist (C5, twice-confirmed; 10/16 frequency profiles, 6 doubled).
  B2 = the refinement (Gleason-shaped) census + the equivariance
  fixed-point; the collision memo for the owner covers the site
  alphabet.
- Record alphabet count: L_x(T_phys-2) (16 at 12x4, 8 at 8x4).
- The joint-weight design fork (checker C4): chain-rule form is
  slot-order-dependent for same-slice records; the one-shot Gibbs
  joint is order-independent but breaks per-slot factorization.
  B2 must carry BOTH forms or the owner's declared choice.
