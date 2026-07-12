# Finite Factorized Hilbert Data Do Not Uniquely Select Physical Graph, Dynamics, or Born Readout

**Date:** 2026-04-12 (original operational experiment); 2026-07-12
(first-principles replacement).
**Type:** no_go
**Status:** exact negative boundary. A bare finite tensor-factorized Hilbert
space fixes factor operator algebras and their disjoint-factor commutativity,
but the base and stated type conditions do not uniquely distinguish an
adjacency graph, a physical CPTP semigroup, or the Born member of the
contextual readout family. The theorem is a non-entailment result, not a
positive one-axiom reduction or a ban on writing definitions from Hilbert data.
**Audit-status authority:** independent audit lane only.
**Runner:**
[`finite_factorized_hilbert_physical_selector_nonuniqueness_2026_07_12.py`](../scripts/finite_factorized_hilbert_physical_selector_nonuniqueness_2026_07_12.py)
**Framework comparison:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

## The question

Can the following data and type conditions alone uniquely distinguish a
physical graph, physical dynamics, and physical Born readout?

\[
  B=\left(I,\{\mathcal H_i\}_{i\in I},
  J:\bigotimes_{i\in I}\mathcal H_i\overset{\mathrm{unitary}}{\longrightarrow}\mathcal H
  \right),
  \qquad 2\le |I|<\infty,\quad 2\le\dim\mathcal H_i<\infty .
\]

Here `B` is the smallest precise reading of “a finite Hilbert space with local
tensor-product structure”: the factors and the tensor identification are
supplied, but no graph, Hamiltonian, time action, measurement context, or
probability functional is included.

Use one fixed expansion signature throughout. An expansion is a triple

\[
 \Sigma=(G,\{\mathcal D_t\}_{t\ge0},R),
\]

where `G` is a simple graph on `I`, `D_t` is a strongly continuous CPTP
semigroup on density operators with `D_0=id`, and `R` assigns a normalized
nonnegative probability vector to each nonzero state and ordered orthonormal
measurement context. These are type conditions only. They impose no relation
between the three fields and do not label any field “physical.”

The answer is no on this precise surface. This is stronger than observing that
a particular runner does not find a derivation. The same `B` has explicit
expansions satisfying the same type conditions that differ on each proposed
physical selector. Therefore the base and type conditions do not uniquely
distinguish one expansion as physical.

There is a useful dichotomy behind the wording:

1. If “local” means only factor-local operator algebras, the theorem below
   applies and no adjacency graph follows.
2. If “local” already includes a graph, a local Hamiltonian, or a readout
   rule, those objects are premises inside the word “local”; reading them back
   out is definitional compression, not derivation.

## Exact underdetermination theorem

### Theorem

For every base object `B` above, the stated expansion type conditions:

1. do not uniquely distinguish a physical adjacency graph on `I`;
2. do not uniquely distinguish a physical CPTP semigroup, and in particular
   do not select the unitary member;
3. do not uniquely distinguish the Born member of the contextual readout
   family.

Separately, `B` does determine the embedded factor algebras
\(\mathcal A_i=J(\mathcal B(\mathcal H_i)\otimes 1_{I\setminus\{i\}})J^{-1}\)
and the exact implication
\([\mathcal A_i,\mathcal A_j]=0\) for \(i\ne j\).

The negative statements remain true if all factors have the same dimension.

### Proof strategy: same reduct, incompatible expansions

A uniquely forced physical selector would require the base axioms and stated
type conditions to exclude every expansion but one equivalence class. It is
enough to construct two expansions with the same reduct `B`, in the same
signature, that satisfy all stated type conditions and disagree.

This is not a claim that no formula can be written from `B`. The empty graph,
complete graph, identity channel, and quadratic amplitude formula are all
definable. The no-go says that `B` contains no premise that calls one such
formula physical and excludes the displayed alternatives.

#### Graph countermodels

Choose two distinct simple graphs on the same factor set, for example a path
`P_N` and the complete graph `K_N` when `N >= 3` (for `N=2`, use the empty and
one-edge graphs). Both use exactly the same factors and unitary tensor map.

To make the disagreement visible in operator support, choose nonzero traceless
Hermitian operators `X_i` on the factors and define, for either graph `G`,

\[
  H_G=\sum_{\{i,j\}\in E(G)} X_iX_j .
\]

Each `H_G` is Hermitian on the same `B`, and its displayed two-factor support
is `E(G)`. The path and complete graph have different degree multisets, so no
factor relabeling identifies them. The base object contains neither `G` nor
`H_G`; it is compatible with both. Hence the stated surface does not uniquely
distinguish either graph as physical.

Even demanding invariance under every permutation of identical factors does
not repair selection: the empty and complete graphs are both invariant under
the full permutation group. Naturality is a constraint on a proposed graph
rule, not a rule choosing one of those two outcomes.

#### Dynamics countermodels

On the same `B`, choose a non-scalar Hermitian factor involution `Z`, so
`Z^2=1`. Such an operator exists on every factor of dimension at least two.
One valid dynamical extension is the induced unitary CPTP group

\[
  \mathcal U_t(\rho)=U_t\rho U_t^\dagger,
  \qquad U_t=e^{-itZ},\qquad t\ge0.
\]

Another is the dephasing semigroup on density operators,

\[
  \Phi_t(\rho)=a_t\rho+b_tZ\rho Z,
  \quad
  a_t=\frac{1+e^{-2\lambda t}}2,
  \quad
  b_t=\frac{1-e^{-2\lambda t}}2,
  \quad \lambda>0.
\]

For `t>=0`, `a_t,b_t >= 0` and `a_t+b_t=1`, so `Phi_t` is completely positive and
trace preserving. Its off-diagonal terms in the `Z` basis are multiplied by
`e^{-2 lambda t}`, so `Phi_s Phi_t = Phi_(s+t)`. For `t>0`, it sends a
`Z`-superposition pure state to a mixed state and therefore is not unitary.
Both \(\mathcal U_t\) and `Phi_t` are strongly continuous CPTP semigroups in the same
expansion signature and live on the same Hilbert space. The base object does not name a
time parameter, a state ontology, reversibility, norm preservation, or a
one-parameter action, so it does not uniquely distinguish between them.

Stone-type reasoning is a valid conditional bridge: once a strongly
continuous unitary one-parameter group is supplied, it has a self-adjoint
generator. It does not derive the supplied group, physical time, or unitarity
from `B`.

#### Readout countermodels

Fix an orthonormal measurement context `C=(e_1,...,e_D)`. For any nonzero
state `psi` and any `p>0`, define normalized context probabilities

\[
  P_p(k\mid\psi,C)=
  \frac{|\langle e_k,\psi\rangle|^p}
       {\sum_j|\langle e_j,\psi\rangle|^p}.
\]

Every `P_p` is nonnegative and normalized in the supplied context. `p=2` is
the Born rule. `p=4` is a distinct contextual rule on the same Hilbert space.
For

\[
  \psi=(e_1+2e_2)/\sqrt5,
\]

the two distributions are

\[
  P_2=(1/5,4/5,0,\ldots),\qquad
  P_4=(1/17,16/17,0,\ldots).
\]

The bare base object contains no probability measure, measurement context,
noncontextuality condition, or rule connecting amplitudes to readout. Thus it
is compatible with both expansions and does not uniquely distinguish `p=2` as
the physical member.

Gleason-type reasoning is another valid conditional bridge: a normalized
noncontextual additive probability measure on projectors, in the theorem's
dimension domain, has Born form. The probability measure, its additivity and
noncontextuality, and the identification of projectors with physical outcomes
are additional premises. The theorem here does not claim that Born readout is
impossible to derive from a richer operational axiom set.

#### Exact positive survivor

If `A` acts only on factor `i` and `B` acts only on a distinct factor `j`,

\[
 (A_i\otimes 1)(1\otimes B_j)
 =A_i\otimes B_j
 =(1\otimes B_j)(A_i\otimes 1).
\]

Therefore disjoint factor algebras commute. This is an exact locality
statement that survives from the factorization alone. It is algebraic
factor locality, not adjacency, a finite propagation speed, a local
Hamiltonian, or a spacetime metric.

This completes the proof. The paired runner gives a finite `N=4` certificate
for all three incompatible-expansion constructions, the positive commutator
identity, and the Cartesian independence of the three selectors.

## Relation to the current framework surface

The current framework does not use `B` as its whole premise set. The Lattice
axiom in [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
supplies `Z^3` and nearest-neighbor adjacency directly. Consequently the
framework graph is not a Hilbert-space consequence; it is Lattice premise
content. The Qubit axiom supplies the one-site algebraic presentation.
Admissibility supplies a covariant nearest-neighbor availability rule. Record
supplies permanent records and finite scalar additivity.

That same framework note explicitly keeps Hamiltonians, transition weights,
Born probabilities, measurement contexts, update laws, and physical
persistence dynamics outside the axioms. The exact underdetermination theorem
is therefore consistent with the live framework boundary. It removes the
invalid “one Hilbert axiom derives all four structures” route; it does not
remove routes that start from the actual named framework axioms and add
retained bridge theorems.

## What the earlier operational tests established

The historical runner constructed local Hamiltonians, chose a Born `p=2`
readout, and defined graph edges from Hamiltonian support. Under those
choices, graph-support recovery and `I_3=0` were legitimate consequences.
They were not a derivation of the choices.

The earlier Test 4 also compared a participation ratio made from six
overlapping, unnormalized qubit-occupation marginals with a participation
ratio made from a normalized 64-outcome distribution. Those are different
sample spaces, so the reported spread ratio was not a valid common-space
localization statistic. The replacement runner deletes that comparison. No
numerical localization claim carries weight in the present theorem.

## Assumptions and imports

The no-go proof uses only finite-dimensional complex linear algebra and the
explicit definition of the base object `B`. There are:

- no observed or fitted values;
- no literature values;
- no selected Hamiltonian in the premise set;
- no probability, measurement, or noncontextuality premise;
- no graph or graph-extraction convention in the premise set;
- no claim that a richer operational reconstruction is impossible.

The displayed `X`, `Z`, graphs, dynamics, and `P_p` rules are countermodel
witnesses. They are not hidden premises of a positive derivation.

## Falsifier and exact scope

The theorem would be falsified by an explicitly stated admissibility or
naturality premise already contained in the claimed base surface, together
with a proof that this premise excludes every displayed counter-expansion and
leaves one physical equivalence class. Merely writing a rule such as “choose
the empty graph,” identity evolution, or `P_2` does not falsify the theorem:
the type conditions also permit the alternatives, and no base premise makes
that definition the physical selector. A rule that adds a graph, Hamiltonian,
time action, probability measure, measurement postulate, or richer framework
axiom changes the premise surface.

The result is not a no-go against:

- graph recovery from a supplied Hamiltonian and a supplied support rule;
- unitary evolution from supplied reversibility/norm-preservation and time
  assumptions;
- Born reconstruction from a supplied operational probability framework;
- the Lattice + Qubit + Admissibility + Record framework;
- any later bridge theorem that explicitly names and discharges its extra
  premises.

## No-go discipline gate (N1-N8)

### N1 — Alternative route enumeration

| Attack route | Attempt and result | Authority or direct-proof locator | Honesty marker |
|---|---|---|---|
| Factor-permutation naturality selects the graph | Full permutation symmetry permits both the empty and complete graphs; less symmetric path and complete expansions are explicitly nonisomorphic. Naturality does not select between compatible invariants. | This note, [Graph countermodels](#graph-countermodels), plus paired runner `graph_countermodels` | ATTEMPTED |
| Tensor factorization selects a local Hamiltonian | The same factor algebra admits `H_G` for every graph `G`, all-to-all operators, and `H=0`. Factorization defines support only after an operator is supplied. | This note, [Graph countermodels](#graph-countermodels); exact factor-local positive theorem at `docs/SINGLE_AXIOM_HILBERT_NOTE.md` (context, not a proof dependency) | ATTEMPTED |
| Wigner/Stone reasoning selects unitary time evolution | The route begins only after a continuous unitary time action is supplied. `Phi_t` is a nonunitary CPTP semigroup on the same base. | This note, [Dynamics countermodels](#dynamics-countermodels); supplied-action route at `docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md` (context only) | ATTEMPTED |
| Hilbert norm alone selects Born weights | `P_2` and normalized contextual `P_4` are distinct readouts on the same state and measurement context. A physical-identification premise is absent. | This note, [Readout countermodels](#readout-countermodels), plus paired runner `readout_countermodels` | ATTEMPTED |
| Gleason-type additivity selects Born weights | This can close a richer operational route, but it supplies a normalized noncontextual additive measure and outcome identification not contained in `B`. | `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_GLEASON_BUSCH_ROUTE_NARROW_NOTE_2026-05-21.md`, opening boundary and grounded lines 573-593 (context only) | ATTEMPTED |
| Current framework axioms collapse to the Hilbert base | Lattice supplies the graph and the framework explicitly withholds Hamiltonian, probability, and measurement dynamics. The route changes the premise surface. | [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), “Relation To Dynamics And Kinetic Branch Selection” and “Open Gates Outside The Axioms” | ATTEMPTED |
| Record additivity selects amplitude-square probabilities | Finite scalar additivity over disjoint records does not supply normalization over alternatives, a projector measure, or an amplitude-to-readout map. | Same minimal-axiom Record section; `docs/POST_RECORD_TRANSITION_KERNEL_INTERFACE_2026-06-06.md`, grounded lines 61-71 and 104 (context only) | ATTEMPTED |

The route count is seven. The no-go is restricted to the bare base object; all
named richer routes remain available as conditional positive programs.

### N2 — Wall-independence audit

The collapsed missing-selector set is:

- `graph selector`: chooses adjacency on the factor set;
- `dynamics selector`: chooses the physical time evolution;
- `readout selector`: chooses physical outcome probabilities.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| graph, dynamics | no: one graph admits both `U_t` and `Phi_t` | no: either dynamics can be placed on path or complete support | yes |
| graph, readout | no: one graph admits `P_2` and `P_4` | no: either readout can be used with either graph | yes |
| dynamics, readout | no: either dynamics admits either terminal readout | no: either readout is compatible with either dynamics | yes |

The runner enumerates all `2 x 2 x 2 = 8` combinations. Factor locality is not
a fourth wall; it is the positive theorem that survives.

### N3 — Hidden-wall scan

The proof and runner were checked for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.

- The finite factorization and dimension bounds are the entire explicit base.
- Graphs, `X`, `Z`, `lambda`, time, the PVM, and `P_p` appear only inside
  countermodel expansions.
- “Current framework” statements are linked contextual comparisons, not proof
  premises for the abstract theorem.
- Stone/Gleason names label conditional rescue routes; no external theorem is
  used to establish the countermodels.

No hidden premise changes the three-selector set.

### N4 — Residual matching

| Witness and durable locator | Witness residual | Current residual | Match? | Use |
|---|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), “Relation To Dynamics And Kinetic Branch Selection” (grounded lines 93-107) | the four live axioms do not supply Hamiltonian, weights, probabilities, or time evolution | whether the richer live framework already supplies the missing Hilbert-only selectors | partial: framework rescue only | context and route exclusion |
| This note, [Graph countermodels](#graph-countermodels), and paired runner `graph_countermodels` | nonisomorphic graphs satisfy the same base and graph type | unique physical graph selection | exact | load-bearing proof |
| This note, [Dynamics countermodels](#dynamics-countermodels), and paired runner `dynamics_countermodels` | unitary and nonunitary CPTP semigroups satisfy the same base and dynamics type | unique physical dynamics selection | exact | load-bearing proof |
| This note, [Readout countermodels](#readout-countermodels), and paired runner `readout_countermodels` | distinct normalized contextual rules satisfy the same base and readout type | unique physical Born selection | exact | load-bearing proof |

No earlier no-go is used as authority for the theorem. The proof is
self-contained, so a mismatched prior residual cannot inflate its support.

### N5 — Rhetoric audit

- **Per factor:** only the embedded algebra and disjoint-factor commutativity
  are claimed.
- **Per pair of factors:** graph adjacency is not selected; a pair can be an
  edge or a non-edge in expansions of the same base.
- **Whole finite factor family:** the theorem covers every finite `N>=2` and
  factor dimensions at least two; the runner is an `N=4` certificate, not the
  universal proof.
- **Per state and measurement context:** `P_2` versus `P_4` is exhibited on
  one state/PVM; the global negative claim is only absence of a selector in
  `B`, not a classification of all probability theories.
- **Per time map and semigroup:** the note proves a full continuous dephasing
  semigroup; it does not infer nonunitarity from one sampled time.
- **Infinite lattice, continuum, gravity, or quantum-field resolutions:** not
  tested and not claimed.

### N6 — Partial-closure paths

Audit states below are a 2026-07-12 grounding snapshot, not author verdicts.

| Path | Grounded current source/audit state | What it can close | What remains outside |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | approved `minimal_axioms` premise node; source `Type: meta` | `Z^3` nearest-neighbor adjacency as Lattice premise content | Hilbert-only graph derivation; Hamiltonian, dynamics, Born weights |
| `docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md` | author-hinted bounded/positive bridge; audit state `unaudited` in the grounding snapshot | strong continuity and unitarity on its supplied free-Dirac mass-shell action | selection of that carrier/action from `B` |
| `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md` | `bounded_theorem`, audit state `unaudited` in the grounding snapshot | finite ideal-record Born form under its effect-probability and record inputs | derivation of those operational inputs from `B` |
| `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_GLEASON_BUSCH_ROUTE_NARROW_NOTE_2026-05-21.md` | `no_go`, audit state `unaudited` in the grounding snapshot | identifies additivity as a Gleason/Busch hypothesis and blocks a circular route | a new operational probability premise or theorem |
| `docs/SINGLE_AXIOM_HILBERT_NOTE.md` | branch-local `bounded_theorem` proposal; independent audit pending | exact consequences after graph support, Hermiticity, and Born readout are supplied | uniqueness of the three physical selectors |

Defining “local tensor-product Hilbert packet” to include graph, local `H`, and
Born readout is a definition refactor, not new physics and not a Hilbert-only
derivation. The approved primitive registry was also checked: scale-reference,
kinetic-isotropy, and realized-state primitives supply none of the three
selectors and are not classified as walls.

These paths prevent a broader “no derivation is possible” claim. They do not
defeat the narrow non-entailment theorem.

### N7 — Steelman

A hostile reviewer can argue that “Hilbert space” in physical use rarely
means the bare object `B`: quantum theory often includes rays as states,
projective measurements, transition probabilities, continuous symmetry
actions, composite-system rules, and operational noncontextuality. From that
richer package, Wigner-, Stone-, and Gleason-type theorems can turn much of
the desired structure into derived mathematics. The live framework is richer
in a different direction because Lattice already supplies adjacency and
Record supplies scalar additivity. Thus a meaningful one-package reduction
might still exist after the package is stated precisely.

The strongest in-repo support for this counterargument is the conditional
finite ideal-record construction at
`docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
and the supplied-action continuity construction at
`docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`.
Both were `unaudited` in the 2026-07-12 grounding snapshot, so they are
steelman routes rather than load-bearing theorem authorities here.

This steelman defeats any global claim that graph/unitarity/Born can never be
derived from a compact operational foundation. It does not defeat the shipped
claim: none of those operational structures occurs in `B`. Adding them is the
exact premise expansion the theorem isolates.

### N8 — Cross-cycle echo

| Prior wall | Grounded status and later mechanism | Could that mechanism retire this wall? |
|---|---|---|
| `docs/POST_RECORD_TRANSITION_KERNEL_INTERFACE_2026-06-06.md`: Record does not supply a transition kernel, Born weights, instrument, or Hamiltonian | `bounded_theorem`, `unaudited` in the 2026-07-12 snapshot; not retired on the base surface | yes, but only by deriving a separate transition/instrument bridge, exactly the richer-surface route left open here |
| `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`: finite Born form needs effect-probability and ideal-record inputs | `bounded_theorem`, `unaudited`; partially addressed by a conditional operational packet, not by unchanged Hilbert data | yes for a richer operational surface; no for the present base-only selector claim |
| `docs/OBSERVABLE_PRINCIPLE_P1_BRIDGE_GLEASON_BUSCH_ROUTE_NARROW_NOTE_2026-05-21.md`: Gleason/Busch takes additivity as input | `no_go`, `unaudited`; no grounded retirement | only a new derivation of the probability/additivity premise could apply |
| `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`: local algebra/admissibility does not select a kinetic law | `no_go`, `unaudited`; kinetic isotropy was checked and explicitly supplies no dynamics | a genuine dynamics selector could apply; the registered isotropy primitive cannot |

No analogous wall in this grounding snapshot was retired merely by choosing a
definition on an unchanged carrier. The mechanisms that can apply—an explicit
instrument, probability premise, or dynamics selector—are all preserved as
richer positive routes.

### Gate result

`PASS` for the narrowly scoped exact negative boundary. All N1-N8 items are
answered; seven alternative routes were examined, three independent selectors
were established by eight compatible combinations, and the strongest richer-
foundation steelman is outside the claim rather than silently foreclosed.

## Conclusion

A finite tensor-factorized Hilbert space is kinematics. It supplies factor
operator algebras and exact disjoint-factor commutativity. The base plus the
stated type conditions do not uniquely distinguish which factors are
physically adjacent, which CPTP semigroup is physical time evolution, or which
normalized contextual function of amplitudes is physical readout.

The missing “single-axiom derivation” therefore closes negatively on the bare
Hilbert surface. Positive work must start from a richer, explicit premise set:
the current framework's Lattice axiom for adjacency, a derived or supplied
dynamical bridge for evolution, and a derived operational probability bridge
for Born readout. Packaging those choices into one phrase is allowed as a
definition, but it is not a first-principles derivation.
