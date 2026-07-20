# KCPT chiral parity: total complex-structure sign reversal and the aligned-block relative sign

Date: 2026-07-19

**Type:** bounded_theorem

**Claim boundary:** This is a bounded theorem on one fixed finite surface — the full `4^3` staggered lattice `C^64`, its antisymmetric integer adjacency `D2`, the corner-wave kernel frame `V8`, and the bulk operator `M = D2 @ D2`. It introduces the staggered chiral parity `S_eps = diag((-1)^{x_1 + x_2 + x_3})`, a real involution, and proves that `S_eps` reverses the parent note's total complex-structure sign, `S_eps J_full S_eps = -J_full`, by a single linear site-parity grading — a different realization in kind from the parent note's antilinear entrywise conjugation `K`, which fixes the real `J_full`. Here the lane's orientation-sign language means the `J <-> -J` two-presentation switch; it is not a reversal of the real orientation induced on `R^64`, because the complex dimension is `32` and `J_full` and `-J_full` induce the same real orientation. The theorem proves `S_eps` is not a member of the ambient group `G_amb`, that it extends the group to order `1536`, and that every member preserves the relative kernel/common-bulk sign. Thus, within the aligned-bulk pair `{J_full, J_alt}`, no member maps `J_full` to `J_alt`; the parent's full sixteen-member independent block-sign family remains and is not reduced to one binary. Established with exact integer arithmetic only; every floating-point gate is tagged `[FLOAT SANITY]` and is redundant — every load-bearing identity is carried by an exact integer gate. It fixes no free parameter, selects no `J`-sign, chooses no dynamics, and forces nothing pre-record. It is r-neutral because `r` never enters, and measure-neutral because it introduces no measure, weight, or probability rule; `S_eps` additionally commutes with the bulk operator `M`. It has no measured, fitted, literature, observational, normalization, or dynamical input beyond the five linked structural dependencies; `S_eps` itself is built from native site coordinates. This is a positive structural sharpening of the parent note's T5 boundary, not a selection of any sign member.

## Setting

The surface is the one delivered in [the corner-carrier delivery note](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md): the staggered `4^3` Dirac graph whose antisymmetric integer adjacency `D2` carries an eight-dimensional kernel spanned by the corner waves `V8`. That note states `D2` has exact rank `56`, so the kernel dimension is eight. Its lattice symmetries are the ones named in [the minimal-axioms note](MINIMAL_AXIOMS_2026-06-29.md) — `standard translations, and proper cubic rotations` — dressed by the staggered sign fields.

[The kernel note](KCPT_KERNEL_INDUCED_REPRESENTATION_CENTRAL_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-18.md) reads the kernel block: the central complex structure whose exact commutant over the rationals is two-dimensional, `span{I, j}`, lifted to the whole space through `V8` as the real antisymmetric operator `J_ker`, supported on the `m = 0` shell. [The ambient isolation note](KCPT_AMBIENT_LATTICE_SYMMETRY_KERNEL_ISOLATION_AVERAGED_COMPLEX_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-19.md) assembles the dressed symmetries into the ambient group `G_amb` of order `768`, the `D2`-commuting closure that fixes the kernel and bulk blocks separately.

[The parent total-complex-structure note](KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md) sums these pieces into a single operator on all of `C^64`, the assembly `J_full = J_ker + J_bulk`, proves it squares to `-I_64` for a purely rational reason, and proves it commutes with `G_amb`. Its T5 boundary records that the assembly selects no orientation and that `the upstream kernel sign remains open separately`, with the sibling assembly `J_alt = J_ker - J_bulk` carrying the opposite bulk sign.

The parent exhibits the assembly and its ambient symmetry but leaves all four block signs open: one kernel sign and three independent bulk-shell signs. This note supplies the linear site-parity grading that reverses the whole assembly, and it measures the action on the aligned-bulk comparison `J_full` versus `J_alt`. The bounded theorem has six parts.

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

the exact statement. This is the linear site-parity realization of the complex-structure sign reversal `J -> -J`, and it is distinct in kind from the parent note's global entrywise conjugation `K`. It is not a real-orientation reversal: a complex structure on `R^64` has complex dimension `32`, so changing `J` to `-J` changes the induced orientation by `(-1)^32 = +1`. The conjugation `K` is antilinear and fixes the real `J_full`, because coordinate conjugation of a real matrix returns it unchanged, whereas the linear `S_eps` negates it. The contrast is concrete on the imaginary unit `i I`: the antilinear `K` conjugates `i`, sending `i I -> -i I`, while the linear `S_eps` preserves it, `S_eps (i I) S_eps = i S_eps^2 = +i I` — the two conjugations act oppositely, one through the coefficients and one through the lattice. The same `S_eps` also reverses the sibling assembly, `S_eps J_alt S_eps = -J_alt`.

## T5 — the extended group and the sign-lock census

The chiral parity is not a member of the ambient group: `S_eps` anticommutes with `D2`, so it lies outside the `D2`-commutant that defines `G_amb`. But it normalizes the group — `S_eps g S_eps` is again in `G_amb` for all `768` members — so the group it generates together with `G_amb` is exactly `G_amb` together with the single coset `S_eps G_amb`. The two cosets are disjoint, and `<G_amb, S_eps>` has order `1536 = 2 * 768`.

On this order-`1536` group the two blocks move together. For every element `h`, both `h J_ker h^T` and `h A_1 h^T` return plus-or-minus the original, and the two signs always agree: the kernel-block orientation and the bulk-block orientation carry the same sign, both `+1` or both `-1`. The census is clean — exactly `768` elements, the `G_amb` coset, fix `J_full`, and exactly `768`, the `S_eps` coset, send `J_full` to `-J_full`.

## T6 — the aligned-bulk relative-sign comparison

Because every one of the `1536` lattice-and-chiral group elements locks the kernel sign equal to the common bulk sign, none reaches the sibling `J_alt = J_ker - J_bulk`, which carries opposite kernel and common-bulk signs. Thus, within the aligned-bulk two-member comparison `{J_full, J_alt}`, the relative kernel/common-bulk sign is invariant under `<G_amb,S_eps>`. The two are invariant-distinct, `J_full - J_alt = 2 J_bulk != 0` and `-J_full - J_alt = -2 J_ker != 0`, both nonzero, so `J_alt` is not in the group orbit `{+J_full,-J_full}`. This does not exhaust the parent's sign freedom: its independent kernel and three bulk-shell signs give sixteen sign members, and the present group orbit reaches two of them, leaving eight group-inequivalent pairs modulo overall sign. Nor does finite-group non-reachability assert physical freedom against a larger symmetry, readout, or dynamics.

This is the positive sharpening of the parent note's boundary. It names exactly which sign the order-`1536` group changes — the overall `J`-sign — and which sign it preserves — the relative kernel/common-bulk sign in the aligned-bulk comparison. It selects no sign member. The next path this opens is the record-registration question of which relative sign a realized stack carries, which is outside this note's claim.

## What the runner checks

The paired runner `scripts/kcpt_chiral_parity_orientation_reversal_relative_binary_2026_07_19.py` verifies the blocks below.

| Block | What it checks | Gates |
|-------|----------------|-------|
| B0 | verbatim source-quote greps into the five dependency notes, plus exactly five dependency links once each in this note | 8 |
| B1 | surface anchor: `D2` antisymmetry and entries, exact rank `56` by a modular lower certificate plus eight independent integer null vectors, `V8` orthogonality and `D2 V8 = 0`, `J64 J64 = -64^2 I_8`, integer kernel lift, exact integer projector resolution of the `M = 2(T_200 + T_020 + T_002) - 6 I` spectrum, `A_0 = 0` with `A_1,A_2,A_3` nonzero | 7 |
| B2 | `S_eps` is a real involution: diagonal `+-1`, `S_eps^2 = I`, traceless, staggered-sign form | 4 |
| B3 | chiral action: `S_eps D2 S_eps = -D2`, `S_eps M S_eps = M`, `S_eps Q_m S_eps = Q_m` and hence `S_eps P_m S_eps = P_m`, anticommutation rejector | 4 |
| B4 | kernel reversal: `S_eps J_ker S_eps = -J_ker`, rejector, `S_eps V8 = V8 Pi`, `Pi^2 = I`, `Pi J64 Pi^T = -J64`, `sign(S^c) = -sign(S)` | 6 |
| B5 | bulk reversal: `S_eps A_m S_eps = -A_m`, rejector | 2 |
| B6 | total linear sign reversal: exact all-pieces-flip, a flagged float sanity check of the linear/antilinear contrast on `i I`, and float confirmation `S_eps J_full S_eps = -J_full` and `S_eps J_alt S_eps = -J_alt` | 3 |
| B7 | extended group: `S_eps` not in `G_amb`, `S_eps` normalizes `G_amb`, order `1536` disjoint cosets, sign-lock, census `768`/`768` | 5 |
| B8 | aligned-bulk comparison: `-J_full != J_alt` exact, `J_full != J_alt` exact, no element has opposite kernel/common-bulk signs (so `J_alt` is outside the orbit), float confirmation all sixteen parent sign-members square to `-I_64` | 4 |

## Honest auditor read

This note reads the structure of a fixed finite symmetry action: a single real involution `S_eps` on `C^64` and the order-`1536` group it makes together with the ambient symmetry. It is not a dynamical selection, not a measurement, and not a probability-weight derivation. It fixes no free parameter and derives no `r`; it is r-neutral because `r` never enters and measure-neutral because it introduces no measure, weight, or probability rule. It has no measured, fitted, literature, observational, normalization, or dynamical input beyond the five linked structural dependencies; `S_eps` itself is built from native site coordinates. It selects no `J`-sign. What it establishes is the complex-structure sign reversal and the invariance of the relative kernel/common-bulk sign within the aligned-bulk `{J_full,J_alt}` comparison under the order-`1536` lattice-and-chiral group. The parent's sixteen-member sign family remains explicit and no physical freedom against larger transformations or dynamics is claimed. This is a finite fixed-surface statement on the `L = 4` torus; no continuum or infinite-volume claim is made, no Hamiltonian or admissibility dynamics is chosen, no physical identification is asserted, and nothing pre-record is forced.

A final line: the [paired runner](../scripts/kcpt_chiral_parity_orientation_reversal_relative_binary_2026_07_19.py) rebuilds `D2`, `V8`, `M`, the drop-one polynomials `Q_m`, the normalized projectors `P_m`, the carriers `A_m`, the kernel lift `J_ker`, the chiral parity `S_eps`, the regenerated `768`-member `G_amb` and its order-`1536` chiral extension, and the sibling `J_alt`; all load-bearing gates are exact integer, every floating-point gate is tagged `[FLOAT SANITY]`, and the runner prints `TOTAL: PASS=N FAIL=0` and exits nonzero on any failure. Its cached output belongs at `logs/runner-cache/kcpt_chiral_parity_orientation_reversal_relative_binary_2026_07_19.txt`.
