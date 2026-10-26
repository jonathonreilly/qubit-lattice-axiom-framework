# Axis relabeling of a supplied finite-volume SU(3) kernel

**Date:** 2026-06-02; conditional-scope correction 2026-10-23
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_cluster_decomp_delta_x_su3_axis_permutation_2026_06_02.py`
**Authority role:** conditional operator relabeling, not physical Wilson transfer
construction or a supply of physical H1/H2. Audit status is independent.

## Premises and recovery

The [corrected temporal parent](CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md)
proves a theorem for a supplied smooth, strictly positive, real symmetric
kernel. It does not identify that kernel with the transfer operator of a
canonical Wilson or fermion action. The former companion's physical H1/H2
supply assertions are withdrawn. Complete old note, runner and cache are
recoverable at commit `8c9957e651a04ae4e156e6cdacc608ffc93dc876` under the
same paths; the repair evidence also preserves their bytes.

Let E be a fixed finite link-label set, X=SU(3)^E with normalized product Haar
measure, and tau>0. This is a compact continuous configuration space;
L²(X) is infinite dimensional despite finite E. Supply

```
T(U,V) = a(U,V) product_l K_tau(U_l V_l^dagger),
a(U,V)=a(V,U)>0, a smooth and real.
```

The parent specifies the heat-kernel Casimir normalization C2(1,0)=4/3,
C2(1,1)=3 and weights exp(-tau C2/6). Choosing
`a=exp(-beta S(U,V))` requires S to be smooth, real and symmetric.
Calling S a Wilson increment does not prove these hypotheses or the
physical action-to-transfer correspondence. The runner supplies only
unweighted single-link spectrum data; it does not calculate interacting a.

## Conditional relabeling theorem

Supply a bijection of the finite factor labels preserving the measure and
transport the entire kernel, including a and any boundary data, by it.
The induced pullback U on L²(X) is unitary, since product Haar integrals are
unchanged by relabeling. The transported operator is U T U^-1: substitution
in its integral proves this identity. Thus smoothness, symmetry, strict
pointwise positivity, compactness, trace class and spectrum are preserved.
This is a relabeling of supplied data, not an assertion that distinct physical
spatial/temporal slabs, their extents or boundary conditions coincide.

Under the parent's hypotheses T is self-adjoint, smoothing and trace class;
its strictly positive kernel is positivity improving. The parent's
Perron–Jentzsch conclusion gives a simple spectral radius r>0 and off-top
spectral modulus s<r. Unitary conjugacy preserves r, s and the modulus gap
r-s>0. The normalized decay rate is -log(s/r), with infinity if s=0.
These conditional operator conclusions do not derive a Hamiltonian or a
physical spatial transfer operator.

Pointwise kernel positivity does not imply positive semidefiniteness of the
operator: [[1,2],[2,1]] has positive entries and eigenvalues3,-1. A positive
transfer operator suitable for taking a Hamiltonian logarithm is additional
input. No physical action-to-transfer correspondence is derived.

## Relationship to the spatial slab bridge

The [spatial slab bridge](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
requires H1 (a positive Hermitian physical slab transfer operator with the
appropriate partition-function/local-observable identification) and H2 (its
strict normalized spectral gap). The constructed kernel theorem supplies
neither the physical identification nor positive semidefiniteness in general.
It therefore does not discharge H1/H2 for a pure-Wilson or full canonical
surface. If those additional hypotheses are supplied and verified, the
bridge's conditional spectral bounds may be applied; its finite-temperature
extension separately requires a trace-class thermal operator.

## Runner scope

The unchanged quantitative controls evaluate the same truncated single-link
heat weights at tau=2 and p+q<=12, compare with cutoff14, inspect the trivial
and fundamental weights and compare identical data under an axis label.
The two-cutoff difference is not a certified infinite-series tail estimate.
The nonidentity sample uses a normalized power of the fundamental character,
not the SU(3) Weyl/Schur character formula; it is a heuristic fixture and does
not prove heat-kernel positivity. Those values and tolerances remain for
recovery and comparison, with honest output labels. The analytic result rests
on the parent's hypotheses and the explicit unitary substitution above.

Documentary checks bind the corrected parent and this note. File presence,
printed assertions and a PASS count confer no retention or physical authority.
No new axiom, thermodynamic/continuum/uniform-volume gap, spatial clustering
of the physical action, fermion extension or Yang–Mills mass gap is claimed.
