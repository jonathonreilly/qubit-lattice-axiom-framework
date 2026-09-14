# Block 5: what a local Gaussian field requires of permanent formation

Personal campaign continuation. Start 2026-09-14 16:48 UTC;
deadline remains 2026-09-15 01:30:44 UTC. No agents.

## Leverage reassessment

PR8125 now gives a conditional fixed-period Gaussian routing/codec theorem,
including the protected local cluster shape. Its checkout was removed after
exact remote and clean-state verification. The original Gaussian action,
compatible periodic DK source and autonomous formation remain open. Adding
more static Gaussian codecs would not by itself address the process gap.
The next target is the missing inference from full-neighbor Gibbs conditionals
to probabilities depending only on readable, previously formed records.

## Assumptions to keep explicit

The native axioms supply permanent readable records and a nearest-neighbor
conditional admissibility rule, but do not select formation sites/rates,
Gaussian noise, a joint history law, a schedule or a scalar readout. Begin
with a sharply specified candidate: a supplied deterministic one-site order,
each record carries the target scalar value only (or an invertible one-site
codec plus independent spectators), and its sampling kernel can use only
previous nearest-neighbor values. No hidden messages, global shared latent
seed, value-dependent schedule or simultaneous correlated block writes are
included in this first candidate. Its failure would not refute the axioms.

For a real nondegenerate Gaussian target with precision Q, forming site v
in past prefix A uses the marginal precision
K_A=Q_AA-Q_AF Q_FF^-1 Q_FA, F the unformed future. The exact conditional
coefficients are -K_(v,u)/K_(v,v), with variance 1/K_(v,v). Thus the candidate
is exact if and only if every such coefficient to a past nonneighbor vanishes.
This should be proved directly, without assuming a Markov full conditional
continues to hold after unformed neighbors are integrated out.

## Derivation to challenge

For positive definite M-matrix Q (negative edge entries), Q_FF^-1 is entrywise
nonnegative and strictly positive within each connected future component.
A Neumann series should show that marginal fill edges are exactly paths whose
internal vertices lie in F; signs cannot cancel. Therefore the candidate
order should be exact precisely when reverse elimination produces no fill.
This is the perfect-elimination/chordal-graph criterion. On a triangle-free
nearest-neighbor lattice an interaction graph with a cycle should fail it.
A self-contained induced-cycle proof can avoid importing a graph theorem.

An independent route uses a Gaussian autoregression factorization:
Q=(I-A)^T D^-1(I-A). Exact target conditionals for an M-matrix give nonnegative
regression coefficients. On the triangle-free lattice, two parents of one
child would contribute a strictly positive precision entry between physical
nonneighbors, with no direct-edge cancellation. This is a useful second
calculation, with its positivity assumptions explicitly checked.

## Small exact target and quantitative metric

Use the four-cycle precision Q=3I-Adj(C4). In order (0,1,2,3), integrating
future vertex 3 should give K_02=-1/3 and K_22=8/3. The exact third conditional
mean is (x0+3x1)/8, variance 3/8; the nonneighbor x0 cannot simply be dropped.
For any fixed order, optimize over ALL local conditional densities, not just
linear Gaussian candidates. The KL projection identity should give
min KL(P||product q_local)=sum conditional mutual informations. The optimum
uses the target's local-parent conditionals. For the cycle above the minimum
over orders is expected to be (1/2)log(64/63), with the opposite-first case
(1/2)log(49/45). These are hypotheses to check exactly, not claimed evidence.

## Alternatives that must remain live

- Extra records carrying separator messages or correlated latent variables.
- New physical sites for successive sampler updates, respecting permanent writes.
- Larger local blocks and simultaneous correlated formation events.
- Value-dependent schedules, or schedules that themselves communicate information.
- Non-Gaussian encodings and the unrestricted continuous M2 domain.
- Approximation with a derived error, rather than exact equality.
- A different causally factorable target law, such as a tree or supplied DAG.
- A separately supplied global history law; this is not derived by a local Gibbs kernel.

For Gaussian components and an exogenous random order, a mixture argument
might extend a fixed-order statement, but arbitrary nonlinear kernels or
adaptive schedules require a separate proof. Do not generalize automatically.
If a negative boundary ships, apply the full no-go discipline and retain these
escapes. No axiom-update claim is currently justified.

## Targeted literature, initial search coverage

The search found Rose--Tarjan--Lueker, Algorithmic Aspects of Vertex Elimination
on Graphs (1976), DOI 10.1137/0205021, publisher abstract only so far; and
Lauritzen's Oxford Gaussian graph lecture page, not yet its full slides.
https://epubs.siam.org/doi/pdf/10.1137/0205021
https://www.stats.ox.ac.uk/~steffen/teaching/gm11/gmi12.htm
Also a primary UCLA covariance-selection paper PDF, not yet read:
https://www.seas.ucla.edu/~vandenbe/publications/covsel1.pdf
Read the relevant hypotheses before importing any theorem. The intended
Gaussian and four-cycle calculations will be derived independently.

## First exact cancellation, 16:53 UTC

A symbolic 4x4 calculation finds a positive local counterexample to a
sign-blind graph obstruction. Take
Q=[[3,-1,0,1],[-1,3,-1,0],[0,-1,3,-1],[1,0,-1,3]].
Its eigenvalues are 3+-sqrt(2), each twice; its inverse is
(1/7)[[3,1,0,-1],[1,3,1,0],[0,1,3,1],[-1,0,1,3]].
The marginal precision on (0,2) after integrating (1,3) is (7/3)I.
Hence order (0,2,1,3) can draw the first two independent N(0,3/7), then
x1=(x0+x2)/3+N(0,1/3), and x3=(-x0+x2)/3+N(0,1/3), using only graph neighbors.
The two parent-parent fill contributions cancel. This must be checked by a
separate covariance/factorization calculation in the finite runner.

The M-matrix/noncancellation hypothesis is therefore load-bearing. The
actual DK source has signed/complex couplings and cannot inherit a generic
attractive-Gaussian obstruction without a source-specific argument. The
positive cancellation suggests a next useful question: can the native
Dirac/Clifford structure enforce the needed orthogonality for a local causal
factorization, or does a dispersive massive scalar Schur block remain?
This is more useful than shipping a sign-blind impossibility statement.

Literature coverage updated: UCLA covariance-selection PDF introduction,
section 2.1 and sections 3.1--3.2 read through the clique Schur induction
(first 406 extracted lines; final few lines of section 3.2 still to read).
The graph theorem is sufficient for no-fill for an entire sparsity class;
it does not exclude tuned numerical cancellations in a nonchordal graph.
