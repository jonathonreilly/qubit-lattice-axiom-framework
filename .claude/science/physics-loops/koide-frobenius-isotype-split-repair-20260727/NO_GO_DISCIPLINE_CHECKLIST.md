# No-Go Discipline Checklist: Koide Frobenius Isotype Split

**Target contract.** On `Herm(3)`, test only whether positive-definiteness,
unitary Ad-invariance, and scalar/traceless orthogonality force `beta = 0`
inside
`B_{alpha,beta}(A,B) = alpha Tr(AB) + beta tr(A) tr(B)`.
The completion witness is one globally positive-definite, Ad-invariant,
block-orthogonal member with `beta != 0`. A claim about all possible future
normalization principles, or a physical derivation of Koide, is forbidden.

## N1 — Alternative route enumeration

| Family | Attack on the no-go | Result and evidence | Marker |
|---|---|---|---|
| Positivity cone | Try to make positive-definiteness collapse the two weights to equality. | The exact block formula gives the open cone `alpha > 0`, `alpha + 3 beta > 0`; scalar `I` and traceless `diag(1,-1,0)` witnesses establish necessity. See the target note, “Exact No-Go Statement,” and the paired runner. | ATTEMPTED |
| Adjoint symmetry | Try to make unitary Ad-invariance eliminate the scalar-trace term. | Both trace factors are conjugation invariant, so every member of the family is Ad-invariant; the runner also checks a continuous symbolic conjugation family. | ATTEMPTED |
| Isotype orthogonality | Try to make scalar/traceless orthogonality eliminate `beta`. | The full cross-bilinear decomposition shows the mixed blocks vanish for every `alpha,beta`, so orthogonality fixes block shape but not relative weight. | ATTEMPTED |
| Overall-scale quotient | Try to identify all positive forms after quotienting by a common normalization. | The scale-invariant ratio is `(alpha + 3 beta)/alpha`; `B_{1,lambda}` spans the continuum `1 + 3 lambda` for `lambda > -1/3`. | ATTEMPTED |
| Circulant AM-GM restriction | Try to make restriction to `Herm_circ(3)` and the unique AM-GM extremum select the Frobenius point. | Equal weighted energies give `kappa(lambda) = 2/(1 + 3 lambda)`, so AM-GM is unique only after `lambda` is supplied and does not select `lambda = 0`. | ATTEMPTED |

These are distinct approach families under the proof-search-governance tuple:
they use, respectively, the positivity cone, group invariance, representation
block structure, projective normalization, and constrained extremization as
their load-bearing mechanisms.

## N2 — Wall-independence audit

The no-go has no list of independent walls. It proves one narrow implication
false by counterexample. The one condition for recovering the old positive
route is a premise or derivation fixing the relative isotype-weight ratio;
`beta = 0`, equal block weights, and the Frobenius point are equivalent names
for that single condition, not three walls.

## N3 — Hidden-wall scan

The proof uses only the displayed definition of `B_{alpha,beta}`, the
scalar/traceless decomposition, cyclicity of trace, and positivity of
`Tr(H^2)` for nonzero Hermitian `H`. It does not use “we assume,” “by
construction,” “as is standard,” “the framework provides,” “bridge context,”
“background,” “naturally,” “obviously,” “standard QFT,” “registered,” or
“canonical” as a load-bearing step. The conditional corollary explicitly
labels `beta = 0` as externally supplied and keeps it outside the no-go proof.

## N4 — Residual matching

No prior no-go is used as a witness. Earlier audits motivate the repair but
are not proof inputs. The present residual is exactly “the listed
linear-algebra premises do not imply `beta = 0`,” and the `B_{1,1}` witness
directly negates that implication.

## N5 — Rhetoric audit

The negative statement is only about bilinear forms on the finite-dimensional
space `Herm(3)`, plus its `Herm_circ(3)` restriction for the AM-GM check. It
makes no per-site, per-mode, or lattice-wide claim. It does not say that
Frobenius normalization is impossible to derive from stronger premises or
that the physical charged-lepton relation cannot be derived.

## N6 — Partial-closure path scan

A source-authoritative convention, a retained theorem, or another approved
premise that fixes the scalar/traceless ratio to one would close the old
conditional positive route. Such a path adds information beyond the three
premises tested here and therefore does not contradict this no-go. The source
note explicitly leaves that route open and does not call it a required new
axiom.

## N7 — Steelman

A hostile reviewer can strengthen “Ad-invariant positive inner product” to
“the Hilbert-Schmidt form inherited from the ambient matrix algebra with its
trace normalization.” That stronger definition fixes `beta = 0` immediately
and restores `kappa = 2`. It does not defeat the stated no-go, because
inheritance with fixed relative normalization is precisely the additional
premise absent from positive-definiteness, Ad-invariance, and block
orthogonality. No concrete route was found that makes the three stated
premises alone exclude `B_{1,1}`.

## N8 — Cross-cycle echo

Repository searches found later Koide notes that reuse the same free
isotype-weight ratio, including
`docs/KOIDE_FINITE_BETA_WEIGHT_IS_THE_PARTITION_BIT_NOTE_2026-06-02.md` and
`docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`.
They expose possible selector or partition inputs but do not invalidate the
finite-dimensional counterexample. No cross-cycle mechanism was found that
derives equal isotype weights from the three premises tested here.

## Gate result

**PASS.** All eight checks preserve the narrow no-go. The strongest surviving
positive route requires an additional relative-normalization premise or
derivation and remains outside this claim.
