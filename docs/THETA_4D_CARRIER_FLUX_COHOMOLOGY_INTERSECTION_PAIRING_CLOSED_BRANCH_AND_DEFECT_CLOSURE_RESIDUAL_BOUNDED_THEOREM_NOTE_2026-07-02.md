# The 4D Carrier Template: on Finite T^4 the Emergent Sector Labels Are the Six Flux-Cohomology Integers and the Theta Charge Is Their Cross-Plane Intersection Pairing, Exact on the Closed-Branch Abelian Surface — Defect (Monopole) Closure Is the Carrier Residual, and the Center Dual Alone Carries Only the Mod-N Pairing (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite cochain constructions on a
witness surface plus wall-sharpening; not a terminal no-go, not a discharge
of the theta admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.py`](../scripts/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.txt`](../logs/runner-cache/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.txt)

## Question

The two-block theta campaign left `W_theta_Q_context` in sharpened form:
per-plaquette character gradings cannot carry a `Z`-valued label
([`GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md`](GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md)),
while on closed 2D surfaces the multi-plaquette gluing derives the integer
exactly and branch-datum-free but with a 2D-specific mechanism — every link
borders exactly two plaquettes
([`GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)).
The sharpened residual was named there:

```text
(i)  the 4D carrier: a derived multi-plaquette structure on the 4D surface
     playing the role the branch-summed abelian slot plays in 2D;
(ii) the action-level pairing selection: that the physical action class
     weights sectors by e^{i theta Q} for that carrier's label.
```

Question answered here: what exactly does the 2D template become on the
finite Euclidean 4-torus — which labels survive, what is the theta charge,
what breaks, and what does the physical `SU(3)` case still need?

## Answer

Four exact finite results on the cubical cochain complex of `T^4` (all
integer/rational linear algebra and cup-product identities, runner-verified
at `L = 2` with `L = 3` stability):

1. **The sector labels are the six flux-cohomology integers.** In 4D each
   link borders `2(d-1) = 6` plaquettes, so the 2D matched-label mechanism
   fails; what survives of the dual-label kernel modulo local dual moves is
   the cohomology `H^2(T^4, Z) = Z^6` — six flux integers `m_(mu nu)`, one
   per coordinate 2-plane (Betti numbers `(1,4,6,4,1)` derived from the
   boundary maps; torsion-free; stable at `L = 3`).

2. **The theta charge is the cross-plane intersection pairing.** For closed
   integer branch 2-cochains `n` (`dn = 0`), the cup square is
   class-invariant, even, and equals twice the intersection form:

   ```text
   Q(n) = (1/2) sum n u n = m01 m23 - m02 m13 + m03 m12   in Z,
   ```

   with **odd support** (`Q = 1` at unit complementary fluxes) and **pure
   cross-plane structure** (every single-plane configuration has `Q = 0`).
   A coordinate reflection flips `Q` (the pairing `Z_Q = Z_(-Q)` mechanism).

3. **The theta slot reduces exactly to the flux pairing on the closed
   branch.** For real link 1-cochains `theta_link` and closed integer `n`,

   ```text
   sum (d theta_link + 2 pi n) u (d theta_link + 2 pi n) = 4 pi^2 Q_raw(n)
   ```

   exactly — every `theta_link`-dependent term telescopes away (via the
   runner-verified Leibniz rule and closed-surface telescoping). So on the
   closed-branch abelian surface the theta insertion weights sectors by
   `e^{i theta Q(m)}` with `Q(m)` the flux intersection **alone**, and the
   sector decomposition `Z(theta) = sum_m e^{i theta Q(m)} Z_m` is an exact
   regrouping of a positive sum, with `Z_m > 0`, reflection-paired, odd-`Q`
   populated.

4. **Two boundaries, each now theorem-shaped.**
   - **Defect closure:** with a branch defect present (`dn != 0`, the
     monopole current), the cup square is not even invariant under local
     branch moves (explicit witness: values `{-2, -1, 0, 1, 3}` over moves,
     including odd `Q_raw`, so the halving fails too) — **no sector
     decomposition exists on the unrestricted branch sum.** The 4D carrier
     exists exactly on the closed-branch (defect-free) subsurface, so the
     carrier residual (i) sharpens to a defect-closure derivation.
   - **Center-dual insufficiency:** the same construction over `Z_3` gives
     six `Z_3` flux sectors with the intersection pairing mod 3, but the
     `Z`-valued pairing has **no period-3 descent** to `Z_3` fluxes (for
     every flux axis `e` there is `x` with `q(x + 3e) != q(x)`). So the
     `SU(3)` center dual alone cannot carry the integer pairing — the
     `Z`-valued carrier must come from the full abelianized (torus) dual
     structure, not the center projection.

**Net effect on the wall.** `W_theta_Q_context`'s residual (i) is refined
into two named sub-walls, and residual (ii) acquires its exact 4D template:

```text
(i-a) defect closure: derive the closed-branch (dn = 0) restriction — or
      its dynamical suppression — on the abelianized multi-plaquette dual;
(i-b) SU(3) abelianization: derive that the glued 4D SU(3) effective weight
      develops the abelian (torus-dual) branch structure carrying Z-valued
      fluxes (the center Z_3 projection provably does not suffice);
(ii') pairing selection: derive the F u F-shaped multi-plaquette insertion
      from the framework surface; its exact sector reduction — theta couples
      to the flux intersection and to nothing else on the closed branch —
      is now supplied by this note.
```

## Source surface (named authorities)

1. **Record axiom** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)), quoted:

   > "When present, a record locks exactly one admissible local possibility. A
   > site never carries more than one record; records are permanent. Only
   > records are readable. A readout value is determined by record content
   > alone. For any finite collection of pairwise-disjoint records, scalar
   > readout `I` is additive, with `I(empty)=0`."

   Used only as the registration/additivity interface shape; the sector
   decomposition is derived, not supplied by Record; record occurrence is
   not claimed.

2. **Tier-A theta registry text**
   ([`docs/audit/data/premise_decision_history.json`](audit/data/premise_decision_history.json),
   gauge side, quoted exactly):

   > "(a) gauge side -- theta_gauge = 0 in the topological-sector weighting,
   > residual localized to the multi-plaquette / large-gauge-winding account
   > (within the supplied per-plaquette class the local cross-plane F Ftilde
   > slot is derived-absent; ...)"

   The pairing constructed here is exactly a **multi-plaquette cross-plane**
   object: the cup product couples plaquettes in complementary planes at
   neighboring sites, single-plane configurations carry `Q = 0`, and no
   per-plaquette density representation is used or implied — fully
   consistent with the registry-tracked per-plaquette absence result, and
   landing on precisely the account the registry names.

All cochain-level facts (boundary maps, Betti numbers, cup products, Leibniz
rule, flux representatives, class invariance, reflection action) are earned
inline by the runner as exact integer/rational linear algebra on the finite
complex. No external comparator, measured value, fitted number, or continuum
input enters anywhere. Deterministic pseudo-random integer/real cochains from
a fixed seed are used solely to test exact identities.

## Setup

The cubical cochain complex of the periodic lattice `T^4_L`: `k`-cells
`(x, S)` with `S` a size-`k` direction set; coboundary

```text
(d a)(x; S) = sum_(mu in S) (-1)^(pos(mu,S)) [a(x + e_mu; S \ mu) - a(x; S \ mu)],
```

and the cubical cup product of a `p`- and a `q`-cochain

```text
(a u b)(x; S) = sum_((S1,S2) shuffles of S, |S1| = p)
                sign(S1,S2) a(x; S1) b(x + e_(S1); S2).
```

Runner-verified structure: `dd = 0`; Leibniz `d(a u b) = da u b +
(-1)^p a u db` exactly on integer and real cochains; the total sum of any
exact 4-cochain over the closed torus vanishes. The branch-summed abelian
weight class is the one from the companion 2D gluing note
([`GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)):
plaquette weights built from a real plaquette variable summed over `2 pi`
shifts, the shift integers forming the branch 2-cochain `n`; the field
2-cochain is `F = d theta_link + 2 pi n`.

## Theorem 1 (flux-cohomology sectors)

On `T^4_L`:

1. Each link borders exactly `2(d-1) = 6` plaquettes (runner A5) — the
   two-sided incidence that made the 2D dual a single matched label is
   absent; local dual freedom exists.
2. The Betti numbers of the complex are `(1, 4, 6, 4, 1)` with torsion-free
   boundary maps (ranks over `Q` equal ranks over `GF(2)`, `GF(3)`,
   `GF(5)`); `dim H^2 = 6` again at `L = 3`. The surviving global sector
   data of the branch/dual 2-cochains modulo local moves is therefore the
   six flux integers `m_(mu nu)` — one per coordinate 2-plane, with explicit
   closed unit-flux representatives (runner C1).
3. Sharpness and Record-interface shape: the flux class is constant on each
   branch class (a partition of the closed-branch sum), the decomposition is
   a finite family in any bounded-flux truncation, and the closed-surface
   class label is invariant under all local branch moves — the permanent,
   content-determined, lock-one-alternative shape of the Record axiom's
   registration clause. (Interface match only; record occurrence is not
   claimed.)

## Theorem 2 (the intersection pairing is the theta charge)

For closed integer branch cochains `n` (`dn = 0`) on `T^4_2`:

1. `Q_raw(n) = sum n u n` is invariant under `n -> n + d lambda` (runner
   C5) and even (C6), so `Q(n) = Q_raw(n)/2` is a well-defined integer on
   branch classes.
2. On flux vectors, `Q` **is** the intersection form (C2):

   ```text
   Q(m) = m01 m23 - m02 m13 + m03 m12.
   ```

3. `Q` has odd support: unit complementary fluxes give `Q = 1` (C3).
4. `Q` is purely cross-plane: every single-plane configuration — however
   large its fluxes — has `Q = 0` (C4). The charge exists only as a product
   of fluxes in complementary planes; it has no single-plane and no
   per-plaquette representation on this surface.
5. A coordinate reflection preserves closedness and maps `Q -> -Q` (F1);
   with any reflection-invariant weight this pairs the sector weights,
   `Z_Q = Z_(-Q)`.

## Theorem 3 (exact theta-slot reduction on the closed branch)

For real link 1-cochains `theta_link` and closed integer `n`:

```text
sum_(4-cells) (d theta_link + 2 pi n) u (d theta_link + 2 pi n)
  = 4 pi^2 Q_raw(n)          exactly (runner D1).
```

Every `theta_link`-dependent term telescopes: `d theta u d theta` and the
cross terms are exact 4-cochains by the Leibniz rule (with `dn = 0`), and
exact 4-cochains sum to zero on the closed torus (B3). Since
`Q_raw = 2 Q`, this is exactly

```text
(1/(8 pi^2)) sum F u F = Q(n)   in Z
```

— the standard `F F-tilde` normalization emerges exactly at the finite
cochain level. Consequences:

- the theta insertion `e^{i theta (1/(8 pi^2)) sum F u F} = e^{i theta Q(n)}`
  is **constant on each branch class**, equal to `e^{i theta Q(m)}`;
- therefore the closed-branch partition sum regroups exactly as

  ```text
  Z(theta) = sum_m e^{i theta Q(m)} Z_m,
  ```

  with `Z_m` a sum/integral of strictly positive weights (positive weight
  class), independent of `theta`, reflection-paired, and populated on odd
  `Q` (interface arithmetic H1-H2: at `theta = pi` every odd-`Q` sector
  carries negative weight; at `theta = 0` all weights are nonnegative);
- the pairing content of the wall's residual (ii) is thereby pinned on this
  surface: **given** an `F u F`-shaped multi-plaquette insertion, theta
  couples to the flux intersection and to nothing else. What remains of
  (ii) is deriving that insertion's presence/shape from the framework
  surface — not its sector reduction.

## Theorem 4 (defect boundary and center-dual insufficiency)

1. **Defect breaks the sector structure.** For an open branch cochain
   (`dn != 0` — a single-plaquette witness), the cup square takes multiple
   values over local branch moves (`{-2, -1, 0, 1, 3}` observed, including
   odd `Q_raw`, so even the halving fails) — no class function exists and
   no sector decomposition survives on the unrestricted branch sum (E1-E2).
   The exact 4D carrier therefore lives on the **closed-branch (defect-free)
   subsurface**; what a physical derivation must supply is the closedness
   restriction or its dynamical suppression. This is the sharpened carrier
   sub-wall (i-a).
2. **Center dual carries only the mod-N pairing.** Over `GF(3)` the same
   complex has `dim H^2 = 6` (G1) and the intersection pairing descends mod
   3 (G2); but the `Z`-valued pairing has no period-3 descent: for every
   flux axis `e` there is `x` with `q(x + 3e) != q(x)` (G3). A `Z_3` flux
   assignment therefore supports only a `Z_3`-valued pairing — consistent
   with and extending the companion per-plaquette obstruction
   ([`GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md`](GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md))
   to the multi-plaquette account: the `SU(3)` **center projection cannot
   carry the integer theta charge**; the `Z`-valued carrier needs the full
   abelianized (torus) dual. This is the sharpened carrier sub-wall (i-b).

## Identification checkpoint (what objects these are)

The `T^4` abelian branch-summed surface is a witness surface: it is not the
physical `SU(3)` gauge sector, and no claim is made that its flux integers or
intersection charge are the physical theta `Q`. The flux labels here are the
4D analogue of the companion 2D note's derived labels — what changes in 4D
is derived, not assumed: labels become cohomology classes, the charge becomes
their quadratic cross-plane pairing, and two failure modes (defects; mod-N
centers) become explicit theorems. The headline is a theory of the 4D
carrier template and its boundaries — not a registration of the physical
theta angle's `Q`.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection-positivity identity is used
here and no bare-theta-slot exclusion is asserted; the reflection map of
Theorem 2.5 is a cochain pullback used to pair sector weights, not an RP
argument.

## What moves

| Prior state | After this note |
|---|---|
| 4D carrier (residual (i) of the linked 2D gluing note) = named unknown | template exact: sector labels = `H^2(T^4,Z) = Z^6` flux integers; charge = cross-plane intersection pairing; odd support at unit complementary fluxes |
| theta pairing in 4D = interface input | derived on the closed branch: all `theta_link`-dependent terms telescope; theta couples to the flux intersection alone |
| "multi-plaquette / large-gauge-winding account" (registry) | given exact finite content: the charge is a multi-plaquette cross-plane pairing with no single-plane or per-plaquette representation — consistent with the registry-tracked local absence result |
| defect role unstated | theorem-shaped: `dn != 0` destroys class invariance (explicit witness values) — carrier requires defect closure (sub-wall i-a) |
| center-dual hope for `SU(3)` | provably insufficient: intersection pairing has no period-3 descent — the `Z` carrier needs the abelianized torus dual (sub-wall i-b) |

## What remains

```text
W_theta_Q_context (sharpened again):
  (i-a) defect closure: derive the closed-branch restriction (dn = 0) or
        its suppression on the abelianized multi-plaquette dual;
  (i-b) SU(3) abelianization: derive the torus-dual branch structure of the
        glued 4D SU(3) effective weight (center Z_3 projection provably
        insufficient);
  (ii') derive the F u F-shaped multi-plaquette insertion from the framework
        surface (its exact sector reduction is supplied here).

W_theta_bar_assembly:
  unchanged; assembly-side bridge work remains outside this note.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the abelian `T^4` witness surface is the physical gauge sector, or
  that its flux/intersection data are the physical theta `Q`;
- a derivation of defect closure (i-a), of `SU(3)` abelianization (i-b), or
  of the framework-level `F u F` insertion (ii') — those are the sharpened
  residuals;
- any local per-plaquette representation of the charge (none exists on this
  surface: single-plane configurations carry `Q = 0`; the registry-tracked
  per-plaquette cross-plane absence result is untouched and matched);
- that compact abelian gauge theory without defect closure has theta
  sectors (the explicit witness shows the opposite on this surface);
- record occurrence, measurement dynamics, any continuum-limit statement, or
  any identification of the framework's Admissibility axiom with the
  closed-branch restriction (the shape-match is noted as a forward question
  only, not asserted);
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Gate result:** PASS as bounded scoping inside positive constructions. The
negative content is exactly: (a) with branch defects present the cup square
is not class-stable, so the unrestricted branch sum has no sector
decomposition on this surface; (b) the `Z`-valued intersection pairing does
not descend to `Z_N` fluxes, so the center dual alone cannot carry it.

### N1 — Alternative-route enumeration

| Route to the physical 4D sharp integer-Q context | Standing here |
|---|---|
| per-plaquette character grading | EXCLUDED by the linked companion obstruction |
| 2D-style matched single label in 4D | FAILS STRUCTURALLY: links border 6 plaquettes; replaced by the cohomology construction (Theorem 1) |
| closed-branch abelian flux sectors + intersection pairing | CONSTRUCTED (Theorems 1-3): the exact 4D template with odd support and action-derived pairing |
| unrestricted branch sum (defects allowed) | EXCLUDED on this surface (Theorem 4.1): no class-stable charge — motivates sub-wall (i-a) |
| center `Z_N` dual as the `SU(3)` carrier | EXCLUDED for the integer pairing (Theorem 4.2): mod-N only — motivates sub-wall (i-b) |
| abelianized (torus) dual of glued 4D SU(3) weight | OPEN — sharpened carrier residual (i-b) |
| framework derivation of the `F u F` insertion | OPEN — sharpened pairing residual (ii') |
| scaling-limit sector functional | OPEN — unchanged live path |
| operational primitive registration | APPROVED-PRIMITIVE PROPOSAL, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side (`W_mass_determinant_action`) or
`W_theta_bar_assembly`. The defect statement (a) is surface-scoped (the
abelian branch-summed class on `T^4`); it does not assert that defect-ful
theories lack theta physics in general — it identifies exactly which
restriction the sector structure needs on this surface. The center statement
(b) excludes one carrier for one job (integer pairing); `Z_N` sectors remain
real structure (mod-N pairing exists).

### N3 — Hidden-wall scan

"Closed branch" (`dn = 0`) is an explicit restriction, stated as a
boundary and named as sub-wall (i-a) — not smuggled: Theorem 4.1 proves the
sector structure fails without it. The normalization `Q = Q_raw/2` is
justified by evenness on closed cochains (C6), itself runner-verified. The
flux representatives are explicit cochains; class invariance is checked with
explicit local moves, not assumed. No positivity, reality, RP, or CPT input
is used.

### N4 — Residual matching

The Tier-A registry names "the multi-plaquette / large-gauge-winding
account" with the local cross-plane slot derived-absent per-plaquette; this
note's charge is a global cross-plane pairing with `Q = 0` on single planes
— landing on that account and respecting the absence result. The companion
notes' residuals map exactly: the linked 2D gluing note's (i) becomes
(i-a) + (i-b); its (ii) becomes (ii') with the sector-reduction half now
supplied. The landed
[`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
Euclidean-carrier relocation is extended: the integer sector functional
exists exactly on the closed-branch 4D abelian surface, with the defect
condition now the named price.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. Negative statements are scoped to
this surface and this carrier question; live paths are named; the wall is
sharpened, not discharged.

### N6 — Partial-closure path scan

Live paths: derive (i-a) defect closure (constraint-level or dynamical
suppression; whether the framework's Admissibility rule bears on it is an
open forward question, not asserted here); derive (i-b) the `SU(3)`
torus-dual branch structure of the glued effective weight; derive (ii') the
`F u F` insertion from the framework surface; the scaling-limit route; and
the separate assembly-side work.

### N7 — Steelman

A hostile reviewer can press: (1) "This is textbook lattice topology
restated." The ingredients are classical; the deliverables are the exact
finite-lattice theorem set in the framework's own audit format — in
particular the telescoping proof that theta couples to the intersection
alone, the explicit defect witness, and the no-descent obstruction — wired
to the named wall decomposition. No novelty claim beyond that wiring is
made. (2) "The closed-branch restriction is doing all the work." Correct —
and Theorem 4.1 makes that unavoidable rather than optional: the note's
point is that the carrier residual IS the defect question. (3) "Calling the
flux classes a sector-record context invites the realist slip." The
identification checkpoint refuses any physical-Q identification; only the
interface shape (sharp lock, record permanence, content-determined additive
readout arithmetic) is matched, on a witness surface. All three objections are
absorbed into scope.

### N8 — Cross-cycle echo

The echo risk after three blocks is compounding witness-surface progress
into physical-surface progress. The guard stays structural: any future cycle
citing this chain must supply (i-a), (i-b), and (ii') — each named
separately here precisely so that none can be silently absorbed. The defect
witness values and the no-descent identity are the canonical counterexamples
to keep against re-attempts of "unrestricted-sum theta sectors" and
"center-dual integer charge."

## Verification

Run:

```bash
python3 scripts/theta_4d_carrier_flux_cohomology_intersection_pairing_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=24 FAIL=0
```

Sections: A complex (`dd = 0`; Betti `(1,4,6,4,1)`; torsion-freeness; `L=3`
stability; 6-plaquette link incidence); B cup machinery (Leibniz on integer
and real cochains; closed-torus telescoping); C flux sectors and pairing
(closed representatives; `Q_raw = 2 x` intersection; odd support;
cross-plane nullity; class invariance; evenness); D theta-slot reduction
(exact telescoping identity and its sector consequence); E defect boundary
(open cochain witness; class instability); F reflection pairing; G center
dual (GF(3) sectors; mod-3 descent of the pairing; no period-3 `Z`-descent);
H sector-decomposition interface arithmetic (positive weight family; odd
support; pairing; `theta = pi` negativity).
