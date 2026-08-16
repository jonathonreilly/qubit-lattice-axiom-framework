---
claim_id: admissibility_dirac_kahler_torus_wrap_defect_bounded_theorem_note_2026-08-16
claim_type: bounded_theorem
claim_scope: "On the primary carrier at both rational shear fixtures, the Block 119 swap family leaves the literal antiperiodic torus pairing non-Hermitian with residual rank four per momentum, and the torus kernel splits exactly as the half-space kernel plus the displayed antiperiodic wrap defect which carries all of the dressed non-Hermiticity; the completed half-space window pencil vanishes identically so the torus pencil value at one is exactly the wrap contribution; the wrap obeys the exact projector law with geometrically decaying stable-channel coefficient while its rank-one unstable-projector channel saturates at an N-independent limit; and subtracting the displayed defect restores the Hermitian positive semidefinite completion with the contractive quotient in the same geometric semigroup — while the torus completion without subtraction, the naturality classification, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_reflection_intertwiner_completion_bounded_theorem_note_2026-08-16
runner: scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_reflection_intertwiner_completion_bounded_theorem_note_2026-08-16
target_blocker_text: "Carry the completed half-space OS package back to the antiperiodic torus and the curved carrier, classify the completion's naturality, and then form the gravity constraint quotient."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Classify the completion's naturality, execute the curved-carrier OS positivity question on the half-space package, and then form the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-119 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact torus/half-space kernel split, exact rank-four dressed anti-Hermitian residuals, exact zero half-space pencil and wrap-only torus pencil identity, exact stable/unstable projector law and finite-size limit, and exact defect-subtracted Hermitian positive-semidefinite inertia and contractive quotient certificates at every momentum and both rational shear fixtures; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Torus Wrap Defect And The Half-Space Carrier

**Date:** 2026-08-16

**Campaign block:** 120

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py`](../scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py)

## 1. Result Up Front

[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:16`
and elaborated at
`docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:1013-1029`:

> Carry the completed half-space OS package back to the antiperiodic torus
> and the curved carrier, classify the completion's naturality, and then
> form the gravity constraint quotient.

**Failure-and-split theorem.** On the primary `Z8_t x Z4_x` carrier, at
each of the rational shear fixtures $c=5/13$ and $c=3/5$, the Block 119
swap family does not complete the literal antiperiodic torus pairing. For
every momentum $k=0,1,2,3$, its completed torus kernel $K_{T,k}$ obeys

\[
 \operatorname{rank}(K_{T,k}-K_{T,k}^{\dagger})=4.    \tag{1}
\]

The kernel is non-Hermitian, so a Hermitian inertia is undefined. This is
not a negative-inertia statement. The exact keystone identity is instead

\[
 K_{T,k}=K_{H,k}+D_k,                                 \tag{2}
\]

where $K_{H,k}$ is the Block 119 completed half-space kernel and $D_k$
is the dressed antiperiodic wrap defect. Since $K_{H,k}$ is Hermitian,

\[
 K_{T,k}-K_{T,k}^{\dagger}=D_k-D_k^{\dagger}.         \tag{3}
\]

Thus all of the dressed torus non-Hermiticity lies in the displayed
defect, not in the half-space package.

**The wrap operator.** With the runner's propagator notation, the
antiperiodic wrap contribution is induced exactly by

\[
 R_{\rm AP}[n,j]
 =-{U[n,0](I+M^2)^{-1}U[4,j+1]e\over C_j}.           \tag{4}
\]

Equivalently, before dressing,

\[
 G_T=-B_{-1}+[(G_{\rm open}+B_{-1})+G_{\rm AP}],     \tag{5}
\]

where $G_{\rm AP}$ is induced by (4). Equation (2) is the corresponding
completed-kernel split.

**The vacuum is exactly at one in the strongest sense.** If $P_H(z)$
and $P_D(z)$ are the completed half-space and defect window pencils,
then

\[
 P_T=P_H+P_D,
 \qquad f_H(z):=\det P_H(z)\equiv0.                  \tag{6}
\]

The half-space determinant is the zero polynomial, not merely a
polynomial which happens to vanish at $z=1$. Defining

\[
 W_f(z):=\det(P_H(z)+P_D(z))-\det P_H(z),            \tag{7}
\]

the torus value is therefore exactly

\[
 f_T(1)=f_H(1)+W_f(1)=0+W_f(1)\ne0.                 \tag{8}
\]

Both the mixed and pure-defect contributions to $W_f(1)$ are nonzero at
every declared sector. The torus pencil value at one is entirely the wrap
contribution.

**Finite-size projector law.** Put $T=M^2$ and $a=\rho_F^2\in(0,1)$.
For the stable and unstable spectral projectors $P_s,P_u$,

\[
 T=aP_s+a^{-1}P_u,
 \qquad
 (I+T^N)^{-1}
 ={P_s\over1+a^N}+{P_u\over1+a^{-N}}.                \tag{9}
\]

With

\[
 c_N={a^N\over1+a^N},                                \tag{10}
\]

the two exact balanced identities are

\[
\begin{aligned}
 (I+T^N)^{-1}-P_s&=c_N(P_u-P_s),\\
 (I+T^N)^{-1}T^N-P_u&=c_N(P_s-P_u).
                                                               \tag{11}
\end{aligned}
\]

Consequently the stable coefficient in the bridge operator is $c_N$,
which decays geometrically, while its rank-one unstable-projector
coefficient is $1-c_N$ and saturates at the $N$-independent limit
$P_u$. Explicitly,

\[
 c_1={a\over1+a},\qquad
 c_2={a^2\over1+a^2},\qquad
 c_3={a^3\over1+a^3}.                                \tag{12}
\]

The correction is balanced between $P_s$ and $P_u$, not an
unstable-only error. What saturates is the unstable channel of the wrap
bridge. The fixed `Z8` chart also contains a non-boundary open/direct
bridge.

**Unstable saturation.** The half-space removes the wrap by fiat: it
sets the winding contribution (D) to zero by choosing the one-sided
carrier. It does not obtain that removal by proving that the literal
fixed-torus kernel converges to it. On any fixed torus the antiperiodic
boundary speaks through the growing mode. Equation (11) makes that
statement exact: the unstable part of the bridge tends to $P_u$, not
to zero.

**Corrected completion and power reconciliation.** Exact subtraction of
the displayed defect gives

\[
 K_{T,k}-D_k=K_{H,k}=y_{+,k}y_{+,k}^{\dagger},
 \qquad
 \operatorname{In}K_{H,k}=(1,0,3).                  \tag{13}
\]

The radical quotient is contractive with

\[
 \beta_k=a_k^2=\rho_{F,k}^4\in(0,1).                \tag{14}
\]

Here $a=\rho_F^2$ is the double-period eigenvalue used by the torus
finite-size calculation. Thus $a^2=\rho_F^4$ per double period is the
same geometric semigroup as Block 119's per-period $\rho_F^2$. The
difference is bookkeeping of the period unit, not a power error.

The conclusion is deliberately narrow. The literal torus completion
without subtracting (D), the completion's naturality classification,
curved OS positivity, the completed ADM/history transporter, joint
gravity, the gravity constraint quotient, Records, audit retention,
axiom amendment, obligation retirement, and TOE percentage movement
remain outside this theorem.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The authority snapshot is
unchanged from Blocks 115--119.

The exact stacked parent is
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
commit `33fd2d21558604718f3a88713fe1976aff8f9dbb`, content-bound through
note blob `ed660c106e8e97f6ce85deef95228170e483e8e5`. No audit verdict is
imported.

The executed contract is:

1. the inherited Blocks 107--119 `d=2` one-fine-mode primary carrier on
   `Z8_t x Z4_x`, its link-centered reflection, Block 118's stable split,
   and Block 119's swap-completed half-space pairing;
2. both rational shear fixtures $c=5/13$ and $c=3/5$, and all four
   fixed momenta $k=0,1,2,3$;
3. the literal antiperiodic torus kernel after applying the Block 119 swap
   family, its Hermiticity test, and the rank of its anti-Hermitian
   residual, with no inertia assigned to a non-Hermitian matrix;
4. the exact torus/half-space split $K_T=K_H+D$, formula (4) for the
   antiperiodic wrap, and the identity locating all dressed
   non-Hermiticity in (D);
5. the completed half-space and defect pencils, the zero-polynomial
   identity for $f_H$, the wrap-only value $f_T(1)=W_f(1)\ne0$, and
   nonzero mixed and pure-defect contributions;
6. the stable/unstable projector decomposition for every positive torus
   length $N$, including the exact $N=1,2,3$ coefficients and the
   rank-one unstable saturation;
7. the exact subtraction $K_T-D=K_H=y_+y_+^\dagger$, Hermiticity,
   positive semidefiniteness, and inertia ((1,0,3)) per momentum;
8. the quotient contraction $\beta=a^2\in(0,1)$, its geometric powers,
   and the reconciliation with Block 119's period convention; and
9. the no-go conclusion only for the displayed carrier, fixtures, Block
   119 swap family, and displayed subtraction, while leaving every other
   torus dressing family, naturality, curved OS, and gravity open.

The supplied exact certificate report ends with
`TOTAL: PASS=792 FAIL=0`; its reported runtime is `178.043` seconds. The
torus failure is represented by exact residual-rank and field-root
certificates, and the positive result by exact split, projector,
factorization, inertia, bound, and quotient identities.

Its decision footer is reproduced with the supplied final-run timing:

```text
TASK4 VERDICT (b): Theta does not complete the literal Z8 torus; Theta plus exact subtraction of D completes it to the half-space carrier. No non-completability theorem for every torus-adapted dressing is claimed.
DECISION: the swap family fails on the finite torus by a full-rank non-Hermitian wrap defect; removing that exact defect recovers the rank-one PSD half-space package and its beta=a^2 contraction.
RUNTIME_SECONDS: 178.043
TOTAL: PASS=792 FAIL=0
```

The exact scope is the primary finite carrier, both rational shear
fixtures, all four fixed momenta, the Block 119 swap family on the literal
antiperiodic torus, the displayed wrap defect, its exact subtraction, and
the half-space correction. Torus completion without that subtraction,
other torus-adapted dressing families, the naturality classification,
curved OS positivity, the completed ADM/history transporter, joint
gravity, the gravity constraint quotient, Records, audit retention,
axiom amendment, obligation retirement, and TOE percentage movement are
outside the executed contract.

## 3. The Torus Failure

Fix one fixture and one momentum, and suppress (k,c) temporarily. The
literal torus test takes the Block 119 swap (Theta) without changing its
displayed dressing family and applies it to the antiperiodic torus
pairing. Let $K_T$ denote the resulting four-by-four completed window
kernel. The exact Hermiticity test fails:

\[
 K_T\ne K_T^\dagger.                                 \tag{15}
\]

More sharply, the anti-Hermitian residual fills the whole displayed
window:

\[
 \operatorname{rank}(K_T-K_T^\dagger)=4.             \tag{16}
\]

Equation (16) holds at each of the four fixed momenta and at both rational
fixtures. It is a residual-rank statement, not an eigenvalue-inertia
statement. Inertia $(n_+,n_-,n_0)$ is defined here only for a Hermitian
matrix, so the torus inertia is **undefined**. Assigning a negative count
to $K_T$ would conceal the stronger preliminary failure that its
eigenvalues need not be ordered on the real line.

The exact certificate rows are:

```text
TASK1 CERT c=5/13: Hermitian=(False, False, False, False), rank(K-K*)=(4, 4, 4, 4), inertia=undefined; f_k#=('25812f18b460', '91cdf457a0bc', '4ecb214fb0e9', 'e8148f572f43'), f_k(1)!=0; roots=('real roots (-inf,0)/(0,1)/(1,inf)/nonreal=2/0/1/0', 'three nonreal roots (no order relative to 1)', 'real roots (-inf,0)/(0,1)/(1,inf)/nonreal=0/0/1/2', 'three nonreal roots (no order relative to 1)').
TASK1 CERT c=3/5: Hermitian=(False, False, False, False), rank(K-K*)=(4, 4, 4, 4), inertia=undefined; f_k#=('35c1a866e063', '0b1bdfe8518d', 'b684028bf6ac', 'faa835df4331'), f_k(1)!=0; roots=('real roots (-inf,0)/(0,1)/(1,inf)/nonreal=1/1/1/0', 'three nonreal roots (no order relative to 1)', 'real roots (-inf,0)/(0,1)/(1,inf)/nonreal=1/0/0/2', 'three nonreal roots (no order relative to 1)').
```

The root classifications use exact Sturm and field-gcd tests. Their role
is diagnostic: they certify that the torus pencil is not secretly the
positive half-space pencil. The rank-four anti-Hermitian residual already
decides the literal completion question for the displayed swap family.

This failure does not contradict Block 119. That theorem completed the
stable-split half-space pairing. It explicitly left transport across the
antiperiodic seam unexecuted. The torus adds precisely that winding datum.
Nor does (16) prove that no other torus-adapted dressing could work. It
tests the Block 119 swap family on the literal torus pairing and nothing
larger.

## 4. The Keystone Split

The torus failure is not left as an opaque residual. The exact propagator
identity separates the open/direct and antiperiodic terms. In the runner's
notation,

\[
 G_T=-B_{-1}+W,
 \qquad
 W=(G_{\rm open}+B_{-1})+G_{\rm AP}.                 \tag{17}
\]

The antiperiodic term $G_{\rm AP}$ is induced by

\[
 R_{\rm AP}[n,j]
 =-U[n,0](I+M^2)^{-1}U[4,j+1]e/C_j.                 \tag{18}
\]

The inverse $I+M^2$ is therefore not an auxiliary fitted correction. It
is the exact finite-torus antiperiodic closure. Removing $G_{\rm AP}$
from (17) leaves the declared open/direct bridge that generates the
half-space window.

Apply the same Block 119 left swap to the two contributions and assemble
the displayed window. If $K_H$ is the completed half-space kernel and

\[
 D:=K_T-K_H,                                         \tag{19}
\]

then exact entrywise comparison gives

\[
 K_T=K_H+D.                                          \tag{20}
\]

The half-space term is the positive rank-one kernel already constructed
in Block 119. In the present four-dimensional window,

\[
 K_H=y_+y_+^\dagger=K_H^\dagger.                    \tag{21}
\]

Taking adjoints of (20) and subtracting proves

\[
 K_T-K_T^\dagger=D-D^\dagger.                       \tag{22}
\]

This is the all-non-Hermiticity-in-(D) identity. It is stronger than
saying merely that $D$ is non-Hermitian: there is no remaining dressed
anti-Hermitian contribution in $K_H$, and there is no residual cross
term outside the exact additive defect.

The operator and split certificates are:

```text
TASK2 OPERATOR: G_AP is induced by R_AP[n,j]=-U[n,0](I+M^2)^-1U[4,j+1]e/C_j; G_T=-B_-1+[(G_open+B_-1)+G_AP].
TASK2 PROBE c=5/13: K_T=K_H+D; K_H Hermitian and f_H==0 all k; D#=('76a5a6a44a93', '2788fbb0fb59', 'b3b56235ae17', 'dc29e8a2d6f8').
TASK2 PROBE c=3/5: K_T=K_H+D; K_H Hermitian and f_H==0 all k; D#=('efa0aa0f26e5', 'f8ee6d26876e', '1b8676a3222f', '067a1c86ee6b').
```

The four defect digests at each fixture are sectorwise fingerprints, not
scalar fits. Equations (20)--(22) are checked exactly before any
finite-size interpretation is assigned.

## 5. The Vanishing Pencil

Let $P_T(z)$ be the displayed completed torus window pencil. The
additive kernel split induces

\[
 P_T(z)=P_H(z)+P_D(z),                               \tag{23}
\]

where $P_H$ and $P_D$ are the half-space and wrap-defect pencils. Set

\[
 f_T(z)=\det P_T(z),
 \qquad
 f_H(z)=\det P_H(z).                                 \tag{24}
\]

The exact half-space certificate is the polynomial identity

\[
 f_H(z)\equiv0                                      \tag{25}
\]

at every momentum and both fixtures. Thus the half-space vacuum is
exactly at one in the strongest sense: $z=1$ is not merely one selected
zero of a nonzero polynomial. The complete determinant polynomial
vanishes.

Because determinants are nonlinear, define the exact wrap increment by

\[
 W_f(z)
 :=\det(P_H(z)+P_D(z))-\det P_H(z).                  \tag{26}
\]

Equations (23)--(26) give the keystone value

\[
 f_T(1)=f_H(1)+W_f(1)=0+W_f(1)\ne0.                 \tag{27}
\]

The certificate expands $W_f(1)$ into terms mixed between $P_H$ and
$P_D$, together with the pure-$P_D$ term. Both parts are exactly
nonzero. The phrase “wrap contribution” therefore includes the
determinantal interaction of the displayed defect with the half-space
pencil; it does not misstate $W_f$ as only $\det P_D$.

The exact keystone rows are:

```text
TASK2 KEYSTONE FORMULA: f_T(1)=f_H(1)+W_f(1)=0+W_f(1), W_f=det(P_H+P_D)-det(P_H).
TASK2 KEYSTONE c=5/13: identity all k; exact (f_T,W_f,mixed,pure-D)#=('4caced4e336f', '335afea72bd4', 'ecc4e81c677b', '37350cda9ec9'); mixed,pure-D !=0.
TASK2 KEYSTONE c=3/5: identity all k; exact (f_T,W_f,mixed,pure-D)#=('3a7c97b3c2a0', '44ff5fe0126f', '9f7c8560b921', 'd042d4e05079'); mixed,pure-D !=0.
```

The half-space zero polynomial and torus nonzero value coexist without
contradiction because they belong to different carriers. Equation (27)
locates the difference exactly at the antiperiodic wrap interface.

## 6. The Finite-Size Law

The wrap has a closed finite-size form. Put

\[
 T=M^2.                                               \tag{28}
\]

On the declared two-channel Floquet block, $T$ has the reciprocal
eigenvalues $a$ and $a^{-1}$, where

\[
 0<a=\rho_F^2<1.                                     \tag{29}
\]

Let $P_s$ and $P_u$ be the corresponding rank-one stable and unstable
spectral projectors. They obey

\[
 P_s+P_u=I,
 \qquad P_sP_u=P_uP_s=0,
 \qquad
 T^N=a^NP_s+a^{-N}P_u.                               \tag{30}
\]

For a torus of (N) double periods, define

\[
 B_N:=(I+T^N)^{-1}.                                  \tag{31}
\]

Exact spectral calculus gives

\[
 B_N={P_s\over1+a^N}+{P_u\over1+a^{-N}}.             \tag{32}
\]

No large-(N) approximation enters (32). With

\[
 c_N={a^N\over1+a^N},                                \tag{33}
\]

equation (32) is equivalently

\[
 B_N=(1-c_N)P_s+c_NP_u.                              \tag{34}
\]

The exact finite-boundary correction is therefore

\[
 B_N-P_s=c_N(P_u-P_s).                               \tag{35}
\]

This correction is balanced: the same $c_N$ subtracts from the stable
projector and adds to the unstable projector. Calling it an
“unstable-only correction” would be false.

The wrap bridge contains the transported closure factor

\[
 Q_N:=B_NT^N.                                        \tag{36}
\]

Using (30)--(34),

\[
 Q_N=c_NP_s+(1-c_N)P_u,                              \tag{37}
\]

and hence

\[
 Q_N-P_u=c_N(P_s-P_u).                               \tag{38}
\]

Equations (35) and (38) are the exact two-sided projector law requested
by the torus split. Because $0<c_N<a^N$, its error coefficient decays
geometrically.

For the three explicitly requested lengths, the identities specialize
without any recurrence fit:

\[
\begin{array}{c|c|c}
 N&c_N&Q_N\\ \hline
 1&{a\over1+a}&{a\over1+a}P_s+{1\over1+a}P_u\\[2mm]
 2&{a^2\over1+a^2}&{a^2\over1+a^2}P_s
                       +{1\over1+a^2}P_u\\[2mm]
 3&{a^3\over1+a^3}&{a^3\over1+a^3}P_s
                       +{1\over1+a^3}P_u
\end{array}.                                         \tag{39}
\]

The supplied exact isolations of (a) are:

\[
\begin{aligned}
 c=5/13:\quad
 a_{\rm even}&\in(32190095809,32190095810)10^{-12},\\
 a_{\rm odd}&\in(404644318,404644319)10^{-12},\\
 c=3/5:\quad
 a_{\rm even}&\in(36167865356,36167865357)10^{-12},\\
 a_{\rm odd}&\in(191977555,191977556)10^{-12}.
                                                               \tag{40}
\end{aligned}
\]

All endpoints are positive and below one by exact integer comparison.
The certificate statement is:

```text
TASK3 FORMULA: put a=rho_F^2, so T=M^2 has (a,a^-1); B_N=(I+T^N)^-1=P_s/(1+a^N)+P_u/(1+a^-N).
TASK3 DEFECT: c_N=a^N/(1+a^N); B_N-P_s=c_N(P_u-P_s), B_N T^N-P_u=c_N(P_s-P_u).
TASK3 CERT c=5/13: a=rho_F^2 in ((32190095809, 32190095810), (404644318, 404644319))/10^12 for k even/odd; c_1=a/(1+a); (P_s,P_u,B_1)#=('9604735e6327', 'f3773519a234').
TASK3 CERT c=3/5: a=rho_F^2 in ((36167865356, 36167865357), (191977555, 191977556))/10^12 for k even/odd; c_1=a/(1+a); (P_s,P_u,B_1)#=('a9e1349ba917', 'bf4d3bb10ff8').
```

The fixed `Z8` window also contains the open/direct bridge visible in
(17). That contribution is not a boundary correction and is not asserted
to decay with (N). The geometric statement concerns the finite-boundary
projector error and the stable/unstable channels of the wrap bridge.

## 7. The Unstable Saturation

The exact limit of (37) is

\[
 \lim_{N\to\infty}Q_N=P_u.                           \tag{41}
\]

Within each declared momentum sector, $P_u$ has rank one and does not
depend on $N$. Its coefficient $1-c_N=1/(1+a^N)$ tends to one. The
stable-projector coefficient $c_N$ tends to zero geometrically. Thus
the antiperiodic wrap does not become a purely decaying stable correction:
its growing-mode channel saturates at an (N)-independent rank-one
limit.

This is the finite-torus meaning of the reciprocal Floquet pair. A mode
which grows as $a^{-N}$ around the winding is multiplied by the closure
factor $1/(1+a^{-N})$. Their product is

\[
 {a^{-N}\over1+a^{-N}}={1\over1+a^N}\longrightarrow1. \tag{42}
\]

The small closure coefficient therefore does not suppress the growing
mode after transport around the torus. On any fixed torus the
antiperiodic boundary speaks through the growing mode.

The half-space package makes a different carrier choice. It retains the
one-sided stable data and omits the winding equation, so $G_{\rm AP}$
and $D$ are absent by fiat. That is an honest definition of the
half-space carrier, not a proof that the literal antiperiodic torus kernel
loses its unstable channel. The finite-size law explains why naively
taking a longer torus does not justify that identification.

The runner records the distinction exactly:

```text
TASK3 INTERPRETATION PASS: the finite boundary error is the balanced P_u-P_s correction, not an unstable-only term; c_N tends geometrically to zero, while the Z8 window also contains the non-boundary open/direct bridge.
```

Equation (41) does not prove that every possible torus dressing retains
the same saturation. A different torus-adapted family might mix or cancel
the rank-one channel. That route remains named and open. What is decided
is the displayed Block 119 swap family and its exact defect (D).

## 8. The Corrected Completion And The Power Reconciliation

The defect split gives a precise corrected object:

\[
 K_{\rm corr}:=K_T-D=K_H.                            \tag{43}
\]

By the Block 119 factorization, rechecked in the present four-dimensional
window,

\[
 K_{\rm corr}=y_+y_+^\dagger.                        \tag{44}
\]

Therefore, for every $z\in\mathbb C^4$,

\[
 z^\dagger K_{\rm corr}z=|y_+^\dagger z|^2\ge0.     \tag{45}
\]

The factor is nonzero, so $K_{\rm corr}$ is Hermitian positive
semidefinite of rank one. With inertia ordered as positive, negative, and
zero,

\[
 \operatorname{In}K_{\rm corr}=(1,0,3)               \tag{46}
\]

at every momentum and both fixtures. This is the corrected half-space
completion. The literal torus matrix $K_T$ remains non-Hermitian and
has no inertia.

After quotienting the three-dimensional radical of (44), one moment
class remains per momentum. The quotient advance is

\[
 \beta=a^2.                                          \tag{47}
\]

The exact intervals in (40) imply

\[
 0<\beta=a^2<1.                                      \tag{48}
\]

It follows that the quotient is contractive and has the exact geometric
semigroup

\[
 \beta^n=a^{2n}=\rho_F^{4n},
 \qquad
 \beta^{m+n}=\beta^m\beta^n.                        \tag{49}
\]

There is no disagreement with Block 119. That block labels the stable
factor for one Floquet period by $\rho_F$, so its quotient advance is
$\rho_F^2$ per period. The present finite-size calculation first groups
the transfer into $T=M^2$ and calls its stable eigenvalue
$a=\rho_F^2$. Advancing both moment indices over that double-period unit
then gives $a^2=\rho_F^4$. Equation (49) samples the same geometric
semigroup on the doubled period lattice. This is bookkeeping, not a
power error or a new transfer law.

The exact positive certificates are:

```text
TASK4 CERT c=5/13: K_T-D=K_H=y_+y_+^H, per-k inertia=(1,0,3); half-space quotient beta=a^2 in (0,1); bounds#=e2f8d6a70d04.
TASK4 CERT c=3/5: K_T-D=K_H=y_+y_+^H, per-k inertia=(1,0,3); half-space quotient beta=a^2 in (0,1); bounds#=bfa32b248ca0.
```

Subtraction in (43) is an exact diagnostic and carrier restriction. It
shows where the obstruction lives and recovers the already honest
half-space package. It is not a derivation of a new torus counterterm,
and it does not establish a literal torus OS completion without
subtraction.

## 9. No-Go Discipline Gate

There is exactly one bounded finite-carrier wall.

- W1 — **LITERAL TORUS WRAP-DEFECT WALL:** on the displayed primary
  `Z8_t x Z4_x` carrier, at both rational shear fixtures and every fixed
  momentum, the Block 119 swap family leaves the literal antiperiodic
  torus pairing non-Hermitian with
  $\operatorname{rank}(K_T-K_T^\dagger)=4$. The exact split
  $K_T=K_H+D$ places the whole anti-Hermitian residual in $D$, and the
  rank-one unstable channel of the wrap bridge saturates rather than
  decays with torus length.

The wall is narrow. It covers the displayed carrier, the two fixtures,
the Block 119 dressing family, the displayed wrap (D), and the exact
subtraction $K_T-D$. It does not classify every torus-adapted dressing,
every possible subtraction, a different carrier, or the curved theory.

Most importantly, W1 is not an OS no-go, and it does not overturn the
positive half-space result.
The **POSITIVE** theorem side remains logically intact: after removing
the exact wrap, $K_H=y_+y_+^\dagger$ is Hermitian positive semidefinite
with inertia ((1,0,3)) and a contractive quotient. That statement is a
bounded theorem-side preservation, not an independent-audit retention
verdict.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). The exact split,
the zero pencil, the projector law, the saturation, the corrected
completion, and the live curved route are kept separate.

1. **PROVED — POSITIVE — torus/half-space kernel pair / exact additive
   defect split and adjoint subtraction / $K_T=K_H+D$ with all dressed
   non-Hermiticity in (D).** Equations (20)--(22) are the strongest row.
   They locate the full rank-four residual without assigning inertia to a
   non-Hermitian kernel.
2. **PROVED — completed half-space and wrap pencils / exact determinant
   identity / zero polynomial $f_H\equiv0$ and
   $f_T(1)=W_f(1)\ne0$.** Both mixed and pure-defect parts of the wrap
   increment are nonzero.
3. **PROVED — finite torus closure / reciprocal spectral projectors /
   exact law (32)--(38).** The balanced correction is
   $c_N(P_u-P_s)$, with exact specializations at $N=1,2,3$.
4. **PROVED — wrap bridge / growing reciprocal Floquet mode / rank-one
   unstable saturation.** The stable coefficient $c_N$ decays
   geometrically while $Q_N\to P_u$, an $N$-independent rank-one
   limit.
5. **PROVED — displayed defect subtraction / half-space rank-one
   factorization and period reindexing / corrected inertia $(1,0,3)$,
   quotient $\beta=a^2\in(0,1)$, and the same geometric semigroup.** The
   $\rho_F^4$ exponent is the doubled-period bookkeeping of Block 119's
   per-period $\rho_F^2$.
6. **UNTESTED-LIVE — naturality classification and curved carrier /
   compare torus-adapted dressings, then transport the honest half-space
   package / curved OS positivity before gravity.** This route remains
   open and is not counted as an attempted route beyond W1.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is distinct from Block 119's W1, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:697-714`.

Block 119 studied candidate selection on an already chosen half-space
pairing. Its wall tested whether fourteen fixed carrier-natural operators
sent the left rank-one factor (x) to the line spanned by (y). The
mechanism was an exact nonproportionality residual. A data-built swap then
passed, so the wall did not become an existence no-go.

The present wall studies carrier transfer of that successful swap. It
asks whether the completed half-space object remains Hermitian after the
antiperiodic winding is restored. Its mechanism is the additive wrap
defect (20), the full-rank residual (22), and the unstable saturation
(41). Candidate selection and carrier transfer are different objects.

Neither wall implies the other. A swap can solve the half-space
proportionality condition while failing after a wrap term is added, as it
does here. Conversely, failure of one named swap on the torus does not
imply that every torus-adapted dressing fails proportionality or
Hermiticity.

The positive corrected package is independent again. Its Hermiticity and
inertia follow from $K_T-D=y_+y_+^\dagger$, while its contraction follows
from $0<a^2<1$. These are exact positive identities, not consequences
of declaring the literal torus swap unsuccessful.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified
explicitly. Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| primary carrier | inherited finite `Z8_t x Z4_x` carrier only |
| both rational shear fixtures | exactly $c=5/13$ and $c=3/5$ |
| block 119 swap family | the displayed data-built swaps, no universal dressing class |
| literal antiperiodic torus pairing | the finite winding pairing tested by the runner |
| non-hermitian | exact failure $K_T\ne K_T^\dagger$ |
| residual rank four per momentum | exact rank of $K_T-K_T^\dagger$, not inertia |
| torus kernel | the displayed completed $K_T$ only |
| half-space kernel | the Block 119 completed $K_H$ only |
| displayed antiperiodic wrap defect | $D=K_T-K_H$ from (19) |
| all of the dressed non-hermiticity | exact identity (22) |
| completed half-space window pencil vanishes identically | zero polynomial $f_H\equiv0$ |
| torus pencil value at one | the exact nonzero value $f_T(1)$ |
| wrap contribution | $W_f=\det(P_H+P_D)-\det P_H$, including mixed terms |
| exact projector law | equations (32)--(38) for every positive (N) |
| geometrically decaying stable-channel coefficient | $c_N=a^N/(1+a^N)$ in $Q_N$ |
| rank-one unstable-projector channel | the $P_u$ term in (37) |
| n-independent limit | $Q_N\to P_u$, sectorwise and independent of torus length |
| subtracting the displayed defect | exactly $K_T-D=K_H$ |
| hermitian positive semidefinite completion | the corrected half-space factorization only |
| contractive quotient | exactly $\beta=a^2\in(0,1)$ after radical quotient |
| same geometric semigroup | period-reindexed powers (49) |
| inertia is undefined | the literal non-Hermitian torus kernel has no Hermitian inertia |
| displayed carrier | no extrapolation to another finite or curved carrier |
| dressing family | the Block 119 swap family only |
| displayed subtraction | exact removal of (D), not an arbitrary counterterm |
| torus completion without subtraction | explicitly not proved |
| naturality classification | untested-live downstream classification |
| curved os positivity | explicit reconstruction firewall |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not coupled |
| gravity constraint quotient | explicitly not formed |
| records | no Records claim |
| retention | independent-audit firewall, not a bare status assignment |
| axiom amendment | explicitly not justified |
| obligation retirement | TOE accounting firewall |
| toe percentage movement | TOE accounting firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting statement |
| no toe percentage moves | TOE accounting statement |
| retained-positive end-to-end theory count remains zero | audit-status accounting |
| actual adm/history transporter remains | standard partial-closure statement |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | the five N5 resolution keys |

No phrase upgrades the displayed torus failure to impossibility of a
torus OS package, promotes defect subtraction to a derived counterterm,
identifies the half-space carrier with a torus limit, asserts naturality
or curved OS positivity, completes the ADM/history transporter,
authorizes gravity, changes audit status, or moves TOE accounting.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 119 next gate](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md), docs/ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md:16 and :1013-1029 | carry the completed half-space OS package to the antiperiodic torus and curved carrier, classify naturality, then form the gravity constraint quotient | the literal torus transfer is now decided negatively for the displayed swap and localized exactly in $D$; the half-space package stands, while naturality, curved OS, and gravity remain |
| [Block 118 Klein/Floquet wall](ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md), docs/ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md:726-752 | the torus retains the Klein structure and negative Floquet eigenvalues with a growing reciprocal channel | the antiperiodic wrap through the growing mode is that structure's torus shadow; $Q_N\to P_u$ makes the shadow exact without changing Block 118's wall |
| [Block 116 non-semigroup wall](ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md), docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md:467-492 | the displayed chart windows did not furnish a stationary one-step semigroup | Block 119 resolved the semigroup on the stable half-space; the present split now places the discrepancy: the wrapped torus was the wrong carrier for that half-space semigroup, while the corrected quotient still has exact powers (49) |

Every inherited residual reaches exactly its stated interface. No citation
is used as an audit verdict. The torus shadow explains the return of the
growing mode without pretending that Block 118 already proved the present
defect formula, and the half-space semigroup is not silently upgraded to
the literal torus.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the primary finite carrier at
both rational shear fixtures, the Block 119 swap family leaves the
literal antiperiodic torus pairing non-Hermitian with residual rank four
per momentum, the exact split $K_T=K_H+D$ places all dressed
non-Hermiticity and the saturating unstable wrap channel in $D$, and
subtracting that defect recovers the Hermitian positive semidefinite
half-space completion with inertia $(1,0,3)$ and the exact contractive
geometric semigroup $\beta^n=a^{2n}$.”

Forbidden upgrades include “the torus OS package is impossible,” “the
half-space limit is proven to reconstruct curved QFT,” and “the
transporter is finished.” The first is not shown: only the displayed
carrier, fixtures, Block 119 dressing family, wrap defect, and subtraction
are decided. The second would confuse a one-sided carrier definition with
a curved reconstruction theorem. The third would erase the explicit
downstream transporter firewall.

Also forbidden are “no torus-adapted dressing can remove the unstable
channel,” “subtracting (D) derives the physical torus counterterm,” “the
fixed torus converges to the half-space package,” “the completion is
natural,” “curved OS positivity holds,” “the gravity constraint quotient
can now be executed,” “an axiom amendment is required,” and “audit
retention follows from this note.”

The runner specification's five resolution lines are reproduced
verbatim:

```text
N5: per_element: exact torus/half-space split, anti-Hermitian residual rank, all-non-Hermiticity-in-D, zero-pencil, projector, subtraction, Hermiticity, inertia, and quotient identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: all four fixed momenta at c=5/13 and c=3/5 have rank(K-K*)=4 before subtraction and corrected inertia (1,0,3) after exact defect subtraction
per_block: the literal Z8 torus pairing splits as K_T=K_H+D; D carries all dressed non-Hermiticity, while K_T-D=K_H=y_+y_+^H has quotient beta=a^2 in (0,1)
lattice_wide: checked and not executed — torus completion without the displayed subtraction, naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The present decision separates an
exact carrier obstruction from an intact half-space package. Remaining
routes concern dressing classification, curved transport, and downstream
reconstruction.

| route | present status | remaining terminal |
|---|---|---|
| literal torus Hermiticity | exact failure at all four momenta and both fixtures | none for the displayed Block 119 swap family |
| anti-Hermitian residual | exact rank four per momentum | none for the displayed torus windows |
| torus/half-space split | exact $K_T=K_H+D$ | none for the displayed defect |
| defect localization | exact $K_T-K_T^\dagger=D-D^\dagger$ | none for all-non-Hermiticity-in-$D$ |
| half-space pencil | exact zero polynomial $f_H\equiv0$ | none for the displayed windows |
| torus value at one | exact $f_T(1)=W_f(1)\ne0$ with nonzero mixed and pure-$D$ terms | none for the displayed pencils |
| finite-size inverse | exact projector law for every $N\ge1$ | none for the displayed reciprocal pair |
| requested sizes | exact $c_1,c_2,c_3$ laws | none for $N=1,2,3$ |
| unstable saturation | exact $Q_N\to P_u$, rank one and $N$-independent | none for the displayed wrap bridge |
| corrected completion | exact $K_T-D=y_+y_+^\dagger$ | none for the displayed subtraction |
| corrected inertia | $(1,0,3)$ per momentum at both fixtures | none for the four-dimensional windows |
| quotient contraction | exact $\beta=a^2\in(0,1)$ | none for the corrected radical quotient |
| power reconciliation | exact doubled-period reindexing of Block 119's semigroup | none for the displayed powers |
| alternative torus dressing | untested-live | test whether another family cancels or mixes the saturating channel |
| naturality classification | untested-live | classify the half-space completion under carrier maps |
| curved OS route | not executed | run curved-carrier positivity on the honest half-space package |
| gravity route | not executed | complete transport, then form the gravity constraint quotient |

The scan finds no axiom-amendment route. The torus part of Block 119's
next gate partially closes: its displayed swap does not complete the
literal torus, and the failure is isolated exactly in the wrap defect.
The positive half-space package remains available after exact carrier
restriction. Naturality, another torus dressing family, curved OS
positivity, the completed transporter, and gravity remain open, so the
end-to-end route does not close.

### N7 — Steelman

**Hostile steelman against subtraction.** Subtracting $D$ by hand is
not a derivation. If $D$ is part of the literal antiperiodic torus, why
should $K_T-D$ count as a completion rather than deletion of the
obstruction?

That objection is correct about the torus. Equation (43) is not presented
as a derived physical torus counterterm. Its value is diagnostic: the
exact subtraction displays **where** the obstruction lives and proves
that no defect is hiding in the completed half-space kernel. The honest
carrier statement is the half-space statement. On that carrier the
winding term is absent by definition, and $K_H=y_+y_+^\dagger$ is the
positive package. The literal torus without subtraction remains a
failure for the displayed swap.

**Hostile steelman against the dressing-family boundary.** The
saturating term is rank one. A different torus dressing might act on its
range, mix it with the stable line, or cancel it against another
torus-local contribution. Why treat W1 as meaningful if that possibility
has not been exhausted?

W1 remains meaningful because its object is explicit and finite: the
Block 119 swap family on the literal torus. Equations (20), (22), and
(37) decide that object exactly. But the objection identifies the correct
open alternative. The saturating piece might be removable by a different
torus dressing family. That route is untested-live, named in N1 and N6,
and excluded from the no-go conclusion.

**Hostile steelman against the half-space interpretation.** Since
$c_N\to0$, why not say that the torus tends to the half-space and ignore
the rest?

Because $c_N$ controls a balanced projector error, while the transported
wrap bridge is $Q_N=c_NP_s+(1-c_N)P_u$. Its unstable term tends to
$P_u$, and the fixed window retains the open/direct bridge. Dropping
only the small coefficient misses the multiplication by the growing
mode. The half-space is a carrier restriction, not the proved limit of
the literal torus package.

These steelmen leave narrow W1 intact. They prevent the displayed
subtraction from being sold as a torus derivation, the half-space from
being sold as a torus limit, and the finite-family failure from being sold
as universal torus non-completability.

### N8 — Cross-Cycle Echo

The fourteen prior campaign blocks each narrowed the hunt; the discipline
held.

| campaign block | narrowing that led to the present wall and correction |
|---|---|
| Block 106 | fixed the local dual-descent entry and preserved the action-to-Gram order |
| Block 107 | isolated the finite two-history seam carrier |
| Block 108 | tested the locality reach of involutive seam dressing |
| Block 109 | forced the dressing search to global support |
| Block 110 | restricted the viable signature to the even sector |
| Block 111 | factorized the positivity frontier and displayed the self-block involution families |
| Block 112 | exposed the paired even-parity branch and its count |
| Block 113 | refuted the paired floor and located the mixed-circle crossing |
| Block 114 | supplied the exact positive chart and endpoint beyond the certified crossing |
| Block 115 | separated Hilbert positivity from transfer contractivity on the displayed windows |
| [Block 116 chart wall](ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md) | proved the paired-chart freeze and recorded the non-semigroup window behavior |
| Block 117 | closed the displayed self charts and named an action-derived stationarity repair |
| [Block 118 Floquet/action wall](ADMISSIBILITY_DIRAC_KAHLER_FLOQUET_MONODROMY_ACTION_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-16.md) | derived the reciprocal stable/growing structure and isolated the half-space geometric-Hankel route |
| [Block 119 swap completion](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | completed the half-space pairing and left the antiperiodic torus transport open |

The current block preserves that narrowing. It carries the displayed swap
back to the literal torus, rejects that transfer by a full-rank
anti-Hermitian residual, and then splits the failure rather than
misreporting it as a failure of the half-space completion. The wrap
through the growing mode is the torus shadow of Block 118's reciprocal
Floquet structure. The corrected half-space quotient preserves Block
119's exact geometric semigroup, while the literal torus is identified as
the wrong carrier for that unmodified swap.

**No-Go Discipline verdict:** **PASS** only for narrow W1: the literal
`Z8` torus pairing rejects the Block 119 swap family exactly through the
displayed wrap defect, whose unstable channel does not decay with torus
length. Exact subtraction of that defect recovers the **POSITIVE**
half-space package. **FAIL** for “the torus OS package is impossible,”
failure of every torus-adapted dressing family, derivation of a physical
torus subtraction, proof of a torus-to-half-space limit, naturality,
curved OS positivity, a completed ADM/history transporter, gravity, axiom
necessity, audit retention, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. The rank-four anti-Hermitian residuals,
torus/half-space split, antiperiodic wrap formula, all-non-Hermiticity
identity, zero half-space pencil, wrap-only torus value, stable/unstable
projector law, finite-size coefficients, unstable saturation, exact
defect subtraction, rank-one positive factorization, inertia, contraction
bound, and geometric powers are finite consequences of the displayed
carrier, fixtures, swap family, and propagator data. No new primitive is
assumed.

This is bounded route progress, not an audit-grade assignment. It retires
no end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. classify the completion's naturality on the honest half-space package;
2. execute the curved-carrier OS positivity question on that half-space
   package; and
3. then form the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed
half-space swap completion, positive semidefinite moment package, exact
torus-wrap diagnosis, and geometric semigroup.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
