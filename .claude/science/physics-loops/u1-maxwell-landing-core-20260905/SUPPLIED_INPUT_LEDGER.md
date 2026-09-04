# SUPPLIED INPUT LEDGER — the U(1)/Maxwell light lane, ranked by value-to-the-chain

**Written 2026-09-05** for block 01. One row per supplied input of the chain
stated in `LANDING_CORE.md`. For each: the input in plain language; the
members that lean on it; what a derivation of it from the four axioms would
buy the chain; and an honest estimate of derivability, naming the axiom
sentence it would come from or saying "genuine supply". Axiom sentences are
quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` (the four axioms: Lattice,
Qubit, Admissibility, Record) and the approved primitives are as registered in
`docs/audit/data/axiom_premise_nodes.json` (scale reference: units only;
kinetic isotropy: `c_t = c_s` only; realized state: pointwise evaluation
only). No primitive is classified here as a wall, an import, or a source of
bounded status; where a member reads a primitive's boundary, that reading is
quoted as the member's.

**Ranking key.** Rows are ordered by the value to the chain of a successful
derivation (tier A: changes the status of the terminal or decides the open
photon item; tier B: removes a supplied input from one link without changing
the terminal; tier C: an open bridge or regime restriction the chain names
but does not use as an input to the photon). Within a tier, rows with a live
axiom lever precede rows estimated as genuine supply, because a genuine supply
cannot be bought by derivation — it can only be named, or taken to the
owner's bar. The top row whose estimate is not "genuine supply" selects
block 02.

**Derivability vocabulary.** *live lever*: an axiom sentence gives the input's
shape or sign directly, under a named identification premise. *partial*: some
of the input follows from an axiom sentence or from a member's own
construction; the rest is supplied. *genuine supply*: no axiom sentence
reaches it, by the axiom memo's own list of what the axioms do not supply.
Every estimate is this synthesis's reading, not a member claim.

## Summary table

| rank | tier | supplied input | leaned on by | a derivation would buy | derivability |
|---:|:---:|---|---|---|---|
| 1 | A | the dynamics class of #7917 (real, linear, first-order, continuous time; NN; translation + proper-cubic covariant; gauge/chain compatible; positive-diagonal energy conserved; minimal edge/face payload) | #7917 (class); #7915 (the generator, supplied); #7920-#7923 (the tick); #7932 (the tangent) | the terminal becomes *unique given the residual supply* instead of *unique inside a declared class*; the residual becomes the exact object of #7917's program choice 2 | mixed: locality and covariance are a live lever (Admissibility's covariance sentence, under an identification premise); gauge compatibility partial (role construction); conservation, first-order linear continuous time, and minimal payload are genuine supply |
| 2 | A | the detuning `V` of the finite-qubit carrier, and the electric stiffness `U > 0` it produces | #7937, #7941, #7943, #7945, #7946, #7952, #7953, #7955, #7963; #7959 (its absence: `V = 0`, `E_e^2 = 1/4`) | decides the two-branch photon split: whether the linear transverse term is a supplied detuning or a derived object | the value of `V`: genuine supply; the sign of an electric stiffness: a live lever exists in the compact branch (#7886's registration curvature from Admissibility's "varies with") whose transplant to the spin-half carrier no member attempts; `U > 0` from matter coupling is a computation on #7959's named candidates |
| 3 | A | the link role: which sites are vertices, edges, faces, cubes, and the U(1) / `Z_K` / integer-flux / spin-half label realized on edge sites | every member | the root of the chain: a derived carrier | genuine supply at law level (Lattice: "No site is privileged"); at most a feature of a realized state (registered data); the spin-half label is the one closest to Qubit's `M_2(C)` |
| 4 | B | the Gauss constraint (ice rule; `div E = rho`) read as support forcing among records | #7893, #7903, #7911, #7936-#7963; #7917 item 5; #7952 (transversality) | the constraint sector of every link, and part of the terminal's gauge-compatibility item, become Admissibility-shaped consequences | partial, high: the shape is a live lever (Admissibility's support clause on the role-compiled NN geometry); the specific rule and background charge are supplied |
| 5 | B | orientation completion: a spatial plaquette factor with `kappa_s = kappa_t` | #7884, #7886, #7887, #7906, #7915 | the magnetic block of the compact branch — without it the kernel has rank one and there is no light | partial: spatial isotropy among the three spatial orientations is a live lever (Admissibility's covariance sentence) once a spatial factor exists; the factor's existence is Admissibility-shaped via #7907 but its alphabet is supplied; `kappa_s = kappa_t` (space against Record time) is genuine supply — the members decline to read the kinetic-isotropy primitive as covering it |
| 6 | B | the Record registration / overlap law used as a multiplicative transfer or action factor | #7886, #7887, #7906; #7915, #7917 (through `kappa`) | `kappa > 0` unconditionally from Record + Admissibility, closing link ii without supply | partial: nonconstancy is derived by #7886 from Admissibility's "varies with" on the shifted-convolution ansatz; the ansatz has a lever in Qubit's "No possibility is privileged"; the path-product (factorized transfer) is genuine supply |
| 7 | B | the finite tick: palindromic three-shear schedule, composed radius three, `h < 1/sqrt(3)` | #7920, #7922, #7923; #7921 (the strict class it refutes) | the exact local tick, "the sharpest dynamics compiler residual" (#7917) | genuine supply; the live question is the reading of the approved kinetic-isotropy primitive's "one tick is one edge in form", which #7921 names as an interpretation boundary for the owner, not a derivation |
| 8 | B | reciprocal coefficients `beta = kappa`, `alpha = 1/kappa` (unit speed) | #7915, #7917, #7932 | `c = 1` in lattice units | the members read the kinetic-isotropy primitive as licensing this after class selection; the electric coefficient's existence is supplied; low value (branch count and gaplessness do not depend on it) |
| 9 | C | matter: the emergent staggered fermion, its minimal coupling, finite matter representations, the coupling normalization / electromagnetic dictionary | #7892, #7893, #7903, #7922-#7932 | sourced Maxwell with a physical unit | genuine supply for the normalization ("source/action and physical-observable identification" is outside the axioms by the memo's list); the fermion is another lane's object |
| 10 | C | the unrecorded field evolution and Record readout of `E`, `B` | #7906, #7915, #7917, #7922 | the chain's connection to the only readable things | open bridge; Record: "Only records are readable"; no member supplies it |
| 11 | C | regime restrictions: weak field, no-wrap window, zero-monopole smooth branch, finite volume, fixed sector | #7884, #7907, #7932, #7945-#7963 | control of the interacting, compact, thermodynamic sectors | not derivation targets; named |
| 12 | C | the four-dimensional Euclidean carrier and a reflection-positive transfer interpretation | #7884, #7886 (Lorentzian reading only) | the Lorentzian dispersion reading of link ii | genuine supply here; cross-lane pointer only |

## Row detail

### 1. The dynamics class of #7917 — tier A, block 02 target

**The input.** Seven declared items (quoted in `LANDING_CORE.md` section 7):
one real `E` per edge-role site and one real `B` per face-role site; real,
linear, first-order, continuous-time evolution; a site derivative reads itself
and its six physical nearest neighbors only; translation and proper-cubic
covariance; gauge invariance of the edge-to-face map and preservation of the
magnetic Gauss row; a positive, diagonal, proper-cubic conserved energy; no
vertex, cube, coin, or hidden time payload.

**Leaned on by.** #7917 declares it; #7915 supplies the generator that lives
in it; #7920-#7923 build ticks and sources on that generator; #7932's tame
tangent is a Hamiltonian of the same shape. #7917: "The four axioms do not
currently select that class. In particular, they do not state real linear
first-order evolution, energy conservation, minimal `(E,B)` payload, or
continuous time."

**What a derivation buys.** The terminal's status. Today the chain ends in
*unique inside a declared class*; a derivation of the class from the axioms
would make Maxwell the framework's weak-field gauge dynamics rather than a
candidate law. A partial derivation buys the exact residual: #7917's "two
honest program choices" (adopt M1-M6 as the candidate law, or "decide whether
a conservative local-dynamics principle belongs in the approved
primitive/axiom boundary") become decidable only once the residual is named
item by item.

**Derivability, item by item.**

- Nearest-neighbor locality (item 3): *live lever*. Admissibility: "There is
  one fixed nearest-neighbor admissibility rule, covariant under lattice
  translations and proper cubic rotations." Under the identification premise
  that the evolution's one-step conditional is the admissibility rule's
  realization, the stencil reads only nearest neighbors. The identification
  premise is itself the supply: the axiom memo says "Admissibility is not a
  dynamics axiom" and that it "does not choose a Hamiltonian or transfer
  operator".
- Translation and proper-cubic covariance (item 4): *live lever*, the same
  sentence, under the same identification premise.
- Gauge and chain compatibility (item 5): *partial*. #7913's compiled factor
  graph has "exact translation, gauge, and proper-cubic covariance" at role
  level; gauge invariance of a face response is what #7917 uses to cut four
  coefficients to the curl stencil. The lever toward the axioms is Qubit's
  "No possibility is privileged" (dependence on relative phase only), but
  that reaches the role's label realization, not the axiom's `M_2(C)` domain
  directly.
- Positive diagonal energy conservation (item 6): *genuine supply*. No axiom
  sentence states a conserved quantity. The candidate lever — Record's
  "records are permanent" read as reversibility — is shown insufficient by
  the members themselves: #7915's Ornstein-Uhlenbeck sampler is reversible,
  preserves the same static measure, and is diffusive ("relaxation
  proportional to `k^2`"); #7917: "energy conservation excludes the
  dissipative sampler". Synthesis reading: the most direct realization of
  the identification premise in items 3-4 (a one-step conditional equal to
  the admissibility distribution) IS the sampler branch of #7915's fork, so
  the lever that buys locality and covariance pulls toward the diffusive
  branch, and item 6 is the item that separates Maxwell from it. This is the
  load-bearing residual.
- Real, linear, first-order, continuous time (item 2): *genuine supply*.
  Linearity is a weak-field regime, not a law; "time metric" and "physical
  persistence dynamics" are on the axiom memo's list of open gates outside
  the axioms; continuous time is in tension with the finite-tick reading of
  the approved kinetic-isotropy primitive (#7917 section 7; #7921).
- Minimal real one-component payload (items 1, 7): *genuine supply*. Qubit
  gives `M_2(C)` per site; one real component per role site is a further
  restriction, and #7921 shows the escapes from its no-go need an enlarged
  carrier or an observable-level reading.

**Block 02 target, exactly.** Derive items 3, 4, and (at role level) 5 from
Admissibility's covariance sentence and the role construction under a named
identification premise; then test whether any axiom sentence yields item 6,
with the expected honest outcome that none does, so that items 6, 2, 1, and 7
are recorded as the exact residual supply of the terminal. Block 02 must not
import continuum Maxwell, must not read the kinetic-isotropy primitive as a
dynamics selector (the members' own boundary), and must name the
identification premise as a premise.

### 2. The detuning `V` and the electric stiffness `U > 0` — tier A

**The input.** In the finite-qubit carrier, the potential term `V N_f` with
supplied `V` (`V = 1` the RK point; `V = 0.95, 0.90` tested; `V = 0` the
ring-exchange law alone), and the coarse-grained electric stiffness `U` the
members measure from the flux tower and charge response.

**Leaned on by.** #7937 (`U/|delta V| = 3.18`), #7941, #7943, #7945
(`c_V^2 = gamma |V-1|`), #7946, #7952, #7953, #7955, #7963; #7959 by its
absence: at `V = 0` "the electric term is the c-number `E_e^2 = 1/4` and
supplies none".

**What a derivation buys.** The lane's open item. If the framework's law on
this carrier has a derived positive electric stiffness, the linear transverse
term is a derived object; if the stiffness exists only as a supplied
detuning, the photon of branch B is a supplied object and branch A's
quadratic mode is what the carrier does on its own at the sizes reached.

**Derivability.** The value of `V`: *genuine supply* — Admissibility's
distribution sentence names determination and variation, and the memo says
"the distribution's extensional form and values are not specified by this
memo". The sign of an electric stiffness: a *live lever* exists in the
compact branch — #7886 derives `kappa_t > 0` (the temporal, i.e. electric,
curvature) from a nonconstant registration kernel, with nonconstancy tied to
Admissibility's "varies with" — and no member transplants that argument to
the spin-half carrier, where the electric term is a c-number and the
stiffness would have to be an emergent coarse-grained quantity. The existence
of `U > 0` from matter coupling (#7959's first named candidate, the fermion
charge coupling of #7893) or from a larger link representation (its second)
is a computation, not an axiom derivation. Synthesis reading of the cross-
branch shape: in the compact branch the electric sign is the derived part and
the magnetic block is supplied; in the spin-half branch the magnetic
(ring-exchange) term is the declared law and the electric stiffness is what
is missing. A block that measured the electric stiffness of the
ring-exchange-alone law at a same-detuning point, or extended #7959 below
`k = pi/6`, would be a computation block on this row, not a derivation.

### 3. The link role — tier A, genuine supply

**The input.** A period-two assignment of vertex, edge, face, and cube roles
to `Z^3` sites (#7913: "exactly eight translated parity-role sectors on even
tori"), and the label realized on the edge sites: compact U(1) (#7884-#7887,
#7906, #7907), `Z_K` Weyl clock (#7932: "for K=2^q the complete link is
exactly q qubits"), integer flux (#7903), spin-half (#7893, #7911,
#7936-#7963; #7959: "ONE DESIGNED SPIN-1/2 LINK ROLE per edge").

**Leaned on by.** Every member.

**What a derivation buys.** The root of the chain: a carrier that is a
consequence rather than a design.

**Derivability.** *Genuine supply at law level.* Lattice: "No site is
privileged. Sites are distinguished by the supplied lattice structure alone."
A law-level role assignment privileges sites. The Qualification says "A state
is a configuration of records" and "A law privileges no states", so a role
pattern can at most be a feature of a realized state — registered data under
the realized-state slot, invariant over no law-admissible family, hence not a
derivation output. Of the labels, the spin-half role is the one closest to
Qubit's "The full one-site possibility domain has algebraic presentation
`M_2(C)`": one qubit per link site (#7959: "one further two-state site per
edge"); the others need many qubits per link (#7932) and a compiler the
members name as open. Not a block target; named.

### 4. The Gauss constraint as support forcing — tier B, live lever

**The input.** The ice rule (three-of-six) and the charge rule `div E = rho`,
with a supplied background (`rho_v = 0` on tori; the staggered convention on
#7911's ladder).

**Leaned on by.** #7893 ("Gauss operators that commute with the coupled law
and are implemented as order-independent site-level support forcing among
corner records"), #7903, #7911, #7936-#7963; #7917's item 5; #7952 ("gauge
transversality comes from the supplied ice constraint and carrier
construction").

**What a derivation buys.** Every link's constraint sector, and part of the
terminal's gauge-compatibility item, become consequences of Admissibility
rather than a supplied constraint.

**Derivability.** *Partial, high.* Admissibility's reading note:
"'available'/'admissible' denotes its support -- on finite menus, exactly the
possibilities of nonzero probability." On the role-compiled lattice a
vertex-role site's six physical nearest neighbors are its six edge-role sites,
so *the admissible vertex possibilities are those compatible with the six
neighboring link records* is exactly the shape of the Admissibility sentence: the
distribution's support at a site determined by nearest-neighbor conditions.
#7893 already words Gauss's law that way. What is supplied is the content of
the rule (which combination of neighboring link values is admissible, and the
background charge). A natural block-03 candidate.

### 5. Orientation completion — tier B, partial

**The input.** A spatial plaquette factor on every spatial orientation with
curvature equal to the temporal (registration) curvature: `kappa_s = kappa_t`.

**Leaned on by.** #7884 (isotropic germ hypothesis), #7886 ("A temporal
registration kernel by itself supplies only the electric/temporal quadratic
block. It has no magnetic restoring block and is not Maxwell."), #7887,
#7906 ("Completing all face orientations"), #7915 (omitting one face
orientation loses a transverse branch).

**What a derivation buys.** The magnetic block of the compact branch; without
it there are no transverse modes.

**Derivability.** Three parts. Isotropy among the three spatial orientations:
*live lever* — Admissibility's "covariant under lattice translations and
proper cubic rotations" relates the spatial orientations once a spatial
factor exists (#7886: "The spatial cubic lattice symmetries can relate spatial
orientations after a spatial action surface is present."). Existence of a
spatial factor: *partial* — #7907's face and link full conditionals are
"incidence-nearest-neighbor", so the factor is Admissibility-shaped, but the
face alphabet and the weight are supplied. Equality of the spatial and
temporal curvatures: *genuine supply* — #7886: the spatial symmetries "do not
exchange space with Record time", and both #7884 and #7886 decline to read the
approved kinetic-isotropy primitive as covering the gauge-action Hessian; no
axiom sentence relates a Record-time kernel to a lattice-space one.

### 6. The Record law as a multiplicative transfer/action factor — tier B, partial

**The input.** A positive central Lueders registration (#7886), a
distribution-overlap kernel (#7887), or an overlap-success Record law
(#7906), used as the per-plaquette factor of a path weight.

**Leaned on by.** #7886, #7887, #7906; #7915 and #7917 through `kappa`.

**What a derivation buys.** `kappa > 0` unconditionally from Record and
Admissibility: link ii without supply.

**Derivability.** Nonconstancy: derived by #7886 from Admissibility's "varies
with" on the shifted-convolution ansatz ("the conditional family changes for
some neighboring conditions iff K is nonconstant"). The ansatz (dependence on
relative phase only): *live lever* in Qubit's "No possibility is privileged.
Possibilities are distinguished by the supplied algebraic structure alone." —
if the link's possibility structure is the U(1) relative phase, a rule that
privileges no possibility can depend only on differences. Representation
positivity: derived by #7887 for overlap kernels, supplied by a Lueders
channel in #7886. The path-product (#7886: "The factorized transfer
interpretation is an explicit premise of this step"; "no global joint law is
inferred merely from arbitrary local full conditionals"): *genuine supply*.
Cross-lane pointer, not a finding: the sister lane's landing core records its
statistical bridge (slice-Gram weights equal record frequencies) as sealed
non-supplied and proposed as an axiom; the path-product here is a kin
statement (a joint law from per-record conditionals), and whether the sister
lane's closure reaches it is not examined by any member.

### 7. The finite tick — tier B, genuine supply

**The input.** The palindromic three-shear Yee/leapfrog schedule with
composed radius three and `h < 1/sqrt(3)` (#7920); the half-full-half
coefficients are the unique first-order-consistent choice: "Within the
declared palindromic schedule, first-order Maxwell consistency uniquely
selects the half-full-half coefficients".

**Leaned on by.** #7920, #7922, #7923; #7921 refutes the strict alternative
(complete-map radius one, raw onsite norm, minimal payload).

**What a derivation buys.** The exact local tick — #7917: "the infinitesimal
law is unique inside M1-M6, while a strictly radius-one exact unitary tick has
not been selected or constructed."

**Derivability.** *Genuine supply.* No axiom sentence sets a tick. The
approved kinetic-isotropy primitive supplies `c_t = c_s` and "one tick is one
edge in form"; #7921's reading is that it "does not define 'one edge in form'
as this complete-map radius-one onsite-unitary class, and it supplies no
dynamics", and that the governance question is "whether 'one tick is one
edge in form' permits a finite-depth nearest-neighbor cycle or refers only
to the normalized regulator form." That is an interpretation question for
the owner, not a derivation; the primitive is not a wall and is not
classified as one here.

### 8. Reciprocal coefficients — tier B, low value

**The input.** `beta = kappa`, `alpha = 1/kappa`, giving speed one (#7915:
"declared here rather than attributed to the static probability law").

**Leaned on by.** #7915, #7917, #7932 (where reciprocal coefficients cancel
`g`).

**What a derivation buys.** `c = 1` in lattice units; nothing about branch
count, gaplessness, or covariance depends on it.

**Derivability.** The members read the approved kinetic-isotropy primitive as
licensing the normalization only after the class is selected (#7917: it "can
normalize the remaining space/time kinetic ratio to one in lattice units. It
does not select M1-M6 and supplies no dynamics on its own."). The existence of
an electric coefficient at all is the supply (#7906's "positive electric
rotor term").

### 9. Matter coupling and normalization — tier C, genuine supply

**The input.** The emergent staggered fermion (#7892), its minimal coupling
(#7893, #7903), the finite matter representations (#7924, #7927, #7930,
#7932), the coupling normalization and electromagnetic dictionary.

**Leaned on by.** #7892, #7893, #7903, #7922-#7932.

**What a derivation buys.** Sourced Maxwell with a physical unit; the
identification of the emergent U(1) with electromagnetism.

**Derivability.** *Genuine supply* for normalization and dictionary: the
axiom memo lists "source/action and physical-observable identification" among
the open gates outside the axioms; #7922: "coupling normalization, and Record
readout remain open"; #7945: "No electromagnetic unit or empirical
fine-structure constant is assigned." The fermion is another lane's object and
is taken as supplied here.

### 10. The unrecorded field evolution — tier C, open bridge

**The input.** That `E` and `B` evolve between record formations and are
readable afterwards (#7915: "'Unitary' is the exponential of the finite skew
generator, not a claim that permanent Records update unitarily"; #7906:
"marginalizing unread face outcomes erases the action").

**Leaned on by.** #7906, #7915, #7917, #7922.

**What a derivation buys.** The chain's connection to Record, the only
readable structure.

**Derivability.** Open by the axiom's own terms — Record: "Only records are
readable. A readout value is determined by record content alone. A site with
no record cannot be read." No member supplies the bridge; #7915 lists it as
its wall W4.

### 11. Regime restrictions — tier C, named

**The input.** Weak field (#7915, #7917, #7921); the no-wrap window (#7932);
the smooth zero-monopole principal branch (#7884); finite volume and fixed
sector (#7945-#7963); `L <= 12` and `k >= pi/6` (#7959).

**Leaned on by.** As listed.

**What a derivation buys.** Control of the compact, interacting,
thermodynamic, and continuum sectors, which every member names as outside its
claim.

**Derivability.** Not derivation targets; each is the boundary of a member's
theorem and is carried into `LANDING_CORE.md` as stated.

### 12. The four-dimensional carrier and reflection-positive transfer — tier C

**The input.** #7884's continuum limit lives on a finite periodic
four-dimensional hypercubic refinement, and its Lorentzian dispersion
`4 sinh^2(E/2) = (kappa_s/kappa_t) P` holds "If a reflection-positive transfer
interpretation is additionally supplied".

**Leaned on by.** #7884, #7886 (Lorentzian reading only).

**What a derivation buys.** The Lorentzian reading of link ii.

**Derivability.** *Genuine supply* here. Cross-lane pointer only: the sister
lane's landing core records a reflection-positivity closure for its own
committed action class at its measured fixtures; whether that result reaches
the compact U(1) one-plaquette class is not examined by any member of this
lane and is not examined here.

## Block 02 selection

Row 1, restricted as stated in its "Block 02 target, exactly" paragraph:
derive the locality, covariance, and (role-level) gauge-compatibility items
of the #7917 class from Admissibility's covariance sentence and the role
construction under a named identification premise, and record conservation,
first-order linear continuous time, and minimal payload as the exact residual
supply — with the synthesis warning that the identification premise's most
direct realization is the diffusive sampler branch of #7915's fork, so the
block's honest product may be a sharpened residual rather than a derivation.
Row 4 (Gauss as support forcing) is the natural block 03. Row 2 is a
computation block, not a derivation block, and is the shortest path to the
lane's open item.
