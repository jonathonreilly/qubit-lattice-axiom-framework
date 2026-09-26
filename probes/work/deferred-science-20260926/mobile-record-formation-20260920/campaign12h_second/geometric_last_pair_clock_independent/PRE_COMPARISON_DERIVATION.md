# Last-pair clock: independent reconstruction before author code

The complete 158-line supplied note, SHA-256
`0f5c6bdb5ce0c2ac3e7aa32bef5dfe57e1de0f914c81af984e4195d92722ebd7`,
has been read. The previous geometric and rare-birth proofs are reused at
their checked identities, including the separately acknowledged rare-birth
F1 correction. The author clock checker, results and logs remain unopened.
No production, phase, wave or unrelated primary source was accessed.

## Joint clock and exit law

Work on the finite near-perfect geometric matching space. The fixed
conservative generator S is symmetric and irreducible, its invariant pi is
uniform, and h indicates an enabled final birth. The unique vacant edge on
a simple graph determines the final matching, so the target indicators a_F
sum to h. The previously checked edge-deletion count gives
pi(a_F)=K/|Omega| and p=pi(h)=K Z/|Omega|>0.

First-step conditioning with killing beta h and discount s beta gives

    [-S+beta(H+sI)] u_beta,s,F = beta a_F.

Irreducibility and a nonempty killing set imply almost-sure eventual birth
and invertibility at s=0; positive s only increases the killing. The
probabilistic vector u is bounded between zero and one. Any convergent
subsequence as beta decreases to zero has an S-harmonic limit, hence a
constant c. Averaging the exact equation against pi gives
pi((h+s)u)=pi(a_F), so c=pi(a_F)/(p+s)=(1/Z)p/(p+s).

The common Laplace limits identify an Exp(p) clock and an independent
uniform exit. Finitely many entrance states and targets make convergence
uniform over entrance distributions, including beta-dependent ones. This
is a joint weak limit of (beta tau,F); it does not assert finite-beta
independence, a whole-growth-time law, or convergence at a fixed physical
time. Laplace continuity at zero gives tightness; uniqueness of Laplace
transforms then identifies the joint limit with the finite target variable.
No moment statement has been inferred just from weak convergence.

## Exact mean and its first correction

Use the pi inner product, with the constant function normalized to norm one.
Let L=-S, P project onto constants and Q=I-P. On the centered subspace L is
strictly positive when |Omega|>1. Because H is nonnegative,

    R_beta=(Q L Q+beta Q H Q)^(-1) on ran Q

exists, is positive, and is bounded near beta=0 at each fixed graph. Put
q=h-p and C_beta=<q,R_beta q>_pi. Write the unique finite mean as t=c+v
with pi(v)=0. Centering (L+beta H)t=1 gives
v=-beta c R_beta q. Averaging gives
beta c(p-beta C_beta)=1. Therefore

    t(M)=[1-beta(R_beta q)(M)]/[beta(p-beta C_beta)].

L+beta H is positive definite: its null-form vectors would be constant
and vanish on a nonempty killing set, and hence zero. Its Schur complement
on constants is beta(p-beta C_beta), proving the stated positive denominator.
The source's factors and inner-product normalization are correct.

At fixed graph, R_beta=R_0+O(beta) and C_beta=C_0+O(beta), giving uniformly
over the finite set of starts

    t(M)=1/(beta p)+C_0/p^2-(R_0 q)(M)/p+O(beta).

Thus beta t converges to 1/p separately from the weak-law argument. The
one-state case has h=1 and t=1/beta directly; no nonzero centered space or
spectral gap is needed. Constant hazard also gives q=0 and exact t=1/beta.

For stationary entrance, pi(t)=1/[beta(p-beta C_beta)]>=1/(beta p).
An independent check of its sign is Jensen's inequality:
P_pi(tau>t)=E_pi exp(-beta integral_0^t h(X_r)dr)>=exp(-beta p t),
followed by integration in t. Pointwise means need not satisfy this bound.
Neither argument supplies size-uniform inverse bounds: the centered
relaxation and p itself may deteriorate with volume.

## Monomer counting and imported equilibrium statement

On an even cubic torus of side N>=4, let Z count all perfect matchings and
Z(u,v) count matchings with exactly the opposite-parity sites u,v vacant.
Each near-perfect matching is counted exactly once by u in the even side
and v in the odd side. Translation by an even site preserves this partition,
so every fixed even u has the same sum over v. With K=V/2,

    |Omega|=sum_{u even,v odd} Z(u,v)=K Z chi,
    chi=sum_{v odd} Z(0,v)/Z,             p=1/chi.

Summing instead over both ordered hole orientations counts every matching
twice; this is the possible factor-of-two error. For a neighbor v of 0,
adding the absent edge bijects these two-hole matchings to full matchings
containing that edge. Cubic torus symmetry and degree 2d give Xi(v)=1/(2d).
The adjacent terms therefore sum to one. Conditional on one vacancy at 0
under the uniform near-perfect law, the other has distribution Xi(v)/chi.
This is not the law of a finite-rate birth-event sample.

The external import was checked in [Taggi v3](https://arxiv.org/html/1909.06558v3)
and authenticated local PDF SHA-256
`50a6f8a42cd5865a509efb706823e2dd0061233f49e6ec06d5395a627c1d2517`.
Its definitions use the same unweighted periodic nearest-neighbor counting
ratio, all sectors, even side and odd sublattice. Theorem 2.1 assumes integer
d>2; Eq. (2.3) averages over the odd half of the volume and takes a liminf.
Eq. (2.5) is the stated finite-even-side pointwise upper bound. The return
parameter excludes the initial walk visit. Eq. (2.4) requires a fixed margin,
large enough even side and odd axis separation below its stated side-scale
cutoff. Definitions and statements, including their application hypotheses,
were checked; the reflection-positivity proof and the prior monotonicity
result behind Eq. (2.5) were not independently re-proved.

Multiplying the imported one-sublattice bounds by K/V=1/2 yields exactly

    (1-r_d/2)/(4d) <= liminf chi_N/V
                     <= limsup chi_N/V <= 1/(4d).

This is an imported-equilibrium bound combined with an independently checked
counting identity and finite-state clock theorem. It applies to the ordered
quantity lim_(beta->0) beta E tau/V at each N, followed by N tending to
infinity along even sides. It asserts neither existence of lim chi_N/V nor
a fixed-rate growth law, and provides no upper bound on total growth from
empty. The PDF and HTML imported formulas agree; version/date details and
the precise reading boundary are in `LITERATURE_READ_RECEIPT.json`.

## Exact independent controls and countercontrols

The new checker imports only previously sealed independent matching
primitives. All mathematical checks passed on their first run:

- C4 and C6 joint Laplace transforms were solved symbolically, including
  every entrance state and full target. Differentiating the total transform
  at s=0 agrees with beta times the separately solved mean, testing the
  time-scale normalization. C6 gives 1/(3s+2) per target. On C4 the clock is
  exactly Exp(beta), but its joint transform differs from the product of
  finite-beta marginals by
  `2 beta s/[(beta+4)(s+1)(beta(s+1)+4)]>0` for a suitable start and target.
  Independence is therefore correctly only a limiting assertion.
- On the 44-state near-perfect cube, p=9/11 and C_0=30/1331. The full
  centered inverse gives stationary first correction 10/297. The three mean
  classes have corrections -1/27, 1/54 and 5/27 (12,24,8 states). Their
  exact three-class means were lifted and checked in all 44 original mean
  equations. Exact full-matrix Schur formulas also agree at beta=1/2 and
  1/10, including denominator positivity.
- A parallel three-edge cube start has mean
  `11/(9 beta)-2/[9(beta+6)]`, below the stationary lower benchmark. The
  note's restriction of that inequality to stationary entrance is necessary.
- The one-state near-perfect chain and the constant-hazard C4 case have zero
  correction and mean exactly 1/beta. A reducible two-state chain can have
  positive averaged hazard while never forming from one component. Scaling
  its symmetric motion rate as beta instead gives scaled means (2,3), not
  the common prediction 1/p=2, illustrating the lost separation of rates.
- Independent matching-polynomial and removed-vertex recursions check chi
  and both counting orientations on cycles of length 4,6,8 and the 4-by-4
  periodic square. The latter has Z=272, |Omega|=3712 and chi=29/17. These
  low-dimensional finite controls validate the identity and normalization,
  not Taggi's d>2 asymptotic theorem. On nontransitive P4 the origin sum is
  2 while |Omega|/(KZ)=3/2, showing why the fixed-origin identity needs the
  translation hypothesis.

No provisional mathematical defect was found. One tooling failure is
preserved: pdftotext was unavailable and the initial follow-up read therefore
failed. A successful pypdf extraction provided the authenticated PDF
statement pages; the complete paper proof was not thereby claimed checked.
