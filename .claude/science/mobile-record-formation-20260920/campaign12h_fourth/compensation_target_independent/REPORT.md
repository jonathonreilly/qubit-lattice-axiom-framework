# Bounded block compensation in the fourth-order formation target

Independent reconstruction before author-source access, 2026-09-23.

**Result.** The fixed-graph compact-time trace-norm approximation survives the
bounded addition `epsilon^2 C`, provided C commutes with W and its norm is
uniformly bounded in the proposed spin family. In the canonical positive-
overlap coordinates the effective coefficients are

\[
\begin{aligned}
 K_2&=C_0-M,\\
 K_4&=M^2-\tfrac12 Z^\dagger Z
       +A^\dagger C_1A-\tfrac12\{M,C_0\},                \tag{1}\\
 B_j&=-Pj\Pi_1TP,
\end{aligned}
\]

where `C_r=Pi_r C Pi_r`, `A=Pi1 T P`, `M=A†A`, and
`Z=Pi2 T Pi1 A`. The braces denote an anticommutator. In particular the
fourth-order correction contains both the excited-block C1 term and the
canonical normalization term. Commutativity of C0 with M is **not** assumed.
Formation operators at leading order are unchanged.

For fixed positive delta and kappa, the effective generator is

\[
 \mathcal L_{P,\epsilon}(X)
 =-i\delta[\epsilon^{-2}K_2+K_4,X]
       +\kappa\sum_j\mathcal D[B_j](X).                  \tag{2}
\]

For every fixed finite T0 there are epsilon0 and c(T0), depending only on the
fixed grade range and uniform operator bounds specified below, such that

\[
 \sup_{0\le t\le T_0}
 \left\|e^{t\mathcal L_\epsilon}(\rho)
    -\iota\,e^{t\mathcal L_{P,\epsilon}}(\rho)\right\|_1
 \le c(T_0)\epsilon                                      \tag{3}
\]

for every density supported in P and `0<epsilon<epsilon0`. Here iota is the
ordinary P-space embedding, and

\[
 \mathcal L_\epsilon(X)
 =-i[\delta\epsilon^{-4}(W+\epsilon T+\epsilon^2 C),X]
      +\kappa\epsilon^{-2}\sum_j\mathcal D[j](X).
\]

The error is uniform over initial densities and over S when the hypotheses
hold uniformly in S. It also holds directly on the unit-rotor trace class
for bounded C. This does not assert an epsilon-independent limit of (2), a
specific local microscopic compensation, or a joint large-S field limit.

## 1. Exact assumptions and source boundary

The abstract Hilbert space may be infinite dimensional. W is bounded,
self-adjoint, with spectrum in a fixed finite set `{0,...,m}` and nonzero
`P=Pi0`. T and C are bounded self-adjoint operators satisfying

\[
 \Pi_rT\Pi_s=0\quad\text{unless }|r-s|=1,
 \qquad [W,C]=0.                                        \tag{4}
\]

Each supplied bounded formation channel satisfies

\[
 [W,j]=-j,\qquad jP=0,                                  \tag{5}
\]

and the channel family is finite, with a uniform bound on
`sum_j ||j||^2`. A finite or uniformly bounded channel count is sufficient;
the constants below depend on the summed norm bound. The parameters delta
and kappa are fixed, not scaled to zero or infinity in this argument.
C is fixed as the perturbation parameter is varied. All physical constraints
are implemented by working on a common invariant physical Hilbert space.

For the record interpretation also require `[N,W]=[N,T]=[N,C]=0` and
`[N,j]=2j`. These ensure number conservation for (1)'s Hamiltonian and number
increase by two for B_j. They are not needed for the abstract trace-norm
estimate. No commutation of C with j, no rank condition on A, no damping gap,
and no irreducibility assumption are imposed.

The sole read scientific source is the already reviewed parent
`campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md`,
SHA-256
`002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`.
It was reread completely for this task. The operator conventions and the
parent proof strategy are reused, with every changed step derived below.
No other author note, runner, result, plan, checkpoint, registry, Git or
publication surface was accessed. In particular the local-compensation,
local-counterterm and cube-unprepared packets remain unopened. No author
builder is imported by the new controls. No external theorem is needed for
the proof given here.

## 2. Full-cluster canonical rotation and parity

Put `h(e)=W+eT+e^2 C`. Choose fixed disjoint circles of radius less than one
half around the occupied integer grades. If
`|e| ||T||+|e|^2 ||C||` is sufficiently small, resolvent Neumann series define
spectral projections Q_r(e), with

\[
 Q_r(e)=\Pi_r+O(e),
\]

analytically in operator norm, uniformly under the stated norm and grade
bounds. This construction uses separation of the entire W clusters, not
separation of individual eigenvalues within them. Infinite-dimensional
cluster subspaces therefore cause no problem.

For real small e let

\[
 S(e)=\sum_r Q_r(e)\Pi_r,
 \quad U(e)=S(e)[S(e)^\dagger S(e)]^{-1/2}.                \tag{6}
\]

The latter inverse square root exists by its norm-convergent series near
identity. The operator `S†S` is grade-block diagonal, with positive block
`Pi_r Q_r Pi_r`. Orthogonal complete cluster ranges imply U is unitary and
maps every Pi_r to Q_r. Its overlap in each original grade is positive.
Thus `U†hU` commutes with W exactly and `U=I+O(e)`.

Let `Xi=(-1)^W`. Equations (4) imply

\[
 h(-e)=\Xi h(e)\Xi,
 \quad U(-e)=\Xi U(e)\Xi.
\]

Since the rotated h is grade-block diagonal and Xi is scalar within each
grade, the entire rotated Hamiltonian is an even analytic function of e.
In particular

\[
 U^\dagger hU=W+O(e^2),\qquad
 \widetilde H_\epsilon
 =\delta\epsilon^{-4}W+O(\epsilon^{-2}).                 \tag{7}
\]

Rotating only P against its complement would not supply the needed global
bound (7): order-e hopping can remain between nonzero W grades. The full-
cluster rotation is therefore load-bearing in the dissipative estimate.
The parity statement continues to hold for arbitrary C0 and C1 obeying
(4), including the noncommuting case tested below.

## 3. Independent fourth-order calculation in positive-overlap coordinates

Write `Q=I-P`, `R=(W|_Q)^-1`, `T_Q=QTQ`, and `C_Q=QCQ`. The low spectral
subspace is the graph of an analytic map `X(e):P H -> Q H`, with X(0)=0.
Its exact invariance equation is

\[
 eA+(W_Q+eT_Q+e^2 C_Q)X
       =X(e^2 C_0)+eXA^\dagger X.                        \tag{8}
\]

Here A is naturally embedded in Q and lies wholly in grade one. Set
`X=eX1+e^2 X2+e^3 X3+...`. Successive orders give

\[
\begin{aligned}
 X_1&=-A,\\
 X_2&=\tfrac12 Z,\\
 X_3&=-R(T_QX_2+C_QX_1-X_1C_0-X_1A^\dagger X_1).
\end{aligned}                                           \tag{9}
\]

Since C_Q preserves grades and `A†Pi1 T Pi2 Z=Z†Z`, these imply

\[
 A^\dagger X_2=0,\qquad
 A^\dagger X_3=M^2-\tfrac12 Z^\dagger Z
                  +A^\dagger C_1A-MC_0.                 \tag{10}
\]

Only C1 can enter this order from the excited grades. A C2 term acts too
late in the graph expansion; W>=3 contributions in X3 are killed by A†.

The graph-coordinate effective operator is

\[
 G(e)=e^2 C_0+eA^\dagger X(e).
\]

It uses a nonorthonormal coordinate system and need not be Hermitian in the
ordinary P inner product. The canonical isometry is

\[
 V(e)=(P+X(e))(I+X(e)^\dagger X(e))^{-1/2}=U(e)P.
\]

Writing `D=I+X†X=I+e^2 M+O(e^3)`, the physical canonical block is
`D^(1/2) G D^(-1/2)`. Its fourth coefficient is consequently

\[
 A^\dagger X_3+\tfrac12[M,C_0-M]
 =M^2-\tfrac12Z^\dagger Z+A^\dagger C_1A
                       -\tfrac12(MC_0+C_0M),            \tag{11}
\]

which proves (1). The possible odd remainder is absent by Section 2, so

\[
 P U^\dagger h(e) U P=e^2K_2+e^4K_4+O(e^6).              \tag{12}
\]

After multiplying by `delta epsilon^-4`, the Hamiltonian truncation error
is O(epsilon^2), not order one. Useful dimension-free coefficient bounds are

\[
 \|K_2\|\le\|C\|+\|T\|^2,\qquad
 \|K_4\|\le\tfrac32\|T\|^4+2\|T\|^2\|C\|.             \tag{13}
\]

Two immediate checks are informative. If `C=cI` on the full Hilbert space,
the two new fourth-order terms cancel, as they must for a scalar shift of h.
If C is supported only on grades at least two, it does not change K2 or K4.
Neither statement licenses dropping C1 for general C. Also, the raw graph
coefficient in (10) cannot replace the canonical coefficient when C0 and M
do not commute.

## 4. Leading formation operators and discrepancy bounds

The first rotation derivative is unchanged: `U'(0)P=-A`. Since jP=0,

\[
 \widetilde j P:=U^\dagger jUP
       =\epsilon B_j+O(\epsilon^2),\qquad
 B_j=-PjA=PB_jP.                                       \tag{14}
\]

In particular `Q j_tilde P=O(epsilon^2)`. There is no assumption that C and j
commute. In fact parity gives

\[
 \widetilde j(-e)=-\Xi\widetilde j(e)\Xi,
 \qquad P\widetilde jP=eB_j+O(e^3),                     \tag{15}
\]

because (5) makes j odd under Xi. Thus the leading recycling and loss inside
P are exactly those of the **supplied** channel family B_j. Resolved and
coherent channels remain their respective supplied instruments; they are
not silently equated.

Let `G_epsilon` be the full generator in the rotated picture, let E0 be the
ordinary P embedding, and write

\[
 \mathcal R_\epsilon
   =\mathcal G_\epsilon E_0-E_0\mathcal L_{P,\epsilon}.
\]

For full trace-class matrices set
`Off Y=QYP+PYQ` and `Diag Y=PYP+QYQ`. The following are induced trace-norm
bounds (on Hermitian inputs suffices):

\[
 \|\operatorname{Off}\mathcal R_\epsilon\|
          =O(\epsilon^{-1}),\qquad
 \|\operatorname{Diag}\mathcal R_\epsilon\|
          =O(\epsilon^2).                              \tag{16}
\]

The weaker second estimate O(epsilon), used in the parent argument, would
also suffice. For completeness, the stronger estimate here follows directly
from (12), (14), and (15):

- The rotated Hamiltonian has no off-grade source; its P-block error is
  O(epsilon^2).
- PP recycling has `epsilon^2 B_j X B_j†+O(epsilon^4)` before its
  `kappa epsilon^-2` prefactor. QQ recycling is O(epsilon^4).
- The PP loss is `epsilon^2 B_j†B_j+O(epsilon^4)`, because the PP part of
  `j_tilde P` is odd and its Q part is O(epsilon^2).
- In contrast, `Q j_tilde† j_tilde P=O(epsilon)`, so the off-block loss source
  can be O(epsilon^-1). It cannot be discarded by direct generator norm
  comparison. Off-block recycling is only O(epsilon).

All estimates use `||AXB||_1 <= ||A|| ||B|| ||X||_1`; constants do not count
Hilbert-space dimension. Moreover
`sum ||B_j||^2 <= ||T||^2 sum ||j||^2`.

## 5. Off-block corrector and complete density-error argument

Define `A0(Y)=-i delta[W,Y]`. On P-Q off-block matrices its bounded inverse is

\[
 A_0^{-1}Y=\frac{i}{\delta}R QYP
                 -\frac{i}{\delta}PYQ R.                \tag{17}
\]

The gap from zero to the nonzero W spectrum is at least one. Thus the inverse
bound is independent of dimension and S. Form the correction map

\[
 F_\epsilon=-\epsilon^4 A_0^{-1}
                  \operatorname{Off}\mathcal R_\epsilon,
 \qquad E_\epsilon=E_0+F_\epsilon.                       \tag{18}
\]

It preserves Hermiticity and has norm O(epsilon^3). It is a proof device,
not a positive preparation or physical channel. The exact residual identity
is

\[
\begin{split}
 \mathcal G_\epsilon E_\epsilon
       -E_\epsilon\mathcal L_{P,\epsilon}
 ={}&\operatorname{Diag}\mathcal R_\epsilon\\
   &+(\mathcal G_\epsilon-\epsilon^{-4}A_0)F_\epsilon
      -F_\epsilon\mathcal L_{P,\epsilon}.                \tag{19}
\end{split}
\]

By the full-cluster bound (7) and bounded jumps,

\[
 \|\mathcal G_\epsilon-\epsilon^{-4}A_0\|
      =O(\epsilon^{-2}),\qquad
 \|\mathcal L_{P,\epsilon}\|=O(\epsilon^{-2}).            \tag{20}
\]

Equations (16)--(20) prove that the corrected residual is O(epsilon).
This remains true when K2 and K4 do not commute, or when K2 happens to vanish.
No rapid-mixing, spectral-gap, or time averaging assumption for the P
Hamiltonian is used.

For each fixed epsilon the two Lindblad generators have bounded coefficients.
Their CPTP semigroups exist on trace class, including the infinite-dimensional
bounded-rotor case, by the norm-convergent no-jump/jump expansion. Such
semigroups contract trace norm on Hermitian inputs. Duhamel therefore gives,
for every P density rho,

\[
 \|e^{t\mathcal G_\epsilon}E_0\rho
          -E_0e^{t\mathcal L_{P,\epsilon}}\rho\|_1
 \le 2\|F_\epsilon\|+t\,
   \|\mathcal G_\epsilon E_\epsilon
          -E_\epsilon\mathcal L_{P,\epsilon}\|.          \tag{21}
\]

Positivity of E_epsilon is not needed: the intermediate residual is
Hermitian and the physical semigroups provide the contraction. The input
and output rotation defects for the undressed physical density each obey
`||U rho U†-rho||_1 <= 2||U-I||`. Hence the original-picture error is at most

\[
 4\|U-I\|+2\|F_\epsilon\|+T_0 O(\epsilon)=O(\epsilon),
\]

which is (3). This covers arbitrary initial P coherences, including
coherences between record-number sectors when those exist. No number-offset
reinterpretation of the Hamiltonian is made here.

All constants depend only on the fixed number and separation of W grades,
bounds for T,C and the summed jump norms, delta, kappa and T0. Uniform bounds
in S therefore prove the stated S-uniform estimate. The same proof works
directly for bounded operators on the unit-rotor Hilbert space. No electric
moment assumption enters this lemma.

## 6. New exact and finite-generator controls

`finite_blocks.py` constructs a new nine-dimensional graded model. Its
W grades have dimensions `(5,3,1)` and it has record numbers 0,2,4. T,C and
two formation channels satisfy every selection rule above, including
`[N,T]=[N,C]=0` and `[N,j]=2j`. There are two successive formation stages,
so the full density control includes recycling and does not assume that
formation terminates after a first event. These are abstract finite-block
controls, not a new spatial model or proposed physical compensation.

In its first number sector the relevant matrices are

```
A  = [[1,1],[0,2]],       C0 = [[1,2],[2,-1]],
C1 = [[3,1],[1,-2]],      Z  = [[1,-1]],
M  = [[1,1],[1,5]],
K2 = [[0,1],[1,-6]],
K4 = [[3/2,11/2],[11/2,55/2]].                           (22)
```

The full model also has nontrivial C and T on its next number sector and a
nonzero W=2 block of C. `block_expansion_check.py` verifies (8)--(11)
exactly over rational matrices. On the full P space, the squared Frobenius
norm of `[M,C0]` is 202. The raw graph fourth coefficient has an
anti-Hermitian part with the same squared norm, demonstrating why canonical
normalization cannot be skipped.

Full-cluster spectral rotations were separately computed at
epsilon = 1/8,1/16,1/32,1/64. The dimensionless low-block remainder divided
by epsilon^6 was approximately

```
284.447, 329.931, 343.953, 347.668.
```

The extracted fourth-coefficient error decreased from about 4.444 to 0.0849.
The deliberately incorrect raw-graph coefficient and the formula omitting
C1 retain nonzero errors (about 5.045 and 6.345 at the last epsilon).
A scalar C produced only its exact second-order scalar shift. A C supported
only on W=2 changed the low block first at order epsilon^6, as required.
These countercontrols are preserved as result fields; no assertion failure
was concealed or reclassified.

`density_residual_check.py` constructs the full nine-state Lindblad generator
and the five-state P target without importing a previous or author generator.
At delta=0.7 and kappa=0.4 it checks both a pure fixed-number input and a pure
P input coherent across all three number sectors. Over four epsilon values
and four times through 0.35, the largest observed full trace-norm error divided
by epsilon was about 3.5472. This is a finite floating control, not a numerical
proof of the uniform bound.

The same script checks the actual off-block residual and correction. As
epsilon decreases from 1/8 to 1/64, the Hilbert--Schmidt induced norm of the
uncorrected off-block discrepancy grows from about 20.43 to 184.32. The
corrected residual divided by epsilon remains between about 27.86 and 31.89.
The exact algebraic cancellation in (19) is reproduced to floating precision.
The corrector is Hermiticity preserving but its corrected density has a
negative eigenvalue in this control, confirming that it must not be
interpreted as a CP embedding.

The numerical residual norms are Hilbert--Schmidt induced norms in this
fixed finite model. They are explicitly distinct from the dimension-free
trace-class norm estimates used in the proof. Maximum observed trace
normalization error in the stiff full propagation was about `1.58e-10`;
this is retained rather than rounded away. All runs completed at their
original thresholds, with empty stderr. There are no failed execution
attempts in this packet.

## 7. Scope, reproducibility, and open boundaries

Equation (3) is a fixed-graph, fixed-compact-time statement for the supplied
bounded perturbation family. It does not prove any of the following:

- a volume-uniform estimate, a growing observation-time estimate, or an
  epsilon-independent target when K2 is nonconstant;
- applicability to unbounded C, or S-uniform bounds when `||C_S||` grows
  with S (for example an unscaled electric-square operator);
- a joint spin/epsilon limit of the fast target merely from strong
  convergence of its coefficients: the `epsilon^-2 K2` term can amplify
  coefficient errors;
- locality, native selection, a microscopic implementation of any specific
  C, an energy source, or a persistent field/particle phase.

The parent selection rules are essential inputs; merely separating P from
Q without controlling all W clusters does not justify (20). A different
block-coordinate gauge may express its fourth coefficient differently;
(1) is specifically the positive-overlap canonical block. The theorem
requires no claim about an inaccessible author compensation construction.

From the evidence directory, the checks can be reproduced as

```
python3 block_expansion_check.py
python3 density_residual_check.py
```

`run_logged.py` produced the preserved full stdout, stderr and actual command
receipts, with source and builder hashes, start/end times and exit codes.
`BLOCK_RESULTS.json` and `DENSITY_RESULTS.json` are byte-identical to their
respective complete stdout. `PRE_COMPARISON_SEAL.json` binds the sole read
model source and all new proof/control evidence. No primary source, earlier
sealed packet, Git state or audit status was changed.

The reconstruction is complete for the bounded perturbation lemma and ready
for a separately authorized exact-source comparison.
