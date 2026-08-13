---
claim_id: finite_one_site_product_is_not_plaquette_holonomy_law_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The 16-atom product of one-site binary laws on the four corners of a unit square is an executable finite measure, but plaquette holonomy is a function of the four link angles and is independent of those site bits, so the product is the wrong type for a U(1) holonomy law."
upstream_dependencies:
  - minimal_axioms
runner: scripts/finite_one_site_product_is_not_plaquette_holonomy_law_2026_08_13.py
---

# Finite One-Site Product Is Not A Plaquette Holonomy Law

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact 16-atom product of one-site binary laws on the four corners of
a unit square, and the type split against the Z/2Z holonomy of four two-point
link angles; a holonomy law remains extra.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/finite_one_site_product_is_not_plaquette_holonomy_law_2026_08_13.py`](../scripts/finite_one_site_product_is_not_plaquette_holonomy_law_2026_08_13.py)

## Result Up Front

A joint physical law `L_phys` is not to be taken as a derived object until it
is executable. The finite executable object that does exist on the four
corners of a unit square is the product of one-site binary laws. That product
is a 16-atom table. It is the wrong type for a U(1) plaquette holonomy.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is quoted only
as a premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Qualification of a law is likewise quoted only as a premise:

A law privileges no states. Its domain is a supplied condition, and at every
state where the condition holds it gives exactly one answer.

The current Lattice sentence is quoted only to type the unit square as four
sites of `Z^3` in the plane `z=0`:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

Five exact statements locate the type split.

1. **Product is executable.** For `p_x=1/2` at each of the four sites, each of
   the 16 atoms has mass `1/16`. For `p_x=1/3`, the atom `0000` has mass
   `(1/3)^4=1/81`. The table is a well-defined finite measure.
2. **Holonomy is not a function of site bits.** The holonomy `H` of four link
   angles is independent of the four site bits. With bits held at `0000`,
   `H(0,0,0,0)=0` and `H(1/2,0,0,0)=1` (mod 2). Therefore `H` is independent
   of the product law `P_S`.
3. **Bit-sum is not holonomy.** The bit-sum `B` is a function of the four
   site bits. `H` is a function of the four oriented links. They live on
   different domains. After any declared pairing of bits to links, the product
   law on bits still does not determine a joint law on links.
4. **Type residual.** The executable finite object is `P_S`. A holonomy law
   would be a law on links (or on group elements). These are unequal types.
   This note does not adopt `L_phys`, does not adopt a holonomy law, and does
   not claim that gauge theory is impossible.
5. **Not a factorization theorem.** Distant-bit factorization of one-site
   laws on disjoint neighbor supports is a different theorem about bit-bit
   joints. It is not this bit-link type split. An axiom edit is not required.
   Do not adopt `L_phys`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 16-atom product masses 1/16 and 1/81, and the holonomy witnesses H=0 versus H=1 at fixed site bits, are proved by exact Fraction arithmetic and integer mod 2; the executable object is a site-bit table, not a holonomy law."
trace_class: negative_route_pruning
target_claim_id: joint_law_l_phys
target_blocker_text: "an executable physical joint law, including holonomy"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "The executable finite product is a site-bit table, not a holonomy law. Do not adopt L_phys. Do not adopt axiom text."
conditional_surface_status: "exact for the 16-atom one-site product and for H=0 versus H=1 at fixed bits; a holonomy law remains extra"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work in the plane `z=0` of the cubic lattice `Z^3`. Write

`e1=(1,0,0)`, `e2=(0,1,0)`, `0=(0,0,0)`.

The **unit square** has sites

`S = {0, e1, e1+e2, e2} = {(0,0,0), (1,0,0), (1,1,0), (0,1,0)}`.

The four oriented links of the square are

`ℓ = {(0,e1), (e1,e1+e2), (e1+e2,e2), (e2,0)}`.

A **one-site binary law** at a site `x ∈ S` is a pair `(p_x, 1−p_x)` on the
ordered menu `{0,1}`, with `p_x` a `Fraction` in `(0,1]`. The 0-label carries
mass `p_x`. The executed `{0,1}` is that declared finite menu. It is not a
derivation that the Qubit one-site domain is binary.

The **product law** on the four corners is

`P_S = ⊗_{x ∈ S} Bern(p_x)`.

It is a 16-atom table on `{0,1}^4`. The mass of a bit string
`s = (s_0, s_{e1}, s_{e1+e2}, s_{e2})` is

`product_mass(s, p) = ∏_{x ∈ S} (p_x if s_x=0 else 1−p_x)`.

A **link angle** is a variable `θ_ℓ ∈ {0, 1/2}` standing for the exact
two-point subgroup `{1, −1}` of `U(1)`, with group elements `exp(2πi θ)`.
This is not a continuum import. The holonomy of the oriented square is the
product of the four group elements. Its `Z/2Z` logarithm is

`H = θ_01 + θ_12 + θ_23 + θ_30` (mod 2),

evaluated as the integer exponent of `−1`: equivalently
`H = 2(θ_01+θ_12+θ_23+θ_30) (mod 2)`. Thus

`H(0,0,0,0)=0`, `H(1/2,0,0,0)=1` (mod 2).

`H` is a function of the four link variables. The four site bits are not
arguments of `H`.

A **bit-sum** is the function of the four site bits

`B = s_0 + s_{e1} + s_{e1+e2} + s_{e2}` (mod 2).

`B` and `H` are both `{0,1}`-valued. They are not the same map: `B` is
indexed by `S`, `H` is indexed by `ℓ`.

The fair product used as the uniform witness is `p_x=1/2` at every site:
every atom has mass `(1/2)^4=1/16`. The biased witness is `p_x=1/3` at every
site: the atom `0000` has mass `(1/3)^4=1/81`.

## Exact Target And Obligation Graph

**Exact target.** On the declared unit square, execute the 16-atom product of
one-site binary laws, prove it is a finite measure, prove that plaquette
holonomy is independent of those site bits, and record that the product is
the wrong type for a holonomy law, without adopting `L_phys`.

| Obligation | Role | Disposition |
|---|---|---|
| pin the Admissibility distribution sentence | premise | quoted; no edit |
| pin “a law privileges no states; its domain is a supplied condition” | premise | quoted; no edit |
| pin Lattice NN adjacency and the unit-square listing | premise | quoted; sites and links listed |
| show the 16-atom table is a finite measure, `1/16` and `1/81` | Theorem 1 | product of Fractions |
| show `H(0,0,0,0)=0` and `H(1/2,0,0,0)=1` at fixed bits | Theorem 2 | integer mod 2 |
| show `B` and `H` live on unequal domains | Theorem 3 | sites versus links |
| record that `P_S` is not a holonomy law and is not `L_phys` | Theorem 4 | type residual |
| record that distant-bit factorization is a different theorem | Theorem 5 | scoped negative |
| adopt `L_phys` or a holonomy law | non-claim | not attempted |
| claim that gauge theory is impossible | non-claim | not attempted |

## Theorem 1 — Product Is Executable

**Claim.** For `p_x=1/2` at each site, each of the 16 atoms has mass `1/16`.
For `p_x=1/3`, the atom `0000` has mass `(1/3)^4=1/81`. The table is a
well-defined finite measure.

**Proof.** There are four sites and a binary menu at each site, so there are
`2^4=16` atoms. The product mass of a bit string is the product of four
one-site masses. If every `p_x` equals `1/2`, then every one-site factor is
`1/2` regardless of the bit, and every atom has mass

`(1/2)^4 = 1/16`.

The sixteen masses sum to `16 · (1/16) = 1`. If every `p_x` equals `1/3`,
the atom `0000` uses the 0-label at each site, so its mass is

`(1/3)^4 = 1/81`.

The complementary atom `1111` then has mass `(2/3)^4=16/81`, and the sixteen
nonnegative rationals still sum to `1`. The construction uses only finite
products of `Fraction` values in `(0,1]`. It is therefore a well-defined
finite measure on a 16-point set. The runner recomputes `product_mass` on
every atom of the fair table and on the biased atom `0000`.

The table is executable. Executability is not a type match with holonomy.

## Theorem 2 — Holonomy Is Not A Function Of Site Bits

**Claim.** There exist two link configurations with the same four site bits
giving `H=0` and `H=1`. Site bits may be held fixed at `0000`. Therefore `H`
is independent of `P_S`.

**Proof.** Site bits are not arguments of `H`. The two executed link
configurations are

`θ^{(0)} = (0,0,0,0)`, `θ^{(1)} = (1/2, 0, 0, 0)`.

The sum of angles is `0` in the first case and `1/2` in the second. Doubling
into the integer exponent of `−1` gives

`H(θ^{(0)}) = 2·0 = 0 (mod 2)`,
`H(θ^{(1)}) = 2·(1/2) = 1 (mod 2)`.

Hold the four site bits at `0000`. The product mass
`product_mass((0,0,0,0), p)` depends only on the four margins `p`. It does
not change when the link angles change. The two holonomy values are
different at that fixed bit string. A function of the site bits, including
every atom mass of `P_S`, is therefore constant on a pair of inputs that
`H` separates. Hence `H` is not a function of `P_S`.

The same pair of holonomy values is obtained at every other fixed bit
string. The independence is not an accident of the zero atom.

A predicate “`product_mass` determines holonomy” is therefore false on the
executed pair: the mass is the same and the holonomy is not.

## Theorem 3 — Bit-Sum Is Not Holonomy

**Claim.** `B` is a function of `S`. `H` is a function of `ℓ`. They live on
different domains. Even after any declared pairing of bits to links, the
product law on bits does not determine a joint law on links.

**Proof.** The domain of `B` is the four-point set `S`. The domain of `H` is
the four-edge set `ℓ`. These sets are unequal: a site is not an oriented
link, and an oriented link is not a site. Equality of `{0,1}` as a value
set does not identify the maps.

A declared pairing that sends each site to a neighboring link is an extra
bijection. It is not supplied by Admissibility, and it is not supplied by
`P_S`. After any such pairing one still has two independent functions: `B`
varies when a site bit flips and the link angles are held fixed, while `H`
varies when one link angle flips and the site bits are held fixed. Theorem 2
is the second variation. The first is the elementary identity
`B(1000)=1 ≠ 0=B(0000)` at fixed `θ`. Neither variation is a function of the
other.

Replacing the holonomy map by the bit-sum therefore fails domain equality:
the identity-gate `holonomy` is typed on `ℓ`, and `bit_sum` is typed on `S`.

## Theorem 4 — Type Residual

**Claim.** The executable finite object is `P_S`. A holonomy law would be a
law on links (or on group elements). These are unequal types. This note
does not adopt `L_phys`, does not adopt a holonomy law, and does not claim
that gauge theory is impossible.

**Proof.** Theorem 1 exhibits `P_S` as a 16-atom measure on site bits.
Theorems 2 and 3 show that holonomy is not a function of those bits and is
not the bit-sum. Qualification states that a law's domain is a supplied
condition. The supplied condition of `P_S` is a 4-tuple of one-site menus
on `S`. The supplied condition of a holonomy law would be a 4-tuple of link
angles on `ℓ`, or a 4-tuple of group elements. Those conditions are
unequal, so the laws are unequal types.

Declaring `P_S` to be `L_phys` would identify a site-bit table with a
physical joint law that is supposed to include holonomy. That identification
fails the type check. The residual is the missing executable law on links,
not a defect of the 16-atom table as a table.

The residual is scoped. It does not say that a later executable holonomy
law on links is closed, and it does not say that gauge theory cannot be
reached by some later bridge whose objects are actually link-valued.

## Theorem 5 — Distant-Bit Factorization Is Not This Type Split

**Claim.** Distant-bit factorization of one-site laws on disjoint neighbor
supports is a different theorem. It is not the present bit-link type split.
An axiom edit is not required. Do not adopt `L_phys`.

**Proof.** A factorization theorem about two distant site bits asks whether
a pair of one-site maps on disjoint 6-tuples is a product measure on
`{0,1}^2`. Both factors are site-bit laws. The present theorem asks whether
a four-site product determines a holonomy on four links. One comparison is
bit-bit. The other is bit-link. A positive or negative answer to the
bit-bit question does not decide the type of `H`.

The Admissibility sentence already names a per-site distribution determined
by nearest-neighbor conditions. The Qualification sentence already names
that a law's domain is a supplied condition. Those sentences do not name a
holonomy on links, and they do not name `L_phys`. Pairing four one-site
maps into `P_S` is already an executable product. Identifying that product
with a holonomy law is a type error, not a missing axiom sentence.

`L_phys` is not required as an axiom. If a later derivation produces an
executable law on the four links, that derivation can be checked then.
Until it is executable and of holonomy type it remains extra. Do not adopt
`L_phys`.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- adopt `L_phys`, or treat `L_phys` as named axiom content;
- adopt a holonomy law, or claim that gauge theory is impossible;
- replace the two-point subgroup `{0, 1/2}` by continuum `U(1)`;
- identify the bit-sum `B` with the holonomy `H`;
- construct intermediate records on a path, or derive record formation;
- identify the executed `{0,1}` menu with the full one-site possibility
  domain `M_2(C)`.

The scope is the exact type split: a 16-atom one-site product on the four
corners, holonomy witnesses `H=0` versus `H=1` at fixed bits, and unequal
domains for `B` and `H`.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Lattice NN sentence | premise | quoted; no edit |
| current Admissibility distribution sentence | premise | quoted; no edit |
| Qualification: a law privileges no states; its domain is a supplied condition | premise | quoted; no edit |
| unit-square sites `S` and oriented links `ℓ` | declared objects | listed here |
| 16-atom product `P_S` and masses `1/16`, `1/81` | Theorem 1 | computed here |
| two-point holonomy `H(0,0,0,0)=0`, `H(1/2,0,0,0)=1` | Theorem 2 | computed here |
| bit-sum versus holonomy domains | Theorem 3 | sites versus links |
| `L_phys` and a holonomy law | residuals | extra; not adopted |
| observed frequencies or fitted joints | none | not used |

The exact advance is a finite type-split theorem. Independent audit is
required. This note authors no audit verdict.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The current Admissibility sentence says that for each site the probability distribution is determined by, and varies with, the nearest-neighbor conditions. Qualification adds that a law privileges no states and that its domain is a supplied condition. The named residual is an executable physical joint law, including holonomy. This note asks whether the executable 16-atom one-site product already is that holonomy law, and answers no: the domains are unequal. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for a one-site product versus plaquette holonomy type split, a 16-atom corner-bit table, and `L_phys` as a joint law. Hits: Wilson and gauge-vacuum notes treat plaquette holonomy as a product of four *link* unitaries, which is already the holonomy type and not a site-bit table; the native-holonomy center-flux note is an `su(3)` taste-space commutator, a different object; Born-form product-menu notes bound effect menus, not holonomy; the token `L_phys` on that commit is a continuum path length in the valley-linear note, not a joint law. Unmerged factorization listings are bit-bit independence on disjoint neighbor supports, not this bit-link type split, and are not premises. No landed theorem that the 16-atom one-site product is not a plaquette holonomy law appears on that commit. |
| V3 | Independently checkable? | Textbook Bernoulli products on four bits do not mention holonomy, the two-point subgroup `{0, 1/2}`, or the four oriented links of a unit square. The runner recomputes `product_mass` and `holonomy` by exact `Fraction` arithmetic and integer mod 2. |
| V4 | More than a restatement? | Yes. The discriminating witnesses are `(1/2)^4=1/16` versus `(1/3)^4=1/81`, and `H(0,0,0,0)=0` versus `H(1/2,0,0,0)=1` at fixed site bits. Neither identity is a restatement of the Admissibility sentence. |
| V5 | One-step relabel? | No. The claim is not a corollary of one-site Admissibility alone. That sentence names a per-site distribution determined by nearest-neighbor conditions. It does not name a four-link holonomy, a 16-atom product, or the type split against `H`. |

## No-Go Discipline Gate (Theorems 4 and 5 only)

The negative claims are restricted to: the executable 16-atom product is not
a holonomy law; distant-bit factorization is not this type split; `L_phys`
is extra and is not adopted. The gate does not ship a global non-existence
theorem against gauge theory.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| declare `P_S` to be `L_phys` | identify the 16-atom site-bit table with an executable physical joint law that includes holonomy | Theorem 4: unequal types; `H` is independent of `P_S` | **ATTEMPTED** |
| identify `B` with `H` | treat the bit-sum on `S` as the holonomy on `ℓ` | Theorem 3: domains unequal; `B` flips with bits at fixed `θ`, `H` flips with `θ` at fixed bits | **ATTEMPTED** |
| continuum `U(1)` | replace `θ ∈ {0, 1/2}` by a continuum angle | a different object; the executed holonomy is the two-point subgroup, not a continuum import | **ATTEMPTED** |
| path records | let intermediate records on a path turn site bits into link angles | residual; not constructed and not declared; a path of records is not `P_S` and is not `H` | **ATTEMPTED** (escape) |
| axiom edit | treat the type residual as requiring an axiom-sentence change | Theorem 5: the domain of a law is already a supplied condition; an axiom edit is not required and is not performed | **ATTEMPTED** |

### N2 — wall independence

Theorems 4 and 5 close only the route that reads a holonomy law off the
16-atom one-site product, and the route that treats distant-bit
factorization as this type split. They do not close a later executable
link-valued holonomy, a later path-of-records construction, or a continuum
`U(1)` object constructed from other premises. Those walls remain
independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| unit square `S` and oriented links `ℓ` in the plane `z=0` | declared Lattice objects |
| one-site pair `(p, 1−p)` on `{0,1}` | declared finite menu; not the full `M_2(C)` domain |
| 16-atom product `P_S` | declared executable table |
| two-point angles `θ ∈ {0, 1/2}` | declared exact subgroup; not continuum `U(1)` |
| holonomy `H` and bit-sum `B` | declared maps on unequal domains |
| path of intermediate records | residual; not constructed |
| declared `L_phys` | extra; not adopted |
| continuum `U(1)` | live escape; not executed here |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Lattice NN sentence; Admissibility distribution sentence; Qualification domain sentence | quoted as premises only; no edit |
| 16-atom product on `S` | masses `1/16` and `1/81` | computed here |
| two-point holonomy on `ℓ` | `H=0` versus `H=1` at fixed bits | computed here |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the 16 atoms of `P_S` and the two holonomy inputs `(0,0,0,0)`, `(1/2,0,0,0)` | no classification of every map on `Z^3` |
| per site | one-site binary laws on the four corners | no composite bonded-pair theorem |
| per mode | two-point holonomy and the bit-sum, not spectral modes | no harmonic-mode exhaustion |
| per block | executability of `P_S` and the bit-link type split only | no dynamics, formation rate, or adopted joint |
| lattice-wide | checked and not executed | no lattice-wide no-go against gauge theory |

The obstruction is per-square / declared four-site product; it is not
lattice-wide.

### N6 — live partial-closure paths

1. A later executable law whose condition is the four link angles, or four
   group elements, rather than the four site bits.
2. A later construction of intermediate records on a path whose content
   supplies link angles. That object is not `P_S`.
3. A later executable object that one might label `L_phys`, if and when it
   is derived rather than declared and is of holonomy type. That object is
   not required as an axiom.
4. A continuum `U(1)` connection, if and when that object is constructed
   from the axioms. It is not the executed two-point subgroup.

The quoted Admissibility and Qualification sentences already name a per-site
distribution and that a law's domain is a supplied condition. The supplied
condition of `P_S` is a site-bit 4-tuple. No axiom sentence is edited here.

### N7 — hostile steelman

> The 16-atom table is executable, and holonomy is a `{0,1}`-valued function
> on four inputs, so one may simply read `H` off the bits after pairing each
> corner to a side. Then `P_S` already is the holonomy law, and the type
> residual is empty.

**Answer.** Pairing corners to sides is an extra bijection, not a theorem of
Admissibility. Even after that bijection, Theorem 2 still supplies two link
configurations with the same four bits and different holonomies. The mass
of every atom of `P_S` is constant on that pair. The discriminating facts
remain `H(0,0,0,0)=0` versus `H(1/2,0,0,0)=1` at fixed bits, together with
the unequal domains `S` versus `ℓ`. Theorem 4 records the residual.
Theorem 5 does not convert the residual into axiom text or into `L_phys`.

### N8 — cross-cycle echo

Wilson and gauge-vacuum notes already treat plaquette holonomy as a product
of link variables. That is the holonomy type. The present negatives face
the opposite identification: a site-bit product is executable and is still
not that type. Distant-bit factorization, when it appears, is a bit-bit
statement about disjoint neighbor supports. It does not cancel the present
type split and is not used as a premise.

**Gate disposition.** PASS for the scoped type split and the two negatives
of Theorems 4 and 5. FAIL / DO NOT SHIP for adopting `L_phys`, for adopting
a holonomy law, or for claiming that gauge theory is impossible.

## Primary Runner

[`scripts/finite_one_site_product_is_not_plaquette_holonomy_law_2026_08_13.py`](../scripts/finite_one_site_product_is_not_plaquette_holonomy_law_2026_08_13.py)
recomputes the 16-atom product, the masses `1/16` and `1/81`, the holonomy
witnesses `H=0` versus `H=1` at fixed site bits, and the site-versus-link
domain split in exact `Fraction` arithmetic and integer mod 2. Identity
gates call `product_mass(bits, ps)` and `holonomy(thetas)`. A predicate
“`product_mass` determines holonomy” must fail on the two executed link
configurations. Replacing holonomy by the bit-sum must fail domain
equality. Setting every `p_x=1/2` must give atom mass `1/16`, not `1`.
