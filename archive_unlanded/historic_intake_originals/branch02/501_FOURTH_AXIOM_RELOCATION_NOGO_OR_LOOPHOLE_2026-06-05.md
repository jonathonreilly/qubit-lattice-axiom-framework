# The 4th-axiom dichotomy: any dynamics relocates the flavor input or gives the wrong (special) modulus — a meta/scoping map, with two genuine openings flagged

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta
**Status:** scoping / meta-exploration. Source-note proposal; no theorem
promotion, no audit verdict claimed. Pipeline-derived status is set only by the
independent post-landing audit. This note imports no axiom and derives no
modulus; it maps the space of candidate 4th axioms and records what a runner
finds when several parameter-free quantities and cross-sector relations are
tested against the observed moduli (which are **observational comparison only**).
**Primary runner:** [`scripts/fourth_axiom_relocation_nogo_2026_06_05.py`](../scripts/fourth_axiom_relocation_nogo_2026_06_05.py) (15/15 PASS).

## The question

The A1/A2/A3 baseline has no dynamics. The per-sector generation modulus

```text
r := |b|^2 / a^2   in   F = a*I + b*(J - I),     Q = 1/3 + (2/3) r,
```

is therefore a free continuous input (one real number per sector after scale).
Sibling lanes test specific dynamics (variational/extremal, RG/β-function,
self-consistency/gap) as candidate 4th axioms. This note asks the **general**
question and genuinely hunts for a loophole rather than confirming a no-go.

**Dichotomy to test.** (i) Any dynamics that selects an *extremum / fixed point
/ equilibrium* lands on a *distinguished* point of the dial (`r ∈ {0, 1/2, 1}` =
the symmetry-enhanced / chiral-distinguished points). The observed quark/neutrino
moduli are *generic* (`r_up ≈ 0.77`, `r_down ≈ 0.60`, `r_ν ≈ 0.24`), so
extremum-type dynamics is **falsified by the quark values**. (ii) Any dynamics
producing a generic value must use a free coupling/boundary condition — which
**relocates** the flavor input. Conjecture: no 4th axiom escapes both horns.

## Observed moduli (OBSERVATIONAL COMPARISON ONLY — never a derivation input)

| sector | Q (observed) | r = (3Q−1)/2 | dial class |
|---|---:|---:|---|
| charged lepton (e,μ,τ) | 0.6667 | **0.5000** | DISTINGUISHED (r=1/2, chiral-null, Q=2/3) |
| up quark (u,c,t) | 0.8488 | **0.7732** | GENERIC |
| down quark (d,s,b) | 0.7313 | **0.5969** | GENERIC |
| neutrino (NO proxy) | 0.4920 | **0.2381** | GENERIC |

The charged lepton sits *exactly* on the dial's one interior distinguished point
(`r=1/2` to ~1e-4) — which is why the rest of the campaign can reduce it to the
single chiral input `AC_φλ`. **The quarks do not.** This is the crux the meta
question sharpens: the charged-lepton story (a special value) does **not**
generalize to the quark sectors (generic values), so an extremum-type 4th axiom
cannot be right for the full flavor sector.

## Loophole route 1 — parameter-free lattice/spectral quantities

The strongest lead (from the arc): the `Z^3` nearest-neighbor graph-Laplacian
Green function is genuinely parameter-free (Watson constant `G(0)=0.252731…`,
asymptotic `1/(4π|r|)`), and *generic-valued*. Does any parameter-free lattice
quantity equal an observed modulus?

**What the runner finds (and why it is NOT a loophole).** Several Green-function
ratios land within ~1% of the moduli — e.g. `G(200)/G(110)=0.774` vs `r_up=0.773`
(|Δ|=3e-4), `G(220)/G(110)=0.502` vs `r_lep=0.500`, `G(221)/G(111)=0.594` vs
`r_down=0.597`. Taken in isolation these look striking. But this is a textbook
**look-elsewhere** artifact:

- The parameter-free Green ratios **densely fill** the modulus window. In
  `(0.40, 0.90)` there are **42** of them, mean gap `≈ 0.012`. Any target in that
  window therefore has a ratio within `≈ 0.006` (half the gap) *by density
  alone*. The runner confirms each modulus' best match (|Δ| ≈ 3e-4 to 5e-3) is
  *within the density-expected* tolerance — i.e. exactly what you get for an
  arbitrary number, no signal.
- No **single canonical, pre-specified** Green quantity (the a-priori first-shell
  ratios you would write down *before* looking — `G(100)/G(000)`, `G(110)/G(100)`,
  `G(111)/G(110)`, …) equals any modulus to the `<1e-3` bar a parameter-free
  *derivation* would require; the closest, `G(111)/G(100)=0.501` near the
  *special* `r_lep=1/2`, still misses at the per-mille level and targets the
  special value, not a generic quark modulus.

So "a lattice Green ratio near the observed modulus" is **numerology forced by a
densely-filled window**, not a parameter-free mechanism. A genuine loophole would
need a *distinguished, pre-registered* parameter-free quantity that is also
*structurally a modulus* (a property of the 3×3 flavor spectrum, not a 2-point
function on the substrate). The Green function is the wrong *type* of object: `r`
is the squared doublet amplitude of a circulant mass matrix, not a propagator
value. No such object is found.

## Loophole route 2 — a cross-sector relational reduction

Could a single relation tying `r_up, r_down, r_lep` reduce the input below
one-per-sector *without forcing values*? The runner tests simple relations:

| relation | value | nearest simple | rel.err | drift (+4% mid mass) |
|---|---:|---:|---:|---:|
| r_up/r_down | 1.2953 | 13/10 | 0.36% | 0.0038 |
| r_down/r_lep | 1.1939 | 6/5 | 0.51% | 0.0090 |
| r_up/r_lep | 1.5464 | 3/2 | 3.09% | 0.0072 |
| (r_up+r_down)/2 | 0.6851 | 2/3 | 2.76% | 0.0041 |
| r_up·r_down | 0.4615 | 4/9 | 3.85% | 0.0056 |

**No relation is both tight and stable.** The two closest near-misses
(`r_up/r_down≈13/10`, `r_down/r_lep≈6/5`) miss at the 0.36–0.51% level, and their
**precision-sensitivity tell** is decisive: nudging the (poorly-known) mid masses
by +4% — well within PDG error — moves each ratio by an amount comparable to or
larger than its own residual gap. A *structural* relation would be invariant
under input precision; these drift with it, exposing them as fit coincidences.
Even were one exact, it would only trade two free moduli for one free modulus + a
fixed ratio — a reduction, granted — but the data does not supply an exact,
precision-stable one.

The **one genuine literature coincidence** (recorded, not endorsed): the
heavy-quark triplet `Q(c,b,t)=0.669 ≈ 2/3` sits near the lepton's special point,
and `Q(all 6 quarks)=0.636 ≈ 7/11`. But the triplet pattern is *selective*:
`Q(s,c,b)=0.458` is nowhere near `2/3`. So "triplet-Koide" is a re-grouping of
species, not a sector law, and it does **not** predict the up/down moduli that
are the actual generic inputs. It relocates (which triplet? why heavy?) rather
than reduces.

## Why the dichotomy is structurally tight

The dial's distinguished points are exactly `{0, 1/2, 1}`:

- `r=0` (Q=1/3): democratic, full `S₃` enhancement;
- `r=1` (Q=1): rank-1 dimension/Plancherel endpoint;
- `r=1/2` (Q=2/3): the chiral-grading null `⟨v|Γ_χ|v⟩=0` (the lepton point).

All other `r` give the *plain* `C₃` pattern (degenerate doublet + singlet) with
**no** symmetry enhancement. This is the same category-mismatch the sibling
assumptions-audit and native-β lanes found (
[`FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md`](FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md),
[`FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30.md`](FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30.md)),
now extended past the charged lepton to the *generic* quark sectors where it
bites hardest:

- **Extremum / fixed-point / equilibrium dynamics** lands on an enhanced point,
  and the quark moduli avoid every enhanced point (gap `> 0.05`). So any such
  4th axiom gives the **wrong** quark value. (RG attractors sit at enhanced
  couplings; gap equations land at `b=0 → r=0`; variational extrema land at the
  symmetric endpoints. The generic quark `r` is none of these.)
- **Generic-value dynamics** must carry a free continuous coupling (the amplitude
  `b`), because `r` *is* the squared amplitude ratio `|b|²/a²`. Fixing it to a
  generic number is choosing a continuous coupling — i.e. **relocation** of the
  flavor input, not its elimination.

The escape the dichotomy would need is a dynamics that is (a) parameter-free,
(b) lands on a *non-enhanced* (generic) value, and (c) hits the *specific*
observed numbers. Route 1 shows parameter-free generic-valued substrate
quantities exist but are the wrong *type* and only "match" via window density;
Route 2 shows no exact precision-stable cross-sector relation. Both horns hold.

## Verdict: RELOCATION-NO-GO-HOLDS (kinematic floor is the honest endpoint)

On the tested surface, **any 4th-axiom dynamics either gives a special
(quark-falsified) modulus or relocates the flavor input into a free coupling /
boundary condition / triplet-choice.** No parameter-free quantity of the right
type hits the generic moduli; no simple exact cross-sector relation reduces the
input. The kinematic floor — **one continuous modulus per sector** (charged
lepton pinned at the special `r=1/2`, quarks/neutrinos genuinely free) — is the
honest current endpoint.

## Two openings this maps (next paths, NOT closed walls)

Per standing practice this is a provisional scoping map, not an airtight
impossibility. Two openings remain genuinely live and are flagged for attack:

1. **A distinguished parameter-free *spectral* (not propagator) quantity.** Route
   1 ruled out Green-function *ratios* (wrong type + window density). It did
   **not** rule out a pre-registered *spectral* invariant of a parameter-free
   `C₃`-native flavor operator (e.g. an overlap/index density of the
   staggered/Kawamoto–Smit operator restricted to the hw=1 orbit) that is
   *structurally a modulus*. If such an object is generic-valued and pre-specified
   (no window-shopping), it would be a true loophole. Untested here.

2. **An exact, precision-stable cross-sector relation among 2+ sectors.** Route 2
   tested simple two-sector ratios at current PDG precision and found only
   precision-sensitive near-misses. A relation derived from a shared structure
   (e.g. a single `C₃`/CKM-linked source law tying `r_up, r_down` through the
   mixing data) could reduce the count even without forcing individual values.
   The heavy-triplet `Q(c,b,t)≈2/3` coincidence is the empirical hint that such a
   structure may exist; it is not yet a relation, but it is not foreclosed.

Neither opening is the "last route." The framework reproduces the full flavor
phenomenology with a few pins; this note narrows *where* a derivation of the
generic moduli would have to come from (a distinguished spectral modulus, or a
cross-sector source law), and removes two tempting blind alleys (Green-ratio
numerology and precision-sensitive fraction-spotting).

## No-Go Discipline Gate

- **N1 alternative routes:** (1) parameter-free lattice Green ratios — ruled out
  (window density + wrong type); (2) canonical first-shell Green quantities —
  none hits to `<1e-3`; (3) simple cross-sector ratios/products/sums — no exact
  precision-stable one; (4) triplet-Koide re-grouping — selective, relocates;
  (5) extremum/RG/gap dynamics — lands on enhanced endpoints (quark-falsified).
  Openings (spectral-invariant route, source-law cross-sector relation) are
  flagged as live, not closed.
- **N2 wall independence:** the per-sector continuous modulus is independent of
  the charged-lepton `r=1/2` chiral pin (`AC_φλ`), the `δ=2/9` readout, and the
  absolute mass scale. This note touches only the *value-selection* horn.
- **N3 hidden-wall scan:** the only inputs are the observed masses (comparison
  only, flagged) and the pure circulant algebra `Q=1/3+(2/3)r`. No PDG value is a
  derivation input; no new axiom is introduced.
- **N4 residual matching:** the "look-elsewhere density" and "precision drift"
  controls match the residuals they bound (a `<1%` Green-ratio hit vs a `0.012`
  mean gap; a `0.36%` ratio near-miss vs a `+4%`-mass drift of comparable size).

## How to run

```bash
python3 scripts/fourth_axiom_relocation_nogo_2026_06_05.py   # 15/15 PASS
```

## Related

- [`FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md`](FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md) — the charged-lepton `r=1/2` assumptions audit (category mismatch).
- [`FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30.md`](FLAVOR_NATIVE_BETA_NO_HALF_ATTRACTOR_NOTE_2026-05-30.md) — RG attractors sit at enhanced points (banner: superseded for `r=1/2` status by the thermalizing-arrow note; the enhanced-endpoint structure used here stands).
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md) — current charged-lepton chain modulo `AC_φλ`.
- [`ANGULAR_KERNEL_ORBIT_CLASS_UNDERDETERMINATION_NARROW_NO_GO_NOTE_2026-05-10.md`](ANGULAR_KERNEL_ORBIT_CLASS_UNDERDETERMINATION_NARROW_NO_GO_NOTE_2026-05-10.md) — orbit-kernel `Q`-value underdetermination (same density phenomenon, kernel side).
