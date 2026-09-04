# Route 1 direct CAR-cell occupation compiler — Cycle 231

**Date:** 2026-07-17

**Type:** route-specific partial-attempt

**Status:** exact bounded onsite/contact embedding plus falsified declared
no-auxiliary stream compiler; audit unset

**Authority:** none

**Audit:** unset

**Constitutional effect:** none

**Packaging:** draft parking branch and existing draft PR #5389 only

Companion runner:

```text
scripts/ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py
```

This Route-1 artifact changes no foundation, axiom, Qualification, primitive,
registry, policy, queue, or audit surface. It is one lane of the Cycle-231
three-route tournament. It is not a disposition of the local gauge/auxiliary
or staggered/time-multiplexed routes.

## Result up front

There is a useful but incomplete direct compiler. Divide the physical cubic
lattice into supplied `3 x 3 x 3` supercells. Put six active physical `M_2`
sites on the face centres of each supercell and fix the other 21 sites to a
blank state. Mode `a` of coarse cell `x` is the occupation qubit at

```text
r(x,a) = 3 x - D_a.
```

This uses six active physical `M2` sites and 27 physical sites per coarse
cell, both constant. The six active qubits have dimension `2^6=64`; hence the
cell occupation map exactly carries the Cycle-230 Fock cell, its local even
algebra

```text
A_x^+ = M_32(C) direct-sum M_32(C),
dim_C A_x^+ = 2048,
```

the `64 x 64` exterior coin `Gamma(C)`, and the contact

```text
W_x(g) = exp[i g binom(N_x,2)].
```

The onsite gates have bounded physical support, preserve number and parity,
have zero active-code leakage, and give exact contact deletion at `g=0`.
Because the contact and every fermionic sign are trivial in the one-particle
sector, the prior rest/curvature/forced-inertia fixture is preserved. The
same block contact also reproduces the Cycle-230 seam block, including its
`1/L^3` plane-wave normalization and singular spectrum, in all 24
proper-cubic frames.

The direct attempt fails at the intercell stream. Cycle 230 factors the stream
as `S=B A`. The onsite `A` swaps are bounded within a supercell, and every
`B` pair is a physical nearest-neighbor pair in the layout above. But after a
global occupation order is chosen, the exact fermionic exchange of modes
`i<j` is

```text
|10>_(i,j) -> (-1)^[sum_(i<k<j) n_k] |01>_(i,j),
|01>_(i,j) -> (-1)^[sum_(i<k<j) n_k] |10>_(i,j),
|11>_(i,j) -> -|11>_(i,j).
```

An endpoint-local two-qubit FSWAP supplies the last sign but not the interval
parity in the first two lines. The runner exhausts every two-particle basis
state at `L=3,4,5`. It finds mismatches at every size while all vacuum and
one-particle states agree. One witness has exact and local phases `-1` and
`+1` on the same output basis state. Therefore, for the declared direct
physical update

```text
G_coarse   = W_g Gamma(B) Gamma(A) Gamma(C),
G_physical = W_g B_endpoint Gamma(A) Gamma(C),
```

the operator-norm intertwining residual is exactly 2:

```text
|| E G_coarse - G_physical E || = 2.
```

The equality follows because the displayed basis witness gives the lower
bound `2`, the difference of two unitaries is at most `2`, and the common
coin, `A`, and contact factors are unitary. Thus the failure is not numerical,
not caused by the interaction, and not visible to the one-particle mass test.

The exact ordered/Jordan-Wigner image does satisfy

```text
E G_coarse = G_JW E
```

identically, but its interval support grows with held-out torus size. It uses
the global ordering and parity service forbidden by the campaign contract.
Conversely, the endpoint-local update has bounded support and no parity
service but fails the exact intertwining contract. This is the sharp Route-1
tradeoff for this declared occupation encoding.

The result is **not** a global compiler impossibility. A different non-product
code, local auxiliary/gauge construction, distinguishable-walker
antisymmetry construction, or staggered compiler remains live. There is no
axiom pressure from this route-specific result.

### Finite-torus code and domain

For each declared `L>=3`, take a physical torus of side `3L` and coarse cells
`x in (Z/LZ)^3`. The code is

```text
H_code(L)
  = [(C^2)^(tensor 6)]^(tensor L^3)_active
    tensor |0...0>_blank,
dim H_code(L) = 2^(6 L^3).
```

After choosing the finite-torus CAR occupation convention, `E_L` maps every
CAR occupation basis ray isometrically to the corresponding active-qubit bit
string and the 21 blank sites of each block to `|0>`. Both `G_JW` and the
endpoint-local candidate are unitary and preserve `H_code(L)` exactly; the
former is nonlocal and intertwines, while the latter is bounded and does not.
Both preserve total particle number and hence global fermion parity. The
norm-two witness lies within the lawful `N=2`, even-global-parity domain, so it
is not created by comparing different superselection sectors. Local parity of
one coarse cell is not fixed because the target stream changes it.

## Exact encoding and physical layout

For each coarse cell let

```text
H_CAR,x = wedge(C^6),
H_phys,x = (C^2)^(tensor 6).
```

Fix the within-cell direction labels only for this direct attempt and define

```text
E_x c_(x,0)^dagger^n0 ... c_(x,5)^dagger^n5 |vac>
  = |n0 ... n5>_x.
```

At one cell `E_x` is unitary. Therefore every cell operator has an exact
six-qubit image. In particular,

```text
E_x Gamma(C) = G_C,x E_x,
E_x W_x(g)   = G_W,x(g) E_x.
```

The direct sum of the even and odd 32-dimensional parity sectors is retained;
the construction does not silently project away local odd parity. That point
matters because the one-particle fixture lives in an odd cell sector and the
stream changes individual cell parities.

The supercell offsets are `{-1,0,1}^3`. The six active offsets are
`{-D_a}`. Proper-cubic rotations permute these six offsets and preserve the
whole supercell. For the Cycle-230 `B` layer, mode `(x,a)` is paired with
`(x-D_a,bar(a))`; their physical face-centre sites differ by one lattice edge.
The `A` layer pairs opposite face centres within diameter two. Thus all
declared gates have a size-independent physical support bound before the CAR
sign is imposed.

This layout supplies a period-three block origin. It does not derive a
translation-covariant local marker or show that the fixed blank pattern is
selected by the framework's one nearest-neighbor admissibility rule. Those
are declared layout/code conditions, not hidden successes.

## Why the intercell equality fails

Let `p_B` be the one-particle permutation of the `B` stream. On an ordered
occupation basis with occupied sources `I={i_1<...<i_n}`,

```text
Gamma(p_B)|I>
  = sgn[p_B(i_1),...,p_B(i_n)] |sorted p_B(I)>.
```

The product of endpoint FSWAPs instead contributes only one minus sign for
each `B` pair whose two endpoints are both occupied. Those rules agree for
`n=0,1` and disagree already for `n=2` when two distinct occupied modes cross
in the chosen order.

The discrepancy cannot be repaired by a bounded phase gate that reads only a
fixed neighborhood of the endpoints for this encoding. On the `L=5` witness,
two states have:

- the same endpoint data out to physical radius two;
- the same particle number `N=2` and the same global even parity;
- one spectator inside the ordered interval in one state; and
- one equally remote spectator outside the interval in the other.

The required interval parities differ. Any gate supported on the endpoint
neighborhood acts with the same conditional endpoint phase on both. More
generally, for any fixed radius, a large enough lexicographically ordered
three-dimensional torus has a physical edge whose ordered interval contains
modes outside that radius. This last analytic statement is restricted to the
declared order-based occupation encoding; it is not a theorem about all
possible codes.

A complementary `L=5` witness puts the two particles at physical positions
`(-1,0,0)` and `(1,0,6)`, farther apart than two radius-two light cones, while
the exact and endpoint signs still disagree. Hence a radius-two correction
whose action factorizes on separated occupation packets cannot repair the
two-particle rule while retaining the exact vacuum and one-particle action.

Changing the total order can move which edges carry long strings, but using
that order is itself forbidden global structure. Ordering modes by the `B`
matching makes the `B` layer adjacent, while the generic onsite exterior coin
then couples modes separated across those matching blocks. The direct attempt
does not obtain simultaneous boundedness by changing presentation.

## Proper-cubic covariance audit

There are two distinct frame actions and they must not be conflated.

1. The coarse CAR frame action is the exterior lift `Gamma(P_R)` of the
   six-direction permutation. The exterior coin and contact commute with it
   in all 24 frames to numerical precision.
2. A geometric rotation of the six face-centre qubits acts by the ordinary
   tensor-factor permutation `Q(P_R)`. For 22 of the 24 frames,
   `Q(P_R)` does not commute with the exterior coin. The maximum runner
   residual exceeds seven.

The representations are not related by one fixed within-block basis change:
their group characters differ for some proper-cubic rotations. This is a
representation statement for the six-arm direct code, not a general symmetry
no-go.

A bounded **onsite** repair exists if one supplies the local diagonal sign
cocycle

```text
D_R = Gamma(P_R) Q(P_R)^dagger,
R_phys = D_R Q(P_R).
```

The runner verifies that this repaired action commutes with the onsite coin in
all 24 frames. But it does not repair the full candidate. Pure geometric
frames preserve the endpoint-FSWAP network and fail the coin in 22 frames;
the locally exterior-corrected frames preserve the coin and fail endpoint
stream covariance in all 23 nonidentity frames on two-particle witnesses. The
exact global CAR frame is covariant, but its occupation image again contains
global ordering signs. Therefore no one of these two bounded frame actions
makes the declared direct update covariant. A different local representation
is not ruled out.

## Mass, contact, and seam controls

On the zero- and one-particle sectors,

```text
W_g = I,
Gamma(B) = B_endpoint,
Gamma(A) = A_endpoint,
Gamma(C)|_(N=1) = C.
```

The direct candidate therefore reproduces the complete one-particle walk and
preserves the Cycle-219 rest, dispersion, and force-response mass fixture.
This is an exact sector statement plus the predecessor's declared finite
packet tolerance. It is not an interacting or renormalized-mass result.

The contact is diagonal in the same local occupations in both descriptions,
so its local generator and the Cycle-230 momentum-balanced `2p2h` form factor
are unchanged by `E`. The runner independently reconstructs the `L=3` block,
its `2 pi` machine-precision phase difference, singular values near
`0.49577141, 0.45566605`, raw plane-wave norm `||F||/L^3`, and all 24 frame
singular spectra.

That contact/seam equality is a gate and matrix-element result. The failed
stream means this Route-1 candidate does not reproduce repeated interacting
updates of the sea. It would be incorrect to call the local contact
embedding alone a physical-site compiler.

The labels `coin`, `A`, `B`, and `contact` describe a supplied factorization
of one spatial-QCA update. Their layer count and circuit substeps are not
physical time, a clock, a rate, or a metric. This route does not address the
emergent-dynamics single-generator gate.

## Leakage, deletion, held-out-size, and lawful-domain controls

| Control | Result | Exact scope |
|---|---|---|
| active-code leakage | pass | all `64` states of each six-qubit active block are retained, so onsite coin/contact and endpoint FSWAP are unitary on the full active space |
| blank-site leakage | conditional pass | the 21 unused sites per supercell remain blank because every candidate gate acts as identity on them; local enforcement/selection of that blank pattern is not constructed |
| interaction deletion | pass | `g=0` gives the identity contact exactly; the stream residual remains, isolating it from interaction choice |
| one-particle deletion | rejected | restricting away `N>=2` would make the stream exact but deletes the contact and seam block |
| global-parity restriction | fails to repair | the runner's two-particle witnesses all have fixed even global parity |
| even parity per cell | unlawful for target | it excludes a single-particle cell and leaks when the stream separates two same-cell particles |
| held-out sizes | fail for local stream | exhaustive `L=3,4,5` two-particle tests retain nonzero mismatches; exact JW interval size grows again at `L=6` |
| lawful domain | partial | full active occupation space is closed under both unitaries, but only the nonlocal exact image intertwines; the local image is the wrong law on valid `N=2` states |

No host-side correction, postselection, lookup table, or global parity oracle is
used by the endpoint-local candidate. Adding any of those would change the
route and violate the success contract.

### Executable numerical ledger

| Check | Exact runner output |
|---|---|
| `L=3` two-particle stream | `4140 / 13041` basis pairs mismatch (`0.31746031746031744`); maximum ordered span `109` |
| `L=4` two-particle stream | `19008 / 73536` mismatch (`0.2584856396866841`); maximum ordered span `289` |
| `L=5` two-particle stream | `60600 / 280875` mismatch (`0.2157543391188251`); maximum ordered span `601` |
| maximum intervening modes, `L=3,4,5,6` | `108, 288, 600, 1080` |
| direct intertwining residual | exact operator norm `2` |
| pure geometric frame/coin | `22 / 24` frames fail; maximum Frobenius commutator `9.237604307034013`; maximum character gap `16` |
| local exterior frame/endpoint stream | `23 / 24` frames fail (every nonidentity frame) |
| exterior coin/contact frame residuals | `1.602143998693333e-15`, `0` |
| mass coordinates | rest `0.4534056541748851`; dispersion `0.4534056690336209`; forced `0.45444242813733504`; analytic `0.4534056541748852` |
| seam reduced singular values | `0.49577141, 0.45566605`; 24-frame residual `1.2947314098277875e-15` |
| raw plane-wave seam norm divided by `g` | `0.024939455786930312 = ||F||/3^3` |

## Supplied-structure inventory

The construction supplies rather than derives:

- the Cycle-219 proper-cubic coin family, `beta=-0.3`, and its physical
  interpretation;
- the Cycle-230 six CAR modes per cell, fermionic statistics, and
  number-preserving exterior lift;
- the contact strength `g=0.37` for the finite diagnostic and the declared
  contact-after-free schedule;
- the `3 x 3 x 3` supercell scale, block origin, active face-centre assignment,
  direction labels, and 21 blank sites;
- a within-cell occupation convention;
- for the exact-but-disallowed image, a total global mode order and its
  interval parity strings;
- for repaired frame covariance, the 24 local exterior-sign cocycles `D_R`;
- periodic finite tori and the Cycle-230 supplied sea/phase cut for the seam
  comparison; and
- identity dynamics on unused physical sites.

The runner does not supply an auxiliary gauge field, Gauss law, parity
service, autonomous schedule, block-marker dynamics, record process, physical
clock, probability rule, or gravitational source.

## Route-1 disposition against the success contract

| Requirement | Disposition |
|---|---|
| bounded support / constant overhead | partial: `27` sites per cell and bounded onsite/A/B geometry; exact B parity is unbounded in the ordered encoding |
| local auxiliary/gauge constraints | not applicable to the no-auxiliary attempt; blank/block enforcement remains conditional |
| no global ordering/parity service | endpoint candidate passes this condition but fails intertwining; exact candidate violates it |
| all 24 proper-cubic frames | coarse global exterior action passes; pure geometric action fails the coin in 22 frames; local exterior cocycle repairs the coin but makes the endpoint stream fail in 23 nonidentity frames |
| one-particle mass | pass |
| local contact | pass as a gate |
| Cycle-230 seam block | pass as a contact-generator block, not as full evolution |
| leakage/deletion/held-out/lawful domain | executed as above |
| `E G_coarse = G_physical E` | fail for the declared local endpoint stream, exact norm residual `2` |

**Final Route-1 status:** `partial-attempt-with-honest-residual`. The natural
direct occupation block closes local capacity, onsite coin, contact, mass, and
form-factor representation, but does not compile the full free-plus-contact
CAR update without the forbidden global interval parity. The result does not
dispose of Route 2 or Route 3.

## TOE dependency ledger and lane effect

| Workstream | Route-1 effect |
|---|---|
| `C_ref` | unchanged: the direct block does not select phase origin, sea, or preparation |
| `C_num` | unchanged: occupation encoding does not select a number reference or superselection rule |
| `C_wrap` | unchanged: no physical clock/history stores winding |
| `C_int` | unchanged from Cycle 230: one supplied contact is represented exactly, but no selected interaction/rate/protection theorem follows |
| `C_local` | sharpened partial: exact bounded onsite/contact block and physical geometry are constructed; the declared no-auxiliary intercell stream has exact residual `2`; gauge and staggered routes remain live |
| `C_source` | unchanged: no conserved physical energy/stress/source ledger is selected |

The calibrated lane maturities remain operational quantum/records `2/5`, time
`1/5`, inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
The direct attempt preserves prior matter evidence but does not close the
substrate compiler, so no score changes.

## Primary-source and novelty boundary

The occupation/Jordan-Wigner sign mechanism, exterior second quantization,
and use of fermionic swaps are standard prior machinery, not Cycle-231
novelty. Farrelly and Short construct qubit-QCA representations of causal
fermions and use finite auxiliary structure in higher-dimensional local
constructions [1]. Mlodinow and Brun prove a scoped higher-dimensional barrier
for their direct occupation/local-creator class [2], then construct a distinct
three-dimensional distinguishable-particle QCA followed by restriction to an
antisymmetric sector [3]. These sources are constructive escape boundaries;
none is treated as a no-go for the full tournament.

The repository-specific contribution is narrower: the six-arm physical block,
exact separation of onsite/contact success from stream failure, exhaustive
fixed-`N` mismatch counts on the named `B` layer, the exact norm-two
intertwining witness, the 24-frame representation/cocycle audit, and the
mass/contact/seam coexistence controls. Global priority is not claimed.

References:

1. T. C. Farrelly and A. J. Short, “Causal Fermions in Discrete Space-Time,”
   *Physical Review A* **89**, 012302 (2014),
   <https://doi.org/10.1103/PhysRevA.89.012302>, arXiv:1303.4652.
2. L. Mlodinow and T. A. Brun, “Quantum field theory from a quantum cellular
   automaton in one spatial dimension and a no-go theorem in higher
   dimensions,” *Physical Review A* **102**, 042211 (2020),
   <https://doi.org/10.1103/PhysRevA.102.042211>, arXiv:2006.08927.
3. L. Mlodinow and T. A. Brun, “Fermionic and bosonic quantum field theories
   from quantum cellular automata in three spatial dimensions,” *Physical
   Review A* **103**, 052203 (2021),
   <https://doi.org/10.1103/PhysRevA.103.052203>, arXiv:2011.05597.

## No-Go Discipline Gate

The freshly fetched `origin/main` no-go-discipline skill was applied. The
narrow claim under audit is only:

> The declared six-arm, six-occupation-qubit, no-auxiliary direct encoding
> does not satisfy the full Cycle-230 free-plus-contact intertwining contract
> with endpoint-local stream swaps; the exact ordered image restores the
> equality only by using size-growing interval parity.

**N1-N8 status:** **PASS for that narrow route-specific claim.** A claim that
no physical compiler exists **FAILS** because auxiliary/gauge,
staggered/time-multiplexed, non-product code, and antisymmetric-walker routes
remain live. The broad claim is not shipped.

### N1 — alternative route enumeration

Every `ATTEMPTED` row below is current executable evidence in the companion
runner: `direct_stream_controls`, `remote_parity_controls`,
`rotation_controls`, `onsite_block_controls`, or `lawful_domain_controls`.
No row is labeled `RULED OUT BY PRIOR`.

| Attack/escape | Marker | Executed disposition |
|---|---|---|
| exact global occupation/Jordan-Wigner image | **ATTEMPTED** | restores `E G=G_JW E` exactly, but the runner's held-out support spans grow and the construction uses the forbidden global order/parity service |
| endpoint-local FSWAP on every physical B edge | **ATTEMPTED** | passes every zero/one-particle state and mass fixture; exhaustive `N=2` tests at `L=3,4,5` give sign mismatches and an exact norm-two witness |
| bounded endpoint parity dressing | **ATTEMPTED** | fixed-`N=2`, fixed-even-parity states identical within radius two require opposite interval signs; the route fails for the declared encoding |
| fixed global parity sector | **ATTEMPTED** | the same witness pair lies entirely in global even parity, so sector fixing does not repair it |
| even local parity per coarse cell | **ATTEMPTED** | excludes the one-particle target and leaks when `B` separates two particles initially in one cell |
| pure geometric proper-cubic arm permutation | **ATTEMPTED** | preserves the endpoint stream but fails the exterior coin in 22 frames; a bounded supplied sign cocycle repairs the coin but the endpoint stream then fails in 23 nonidentity frames |
| delete the contact or multiparticle sector | **ATTEMPTED** | `g=0` leaves the stream mismatch; deleting `N>=2` deletes the required contact and seam domain |

There are more than five genuinely distinct attempted attacks. Separately,
two **unexecuted live routes** defeat any full-compiler impossibility claim:
local auxiliary/gauge or another non-product code is supported as an escape
class by Farrelly–Short [1], and Mlodinow–Brun [3] establish a free
three-dimensional distinguishable-walker construction with antisymmetric
restriction. Their exact Cycle-230 contact/constraint realizations remain
untested, so neither is mislabeled `RULED OUT BY PRIOR`.

### N2 — wall-independence audit

The raw observations “CAR statistics,” “six-mode capacity,” “stream parity,”
“frame sign,” and “block blanks” are not counted as five axiom walls. They are
sub-obligations within `C_local`. Capacity is constructively closed. Frame sign
has a bounded cocycle repair. Blank enforcement is a declared code/layout
condition. The only fatal residual for the declared local update is the
stream intertwining mismatch.

The inherited six-workstream set remains collapsed. Route 1 changes only
`C_local`; therefore no directional implication among the other five is
created. In particular:

| Pair class | first closes second? | second closes first? | Independent? |
|---|---:|---:|---:|
| `C_local` with each of `C_ref,C_num,C_wrap,C_int,C_source` | no | no | yes |
| any pair within `C_ref,C_num,C_wrap,C_int,C_source` | no new implication from Route 1 | no new implication from Route 1 | unchanged from Cycle 230 |

Compiling the CAR stream would not select a sea, number reference, winding
clock, interaction, or source. Conversely, none of those selections constructs
the direct physical-site map. No wall collapse or multiplication is claimed.

For completeness, the inherited directional pair audit is:

| Pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `C_ref,C_num` | no | no | yes |
| `C_ref,C_wrap` | no | no | yes |
| `C_ref,C_int` | no | no | yes |
| `C_ref,C_local` | no | no | yes |
| `C_ref,C_source` | no | no | yes |
| `C_num,C_wrap` | no | no | yes |
| `C_num,C_int` | no | no | yes |
| `C_num,C_local` | no | no | yes |
| `C_num,C_source` | no | no | yes |
| `C_wrap,C_int` | no | no | yes |
| `C_wrap,C_local` | no | no | yes |
| `C_wrap,C_source` | no | no | yes |
| `C_int,C_local` | no | no | yes |
| `C_int,C_source` | no | no | yes |
| `C_local,C_source` | no | no | yes |

### N3 — hidden-wall scan

The mandatory scan for `we assume`, `by construction`, `as is standard`, `the
framework provides`, `bridge context`, `background`, `naturally`, `obviously`,
`standard QFT`, `registered`, and `canonical` finds no load-bearing appeal.
“Standard prior machinery” occurs only in the novelty boundary and is backed
by primary sources [1–3]. “Supplied” labels explicit conditions.

The block scale/origin, blank pattern, mode placement, within-cell convention,
coin/contact/schedule, global order for the exact image, and local frame
cocycle are all promoted into the supplied-structure inventory. No hidden
condition is used to discharge the intertwining residual.

### N4 — residual matching

| Cited witness | Witness residual | Route-1 use | Match? |
|---|---|---|---:|
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:109-130` | `M64` intrinsic-CAR cell is not yet a bounded physical-`M2` compiler | attempts exactly that compiler interface for one direct code | yes |
| same file `:160-183` | stream is intrinsic fermionic `B A`; exterior coin/contact are `64 x 64` local cell gates | imports the exact three operations tested here | yes |
| same file `:43-80` | supplied contact is identity on one particle and has a nonzero seam block with `1/L^3` normalization | tests preservation of exactly those mass/contact fixtures | yes |
| `COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:60-76` | conditional rest/curvature/inertial agreement | reruns the one-particle subset only | yes, coexistence only |
| `MINIMAL_AXIOMS_2026-06-29.md:35-58` | physical lattice sites and one-site `M2` domain with proper-cubic structure | defines the physical-site target; does not imply a compiler | yes, interface only |
| Mlodinow–Brun [2] | scoped direct-occupation/local-creator barrier in `d>=2` | prior-art boundary and steelman context | no as a proof of this exact residual; not used as a witness |

No mismatched prior no-go is used to prove Route 1. The norm-two result comes
from the current executable witness.

### N5 — rhetoric and resolution audit

| Resolution | Tested | Narrow conclusion |
|---|---|---|
| per mode | all one-particle modes at held-out sizes | endpoint stream is exact here |
| per cell/block | all 64 local states algebraically; exact `Gamma(C)` and contact matrices | bounded onsite representation succeeds |
| per edge | exact JW interval formula and physical nearest-neighbor B geometry | endpoint-only gate omits remote interval parity |
| two-particle lattice-wide | every basis pair at `L=3,4,5` | declared endpoint compiler fails with exact norm-two witness |
| fixed global parity | even `N=2` witnesses | global sector restriction does not repair the declared code |
| frame | all 24 proper-cubic frames | exterior action passes; pure geometry fails 22; local cocycle repairs |
| sea/contact block | named `L=3` Cycle-230 `2p2h` subspaces | gate matrix element is retained; full sea evolution is not compiled |
| infinite lattice / arbitrary code | not tested | no general locality or compiler impossibility claim |

Thus “the direct compiler fails” always means the declared direct occupation
code and endpoint stream. It does not mean no direct even-algebra encoding can
exist at any overhead or with a non-product code.

### N6 — partial-closure paths

| Path | Status | What it could close |
|---|---|---|
| local diagonal frame cocycle | executed partial repair | closes the onsite coin mismatch at constant support but not full-update covariance |
| locally enforced auxiliary/gauge parity | live Route 2 | could replace the global interval parity by local constraints |
| staggered/time-multiplexed parity transport | live Route 3 | could carry parity information through an autonomous bounded schedule |
| distinguishable-walker antisymmetric code [3] | published free construction, untested here | could avoid local CAR creators; contact and local constraint remain to compile |
| different non-product block isometry | untested | could invalidate the product-occupation residual |
| local marker/admissibility realization of the period-three tiling | unbuilt | could retire the blank/block-origin condition without new ontology |

These are construction and import-retirement paths. No axiom amendment is
requested or drafted.

### N7 — steelman

> A hostile reviewer should reject any extrapolation from the norm-two witness
> to the full tournament. The witness targets a product occupation encoding,
> exactly the presentation known to expose Jordan-Wigner interval parity.
> Farrelly and Short [1] show that causal fermions admit finite-overhead local
> qubit-QCA representations once auxiliary modes and a constrained subsector
> are allowed, while Mlodinow and Brun [3] evade their earlier scoped barrier
> using distinguishable walker registers followed by antisymmetric-sector
> restriction. A local gauge/rishon encoding or autonomous staggered parity
> carrier may therefore compile this exact six-mode update. Even within the
> present block, the local frame cocycle repairs the onsite representation,
> showing that even a strong partial symmetry mismatch must be retested on the
> full stream before it is treated as an obstruction.

The steelman is compelling. It forces the status
`partial-attempt-with-honest-residual` and makes any shared-substrate or axiom
claim premature.

### N8 — cross-cycle echo

The required repository searches over no-go phrases, `NO_GO_LEDGER.md` files,
`spatial CAR`, `Jordan-Wigner`, `onsite-qubit`, and antisymmetric constructions
give these relevant echoes:

| Prior echo | Prior status | Route-1 effect | Applicable retirement mechanism |
|---|---|---|---|
| `TOE_INTERFACE_CONSTRUCTIVE_GATE_NOTE_2026-07-13.md`: hard-core and CAR share local occupations but differ in cross-site exchange | open interface | exact endpoint-sign witness executes that distinction on Cycle 230 | yes: explicit statistics/compiler construction, not terminology |
| `FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md`: spectral JW matrices are not a spatial onsite compiler | open | onsite block is built; local stream remains | yes: direct construction partially retires capacity only |
| Cycle 230 `C_local` | partial intrinsic CAR, physical compiler open | sharpens the direct route without closing `C_local` | yes: Route 2/3 constructive attempts remain required |
| `CUBIC_SPLIT_STEP_QW_QCA_PRIMARY_SOURCE_UNIQUENESS_AUDIT_2026-07-14.md`: finite auxiliary or antisymmetric-sector bridges keep block route open | open | confirms the present route failure is not route-independent | auxiliary or non-product sector construction |
| earlier fixed-block-origin warning in the same cubic audit | open | the period-three layout explicitly inventories its origin/blanks | local marker or block-origin orbit rather than axiom change |

No convention-only prior retirement removes interval parity from this declared
occupation code. Conversely, multiple prior constructive mechanisms keep the
overall compiler open. The cross-cycle audit therefore supports the narrow
route disposition and rejects axiom pressure.

## Verification

```text
python3 scripts/ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py
```

The runner is required to finish with zero failed checks. Predecessor runners
remain separate coexistence controls.
