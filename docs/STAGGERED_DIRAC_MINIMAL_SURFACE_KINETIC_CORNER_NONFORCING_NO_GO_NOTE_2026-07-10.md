# Staggered-Dirac Minimal-Surface Kinetic/Corner Non-Forcing No-Go

**Date:** 2026-07-10
**Type:** no_go
**Scope:** The current four-axiom minimal surface does not select a nonzero
first-order staggered kinetic law or its eight-corner Bloch-symbol zero set.
There is an explicit model of Lattice, Qubit, Admissibility, and Record whose
physical matter law is the nonzero, Hermitian, number-conserving, nearest-neighbor,
translation/proper-cubic-invariant qubit-exchange interaction. Its
one-particle generator on `ell^2(Z^3)` has Fourier symbol
`2 sum_mu (1-cos k_mu)`, whose Bloch-symbol zero set is only the origin rather
than the eight staggered corners. The plus/minus plaquette-flux split and
finite wrap holonomy are additional sharpened choices after a kinetic surface
is supplied.
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict or effective status.
**Primary runner:**
[`scripts/staggered_dirac_minimal_surface_kinetic_corner_nonforcing_2026_07_10.py`](../scripts/staggered_dirac_minimal_surface_kinetic_corner_nonforcing_2026_07_10.py)
**Runner cache:**
[`logs/runner-cache/staggered_dirac_minimal_surface_kinetic_corner_nonforcing_2026_07_10.txt`](../logs/runner-cache/staggered_dirac_minimal_surface_kinetic_corner_nonforcing_2026_07_10.txt)

## 1. Question and relation to the realization gate

The canonical parent
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` already carries a
bounded conditional synthesis. It does not derive its statistics, kinetic
flux, finite boundary holonomy, or physical labeling premises from the
minimal surface.

This note attacks the genuinely new kinetic/corner residual only:

> Does the current minimal framework surface select a nonzero first-order
> staggered kinetic law, rather than another local cubic qubit-lattice law,
> and therefore force the eight BZ-corner zero set?

The answer is no. This is not a retyping of the positive canonical parent.
The separate claim identity is deliberate: downstream rows that consume the
bounded realization positively must never chain-satisfy merely because a
negative result is retained-grade.

The earlier matter-statistics and generation-label questions already have
their own negative authorities. They are cross-cycle context here, not parts
of this headline theorem.

## 2. Exact allowed premise surface

The only physical premise is the current axiom node
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The relevant
source text is quoted verbatim.

**Lattice:**

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.
>
> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

**Qubit:**

> Each site has a domain of local possibilities.
>
> The full one-site possibility domain has algebraic presentation `M_2(C)`.
>
> A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently
> and adds no further primitive structure.
>
> No possibility is privileged. Possibilities are distinguished by the
> supplied algebraic structure alone.

**Admissibility:**

> There is one fixed nearest-neighbor admissibility rule, covariant under
> lattice translations and proper cubic rotations.
>
> For each site, the available possibilities are determined by, and vary
> with, the nearest-neighbor conditions.

**Record:**

> Records form.
>
> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.
>
> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

**Qualification:**

> These axioms state only their named primitive content. Further physical
> structure requires derivation, bridge, explicit admission, or approved
> primitive registration before use as a premise. In particular, a law may not
> depend on a choice not fixed by the supplied structure, unless that choice is
> admitted.
>
> A state is a configuration of records.
>
> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

The memo then states, again verbatim:

> Admissibility is not a dynamics axiom. It determines availability by a
> nearest-neighbor rule: for each site, the available possibilities are
> determined by, and vary with, the nearest-neighbor conditions. It does not
> choose a Hamiltonian or transfer operator, supply transition probabilities
> or weights, select a scalar or nonzero kinetic branch, assert a Dirac-square
> carrier, define a time metric, or provide a record-production process or
> physical persistence dynamics.

Forbidden as proof inputs are a supplied kinetic/action law, a pairing of the
three Pauli generators with lattice directions, the naive Dirac vertex,
P-KIN, P-SD, the minus-flux selector, a zero-set/relativistic-cone selection
rule, a finite wrap holonomy, the target eight-corner count, observed values,
and fitted selectors.

The approved
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
is not a premise of the theorem in §5. It is checked as a proposed rescue
route, and its own boundary says it supplies only `c_t=c_s`, not dynamics, a
selector, or a Lorentz-closure theorem. The approved
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
is likewise a contextual rescue route, not a theorem premise; it supplies
pointwise evaluation at a supplied realized state, not a state,
state-selection rule, or kinetic branch.

## 3. A complete current-`A_min` model

### 3.1 Local algebra and Admissibility

At every `x in Z^3`, take the full one-site possibility domain to be the
algebra `A_x = M_2(C)`. Rank-one projectors are the recordable local
possibilities used below. For a record configuration `R`, write `rho_y` for
the recorded projector at neighbor `y`, and set `rho_y=0` when that neighbor
is unrecorded. Define

```text
S_x(R) = sum_(y~x) rho_y.
```

Let `P_x(R)` be the projector onto the full largest-eigenvalue eigenspace of
`S_x(R)`, and define the available subdomain to be

```text
A_x(R) = P_x(R) M_2(C) P_x(R).
```

Thus the available rank-one record possibilities are exactly those whose
ranges lie in `P_x(R)`. If `S_x(R)` is scalar, `P_x(R)=I` and the whole
one-site domain `M_2(C)` is available.

This is one fixed rule on every site. It depends only on the unordered six
nearest neighbors, so translations and proper cubic rotations preserve it.
Under a common one-site unitary `U`, `S_x -> U S_x U^dagger` and the full top
eigenspace projector transforms covariantly. In the scalar case the available
set is the whole projective line, so the rule selects no arbitrary eigenvector.
It varies with conditions: six `|0><0|` neighbors allow `|0><0|`, while six
`|1><1|` neighbors allow `|1><1|`.

### 3.2 Record formation, permanence, and readout

A history is a monotone sequence of finite partial maps

```text
R_t : Z^3 -> {rank-one projectors},
```

where a new entry at `x` must be available under the preceding configuration,
and every old entry is unchanged. Such histories exist and are nonempty. For
example: start empty; lock `|0><0|` at the origin (all neighbors unrecorded,
so `S=0` and every possibility is available); lock `|1><1|` at `(2,0,0)`;
then lock `|+><+|` at `(1,0,0)`, whose two recorded axial neighbors contribute
the scalar matrix `I` and again leave every possibility available.

The domain of a partial map enforces one record per site; monotonicity gives
permanence. Define

```text
I(R) = sum_(x in dom R) Tr(rho_x) = |dom R|.
```

It depends only on record content, `I(empty)=0`, and is additive for disjoint
finite record domains. Both the qubit-exchange kinetic completion below and the
staggered comparator can be added to this identical axiom reduct without
changing any availability or record statement.

## 4. Infinite-`Z^3` qubit-exchange kinetic completion

Let `A` be the quasi-local inductive-limit algebra generated by the finite
tensor products of the `A_x`. On every undirected lattice edge define the
positive local interaction

```text
Phi_{x,y} = I - SWAP_{x,y},                           y~x.             (0)
```

The family `Phi` is finite range, nonzero, Hermitian, number conserving,
translation invariant, and proper-cubic invariant. Because `SWAP` commutes
with every common one-site frame change `U tensor U`, the law privileges no
one-site possibility or Pauli axis. It defines a quasi-local finite-range
interaction; no claim is made that the infinite extensive sum is itself a
bounded operator.

Choose any supplied homogeneous one-site reference and its orthogonal
one-flip state. Global frame invariance makes the choice immaterial. On the
resulting one-excitation Hilbert space `ell^2(Z^3)`, the associated bounded
generator is the cubic graph Laplacian

```text
Delta = 6 I - sum_(mu=1)^3 (T_mu + T_mu^dagger).                    (1)
```

Fourier transformation on `Z^3` gives

```text
Delta_hat(k)
  = 6 - 2(cos k_1 + cos k_2 + cos k_3)
  = 2 sum_mu (1-cos k_mu)
  = 4 sum_mu sin^2(k_mu/2).                                        (2)
```

Every term in the final expression is nonnegative. Therefore
`Delta_hat(k)=0` iff every `k_mu=0 mod 2pi`. At the eight corners
`k_mu in {0,pi}`, equation (2) equals `4 h`, with `h` the corner Hamming
weight. Exactly one corner is null, not eight.

The law is compatible with the record surface because current `A_min` states
no relation identifying availability projectors or records with kinetic
coefficient algebras. Supply the law domain by the condition “`R` is a lawful
finite record configuration,” and define `L(R)=Phi` for every such `R`. The
law therefore gives exactly one answer at every state in its domain and, being
constant on that domain, privileges no record state.

## 5. Theorem

> **Theorem (minimal-surface kinetic/corner non-forcing).** Lattice, Qubit,
> Admissibility, and Record do not select a nonzero first-order staggered
> kinetic law or the associated eight-corner Bloch-symbol zero set. This
> remains true after additionally asking for a nonzero,
> Hermitian, number-conserving, nearest-neighbor, translation-invariant, and
> proper-cubic-invariant physical matter law.

**Proof.** Sections 3-4 construct a model of every allowed premise and every
additional property named in the theorem. Its physical matter law is the
qubit-exchange finite-range interaction `Phi`; its one-particle generator is (1),
whose exact infinite-lattice Bloch symbol is (2). Its zero set contains only
`k=0 mod 2pi` and does not equal the staggered kinetic/corner conclusion. A
universal selection claim is false when one model of all its premises carries
a different physical law. Therefore the minimal surface does not select the
staggered kinetic or its eight-corner Bloch-symbol zero set. QED.

This no-go is about selection, not mathematical definability. One can write a
Kawamoto-Smit matrix on the same lattice, just as one can write many other
operators. The conclusion denied is that the framework premises designate it
as the physical kinetic law.

## 6. Sharpened conditional coordinates

The runner also checks two downstream coordinates. They are not independent
premises of the headline proof.

1. On the sign-link surface, the uniform plus system has plaquette flux `+1`
   and the Kawamoto-Smit system has flux `-1`. Flux is invariant under
   site-local `Z_2` gauge changes, so the systems are inequivalent.
2. For the same local Kawamoto-Smit law on a `4^3` torus, PBC has eight exact
   corner null vectors while wrap holonomy `(-1,-1,-1)` has none (minimum
   singular value `sqrt(3/2)`). This is a finite regulator statement, not an
   infinite-lattice boundary theorem.

These reproduce the sharp boundary of
[`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md):
within its licensed bilinear surface, symmetry collapses the candidates to
plus/minus flux classes but does not select the minus class.

## 7. No-Go Discipline Gate

**Status: PASS for the theorem in §5.** The headline has one wall: the minimal
surface does not select a physical kinetic law. Flux and wrap holonomy are
nested sharpeners, not inflated into additional axioms.

### N1 — alternative-route enumeration

| Route | Honesty marker | Positive attack | Result and authority |
|---|---|---|---|
| symmetry/naturality uniqueness | `ATTEMPTED` | demand a nonzero local Hermitian number-conserving law with every Lattice symmetry | `Phi` satisfies all demands but is graph-Laplacian, so uniqueness fails; runner M01-M04/K01-K05 |
| Admissibility-variation selector | `ATTEMPTED` | identify the varying availability rule with kinetic coefficient projectors to exclude the scalar branch | the explicit covariant top-eigenspace rule varies while remaining independent of kinetic coefficients; runner R01-R05; current axiom text says Admissibility is not dynamics |
| `Cl(3)` vector/scalarization | `ATTEMPTED` | pair Pauli generators with axes, then spin-diagonalize to force the minus-flux class | Qubit says the `Cl(3,0)` presentation adds no primitive structure; the plus-flux class survives the retained-bounded two-class theorem cited in §6 |
| approved kinetic isotropy | `RULED OUT BY PRIOR` | use `c_t=c_s` to force first-order staggered dynamics | the linked primitive explicitly supplies no dynamics, selector, or Lorentz-closure theorem |
| Record/realized-state selection | `ATTEMPTED` | let formation or the realized state select the kinetic branch | the explicit nonempty record history coexists with `Phi`; the linked realized-state primitive supplies no state-selection or kinetic rule |
| isolated-zero/spectral criterion | `ATTEMPTED` | require eight isolated first-order zeros as the admissibility test | this inserts the target zero-set criterion, which is absent from the verbatim premise surface; `Phi` is an allowed model until such a rule is separately derived |

The six routes occupy distinct classes: symmetry, local representation,
Admissibility semantics, approved primitive, Record/state, and spectral
selection.

### N2 — wall-independence audit

Define `W_K` as physical kinetic-law selection from the minimal surface,
`W_F` as selection of minus flux after a sign-link kinetic surface is supplied,
and `W_H` as finite wrap-holonomy selection after the local law is supplied.

| Pair | Closing first automatically closes second? | Closing second automatically closes first? | Independent? |
|---|---|---|---|
| `W_K`, `W_F` | no: a selected non-staggered law need not define the sign-link flux bit | no: choosing minus flux does not derive why that kinetic surface is physical | yes |
| `W_K`, `W_H` | no: a physical local law does not select finite wrap signs | no: wrap signs do not select a physical bulk law | yes |
| `W_F`, `W_H` | no: plaquette flux does not fix torus holonomy | no: torus holonomy does not fix plaquette flux | yes |

The theorem claims closure only of the negative `W_K` selection question.
`W_F` and `W_H` are separately reported conditional coordinates, not counted
as additional headline walls. The collapsed headline wall set is `{W_K}`.

### N3 — hidden-wall scan

| Trigger/close variant | Occurrence | Classification |
|---|---|---|
| “framework/minimal surface supplies” | §2 | verbatim linked Class-A axiom text; no enlargement |
| “by construction” | §§3-4 in substance | explicit countermodel definitions, not premises asserted of every model |
| “standard” | quasi-local/Fourier mathematics | non-load-bearing mathematical infrastructure; no physical selector |
| “canonical” | absent from the theorem/proof | no hidden uniqueness premise |
| “background” / “naturally” / “obviously” | absent from the theorem/proof | none |
| finite torus | §6 | explicit regulator support only; not used for the infinite proof |

No hidden admission is promoted into the headline proof.

### N4 — residual matching

| Witness | Witness residual | Residual used here | Match? |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), lines 106-119 | axioms choose no Hamiltonian/kinetic branch | `W_K` | yes |
| [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md), lines 84-106 | minus-flux bit is unforced on its licensed kinetic surface | `W_F` sharpener only | yes for `W_F`; not cited as proof of `W_K` |
| [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), lines 62-75 | `c_t=c_s` supplies no dynamics/selector | contextual isotropy rescue route against `W_K` | yes; not a theorem premise |
| [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md), lines 34-45 and 58-65 | supplied realized-state slot carries no selection rule | contextual Record/state rescue route against `W_K` | yes; not a theorem premise |
| `docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md:6-19` | representative selection after assuming the licensed kinetic structures carry availability | full `W_K` | no; context dropped as authority because its licensed-surface semantic premise is stronger than current `A_min` |

No nonmatching prior result is used as evidence for the headline theorem.

### N5 — rhetoric/resolution audit

| Resolution | What is established | What is not claimed |
|---|---|---|
| per-site | exact `M_2(C)` possibility domain and basis-independent `SWAP` interaction | no per-site momentum or corner statement |
| nearest-neighbor edge | exact finite-range interaction `Phi` on every `Z^3` edge | no continuum or empirical interpretation |
| per-mode | exact infinite-lattice Fourier symbol (2), whose zero set contains only the origin | no normalizable infinite-volume zero eigenvector or finite-boundary statement is inferred from it |
| finite block | `2^3` Hamiltonian restriction and `4^3` spectra reproduced by the runner | finite quotients are not substituted for the infinite model |
| lattice-wide | quasi-local interaction family and bounded one-particle generator on `ell^2(Z^3)` | no claim that the infinite extensive Hamiltonian sum is bounded |
| finite torus holonomy | PBC versus `(-1,-1,-1)` result only | no universal “APBC” or thermodynamic boundary theorem |

The phrase “not selected” is used only at the model-theoretic law level
established by the infinite construction.

### N6 — partial-closure paths and primitive/convention scan

| Path | Current role | What it closes | What it does not close |
|---|---|---|---|
| `docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — `audited_clean` / `retained_bounded` | declared-premise consequence map | composition after statistics, flux, holonomy, and labeling inputs | derivation of those inputs from the minimal surface |
| `docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` — `audited_clean` / `retained_bounded` | exact bounded narrowing | all licensed sign-link systems reduce to plus/minus flux; absorption on minus branch | physical kinetic-surface selection or the flux bit |
| `docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md` — `unaudited` | conditional route context | representative selection after identifying availability carriers with kinetic coefficients | exhaustive bridge from the axiom's rule to those coefficients; the explicit rule in §3 is a counterexample to exhaustiveness |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` — registered axiom-premise primitive (`meta`) | approved contextual rescue route | `c_t=c_s` only | dynamics, flux, zero set, or kinetic branch |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` — registered axiom-premise primitive (`meta`) | approved contextual rescue route | pointwise evaluation at a supplied state | state or kinetic selection |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` — registered axiom-premise primitive (`meta`) | units-only rescue scan | conversion by one supplied dimensionful scale | every dimensionless selector, kinetic law, flux, or zero set |
| `docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:87-92` — registered owner-governed residual | flavor occupancy/readout governance only | its recorded AC atoms | above-`C3` taste/Dirac/chirality or kinetic content |
| explicit wrap-sign convention in §6 — no authority status claimed | finite regulator convention | selects a finite torus sector | bulk physical law |

No partial path is misclassified as a new axiom. A future derived bridge that
excludes the model of §§3-4 would narrow or invalidate this no-go on its exact
scope.

### N7 — strongest steelman

> A hostile reviewer should argue that the `Cl(3)` presentation already
> contains a vector triple matching the three lattice axes, while the
> Admissibility variation clause requires nonconstant directional projectors;
> coupling those structures gives a first-order Clifford kinetic vertex,
> spin diagonalization gives Kawamoto-Smit phases, and the isolated eight-zero
> spectrum then distinguishes the physical branch. The qubit-exchange graph
> Laplacian would be irrelevant because it fails this intended
> availability-to-kinetic identification.

This would defeat the no-go only if the intended identification were a theorem
of current `A_min`. It is not: the linked
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), lines 49-53 and
57-61, says the compatible `Cl(3,0)` presentation adds no further primitive
structure and requires only that available possibilities vary with neighbor
conditions. Section 3 gives a rule satisfying that text, including covariance
and no-preference at degeneracy, without identifying availability with kinetic
coefficients. Section 4 supplies the corresponding symmetric physical law.
Thus the steelman proposes an additional semantic bridge; it does not find a
violated premise in the countermodel.

### N8 — cross-cycle echo

| Prior wall | Current status/mechanism | Could the retirement mechanism close `W_K`? |
|---|---|---|
| `docs/STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md` — `audited_clean` / `retained_no_go` | hard-core/CAR frame nonselection remains an exact negative boundary; bounded work proceeds by explicit statistics premise | no; it is an analogous premise-vs-selection wall, not a kinetic selector |
| kinetic two-flux-class note (§6) | plus branch remains the explicit countermodel inside the licensed surface | no current retirement; a valid exhaustive Admissibility bridge could close only its flux sub-residual |
| `docs/STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` — `audited_clean` / `retained_no_go` | physical names close by convention, not derivation | no; naming convention has no kinetic content |
| canonical bounded realization parent | declares extra premises and composes consequences | no; it is the legitimate bounded path already preserved |
| owner-governed AC adoption | governance retires specified occupancy/readout atoms with explicit boundaries | no; its boundary explicitly supplies no above-`C3` taste/Dirac/chirality content |
| registered primitive route | kinetic isotropy was adopted with a narrow structural boundary | no; the primitive explicitly supplies no dynamics or selector |

Every similar retirement mechanism has been tested against the actual kinetic
wall. None supplies the missing physical-law selection.

## 8. Imports and boundaries

| Item | Class | Role |
|---|---|---|
| four current axioms | accepted axiom premise | only physical premise |
| kinetic-isotropy, realized-state, and scale-reference primitives | accepted framework primitives | contextual rescue-route scan only; none is a theorem premise, and their registered boundaries supply no kinetic selector |
| finite-dimensional algebra, quasi-local inductive limit, Fourier transform | mathematical infrastructure | exact construction/proof |
| qubit-exchange interaction and top-eigenspace availability rule | explicit countermodel choices | establish existence of a non-staggered model; not asserted as derived physical laws |
| PBC and `(-1,-1,-1)` holonomy | finite regulator choices | sharpened comparison only |
| observations, fits, PDG/lattice-MC values | absent | none |

The theorem does not say staggered fermions are inconsistent, impossible, or
empirically false. It says only that the present premise surface does not
select that kinetic/corner realization over the explicit alternative model.

## 9. Runner and expected result

```bash
python3 scripts/staggered_dirac_minimal_surface_kinetic_corner_nonforcing_2026_07_10.py
```

Expected deterministic summary:

```text
TOTAL: PASS=27 FAIL=0
VERDICT: exact kinetic/corner non-forcing countermodel VERIFIED.
```

The runner checks finite restrictions and formula certificates. The
infinite-`Z^3` no-go is the analytic construction and Fourier proof in §§3-5,
not an extrapolation from the finite matrices.
