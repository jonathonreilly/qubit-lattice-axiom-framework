# Last-pair clock and monomer ratio: bounded independent check

**No unresolved mathematical defect or required source correction was found.**
The fixed-graph joint clock/exit limit, exact Schur-complement mean, first
correction and monomer-counting identity reconstruct. The volume bound uses
an explicitly imported equilibrium theorem: its statement and application
hypotheses were verified, not its entire proof. This is scientific scrutiny,
not an audit, retained-status or landing decision.

The preceding rare-birth F1 wording correction is separately closed in
`../geometric_rare_birth_independent/F1_ACK.json`, SHA-256
`7406f50284d8397923199e9b81bd4942c8618595f84598e181cae7bd4b52a77e`.
Its inverse replacement recovers the old source exactly; the previous report,
seal and all nineteen review artifacts are unchanged. No theorem was rerun
for that acknowledgment.

## Reconstructed claims

On the finite irreducible near-perfect matching space, the conservative
generator S is fixed and symmetric, pi is uniform, and p=pi(h)>0. First-step
conditioning for the unique final birth and discount s beta gives
`[-S+beta(H+sI)]u=beta a_F`. The probability vector is bounded. Any
subsequential beta-down-to-zero limit is S-harmonic and hence constant;
averaging the exact equation determines it as

    pi(a_F)/(p+s) = (1/Z) p/(p+s).

The finite set of entrances and exits makes convergence uniform over
entrance laws, including beta-dependent ones. Laplace uniqueness gives the
joint limit: beta tau is Exp(p), independent of a uniform full matching.
The clock starts on first reaching the two-vacancy level. It is not the
total empty-start clock, a fixed-physical-time limit, or finite-beta
independence.

For the mean, write L=-S and `t=c 1+v`, with pi(v)=0. Centering the mean
equation gives `v=-beta c R_beta q`; averaging gives
`beta c(p-beta C_beta)=1`. Thus the source's exact formula is correct:

    t(M)=[1-beta(R_beta q)(M)]/[beta(p-beta C_beta)].

L+beta H is positive definite, and its scalar Schur complement is
`beta(p-beta C_beta)>0`. The centered inverse remains bounded at each fixed
graph. Expanding it at zero gives, uniformly over that finite state space,

    E_M tau=1/(beta p)+C_0/p^2-(R_0 q)(M)/p+O(beta).

This establishes mean convergence separately from weak convergence. The
one-state case and constant hazard have mean exactly 1/beta and no centered
correction. The stationary-start lower bound follows both from C_beta>=0
and independently from Jensen's inequality applied to stationary integrated
hazard. It need not hold for each individual initial state, as the note
correctly states.

For the even cubic torus, every near-perfect matching has one even vacancy
and one odd vacancy. Counting it once with that ordering and using
translations within the even sublattice gives

    |Omega| = sum_(u even,v odd) Z(u,v) = K Z chi,
    p=K Z/|Omega|=1/chi,                  K=V/2.

Counting both hole orientations would double |Omega|. For a nearest neighbor
v of 0, insertion of the absent edge is a bijection to full matchings
containing that edge. Cubic symmetry gives Xi(v)=1/(2d), so the adjacent
terms sum to one. Under uniform near-perfect equilibrium conditioned on a
vacancy at 0, the other has law Xi(v)/chi. This equilibrium law is not
silently assigned to a finite-rate birth-event sample.

## External import and the ordered volume consequence

[Taggi, arXiv:1909.06558v3](https://arxiv.org/html/1909.06558v3), definitions
and Theorem 2.1/Eqs. (2.3)-(2.5), were checked in the primary HTML and the
authenticated PDF. They concern unweighted full matchings on even periodic
nearest-neighbor cubic tori, include all matching sectors, and require
integer d>2. The ratio removes precisely the two specified vertices. The
average in Eq. (2.3) is over the odd sublattice; r_d counts returns at strictly
positive times. Eq. (2.5) supplies the stated pointwise upper bound. The
axis-separation statement requires the theorem's fixed margin, sufficiently
large even side and odd separation below its side-scale cutoff.

Since K/V=1/2, the stated bounds convert to

    (1-r_d/2)/(4d) <= liminf chi_N/V
                     <= limsup chi_N/V <= 1/(4d).

The factor of two and the return-count convention are correct. The local
PDF has SHA-256
`50a6f8a42cd5865a509efb706823e2dd0061233f49e6ec06d5395a627c1d2517`.
Definitions and statements were inspected on PDF pages 3-6; the archival
version page and HTML formula cross-check are recorded in
`LITERATURE_READ_RECEIPT.json`. The full reflection-positivity proof and
the earlier site-monotonicity proof behind Eq. (2.5) were not independently
verified.

Combining that import with the independently checked identity and clock
theorem bounds the ordered mean coefficient: beta tends to zero at each
fixed N, then N grows through even sides. It does not prove that chi_N/V
converges, a simultaneous/fixed-rate volume law, or an upper bound on the
whole growth time. Conservative relaxation and p may deteriorate with N.
The source preserves these qualifications and makes no quantum, physical-charge,
Gaussian-field, mixing, phase or wave identification.

## Decisive independent evidence and countercontrols

The blind checker imports only this reviewer's previously sealed matching
primitives. Exact C4 and C6 joint transforms agree with the proposed limit
for every entrance and target. Derivatives at zero give beta times the
independently solved mean, checking the time normalization. On C4 the
waiting time is exactly exponential at finite beta, but one joint transform
differs from the product of its marginals by a rational function that is
strictly positive for beta,s>0. Finite-beta clock/exit independence is
therefore not inferred.

On the full 44-state near-perfect cube, the independent centered inverse
gives p=9/11, C_0=30/1331 and stationary first correction 10/297. The three
mean classes have corrections -1/27, 1/54 and 5/27, with multiplicities
12,24,8. The exact three-class means were lifted and verified in every
original mean equation, and full-matrix Schur checks agree at beta=1/2 and
1/10. In particular, a parallel three-edge start has mean

    11/(9 beta)-2/[9(beta+6)],

strictly below 1/(beta p). This validates the source's stationary-entrance
qualification. Reducible and collapsing-motion-rate two-state examples
respectively invalidate automatic absorption and the common exponential
limit when the fixed irreducible generator hypothesis is removed. They
are general-chain countercontrols, not growing-cubic-torus claims.

Independent matching-polynomial and removed-vertex recursions verify the
counting identity and both hole orientations on cycles of length 4,6,8
and the 4-by-4 square torus. The square has Z=272, |Omega|=3712 and chi=29/17.
On nontransitive P4 the fixed-origin sum is 2 while |Omega|/(KZ)=3/2,
demonstrating the translation qualification. These low-dimensional finite
controls do not validate Taggi's d>2 asymptotic theorem numerically.

## Source comparison and provenance

The complete 158-line note was read before the author checker/results.
Independent derivation and controls were frozen in `PRE_COMPARISON_SEAL.json`,
SHA-256 `41eb0f77e2296e6182073e9d27b1e29a7f63797a9c7e9754c8284dc05396dce4`.
All eleven pre-comparison artifacts remain unchanged. The complete 121-line
author checker and all requested results/logs were then inspected.

No code/prose drift was found. The three recorded author groups match the
complete stdout, with empty stderr and all four source bindings authenticated.
A separate comparison checker confirmed the additional scalar first/second
moment limits by differentiating the transform, matched all cube mean/error
receipts using the already independently reconstructed symbolic means, and
recomputed every reported origin monomer ratio using the separate recursion.
The author runner was neither imported nor executed. Authenticating its
log is distinguished from these independent calculations.

| Frozen primary source | SHA-256 |
|---|---|
| `GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md` | `0f5c6bdb5ce0c2ac3e7aa32bef5dfe57e1de0f914c81af984e4195d92722ebd7` |
| `geometric_last_pair_clock_check.py` | `60eae29b78c46d04fff388d7d4eba6b918fabe0669625c8a61239ef541c21e38` |
| Corrected rare-birth prerequisite | `bb01519ad5a072da32a1d53075048a847a9a3c2675b9874327cb94ab496d1e1e` |
| Geometric-partner prerequisite | `1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969` |

Parent-supplied recovery commit `4d6a7634bd13487bb30ddfcfd51fdaefc01f0530`
was not queried with Git. `FINAL_SEAL.json` records every source, dependency,
procedure and review artifact, including the externally located PDF identity.
No production diagnostic or unrelated primary source was read, and no
primary file, prompt, Git state or audit status was changed.

Reproduce from this directory:

```
python3 independent_check.py --out INDEPENDENT_RESULTS.json
python3 comparison_check.py --out COMPARISON_RESULTS.json
```

All mathematical runs passed on their first attempt; full receipts and
stdout/stderr are present. An unavailable-pdftotext extraction attempt and
its failed follow-up read are preserved; pypdf then supplied the authenticated
statement pages. Reproducing the source-binding check requires the frozen
source paths or an explicit path adaptation. Detailed proof reconstruction
is preserved in `PRE_COMPARISON_DERIVATION.md`.
