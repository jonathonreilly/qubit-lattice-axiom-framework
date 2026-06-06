# P2 is a Euclidean-vs-native-Lorentzian fork, not a "derive d=4" gap

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta scoping / reframing.
**Status authority:** independent audit lane only. Bounded-support reframing;
sets no audit status, proposes no axiom/import, retires/promotes no row.
**Runner:** `scripts/p2_euclidean_vs_lorentzian_fork_2026_06_05.py` (SUMMARY: PASS=19 FAIL=0).
**Cached log:** `logs/runner-cache/p2_euclidean_vs_lorentzian_fork_2026_06_05.txt`
**Companion (the decisive computation):** `P2_NATIVE_LORENTZIAN_MAGNITUDE_TEST_2026-06-05`
(runner 46/46) — **source result: NATIVE-GIVES-DIFFERENT.**

## Statement

The framework's magnitude exponents — the hierarchy `v = M_Pl (7/8)^{1/4} alpha_LM^16`
(matches v to <1% here; ~0.03% in the framework's precise chain) and the Yukawa
suppression `256 = (dim_C M_2)^4` — load-bear on the **staggered Euclidean Z^4
taste count** `2^{d/2} = 4`, which requires **even d = 4**. The framework is
**d = 3+1** (Lorentzian, with an *emergent* time). The previously-named open gate
"primitive P2 / derive d=4" is therefore **not a gap to close** but a **fork**:

- **Euclidean branch (P2):** Wick-rotate `Z^3 + emergent time -> Z^4` Euclidean,
  giving the integer taste `2^{4/2}=4`, hence the `16`, hence the v-match.
- **Native d=3+1 branch:** compute the spectrum in the real-time structure
  (`H^2 = (k^2+m^2) I`, gapped) — which carries **no taste-16 at all**; in
  genuine d=3 the taste count is the non-integer `2^{3/2} = 2.83`.

These two computations produce **structurally different objects** (runner,
PASS=19). P2 is the choice between them — and the companion decisive test
(below) **resolves it: the magnitude lives in the Euclidean branch.**

## Assumption stack (foundational -> specific; weak joints flagged)

| label | Assumption | Tag | If wrong |
|---|---|---|---|
| path-integral mass readout | Masses come from a *path integral* at all | **implicit** | masses are spectral / record-structural; no determinant, no taste, **the 16 never arises** -- P2 dissolves |
| Euclidean determinant branch | The path integral must be *Euclidean* (hence Wick rotation) | implicit | a real-time computation is native; the Euclidean choice is convenience, not necessity |
| symmetric Euclidean-time promotion | *Emergent* time Wick-rotates to a *symmetric 4th Euclidean dimension* (Z^3 -> Z^4) | **implicit (crux)** | corner count stays `2^3=8`, taste stays `2^{3/2}=2.83`; the integer 16/256 are not native |
| isotropic rotated lattice | The rotated lattice is *isotropic* (time = space) | implicit | anisotropic Z^4 breaks the `2^4` symmetry; the exponent fragments |
| staggered taste-count identification | Staggered taste `= 2^{d/2}`, and 16/256 *are* this count | explicit (standard) | well-supported (verified the 16 is the determinant power); this is what makes P2 load-bearing |
| OS reconstruction authority | Osterwalder-Schrader holds (Euclidean -> physical Lorentzian masses) | implicit | the 16/256 are **regulator artifacts**, not physical exponents |

The load sits on **path-integral mass readout**, **symmetric Euclidean-time
promotion**, and **OS reconstruction authority** — all implicit, all assuming
Euclidean-determinant machinery is valid for an *emergent-time* system. The
staggered taste-count identification (the joint that makes P2 real) is solid;
the foundations under it are not.

## Delete the requirement

d=4 appears **nowhere** in the axioms (Z^3 spatial, time emergent = 3+1). It
enters *only* through the choice to compute a Euclidean determinant, which forces
a 4th symmetric dimension to make the taste integer. **Delete that choice and the
"derive d=4" requirement vanishes** — there is no Z^4. The Euclidean computation
is borrowed machinery (standard lattice QCD assumes a *fundamental* Euclidean
time). The honest counter: the Euclidean 16 hits v to ~0.03%, so the deletion
*owes* a native-Lorentzian reproduction of that number — which converts P2 from a
gap into a **decidable test**.

## Literature (and the wrong-escape check)

- **Causal Dynamical Triangulations (Ambjorn-Loll).** The decisive precedent: in
  emergent-spacetime gravity, **Lorentzian != Euclidean.** Euclidean DT gives
  degenerate geometries with no 4D continuum limit; imposing the *Lorentzian
  causal* structure (a distinguished time with an arrow — the framework's exact
  situation) is what yields extended 4D spacetime. The Wick rotation genuinely
  **fails** for emergent time. (Comparator only; not adopted.)
- **Osterwalder-Schrader.** Euclidean->Lorentzian reconstruction needs reflection
  positivity, a theorem for *fundamental*-time theories; staggered fermions are a
  known stress case. OS reconstruction authority is assumed, not shown.
- **Staggered tastes** are `2^{d/2}` *for even d*; odd d is genuinely pathological
  (non-integer). The literature confirms the integer taste needs even d.
- **Wrong-escape-via-citation:** "Wick rotation is standard, so P2 is fine" cites
  the *fundamental*-time theorem to license an *emergent*-time rotation -- a
  different category, and CDT is the published counterexample where it fails.

## Math (the fork, concretely)

Staggered BZ has `2^d` corners; `eps(x)=(-1)^{sum x_mu}` reduces to `2^{d/2}`
tastes. d=4: 16 corners -> 4 tastes -> the 16, and `256 = dim_C(M_2)^4`. d=3:
`2^{3/2}=2.83`, non-integer -- no clean taste. The emergent-time chiral 2-fold
(`gamma_5`) is real but supplies a **factor 2** (two chiral blocks), not the
**taste factor 4**, and labels eigenvalues rather than adding determinant factors
-- so it provably **cannot** manufacture the 16 (runner). The native Lorentzian
`H^2 = (k^2+m^2) I` is gapped with **no 16-structure**. The two branches are
structurally distinct objects.

## The reframe and the decisive test

The right question is **not** "derive d=4 to justify the 16." It is:

> Is the framework's mass computation **Euclidean** (Z^4, manufactures 16, matches
> v -- but rests on an emergent-time Wick rotation the lit says fails) or
> **native-Lorentzian/records** (d=3+1 exact, no 16 to derive, but must reproduce
> v ~ 0.03% spectrally)?

This is **decidable**, far more tractable than "derive a dimension." The test:
compute the EW/lepton magnitude in the native d=3+1 spectral (or records)
structure and check whether the v-match survives **without** the Euclidean taste.

- Survives -> the 16 was a re-expression, **P2 dissolves**, the magnitude is
  native to d=3+1.
- Differs -> the 16 is **Euclidean-specific**; the v-match must be flagged as
  **regulator-dependent**, not a clean prediction.
- Underdetermined -> the Euclidean Z^4 is genuinely load-bearing -> P2 is real and
  the framework relies on a Wick rotation it cannot justify for emergent time.

## Source result: DIFFERS — the v-match is Euclidean-regulator-specific

The companion `P2_NATIVE_LORENTZIAN_MAGNITUDE_TEST_2026-06-05` (runner 46/46)
ran the native real-time Dirac Hamiltonian `H = alpha.k + beta m` on Z^3
(single emergent clock = the continuous generator `U(t)=exp(-itH)`, *not* a 4th
symmetric lattice momentum) and returned **NATIVE-GIVES-DIFFERENT.** The exact
discriminator:

> **16 = 8 (spatial Z^3 BZ corners) x 2 (Euclidean temporal lattice-momentum
> corner `k_4 in {0, pi}`).**

The extra factor of 2 — and therefore the whole exponent 16 — is the *second
temporal momentum corner*, which exists only once time is promoted to a discrete
lattice direction. The framework's **continuous** emergent time has no such corner:
the native count stays `2^3 = 8`, the native magnitude carries `alpha_LM^8`, and
`v_native ~ M_Pl (7/8)^{1/4} alpha_LM^8 ~ 5.4e10 GeV` overshoots the EW scale by
~8.3 decades (runner). The chiral `gamma_5` two-fold grades the spinor (corner-rank
stays 3) and provably cannot supply the temporal corner.

**Honest consequence (states plainly, claims nothing beyond it).** The beautiful
`v` match (~0.0255% in the precise chain) is **not a clean native d=3+1
prediction**; it lives in the Euclidean Z^4 branch and is **regulator-dependent**.
Worse for the Euclidean branch: the P2 Wick sign-closure legitimizes the
framework's `Cl(3,1)` Lorentzian signature **precisely by analytically continuing
the discrete `L_t` away** — which dissolves the very temporal corner the 16 reads
off. So the framework **cannot** simultaneously (a) have a continuous emergent time
and (b) keep the Euclidean 16 as a native prediction. P2 is **real and
load-bearing** for the magnitude, not a dissolvable bookkeeping gap.

## The next path this opens (not a closed enumeration)

The verdict turns a vague "derive d=4" gap into a **sharp, named physical
question**: *is there a native d=3+1 structure that supplies a genuine temporal
2-fold* — the missing factor of 2 — *without a Euclidean lattice time?* The
framework already carries a candidate it has not been tested against: the **Record
axiom's K/CPT orbit**. A durable record and its CPT/time-reverse conjugate form a
2-element orbit; if the magnitude readout counts that orbit, the "second temporal
corner" could be **native record structure rather than a Euclidean artifact**,
restoring `alpha_LM^16` on d=3+1 terms. This is a *direction*, not a result — the
honest current state is: the v-match is regulator-dependent until a native
temporal 2-fold is exhibited and shown to reproduce it.

## Scope

No axiom, import, or comparator adopted. CDT/OS are cited as literature context
only. Observed v is a labelled comparison, never a derivation input. The
contribution is twofold: (1) the **reframe** — a "deep open gate (derive d=4)" is
a **decidable Euclidean-vs-Lorentzian fork**; and (2) the **source result** —
the companion decisive test returns DIFFERS, **locating** the v-match in the
Euclidean regulator branch and flagging it as regulator-dependent. This does
**not** retract the v formula or demote any ledger row; it identifies *where* the
match lives and names the precise native structure (a temporal 2-fold) that would
be needed to make it a clean d=3+1 prediction. Status remains with the independent
audit lane.

## No-Go Discipline Gate (N1-N8)

**Status:** PASS for the scoped fork/result only. This note rules out the tested
native real-time Hamiltonian/taste-count route as reproducing the Euclidean 16;
it does not rule out future native temporal two-fold routes.

| Gate | Result |
|---|---|
| N1 alternative routes | Checked Euclidean determinant, native real-time Hamiltonian, spatial BZ corner count, chiral `gamma_5` two-fold, and future Record `K`/CPT orbit routes. Only the tested native Hamiltonian/taste-count route differs; the Record-orbit route remains open. |
| N2 wall independence | Path-integral mass readout, symmetric Euclidean-time promotion, OS reconstruction authority, and native temporal two-fold supply are independent residuals. |
| N3 hidden-wall scan | Euclidean, OS, CDT, and staggered-taste language is marked as context or explicit assumption; no readout context, probability, or dynamics is imported from Record. |
| N4 residual matching | The residual matched here is the missing temporal lattice-momentum corner in the native computation, not all possible native d=3+1 magnitude mechanisms. |
| N5 rhetoric audit | Negative language is scoped to taste-count/determinant structure and the tested native Hamiltonian branch, not to arbitrary spectral or record readouts. |
| N6 partial-closure scan | A native temporal two-fold supplied by a separate theorem could retire the Euclidean import without a new axiom; the note names that path rather than declaring it impossible. |
| N7 steelman | A reviewer can argue that Record `K`/CPT orbit counting or another native two-fold could reproduce the missing factor; this note explicitly leaves that as the next target. |
| N8 cross-cycle echo | Prior P2 notes separated Euclidean regulator support from native d=3+1 support; this note preserves that split and does not promote either branch to audit status. |
