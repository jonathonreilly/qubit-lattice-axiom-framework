# KCPT kernel induced representation: central complex structure

Date: 2026-07-18

Claim type: bounded theorem — a structure theorem on a fixed finite surface,
established by exact integer and rational arithmetic (numpy int64 plus sympy; no
floating point in any load-bearing gate). It states what the induced symmetry
action on the corner-wave kernel *is*; it fixes no free parameter and forces
nothing pre-record. The paired runner recomputes every gated quantity from the
construction, so this note carries no number that the runner does not derive.

## Setting

The surface is the landed periodic staggered lattice on the `4^3` torus, with the
Kawamoto-Smit staggered phases of the corner-carrier construction: `eta_1 = 1`,
`eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1 + x_2}` (the corner-carrier delivery
note fixes these and records that "its exact rank is `56`", leaving an eight-
dimensional kernel; see the
[corner-carrier note](docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)).
The integer antisymmetric operator is written `D2` here, `D2[i, j]` accumulating
`eta_mu(x)` for the forward neighbour and `-eta_mu(x)` for the backward neighbour
along each of the three axes, with site order `idx(x1, x2, x3) = (x1*L + x2)*L + x3`,
`L = 4`, `N = 64`.

The kernel is spanned by the eight corner waves `chi_S(x) = (-1)^{sum_{k in S} x_k}`
indexed by subsets `S` of `{0, 1, 2}` in the fixed order
`[(), (0,), (1,), (2,), (0,1), (0,2), (1,2), (0,1,2)]`, "graded by Hamming weight as
`1 + 3 + 3 + 1`". Stacked as the columns of `V8` these satisfy `D2 @ V8 = 0` and
`V8^T @ V8 = 64 I`, so `V8` is a scaled isometry onto the kernel.

Each base surface symmetry is dressed. The three bases are the stabiliser
(identity), the order-two proper rotation `U2: x -> (-x2, -x1, -x3) mod 4`, and the
proper cubic rotation `UR: x -> (x2, x3, x1)`; these are exactly the
"standard translations, and proper cubic rotations" admitted by the
[minimal-axioms note](docs/MINIMAL_AXIOMS_2026-06-29.md). A dressed candidate is
`U = diag(d) @ base @ trans(t)`, where `trans(t): x -> x - t mod 4` ranges over all
`64` translations and the quadratic sign field is

`d(x) = (-1)^{a1 x1 + a2 x2 + a3 x3 + b12 x1 x2 + b13 x1 x3 + b23 x2 x3}`

ranging over all `64` sign patterns. Each base therefore carries a dressed class of
`64 x 64 = 4096` members. The action of a dressed candidate on the kernel is the
induced operator `K8 = V8^T @ U @ V8`, an integer `8 x 8` matrix. The staggered
realisation gate handle `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` is the
context for reading `D2` as the staggered Dirac operator on this surface.

## T1 — whole-class kernel preservation and the parity-qubit dictionary

Every one of the `3 x 4096` dressed candidates preserves the corner-wave kernel
exactly: `64 (U @ V8) = V8 @ K8` as an integer identity, so `U` maps the kernel into
itself with no residual (gate B1-4). On each base exactly `64` of the `4096`
candidates commute with `D2` (gate B1-5), and for every commuting member the induced
`K8` is a scaled orthogonal matrix, `K8^T @ K8 = 4096 I` (gate B1-6).

The induced action reads as a dictionary on the three parity qubits carried by the
subset index (qubit `k` is the `x_k`-parity bit):

- a translation induces a parity diagonal, `induced(trans(t)) = 64 Z(t)` with
  `Z(t)_S = (-1)^{sum_{k in S} t_k}` (gate B1-7a);
- the undressed order-two rotation `U2` induces `64` times the subset permutation that swaps
  axes `0` and `1` (gate B1-7b), and the undressed rotation `UR` induces `64` times
  the cyclic subset permutation `0 -> 1 -> 2 -> 0` (gate B1-7c);
- a linear sign field induces a symmetric-difference convolution: for
  `d = chi_{(1,2)}`, `induced(diag(d)) = 64 X_{(1,2)}`, the operator
  `S -> S xor {1, 2}` (gate B1-8).

The general commuting member factors as `K8 = Ms(shat) @ P_base @ Z(t)`, where
`P_base` is the subset permutation of its base, `Z(t)` its translation diagonal, and
`Ms(shat)_{S xor R, S} = shat_R` is the convolution by `shat = V8^T @ d`. The worked
exemplar (base `U2`, bits `(0,1,0,1,0,0)`, `t = (1,0,0)`) commutes with `D2`, and its
`shat` has support `{(): 32, (0,): -32, (1,): 32, (0,1): 32}` (gate B1-9). Because the
convolution kernel `shat` carries half-unit weights, most induced members are `64`
times an orthogonal matrix with `+/- 1/2` entries rather than a signed permutation;
the runner keeps such members as raw integer matrices wherever a test is scale-
invariant so that no division corrupts them.

## T2 — forced quadratic class signatures

The `64` commuting members of each base split as `4` sign fields times `16`
translations (gate B2-4). The quadratic part `(b12, b13, b23)` is pinned by the base:

- stabiliser: purely linear, `(b12, b13, b23) = (0, 0, 0)`, with linear compensator
  law `(a1, a2, a3) = (0, t1, t1 + t2)` (gates B2-1, B2-3);
- order-two rotation `U2`: forced `(b12, b13, b23) = (1, 0, 0)` uniformly, law
  `(a1, a2, a3) = (1 + t1, 1, 1 + t1 + t2)` (gates B2-2, B2-3);
- rotation `UR`: forced `(b12, b13, b23) = (1, 1, 0)` uniformly, law
  `(a1, a2, a3) = (t1 + t2, 0, t1)` (gates B2-2, B2-3).

The compensator laws are congruences mod `2` in the translation components, and
`t3` never enters them, so its parity stays free in every class.

Hamming-grading preservation and triplet preservation occur only in the linear
stabiliser class, with counts `16 / 0 / 0` across stabiliser / U2 / UR (gate B2-5),
and the `16` stabiliser grading-preservers are exactly the `a = (0, 0, 0)` members,
each a pure parity diagonal. The stabiliser Hamming-block support census is
`32 / 16 / 16` over the three named supports (gate B2-7). The dichotomy is sharp
at class level: the non-trivial base symmetries can be realised on the kernel at
all only at their forced quadratic price, no quadratically-dressed member
preserves the Hamming grading or the triplet, and within the purely-linear
stabiliser class preservation is confined to the trivially-dressed members.

## T3 — the induced group

The distinct induced images generate a group `G` of order `|G| = 96` (gate B3-1).
Per-class images close to proper subgroups of orders `16 / 32 / 48`, and among the
three base pairs only `U2` together with `UR` generates all of `G`
(closures `32 / 48 / 96`; gate B3-2). The scalar `-64 I` lies in `G`; the centre has
order `4`, namely `{+/- I, +/- J}`, and exactly two central elements square to `-I`
(gate B3-3). The exponent is `24`; there are `16` conjugacy classes with sizes
`[1,1,1,1,6,6,6,6,6,6,8,8,8,8,12,12]`; the commutator subgroup has order `24` and the
abelianisation has order `4` (gate B3-4). The grading-preserving subgroup of `G` has
order `4`, equal to the triplet-preserving subgroup, with triplet restrictions
`{I, diag(1,1,-1), diag(-1,-1,1), -I}` in which the `x1` and `x2` slots are sign-
locked to a common value (gate B3-5). The sum of all `96` induced matrices is the
zero matrix, so `G` fixes no vector in the kernel (gate B3-6).

## T4 — central complex structure and rational irreducibility (headline)

The exact commutant of `G` over the rationals is two-dimensional, `span{I, J}`, and
`Q(J)` is isomorphic to `Q(i)` (gate B4-3). The element `J` is a canonical central
complex structure: the runner *finds* it as the unique central element that squares
to `-I` and carries the weight-one corner wave `chi_{x2}` to the vacuum corner
wave with a `+` sign (canonical orientation),
and only then gates the found matrix against its closed form — `J` is never hard-
coded. It satisfies `J^2 = -I`, `J^T = -J`, `trace J = 0`, and is integer-exact at
scale `64` (gates B4-4, B4-5). Its closed form is the real Pauli word
`Z (x) iY (x) Z` on the three parity qubits, with the complex axis on the middle
`x2` parity qubit — the middle link of the staggering chain (`eta_2`, `eta_3`
above): `J[index(S xor {1}), index(S)] = 64 (-1)^{|S and {0,2}|} (+1 if 1 in S else -1)`,
with Hamming-block support `{(0,1),(1,0),(1,2),(2,1),(2,3),(3,2)}` and vacuum column
`-64 e_{(1,)}`.

Because `Q(J)` is a field, `G` admits no proper rational invariant subspace: the
characteristic polynomial of `J` is `(lambda^2 + 1)^4`, and
`det(a I + b J) = (a^2 + b^2)^4` factors over the rationals with no linear factor
(gates B4-6, B4-7). Over the complex numbers the representation splits as exactly one
conjugate pair `W + Wbar` with `dim W = 4`: the `+i` and `-i` eigenspaces of `J` each
have dimension `4`, and the character satisfies `<chi, chi> = 2` with Frobenius-Schur
sum `0`, the complex type (gates B4-1, B4-2, B4-6). The orbit of a single
Hamming-weight-one corner wave under `G` spans the whole eight-dimensional kernel
(rank `8`; gate B4-8): each weight-one corner wave is a cyclic vector, so any
`G`-stable subspace containing one is the whole kernel. The four graded members
of `G` are simultaneously diagonal — on the graded subgroup alone the kernel
splits completely into coordinate lines — so the rational irreducibility of the
full `G` is carried entirely by the members off the graded subgroup (gate B4-9).

## T5 — FLAG registration

The two-presentation binary of the coupling-triple mechanism registers on this
surface as an orientation choice. The
[two-presentation mechanism note](docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md)
records:

> **FLAG — two-model mechanism:** the entrywise-conjugate presentations in L-K2 satisfy the same named clauses and exchange every K-odd seed.

> The memo's live Qualification leaves the unfixed choice conditional/open.

At the kernel level: entrywise complex conjugation fixes the entire real induced
group `G` (every member is a real integer matrix) and carries `ker(J - iI)` onto
`ker(J + iI)`, exchanging `W` and `Wbar` (gate B5-1). The two entrywise-conjugate
presentations therefore materialise here as the two central complex structures `+J`
and `-J` — a choice of which central complex structure is called `i`. The vacuum
orbit under `G` has size `48` and mixes every Hamming level (its support set spans
weights `0` through `3`; gate B5-2), so no graded, vacuum-anchored splitting exists to
prefer one orientation over the other. The graded restrictions commute with a free
diagonal `diag(w1, w2, w3)`, so the theorem attaches no per-slot weight relation
(gate B5-3).

## Boundary — what this does NOT establish

- It does NOT select the orientation: `+J` versus `-J` remains the two-presentation
  choice, exactly as flagged; the theorem exhibits the binary, it does not break it.
- It does NOT act on the mechanism note's live Qualification: the unfixed choice
  stays conditional and open at the memo level; this surface adds structure around
  it, not a decision of it.
- It derives no `r` value and imposes no weighting: the graded restrictions commute
  with an unconstrained diagonal (gate B5-3), so no per-slot ratio is forced.
- It is a finite-surface structure theorem: no continuum limit and no interacting
  claim are asserted, only exact facts about the `8`-dimensional kernel of a fixed
  `4^3` operator.
- Register-not-read: the corner-wave kernel is the record-carrier surface and the
  induced group is a reconstruction-level symmetry action. The theorem registers
  structural facts about that carrier and forces nothing pre-record.

## Negative controls

- The undressed rotations `U2` and `UR` do not commute with `D2`, so dressing is
  required, not cosmetic (gate B6-1).
- A one-bit change to the T1 exemplar (flipping `b13`, bits `(0,1,0,1,1,0)`, same
  `t`) breaks commutation with `D2` (gate B6-2).
- The two wrong-axis Pauli words — the same formula with the complex axis moved to
  the `x1` parity qubit, and to the `x3` parity qubit — each fail to commute with at
  least one member of `G`, so the `x2` axis is forced (gate B6-3).
- A stabiliser candidate with all-zero bits and `t = (1,0,0)` violates the stabiliser
  compensator law and indeed does not commute with `D2` (gate B6-4).

## Gate map

The runner emits `[Bx.y]`-tagged `PASS/FAIL` lines covering every row below (rows
spanning several bases or items expand to one line each) and a final
`TOTAL: PASS=N FAIL=M` line; it exits `0` if and only if `M = 0`.

| Gate | Claim |
| --- | --- |
| B1-1 | `D2` integer antisymmetric, entries in `{-1, 0, 1}` |
| B1-2 | `rank(D2) = 56`, kernel dimension `8` |
| B1-3 | `D2 @ V8 = 0`, `V8^T @ V8 = 64 I`, grading `1 + 3 + 3 + 1` |
| B1-4 | all `3 x 4096` dressed candidates preserve the kernel (residual identity) |
| B1-5 | exactly `64` commuting members per base |
| B1-6 | each commuting `K8` has `K8^T @ K8 = 4096 I` |
| B1-7 | dictionary: translation to `Z`-diagonal, base to subset permutation |
| B1-8 | linear sign field to symmetric-difference permutation `X_{(1,2)}` |
| B1-9 | exemplar commutes, `K8 = Ms(shat) @ P_swap01 @ Z(t)`, named `shat` support |
| B1-10 | exemplar `(bits, t)` present in the `U2` commuting set |
| B2-1 | stabiliser purely linear; `U2`, `UR` have no purely-linear member |
| B2-2 | forced quadratic signature `(1,0,0)` for `U2`, `(1,1,0)` for `UR` |
| B2-3 | per-base compensator laws `(a1, a2, a3)` |
| B2-4 | commuting set is `4` sign fields times `16` translations |
| B2-5 | grading- and triplet-preserving counts `16 / 0 / 0`; graded stabiliser members are diagonal |
| B2-6 | distinct induced `K8` per base `= 8`; distinct vacuum images `= 4` |
| B2-7 | stabiliser Hamming-block-support census `32 / 16 / 16` |
| B3-1 | `\|G\| = 96` from the `24` distinct generators |
| B3-2 | single-base closures `16 / 32 / 48`; only `U2 + UR` gives all of `G` |
| B3-3 | `-64 I` in `G`; centre order `4`; two central squares of `-I` |
| B3-4 | exponent `24`; `16` conjugacy classes; commutator `24`; abelianisation `4` |
| B3-5 | graded subgroup order `4`; triplet restrictions; `x1`, `x2` sign-locked |
| B3-6 | sum over `G` is the zero matrix |
| B4-1 | sum of `tr(K8)^2` gives `<chi, chi> = 2` |
| B4-2 | Frobenius-Schur sum `0` |
| B4-3 | exact commutant over the rationals has dimension `2` |
| B4-4 | unique canonical `J` found; the other central square of `-I` is `-J` |
| B4-5 | `J` closed form, `J^2 = -I`, `J^T = -J`, `trace 0`, central, named support, vacuum column |
| B4-6 | charpoly `(lambda^2 + 1)^4`; both `J`-eigenspaces dimension `4` |
| B4-7 | `det(aI + bJ) = (a^2 + b^2)^4`, so the commutant is a field |
| B4-8 | orbit of one Hamming-weight-one carrier spans the kernel (rank `8`) |
| B4-9 | the four graded members of `G` are diagonal |
| B5-1 | conjugation fixes `G` and swaps `W` and `Wbar` |
| B5-2 | vacuum orbit size `48`, mixed-grade support set |
| B5-3 | graded restrictions commute with `diag(w1, w2, w3)` (weight-neutral) |
| B6-1 | undressed `U2`, `UR` do not commute with `D2` |
| B6-2 | one-bit rejector breaks commutation |
| B6-3 | wrong-axis words on `x1`, `x3` fail; `x2` axis forced |
| B6-4 | law-violating stabiliser candidate does not commute |
| B7-1..B7-6 | verbatim source fragments present in source and in this note |
| B8-1..B8-3 | consumed-dependency ledger shards exist and parse |
| B9-1..B9-5 | note hygiene: forbidden strings absent, no bare decimals, link inventory, required and verbatim strings present |

## Paired runner and cache

- [paired runner](scripts/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.py)
- [runner cache](logs/runner-cache/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.txt)

The cache path is
`logs/runner-cache/kcpt_kernel_induced_representation_central_complex_structure_2026_07_18.txt`;
it records the runner's per-gate lines and final `TOTAL` count.
