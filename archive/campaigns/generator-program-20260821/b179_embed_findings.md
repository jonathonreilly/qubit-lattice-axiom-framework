# Block 179 — cross-lane embedding probe (physics tier)

SCOPE: exact finite algebra at the committed 12x6 constant carrier; rational or
disclosed cyclotomic decisions only. Addendum-10's cross-block test is not reused.

## T1. Flavor-lane objects and the conditional input

Authorities: the 2026-06-04 and 2026-06-15 notes/runners from `origin/main`.

The fork uses the regular real module `R[Z_3]`: generator
`C=[[0,0,1],[1,0,0],[0,1,0]]`, singleton projector
`P_s=(I+C+C^2)/3`, and doublet projector `P_d=I-P_s`.
The runner uses columns `(1,-1,0),(1,1,-2)` for the doublet and `(1,1,1)` for
the singleton, with `J=B[[0,-1,0],[1,0,0],[0,0,0]]B^-1`, so `J^2=-P_d`.
Its determinant acts on `M(alpha,beta)=alpha P_s+beta P_d`: the runner proves
`det_R M=alpha beta^2`; after a chosen doublet complex structure, its
holomorphic 1x1 doublet block is tested by the runner's `det_cpair` and its
2x2 real metric by `complex_realification`.

`POLARIZATION-SELECT` requires as input a polarization already SUPPLIED for the
generation doublet: either two real slots, or a chosen `J` with `J^2=-P_d` so
the doublet counts as one complex slot. The fork does not select either input;
changing Gaussian to Berezin statistics does not select it.

The translation theorem's supplied carrier is the 2x2x2 site module. Its eight
`Z_2^3` characters are `psi_k(n)=(-1)^(k.n)/sqrt(8)`. The three `hw=1`
characters form a transitive orbit under the coordinate cycle
`(x,y,z)->(z,x,y)`, the flavor lane's `C_3` action; its runner constructs the
rank-one character projectors exactly but assigns no physical generation role.

## T2. Exact 12x6 embedding

The probe imports `block174_gate_solve`, installs only in memory
`RULES["const"] = lambda t,x: Rational(7,5)`, and builds `Width(6,"const")`.
Thus `T_phys=6`, `N=36`, `Q` is symbol-free rational, and
`inertia(herm(Q))=(36,0,0)` exactly. Let `U|t,x>=|t,x+2 mod 6>`.
Entrywise, `U^3=I`, `U^dag U=I`, and `[Q,U]=0`.

DISCLOSED CYCLOTOMICS: `omega=(-1+i sqrt(3))/2`, so all non-rational entries
lie in the exact field `Q(omega)=Q(sqrt(-3))`, with `omega^2+omega+1=0`.
The projectors are `P_k=(I+omega^(-k)U+omega^(-2k)U^2)/3`. Exactly,
`P_k^dag=P_k`, `P_k P_l=delta_kl P_k`, `sum P_k=I`, and `tr P_k=12`.

On the abstract doublet take the orthonormal basis
`a=(2,-1,-1)/sqrt(6)`, `b=(0,1,-1)/sqrt(2)`. Its generator matrix is
`R_omega=[[-1/2,-sqrt(3)/2],[sqrt(3)/2,-1/2]]`. On the chart orbit
`(t,x)=(0,0),(0,2),(0,4)`, set
`f_k=3^(-1/2) sum_j omega^(-kj)|0,2j>`. Then
`Uf_1=omega f_1`, `Uf_2=omega^2 f_2`, `f_2=conj(f_1)`, and `P_k f_k=f_k`.

The real-linear intertwiners are `T_1=[f_1, i f_1]` and
`T_2=[f_2,-i f_2]`: entry-for-entry, `U T_1=T_1 R_omega` and
`U T_2=T_2 R_omega`. Thus the complexified abstract doublet has the exact
conjugate `(k=1,k=2)` chart pair. The holomorphic realization uses `T_1`;
ambient multiplication by `i` obeys `i T_1=T_1 J`, with
`J=[[0,-1],[1,0]]`, `J^2=-I`, and `[J,R_omega]=0`.

## T3. Non-vacuous antilinear test and induced metric

Inspected assembly sites: closure-audit-two runner lines 137-140 declares the
only quotient field measure `exp(-phi^dagger Q phi)` and covariance
`<phi_i phibar_j>=Q^-1`; lines 607-617 assemble `Q=m Hq+Kq`; the imported
cover action is `mH+i(Hd+d^dagger H)` at bare-character lines 542-546.
Every field occurrence in that committed layer has one conjugated and one
unconjugated leg. There is no `phi^T B phi`, conjugate partner, Nambu doubling,
or Majorana block in the form grammar: the committed class is sesquilinear-only.

For `phi=z f_1`, the direct restriction (not a cross-sector block test) is
`phi^dagger Q phi=(3193/2240) conjugate(z) z`. On the doublet real basis
`(f_1,i f_1)`, the induced operator metric is therefore exactly
`G_d=complex_realification(3193/2240)=diag(3193/2240,3193/2240)`.
This exhibits one ambient complex direction and no antilinear `z^2` or
`conjugate(z)^2` term. The rejected identity `P_1 Q P_2=0` is neither computed
nor used as evidence.

## T4. The fork fires

The probe loads the fork runner itself from `origin/main` and calls only its
exact `CPair`, `det_cpair`, `complex_realification`, `det_fraction`,
`pfaffian_2x2`, `r_from_slot_count`, and `q_from_r`; its floating motivation
replay is not called. With `beta=3193/2240`, their own functions give
`det_C[[beta]]=beta` and `det_R(complex_realification(beta))=beta^2`
`=10195249/5017600=norm2(det_C)`.

Their four cells read exactly: real Gaussian `(2 real,r=1,Q=1)`; Majorana
Berezin `(2 real,r=1,Q=1)`; holomorphic Gaussian
`(1 complex,r=1/2,Q=2/3)`; holomorphic Berezin
`(1 complex,r=1/2,Q=2/3)`. The committed measure is the holomorphic-Gaussian
cell; the Berezin cell is the runner's equal-count control, not a relabeling of
the gravity measure. Therefore the HOLOMORPHIC cell applies and gives `Q=2/3`.

## T5. Verdict and honest residue

VERDICT: for the explicit doublet, `POLARIZATION-SELECT` is SUPPLIED at
action/type level: ambient `i` is its `J`, and no antilinear term is induced.

This does not identify the flavor carrier. Their group is the `C_3`
cube-diagonal/coordinate-cycle rotation on the `Z^3` shell (`hw=1` characters
in the theorem fixture); ours is chart translation `x->x+2`. We proved the two
abstract `R[Z_3]` doublet matrices isomorphic. If the fork requires their
specific physical action, the precise residue is an observable-preserving,
equivariant carrier map from that `hw=1`/cube-rotation carrier into the selected
chart line, not merely equality of representation matrices.

Also unresolved: the flavor `M_2(C)` carrier was not embedded as an algebra;
each `P_k` has multiplicity 12, with no orbit or `k=1`/`k=2` selector. No mass
spectrum or readout is derived; `Q=(1+2r)/3` remains imported authority.

## 10-line summary
- SUPPLIED: exact `R[Z_3]` doublet-to-chart intertwiner.
- SUPPLIED: ambient `i` realizes the embedded doublet's `J`.
- SUPPLIED: committed restriction is sesquilinear, `beta|z|^2`.
- RESIDUE: cube-diagonal `C_3` is not physically identified with chart `U`.
- RESIDUE: the flavor `M_2(C)` carrier algebra is not embedded.
- RESIDUE: the rank-12 chart multiplicity has no selector.
- RESIDUE: the `k=1`/`k=2` orientation has no selector.
- Q-VALUE: fork-arbiter holomorphic slot count gives `r=1/2` exactly.
- Q-VALUE: the imported Koide lever then gives `Q=2/3` exactly.
- STATUS: counting-bit supplied for this embedding; full flavor bridge remains.
