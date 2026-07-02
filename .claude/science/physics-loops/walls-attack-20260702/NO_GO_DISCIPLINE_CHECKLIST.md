# Block03 No-Go Discipline Checklist

Scope: the narrow negative "imported-basis scorings are not R*-registrable".
Status: conditional-support only; conditional on the registrability reading R*;
C1b remains open.

## N1 - Rescue Routes

1. Declare the per-mode basis supplied by Lattice axes. RULED OUT BY PRIOR:
   Minimal Axioms say "Physical sites are the points of the cubic lattice
   `Z^3`, with nearest-neighbor adjacency, standard translations, and proper
   cubic rotations." The `hw=1` carrier is an internal factor; Lattice supplies
   spatial adjacency, not an internal per-mode basis. The open-gates list also
   leaves "context selection, measurement basis selection" outside axiom
   content.
2. Basis-averaging. ATTEMPTED: Block03 T4. The averaged per-mode squares
   collapse to invariant total content, so this changes S2 into
   invariant-content scoring rather than rescuing an imported-basis S2 rule.
3. Promote the basis to supplied readout context. RULED OUT BY PRIOR: that is
   exactly a C1-supplier admission, the wall itself, not a rescue within the
   baseline.
4. Use `Y`'s eigenbasis. ATTEMPTED: Block03 T3. This is S3-class, a different
   `Y`-dependent rule, and is unaffected by the imported-basis exclusion.
5. Reject R*. ATTEMPTED: then no registrability constraint applies here. That
   contradicts the complement-note precedent pattern and leaves the parent
   walls exactly as before: no rescue, just retreat.

## N2 - Wall Independence

- C1a is independent of C2: Block02 T2 gives a fixed frame with multiple
  additive weights.
- C1a is independent of C1b: Block03 T3 gives the S3 `Y`-dependent partition
  witness, which R* does not exclude.
- C1b is independent of C2 by construction: partition state-independence and
  scalar weighting are separate supplier shapes.

## N3 - Hidden-Wall Scan

Scan terms: `we assume`, `by construction`, `supplied`, `registered`,
`standard`.

- In the Block03 note, only `supplied` appears among those terms.
- `supplied`: classified as declared input language from the five read source
  files and the finite `hw=1` setup.
- `we assume`: no note occurrence.
- `by construction`: no note occurrence.
- `registered`: no note occurrence.
- `standard`: no note occurrence.
- In this checklist, `by construction` appears in N2 only to state the requested
  C1b/C2 independence classification, and `standard` appears only inside the
  quoted Lattice descriptor from Minimal Axioms.

R* is the single named interpretive premise.

## N4 - Witnesses

- Block01 Hadamard identities: MATCH. The witness
  `H(1, 1)^T = (sqrt(2), 0)^T` is reused for the S2 imported-basis verdict
  change.
- Complement-note precedent: PATTERN MATCH ONLY. Its registrability statements
  are slot-model-scoped, not stated in transportable generality.

## N5 - Resolution Audit

The phrase "imported-basis scorings are not registrable" is tested at the
per-witness and imported-choice-orbit level under R*. The note does not claim
per-all-models resolution.

## N6 - Partial-Closure Scan

No existing convention or reframing in the five-file read set supplies the
per-mode basis. Minimal Axioms' open-gates list leaves measurement basis and
context selection outside axiom content.

## N7 - Steelman Against The Exclusion

"R* is doing all the work and R* is not axiom text; a reviewer reading Record as
silent on unsupplied choices gets no exclusion."

Answer: correct. That is why the claim is bounded and conditional on R*, and
why the note's certificate keeps audit_required true.

## N8 - Cross-Cycle Echo

Nearest prior retired-wall mechanism: the complement note excludes
frame-orbit content by registrability on its supplied slot model. Block03 uses
the same mechanism as a scoped precedent pattern, consistently, without
transporting the theorem beyond its slot-model scope.

## Block05 No-Go Discipline Checklist

Scope: the narrow negative "S3-class fine-partition rules are not D-total".
Status: conditional-support only; conditional on D-totality, which is not
adjudicated here. Pointwise escape remains without D-totality.

### N1 - Rescue Routes

1. Restrict the rule to the nondegenerate stratum. HONEST MARKER: this rejects
   D-totality itself. It is the adjudication question, not a rescue within
   D-totality.
2. Coarsen at the locus. ATTEMPTED: Block05 T2. The fine per-cell data the S3
   condition needs is not present in the coarsened algebra. At `delta=0`, the
   coarsened spectral data is `{P_0, P_1+P_2}` with eigenvalues
   `{a+2|b|, a-|b|}`. The S3 defining relation references fine
   eigenvalue/idempotent content; on the coarsened locus it degenerates to a
   rank-two cell and only total content such as
   `c_{P_1+P_2}(T)=1` remains, while valid fine splits give `(1,0)` and
   `(1/2,1/2)`.
3. Borrow the algebra frame. ATTEMPTED: Block05 T3. This is provenance collapse
   to S1: the Fourier split is determined by `U`, the circulant algebra frame,
   not by `Y` on the degeneracy locus.
4. Perturb `Y` off the locus. HONEST MARKER: this violates the pointwise
   interface. The realized-state primitive says derivations evaluate at the
   realized state, pointwise, and supplies "no averaging over alternatives, no
   typical or generic claim".
5. Declare the locus measure-zero or atypical. HONEST MARKER: the
   realized-state primitive supplies no "measure, weighting, probability rule,
   typicality claim, genericity claim" and no state-selection rule.

### N2 - Wall Independence

- D-totality is independent of R*. R* blocks imported-basis or unsupplied-choice
  variation; D-totality blocks partial readout domains over law-admissible
  realized states. Block03 T3 is the witness pair: a `Y`-dependent partition is
  not imported-basis variation, so R* alone leaves it open.
- D-totality is independent of C2. C2 concerns weighting once cells are
  supplied; D-totality concerns whether the fine cells are defined at every
  law-admissible realized state.

### N3 - Hidden-Wall Scan

Scan terms: `we assume`, `by construction`, `supplied`, `registered`,
`standard`.

- The Block05 note uses `supplied` only for named source-surface content and
  for the primitive's pointwise realized-state interface.
- D-totality is explicitly named as this note's single interpretive premise.
- No probability, measure, typicality, perturbation, genericity, observed value,
  fitted selector, or equal-channel-energy theorem is imported.

### N4 - Witnesses

- Exact eigenvalue collision enumeration on the `delta = m pi/3` residues.
- Exact projector checks for `P_1,P_2` and the rotated `Q_1,Q_2` split:
  idempotent, orthogonal, summing to `P_1+P_2`, and commuting with degenerate
  `Y`.
- Exact per-cell Hilbert-Schmidt content witness using `T=P_1`: Fourier split
  gives `(1,0)`, rotated split gives `(1/2,1/2)`, and the coarsened cell gives
  only total content `1`.

### N5 - Resolution Audit

The claim is tested at the finite `hw=1` circulant-surface level only. It does
not claim all-models resolution or actual-surface wall closure.

### N6 - Partial-Closure Scan

No existing convention in the four-file Block05 read set supplies fine cells at
degeneracy loci. Minimal Axioms' open-gates list keeps context selection,
measurement basis selection, Born weights, probability rules, source/action,
and physical-observable identification outside axiom content.

### N7 - Steelman Against The Exclusion

"physics only ever evaluates at THE realized state; demanding totality is a
philosophical preference, not physics"

Answer: correct as stated. That is why the exclusion is conditional on
D-totality and D-totality is flagged for adjudication rather than asserted.
There is a law-likeness precedent in the shape of state-independent rules, but
this checklist does not claim repo authority has already adopted D-totality.

### N8 - Cross-Cycle Echo

R* from Block03 is the structurally similar prior. Both R* and D-totality are
conditional premise mechanisms at the rule level; both are treated consistently
as audit-adjudication premises rather than as already-retained axiom content.
