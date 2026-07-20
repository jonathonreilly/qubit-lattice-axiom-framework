# KCPT chiral parity: total complex-structure sign reversal and the common-sign orbit

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the full `4^3` staggered lattice `C^64`, its antisymmetric integer adjacency `D2`, the corner-wave kernel frame `V8`, and the bulk operator `M = D2 @ D2`. It introduces the staggered chiral parity `S_eps = diag((-1)^{x_1 + x_2 + x_3})`, a real involution, and proves the parent note's total complex-structure sign reversal, `S_eps J_full S_eps = -J_full`, by a single linear lattice symmetry — a different realization in kind from the parent note's antilinear entrywise conjugation `K`, which fixes the real `J_full`. This is not a reversal of the real orientation on `R^64`: the complex dimension is `32`, so `J_full` and `-J_full` induce the same real orientation. It proves `S_eps` is not a member of the ambient group `G_amb`, that it extends the group to `H = <G_amb,S_eps>` of order `1536`, and that the exact `H`-orbit of `J_full` is `{J_full,-J_full}`. Consequently the specific sibling `J_alt = J_ker-J_bulk` is not in that orbit. This does not classify a free binary: the parent sign family has `16` sign tuples and `8` relative-sign classes after quotienting by common sign, represented by `(e_ker e_1,e_ker e_2,e_ker e_3) in {+1,-1}^3`. The theorem exhausts only the explicitly generated finite group `H`, not a larger normalizer or all automorphisms. Established with exact integer arithmetic for every load-bearing identity; each floating-point gate is tagged `[FLOAT SANITY]` and redundant. It fixes no free parameter, selects no complex-structure sign, chooses no dynamics, and forces nothing pre-record; it is r-neutral and measure-neutral (`S_eps` commutes with `M` and makes no weight or probability claim). It has no external numerical or literature input; its five linked internal authorities remain explicit dependencies. It is a positive structural sharpening of the parent note's T5 boundary, not a selection of any sign member.

## Setting

The surface is the one delivered in [the corner-carrier delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph whose antisymmetric integer adjacency `D2` carries an eight-dimensional kernel spanned by the corner waves `V8`. That note states `D2` has exact rank `56`, so the kernel dimension is eight. Its lattice symmetries are the ones named in [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md) — `standard translations, and proper cubic rotations` — dressed by the staggered sign fields.

[The kernel note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) reads the kernel block: the central complex structure whose exact commutant over the rationals is two-dimensional, `span{I, j}`, lifted to the whole space through `V8` as the real antisymmetric operator `J_ker`, supported on the `m = 0` shell. [The ambient isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) assembles the dressed symmetries into the ambient group `G_amb` of order `768`, the `D2`-commuting closure that fixes the kernel and bulk blocks separately.

[The parent total-complex-structure note](KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md) sums these pieces into a single operator on all of `C^64`, the assembly `J_full = J_ker + J_bulk`, proves it squares to `-I_64` for a purely rational reason, and proves it commutes with `G_amb`. Its T5 boundary records that the assembly selects no orientation and that `the upstream kernel sign remains open separately`, with the sibling assembly `J_alt = J_ker - J_bulk` carrying the opposite bulk sign.

This note takes one move the parent leaves on the table: the parent exhibits the assembly and its ambient symmetry while retaining three independent bulk-shell signs and a separate kernel sign. This note supplies a linear lattice symmetry that reverses the whole assembly and computes the orbit of one sign tuple under the explicitly generated finite group `H`. It does not exhaust transformations outside `H` or collapse the full relative-sign quotient. The bounded theorem has six parts.

## T1 — the staggered chiral parity

Define the staggered chiral parity — the site-parity grading —

`S_eps = diag((-1)^{x_1 + x_2 + x_3})`,

the diagonal sign operator that reads the site parity. It is a real involution: its diagonal entries lie in `{-1, +1}`, it squares to the identity, `S_eps^2 = I`, and it is traceless, `tr S_eps = 0`, an equal split of the `64` sites into the two parities. Against the adjacency it is chiral: it anticommutes, `S_eps D2 S_eps = -D2`. Against the bulk operator it commutes, `S_eps M S_eps = M`, because `M = D2 @ D2` is quadratic in the adjacency and the two sign flips cancel; consequently it fixes every drop-one polynomial `Q_m` and every normalized spectral projector `P_m = Q_m/N_m`, `S_eps Q_m S_eps = Q_m`, for the four Hamming shells. A rejector confirms the anticommutation is genuine — `S_eps D2 S_eps != +D2` — so the minus sign is real and not an artifact of an operator that merely commutes.

## T2 — kernel-block reversal

The crux is that the chiral parity reverses the kernel structure,

`S_eps J_ker S_eps = -J_ker`.

The mechanism is combinatorial. On the corner frame the chiral parity acts as a permutation of the eight corner waves, `S_eps V8 = V8 Pi`, where `Pi` is the corner-wave complementation that sends a subset `S` of `{0, 1, 2}` to its complement `S^c`; it is an involution, `Pi^2 = I`. Under complementation the kernel monomial flips sign, `Pi J64 Pi^T = -J64`, because `sign(S^c) = -sign(S)` for every one of the eight corner subsets. Lifting that flip through `V8` gives `S_eps J_ker S_eps = -J_ker`. A rejector confirms `S_eps` does not fix `J_ker`.

## T3 — bulk-block reversal

Each integer bulk carrier `A_m = D2 Q_m`, for `m = 1, 2, 3`, reverses under the chiral parity,

`S_eps A_m S_eps = -A_m`,

and therefore so does their sum, `S_eps J_bulk S_eps = -J_bulk`. The mechanism is the product rule of T1: in `A_m = D2 Q_m` the adjacency `D2` flips sign while the drop-one polynomial `Q_m` is fixed, so the product flips. A rejector confirms `S_eps` does not fix `A_1`.

## T4 — total linear complex-structure sign reversal, contrasted with the antilinear conjugation

Every additive piece of the assembly flips — `J_ker` by T2 and each `A_m` by T3 — so the whole operator reverses,

`S_eps J_full S_eps = -J_full`,

the exact statement. This is the linear lattice realization of the complex-structure sign reversal `J -> -J`, and it is distinct in kind from the parent note's global entrywise conjugation `K`. It is not a real-orientation reversal: on `R^64` the complex dimension is `32`, so the induced orientations of `J` and `-J` differ by `(-1)^32 = +1`. The conjugation `K` is antilinear and fixes the real `J_full`, because coordinate conjugation of a real matrix returns it unchanged, whereas the linear `S_eps` negates it. The contrast is concrete on the imaginary unit `i I`: the antilinear `K` conjugates `i`, sending `i I -> -i I`, while the linear `S_eps` preserves it, `S_eps (i I) S_eps = i S_eps^2 = +i I` — the two conjugations act oppositely, one through the coefficients and one through the lattice. The same `S_eps` also reverses the sibling assembly, `S_eps J_alt S_eps = -J_alt`.

## T5 — the extended group and the sign-lock census

The chiral parity is not a member of the ambient group: `S_eps` anticommutes with `D2`, so it lies outside the `D2`-commutant that defines `G_amb`. But it normalizes the group — `S_eps g S_eps` is again in `G_amb` for all `768` members — so the group it generates together with `G_amb` is exactly `G_amb` together with the single coset `S_eps G_amb`. The two cosets are disjoint, and `<G_amb, S_eps>` has order `1536 = 2 * 768`.

On this order-`1536` group the two blocks move together. For every element `h`, both `h J_ker h^T` and `h A_1 h^T` return plus-or-minus the original, and the two signs always agree: the kernel-block orientation and the bulk-block orientation carry the same sign, both `+1` or both `-1`. The census is clean — exactly `768` elements, the `G_amb` coset, fix `J_full`, and exactly `768`, the `S_eps` coset, send `J_full` to `-J_full`.

## T6 — the exact common-sign orbit and the eight-class boundary

Because every one of the `1536` elements of `H` locks the kernel sign to all three bulk-shell signs, the coefficient image on `(e_ker,e_1,e_2,e_3)` is exactly `{(+,+,+,+),(-,-,-,-)}`. Therefore

`orbit_H(J_full) = {J_full,-J_full}`.

The sibling `J_alt = J_ker-J_bulk`, with coefficient tuple `(+,-,-,-)`, is not in this orbit. The matrix distinctions are exact: `J_full-J_alt = 2J_bulk != 0` and `-J_full-J_alt = -2J_ker != 0`.

This two-element orbit is not the full relative-orientation space. The parent construction permits `16` sign tuples `(e_ker,e_1,e_2,e_3)`. Quotienting by the common flip leaves `8` relative classes, represented by the three invariants `(e_ker e_1,e_ker e_2,e_ker e_3)`. `J_full` and `J_alt` occupy two of those eight classes; the other six are neither classified nor excluded here. Likewise, no claim is made about a larger normalizer or transformations outside `H`. The result selects no orientation. The record-registration question of which relative class a realized stack carries remains outside this note.

## What the runner checks

The paired runner `scripts/kcpt_chiral_parity_common_sign_orbit_2026_07_19.py` verifies the blocks below.

| Block | What it checks | Gates |
|-------|----------------|-------|
| B0 | verbatim source-quote greps into the five dependency notes, including the upstream `J64` action and normalization, plus exactly five dependency links once each in this note | 9 |
| B1 | surface anchor: `D2` antisymmetry and entries, exact rank `56` by a modular lower bound plus eight independent null vectors, `V8` orthogonality and `D2 V8 = 0`, `J64 J64 = -64^2 I_8`, an independently expanded upstream monomial/lift witness, the exact translation identity with Fourier-character spectrum counts `{0:8,-4:24,-8:24,-12:8}`, and `A_0 = 0` with `A_1,A_2,A_3` nonzero | 7 |
| B2 | `S_eps` is a real involution: diagonal `+-1`, `S_eps^2 = I`, traceless, staggered-sign form | 4 |
| B3 | chiral action: `S_eps D2 S_eps = -D2`, `S_eps M S_eps = M`, `S_eps Q_m S_eps = Q_m`, anticommutation rejector | 4 |
| B4 | kernel reversal: `S_eps J_ker S_eps = -J_ker`, rejector, `S_eps V8 = V8 Pi`, `Pi^2 = I`, `Pi J64 Pi^T = -J64`, `sign(S^c) = -sign(S)` | 6 |
| B5 | bulk reversal: `S_eps A_m S_eps = -A_m`, rejector | 2 |
| B6 | total linear reversal: exact all-pieces-flip, the linear/antilinear contrast on `i I` (labelled structural), float confirmation `S_eps J_full S_eps = -J_full` and `S_eps J_alt S_eps = -J_alt` | 3 |
| B7 | extended group: `S_eps` not in `G_amb`, `S_eps` normalizes `G_amb`, order `1536` disjoint cosets, sign-lock, census `768`/`768` | 5 |
| B8 | exact orbit boundary: `J_alt != +/-J_full`, coefficient image equal to the common sign, `16` sign tuples giving `8` relative classes, and a redundant float confirmation that all sixteen sign-members square to `-I_64` | 5 |

## Honest auditor read

This note reads the structure of a fixed finite symmetry action: a single real involution `S_eps` on `C^64` and the order-`1536` group `H` it makes together with the ambient symmetry. It is not a dynamical selection, not a measurement, and not a probability-weight derivation. It fixes no free parameter and derives no `r`; it is r-neutral and measure-neutral because `S_eps` commutes with the bulk operator `M`. Its internal dependencies are the five linked notes; it uses no external numerical, fitted, observational, or literature input. It selects no orientation. What it establishes is only the exact common-sign orbit of `J_full` inside `H`; it explicitly preserves the parent's eight-class relative-sign quotient and leaves transformations outside `H` open. It is a finite fixed-surface statement on the `L = 4` torus; no continuum or infinite-volume claim is made, no Hamiltonian or admissibility dynamics is chosen, no physical identification is asserted, and nothing pre-record is forced.

## No-Go Discipline Gate for the narrow outside-orbit corollary

The sentence “`J_alt` is outside `orbit_H(J_full)`” is a derived negative boundary inside this positive finite-group theorem. It is not a claim about all automorphisms, all lattice symmetries, or all orientation-selection mechanisms. The N1–N8 stress test is recorded here so the narrow corollary is not mistaken for a broader no-go.

### N1 — five distinct attacks

1. **ATTEMPTED — full matrix orbit enumeration.** Conjugate `J_full` by each of the `1536` exact signed-permutation matrices. The resulting orbit has exactly the two matrices `+/-J_full`, neither equal to `J_alt` (B7.5, B8.1–B8.3).
2. **ATTEMPTED — generator-word action.** Every generator inherited from `G_amb` fixes the kernel and bulk-shell pieces, while `S_eps` flips every piece. Induction on words therefore supplies only a common sign and cannot produce the tuple `(+,-,-,-)` (B4.1, B5.1, B7.4).
3. **ATTEMPTED — two-coset normalizer decomposition.** Exact normalization gives `H = G_amb union S_eps G_amb`; the first coset fixes `J_full` and the second negates it. The terminal coset calculation exhausts `H` without relying on a numerical orbit tolerance (B7.2–B7.5).
4. **ATTEMPTED — shell-projection separation.** `H` preserves the drop-one polynomials `Q_m` and hence the normalized spectral projectors `P_m = Q_m/N_m`; restricting the conjugation action independently to the kernel shell and each nonzero bulk carrier gives equal signs on every shell. `J_alt` has the opposite kernel-versus-bulk pattern (B3.3, B5.1, B7.4).
5. **ATTEMPTED — coefficient-sign representation.** The induced action of `H` on `(e_ker,e_1,e_2,e_3)` has image exactly `{(+,+,+,+),(-,-,-,-)}`. The tuple of `J_alt` is `(+,-,-,-)`, so it is absent from that exact image (B8.3–B8.4).

These routes differ in primary object and terminal obligation: full `64 x 64` orbit matrices, generator words, group cosets, spectral-shell restrictions, and the four-sign coefficient representation.

### N2 — wall independence

No multiple physical walls are claimed. “Fixed `L=4` surface” and “membership in the explicitly generated group `H`” are domain restrictions of one theorem, not independent open conditions.

### N3 — hidden-wall scan

The load-bearing restrictions are explicit: the surface is fixed, the exhausted group is exactly `H`, and no larger normalizer or full-automorphism search is claimed. The construction language does not import an unlisted dynamical or physical premise.

### N4 — residual matching

The parent residual is the independent sign family with one kernel sign and three bulk-shell signs. This note retains that exact residual as `16` tuples modulo common sign, hence `8` classes. It closes only the `H`-orbit of the all-plus representative and cites no prior no-go as evidence that the other six relative classes are excluded.

### N5 — rhetoric and resolution

The runner tests the claim per group element, per kernel/bulk shell, per coefficient tuple, and for the full finite lattice matrix. It does not test other lattice sizes, a continuum limit, transformations outside `H`, or a selection dynamics; the prose makes no negative claim at those resolutions.

### N6 — partial-closure paths

No new-axiom boundary is asserted. Record registration or a dynamical selector could choose a relative class, but that question is deliberately outside this finite group-action theorem and is not declared impossible.

### N7 — steelman

The strongest objection to a broad no-go is decisive: a transformation in a larger normalizer or full automorphism group might act with unequal shell signs and connect `J_full` to `J_alt`; the parent already exposes eight relative classes. That objection defeats any claim beyond `H`, so this note makes none. It does not defeat the narrow statement because the exact enumeration and coset proof exhaust every member of `H`.

### N8 — cross-cycle echo

The immediate parent is the controlling echo: it warns that `J_alt` is one member of the independent bulk-shell sign family, not an extra exhaustive binary. This note incorporates that correction explicitly through the `16/2=8` quotient and confines its negative corollary to the computed two-element `H`-orbit.

**No-Go Discipline disposition:** `PASS` for the narrow finite-group outside-orbit corollary; no broader no-go ships.

A final line: the [paired runner](../scripts/kcpt_chiral_parity_common_sign_orbit_2026_07_19.py) rebuilds `D2`, `V8`, `M`, the drop-one polynomials `Q_m`, the normalized projectors `P_m`, the carriers `A_m`, the kernel lift `J_ker`, the chiral parity `S_eps`, the regenerated `768`-member `G_amb` and its order-`1536` chiral extension, and the sibling `J_alt`; all load-bearing gates are exact integer, every floating-point gate is tagged `[FLOAT SANITY]`, and the runner prints `TOTAL: PASS=N FAIL=0` and exits nonzero on any failure. Its cached output belongs at `logs/runner-cache/kcpt_chiral_parity_common_sign_orbit_2026_07_19.txt`.
