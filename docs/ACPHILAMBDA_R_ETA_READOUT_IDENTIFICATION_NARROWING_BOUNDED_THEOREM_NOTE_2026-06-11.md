# AC_phi_lambda Sub-Admission (ii) Narrowing: R-eta Decomposes Into a Forced Form Layer Plus One Identification Atom — Bounded Theorem

**Date:** 2026-06-11
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry (`docs/audit/data/tier_a_admissions.json`), ledger, queue, or any
publication-status surface.
**Primary runner:**
[`scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py`](../scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py)
(`TOTAL: PASS=55 FAIL=0`; exact sympy, 3x3 class-A finite-dimensional; cached:
[`logs/runner-cache/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.txt`](../logs/runner-cache/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.txt))

> **What this is.** The live Tier-A registry states AC_phi_lambda
> sub-admission (ii) as "the delta readout identification (R-eta:
> density-read-as-angle; the magnitude 2/9 is fixed-locus arithmetic
> conditional on R-eta, not an admitted number)". This note decomposes that
> R-eta package into (1) a **forced form layer** — derived from the Record
> axiom's registrability constraints plus exact circulant algebra, re-proven
> from scratch in the runner — and (2) a **single named identification atom**
> `A_R-eta` that is the honest admitted residual. The admission is narrowed,
> not retired: `A_R-eta` remains genuinely admitted, and the note quantifies
> exactly how much work it does (one real parameter: the value of `|delta|`
> in the forced fundamental domain). The delta sign, the channel, the
> orientation-freeness, the r-decoupling of the named atom, the forced
> weights, and the magnitude arithmetic are all shown to be derived or exact,
> not admitted.

## r-firewall declaration (read first)

This note is delta-side work only. Nothing here constrains, forces, derives,
or prefers any value of the occupancy modulus `r`. The runner verifies that
the `r`-carrier invariant (`e2`) is delta-blind and is left untouched; `r`
remains the registered dial setting with sectors `r in {0, 1/2, 1}` (the
charged-lepton registered setting `r = 1/2` is a stable setting on that dial,
not a forced value, and is not used here — the sibling chain note's mass
comparator, which uses `r = 1/2`, is **not consumed**).

## 2026-06-13 audit-conditional boundary

This is conditional support for narrowing sub-admission (ii), not a retirement
of that admission. The forced form layer is finite algebra on the supplied
AC_phi_lambda circulant/K-orbit/readout context. The surviving atom
`A_R-eta` (h-class + h-unit, one real parameter) remains admitted, and the
standing physical readout-context premise remains supplied. A consumer may
cite this note only for the form/value split: it cannot cite it as a
framework-native derivation of `|delta| = 2/9`, as a registry edit, or as a
closure of the carrier gate / R2 / `r` lanes.

## 2026-06-20 dependency-status split — formal H(delta) layer

Dependency review on current `main` leaves only one retained-grade one-hop
input available for this narrowing: the K-orbit circulant/sign-flip authority.
The carrier-gate/readout context and the R-eta source remain context notes
rather than retained-grade dependencies, so this source takes the formal split:
prove only the finite `H(delta)` algebra from the retained K-orbit input and
keep the physical readout identification conditional/open.

Current dependency status, reviewed 2026-06-20:

- **K-orbit circulant/sign-flip authority** —
  `TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09`:
  retained-bounded one-hop source for the circulant form and sign flip.
- **carrier gate / readout-context authority** —
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03`: not retained-grade;
  context only here.
- **R-eta source** —
  `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09`:
  not retained-grade; context only here.

Because two of the three named authorities (carrier gate, R-eta source) are
not retained-grade on current `main`, they cannot be used as retained one-hop
authorities. This note therefore restates the bounded algebraic narrowing as an
**explicitly formal H(delta) theorem** — a finite mathematical result about the
Hermitian circulant `H(delta)`, taken as a formal symbolic object — whose one
retained-grade input is the K-orbit
circulant form, now wired as a one-hop markdown-link authority. The *physical*
readout identification (that `H(delta)` is the realized charged-lepton carrier
surface, that the registered angle is the AB/Lefschetz density, and the
identity-radian reading) is explicitly **conditional and open**, routed
through the two context notes, and is **not claimed** here. This
respects the firewall: the readout-import identification is the irreducible
register-not-read price class and is not derived.

## Formal theorem (H(delta) layer)

The following is a **formal** result: it treats `H(delta) = a I + B e^{i delta}
C + B e^{-i delta} C^T` (the circulant form L2 supplied by the one
retained-grade one-hop authority, the Tier-A K-orbit note) as a symbolic object over
`{a, B, delta}` and derives the form/value split by finite exact algebra. No
physical readout identification is used in this layer; the runner sections
S1-S8 are this formal layer verbatim (symbolic sympy, no PDG/fitted/measured
value, no density object in the channel derivation — runner S7).

**Formal claim.** For the symbolic Hermitian circulant `H(delta)`:
(F1) `conj(H(delta)) = H(-delta)`; the sign line `sin(3 delta)` is odd under
the conjugation, so any orbit-constant additive functional of the spectrum is
even in `delta` (S1-S2). (F2) The elementary symmetric functions satisfy
`e1 = 3a`, `e2 = 3a^2 - 3B^2` (both `delta`-blind), `e3 = a^3 - 3aB^2 +
2B^3 cos(3 delta)`, all even in `delta`, with `e3` of period `2 pi/3`; the
registrable delta-content folds to `[0, pi/3]` on the `cos(3 delta)` channel
(S3). (F3) On the determinant-class character `chi_k(z)=exp(i k arg z)`, orbit
constancy forces `k=0` (S5). (F4) The constant-magnitude family `|delta|=c`,
`c in (0, pi/3)`, satisfies every formal constraint for all five hostile
candidates, so the formal layer selects **no** value (S4). (F5) Within the
AB/Lefschetz fixed-locus density class with the 3-cycle's own transverse
weights `(1,2)` (forced as the cycle's eigenvalues), the density is the unique
value `L3(1,2) = 2/9` (S6).

The formal theorem is exactly (F1)-(F5). The map from this formal object to
the physical charged-lepton surface, and the identification of the registered
`|delta|` with the fixed-locus density read in radians (the atom `A_R-eta`),
are **conditional/open** physical hypotheses routed through the unaudited
carrier gate and R-eta source; they are not part of the formal theorem and are
not claimed derived.

## Statement

Write the AC_phi_lambda Hermitian circulant of the carrier context as
`H(delta) = a I + B e^{i delta} C + B e^{-i delta} C^T` (the form consumed
from the Tier-A K-orbit note, L2). The R-eta statement of the sibling chain
note — "the registered C3-breaking phase magnitude is the fixed-locus
spectral density, read directly as the angle: `|delta| = L3(1,2)`" — bundles
four distinguishable contents:

- **(S-form-1)** magnitude-only registration: the registered datum is
  `|delta|`; sign/orientation carries no registrable content;
- **(S-form-2)** single-channel registration: the registrable delta-content
  of the species surface enters through `cos(3 delta)` alone, on the
  fundamental domain `[0, pi/3]`, decoupled from the `r`-carrier;
- **(S-form-3)** no det-class packaging factor: on the determinant-class
  registrable surface no `pi * n_minus` det-sign phase factor is available;
- **(S-value)** the identification proper: the registered `|delta|` equals
  the Atiyah-Bott/Lefschetz fixed-locus density of the realized `C3[111]`
  cycle, identity-read in radians.

**Theorem (narrowing, bounded).**

1. **(S-form-1) is forced.** By Record (Additivity) + (Orbit) — an additive
   scalar functional is odd by pure algebra (`g(0)=0`, `g(-x)=-g(x)`; no
   continuity assumed), and K/CPT-orbit constancy makes it even; odd AND even
   is identically zero. The K/CPT conjugation acts on the circulant as
   `conj(H(delta)) = H(-delta)` (verified exactly), so the orientation-odd
   line `sin(3 delta)` is K-odd and unregistrable. Any registrable
   delta-readout is an even function of delta, i.e. a function of the orbit
   invariant `|delta|`. (Runner S1-S2.)
2. **(S-form-2) is forced.** Exact symmetric-function algebra on `H(delta)`:
   `e1 = 3a` and `e2 = 3a^2 - 3B^2 = 3a^2(1-r)` are delta-BLIND (`e2` is the
   `r`-carrier); `e3 = a^3 - 3aB^2 + 2B^3 cos(3 delta)` carries delta solely
   via `cos(3 delta)`; all `e_i` are even in delta as symbolic identities;
   and `e3(delta + 2 pi/3) = e3(delta)`, so evenness + period fold the
   registrable delta-content onto `[0, pi/3]`. (Runner S3.)
3. **(S-form-3) is forced on the det-class surface, bounded elsewhere.**
   Orbit constancy of a multiplicative determinant character
   `chi_k(z) = exp(i k arg z)` forces `k = 0` (finite scan witness), so no
   registrable `pi * n_minus` det-sign factor exists on that surface. This is
   a bounded forcing: it does not foreclose a future non-det readout context
   supplying another dimensionless factor. (Runner S5.)
4. **The machinery provably cannot select (S-value).** The forced form layer
   admits the entire family of constant-magnitude identifications
   `|delta| = c`, `c in (0, pi/3)`: five physically inequivalent hostile
   candidates (`2/9`, `1/9`, `4/9`, `2 pi/9`, `3/10`) all pass every forced
   constraint (in-domain, K-even registered surface, cos3delta channel) and
   give five distinct registered mass multisets. Registrability does not even
   forbid `r`-coupled identifications (e.g. `|delta| = (1-r)/2` is K-even):
   it is the named atom — pure C3-cycle data — that keeps delta `r`-decoupled.
   (Runner S4.)
5. **Within the natural class the density is unique, so the atom is minimal.**
   The transverse spectrum of the 3-cycle is `{omega, omega^2}`, forcing the
   weight exponents `(1,2)` (they are the cycle's own eigenvalues, not a
   choice); `(omega-1)(omega^2-1) = 3` exactly; `L3(1,2) = 2/9` exactly; the
   contrast cells `L3(1,1) = L3(2,2) = 1/9` require equal weights, which the
   spectrum does not supply. So within the AB/Lefschetz fixed-locus density
   class with the cycle's own (forced) weights, the density value is unique.
   (Runner S6; the arithmetic cross-checks the retained-bounded fixed-locus
   note.)

**The minimal admitted atom.** What remains admitted in sub-admission (ii) is
the single identification

```text
A_R-eta:  the registered |delta| IS the AB/Lefschetz fixed-locus density of
          the realized C3[111] cycle, identity-read in radians.
```

`A_R-eta` has two named hypothesis components, neither derived here:
**(h-class)** class membership — the registered angle is a fixed-locus
density of the realized cycle at all (as opposed to any other K-even
functional of the carrier data); **(h-unit)** identity reading — radians with
conversion factor 1 (the det-class `pi` route is closed by item 3; other
future contexts remain bounded-open). Conditional on `A_R-eta`, the weights
are forced, the value is exact arithmetic (`|delta| = 2/9`, in-domain, not a
`{n pi/3}` stationarity point), and every other clause of the original R-eta
statement is derived. The magnitude `2/9` is **not** claimed derived.

## Quantifying the atom's work (hostile guard (b), answered head-on)

The hostile objection "an inequivalent even functional gives a different
`|delta|`, so the atom is doing all the work" is **correct about the value
and only about the value** — and that is the content of this note. Measured
exactly (runner S4):

- the forced form layer cuts the candidate readout space from "all functions
  of delta" down to the constant-magnitude family on `(0, pi/3)` read on the
  `cos(3 delta)` channel — but it selects **no member** of that family
  (5/5 inequivalent hostile candidates pass all forced constraints);
- the atom therefore carries **exactly one real parameter** of load: the
  value of `|delta|`. It carries none of the form load: sign-strip, channel,
  domain, `r`-decoupling of the named atom, weights, and arithmetic are
  forced or exact independently of it.

Before this note, sub-admission (ii) read as the whole "density-read-as-angle"
package; after it, the honest admitted content is the one-parameter
identification `A_R-eta` (equivalently: h-class + h-unit). That is a strictly
smaller residual with the same admitted status — narrowed, not retired.

## Hostile guard (a): no circularity

The objection "the cos3delta channel already assumes R-eta" fails on the
derivation order (runner S7): the channel result is exact symmetric-function
algebra on `H(delta)`, symbolic in `{a, B, delta}`, holding as an identity
for ALL delta, with no density object, no `L3`, and no `2/9` anywhere in the
computation. The circulant form itself is consumed from the carrier / Tier-A
K-orbit context, which predates and is independent of R-eta. R-eta enters
exactly once, at the final identification step — which is why it can be
isolated as the atom.

## Boundary

- **Not retired.** Sub-admission (ii) remains a Tier-A admission; this note
  narrows what it admits to `A_R-eta` and proves the rest of the package.
  Registry wording changes are audit-lane / owner business, not enacted here.
- **Not derived.** `|delta| = 2/9` remains conditional on `A_R-eta`. No claim
  that `A_R-eta` is forced; the runner shows the opposite (the form layer
  cannot select it).
- **Unaudited siblings, handled honestly.** The three siblings whose content
  this note touches are unaudited on origin/main; every leg of theirs that
  this note load-bears is **re-derived from scratch in this runner** (S2
  re-proves the additive+even sign-strip; S3 re-proves the e1/e2/e3
  separation; S6 re-proves the density arithmetic against the
  retained-bounded fixed-locus note). What is inherited from the siblings is
  framing only (the R-eta name and the chain assembly), flagged below.
- **Out of scope.** Sub-admission (i) (occupancy selection — the `r` dial),
  sub-admission (iii) (species bridge), the R1b anchor (separate lane), the
  R2 global PL/ABSS bridge (external-math LIVE in the retained-bounded
  fixed-locus note), the carrier-gate realization, and strong-CP premise 1.
- **Bounded forcings stay bounded.** The `k = 0` det-character forcing is the
  det-class surface only; a future non-det readout context supplying another
  dimensionless conversion factor is not foreclosed (that would attack
  h-unit). The next paths this opens: (1) derive h-class — e.g. a registrable
  C3-covariant holonomy / eta-invariant construction on the carrier (the
  route the phase/modulus separation note leaves open) whose registered datum
  is provably the fixed-locus density; (2) close h-unit beyond the det class
  by classifying the registrable conversion-factor sources; (3) the R1b
  anchor lane joining onto the narrowed atom.
- **No comparator consumed.** No PDG/fitted/measured value enters; the
  sibling chain note's mass comparator (E4) is not used.

## Source-side W2/readout-context bridge (2026-06-18)

[`ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md`](ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md)
is a later source-side bounded support packet for one soft spot named below:
the standing W2-type premise that the supplied charged-lepton readout context
satisfies Record registrability constraints. That bridge checks the supplied
finite AC_phi_lambda slot/circulant context as a Record-registrable context and
therefore narrows the residual to the physical carrier/context realization
plus the unchanged `A_R-eta` h-class/h-unit value atom. It does not retire this
admission, derive `|delta| = 2/9`, edit the Tier-A registry, or set/predict any
downstream status.

## Honest-auditor-read

An auditor should read this note as: *a bounded structural theorem that
re-partitions the content of an existing Tier-A sub-admission, with all
load-bearing algebra re-derived in an exact 55-check runner, and with the
admitted residual restated in a strictly smaller, named form (`A_R-eta` =
h-class + h-unit, one real parameter of load).* The note's value is the
honest split, not a value derivation. Soft spots an auditor should press:

1. the identification of the runner's 3x3 circulant with the physical
   charged-lepton surface routes through the carrier gate
   (`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03`, context only here) and
   the Tier-A K-orbit note's L2 form (retained-bounded on current `main`;
   one-hop authority for the formal circulant form only). The *physical*
   identification is conditional on the carrier-gate
   context; the formal H(delta) algebra of section "Formal theorem (H(delta)
   layer)" depends on the retained circulant form alone;
2. "weights forced" is forced *within* the AB/Lefschetz class — class
   membership is h-class, i.e. still admitted; the note does not hide this;
3. the additive+even sign-strip is re-derived here, but its application to
   the physical readout assumes the standing premise that the physical
   readout context satisfies the Record registrability constraints (the
   named W2-type premise of the sibling registrable-readout note);
4. the fundamental-domain forcing uses the C3 relabeling fold of the
   unordered multiset — an auditor should confirm the relabeling is the
   vacuous naming freedom the registry already excludes from the admission.

## Dependencies (current-main status reviewed 2026-06-20)

- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  — meta (the live registry; source of the sub-admission (ii) text being
  narrowed).
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — approved
  axiom surface (Record (Additivity)+(Orbit), the only axiom input).
- [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — **retained_bounded** (the fixed-locus arithmetic this runner
  cross-checks; also where R2 is named LIVE).
- [`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
  — retained-bounded (one-hop authority for the circulant form L2 and the
  K/CPT sign-flip context: `H(delta) = a I + B e^{i delta} C + B e^{-i delta}
  C^T` and `conj(H(delta)) = H(-delta)`. The formal H(delta) algebra below is
  a finite re-derivation on this retained circulant form).
- `CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md`
  — **retained_pending_chain** (the bounded Tier-A surface for the delta
  admission this note narrows; target surface, not authority for this proof).
- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  — **retained_no_go** (boundary: why a rational density is not automatically
  a radian — exactly the h-unit component of the atom; respected, not
  entered).
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  — **unaudited** (carrier gate; context only, not retained-grade authority
  for this proof).
- `REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`
  — **UNAUDITED sibling** (the additive+even theorem and the orientation
  strip; its load-bearing legs are re-derived from scratch in this runner —
  S2, S5 — so this note's algebra does not lean on its audit status; the
  W2-type standing premise is inherited and flagged).
- `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  — **UNAUDITED sibling conditional source** (the R-eta statement being
  decomposed; treated as a sibling conditional source per the live ledger,
  NOT cited as retained; its E1 arithmetic is re-proven here, its E4
  comparator is not consumed).
- `LEPTON_PHASE_MODULUS_SEPARATION_NO_GO_2026-06-06.md`
  — **UNAUDITED** (the e1/e2/e3 separation and the `{n pi/3}` nondegenerate
  stationarity boundary; both re-derived/re-checked exactly in this runner —
  S3, S8).

**No-promotion statement:** this note does not promote, demote, or set the
status of any dependency. The independent audit lane is the only status
authority.
