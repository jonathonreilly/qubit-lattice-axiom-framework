# PMNS `hw=1` Carrier Nonselection and Scalar Source/Transfer Boundary

**Status:** exact boundary theorem on the baseline-framework carrier interface
**Type:** bounded_theorem
**Date:** 2026-04-16
**Revision:** 2026-07-12 — replaces the unsupported claim that the framework
axioms select the active/passive pair `(I_3,I_3)` with (i) an exact joint-
commutant classification, (ii) an explicit same-axiom model-separation
witness for the unfixed scalar normalization, and (iii) a family-wide
source/transfer rejection theorem that does not require the unit choice.
**Primary runner:**
[`scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py`](../scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py)
**Status authority:** independent audit lane only.

## Question

On the three-dimensional `hw=1` joint-character carrier, what follows for an
active/passive pair **if** each candidate block is invariant under the three
restricted translations and the proper-cubic three-cycle? Do the current
Lattice, Qubit, Admissibility, and Record axioms select the implemented unit
pair `(I_3,I_3)`, and does the conditional source/transfer boundary depend on
that normalization?

## Answer

The unit pair is **not** selected by the current axiom surface. Within the
explicit invariant candidate class, the exact result is sharper and
normalization-independent:

1. an endomorphism invariant under all three restricted lattice translations
   and the supplied proper-cubic three-cycle is necessarily `alpha I_3`;
2. applied separately, the most the symmetry classification gives is
   `(D_act,D_pass)=(alpha I_3,beta I_3)` — it neither fixes either scalar nor
   equates them;
3. the current axioms contain no carrier/source-action map, transfer operator,
   active/passive sector split, or normalization rule that could select
   `alpha=beta=1`;
4. under the explicitly defined response and one-sided-minimal support
   interfaces, every nonsingular
   scalar pair produces only scalar multiples of the three basis-source
   columns and a scalar-weighted cycle frame, and every such pair is rejected
   by the displayed support criterion.

Thus `(I_3,I_3)` remains one valid implementation point in the scalar family,
but it is not a first-principles consequence. The source/transfer rejection
boundary survives for the entire invariant family, so the missing
normalization is no longer load-bearing.

## Claim scope and premises

This note proves a bounded exact theorem with four distinct layers.

### Framework premise

The only supplied physics premise is the current
[`Lattice + Qubit + Admissibility + Record` axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
The runner instantiates the one-site `M_2(C) ~= Cl(3,0)` presentation, the
three `hw=1` lattice characters, and the proper-cubic three-cycle directly.

The axiom memo also fixes the relevant boundary: Admissibility is not a
dynamics axiom and does not choose a Hamiltonian or transfer operator. The
axioms supply no source/action or physical-observable identification. No
approved primitive is invoked by this theorem.

### Explicit mathematical hypothesis

The scalar-shape theorem is conditional on the candidate `hw=1` endomorphism
being invariant under the restricted translations and the proper-cubic
three-cycle:

```text
[D,T_x]=[D,T_y]=[D,T_z]=0,
C D C^{-1}=D.
```

This is an explicit mathematical candidate class, not a consequence or a
maximality theorem extracted from the four axioms. The note does **not** claim
that the axioms create a physical `D` or assign this transformation type to
one; the absence of that carrier map is part of the exact nonselection result.

### Defined response interface

For nonzero probe parameters and away from resolvent poles, the implemented
PMNS response maps are used as explicit definitions:

```text
R_act(D)  = [I_3 - lambda_act (D-I_3)]^{-1},
R_pass(D) = [I_3 - lambda_pass D]^{-1}.
```

These asymmetric definitions are an interface for the family theorem, not
claimed consequences of the four axioms.

### Defined one-sided-minimal support interface

The local rejection statement also uses an explicit finite support interface,
not an axiom-derived physical law:

- an active block is support-admissible when a simultaneous permutation of
  its rows and columns has the six-entry mask `supp(I_3+C)`;
- a passive block is support-admissible when its mask is one of the three
  cyclic monomial masks `supp(I_3)`, `supp(C)`, or `supp(C^2)`;
- a pair is one-sided minimal when exactly one side has active support and the
  other side has cyclic monomial support.

The runner implements these permutation-orbit/cyclic-mask definitions locally
and includes positive and negative controls. “Rejected” below means rejected
by this displayed finite interface; it is not a claim that the four axioms
derive the PMNS classifier or the response convention.

No observed PMNS angles, phases, masses, fitted coordinates, literature
values, new axioms, or new framework primitives enter.

## Derivation

### 1. The `hw=1` character carrier

In the ordered basis for the three weight-one lattice characters,

```text
chi_1=(-1,+1,+1),
chi_2=(+1,-1,+1),
chi_3=(+1,+1,-1),
```

the restricted translations are

```text
T_x=diag(-1,+1,+1),
T_y=diag(+1,-1,+1),
T_z=diag(+1,+1,-1).
```

Their joint spectral projectors are the rank-one matrices

```text
P_1=E_11,  P_2=E_22,  P_3=E_33,
P_1+P_2+P_3=I_3.
```

The proper-cubic rotation about the `(1,1,1)` axis restricts to the cyclic
matrix `C`, which transitively permutes these three character lines. The runner
constructs every object above from the character table and verifies the
projector identities rather than importing a PMNS helper.

### 2. Joint-commutant theorem

Let `D=(D_ij)` commute with all three translations. In the character basis,

```text
([D,T_a])_ij = (chi_j(a)-chi_i(a)) D_ij.
```

Every pair of distinct joint characters is separated by at least one
translation, so `D_ij=0` for `i != j`. Therefore the translation commutant is
the diagonal algebra

```text
Cent(T_x,T_y,T_z)=span_C{P_1,P_2,P_3}.
```

Independently, `Cent(C)=span_C{I_3,C,C^2}`. Requiring a diagonal `D` also to
commute with the transitive cycle forces its three diagonal entries to be
equal. Hence

```text
Cent(T_x,T_y,T_z,C) = C I_3.
```

For Hermitian blocks the scalar is real; positivity would only add
`alpha >= 0`. Applied separately to the two response sectors,

```text
D_act=alpha I_3,  D_pass=beta I_3.
```

Nothing in this calculation supplies a sector-exchange map, so it does not
imply `alpha=beta`.

The runner verifies the result a second way by constructing the full linear
commutator constraint matrix. It obtains translation-commutant dimension `3`,
cycle-commutant dimension `3`, and joint-commutant dimension `1`, with the
joint nullspace exactly spanned by `I_3`.

### 3. Why projector resolution does not select the unit

The translation-projector map is the dephasing conditional expectation

```text
E_T(X) = sum_i P_i X P_i.
```

For a scalar seed,

```text
E_T(alpha I_3) = alpha sum_i P_i = alpha I_3.
```

The old calculation

```text
sum_i P_i I_3 P_i = I_3
```

is the special case `alpha=1`: it evaluates the already supplied algebra unit.
It does not derive a physical active/passive carrier operator or its
normalization.

Adding the `C_3` average makes the type distinction even clearer:

```text
E_G(X) = (1/3) sum_{k=0}^2 C^k E_T(X) C^{-k}
       = (Tr X / 3) I_3.
```

Symmetry fixes the scalar **shape**; the input trace fixes the value. A theorem
such as `Tr D=3`, a unital carrier functor, or a separately derived physical
normalization would select `I_3`, but none is present in the current premise
surface.

### 4. Formal same-premise expansion argument

The nonselection statement is not inferred from missing prose alone. In the
formal premise signature, the four axioms constrain the lattice, one-site
possibility algebra, nearest-neighbor admissibility, records, and finite record
readout. They contain no symbols `D_act` or `D_pass`, no map into
`End(H_hw1)`, and no equation fixing a carrier trace or unit normalization.

Take any model of those four axioms and adjoin the displayed finite `hw=1`
character/rotation carrier as the explicit mathematical hypothesis of this
note. Expanding that same premise structure by either of the following
assignments cannot change the truth of any axiom sentence, because the new
carrier symbols occur in none of those sentences:

```text
M_1:   D_act=D_pass=I_3,
M_1/2: D_act=D_pass=(1/2) I_3.
```

Both pairs are state-independent positive Hermitian contractions, commute
with every named carrier symmetry, and preserve active/passive equality. They
differ only in an added symbol and normalization not constrained by the
premise signature. Thus the axioms plus the named invariant `hw=1` carrier
data cannot entail the unit pair.

This is a narrow model-separation result about the `3 x 3` carrier-construction
map. The runner verifies the syntactic boundary in the current axiom source
and checks that both displayed expansions satisfy Hermiticity, positivity,
contraction, and every explicit carrier invariance. It does not claim to
encode a complete infinite-lattice axiom model. This is not a claim that no
future carrier theorem can exist.

### 5. Scalar-family response theorem

For the complete invariant pair and away from poles,

```text
R_act(alpha)  = [1-lambda_act(alpha-1)]^{-1} I_3,
R_pass(beta)  = [1-lambda_pass beta]^{-1} I_3.
```

Source insertion through the joint-character lines therefore gives

```text
c_i^act  = r_act e_i,
c_i^pass = r_pass e_i.
```

Inverting these response-column matrices with the implemented reconstruction
formulas returns `alpha I_3` and `beta I_3` exactly. The runner verifies this
over a deterministic grid of unequal/equal, zero/unit/nonunit scalar pairs.

Forward graph transport contributes only

```text
P_1 C=E_12,  P_2 C=E_23,  P_3 C=E_31,
```

with any source amplitude remaining a common scalar. It supplies the ordered
cycle frame but no relative cycle values.

Finally, a scalar block remains diagonal under every simultaneous
permutation, so it never has the six-entry active support mask of `I_3+C`. A
nonzero scalar block has the allowed identity monomial mask; a zero scalar
block has empty support. Therefore neither member of a scalar pair has active
support, so no nonsingular scalar pair can realize the displayed
one-sided-minimal support interface.

At

```text
alpha=1+1/lambda_act  or  beta=1/lambda_pass,
```

the corresponding resolvent is undefined, so there is no valid response pack
rather than a PMNS escape.

## Falsifiers and boundary

The theorem would be moved by any one of the following:

1. a retained carrier/source-action theorem that constructs `D_act,D_pass`
   from the four axioms and assigns their transformation type;
2. a retained normalization theorem fixing `alpha` and `beta` (and, if needed,
   a sector-exchange theorem equating them);
3. a derived non-scalar source or state tensor that breaks at least one of the
   explicit translation/`C_3` invariances.

The runner includes the last possibility as a negative control:
`I_3+epsilon C` has the desired `I_3+C` support shape but fails translation
invariance. This shows exactly where nontrivial PMNS support can enter and why
it is outside the zero-input invariant family.

This note does **not** claim:

- that `I_3` is impossible or physically wrong;
- that every lattice or PMNS operator must be scalar;
- that the axioms forbid a future carrier, kinetic, source, or normalization
  derivation;
- that the implemented asymmetric response formulas are axiom-derived;
- full PMNS value, mass, angle, phase, or selector closure;
- rejection of any route carrying an explicit non-scalar source or
  symmetry-breaking input.

For downstream runner compatibility, the paired script retains the historical
function name `sole_axiom_hw1_source_transfer_pack` as an alias of
`conditional_unit_hw1_source_transfer_pack`. Its docstring and returned
`normalization_status` metadata identify it explicitly as the conditional
`alpha=beta=1` member of the family. The revised derivation never calls that
wrapper.

## Consequence

The earlier load-bearing sentence must be replaced:

```text
Unsupported: the framework axioms therefore give exactly (I_3,I_3).

Exact boundary: every jointly translation/C_3-invariant hw=1 block is scalar;
the axioms do not select its normalization, while the implemented PMNS
source/transfer interface rejects the entire nonsingular scalar pair family.
```

This closes the audited definition/renaming defect without pretending that an
absent carrier law has been derived. The remaining scientific target is a
non-scalar carrier/source theorem, not another evaluation of the identity
projector sum.

## Verification

```bash
python3 scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py
```

The runner is deterministic, imports no PMNS helper, and exits nonzero on any
failed check. Its result line reports the exact PASS/FAIL count.
