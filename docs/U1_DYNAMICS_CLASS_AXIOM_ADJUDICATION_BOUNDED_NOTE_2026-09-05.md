---
claim_id: u1_dynamics_class_axiom_adjudication_bounded_note_2026-09-05
claim_type: bounded_theorem
claim_scope: "On the supplied period-two role compilation of the cubic gauge complex onto Z^3 sites, for the seven items of the weak-field edge/face dynamics class declared by the open PR #7917 (an evidence address, not a premise): the gauge-and-chain-compatibility item and the translation-and-proper-cubic-covariance item are each theorems conditional on the remaining items (compatibility from payload, locality, covariance and the vector-type transformation law of the payload; covariance from payload, locality, compatibility and conservation with no orientation premise), proved by the exact classification of every covariant nearest-neighbor real linear generator on the one-component payload under all sixteen signed-permutation representations and by the exact nullspace of the gauge-plus-chain constraints; covariance additionally has a named axiom lever (the Lattice no-privileged-site sentence under a law-level reading). The payload, time-rule, locality and conservation items are recorded as supplies (locality conditional on an identification premise), each with an explicit alternative law that satisfies every axiom sentence relied on and violates that item, exact on the side-4, side-6 and side-8 compiled tori. The sampling identification of the dynamics with the Admissibility rule is shown to decrease the field energy. No item is derived from the four axioms alone, no dynamics class is selected, and no continuum, infinite-volume, Record-readout or electromagnetic statement is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py
---

# The Declared Edge/Face Dynamics Class Against the Four Axioms: Compatibility and Covariance Are Mutually Redundant; Payload, Time Rule, Locality and Conservation Are the Supplied Residual

**Date:** 2026-09-05
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This note changes no audit
verdict, TOE score, axiom, or approved primitive, and it proposes none.
**Axiom boundary:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
**Primary runner:**
[`scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py`](../scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py)
**Cached receipt:**
[`logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt`](../logs/runner-cache/u1_dynamics_class_axiom_adjudication_2026_09_05.txt)
(`TOTAL: PASS=95 FAIL=0`; exact integer, rational and symbolic arithmetic only)

**Target claim, in one sentence.** For each of the seven items of the
declared dynamics class quoted in section 1, decide — from the four axiom
sentences plus the supplied role compilation, with every hypothesis carried
through every step — whether the item is DERIVED, DERIVED-CONDITIONAL-ON a
named premise, or a GENUINE SUPPLY, and for every non-derived item exhibit an
explicit alternative law that satisfies every axiom sentence relied on and
violates the item.

Evidence addresses. The class is declared in the open, unlanded PR `#7917`
(branch `physics-loop/u1-maxwell-generator-uniqueness-classification-20260903`);
the compilation is declared in the open PR `#7913`; the generator and its
time-selection fork in `#7915`; the finite tick in `#7920`; the radius-one
obstruction in `#7921`. None of these is a dependency of this note; nothing
from them is used as a premise; each is quoted only at its own scope. The
pack for this block is `.claude/science/physics-loops/u1-maxwell-landing-core-20260905/`
(provenance pointer only).

## Result up front

| item (as declared) | verdict | from what | existence witness (all exact) |
|---|---|---|---|
| 1. one real `E` per edge-role site, one real `B` per face-role site | GENUINE SUPPLY (with one derived bound: at most eight real linear coordinates per site, from Qubit's `M_2(C)`) | no axiom sentence names which coordinate of the possibility domain evolves, nor that one does | a complex (two-real-component) law with an onsite phase: conservative, nearest-neighbor, covariant, gauge-compatible |
| 2. real, linear, first-order, continuous-time evolution | GENUINE SUPPLY; the memoryless (first-order) clause alone is DERIVED-CONDITIONAL-ON(SI) | the axioms name no time parameter (the memo lists "time metric" and "physical persistence dynamics" among the open gates); the Qualification's one-answer sentence gives memorylessness once the field configuration is taken as the law's state (SI) | a reversible finite tick (exact modified-energy conservation, no continuous parameter); a nonlinear constitutive law conserving a positive quartic energy; the complex law (not one real component); the sampling law (stochastic, section 5) |
| 3. a site derivative reads itself and its six physical nearest neighbors only | DERIVED-CONDITIONAL-ON(IP-B); the premise is target-equivalent for this item | "six physical nearest neighbors" is a Lattice fact; what they are (two vertices and four faces for an edge; four edges and two cubes for a face; never a same-role site; opposite-role couplings only at odd distance) is a compilation fact; that a dynamics reads only them is inherited only if the dynamics reads what the Admissibility rule reads (IP-B) | the improved-curl law `L = C(1 + eps C^T C)`: conservative, covariant, gauge- and chain-compatible, minimal payload, support radius three |
| 4. translation and proper-cubic covariance | DERIVED-CONDITIONAL-ON(items 1, 3, 5, 6, 7) with no orientation premise; also DERIVED-CONDITIONAL-ON(LR) from the axioms | nearest-neighbor face rows with `L d_0 = 0` and `d_2 L = 0` are exactly the multiples of the oriented curl by one lattice-wide scalar (exact nullspace); conservation then fixes the reverse block and kills onsite terms, and the result is covariant. From the axioms: Lattice's "No site is privileged. Sites are distinguished by the supplied lattice structure alone." read as binding the dynamical law (LR) | an anisotropic law (orientation coefficients 1, 2, 3): conservative, nearest-neighbor, gauge-invariant, not covariant — and, as a consequence, not magnetic-Gauss preserving; a site-privileging law (one face row doubled) |
| 5. the edge-to-face map is invariant under `A -> A + d_0 lambda` and preserves the magnetic Gauss row | DERIVED-CONDITIONAL-ON(items 1, 3, 4, 7 and OL, the vector-type transformation law of the payload) | the sector-preserving stabilizer of a face-role site (a `D_4` of proper rotations named by the Lattice axiom) fixes exactly the oriented-curl stencil on the four boundary edges; all sixteen signed-permutation payload representations are classified: eight admit a coupling, four distinct couplings result, and only the curl is gauge- and chain-compatible | the unoriented law on the unsigned incidence `S`: conservative, covariant (scalar representation), nearest-neighbor, minimal payload, `S d_0 != 0`, `d_2 S != 0`, no soft mode at zero momentum |
| 6. a positive, diagonal, proper-cubic field energy is conserved | GENUINE SUPPLY | inside the covariant family `[[u, r C^T],[q C, v]]` conservation is the two-condition cut `u = v = 0`, `w_E r + w_B q = 0`; no axiom sentence names a conserved quantity, a reversible flow, or a stationary measure for a field evolution; the sampling identification of the dynamics with the Admissibility rule decreases the energy (section 5) | damped (`u = v < 0`), overdamped (`u = 0, v < 0`: slow root `-s^2 - s^4/gamma - ...`, the diffusive branch), same-sign (`r = +q`: real eigenvalues) — each nearest-neighbor, covariant, gauge- and chain-compatible, minimal payload |
| 7. no vertex, cube, extra coin or hidden time payload | GENUINE SUPPLY | no axiom sentence restricts which role sites carry an evolving coordinate | a scalar vertex payload `phi`: conservative, nearest-neighbor (a vertex reads its six edges), covariant, gauge-compatible edge-to-face map; a third branch per nonzero momentum (the edge operator becomes the Hodge Laplacian) and a two-speed conservative family |

Two consequences for the declared class, at its own scope.

- Items 4 and 5 are mutually redundant inside the class: 5 follows from
  1, 3, 4, 7 once the payload transforms as an oriented edge and face
  quantity; 4 follows from 1, 3, 5, 6, 7 with no orientation premise at all.
  The declared class's independent content is the payload (items 1 and 7,
  with the vector-type transformation law), the time rule (item 2), the
  locality (item 3), the conservation (item 6), and one of the two symmetry
  items.
- The exact residual supply of the terminal relative to the four axioms is
  therefore: payload and its transformation law, deterministic real linear
  continuous time, nearest-neighbor locality (unless the identification
  premise IP-B is granted), and positive diagonal energy conservation. None
  of these is reached by an axiom sentence; each has an exact existence
  witness below. Covariance has an axiom lever (LR) and compatibility follows
  from covariance; neither is reached without a named premise.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Every derived statement is an exact finite computation on the side-4, side-6 and side-8 compiled tori (integer, rational and symbolic arithmetic) plus a one-face stabilizer argument valid at every size; every conditional premise is named; every supply carries an explicit exact witness. No item is derived from the four axioms alone, no class is selected, and no infinite-volume, continuum, Record-readout or electromagnetic statement is made."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The classification does not derive that dynamics class from the axioms, and exact finite local tick selection remains open."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the light lane's terminal (the uniqueness classification of open PR #7917) is the consumer: its declared class can be restated with either the covariance item or the compatibility item dropped, and its residual supply is now item-exact — payload and transformation law, time rule, locality, conservation; the next derivation target is conservation, whose only live in-framework route (reflection positivity of a supplied transfer interpretation, section 12 N7) needs two supplied structures"
conditional_surface_status: "exact on the finite compiled tori of sides 4, 6 and 8 and by the one-face stabilizer argument at every even size; conditional on the named premises LR, IP-B, OL and SI where stated; no derivation of the declared class from the axioms"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 1. The setting: what is supplied, what the axioms say, what is named

**The declared class (quoted at scope from the open PR `#7917`).** "Declare
the following weak-field dynamics class on the role-compiled physical
lattice: 1. one real electric component lives at each edge-role site and one
real magnetic component at each face-role site; 2. evolution is real, linear,
first order, and continuous in time; 3. a site derivative may use its own
component and the dynamical components among its six physical nearest
neighbors, but no farther site; 4. the law is translation- and
proper-cubic-covariant; 5. the edge-to-face map is invariant under
`A -> A+d_0 lambda` and preserves the magnetic Gauss row; 6. a positive,
diagonal, proper-cubic field energy is conserved; and 7. no vertex, cube,
extra coin, or hidden time payload participates." Its own boundary: "The
classification does not derive that dynamics class from the axioms" and "The
four axioms do not currently select that class. In particular, they do not
state real linear first-order evolution, energy conservation, minimal
`(E,B)` payload, or continuous time." This note adjudicates that boundary
item by item; it neither uses the class as a premise nor treats the PR as
authority.

**The supplied role compilation (a named supply, never derived here).** On an
even periodic cubic lattice every site carries a role label equal to its
coordinate parity up to one of eight sector offsets; Hamming weight zero,
one, two, three is vertex, edge, face, cube; an edge on axis `i` is
oriented along `e_i`; a face with normal `e_k` has the ordered plane pair
`(i, j)` with `e_i x e_j = e_k`. The oriented incidence maps are the vertex
gradient `d_0`, the edge-to-face curl `C` (a face reads `E_i(f - e_j)`,
`-E_i(f + e_j)`, `E_j(f + e_i)`, `-E_j(f - e_i)`), and the face-to-cube
divergence `d_2`. This is the doubled incidence declared in the open PR
`#7913` ("exactly eight translated parity-role sectors on even tori"); the
runner rebuilds it from the parity rule alone and re-proves its facts. Sector
zero is used throughout; the law-level statements hold in every sector by
translation.

**The axiom sentences relied on (verbatim, checked by the runner against the
memo).** Lattice: "Physical sites are the points of the cubic lattice `Z^3`,
with nearest-neighbor adjacency, standard translations, and proper cubic
rotations about each site." and "No site is privileged. Sites are
distinguished by the supplied lattice structure alone." Qubit: "The full
one-site possibility domain has algebraic presentation `M_2(C)`." and "No
possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone." Admissibility: "There is one fixed
nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." and "For each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions." Record: "Records form." "A site never carries
more than one record; records are permanent." "Only records are readable. A
readout value is determined by record content alone. A site with no record
cannot be read." Qualification: "A law privileges no states. Its domain is a
supplied condition, and at every state where the condition holds it gives
exactly one answer." The memo's own boundary: "Admissibility is not a
dynamics axiom." It does not "choose a Hamiltonian or transfer operator ...
define a time metric, or provide a record-production process or physical
persistence dynamics"; "arrow, record-production dynamics, physical
persistence dynamics, time metric, and local observability of records"
remain outside axiom content; and "The 2026-08-13 owner-approved revision
removed the named scalar functional `I`, finite additivity over disjoint
record collections, and `I(empty)=0` from Record."

**Primitive registry check.** `docs/audit/data/axiom_premise_nodes.json`
was read: the scale-reference primitive is units only; the kinetic-isotropy
primitive supplies the structural ratio `c_t = c_s` and, by its own note, "is
not a new dynamics"; the realized-state primitive is pointwise evaluation
only. None is classified below as a wall, an import, or a source of bounded
status; none supplies any of the seven items.

**The named premises.** Every conditional verdict names one of these; none
is an axiom, and each is shown load-bearing by a witness.

- LR (law-level reading): the dynamical law is a law in the Qualification's
  sense, so that Lattice's no-privileged-site sentence and the
  Qualification's no-privileged-state sentence bind it, with the proper
  cubic rotations about each site counted as part of "the supplied lattice
  structure" because the Lattice axiom names them.
- IP-B (neighborhood inheritance): the dynamical rule at a site is a fixed
  function of the same six-neighbor conditions the Admissibility rule reads.
- IP-A (sampling identification, stronger than IP-B): the per-site update of
  the dynamics draws the site's value from the Admissibility conditional
  given the current neighbor conditions.
- OL (orientation law): the edge payload transforms as an oriented edge
  quantity and the face payload as an oriented face quantity — the vector
  components along the edge axis and the face normal — the same convention
  the compilation uses for its oriented link value.
- SI (state identification): the configuration of the dynamical components
  is the domain element on which the law acts, so that the Qualification's
  one-answer sentence applies to it.

## 2. Compilation facts, and which of them are lattice facts

The runner establishes exactly, on the side-4, side-6 and side-8 tori:

- the role census (`n^3/8` vertices and cubes, `3 n^3/8` edges and faces), the
  shell census (an edge sees two vertices and four faces; a face sees four
  edges and two cubes; a vertex six edges; a cube six faces), and the absence
  of any same-role nearest-neighbor pair;
- the parity theorem: the torus distance between an edge site and a face
  site is always odd, between two same-role sites always even. Hence an
  opposite-role coupling has physical radius one or at least three, and a
  same-role coupling has radius at least two;
- the chain identities `C d_0 = 0`, `d_2 C = 0` over the integers; every
  curl row couples a face to four nearest-neighbor edges with signs
  `(+1, +1, -1, -1)`;
- the eight parity translates satisfy the neighbor bit-flip rule (translation
  permutes sectors); every proper rotation about a site of every role type
  maps the role field onto one of the eight sectors, and rotations about a
  vertex or cube site fix the sector (24 each) while about an edge or face
  site exactly eight do;
- the oriented curl and the gradient are covariant under all 24 proper
  rotations about a vertex and under all even translations.

Adjudication of item 3's phrase "six physical nearest neighbors": that a
site has six nearest neighbors is the Lattice axiom (adjacency on `Z^3`).
Which roles they carry, that no same-role site is among them, and that a
face's boundary sits at physical distance one, are facts of the supplied
compilation, not of the lattice. That a dynamics reads only them is neither:
it is a property of a supplied dynamics, inherited only under IP-B.

## 3. Covariance forces the curl: the classification behind item 5

**Theorem (exact, side 4; stabilizer argument at every even size).** Let the
payload be one real component at every edge-role and face-role site,
transforming under the sector-preserving lattice symmetries by a signed
permutation. Every such transformation law is induced from a character of
the site stabilizer (a `D_4` of proper rotations about the site, all named by
the Lattice axiom); the characters are realized by tensor transport, so the
edge payload transforms as a scalar or as the vector component along its
axis, each optionally twisted by the rotation group's global sign character
(the parity of the axis permutation), and likewise the face payload as a
scalar or as the vector component along its normal. This gives sixteen laws. For each, the space of translation- and
proper-cubic-covariant real linear nearest-neighbor generators on the payload
is computed exactly as the nullspace of the covariance constraints on the 30
translation-covariant nearest-neighbor patterns:

- the onsite terms are always covariant (two dimensions);
- a covariant edge-face coupling exists exactly when the two characters
  agree on the in-plane 180-degree flip (eight of sixteen laws), and it is
  then unique up to scale in each direction (total dimension four);
- the eight coupling-admitting laws carry exactly four distinct couplings:
  the oriented curl `C` (for the vector/vector law and its global sign
  twist), the unsigned incidence `S` (scalar/scalar and its twist), and their
  two sign-twisted partners whose one-face stencils are `(1,-1,-1,1)` and
  `(1,-1,1,-1)`;
- exactly `C` satisfies `X d_0 = 0` and `d_2 X = 0`.

The one-face argument that makes this size-independent: the eight
sector-preserving proper rotations about a face-role site act on the four
boundary-edge values; the 90-degree rotation about the normal cycles them
with the vector signs `(a, b, c, d) -> (-d, a, -b, c)`, and the only stencil
invariant under it with the face value fixed is `(1, 1, -1, -1)`, the
oriented curl; for the scalar law it is `(1, 1, 1, 1)`. The runner performs
this stabilizer computation for all sixteen character pairs and separately
re-derives, by its own row reduction, that the gauge-invariant one-face
stencils are exactly the curl multiples.

**Verdict on item 5.** Given items 1, 3, 7 (one real component, nearest
neighbor, no other payload) and item 4 (covariance), the edge-to-face map is
a multiple of the covariant coupling; under OL that coupling is the oriented
curl, and both clauses of item 5 are then the chain identities of the
compilation. So item 5 is DERIVED-CONDITIONAL-ON(1, 3, 4, 7, OL). The
witness that OL is load-bearing is the unoriented law
`[[0, -S^T],[S, 0]]`: nearest-neighbor, covariant under the scalar
representation, conserving `(|E|^2 + |B|^2)/2`, minimal payload, with
`S d_0 != 0` and `d_2 S != 0`, and with no soft mode at zero momentum (the
unsigned incidence maps the three constant edge fields to three independent
face fields while the curl annihilates them). Relative to the four axioms
alone, item 5 inherits the status of its premises: OL is a supply (the
axioms fix no transformation law for a payload they do not name), and items
1, 3, 4, 7 are adjudicated in their own rows.

## 4. Compatibility forces covariance: the redundancy behind item 4

**Theorem (exact, side 4 in full generality; side 6 after the per-face
reduction).** Let each face row read only its four boundary edges with free
coefficients (96 unknowns on side 4). The constraints `L d_0 = 0` and
`d_2 L = 0` alone — no covariance assumed — leave exactly a one-dimensional
space, spanned by the oriented curl. The mechanism: gauge invariance on one
face star forces each row to be a multiple `q_f` of its own curl; the
magnetic Gauss identity around every cube then forces `q_f` equal on all six
faces of the cube (each cube edge lies in exactly two of them with opposite
signs), and cube connectivity makes `q_f` one lattice-wide scalar (on side
6, the reduced nullspace over the 81 face coefficients is the all-ones
vector). With item 6, the diagonal blocks vanish and the reverse block is the
weighted negative adjoint `-(w_B / w_E) q C^T`, so the generator is
`c [[0, -C^T],[C, 0]]` after normalization — covariant under all 24 proper
rotations and all even translations.

**Verdict on item 4.** DERIVED-CONDITIONAL-ON(1, 3, 5, 6, 7), with no
orientation premise: the oriented structure enters through `d_0` and `d_2`
inside item 5 itself. The anisotropic law with orientation coefficients
`(1, 2, 3)` is the witness in both directions: it is nearest-neighbor,
conservative, minimal-payload and gauge-invariant (`L d_0 = 0`), it is not
covariant, and — this is the same fact seen from the other side — it fails
`d_2 L = 0`. A second witness, one face row doubled, breaks translation
covariance while keeping every other item.

**The axiom lever.** Item 4 is the one item with a sentence of its own in the
axioms: "No site is privileged. Sites are distinguished by the supplied
lattice structure alone." A law with a site-dependent coefficient
distinguishes sites by something other than the supplied structure; a law
with an orientation-dependent coefficient distinguishes directions the
Lattice axiom's named rotations relate. Under LR — that the dynamical law is
a law in the Qualification's sense and so bound by these sentences — item 4
is DERIVED-CONDITIONAL-ON(LR), and the compilation's covariance (re-proved in
section 2) carries the covariance from the lattice to the compiled payload.
LR is weaker than the item (it is a reading of scope, not a statement about
any generator) and it is not forced: the Qualification allows "further
physical structure" to be supplied, and a supplied dynamics may be read as
exempt from the no-privileged-site sentence. The two witnesses above are the
laws LR excludes.

## 5. Conservation (item 6): a two-condition cut that no axiom sentence makes

Inside the covariant nearest-neighbor family of section 3 (vector/vector law)
the general generator is

```text
G = [[u I, r C^T],
     [q C, v I]],           u, v, q, r real.
```

Positive diagonal conservation, `M G + G^T M = 0` with `M = diag(w_E I, w_B I)`
and `w_E, w_B > 0`, is blockwise `2 w_E u = 0`, `2 w_B v = 0`,
`w_E r + w_B q = 0` (symbolic, checked). So item 6 is exactly the cut
`u = v = 0`, `r = -(w_B / w_E) q`, after which field rescaling leaves the
one-speed generator. The runner checks the surviving member exactly: metric
skew defect zero; `dH/dt = 0` on a random rational field; both Gauss rows
preserved; on the side-6 torus the edge operator `C^T C` satisfies
`Q(Q-3)(Q-6)(Q-9) = 0` with multiplicities `{0:29, 3:12, 6:24, 9:16}`, i.e.
two transverse branches at each of the 26 nonzero momenta, the 29 zero modes
being 26 gradients and three harmonic fields; the face operator has the same
nonzero multiplicities. Per-site energy `E_e^2 / 2` is not conserved even by
this member; only the lattice-wide sum is.

**No axiom sentence reaches the cut.** Admissibility determines a
distribution and its variation; the memo says it does not "choose a
Hamiltonian or transfer operator". Record's sentences concern locking,
uniqueness, permanence and readability of records; none names a quantity
conserved along an evolution of unrecorded possibilities, and "records are
permanent" cannot be read as a tick or as reversibility of a field law: a
site records once, so a field that evolves at a site is not a sequence of
records there. Qubit names a domain, not a flow on it; Lattice names sites
and their symmetries. The Qualification's "gives exactly one answer" is
about determination, not invariance.

**The three witnesses**, each nearest-neighbor, covariant, with the
gauge-compatible edge-to-face block `q C`, and minimal payload:

- damped, `u = v = -1/3`, `q = 1`, `r = -1`: `dH/dt < 0` on a random rational
  field; trace `-54` on side 6, so no positive form of any kind is conserved;
- overdamped, `u = 0`, `v = -2`, `q = 2`, `r = -1`: per transverse mode with
  symbol `s` the characteristic polynomial is
  `lambda^2 + gamma lambda + gamma s^2`, whose slow root is
  `-s^2 - s^4/gamma - ...` — the diffusive infrared relaxation of a gradient
  sampler — against the conservative member's `+/- i s`;
- same-sign, `r = +q`: `G^2 = diag(C^T C, C C^T)` has the eigenvalue `9 > 0`,
  so `G` has real eigenvalues and conserves no positive form.

**The sampling identification lands on dissipation.** The most direct way
to read a dynamics off the Admissibility sentence is IP-A: each site's
update draws its value from the Admissibility conditional given its
neighbors. For the harmonic static law
`pi(A) proportional to exp(-(kappa/2) |C A|^2)` the conditional mean at an
edge is the minimizer of the energy over that edge's value, so a sweep of
conditional-mean updates is the Gauss-Seidel iteration of `C^T C`: the runner
shows one sweep strictly decreases `A^T C^T C A / 2` on a random rational
field, and that this collapsed update reads edges at physical distance two
(the auxiliary face payload of the compilation is what makes the sampler
nearest-neighbor, at the price of a face alphabet the axioms do not name).
IP-A therefore yields items 3 and 4 and violates items 2 (stochastic) and 6
(dissipative). The identification premise that most directly buys locality
and covariance is the one that selects the diffusive branch of the
time-selection fork the open PR `#7915` displays; the conservative branch is
the one it does not select.

**Item 6 against the 2026-08-13 revision (the required edge case).** The
revision "removed the named scalar functional `I`, finite additivity over
disjoint record collections, and `I(empty)=0` from Record." A positive
diagonal field energy is a scalar, finitely additive over disjoint site
collections, zero on the empty collection: the exact shape of the removed
structure, transported from records to unrecorded field components. What
the revision implies: the current Record supplies no additive scalar of any
kind, so even a "record energy" is not axiom content, and re-supplying an
additive scalar is a bar item, not a derivation. What it does not imply:
(i) it does not forbid a supplied additive scalar as downstream structure
(the memo: such rows "must cite a separate retained authority or remain
conditional/open"); (ii) it is silent on conservation, which is dynamical —
additivity is static — and the pre-revision Record, which had `I`, named no
dynamics either, so item 6 was never Record content before or after the
revision. Item 6 needs three things: an additive positive scalar, a
dynamics, and the invariance of the first under the second; the revision
removed the first for records; the axioms never contained the second or
third for anything. Verdict: GENUINE SUPPLY.

## 6. The time rule (item 2): the axioms name no time parameter

The four axioms contain no time parameter, tick, order of events beyond a
site's single record, or update law: the memo lists "time metric" and
"physical persistence dynamics" among the open gates outside axiom content,
and "update laws" among the formation rules it does not supply. The
kinetic-isotropy primitive names "the emergent evolution tick" and fixes
only the ratio `c_t = c_s`; by its own note it is "not a new dynamics", and
whether "one tick is one edge in form" refers to a continuous parameter, a
finite-depth cycle, or only the regulator form is the interpretation
boundary the open PR `#7921` names for the owner; nothing here reads it as
selecting continuous or discrete time. So "continuous in time" is a supply.
Witness: the reversible finite tick — the three-shear leapfrog `B += (h/2) C E`,
`E -= h C^T B`, `B += (h/2) C E` — is checked exactly on side 6 at `h = 1/2`:
each shear reads one site and four opposite-role neighbors; `U(-h) U(h)` is
the identity; each shear preserves its Gauss row; the modified energy
`|B|^2/2 + |E|^2/2 - (h^2/8)|C E|^2` is conserved exactly and is positive
because `spec(C^T C) <= 9 < 4/h^2`; and the one-tick map is not `exp(h G)`.
This is the schedule the open PR `#7920` declares; it is re-derived here as a
witness that the same items 1, 3, 4, 5, 7 and a positive conserved energy are
carried by a law with no continuous parameter.

"Linear" is a supply. Witness: `dE/dt = -C^T (B + eps B^3)`,
`dB/dt = C E` (componentwise cube, `eps = 1/5`) conserves the positive
energy `|E|^2/2 + |B|^2/2 + (eps/4)|B|^4` exactly, is nearest-neighbor,
covariant and gauge-compatible, and fails homogeneity of degree one.

"Real" (one real component) is item 1's supply restated; the complex law of
section 7 is its witness. "Deterministic" is a supply; the sampling law of
section 5 is stochastic and satisfies every axiom sentence relied on — it is
the axiom-nearest dynamics there is.

The one clause with an axiom lever is "first order". Under SI — the field
configuration is the element of the law's domain — the Qualification's "at
every state where the condition holds it gives exactly one answer" says the
rate (or the next-step distribution) is a function of the configuration
alone: no memory, no velocity outside the state. That is memorylessness, the
first-order clause; it is weaker than item 2 (it gives neither linearity,
determinism, nor a continuous parameter), and it is not independent of item
7: any finite-order law is first-order on an enlarged payload, so
"first-order" is a statement about what the payload is. SI itself is a
supply: the Qualification's state is "a configuration of records", and the
components here are unrecorded possibilities whose connection to records is
the open bridge the open PR `#7915` lists as its wall W4.

## 7. The payload (items 1 and 7): what Qubit bounds and what it leaves

Qubit names the possibility domain and its presentation `M_2(C)`; it does
not name a coordinate on it that evolves, nor that exactly one real
coordinate does, nor which role sites carry one. The one thing it does fix:
a real-linear one-site coordinate system has at most `dim_R M_2(C) = 8`
components, so a linear one-site payload has at most eight real components
(a nine-component linear payload cannot be a one-site coordinate; a
composite object spread over several sites is outside this bound, as the
open PR `#7913` notes for its own alphabet). Every witness in this note fits
(one, one, two, one components per site).

Item 1 witness: one complex scalar per edge and face with an onsite phase
`theta = 3/7` — `dE/dt = -C^T B + i theta E`, `dB/dt = C E + i theta B` —
is a real-linear, nearest-neighbor, covariant, gauge-compatible law
conserving `sum |E|^2 + sum |B|^2` exactly, with two real components per
site. It is the minimal member of the payload class the open PR `#7921`
declares for its radius-one obstruction.

Item 7 witness: a scalar `phi` on the vertex-role sites,
`d phi/dt = -d_0^T E`, `dE/dt = d_0 phi - C^T B`, `dB/dt = C E`. It conserves
`(|phi|^2 + |E|^2 + |B|^2)/2` exactly, is nearest-neighbor (a vertex reads
its six edges, an edge its two vertices and four faces), is covariant, and
keeps the gauge-compatible edge-to-face block. Its edge operator `-G^2|_E`
is the Hodge Laplacian `d_0 d_0^T + C^T C` with multiplicities
`{0:3, 3:18, 6:36, 9:24}` on side 6: three branches at every nonzero
momentum instead of two — the longitudinal sector propagates. And the
extended covariant nearest-neighbor class (dimension seven: three onsite
terms, `C`, `C^T`, `d_0`, `d_0^T`, classified exactly) has a conservative
subfamily with two independent ratios (`a_2 = -w_V a / w_E` and
`r = -w_B q / w_E`), so with a vertex payload the conservative law is unique
only up to two speeds (`a = -2`, `a_2 = 2` is checked to conserve). Item 7 is
what makes the terminal's "up to one speed" true; the axioms do not supply
it.

## 8. Locality (item 3): what is a lattice fact and what needs the identification premise

Section 2 settled the phrase: six neighbors is the Lattice axiom; their
roles and the odd-distance parity of edge-face couplings are compilation
facts. That a law reads only nearest neighbors follows under IP-B and under
IP-A, and under nothing weaker: the Admissibility sentence is about the
admissibility rule, and the memo says that rule is not a dynamics. IP-B is
exactly as strong as item 3 for the dynamics (it says the rule reads the
six-neighbor conditions), so the verdict is DERIVED-CONDITIONAL-ON(IP-B)
with a target-equivalent premise — a sharpened residual, not a derivation.
Witness without IP-B: the improved curl `L = C (1 + eps C^T C)`,
`eps = 1/7`, on the side-8 torus: the generator `[[0, -L^T],[L, 0]]` is
conservative, gauge- and chain-compatible (`L d_0 = 0`, `d_2 L = 0`),
covariant, minimal payload, and its support radius is exactly three — the
smallest possible beyond one, by the parity theorem.

## 9. The seven-row obligation table

| item | verdict | derivation, or the exact terminal missing lemma | strength of the missing lemma against the item |
|---|---|---|---|
| 1 | GENUINE SUPPLY | missing: a sentence selecting one evolving real coordinate of `M_2(C)` at edge and face roles; the axioms give only the capacity bound eight | comparable: it is the item |
| 2 | GENUINE SUPPLY (memoryless clause DERIVED-CONDITIONAL-ON(SI)) | missing: a time parameter and its continuity, linearity, determinism; the Qualification gives memorylessness given SI | continuous time: target-equivalent (a time-parameter supply); linearity and determinism: comparable |
| 3 | DERIVED-CONDITIONAL-ON(IP-B) | IP-B restates the item for the dynamics | target-equivalent (`blocked-equivalent` in the registry sense) |
| 4 | DERIVED-CONDITIONAL-ON(1, 3, 5, 6, 7); DERIVED-CONDITIONAL-ON(LR) | section 4 (exact nullspace, no orientation premise); LR from Lattice's no-privileged-site sentence | LR is weaker than the item (a scope reading); the items 1, 3, 5, 6, 7 are adjudicated in their rows |
| 5 | DERIVED-CONDITIONAL-ON(1, 3, 4, 7, OL) | section 3 (exact classification; one-face stabilizer at every size) | OL is weaker than the item (a one-bit transformation-law choice among sixteen) |
| 6 | GENUINE SUPPLY | missing: a conservation, reversibility or self-adjointness principle for an evolution of unrecorded possibilities; the nearest kin was removed from Record on 2026-08-13 and never contained a dynamics | target-equivalent |
| 7 | GENUINE SUPPLY | missing: a sentence restricting the evolving coordinates to the edge and face roles | comparable: it is the item |

## 10. The exact residual, collapsed

Walls, as the supplies the terminal still rests on after this adjudication:
W-payload (items 1 and 7 together with OL), W-time (item 2), W-locality
(item 3, i.e. IP-B), W-conservation (item 6), W-symmetry (item 4 or item 5,
either one). Section 12 N2 gives the pairwise table; the collapse is: the
memoryless clause of W-time folds into W-payload (given SI); W-symmetry is
one wall, not two, because 4 and 5 imply each other in the presence of the
rest. Five walls; the four axiom sentences reach none of them without a
named premise, and W-symmetry is the only one with a named axiom lever.

## 11. What is and is not claimed

Claimed: the exact finite statements listed in sections 2-8 on the side-4,
side-6 and side-8 compiled tori; the one-face stabilizer argument and the
cube-connectivity argument, which hold at every even size; the per-item
verdicts with their named premises; the existence witnesses.

Not claimed: that any item follows from the four axioms alone; that any
dynamics class, time rule, or member of the fork is selected; any
infinite-volume, continuum, thermodynamic or Lorentz statement; any Record
readout of `E` or `B`; any identification with electromagnetism; any change
to an axiom or primitive; any audit verdict. The open PRs are quoted at
scope as evidence addresses and are not presented as landed or audited.

## 12. No-Go Discipline Gate

This note asserts, at family level, that items 1, 2, 6 and 7 are not forced
by the four axiom sentences plus the supplied compilation, and that items 3,
4 and 5 are forced only under named premises. Those are negative claims and
the gate applies. The load-bearing one is item 6; the routes below attack
it, and the same routes cover items 1, 2 and 7 where noted.

### N1 — Alternative route enumeration

Each row is a distinct family under the tuple (object, mechanism, terminal
obligation). No prior surface cited here is retained; every closed route is
executed in this block's runner or excluded by an approved premise node.

| route | what it would attempt | why it fails here | marker |
|---|---|---|---|
| R1 permanence-to-reversibility | read "records are permanent" as reversibility of the field law and reversibility as conservation | permanence concerns records, one per site, never re-recorded; an evolving field at a site is not a record sequence; and reversibility is not conservation: the harmonic sampler is reversible with respect to its measure while its conditional-mean map strictly decreases the energy (runner section G). Context, unaudited: the post-record algebra carries no reversible Hamiltonian-like flow (`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`) | ATTEMPTED |
| R2 no-privileged-state | read "A law privileges no states" as excluding attractors, hence forcing measure preservation | the damped law applies one rule at every state; and excluding attractors leaves the same-sign law (no attractor, conserves no positive form) and the unoriented law (conserves, but is not the class); the sentence concerns the law's domain, not invariants (runner sections F, H) | ATTEMPTED |
| R3 sampling identification | take the dynamics to be the per-site Admissibility sampler (IP-A) | the induced mean map is the Gauss-Seidel iteration of the static quadratic form and strictly decreases the energy; the induced law is the diffusive branch (runner section G) | ATTEMPTED |
| R4 kinetic-isotropy primitive | read "the emergent evolution tick" or the OS0 normalization as a self-adjoint transfer structure | the registered primitive's own note: "not a new dynamics", supplies only `c_t = c_s`; registry check performed; the primitive is an approved premise, not a wall, and it supplies no item | RULED OUT BY PRIOR (approved primitive source note, registry node `kinetic_isotropy_primitive`) |
| R5 Record additivity | use the additive record scalar as the energy and its invariance as the law | the structure was removed from Record on 2026-08-13 and, before that, contained no dynamics; the axiom memo is the canonical premise node | RULED OUT BY PRIOR (the axiom memo's 2026-08-13 paragraph) |
| R6 Noether from covariance | derive a conserved quantity from item 4 or LR | a symmetry yields a conserved quantity only through a supplied variational or Hamiltonian structure; the damped law is fully covariant and conserves no positive form (runner section F) | ATTEMPTED |
| R7 per-site unitarity from Qubit | read `M_2(C)` as forcing a per-site norm-preserving update, then sum | the conservative member does not conserve per-site energy (runner section F); the lattice-wide energy is not a per-site fact; and per-site norm preservation with a complete nearest-neighbor map is the object of the open PR `#7921`'s obstruction at its own scope (an evidence address, not a premise) | ATTEMPTED |
| R8 reflection positivity of a transfer interpretation | supply a Euclidean transfer reading of the compiled static law, prove reflection positivity, reconstruct a self-adjoint generator | not closed: this is the live route of N7; it needs two supplied structures (a path-product transfer interpretation and an evolution axis) | OPEN (not counted as closed) |

### N2 — Wall-independence audit

The walls are the supplies of section 10: `W_P` payload with its
transformation law (items 1, 7, OL); `W_T` time rule (item 2); `W_L` locality
(item 3, IP-B); `W_C` conservation (item 6); `W_S` symmetry (item 4 or 5).

| pair | first closes second? | second closes first? | independent? | exact witnesses |
|---|---:|---:|---:|---|
| `W_P`, `W_T` | only the memoryless clause (via SI) | no | partly: collapse the first-order clause into `W_P` | nonlinear law (minimal payload, nonlinear); vertex law (extended payload, linear continuous) |
| `W_P`, `W_L` | no | no | yes | complex law (nearest-neighbor); improved curl (minimal payload) |
| `W_P`, `W_C` | no | no | yes | vertex law (conserves); damped law (minimal, dissipative) |
| `W_P`, `W_S` | no | no | yes | complex law (covariant, gauge-compatible); anisotropic law (minimal) |
| `W_T`, `W_L` | no | no | yes | finite tick (each shear nearest-neighbor); improved curl (linear, continuous) |
| `W_T`, `W_C` | no | no | yes | nonlinear law (conserves); damped law (linear, continuous) |
| `W_T`, `W_S` | no | no | yes | finite tick (covariant, gauge-compatible); anisotropic law (linear, continuous) |
| `W_L`, `W_C` | no | no | yes | improved curl (conserves); damped law (nearest-neighbor) |
| `W_L`, `W_S` | no | no | yes | improved curl (covariant, gauge-compatible); anisotropic law (nearest-neighbor) |
| `W_C`, `W_S` | no | no | yes | unoriented law (conserves, not gauge-compatible); damped law (covariant, gauge-compatible, dissipative) |
| item 4, item 5 (inside `W_S`) | yes, given 1, 3, 7 and OL | yes, given 1, 3, 6, 7 | no: one wall | sections 3 and 4 |

Collapsed set: five walls. The headline uses the collapsed set.

### N3 — Hidden-wall scan

The scan phrases were searched in this note. "Supplied", "declared" and
"named premise" mark the compilation, OL, SI, IP-A, IP-B and LR, all listed
in section 1 as explicit premises. "Registered"/"registry" occur only in the
primitive registry check, which is a cited approved-premise surface, not a
condition. "By construction", "as is standard", "naturally", "obviously",
"standard QFT", "bridge context" and "background" do not occur as
load-bearing phrases. The sizes 4, 6, 8 and the rational parameters
(`h = 1/2`, `eps = 1/7`, `eps = 1/5`, `theta = 3/7`, `gamma = 2`) are
declared finite choices of the executed witnesses, not conditions of any
theorem (the one-face stabilizer and cube-connectivity arguments are
size-free). No hidden condition was promoted to a wall.

### N4 — Residual matching

| cited surface (status) | residual it attacks | residual claimed here | match |
|---|---|---|---|
| open PR `#7917` (unlanded) | the class is not derived from the axioms | the class, item by item, with witnesses | partial: same residual, sharpened; not a prior witness |
| open PR `#7915` (unlanded) | the static law does not select among three time rules | the sampling identification selects the diffusive one | partial: this note names which identification selects which branch |
| open PR `#7921` (unlanded) | raw onsite unitarity with a complete radius-one map kills transport | lattice-wide conservation is not a per-site fact | no: different residual; used in R7 as an evidence address only, not as a witness |
| `DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06` (no_go, unaudited) | the Wilson gauge-invariant-local class does not select a Hamiltonian | the declared edge/face class is not selected by the axioms | no: different class and mechanism; context |
| `RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06` (bounded_theorem, unaudited) | no reversible flow on the finite post-record algebra | no conservation principle for unrecorded fields | no: different object; context for R1 |
| `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_..._2026-06-05` (bounded_theorem, unaudited) | gauge covariance of a supplied Hamiltonian from record preservation under bridges | gauge compatibility from cubic covariance of the compiled payload | no: different mechanism; N8 echo |
| `SINGLE_CLOCK_AXIS_SELECTION_..._2026-06-11` (no_go, unaudited) | the evolution axis is a declared premise | the axioms name no time parameter | partial (shape); not needed as a witness |

After dropping non-matches, no prior witness supports any negative claim
here; each claim rests on this block's own exact witnesses, which is what
the claims need.

### N5 — Rhetoric and resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "item 6 is not forced" | executed: the four family parameters and the exact two-condition cut | executed: per-site energy is not conserved even by the conservative member, so conservation is a lattice-wide fact only | executed: witness spectra (symbolic slow root; real eigenvalues) | executed: skewness per block | executed on the side-6 torus; no infinite-volume statement |
| "the axioms name no time parameter" | textual (memo integrity read) | — | executed: the tick's per-mode phases are not those of `exp(hG)` | executed: shear by shear | executed: the full tick on side 6 |
| "items 1 and 7 are supplies" | executed: capacity bound eight | executed: two components per site; vertex sites carrying a component | executed: the third branch multiplicities | executed: the seven-dimensional extended class | executed on side 6 |
| "covariance forces the curl" | executed: sixteen characters, four couplings | executed: the face-site stabilizer | — | executed: coupling blocks | executed: side 4 in full generality |

The narrowest accurate forms are used in the tables: every negative is "not
forced by the four axiom sentences plus the supplied compilation, on the
finite compiled tori and by the stated size-free arguments"; none is "no
route exists". The runner prints matching `per_element:`, `per_site:`,
`per_mode:`, `per_block:` and `lattice_wide:` lines.

### N6 — Partial-closure paths and primitive scan

The registry was reread (section 1); no primitive supplies any item and none
is classified as a wall. Convention or reframing paths found:

- adopting the declared class as the candidate law (the open PR `#7917`'s
  first program choice): a convention adoption; it closes nothing at axiom
  level and is not a derivation;
- the interpretation of "one tick is one edge in form" in the approved
  kinetic-isotropy primitive (named as an owner interpretation boundary by
  the open PR `#7921`): bears only on item 2's continuous-versus-tick
  clause, not on conservation;
- the historical, unadopted proposal `DYNAMICS_AXIOM_MINIMAL_NONTRIVIALITY_BRANCH_PROPOSAL_2026-06-29`
  (a nonzero local self-adjoint generator): it would supply exactly items 2
  and 6; it has zero premise weight and is an axiom-shaped path, which is
  what the open PR `#7917`'s second program choice names;
- `docs/repo/DEFERRED_DECISIONS.md` on `origin/main` parks six owner-bar
  decisions; none names a conservative-dynamics principle or a time rule.
  Two are kin to walls here and are recorded as such: the parked
  `M_4(C)` Qubit-domain enlargement would change only the capacity bound of
  section 7 (eight real components per site becomes thirty-two), not any
  verdict; the parked OS-closure residue of the sister lane is kin to the
  reflection-positivity route of N7 and shows that route ends at the same
  owner bar, not at a derivation.

No path closes `W_C` by convention. This note does not say "a new axiom is
required"; it says no axiom sentence reaches the wall and names the live
derivation route (N7).

### N7 — Steelman

Hostile reviewer: "You have shown that no axiom *sentence* names
conservation, but the framework's own program derives its time from
records: the codimension-one evolution construction reads a Euclidean
transfer structure off the record statistics, and once the compiled static
law is reflection positive along a chosen axis, Osterwalder-Schrader
reconstruction gives a positive transfer matrix and a self-adjoint generator
— that is item 6 and the linear continuous first-order clause of item 2 at
once, and the sister lane already records a reflection-positivity closure
for its own action class. Your 'genuine supply' is a failure to run the
reconstruction." The route is concrete and its terminal obligations are
named: (i) a path-product transfer interpretation of the compiled static
law — the light lane's own members declare it supplied ("The factorized
transfer interpretation is an explicit premise", the open PR `#7886` at its
scope; the block-01 ledger's row 6) — and (ii) an evolution axis, which the
landed single-clock notes carry as a declared premise (B-AXIS, unaudited).
With both supplied, reflection positivity would have to be proved for this
compilation and the reconstruction would deliver a self-adjoint generator on
the reconstructed space, which then has to be shown to be the edge/face
payload of item 1 rather than an enlarged one. None of this is done by any
member or here. The steelman therefore does not defeat the scoped claim
("not reached by an axiom sentence") but it does forbid the broader one
("no route"), which this note does not make. Disposition: the negative claims
stay at family level with the route recorded as the next derivation target
in the machine-status block.

### N8 — Cross-cycle echo

| similar prior wall | retired? | mechanism since | applies here? |
|---|---|---|---|
| the static law does not select the time rule (open PR `#7915`, its W1) | no (open) | none | it is this block's `W_T` and `W_C`; the sampling identification now names which branch the axiom-nearest identification selects |
| allowed class is not a selected law (`DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06`, unaudited) | no | none | the same shape; this block adds that two of the class's items are internally redundant |
| no reversible flow from Record (`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06`, unaudited) | no | none | route R1 |
| the evolution axis is declared (single-clock notes, unaudited) | no; reframed from theorem to declared premise on 2026-06-11 | reframing as a declared premise | the same reframing is available for item 2's tick clause and is exactly the interpretation boundary the open PR `#7921` names; it is not a derivation |
| kinetic-order selector unsupplied (`INDEX_PAIRING_NOT_FORCED_..._2026-06-08`, unaudited) | no | none | different object (spatial order of the matter operator) |
| the sister lane's statistical bridge sealed non-supplied (gravity lane pack, `.claude/science/physics-loops/`) | no; parked at the owner bar | owner decision path | the two supplied structures of N7 are its kin; the same owner path, not a derivation |

No structurally similar wall was retired by a mechanism not considered here.

**Gate result:** PASS for the scoped negative claims (four supplies and three
conditionals, each with an exact witness; the collapsed wall count five;
the live route named). FAIL, and not shipped, for any claim that no
derivation route exists, that a new axiom is required, or that the class is
selected or rejected.

## 13. Falsifiers

The bounded theorem fails if any of the following is found:

- a covariant nearest-neighbor edge-to-face coupling on the minimal payload,
  under one of the sixteen signed-permutation laws, that is not one of the
  four listed, or a fifth transformation law of a real one-component payload
  by site permutation;
- a nearest-neighbor face row with `L d_0 = 0` and `d_2 L = 0` that is not a
  lattice-wide multiple of the oriented curl;
- a proper rotation about a vertex or cube site that changes the sector, or
  an edge-face pair at even physical distance;
- a positive diagonal energy conserved by a member with a nonzero onsite
  scalar or with `w_E r + w_B q != 0`;
- a Gauss-Seidel sweep of the harmonic conditional means that increases the
  energy, or a conditional-mean map on the edge field alone with radius one;
- a witness law that fails one of the items it is claimed to keep (each is
  checked exactly);
- an axiom sentence, read at its own scope, that names a time parameter, a
  conserved quantity of a field evolution, or an evolving coordinate.

## Imports

Every underivable input, in plain language, with role, provenance and
open-bridge status stated separately.

- The period-two role compilation (parity roles, oriented link value, doubled
  edge/face incidence). Role: the arena of every statement. Provenance:
  declared by the light lane's own construction (the open PR `#7913`), rebuilt
  here from the parity rule. Open bridge: its compilation into the
  homogeneous physical-site law is named open by that PR at its scope; not
  examined here.
- The named premises LR, IP-A, IP-B, OL, SI (section 1). Role: the hypotheses
  of the conditional verdicts. Provenance: this note's own readings, each
  shown load-bearing by a witness. Open bridge: SI's connection between
  unrecorded components and the Qualification's record configurations is the
  open bridge the open PR `#7915` lists as its wall W4.
- The finite sizes (sides 4, 6, 8) and the rational witness parameters.
  Role: the executed instances. Provenance: declared here. Open bridge: none;
  the two structural arguments are size-free.
- Computational tools: integer and rational arithmetic, `sympy` for the
  symbolic identities. Role: exact evidence. Provenance: standard software;
  no physics content.
- No comparator is used: continuum Maxwell theory, the leapfrog literature,
  and the sampler literature enter nowhere as inputs; the finite tick and
  the sampler are re-derived constructions used as witnesses.
- The members (`#7913`, `#7915`, `#7917`, `#7920`, `#7921`, `#7886`) are
  evidence addresses quoted at scope, not imports and not dependencies.

## Review record

Worker provenance: drafted by a Fable primary seat under the block-02
contract of the campaign pack (`GOAL_block02.md`), with the value gate V1-V5
answered in the pack's `REVIEW_HISTORY.md` before any PR. Independence
class: single family, cross-context (the runner's exhaustive finite
computations against the hand-derived one-face stencil, the blockwise
conservation equations and the cube-connectivity argument, which were
written before the runner and agree with it). Independent-math checks per
conformance section 6: the one-face stencil (hand computation, section 3),
the blockwise metric-skew equations (symbolic, section 5), the
cube-connectivity argument (hand, section 4), the finite-tick modified
energy (hand derivation of the kick-drift-kick invariant, section 6), and
the exact multiplicity counts (predicted from the momentum census, section
5). Mutation checks on scratch copies, one per check family, all detected by
the checks they target: axiom sentence altered; one curl sign flipped;
face-character factor dropped; metric-skew defect zeroed; Gauss-Seidel sign
flipped; modified-energy coefficient altered; quartic energy term dropped;
chain constraint disabled; a multiplicity altered; the stabilizer face sign
fixed; the support-radius test disabled; the covariance test disabled.
Nothing landed is replaced or narrowed (this is a new note). Hard landing
conditions: none; no helper runner; the citation-graph manifest co-lands
for the one added node.

## Verification

Run:

```text
python3 scripts/u1_dynamics_class_axiom_adjudication_2026_09_05.py
```

Expected final line:

```text
TOTAL: PASS=95 FAIL=0
```

The runner declares `AUDIT_TIMEOUT_SEC = 900` and reads one external input,
the axiom memo, declared in `AUDIT_INPUT_PATHS`; it performs no
package-local integrity read.
