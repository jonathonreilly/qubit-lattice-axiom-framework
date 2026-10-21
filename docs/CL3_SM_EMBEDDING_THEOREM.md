# Supplied Cl(3) carrier: commuting actions and a restricted determinant identity

**Date:** 2026-04-19; correction 2026-10-21
**Type:** bounded_theorem
**Primary runner:** `scripts/verify_cl3_sm_embedding.py`
**Status authority:** independent audit lane only.

## Supplied construction

On `V=(C^2)^tensor3`, supply Pauli matrices and
`Gamma1=X tensor I tensor I`, `Gamma2=Z tensor X tensor I`,
`Gamma3=Z tensor Z tensor X`. They obey the Euclidean Clifford relations.
The real even algebra has basis `I,e12,e13,e23` and is isomorphic to `H`.
Its unit quaternions form SU(2); the Lie algebra has three generators, not four.
The central `omega=Gamma1 Gamma2 Gamma3` squares to `-I` and is independent
of that four-dimensional even span. It defines a central U(1) action; identifying
it with physical hypercharge is an additional bridge.

Supply a base/fiber split `C^4 tensor C^2` and swap the two base bits.
`P_sym=(I+swap)/2` has rank six and `P_asym` rank two. The selected operator
`Y=(1/3)P_sym-P_asym` has eigenvalues1/3 and−1 with those multiplicities and
trace zero. It commutes with the separately supplied fiber generators
`Jf_i=I4 tensor sigma_i/2`. An SU(3) action embedded on the symmetric
three-dimensional base also commutes with the fiber action and Y. These are
matrix constructions, not a derivation of physical color, weak interactions,
charges, anomaly cancellation or three generations from a one-site algebra.
The bare three-state axis orbit does not even have uniform restricted Y values.

## Coupling normalization remains supplied

The dimensions4 and5 are algebraic facts. Defining `g2^2=1/4` and `gY^2=1/5`
is a separate normalization prescription. Neither dimension counting nor
`L=(1/g^2)Tr(F^2)` fixes the coefficient multiplying an invariant kinetic term.
Any positive coefficient preserves its algebraic symmetries. The identity
matrix is not a fourth su(2) Lie generator.

In this eight-dimensional realization, the ordinary trace gives
`Tr(Jf_i Jf_j)=2 delta_ij`, not `delta_ij/2`; the latter is the usual
fundamental two-dimensional trace convention. A normalized trace may be
chosen, but that convention still cannot select a physical coupling.
Given the supplied reciprocal-dimension prescription, the arithmetic
`gY^2/(g2^2+gY^2)=4/9` follows. This is not a prediction of a measured angle.

## Restricted L-sector determinant: valid conclusion, corrected proof

Restrict `J1=(i/2)e23`, `J2=(i/2)e13`, `J3=(i/2)e12` to the four-dimensional
even-parity subspace. They are Hermitian and satisfy
`{Ji,Jj}=(delta_ij/2)I4`, `Tr(Ji)=0`.
For real `a,b1,b2,b3`, write `H=a I4+B`, `B=sum bi Ji`. Then
`B^2=(|b|^2/4)I4`. If `b!=0`, tracelessness gives eigenvalues
`+|b|/2` and `−|b|/2`, each twice. If `b=0`, H is scalar. Thus exactly

```
det(H) = (a^2-|b|^2/4)^2 >= 0.
```

This is a statement about that explicit four-real-parameter class. It says
nothing about every Hermitian matrix on the same space: `diag(-1,2,3,4)` has
determinant−24. Nor does nonnegative determinant imply positive definiteness.

The old Kramers proof omitted the commutation hypothesis. With the supplied
matrices, `U=2J2` is unitary and the antiunitary `T=U K` satisfies `T^2=-I`.
But `T J2 T^-1=-J2`, so a generic H in the displayed span is not T-invariant.
The unnormalized `J2 K` is not antiunitary. Kramers degeneracy applies to
Hermitian H satisfying `U conjugate(H) U^dagger=H`; it is not applicable merely
because the vector space admits such a T. The polynomial proof above retains
the restricted determinant result without that invalid inference.
No A-BCC sheet, positivity of a physical charged matrix or experimental
exclusion follows from this identity.

## Related mathematical constructions and limits

The [native gauge note](NATIVE_GAUGE_CLOSURE_NOTE.md) and
[systematic budget note](YT_EXPLICIT_SYSTEMATIC_BUDGET_NOTE.md) record additional
physical conventions and bridges; they are not supplied by these matrix identities.
The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) remains the foundation.
Original arguments are recoverable at `f24d17d97d372df977476e4a69674577f31af575`.
Stable filenames do not preserve withdrawn coupling or Kramers claims.

Prior work includes [Susskind, Lattice fermions (1977)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.16.3031),
[Furey, Standard model physics from an algebra? (2016)](https://arxiv.org/abs/1611.09182),
and [Stoica, The Standard Model Algebra (2017)](https://arxiv.org/abs/1702.04336).
These are related lattice/Clifford constructions, not proofs of this supplied
carrier's physical identification. No priority or equivalence claim is made.

## Verification

The runner checks finite matrix identities, the chosen normalization arithmetic,
T-invariance controls and the restricted determinant formula. Numerical checks
are finite support for the displayed hand proof, not physical selection evidence.
A nonzero failure count exits nonzero when run as a script.
