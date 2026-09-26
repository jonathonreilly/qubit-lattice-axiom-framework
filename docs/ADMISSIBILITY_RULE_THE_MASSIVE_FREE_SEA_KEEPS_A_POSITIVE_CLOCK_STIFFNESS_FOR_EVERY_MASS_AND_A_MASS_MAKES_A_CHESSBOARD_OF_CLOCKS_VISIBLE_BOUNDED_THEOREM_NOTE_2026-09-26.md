---
claim_id: admissibility_rule_the_massive_free_sea_keeps_a_positive_clock_stiffness_for_every_mass_and_a_mass_makes_a_chessboard_of_clocks_visible_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 77's walk with a staggered mass, H_m = H + m eps (eps_x = (-1)^(x+y+z), m != 0 real), clocked as phi H_m phi = phi H phi + m w eps (w = phi^2 = e^u), block 76's filled sea E_sea = sum of the negative levels, block 55's energy density, and the kernel normalisation E(a) - E(0) = Pi(q) a^2 N + O(a^3) for u = a cos(q.x) (2q not 0 or Q), Pi = c0/4 + (kappa/4)|q|^2_lat + O(|q|^4): (T1) the even exchange maps commute with H_m, the odd ones after eps, no map commuting with eps is a twin (block 71's on-site twin fails by 2 m w eps |psi|^2), and eps T is a twin with e_x[eps T psi; T phi] = -e_{x-e1}[psi; phi]; (T2) the filled sea's energy density is exactly m eps_x - <E>, E = sqrt(|sin k|^2 + m^2), and its second-order kernel is the held sea's plus a term in [-9|q|^4/(64|m|^3), 0]; (T3) hence c0 = -<E> and kappa(m) = (1/12)<|sin k|^2/E>, positive and strictly decreasing in |m| for every m, tending to the massless value as m -> 0, with 1/(8m) - 7/(64m^3) + 81/(512m^5) - ... for m > sqrt3 and exact enclosures at m = 2, 4; (T4) a chessboard of clocks, invisible without a mass (block 76 T1), has first variation N m and second -N m^2 <1/E> with one. Exact (integers, fractions, sympy); T2's kernel uses standard second-order perturbation theory for the gapped sea. A harvest of probe #9210 (Claude Opus 5.5, the supervisor's family) confirmed by an other-family referee (#9295); nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_massive_free_sea_keeps_a_positive_clock_stiffness_for_every_mass_2026_09_26.py
---

# The massive free sea keeps a positive clock stiffness for every mass, and a mass makes a chessboard of clocks visible

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within the supplied clauses; a harvest of probe #9210, confirmed by an other-family referee in #9295; nothing adopted or registered; unaudited)

This note works within blocks 55, 70, 71, 76 and 77 as landed on main (the energy density, the exchange maps and twins, the filled sea and the clocked walk with a staggered mass); it reports the massive free sea's density and clock stiffness exactly, and what a mass does to the chessboard of clocks; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 77 gave the walk a staggered mass `m ε`, and deferred its numerical massive-sea experiments. Block 76 used a clock stiffness `κ` and a volume term `c` as inputs, "not derived sea coefficients". This note derives them exactly for the massive free sea.

- **T1: which maps survive a mass.** The even exchange maps survive. The odd ones survive after the site sign. No map that keeps the site sign turns energies over, so block 71's on-site twin fails. The one-site shift after the site sign, `εT`, is a twin, and it carries each state's energy density to minus itself one site over.
- **T2: the sea.** The filled sea's energy density is exactly `mε_x − ⟨E⟩`: a uniform part and a chessboard of amplitude exactly `m`. Its response to a clock profile, at second order, is the held sea's plus a term of order `|q|⁴/|m|³`.
- **T3: the stiffness.** `κ(m) = (1/12)⟨|sin k|²/√(|sin k|² + m²)⟩`. It is positive for every mass and falls as the mass grows: it is `1/(8m)` for a heavy sea. So a staggered mass never turns the sea's clock stiffness negative. The volume term is `c₀ = −⟨E⟩`.
- **T4: the chessboard.** Without a mass, a chessboard of clocks is invisible (block 76 T1). With one, it is not. The sea's energy changes at first order, by `N m`, which is exactly the sea's own chessboard density of T2.

In plain terms: giving the walk a mass does not destabilise the clocks, since the sea still resists a varying clock rate. But the mass lets the sea feel an alternating clock pattern that it could not feel before, and the sea's own alternating density is what it feels.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walk, its mass, the clocks and the sea are supplied clauses. Nothing is adopted.
- **The walk** (block 54): `H = Σ_a σ_a S_a`, `S_a = (T_a − T_a⁻¹)/(2i)`.
- **The mass and the clocks** (block 77, landed).
  - `ε_x = (−1)^{x+y+z}` and `H_m = H + mε`, with `m ≠ 0` real.
  - The clocked walk is `H_w = φH_mφ = φHφ + mwε`, with `w = φ² = e^u`. The landed text says "Moreover `phi(K+m eps)phi=phi K phi+m w eps`."
  - It also says "Numerical packet and massive-sea experiments are deferred."
- **The sea** (block 76, landed).
  - "The filled negative-level energy is E_-=sum_{lambda<0}lambda of this finite matrix."
  - The held sea `E_fix[u] = tr(P₋H_w)` keeps the projector at uniform clocks.
  - Block 76's `c` and `κ` "are inputs, not derived sea coefficients."
- **The energy density** (block 55): `e_x = Re ψ_x†(H_wψ)_x`.
- **The exchange maps and twins** (blocks 70 and 71, landed).
  - "(b) `V_nHV_n = s_nH`, and `V_n(φHφ)V_n = s_n φHφ` for every rate field."
  - Twins satisfy "`e_x[A_nψ] = −e_x[ψ]`".
- **The kernel.**
  - For `u = a cos(q·x)` with `2q` not `0` or `Q = π(1,1,1)`: `E(a) − E(0) = Π(q)a²N + O(a³)`, with `Π(q) = c₀/4 + (κ/4)|q|²_lat + O(|q|⁴)` and `|q|²_lat = Σ_j 2(1 − cos q_j)`.
  - `E(k) = √(|s|² + m²)` with `s = sin k`, and `⟨·⟩` is the zone average.
- **Standard imports, named at definition level.**
  - Second-order perturbation theory for the sum of the occupied levels of a gapped finite matrix. The gap `2|m|` makes it analytic.
  - Alternating series with decreasing terms bracket their sums.
  - Exact integer and rational arithmetic.

## Theorem T1 — which maps survive a mass

*Statement.*
- (a) Every exchange map `V_n` keeps `ε`. For even `n`, `V_n` commutes with `H_m`. For odd `n`, `εV_n` does.
- (b) No map that keeps `ε`, site by site or by a permutation that keeps the two parities, turns `H_m` into `−H_m`. Block 71's on-site twin `ΘV₁₁₁` gives `e[Aψ] + e[ψ] = 2m w ε|ψ|²`.
- (c) `εT` (the one-site shift after the site sign) turns `H_m` into `−H_m`. In the clocked walk it carries a state in the field `φ` to one of opposite energy in the field `Tφ`, with `e_x[εTψ; Tφ] = −e_{x−e₁}[ψ; φ]` at every site.

*Proof.*
- (a) and (c): `εHε = −H` and `THT⁻¹ = H`, while `TεT⁻¹ = −ε`, and block 70 T1(b) (runner B1).
- (b) `H` has no site-diagonal block, and a map that keeps `ε` keeps that property. But `−H − 2mε` has one.
- The density identities hold exactly for a rational rate field, `m = 7/5` and a Gaussian-rational state on the `4³` torus (runner B2). ∎

## Theorem T2 — the sea

*Statement.*
- (a) At uniform clocks the filled sea's energy density is exactly `e_x^sea = mε_x − ⟨E⟩`.
- (b) For every `m ≠ 0`, the free sea's second-order kernel is

  `Π(q) = −⟨E⟩/4 + (κ(m)/4)|q|²_lat − (1/16)⟨(1 − n·n′)(E − E′)²/(E + E′)⟩`,

  with `n = (s, m)/E` and primes at `k + q`. The last term lies in `[−9|q|⁴/(64|m|³), 0]`.

*Proof.*
- (a) In the block of `k` and `k + Q`, `M(k)² = E²`, so `P₋M = (M − E)/2`. The mass block has coin trace `2m`, and the diagonal of `√(H² + m²)` is uniform (runner C1).
- (b) The first-order element of `½{u, H_m}` is `½(λ_i + λ_j)⟨j|u|i⟩`. The projector overlaps are `1 + ab(s·s′ + m²)/(EE′)`. Summed, the second-order weight is `G = −½[(E + E′)(1 + n·n′) + (1 − n·n′)(E − E′)²/(E + E′)]`, and `Π = ⟨G⟩/8` (runner C2).
  - The first part is the held sea's kernel `3β/4 − m²J/4 − (β/16)|q|²_lat`, with `β = −⟨|s|²/E⟩/3` and `J = ⟨1/E⟩` (runner C4).
  - The bound follows from `|∂_j n|² ≤ 1/m²` and `|∂_j E| ≤ 1` (runner C3). ∎

## Theorem T3 — the stiffness

*Statement.*
- (a) `c₀(m) = −⟨E⟩` and `κ(m) = (1/12)⟨|s|²/√(|s|² + m²)⟩`.
- (b) `κ(m)` is positive and strictly decreasing in `|m|` for every `m`. It tends to the massless value `⟨|s|⟩/12` as `m → 0`.
- (c) For `|m| > √3`, `κ(m) = 1/(8m) − 7/(64m³) + 81/(512m⁵) − …`, from the exact zone moments `3/2, 21/8, 81/16`.
- (d) `κ(2)` and `κ(4)` lie in exact rational intervals of width below `10⁻¹⁰`, both positive.

*Proof.*
- (a) From T2(b): `κ = −β/4` and `c₀ = 3β − m²J = −⟨E⟩` (runner C4).
- (b) The integrand is nonnegative, positive almost everywhere, and strictly decreasing in `|m|`. The limit follows by domination (the integrand is bounded by its value at m = 0).
- (c) `(1 + x)^{−1/2}` with `x = |s|²/m² ≤ 3/m² < 1` is an alternating series with decreasing terms. Its partial sums bracket it pointwise, and averaging keeps the brackets (runner D1).
- (d) Runner D2. ∎

## Theorem T4 — the chessboard

*Statement.* Let `φ = c^ε` and `a = 2 log c`.
- (a) `φ_xφ_y = 1` on every bond, so `φHφ = H`, as in block 76 T1. But `mwε = m cosh(a) ε + m sinh(a)`.
- (b) No level crosses zero, and `E_sea(a) = N m sinh a − Σ_k √(|s|² + m² cosh² a)`.
- (c) The first variation along the chessboard is `N m`, which equals `Σ_x ε_x e_x^sea` of T2(a). The second variation is `−N m² ⟨1/E⟩`.

*Proof.*
- (a) Exact on the `4³` torus (runner D3).
- (b) The levels are `±√(|s|² + m² cosh² a) + m sinh a`, and `|m sinh a| < |m| cosh a`.
- (c) Differentiation (runner D3). ∎

## What this settles and what it does not

- **Settled.**
  - Block 76's inputs `c` and `κ`, for the free sea with a staggered mass, are now derived: `c₀ = −⟨E⟩` and `κ(m) = ⟨|s|²/E⟩/12 > 0`.
  - A mass never turns the stiffness negative.
  - A mass makes the chessboard of clocks visible, with a linear source equal to the sea's own chessboard density.
- **Not settled.**
  - The kernel at `q = Q`, where the linear source enters.
  - The projected (one record per site) sea of block 78.
  - The `|q|⁴` coefficient.
  - Which ledger clause, if any, uses `κ(m)`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 77: numerical packet and massive-sea experiments are deferred; block 76: c and kappa are inputs, not derived sea coefficients (probes task the-sixteen-branches-and-the-ledger-with-a-staggered-mass)"
source_of_blocker_text: landed notes of blocks 76 and 77; probes task J:derive:the-sixteen-branches-and-the-ledger-with-a-staggered-mass
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the kernel at q = Q with the sea's chessboard source; the projected sea of block 78"
conditional_surface_status: "free sea; 2q not 0 or Q; second-order perturbation theory for the gapped sea"
hypothetical_axiom_status: "the walk, its mass, the clocks and the sea are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Blocks 54 and 55: the walk and its energy density.
  - Blocks 70 and 71: the exchange maps and twins.
  - Block 76: the filled sea; a chessboard of clocks is invisible; `c` and `κ` as inputs.
  - Block 77: the staggered mass, and the clocked walk with it.
- **Probes.**
  - #9210, worker `w-macbookpro9927a-j17cc`, Claude Opus 5.5, the supervisor's own model family, found T1–T4 with an exact checker plus floating-point checks.
  - Attempt a2 (`w-jonathonsmac4f50-ja540`, the same family) had found the maps, the twin `εT`, the chessboard energy and floating-point `κ` values.
  - #9295, a Grok worker, another model family, refereed #9210 with its own checker. Its verdict: "Confirmed partial. A staggered mass does not change the sign of the free sea's stiffness."
- **New here.** The harvest. The supervisor ported the exact families, dropped the floating-point ones, and added the held-sea kernel check (C4).
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: block 76's `c` and `κ` for the massive free sea, and the chessboard with a mass. The obligations are:
- (O1) the landed premises (A3);
- (O2) the maps and twins (B1, B2);
- (O3) the sea's density and kernel (C1–C4);
- (O4) the stiffness and the chessboard (D1–D3).

The strongest missing step is the kernel at `q = Q`.

## No-Go Discipline Gate

The note's negative sentences:
- no map that keeps the site sign is a twin with a mass;
- the stiffness never changes sign.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A twin keeps the site sign.* The site-diagonal argument, and block 71's twin failing exactly (B2). ATTEMPTED.
2. *The free sea's extra term flips the sign of `κ`.* It is `O(|q|⁴/|m|³)` (C3). ATTEMPTED.
3. *`κ` turns negative at some mass.* The integrand is positive, with exact enclosures at `m = 2, 4` (D1, D2). ATTEMPTED.

Scope left open:
- maps that exchange the parities other than `εT`;
- `q = Q`;
- the projected sea.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The perturbation theory for the gapped sea is a named import.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 70, 71, 76, 77 (landed) | maps, twins, the sea, the clocked massive walk | yes (quoted and checked, A3) |
| block 55 (landed) | the energy density | yes (restated) |
| probe #9210 and referee #9295 | the result and its confirmation | yes (ported, rerun) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "twins, the sea's density, kappa(m) > 0, the visible chessboard" | executed: operator identities on the 4^3 torus | executed: twin densities site by site | executed: block algebra, overlaps, weight, bounds | executed: moments, series, enclosures; chessboard | not executed: brute-force diagonalization; `q = Q`; projected sea |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "`κ > 0` is obvious from a positive integrand."
  - *Reply:* The integrand is the held sea's. The free sea differs from it, and T2(b)'s bound is what makes the formula exact at order `|q|²`.
  - The chessboard statement T4 goes beyond block 76 T1, which is for the massless walk. With a mass the zero mode is gone, because the rest term scales with the clock rate.

### N8 — Cross-cycle echo
- Block 76: a chessboard of clocks is invisible, and `c`, `κ` are inputs.
- Block 77: the mass.
- This note: with a mass, `c₀`, `κ` are derived, and the chessboard is visible.

## Falsifiers

- A mass at which `κ(m) ≤ 0`.
- A site where `e_x^sea ≠ mε_x − ⟨E⟩` at uniform clocks.
- A map that keeps `ε` and is a twin.

## Boundaries and non-claims

- The free (unprojected) sea.
- `2q` not `0` or `Q`.
- Second-order perturbation theory for the gapped sea.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 55, 70, 71, 76 and 77 (landed), restated and quoted.
- Named standard imports, at definition level:
  - second-order perturbation theory for a gapped finite matrix;
  - bracketing by alternating series;
  - exact arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9210 (Claude Opus 5.5) found the result.
  - #9295 (a Grok worker, another family) refereed it with its own checker: confirmed partial, with the floating-point averages not rebuilt.
  - The supervisor ported the exact families and dropped the floating-point ones.
- **Before writing.** The own prior-art check covered memory, open PRs and main. It found blocks 76 and 77 with their deferrals, and no earlier harvest.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_massive_free_sea_keeps_a_positive_clock_stiffness_for_every_mass_2026_09_26.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
