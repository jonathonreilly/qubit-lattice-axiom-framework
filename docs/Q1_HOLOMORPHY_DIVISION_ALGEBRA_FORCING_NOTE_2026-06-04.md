---
claim_id: q1_holomorphy_division_algebra_forcing_note_2026-06-04
claim_type_author_hint: meta
---

# Q1 Holomorphy: Does the Frobenius-Schur Division-Algebra Reading FORCE det_C?

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (reading-choice adjudication / route-pruning support)
**Claim type:** meta
**Status:** source-only adjudication. This note approves no axiom, import,
primitive, or verdict. It records a tested mathematical adjudication of one
candidate forcing mechanism for the open `det_C`-vs-`det_R` polarization choice
on the `C_3` generation doublet.
**Primary runner:**
[`scripts/q1_holomorphy_division_algebra_forcing_2026_06_04.py`](../scripts/q1_holomorphy_division_algebra_forcing_2026_06_04.py)
(SCORECARD PASS=52 FAIL=0, exact sympy + numpy).
**Cached log:**
[`logs/runner-cache/q1_holomorphy_division_algebra_forcing_2026_06_04.txt`](../logs/runner-cache/q1_holomorphy_division_algebra_forcing_2026_06_04.txt)

## Question

The charged-lepton Koide lane reduces (retained
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md))
to one binary on the generation algebra `R[Z_3] = R (+) C`: is the doublet
coefficient `b` **one complex slot** (`det_C` -> `r = 1/2` -> `Q = 2/3`) or **two
real slots** (`det_R` -> `r = 1` -> `Q = 1`)? The companion
[`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
isolates this to the **polarization** column (holomorphic vs real), independent
of Gaussian-vs-Berezin statistics, and leaves the polarization SELECTOR open.

This note tests one named candidate selector:

> **Q1 angle A.** Does reading each real Wedderburn block by its OWN division
> algebra (its Frobenius-Schur class) FORCE the holomorphic (`det_C`) readout on
> the complex doublet block, hence `r = 1/2`? And does the Record axiom's "real"
> adjective ("a record registers which REAL classical alternative is realized")
> ENTAIL that holomorphic reading?

The structures here (the `(scale a, ratio |b|, phase delta)` circulant
decomposition, the `Q in [1/3, 1]` range) are Koide & Nishiura's own
`Z_3`-symmetric parametrization (arXiv:1301.4143); the framework contribution is
the axioms-up carrier derivation and this adjudication of the polarization
selector. No PDG values, fits, or comparators are used; `2/3` appears only as
the target of the lever, not as input.

## The mathematics established (verified)

**Wedderburn + Frobenius-Schur.** Over `R`, `R[Z_3] = R (+) C`. The three complex
characters of `Z_3` have Frobenius-Schur indicators `nu = (1/|G|) sum_g chi(g^2)`
equal to `+1` (trivial, type **real**, division algebra `R`), `0`, `0` (the two
faithful characters, type **complex**). The two complex characters are
conjugate, so they fuse into **one real-irreducible doublet block** whose
endomorphism division algebra is `C`. Verified: `nu(chi_0)=1`, `nu(chi_1)=nu(chi_2)=0`;
the real projectors split `1 = P_s + P_d` with `tr P_s = 1`, `tr P_d = 2`.

**The doublet block genuinely IS `C`.** The operator `J = -i(e_1 - e_2)` (built
from the central idempotents) is **real**, supported on the doublet, satisfies
`J^2 = -P_d`, and **commutes with the `Z_3` action** — i.e. `J` lies in the
centralizer `End_{R[Z_3]}(doublet)`, which has real dimension 2 (`span_R{P_d, J}
~= C`). So `J` is an **intrinsic** element of the algebra's own structure, NOT an
externally imported operator. (This is the strongest version of the pro-`det_C`
case, and it is real.)

**The two readouts.** `det_C` treats the doublet as one complex slot
(`-> r = 1/2 -> Q = 2/3`); `det_R` treats it as two real slots (`-> r = 1 ->
Q = 1`). Connected to the signed-vs-singular dichotomy
([`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md)):
the signed/Brannen readout (`Q = 2/3` `theta`-independently at `r = 1/2`) sits on
the `det_C`-compatible side; the singular-value readout (`theta`-dependent,
`Q < 2/3`) on the `det_R` side. Both give identical masses `m_k = lambda_k^2`;
they differ only in the `sqrt(m)` sign.

## Verdict on the forcing: **NATURAL-NOT-FORCED**

Reading by native division algebra is a *natural* (functorial) reading, but it is
**not the forced one**. Three independent facts (all verified) establish this:

1. **Restriction of scalars is an equally-standard functor.** `C` as an
   `R`-algebra is genuinely 2-dimensional over `R`; `Res^C_R` is a textbook
   functor. Wedderburn's theorem says the block is *isomorphic to* `End_D(V)`; it
   is **silent on whether a measure / determinant on the block is taken over `D`
   or over `R`.** No representation-theoretic theorem privileges the `D`-module
   structure over the underlying real vector space for the purpose of a
   determinant.

2. **`det_R = |det_C|^2` — both are legitimate and DISTINCT.** For a `C`-linear
   (`J`-commuting) operator on the doublet, the real determinant equals the
   modulus-squared of the complex determinant (verified, max deviation `1e-14`
   over 500 random `C`-linear operators). They are genuinely different
   functionals answering different questions ("real volume scaling" vs "complex
   volume scaling"); `det_C` is **not** a forgetful artifact of `det_R` nor vice
   versa. Choosing `det_C` is choosing **which volume to measure** — a measure
   choice, set by the physics/action, not by the algebra.

3. **Possessing `J` does not force complex-dimensional counting.** A real
   2-space *equipped with* a chosen complex structure `J` is still a real
   2-space; `J` is extra **usable** data, not a constraint forcing a quotient.
   The same doublet supports BOTH a faithful real reading (2 modes) and a
   faithful complex reading (1 mode), each internally consistent. Wedderburn
   fixes the block; it does not privilege one module structure for a measure.

This is the same conclusion the retained block-count route reached from the other
side
([`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md),
no_go: the `(1,1)` block-count is permitted-not-forced; the irreducible pin is a
continuous `SO(2)/U(1)_b` doublet-frame quotient), and consistent with the A1
default being `det_R`
([`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`](FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md),
audited_conditional). The division-algebra reading is the *natural* sibling of
those routes, and it does not upgrade "permitted" to "forced."

## Does the Record axiom's "real" adjective ENTAIL holomorphic? **No.**

The decisive part. The candidate resolution of the apparent paradox ("real
sectors, yet holomorphic readout") was: *the real Wedderburn decomposition
CONTAINS a complex block, so reading it faithfully means reading that block
complexly.* That resolution **fails** at the word "real", for a sharp reason:

- A record that registers "which REAL classical alternative is realized" on the
  doublet distinguishes the two real pointer directions `B1, B2`. The record is
  the real-frame projector pair `{|B1><B1|, |B2><B2|}`.
- **`J` rotates `B1 <-> B2`** (verified: `<B2|J|B1> = 1`, `<B1|J|B1> = 0`). A
  record fixing the real frame therefore **does NOT commute with `J`** (`[P_B1,
  J] != 0`, verified): **registering which real alternative BREAKS the complex
  structure.**
- Hence "which REAL alternative is realized" counts the **real** pointer
  directions = 2 = `det_R` = `(1,2)` = `r = 1` = `Q = 1`. The holomorphic reading
  would require the record to count **complex** alternatives (treat `{B1, B2}` as
  one complex ray and gauge out `arg` by `J`) — which is precisely what the word
  "real" excludes.

So both senses of "real" converge on `det_R`: (a) "real Wedderburn blocks read by
their fields" still gives `det_R` once a record fixes the doublet's real frame
(the record breaks `J`); (b) "read everything over `R`" trivially gives `det_R`.
The **only** route to `det_C` is to count *complex* alternatives, contradicting
the "real" adjective. The paradox is resolved in the opposite direction from the
candidate: *faithful* does not mean *field-native*, and a real record picks a
real frame.

## Net standing

- **Forcing verdict:** `det_C`/holomorphic is **NATURAL-NOT-FORCED** by the
  division-algebra (Frobenius-Schur) structure. Restriction-of-scalars (`det_R`)
  is an equally-valid faithful reading; the holomorphic polarization is a
  measure CHOICE (Stance H), independent of any "real records" stance (Stance R).
- **Record-axiom entailment:** the "real" adjective does **not** entail
  holomorphic; if anything it points to `det_R` (`r = 1`, `Q = 1`), because a
  real classical record breaks the doublet complex structure `J`.
- **Consequence for the keystone:** angle A does not close `r = 1/2`. It prunes
  one candidate selector (division-algebra reading) and shows the "real records"
  framing is in *tension* with — not supportive of — the holomorphic readout. The
  open handle remains exactly where the retained block-count note left it: a
  selector that equips the doublet with `J` *as a measure* without contradicting
  the real/record structure (equivalently, a readout functional that factorizes
  through the `SO(2)`/complex-slot quotient). That selector is not supplied by
  the division-algebra structure, and is not supplied by the Record axiom's
  "real" adjective.

## What this does NOT claim

- It does not adopt either polarization, nor any axiom, import, or primitive.
- It does not assert `r = 1/2` (or `Q = 2/3`) is impossible to derive natively;
  it prunes one candidate forcing route and adjudicates one reading-choice.
- It does not establish a charged-lepton mass prediction; `2/3` is comparator-
  level only and `r = 1/2` remains a hypothesis.
- It does not edit generated ledger, queue, or publication-status files.

## Provenance (verified 2026-06-04)

- FS indicators (`+1, 0, 0`), `R (+) C` split, intrinsic real `J` with
  `J^2 = -P_d` in the order-2 commutant: runner Part 1.
- `det_C/det_R -> r = 1/2 / r = 1`, signed-vs-singular connection: runner Part 2
  (cross-ref the retained circulant lever and the signed-vs-singular note).
- `det_R = |det_C|^2`, two-readings consistency, Wedderburn measure-silence:
  runner Part 3 (the NATURAL-NOT-FORCED adjudication).
- `J` rotates the real pointer frame, real record breaks `J`, "real" -> `det_R`:
  runner Part 4 (the Record-adjective adjudication).
- Does not load-bear on `closure_c_staggered_dirac_gate` or
  `koide_phase_aps_eta_parity_route`.
