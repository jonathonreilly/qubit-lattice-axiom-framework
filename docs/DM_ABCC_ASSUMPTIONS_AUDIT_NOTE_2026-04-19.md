# A-BCC input audit: quaternion representations and supplied source paths

**Type:** bounded_theorem
**Date:** 2026-04-19; mathematical scope corrected 2026-10-21.
**Status:** partial narrowing of the former “FULL NO-GO”; no exhaustive impossibility result or physical basin closure.
**Primary runner:** `scripts/frontier_dm_abcc_assumptions_audit.py`.
The former source and PASS/status summaries are recoverable at f24d17d97d372df977476e4a69674577f31af575. Historical CP-fit labels are not current experimental evidence.

## 1. Supplied chart, not an algebra-derived physical sector

The diagnostic uses E1=sqrt(8/3), E2=sqrt(8)/3, Gamma=1/2 and

```text
H0 = [[0,E1,-E1-i Gamma],[E1,0,-E2],[-E1+i Gamma,-E2,0]],
M  = [[1,0,0],[0,0,1],[0,1,0]],
D  = [[0,-1,1],[-1,1,0],[1,0,-1]],
Q  = [[0,1,1],[1,0,1],[1,1,0]],
H(m,delta,q)=H0+m M+delta D+q Q.
```

These matrices and the chamber q+delta>=E1 are supplied model choices. det(H0)>0 and det(M)=-1. For fixed delta,q the determinant tends to -infinity as m tends to positive infinity. Since the chamber imposes no upper bound on m, it does not force a positive determinant. The runner gives an exact chamber witness, not only a finite percentage.

C_base means the connected component of the nonsingular **source domain** containing the baseline. It lies in the positive-determinant locus but need not equal that entire locus. In the full Hermitian space, equal determinant signs need not mean equal inertia. No complete component classification of this affine source chamber is claimed.

## 2. Correct quaternion module statement

Cl^+(3,0) is isomorphic as a real algebra to the division algebra H. It has **one** irreducible unital left real module up to equivalence, namely H itself, of real dimension four. Proof: for a nonzero vector v in an irreducible module V, q -> qv is injective because every nonzero q is invertible. Its nonzero image is an invariant submodule, hence all of V. Thus V is isomorphic to H.

A right H action is an action of the opposite algebra; it does not supply a second inequivalent left H module. Quaternion conjugation identifies H with its opposite algebra. Concretely, if C(x)=bar(x), L_q(x)=qx and R_q(x)=xq, then C L_q C=R_bar(q). The runner verifies this on the real basis 1,i,j,k, with the multiplication identities.

For complex-linear representations of the real algebra, complexification H tensor_R C is M2(C), giving the unique complex irreducible of dimension two. The spin-1 three-dimensional representation of the rotation group is a group/Lie-algebra representation, not a unital three-dimensional complex representation of the associative algebra H. Weyl handedness under a Lorentz spin group requires additional structure; it is not two irreducible modules of Cl^+(3,0).

Therefore choosing left versus right quaternion notation cannot, by itself, impose a determinant sign on the independently supplied three-dimensional flavor operator. No physical chirality-to-flavor map is derived here.

## 3. Kramers hypotheses and embedding scope

Kramers pairing requires a normalized antiunitary T with T^2=-I **and** a Hermitian operator commuting with T. A map whose square is -(1/4)I is not antiunitary in the same norm; it needs normalization before the theorem applies. The existence of quaternion multiplication does not prove that an arbitrary observable is T invariant.

There is no antiunitary T=UK on C^3 with T^2=-I: unitarity gives det(U bar(U))=|det U|^2=1, whereas det(-I3)=-1. This is a same-space obstruction. It is not a prohibition on embedding a three-dimensional complex Hermitian matrix in a larger quaternionic system.

Indeed, for any complex Hermitian A, set A_tilde=diag(A,bar(A)) and J=[[0,I],[-I,0]]. Then T=JK obeys T^2=-I and commutes with A_tilde. This six-dimensional lift has paired eigenvalues but does not make A positive: negative eigenvalues of A remain negative in the lift. The runner tests A=diag(-1,2,3) explicitly. Thus the earlier unrestricted “quaternionic embedding impossible” statement is withdrawn; positivity would be a separate assumption.

## 4. What the numerical fixtures support

The old decimal sources (Basin1, Basin2, BasinX) are retained as fixtures, not claimed physical solutions or current CP exclusions. The current 20x10x10 chamber grid has 1063 negative determinants among 2000 samples (53.15%); this is a sampling statistic, not the fraction of a defined chamber measure. The former 6000-point/5769 count did not describe the current runner.

For those rounded sources the runner samples a positive Basin1 path, with minimum near 0.8783, and a Basin2 sign change near 0.028. These samples do not certify positivity on a continuum interval. Opposite endpoint determinant signs do prove a zero somewhere on every continuous path, by IVT; they do not imply exactly one crossing or its location on every path.

Continuity alone does not preserve nonsingularity. A continuous path that is assumed nonsingular preserves full inertia; deciding whether the physical preparation supplies that assumption remains open. The [PNS source](DM_ABCC_PMNS_NONSINGULARITY_THEOREM_NOTE_2026-04-19.md) supplies a conditional implication, not a derivation of the premise. The [P3 source](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md) addresses a specified endpoint/path. Neither logically identifies the physical endpoint merely by checking a path already chosen to reach it.

## 5. Corrected closure accounting

The [DPLE correction](DM_DPLE_DIMENSION_PARAMETRIC_EXTREMUM_THEOREM_NOTE_2026-04-19.md) bounds log-absolute-determinant minima and evaluates an added chart predicate; it does not force F4, uniquely select dimension three, or discharge A-BCC. The [sign-blindness companion](DM_DPLE_ABCC_NO_GO_NOTE_2026-04-19.md) applies only to W-only rules on sign-paired pencil classes. H -> -H need not preserve this fixed baseline or chamber.

This note does not reconcile old “CLOSED” summaries by promoting them. It supersedes their use as current authority and distinguishes conditional source mathematics from physical selection. It establishes no current experimental exclusion, no complete search over all algebraic routes, no independence/minimality of the remaining inputs, and no claim that a new axiom is necessary. The current [four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) does not itself identify these finite chart fixtures with physical PMNS data.

## No-Go Discipline Gate

This repair is partial narrowing, not packet PASS. N1: two mathematical checks are executed (module equivalence and same-space antiunitary/embedding structure); no five-family exhaustive search is asserted. N2: no independent-wall count. N3: chart, representation category, normalization and commutation hypotheses are explicit. N4: the quaternion checks concern representations, while P3/PNS concern a supplied path; neither is evidence for the other's missing physical identification. N5: finite basis entries, finite blocks and sampled source paths only; no site or lattice dynamics. N6: larger embeddings, additional dynamics and physical sector identification remain possible; no primitive absence or new-axiom necessity is asserted. N7: a physical preparation law could select a nonsingular component, but would need a proof without assuming the desired endpoint; this concrete escape is outside the finite algebra check. N8: the same-day PNS conditional source is an existing partial route, not a completed derivation of that law. The five-family procedural requirement is unmet and explicitly withheld, independently of the exact module identities.
