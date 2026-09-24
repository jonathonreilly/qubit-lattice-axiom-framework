# Star birth energy across the local electric family

Personal conditional bridge calculation, 2026-09-24; independent reconstruction
pending. The positive terminal-field completion is a different question from the
microscopic energy carried by the original formation channel. This exact star
calculation relates them without changing that channel or selecting lambda.

## 1. Same supplied family, common finite-energy preparation

Use the physical star A={0}, B={1,2,3}, div E=q-1_A, with integer S>=1. The
Gauss constraint gives E_0b=-q_b. On this entire sixteen-state physical sector,
D_ext=0 because every active outward edge ends at an empty leaf with E=0.
The previously supplied electric family is

`C_S^lambda=C_S+lambda(E2-D_ext)/[S(S+1)]`, `0<=lambda<=1`.

At `epsilon² S(S+1)=delta/K`, its full microscopic Hamiltonian is exactly

`H_lambda=H_0+K lambda E2`,

where H_0 is the positive square Hamiltonian in the original exact-star note.
Since E2 is the number of occupied leaves, it obeys

`E2|_(N=1)=W`, `E2|_(N=3)=2I+W`.

In particular the addition is bounded by 3K on this entire physical space.
All original resolved/coherent j and their epsilon scaling are retained.

Choose the same explicit preparation for every lambda:

`psi=(g+epsilon Fg)/sqrt(a)`, `a=1+3epsilon²`.

It has zero H_0 energy, but it is not an exact eigenstate of H_lambda for
lambda>0. Its actual initial energy is

`E_initial(lambda)=3K lambda epsilon²/a`.                       (1)

It tends to zero. Thus the preparation does not hide a divergent initial energy
supply. No assertion of exact low-cluster preparation for the changed law is
needed. The initial density still approaches gg* in trace norm.

## 2. Exact actual-output moments

The unchanged marks give precisely the same immediate normalized states v as
in the exact-star note. Every such state lies in the N=3 P space, so E2 v=2v.
Although H_0 and E2 do not commute on the full space,

`H_lambda v=H_0 v+2K lambda v`.

Consequently its mean and variance are exactly

`mean(H_lambda)=c delta/epsilon²+2K lambda`,

`Var(H_lambda)=c delta² epsilon^-6 [1+(3-c)epsilon²]`,            (2)

where c=2 for a plus resolved mark, c=1 for a minus resolved mark, and c=3/2
for a coherent edge mark. The lambda addition changes the mean by a scalar on
the immediate output but leaves this variance unchanged. This argument uses the
norm of H_lambda v, so it retains the entire high-energy spectral contribution.
It does not assume that the new spectrum still has only the two old energies.

The total initial intensity is still `12kappa/a`. The initial full GKLS energy
derivative is

`d mean(H_lambda)/dt|0 = 18kappa delta/(epsilon² a)+12kappa K lambda/a`. (3)

Here the gain is `18kappa delta/(epsilon²a)+24kappa K lambda/a`, and the
loss contribution is `-12kappa K lambda/a`. For lambda>0 the loss-energy term
cannot be omitted by carrying over the old zero-energy-eigenstate argument.
The Hamiltonian contribution to its own energy remains zero.

## 3. Exact finite-time relation and its asymptotic

The no-event state again remains in span(g,s), s=Fg/sqrt(3). Its two-by-two
generator is the earlier G plus `-iK lambda diag(0,1)`. Write this G_lambda,
`v_lambda(t)=exp(tG_lambda)ell`, and `P_b,lambda(t)=1-||v_lambda(t)||²`.
Each possible first mark still produces the same normalized output with the
same instantaneous relative mark weights. No second microscopic birth is
possible. Subsequent N=3 evolution conserves its H_lambda energy. Therefore

`E_total,lambda(t)=E_no,lambda(t)`
`                +[3delta/(2epsilon²)+2K lambda] P_b,lambda(t)`,     (4)

`E_no,lambda(t)=<v_lambda(t),H1,lambda v_lambda(t)> >=0`.

Positivity follows from H_0>=0 and K lambda E2>=0. This is an exact finite-time
identity for both instruments.

The scaled characteristic polynomial of G_lambda is

`epsilon⁴ z²+[i delta a+2kappa epsilon²+iK lambda epsilon⁴]z`
`             +i6kappa delta-3delta K lambda epsilon²=0`.

The root continuous from -6kappa is

`z_s=-6kappa+[18kappa-i(12kappa²/delta+3K lambda)]epsilon²`
`                    +O(epsilon⁴)`.

In the old orthonormal low/high coordinates, its low diagonal entry is
`-6kappa/a-i3K lambda epsilon²/a`. The off-diagonal entry is
`2sqrt(3)kappa/(epsilon a)+i sqrt(3)K lambda epsilon/a`; the large imaginary
high diagonal remains of order epsilon^-4. The same eigenvector argument as in
the finite-time star note gives high amplitude O_T(epsilon³), low amplitude
`exp(-6kappa t)+O_T(epsilon²)`, and therefore

`P_b,lambda(t)=1-exp(-12kappa t)+O_T(epsilon²)`,

`E_no,lambda(t)=O_T(epsilon²)`.

For each fixed lambda in [0,1], fixed positive K,delta,kappa and each fixed t>0,

`epsilon² E_total,lambda(t) -> (3delta/2)[1-exp(-12kappa t)]`,       (5)

or `E_total,lambda(t)/[S(S+1)] -> (3K/2)[1-exp(-12kappa t)]`.
The leading cost is the same throughout this family. This is a finite-star
statement, not a general-graph uniform theorem.

## 4. Consequence for a proposed energy account

For an additional proposed energy-conserving dilation with nonnegative
reservoir energy, reproduction of the microscopic system energy requires

`E_R(0) >= E_total,lambda(t)-E_initial(lambda)`
` >= [3delta/(2epsilon²)+2K lambda] P_b,lambda(t)-3K lambda epsilon²/a`. (6)

A bounded interaction allowance changes the left side to E_R(0)+2||V|| under
the conservation hypothesis stated in the preceding finite-time note. These are
resource inequalities under explicit extra assumptions, not a construction of
that dilation and not a prohibition on resources growing with S.

The electric completion can change target postbirth phases while leaving this
microscopic resource scaling intact. It therefore does not by itself supply an
energy source for the original birth instrument. This conclusion does not
reject the family as a supplied effective model or select a member. A reservoir,
additional microscopic degrees of freedom, changed energy law or controlled
moment approximation would have to be stated and examined separately.

## 5. Evidence and limits

The standalone symbolic control reuses the pinned root star matrices and checks
(1)-(3), the new two-by-two polynomial and its slow root through epsilon².
The analytic symmetry and eigenvector argument supply (4)-(5); a finite collection
of epsilon values is not used to infer them. The output variance is checked
from complete twelve-dimensional Hamiltonian action. The reuse is recorded as
author consistency evidence, not independent review.

The conditional common target on this star is zero in N=1 and 2K lambda in
N=3; its energy is finite. This does not identify its energy moments with those
of the microscopic Hamiltonian. The star has no cycle and can form only once.
No general cube leakage coefficient, infinite-volume result, autonomous
reservoir, empirical particle law, native selection or audit status is claimed.
