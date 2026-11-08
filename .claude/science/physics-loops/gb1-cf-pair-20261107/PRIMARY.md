# Primary calculation: five-state two-plaquette model

Status: exact author calculation completed; no independent-check or audit status.

Source identities: main `f5af11cd0102cfd0b51aef0911f600130bf5beb1`;
assembly definitions `fb9508e8390bf66da8f29ddb44611d2a531768cb`,
`.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md` §§1.1–1.3;
the local `PRIMARY_SPEC.md` and `GOAL.md`. The source extraction inadvertently
displayed §§1.4–1.5 as well; they are not inputs to this calculation. No
external physics sources are being consulted under this bounded dispatch.
The workhorse procedure is used only for this scoped author computation.

Supplied construction data: five states per link, the stated `P_mu`, the
seven oriented links and reverse-ordered loop convention, gauge transformations
at every vertex, and no external links or matter charges. The latter is a
supplied boundary sector. Neither it nor the dynamics is derived from the four
physical axioms.

## Result and current checkpoint

The supplied zero-external-charge physical space has dimension four. In the
ordered orthonormal basis `(empty-flux, L, R, O)`, where `O` is the outer
six-link cycle, the left magnetic operator has couplings `empty-flux ↔ L = 2`
and `R ↔ O = 1`; the right operator has exchanged couplings. In particular,
`[B_L,B_R]|L> = -3|R>` exactly. They do not commute even on this physical
sector. A chronological ordered product breaks square exchange at second
order, and the palindromic Strang product breaks it at third order. The joint
exponential preserves gauge covariance and exchange exactly at finite angles,
as does its composition with the uniform on-link electric layer. These are
properties of the stated finite mathematical model, not an axiom-derived law.

The final numeric job completed in 1.041 seconds with peak RSS 27,639,808
bytes. It used Python 3.13.5 and exact rational/Gaussian-rational arithmetic,
an 80-second alarm, a 240 MB RSS stop, and one thread for each requested math
library setting. The numeric preflight passed; lease
`gb1cf-primary-20261107-run02` was acquired and released. The runner created
no dense matrix larger than `10 × 10`. The full link space has dimension
`5^7 = 78125`; its vectors and loop operations were represented sparsely.
The source hash executed was
`3f2e47d0b2d5737d1dfa4c2586586f860d18556ece82197ea9ca1ecaa12c4e30`.
The preceding run (0.9885 seconds, 27,590,656 bytes) is retained in the same
log. The final source revision added the explicit `AUDIT_TIMEOUT_SEC=80`
constant requested by the supervisor and robust Gaussian-number formatting;
both runs produced the same scientific results. There were no failed numeric
executions. Only resource/timing diagnostics use floating-point values.
Model and reasoning effort were inherited unchanged from the supervising
host; this worker does not infer an unavailable concrete model identifier.

All assigned author obligations below have an argument and exact self-check.
The next decision is the supervisor's independent comparison and review.
No other worker's output was read. The abandoned route was the initial
root-level `GB1QL.md` lookup, which failed; the pinned nested source was then
located. There was no failed physics search or claimed no-go theorem.

## 1. Link algebra and endpoint conventions

Let `Q = sum_{mu=1}^4 |mu><mu|` and `Q_mu = 2 P_mu`. Write

```
J_1=L_23, J_2=L_31, J_3=L_12,   K_a=L_a4,
N+_a=(J_a+K_a)/2,                N-_a=(J_a-K_a)/2.
```

Direct matrix multiplication gives

```
[N+_a,N+_b]=i epsilon_abc N+_c,
[N-_a,N-_b]=i epsilon_abc N-_c,   [N+_a,N-_b]=0,
sum_a (N+_a)^2 = sum_a (N-_a)^2 = (3/4)Q = E^2,
[P_mu,P_nu]=(i/4)L_mu,nu.
```

For example, `[L_mu,nu,P_rho] = i(delta_mu,rho P_nu -
delta_nu,rho P_mu)`. Substitution into `U=P_4 I+i P_a sigma_a` yields

```
[N+_a,U] = -(sigma_a/2) U,
[N-_a,U] = U (sigma_a/2).
```

The signs depend on which side implements the observable conjugation. Here
the Gauss generator at a vertex is

```
G_v,a = sum_{links ending at v} N+_a
      + sum_{links starting at v} N-_a.
```

For `h_v=exp(i alpha_v,a sigma_a/2)`, let the state representation be
`D_v(h_v)=exp(i alpha_v,a G_v,a)`. The chosen Heisenberg convention is
`D(h)^dagger U_(x,y) D(h) = h_y U_(x,y) h_x^(-1)`. The displayed
commutators prove this by exponentiation. Endpoint actions on adjacent
vertices commute because `N+` and `N-` commute on their shared link. Each
`G_v` is an su(2) triple. The physical subspace is their joint kernel,
equivalently the invariant subspace under all six state representations.

This link matrix is not a rotor-valued unitary. With
`S=sum_mu P_mu^2 = |0><0|+Q/4`, exact identities are

```
U^dagger U = I_2 tensor S - (1/2) sum_a sigma_a tensor N-_a,
U U^dagger = I_2 tensor S - (1/2) sum_a sigma_a tensor N+_a.
```

Both are rank-four projectors on the ten-dimensional color/link space,
so `U` is a partial isometry, not a unitary. This does not obstruct the
endpoint covariance just proved. The orientation reversal operator on the
five-state register is `C=diag(1,-1,-1,-1,1)`: it obeys
`C U C=U^dagger` and `C N+_a C=N-_a`.

The runner checks all these finite matrix identities using exact Gaussian
rationals, including both Casimirs and both endpoint commutators. Its
`U^dagger U` idempotence/rank check is a self-check, not an independent gate.

## 2. Gauge covariance and the complete physical sector

For a traversed edge, use `F=U` in the stored direction and `F=U^dagger`
in the opposite direction. In both cases `F` transforms as
`h_destination F h_origin^(-1)`. For a closed traversal with successive
factors `F_1,...,F_n`, define

```
W_C = tr(F_n ... F_1),   B_C = W_C+W_C^dagger.
```

In this exact order every adjacent gauge factor cancels. The product
transforms by conjugation at the starting vertex, hence its color trace is
invariant on the entire finite link Hilbert space. This proof does not use
unitarity of `U`. In particular, every `B_C` commutes with all `G_v,a`.

The link representation is `(0,0) + (1/2,1/2)` under its two endpoint
SU(2) actions. Indeed, `|0>` is killed by both triples; each triple has
Casimir `3/4` on the remaining four states, and the commuting endpoint
actions there have dimension `2 × 2`. Thus an occupied link contributes one
spin-half at each endpoint. An unoccupied link contributes the trivial
representation. All occupation projectors commute with the gauge actions.

At a vertex of this graph the occupied degree is at most three. A singlet
exists exactly at degree zero or two: one or three spin-halves have only
half-integral total spin, while `1/2 tensor 1/2 = 0 + 1` contains one
singlet. Consequently an admissible occupation pattern must be an even
subgraph and has one invariant vector, not several. Endpoint tensor factors
may be regrouped by vertices, so the singlet multiplicities multiply; there
is no additional link constraint after its `(1/2,1/2)` factors are assigned.

This graph can be counted explicitly. Let `l=n_AB` and `r=n_BC`.
The corner constraints give `n_AD=n_DE=l` and `n_CF=n_EF=r`.
The middle constraints give `n_BE=l XOR r`. Thus, in the prescribed link
order, all possibilities are

```
(l,r,l,r,l,l XOR r,r),   l,r in {0,1}.
```

They are the empty subgraph, the left square, the right square, and the
outer cycle. This proves physical dimension four for the supplied
zero-external-charge boundary. It does not infer that boundary from a
larger lattice or from a physical state-selection rule.

Let `|Omega_0>=|0>^tensor7` denote only the empty-flux reference, and put
`|C>=W_C|Omega_0>` for the three simple cycles. For `e_4=I_2` and
`e_j=i sigma_j`, an amplitude on a length-`n` cycle is

```
2^(-n) tr(e_mu_n^(direction_n) ... e_mu_1^(direction_1)),
```

where a negative direction means Hermitian adjoint and all other links
remain in state zero. A product of quaternion basis elements is a signed
basis element. Its trace is either zero or `+/-2`. Exactly `4^(n-1)` label
assignments give a scalar product: after the first `n-1` labels there is
one possible last basis index. The nonzero amplitudes therefore have
magnitude `2^(1-n)`, and the norm squared is
`4^(n-1) 2^(2-2n)=1`. Distinct occupation patterns make the four vectors
orthogonal. Gauge covariance proves their invariance, and the dimension
argument proves their completeness.

The script independently enumerates the 128 occupation patterns within its
own implementation, builds the three sparse loop vectors, checks the exact
Gram matrix, and applies all 18 Gauss generators to each basis vector. The
support sizes are `1,64,64,1024`; square amplitudes are `+/-1/8` and outer
amplitudes are `+/-1/32`. These are author checks of the proof, not separate
lineages of evidence.

## 3. Exact magnetic operators and a noncommutation witness

Because each loop uses distinct links, its operator expansion is a sum of
commuting-link Hermitian tensor products with real quaternion trace
coefficients. Hence `W_C=W_C^dagger` and `B_C=2W_C`. In terms of toggles
`Q_mu=|mu><0|+|0><mu|`, the expansion is

```
B_C = sum_(mu_1,...,mu_n)
      [2^(1-n) tr(e_mu_n^(direction_n)...e_mu_1^(direction_1))]
      tensor_(edges in C) Q_mu_edge.
```

This supplies the full operators without a full dense matrix. There are
64 nonzero terms for each square and 1024 for the outer cycle. Each square
toggle flips exactly its occupied edges, so the sector images are fixed by
the preceding dimension count. The coefficient from empty flux to its
cycle is `2` by normalization. Hermiticity gives the reverse coefficient.

For the cross coefficient, abbreviate link labels on
`(AB,BC,DE,EF,AD,BE,CF)` as `(a,b,c,d,e,f,g)`. Applying `W_L` to
`|R>` annihilates the shared `BE` label and creates the other three left
labels. The coefficient of an outer-cycle configuration is

```
2^(-8) sum_f tr(e_e^dagger e_c^dagger e_f e_a)
                  tr(e_f^dagger e_d^dagger e_g e_b)
= 2^(-7) tr(e_e^dagger e_c^dagger e_d^dagger e_g e_b e_a).
```

Here the exact completeness identity
`sum_mu tr(A e_mu) tr(e_mu^dagger B)=2 tr(AB)` follows from the
Hilbert-Schmidt orthogonality `tr(e_mu^dagger e_nu)=2 delta_mu,nu`.
The normalized outer coefficient is `2^(-6)` times the last trace, so
`W_L|R> = |O>/2`. Therefore `B_L|R>=|O>`; Hermiticity and reflection
give the other cross coefficients.

For completeness, the same argument covers two cycles sharing a longer
path. Reverse one cycle if necessary so the shared path is traversed in
opposite directions; this does not change its real trace. For a shared
path of length `k`, its quaternion product takes each signed basis index
`4^(k-1)` times after signs cancel between the two traces. The contraction
factor is `2*4^(k-1)`. Since the new cycle has length `n+m-2k`, the ratio
to its normalized coefficient is again
`2*4^(k-1)*2^(-2k)=1/2`. This also gives the outer-loop cross couplings.

In the basis `(Omega_0,L,R,O)` the exact matrices are

```
B_L = [0 2 0 0]    B_R = [0 0 2 0]    B_O = [0 0 0 2]
      [2 0 0 0]          [0 0 0 1]          [0 0 1 0]
      [0 0 0 1]          [2 0 0 0]          [0 1 0 0]
      [0 0 1 0]          [0 1 0 0]          [2 0 0 0].
```

The sparse runner computes each matrix element and also verifies equality
of each full sparse image with its projected four-state reconstruction.
There is no untested leakage term hidden by projection. Thus

```
[B_L,B_R] = [0  0 0 0]
            [0  0 3 0]
            [0 -3 0 0]
            [0  0 0 0],

[B_L,B_R]|L> = -3|R>,   ||[B_L,B_R]|L>||^2 = 9.
```

This physical vector is also a full-Hilbert-space witness. The commutator
kills the empty-flux reference and the outer-cycle state, so checking only
the empty-flux reference would have missed the failure.

On the physical space the unital associative complex algebra generated by
`B_L,B_R` is all `M_4(C)`. Indeed,
`B_L^2=diag(4,4,1,1)` and `B_R^2=diag(4,1,4,1)`. Products of their
spectral projectors give all four one-dimensional basis projectors: for
example `P_empty=(B_L^2-I)(B_R^2-I)/9`. Sandwiched magnetic operators
then give matrix units along the four nonzero graph edges, and their
products give every matrix unit because that graph is connected. This is
an associative-algebra statement, not a classification of a control Lie
algebra or a statement about all full-space gauge sectors.

## 4. Geometric exchange and finite-angle update choices

Reflection `x -> 2-x` sends `A ↔ C`, `D ↔ F`, and fixes `B,E`.
On the stored links it permutes
`AB ↔ BC`, `DE ↔ EF`, `AD ↔ CF`, and fixes `BE`.
The four horizontal links reverse orientation, so the register reflection
also applies `C=diag(1,-1,-1,-1,1)` on those four factors. This defines an
exact unitary involution `R` on the entire seven-link space. It exchanges
the two square magnetic operators and fixes the outer one. It also maps
each Gauss generator to the reflected vertex's generator. On the physical
basis it fixes `Omega_0,O` and swaps `L,R`; the runner checks this directly
on every sparse amplitude, including the orientation signs.

Write `A=B_L`, `B=B_R`, `C_AB=[A,B]`, and `H=A+B`. All angles below are
real and dimensionless supplied parameters. Each of the following unitary
products preserves gauge invariance because each individual magnetic
operator does. Their square-exchange behavior differs.

**Chronological left-then-right product.** Define
`T_LR(theta)=exp(-i theta B) exp(-i theta A)`. Its reflected operator is
`T_RL(theta)=exp(-i theta A) exp(-i theta B)`. Exact Taylor expansion gives

```
T_LR - T_RL = theta^2 [A,B] + O(theta^3).
<R|(T_LR-T_RL)|L> = sin(theta)^2-sin(2 theta)^2
                  = -3 theta^2+5 theta^4+O(theta^6).
```

The exact sine expression follows by exponentiating the `2` and `1`
coupled two-state blocks displayed above. The empty-flux reference detects
the defect only one order later:

```
(T_LR-T_RL)|Omega_0>
  = -i sin(2 theta)[cos(theta)-cos(2 theta)] (|L>-|R>)
  = -3i theta^3 (|L>-|R>) + O(theta^5).
```

Thus the ordered rule is not exchange invariant for all angles; the local
analytic witness already excludes sufficiently small generic nonzero
angles. Special angles with coinciding products are not excluded.

**Palindromic (Strang) product.** The commonly called symmetric product

```
S_L(theta)=exp(-i theta A/2) exp(-i theta B) exp(-i theta A/2)
```

is symmetric under reversing the time ordering; this does not make it
square-exchange invariant. Its reflected operator is the analogous `S_R`
with `A,B` exchanged. Multiplying the exact power series gives

```
S_L-S_R = -(i theta^3/8)[A+B,[A,B]] + O(theta^4),
<L|(S_L-S_R)|Omega_0> = (3i/4)theta^3
                            -(73i/64)theta^5 + O(theta^7).
```

The runner calculates the full cubic matrix and checks the nested
commutator identity; the displayed entry supplies a nonzero exact witness.
This excludes only this product's purported exact exchange symmetry, not
all symmetric circuits or all finite-register dynamics.

If instead “symmetric” means the arithmetic mean
`M=(T_LR+T_RL)/2`, exchange invariance holds, but generic unitarity fails:
the exact identity
`M^dagger M=I-(T_LR-T_RL)^dagger(T_LR-T_RL)/4`
shows that the mean is unitary precisely when the two products coincide.

**Joint exponential.** The declared update
`J(theta)=exp[-i theta(A+B)]` obeys `R J R=J` exactly, because
`R(A+B)R=A+B`. It is also exactly gauge invariant on the full register
space. On the physical sector,

```
H^3=10H,
J(theta)=I-i sin(sqrt(10)theta) H/sqrt(10)
           +[cos(sqrt(10)theta)-1] H^2/10.
```

This polynomial formula follows by separating the powers in the exponential
series using `H^3=10H`; it is valid at every finite real angle. The nonzero
eigenvalues are `+/-sqrt(10)`, with a two-dimensional kernel. Exact
exchange symmetry is therefore available in this supplied finite model.

**Electric composition.** Put `E_tot=sum_links E_link^2` and
`E(tau)=exp(-i tau E_tot)=product_links exp(-i tau E_link^2)`.
Each link Casimir commutes with both endpoint actions. Reflection only
permutes links or applies `C`, which preserves occupied versus empty
states. Thus `E(tau)` is gauge invariant and exchange invariant for every
real `tau`. Its physical matrix is

```
E_tot=diag(0,3,3,9/2).
```

Both counts and exchange commutation are checked exactly by the runner.
Consequently the declared finite-step product
`J(theta) E(tau)` has both symmetries at arbitrary finite angles. This is
not a derivation of a selected update law, a unique physical Hamiltonian
from its logarithm, or a full-lattice construction.

## 5. What the qubit encodings establish

One five-state link embeds isometrically into three logical qubits, for
example by sending `|mu>` to binary `|mu>` for `mu=0,...,4`. A full seven-link
register therefore has a code in 21 qubits. For a Hermitian patch operator
`K`, define its encoded operator as `V K V^dagger` on the code and zero on
the orthogonal complement. Its exponential acts as the intended update
on the code and the identity on its complement. This proves finite-register
unitary realizability and exact code preservation for these ideal encoded
operators. Three is minimal for a single link because `2^2<5<=2^3`.

The supplied physical sector admits a smaller abstract encoding in two
logical qubits. Identify

```
|Omega_0> = |00>, |L> = |10>, |R> = |01>, |O> = |11>.
B_L = X_L(3I+Z_R)/2,
B_R = (3I+Z_L)X_R/2.
```

The runner verifies these Pauli formulas exactly. This two-qubit encoding
represents the four-dimensional invariant sector and its restricted
operators; it does not encode the full kinematical link space or preserve
the link-local tensor-factor interpretation. Its loop bits describe
extended gauge-invariant patterns in the original seven links.

Neither encoding provides a homogeneous assignment of the framework's
physical site qubits, a translation-compatible way to share overlapping
link codes throughout a cubic lattice, or a prescribed nearest-neighbor
gate schedule with the framework's allowed operations and auxiliaries.
No compatibility with Admissibility or permanent Record dynamics is proved
here. The joint finite-patch exponential is well-defined without resolving
those native implementation questions. The local model and its four-state
boundary sector remain supplied construction data.

## 6. Reproduction and evidence limits

Assigned source: `scripts/gb1_cf_two_plaquette_s1_2026_11_07.py`.
Full execution record:
`logs/runner-cache/gb1_cf_two_plaquette_s1_2026_11_07.txt`.
The log identifies the script, spec and goal hashes, base commit, arithmetic,
thread settings, exact matrices, sparse witness, resource use, and lease
release. The script uses only the Python standard library. Before rerunning,
run `lab_ops.py preflight --numeric`, acquire a unique numeric lease, set
`OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1`,
execute the runner, and release the lease on exit. Do not run if preflight
refuses. The host reports shell memory caps unavailable; the runner uses a
240 MB RSS watcher and an 80-second alarm instead, and the completed job
used under 28 MB. No floating-point calculation is used for scientific
coefficients; only resource timing uses floating point.

The sparse contractions, quaternion/2x2 color comparison, occupation
enumeration, and exact Taylor arithmetic are self-checks within this author
lineage. A separate checker must still assess the endpoint convention,
sector count, normalization and update conclusions before substantial
reuse. No independent review, audit verdict, retained promotion, continuum
limit, mass gap, state-selection principle, or four-axiom derivation is
claimed. Only the three assigned deliverables were authored; no editable
prompt, axiom, authority, or platform-instruction file was changed.
