---
claim_id: admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied smooth continuum coframe scalar-density functional with scalar log rate, coordinate invariance yields the stated differential identity among variational derivatives. Coupled static equations imply the exact covariant stress balance as a necessary consistency condition, not a dynamical force law or existence theorem. Separately, the finite clocked identity-frame lattice walk obeys the exact commutator and bond-current momentum balance with the stated nonlocal force density. In the smooth-amplitude, smooth-rate small-spacing expansion its leading force equals energy density times log-rate difference. No exact arbitrary-packet energy-times-gradient law is inherited from the earlier phase note. Curl-only discrete energies invariant under strain gradients at fixed site rates instead require divergence-free strain response and cannot accommodate the specified nonzero stationary lattice force without further structure."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_2026_09_21.py
---

# Continuum variational stress balance and the clocked walk's distinct exact lattice momentum identity

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (an exact continuum identity of block 60's and 64's supplied ledger, and exact lattice identities of block 54's supplied clocked walk; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a ledger linear in the rates built from the strains of a frame; it reports an identity of such a ledger and the exact momentum balance of the clocked walk, and that the two agree; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Two different identities are established. A coordinate-invariant continuum frame functional has a variational identity. Substitution of static field equations gives a necessary covariant stress balance. It does not derive arbitrary-packet dynamics, unique matter sources or static existence.

The clocked lattice walk separately has an exact bond-current momentum identity. Its force density contains weighted hops, and equals energy density times the log-rate difference only at leading order for smooth rates and smooth amplitudes. The earlier claim of an exact universal packet-force law has been withdrawn in the corrected phase note and is not an input here.

The author's 2026-09-23 continuum/lattice corrigendum is incorporated with a precise boundary: a discrete energy depending on B only through its additive curls is invariant under B->B+d xi even with arbitrary fixed rate weights. Its strain equations have zero divergence. Combining that with the stationary walk identity requires f=0, so it cannot accommodate a source with nonzero f. Inverse-frame contractions depending explicitly on B are not automatically in this curl-only class. A full lattice realization of the continuum carried-rate identity is still missing.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 55, 60, 63, 64 (open PRs) supply everything else.

- **Domains and boundary terms.** The continuum coframe is smooth and invertible with positive determinant; coordinate variations are compactly supported or boundary terms vanish. Lattice identities use finite tori or local finitely supported data, with suitable domains for summed infinite-lattice expectations. G_xi is time independent.
- **Clocked walk.** `H_w = φHφ`, `H = Σ_a σ_a S_a`, `φ = √w`, `u = log w`. **Energy density** `𝔢(x) = Re ψ†(x)(H_wψ)(x) = ∂⟨H_w⟩/∂u_x` (block 55).
- **Relabelling** `G_ξ = ½Σ_j{ξ_j, S_j}`; **bond current** `J_a^j[χ]` of a state `χ` (block 63); **symmetric hop** `C_j[v]` weighted by a bond function `v`; `d_jφ = φ(x + e_j) − φ(x)`.
- **Carried rate** `Λ_ξ = ½Σ_j{ξ_j, C_j[d_jφ]}`. **Force density** `f_j(x) = Re[(C_j[d_jφ]ψ)†(Hφψ) + ψ† C_j[d_jφ](Hφψ)](x)`.
- **Ledger** `F = ∫ e^{u} D(e)`, `D` a member of block 64's family for the frame `e = 1 +` strain; `E_j^a = δF/δe^j_a`, `U = δF/δu`. **Content's response** `𝒥_j^a = ∂⟨H⟩/∂e^j_a`; to first order it is minus block 63's bond current.

That the invariance of a field's energy under relabellings gives an identity among its field equations, and that with the rate of clocks as a multiplier this identity ties the divergence of the spatial equations to the constraint times the gradient of the rate, is Noether's second theorem applied to the formulation of Arnowitt, Deser and Misner; that the equations of motion of the content then follow from the field equations is the observation of Einstein and Grommer and of Infeld and Hoffmann. The balance of a stress gradient against weight is the hydrostatic equation. None is used as authority.

## Prior art and what is new

The bounded content is a continuum variational identity, an exact discrete commutator identity and their stated leading-order comparison. No removal of a supplied physical premise or derivation of a universal force law follows.

## Theorem T1 — the field's identity

*Statement.* Let `F = ∫ e^{u} D(e)` with `D` a member of block 64's family. Then for `b = 1, 2, 3`: `E_j^a ∂_b e^j_a − ∂_a(E_j^a e^j_b) + U ∂_b u = 0`, identically in `e` and `u`.

*Proof.* Each term of `D` is a scalar density under `x → x + ξ(x)`: the coin index is inert, the bond indices are contracted with the frame and its inverse, `det e` is a density, and `∂_b(det e V^b)` is the divergence of a vector density. `e^u` is a scalar if `u` is carried along. So `F` is unchanged under `δe^j_a = ξ^b∂_be^j_a + e^j_b∂_aξ^b`, `δu = ξ^b∂_bu`; inserting these variations and integrating by parts gives the identity, `ξ` being arbitrary. The runner checks it through second order in the fields for three members (C1 and the refuting pass), and that the expression without `U∂_bu` does not vanish. ∎

## Theorem T2 — the fall is owed

*Statement.* Let a content with energy `⟨H⟩[e, u]` be coupled through the ledger `⟨H⟩ + F`, stationary in `u` and in `e`: `𝔢 + U = 0`, `𝒥_j^a + E_j^a = 0`. Then `∂_a(𝒥_j^a e^j_b) − 𝒥_j^a ∂_b e^j_a = 𝔢 ∂_b u`. For an exactly identity coframe the expression reduces to `∂_a 𝒥_b^a = 𝔢 ∂_b u`. For a perturbed coframe the displayed full expression must be kept: products of stress with strain gradients can be of the same order as energy times rate gradient, so dropping them is not justified by weak fields alone.

*Proof.* Substitute into T1. ∎

This is a necessary condition on a supplied stationary coupled solution. A nonzero right side cannot be balanced by a vanishing full covariant left side. It does not imply a time-evolution law for a free packet, pairwise action and reaction in every geometry, or a unique source density from energy conservation alone. Zero gradients, vanishing sources and extra stresses are allowed exceptional cases.

## Theorem T3 — the walk's own law, exactly

*Statement.* For every state, rate field and real displacement `ξ`: (a) `i[φ, S_j] = −C_j[d_jφ]`; (b) `i[H_w, G_ξ] = φ(i[H, G_ξ])φ − (Λ_ξ Hφ + φH Λ_ξ)`; (c) `d⟨G_ξ⟩/dt = Σ_{a,j,x}(d_aξ_j)(x) J_a^j[φψ](x → x + e_a) − Σ_{j,x} ξ_j(x) f_j(x)`; (d) if `ψ` is stationary for `H_w`, `Σ_a[J_a^j[φψ](x → x + e_a) − J_a^j[φψ](x − e_a → x)] = −f_j(x)` at every site; (e) for uniform `ξ`, the total lattice momentum changes at minus the total force.

*Proof.* (a) As in block 65 T1: `[φ, S_j]ψ(x) = (1/(2i))[(φ(x) − φ(x + e_j))ψ(x + e_j) − (φ(x) − φ(x − e_j))ψ(x − e_j)]`. (b) `[φHφ, G] = φ[H, G]φ + [φ, G]Hφ + φH[φ, G]` and `i[φ, G_ξ] = ½Σ_j{ξ_j, i[φ, S_j]} = −Λ_ξ`. (c) The first term is block 63 T2(b) for the state `φψ`; the second is `−2 Re⟨Λ_ξψ|Hφψ⟩`, and `Λ_ξ` is hermitian with real weights, which gives `f`. (d) `⟨ψ|[H_w, G]|ψ⟩ = 0`; summation by parts. (e) `dξ = 0`. ∎

A relabelling carries the rates along, as T1 assumes — but on the lattice what it makes of a rate is not a rate: it is the hop `Λ_ξ`. That is why T1 has no exact lattice form here, while T3 is exact.

## Theorem T4 — the smooth small-spacing comparison

*Statement.* On a line with lattice spacing `h`, for smooth `φ` and a smooth complex amplitude, `f = 𝔢 · (u(x + h) − u(x))` at the leading order in `h` (both sides begin at order `h²`). Hence, by T3(d), stationary states of the clocked walk have a bond current whose divergence is minus their weight at leading order, which with `𝒥 = −J` is T2's requirement.

*Proof.* Expansion (runner D1): `C_j[d_jφ] → hφ'`, so `f → 2hφ' Re ψ†Hφψ = h(2φ'/φ)𝔢`. ∎

For a finite carrier wave number, lattice momentum is sin(k), so a semiclassical momentum change brings a cosine factor. This is not an exact pointwise formula for arbitrary fields or packets. The canonical comparison proved here is the smooth small-spacing limit. It does not restore the earlier universal phase-force assertion.

## Historical experiments — deferred

Original numerical packet evolution, stationary diagonalizations and additional continuum parameter examples remain recoverable on the original PR branch. They have not been re-executed for this landing. Exact finite rational identities and the explicitly truncated symbolic checks are the canonical evidence.

## No-Go Discipline Gate

The note's negative sentences: without the rates' term the identity fails; a rate field can exchange lattice momentum with the walk; a nonzero weight cannot coexist with a vanishing full covariant stress divergence in the stated static system; T1 has no exact lattice form here.

### N1 — Routes by which the sentences could fail
1. *A field energy not linear in the rates.* Blocks 55 and 56's ledgers are functions of the rates alone; they have no strains whose equations could be inconsistent, and the matching of pulls had to be argued separately (block 55 T3). T2 is a statement about ledgers of block 60's kind.
2. *A content that is not timed by the rates it sources.* T2 constrains the actual variational derivatives in the supplied static model. It does not classify every possible content coupling or exclude all alternative source conventions.
3. *The lattice.* The two sides agree at leading order in the wave vector. Beyond that the field's side has no unique lattice form (block 64 N1.3) and the content's side has the hop `Λ_ξ` in place of a carried rate; whether some lattice ledger has T3's exact force density on its right-hand side is the named next step.
4. *Non-static situations.* T2 is a statement about the static equations. With kinetic terms for the strains the identity acquires their momenta; not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T1 continuum; checked through second order in the fields. T2 static. T3 identity frame for the walk's coin, arbitrary positive rates. T4 one dimension, one coin component, leading order; the three-dimensional statement is the same computation along each axis.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra; the absences that motivate the clauses | yes (premise) |
| block 54 (open PR #8570) | the clocked walk; its corrected ray and packet scope | yes (restated) |
| block 55 (open PR #8571) | the energy density as the source; matched pulls | yes (restated) |
| blocks 60, 64 (open PRs #8590, #8595) | the ledger linear in the rates; the family of densities | yes (restated) |
| block 63 (open PR #8593) | the relabelling, the bond current | yes (restated) |
| block 65 (open PR #8596) | the commutator of a site function with `S_j` | restated |
| decision record (open PR #8572) | clauses B and C; the open item | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the ledger's identity; the content's stress gradient must equal its weight; the clocked walk's exact momentum balance and force density; agreement at leading order" | executed: `i[φ, S_j]` at all 60 sites of a `5×4×3` torus | executed: `i[H_w, G_ξ]` against its decomposition at all 60 sites; the force density site by site | executed: the identity through second order in nine strain functions and the log rate for two members | executed: `d⟨G_ξ⟩/dt` against current term minus force term; total momentum against total force; force density against weight at leading order in the lattice spacing | T1 every frame and rate field; T2 every content coupled through such a ledger; T3 every state, rate field and displacement; T4 leading order; the ledger, the strains, the relabellings and the clocked walk supplied; no exact lattice form of T1 |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Strongest objections
Static compatibility does not determine evolution. The full coframe terms cannot be dropped at the same perturbative order as the proposed weight. The lattice curl-only identity has a different transformation law from the continuum one; no exact coupled lattice theory has been supplied.

### N8 — Earlier claims
The phase note's exact universal force assertion and the general conservation-implies-source assertion are not used. The correct inputs are the selected Hermitian clocked generator and explicitly supplied variational equations.

## Falsifiers

- A member of block 64's family, a frame and a rate field violating T1 at second order.
- A state, rate field and displacement violating T3(b) or (c); a stationary state of `H_w` with `div J[φψ] + f ≠ 0` at some site.
- A smooth amplitude and rate field with `f ≠ 𝔢 du` at leading order in the lattice spacing.

## Boundaries and non-claims

The field functional, matter generator, frame and transformations are supplied. The continuum identity and discrete momentum identity are individually exact under their stated domains, but their comparison is a leading smooth limit. The curl-only fixed-rate lattice obstruction above is conditional, not a no-go for every inverse-frame discretization. No universal force, unique source rule, static existence or dynamical stability is claimed.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 55, 60, 63, 64, 65 and the decision record (PRs #8570, #8571, #8590, #8593, #8595, #8596, #8572, open): restated or placed.
- Named standard imports at definition level: invariance of an integral of a scalar density under a change of coordinates; variational derivatives with second derivatives; commutators with shifts; summation by parts; expansions in a lattice spacing.
- Reference only: Noether; Arnowitt, Deser and Misner; Einstein and Grommer; Infeld and Hoffmann.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8571](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8590](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8593](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8595](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8596](ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author material and the 2026-09-23 corrigendum are preserved at PR #8597 head `c4afb022c22e1f4e677675fab6326b0f839e55e3`, branch `physics-loop/admissibility-induced-law-block66-the-fall-is-owed-by-the-ledger-20260921`. Landing review keeps the exact identities, removes reliance on the earlier universal packet-force claim, and separates static compatibility, continuum approximation and the discrete curl-only obstruction. Auxiliary evidence remains deferred; no audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
