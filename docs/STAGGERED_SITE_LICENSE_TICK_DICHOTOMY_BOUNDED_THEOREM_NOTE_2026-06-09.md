# The Site-Licensed Staggered Tick Dichotomy: Dispersive Means Saturating

**Date:** 2026-06-09
**Claim type:** bounded_theorem (a structural dichotomy for the realized
carrier's licensed ticks; discharges block01's P3 and reduces P4)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/staggered_site_license_tick_dichotomy_2026_06_09.py`](../scripts/staggered_site_license_tick_dichotomy_2026_06_09.py)
(SCORECARD: PASS=16, FAIL=0; cached:
[`logs/runner-cache/staggered_site_license_tick_dichotomy_2026_06_09.txt`](../logs/runner-cache/staggered_site_license_tick_dichotomy_2026_06_09.txt))

---

## What this closes (relative to block01)

The block01 theorem
([`KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md),
PR #3442) derived |v| = 1 for a winding band of a strict radius-1 unitary
2-band tick, conditional on (P3) CPT pairing of the tick spectrum and (P4)
the realized carrier sitting in the winding cell. Both were named conditional
inputs. **This cycle discharges P3 and reduces P4** for the framework's
realized carrier density: CPT pairing is not used anywhere, and chirality
need not be assumed — winding is FORCED by dispersiveness once the carrier's
actual structure is used. P4's surviving content is only "the realized tick
is dispersive (nonflat)".

The load-bearing structural fact: the landed, audit-pending scheme-forcing
([`STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md))
puts ONE Grassmann per site. For a one-component-per-site bipartite chain,
the adjacency license — radius 1 in SITES — forbids the diagonal Bloch
entries from carrying any momentum dependence: a same-sublattice hop
`A_j -> A_{j+-1}` is a distance-2 move (degree-table check). Block01's
tunable degree-1 trace freedom is structurally GONE for this carrier
(constant-trace check).

## The theorem (1D / per-axis, exact)

**Setting:** site-licensed (radius-1-in-sites), unitary, 2-site-periodic
one-tick updates on the one-Grassmann-per-site chain — the staggered
carrier's natural bipartite periodicity. The general licensed Bloch tick is
`U(z) = [[alpha, p + q/z], [r + s z, delta]]` with six constants.

**Structure (derived):** `tr U = alpha + delta` is CONSTANT; unitarity
kills the hopping cross terms (`s conj(r) = 0`, `p conj(q) = 0`) so each
off-diagonal entry is a single monomial; `det U` is a unimodular Laurent
polynomial, hence a monomial `e^{iD} z^w`, `w in {-1, 0, +1}` by the
block01 monomial lemma.

**The two-circles lemma:** a band eigenvalue `mu` satisfies
`|mu| = 1` and `det = mu(T - mu)`, so `|T - mu| = 1`: `mu` lies on the
intersection of the unit circle and the unit circle centered at `T` — at
most TWO points when `T != 0`. But for `w != 0` the
determinant `e^{iD} z^w` takes infinitely many values over the Brillouin
zone, while `mu(T - mu)` from two points takes at most two — contradiction
(a cardinality argument; no continuity needed). Hence:

```text
dispersive  =>  T = 0  =>  mu^2 = -e^{iD} z^w  =>
omega_pm(K) = (D + pi + wK)/2 + {0, pi}   EXACTLY
```

slope `w/2` in cell units = `w` in site units: **|v| = 1 edge/tick at every
momentum**, all curvature orders of the free single-particle dispersion
vanishing identically. `w = 0` cells are FLAT — constant bands, zero
transport. The dichotomy:

```text
{ FLAT (no transport) }  or  { SATURATING (|v| = 1 exactly) }.
```

No third cell exists: a dispersive site-licensed tick cannot be tuned. The
marginal anisotropy dial is structurally absent — and unlike block01, no
chirality or CPT premise selects the cell: **dispersiveness itself forces the
winding** (the seeded sweep corroborates on every dispersive solution found —
24 samples covering both windings `w = -1` and `w = +1` — `tr ~ 0`,
`|w| = 1`, `v = 1` site/tick; the sweep corroborates, the symbolic
dichotomy is the load-bearing item).

## The realization tie: the dispersive cells share the staggered hopping shape

- The dispersive cells in closed form are the two phase-decorated
  SITE-SHIFTS: `(U psi)_A(j) = q psi_B(j-1)`, `(U psi)_B(j) = r psi_A(j)`
  — one edge per tick, in amplitude.
- They are sublattice-off-diagonal (`eps U eps = -U`): pure `A <-> B`
  hopping, the staggered hopping shape. This is the hopping STRUCTURE
  shared with the landed staggered generator, not a claim that
  `{eps, D} = 0` transfers to the tick.
- Each dispersive cell is a SINGLE chiral mover; the two cells form the
  conjugate left/right sector pair. Dirac pairing and curved massive
  bands live at larger periodicity — the named open below. Note the licensed
  period-2 surface cannot reproduce the landed two-mover `sin(k)` dispersion
  (whose generator exponential is not site-licensed): the landed two-mover
  structure is necessarily larger-cell content, which sharpens the N7
  steelman rather than weakening it.
- The Kawamoto-Smit phases
  ([`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md))
  are constant along each direction's own axis (verified mechanically
  from the landed formulas on a 3^3 block), so the 1D theorem applies to any
  per-axis FACTOR, where the tick factorizes — the 3D simultaneous tick is
  the named open; the Lattice axiom's cubic symmetry equalizes the axes.

## Why block01's tunable cells cannot occur here

- The split-step walk — block01's P4 hostile witness — has K-dependent
  DIAGONAL Bloch entries: distance-2 site hops, license-illegal for this
  carrier density.
- Even block01's saturating cell-level construction (the full-swap
  brickwork, diagonal `z`-entries = 2-site moves) is site-license-illegal
  here: the realized saturating cells are the site-shifts above. With no
  tunable cell left to select against, **the CPT-pairing conditional is
  discharged and the winding-realization conditional reduces to nonflatness;
  neither is an assumption about WHICH dispersive cell**.
- The legal gapped cell at this periodicity is FLAT (dispersionless
  exchange): mass as a curved band needs a larger unit cell.

## The premise ledger after this cycle

| block01 premise | status after this cycle |
|---|---|
| P1 strict license reading | SHARPENED to the site-radius reading (same retained note, same verbatim definition, read in site units) |
| P2 unitary-tick reading | still a named conditional (unchanged) |
| P3 CPT pairing of the tick spectrum | **DISCHARGED** — not used anywhere |
| P4 nonzero band winding (chirality) | **REDUCED** to "the realized tick is dispersive (nonflat)" at the natural periodicity — winding itself is forced, no cell selection remains |
| B-W OS0 Wick identification | still a named bridge (unchanged) |
| block01 monomial lemma/source row | consumed; landed but unaudited, so conditionality is inherited |
| (new) landed scheme-forcing | consumed: one Grassmann per site (`unaudited` on the live ledger — conditionality inherited) |
| (new) KS per-axis phase tie | used only for the per-axis realization tie; landed but unaudited, so conditionality is inherited for that tie |
| (new) 2-site periodicity scope | the carrier's natural bipartite periodicity; larger cells = named open |

Remaining conditional set for "the realized carrier's kinetic-form ratio is
quantized to 1": **{P1' site-strict reading + P2 unitary reading + B-W
bridge + block01 source row (landed, unaudited) + scheme-forcing (landed,
unaudited) + KS per-axis tie where the per-axis realization is invoked
(landed, unaudited) + a dispersive (nonflat) realized tick + the periodicity
scope}.**

## What this note does NOT claim

- **Not a retirement of the primitive.** The registry is owner/audit
  territory; the conditional set above is real and named.
- **Periodicity scope.** The theorem is proved at the carrier's natural
  2-site (bipartite) periodicity. Larger unit cells — where curved massive
  bands and Dirac pairing live — are a NAMED OPEN: the expectation (from
  block01's D6b family) is that mass curves the IR while the saturating
  massless normalization point persists, but that is not proved here.
- **Single-mover structure.** A dispersive period-2 tick realizes one chiral
  sector; the full matter realization (pairing, mass, interactions) is
  larger-cell/composite content. The kinetic-form normalization statement —
  the primitive's content — concerns exactly the dispersive/massless
  structure quantized here.
- **1D / per-axis.** The full simultaneous 3D tick (Weyl-block mixing)
  remains the named open from block01.
- **No empirical input.** No comparator is cited anywhere.

## Falsifiers

- A framework derivation that the realized tick is non-unitary, non-strict,
  or not 2-site-periodic at the fundamental level (the dial returns through
  the named opens).
- A larger-cell enumeration finding a dispersive licensed tick with
  tunable cone slope at the massless point (would localize the primitive's
  content in the periodicity scope).
- The 3D enumeration producing a quantized slope different from 1.

## No-Go Discipline Gate (for the negative leg)

The negative claim: "no dispersive tunable site-licensed 2-site-periodic
tick exists."

- **N1 alternative routes:** (1) tunable trace — RULED OUT structurally by
  the constant-trace check;
  (2) blended hops `p, q != 0` — RULED OUT by unitarity; (3) tunable
  flat-to-dispersive interpolation — RULED OUT by the exact dichotomy;
  (4) two components per site — excluded only by the stated one-component
  carrier-density premise, inherited from the landed but unaudited
  scheme-forcing row; (5) larger periodicity — NOT ruled out: NAMED OPEN,
  stated in scope.
- **N2 wall independence:** collapsed wall set for the negative leg:
  site-radius license, unitary tick, one-component carrier density, and
  2-site periodicity. They are pairwise independent: dropping unitarity
  restores blended hops; dropping the site radius restores the split-step;
  dropping one-component density returns block01's two-component-cell regime;
  dropping period-2 scope opens the larger-cell route named above.
- **N3 hidden-wall scan:** "2-site periodicity" — declared in scope;
  "one component per site" — the landed scheme-forcing, cited with live
  landed-but-unaudited status; "translation covariance" — the Lattice axiom.
- **N4 residual matching:** block01's P3/P4 are the residuals discharged;
  the discharge is exact only at this periodicity and conditional on the
  wall set above; larger-periodicity residuals are not claimed closed.
- **N5 rhetoric audit:** "the dial does not exist" is scoped to site-licensed
  unitary 2-site-periodic ticks of the one-component carrier in 1D/per-axis.
- **N6 partial-closure scan:** no existing note covers the site-radius
  collapse (the anisotropy gate counts coefficients under symmetry, not
  under the license; block01 works at the 2-component-cell generality).
- **N7 steelman:** "the carrier's TRUE tick may be a larger-cell composite
  (to host mass), so the period-2 dichotomy may not bind the realized
  dynamics." Acknowledged as the periodicity-scope named open — the
  strongest residual, stated in the premise ledger and falsifiers. The
  counter-consideration: the kinetic-form normalization (the primitive's
  content) is the massless/dispersive structure, and every dispersive cell
  at the natural periodicity saturates.
- **N8 cross-cycle echo:** per-plaquette retired its structural statement by
  reading the license strictly at the generator level; block01 used the same
  reading at the 2-component-cell level; this cycle uses it at the
  realized-carrier-density level. Same mechanism, three rungs down.

## Dependencies

- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — the license (retained); read here at site radius.
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block01: the monomial lemma (consumed) and the premises discharged here; landed but unaudited, so conditionality is inherited.
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md) — one Grassmann per site; landed but unaudited, so conditionality is inherited.
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — landed phase formulas used in the per-axis constancy check; landed but unaudited, so conditionality is inherited for that realization tie.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the target.
- [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md) — the independence surface (sharpened by block01; this cycle adds the carrier-density collapse).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
