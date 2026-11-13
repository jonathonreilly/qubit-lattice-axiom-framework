# Independent check of partial terminal normalization and released gauge directions

Research gate completed, 2026-11-09. This is a same-provider fresh-context
mathematical check, not a formal audit, landing review, retained status, or
physical-gap result. The assigned supervisor profile is inherited without a
model or effort override. The concrete backend model identifier is not exposed.
The checker was given a bounded neutral brief and the frozen sources, not the
authors' private reasoning or another checker's conclusions.

## Source identity and scope

Worktree: `/Users/jonreilly/.codex/worktrees/su2-terminal-check/Physics`.
Assigned and observed HEAD: `4a3f6be4cf4ea0321bb5042c2969fc035479e7c2`.
All science paths below are relative to
`.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/`.

| Source | SHA-256 | Coverage |
|---|---|---|
| released-terminal-gauge-directions.md | a8271fb33178da46f747075f8b98f266cb06833ae900b99ef0544f36adcb403b | Complete proof |
| partial-terminal-normalization.md | 722e622dd64763e7f85461ef037f78810ec1c96d5bb71ddc7d60647c858b9867 | Complete proof; finite normalization, derivative, and cumulant identities checked |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 | Sections 1, 2, 5 |
| frozen-gaussian-producers.md | ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3 | Section 1; convention and claimed pinned bound only |
| full-connected-four-response.md | 04ef141738a356dd914608421a1d2cd135ff0f3cfbc1ac5f1ece81a71f0825c7 | Sections 1, 5, 6; exact law and stated scope only |

Instructions read: local AGENTS.md, SCIENCE_WORKFLOW.md, the supporting
physics-claim-reviewer skill, skill-freshness check, and proof-search governance.
The skill's relevant procedures were checked at assigned HEAD; its installed
copy was not used as an authority over this fixed research task. No Git
mutation or fetch was performed under the handoff's explicit restriction.
The local origin/main ref observed was
`bf92a1d763030836ed55631d5d7a7ef3b288f284`; this gate establishes no main/audit
status and makes no claim of live remote freshness. Parent supplied a passed
19:35 UTC preflight. No numerical job, external worker, or proof edit was run.
Only this report is written by the checker.

## Released-terminal proof: independently reconstructed argument

**Current result: the exact symmetry/Hessian statement is confirmed on its
stated finite, zero-source, identity-exterior domain.** This does not verify
the old quantitative response proof or a physical mass gap.

1. **Deletion and normalizers.** For each integrated terminal coordinate,
   conditional on U1, the entire normalized k1,e integrates to one against
   probability Haar. Hence the zero-source denominator is exactly q_u K0
   times the surviving k1,e factors. Overlap of path readers changes none
   of this conditional integration. No surviving radial denominator or
   q_u normalization may be omitted.
2. **Admissibility and covariance.** Let a terminal-component label prescribe
   one SU(2) element on each fine forest cell. It is constant on each fine
   tree, so simultaneous endpoint action on all hidden links preserves
   every tree value I. It is a fixed product of left/right translations on
   retained coordinates and preserves product Haar. Telescoping along each
   original path gives M -> k_x M k_y*. The real quaternion pairing and norm
   are invariant under this common left/right action. Both the first-layer
   numerator and its radial denominator are invariant because its output
   transforms too. At every surviving terminal edge k_x=k_y, its output I
   is fixed, and its mean is conjugated. Its full normalized factor is
   invariant. Fine plaquette traces are invariant. Thus the asserted group
   action preserves the actual sliced physical density, not just its value
   on the orbit through I.
3. **Stationarity.** Global simultaneous conjugation preserves each complete
   term and fixes identity. On each retained Lie-algebra factor it acts by
   all three-dimensional rotations. A differential invariant under all
   these rotations has zero restriction to each factor, so dS_H(0)=0.
4. **Kernel rather than scalar curvature: an independent Ward-identity
   derivation.** For fixed component Lie-algebra parameters let X(z) be the
   infinitesimal vector field of the slice action. Exact invariance gives
   dS_H(z)[X(z)]=0 for all z near 0. Differentiating in an arbitrary direction
   w at 0 yields Hess S_H(0)[w,X(0)]+dS_H(0)[DX(0)w]=0. The second term
   vanishes by stationarity, hence Hess S_H(0)v=0, where
   v_e=xi_component(b(x))-xi_component(b(y)). This checks the load-bearing
   implication without a positivity assumption. Merely showing v^T H v=0
   would fail: H=[[0,1],[1,0]], v=(1,0) has zero scalar curvature but Hv!=0.
   The supplied proof uses full invariance and so avoids that defect.
5. **Rank.** If all retained differences vanish, the differences on tree
   links also vanish because the label is constant on each tree. Therefore
   the fine-vertex label has zero difference on every nearest-neighbor edge
   of the connected fine torus, and is constant. Every terminal root is
   among these fine vertices. The only kernel of the map from the r
   component labels is thus the three-dimensional common constant label;
   its image has exactly 3(r-1) dimensions. Intermediate coordinates can
   increase the ambient dimension but cannot change this kernel argument.
6. **Coordinate Haar curvature.** The expansion sin(r)/r=1-r^2/6+O(r^4)
   gives -log[(sin(r)/r)^2]=r^2/3+O(r^4). Product Haar therefore contributes
   exactly (2/3)I to the coordinate Hessian, yielding the exact finite-u
   eigenvalue 2/(3u) on the above subspace. This value belongs to the
   negative log density in the chosen exponential coordinates. It is not
   curvature of the Haar-relative physical action and has no demonstrated
   identification with a physical mass.
7. **Witness and boundaries.** On the four-dimensional terminal torus with
   m>=3 the four incoming and four outgoing incident links at one vertex
   are eight distinct independent edges. Releasing them isolates that
   vertex in G_O, so r>=2 and there are at least three displayed directions.
   Their eigenvalues tend to zero as u tends to infinity; a fixed positive
   bound uniform in u cannot hold on this unchanged slice for all J. The
   canonical two-adjacent-plaquette union has seven edges. The eight-edge
   construction proves nothing about its complement's connectivity or its
   precision/decay constants. When r=1 the displayed subspace has dimension
   zero, which is neither coercivity nor the absence of other soft modes.

No false step, omitted normalizer, inadmissible action, or rank defect was
found in this proof. Its zero-source/identity-exterior setting is the domain
checked; arbitrary source tilts and backgrounds are not covered by this
symmetry argument. An adapted quotient and the quantitative seven-edge
denominator estimate remain separate research tasks.

## Partial-terminal normalization proof: independent finite-measure check

**Result: equations (P1)–(P7) are confirmed under their stated finite-model
hypotheses.** No decay estimate is supplied by this result. No mathematical
correction to the frozen second proof is required by this check.

### Exact conditional law and every normalization

Write w(H)=q_u(U0) K0(U1|U0) exp(sF(H)+tG(H)). The joint weight at fixed
exterior is w(H) product_O k1,e(V_e|U1) product_J k1,e(y_e|U1).
Integrating y first gives w product_O k1,e because the last product is a
conditional probability density, even when its path readers overlap. Its
normalizer is Q_J. Dividing the joint weight by Q_J instead, and factoring
it as [N_(y,V_O)/Q_J] times [w product_E2 k1,e/N_(y,V_O)], proves (P3)
pointwise and gives both required marginals. All factors from K0 and all
surviving last-level radial normalizers remain inside both laws. The q_u
normalization is carried until its common constant cancels in the ratio.

Normalizing the full joint terminal density by Z_glob and the exterior
marginal by the same Z_glob yields (N/Z_glob)/(Q_J/Z_glob)=N/Q_J exactly.
This cancels log Z_glob, not log Q_J. If F,G are fine-level functions, K0
integrates to one and Z_glob is the original Wilson source integral. For
general hidden sources exp(sF+tG) can depend on U1, so K0 cannot be dropped
from that integral. The proof states these cases correctly.

The finite compact model, positive kernels, finite couplings, and bounded
sources make all normalization integrals finite and positive. Terminal
kernel derivatives are bounded at fixed finite parameters; source
derivatives insert bounded F,G. Differentiation under the relevant integrals
is therefore justified. This uses no concentration, coercivity, or decay
claim from the earlier proof corpus.

### Independent response derivation by differentiation of normalized laws

For a differentiable density w_theta with score A=partial_theta log w,
quotient differentiation gives

    partial_theta E_mu B = E_mu(partial_theta B)+Cov_mu(B,A).

Introduce auxiliary independent parameters z_i multiplying fixed variables
B_i. Differentiate log integral w_theta exp(sum_i z_i B_i) first in theta.
For B_i independent of theta, taking its square-free z derivatives gives

    partial_theta kappa_mu(B1,...,Br)
        = kappa_mu(B1,...,Br,A).

If the B_i depend on theta, add one same-order cumulant for each differentiated
argument. Apply this elementary rule to partial_s partial_t log N=Cov_pi(F,G):
one c derivative inserts A_c, and the distinct d derivative inserts A_d.
There is no derivative-of-argument term because F,G are terminal independent
and partial_d A_c=0 for c!=d. This yields the numerator fourth cumulant in
(P5). The same argument for Q inserts both scores only when c,d are in O.
If either lies in J, Q is exactly independent of that output coordinate and
its mixed derivative is zero, despite possible nonzero source/exterior
derivatives of Q. Thus both branches of (P5), including one integrated and
one exterior derivative, follow directly. No assumption that Q is source
independent is used.

The output score is lambda_e<D_e V_e,M1,e>; the radial normalizer depends
only on U1 and contributes zero output derivative without disappearing from
the law. At identity and lambda_e=kappa u this is precisely (P4). Two
terminal derivatives on the same edge would also differentiate A_c, so
excluding repeated links is essential and is done explicitly.

### All fifteen total-cumulance terms by a different combinatorial route

This check uses moment partitions and their regrouping, rather than the
author's composition of two logarithmic generating series. Let I={1,2,3,4},
let M_D(Y)=E[X_D|Y], and let C_B(Y) be conditional joint cumulants. Conditional
moment inversion gives

    M_D = sum_(pi partition D) product_(B in pi) C_B.

Use the ordinary finite moment formula for the unconditional cumulant:

    kappa_rho(X_i:i in I)
      = sum_(sigma partition I) mu(sigma)
          product_(D in sigma) E_p M_D,
    mu(sigma)=(-1)^(|sigma|-1)(|sigma|-1)!.

After substituting the conditional moment inversion, each summand determines
a fine partition pi of I (the union of the partitions inside the D blocks)
and a coarsening sigma of pi. Fix pi. Coarsenings sigma are exactly partitions
tau of the finite set of blocks of pi. Hence all terms with this pi sum to

    sum_(tau partition pi) (-1)^(|tau|-1)(|tau|-1)!
       product_(A in tau) E_p product_(B in A) C_B
       = kappa_|pi|,p(C_B:B in pi).

This is an exact finite reordering of sums. It proves the displayed total
cumulance identity, with no analytic conditional-limit issue and no
assumption about source or reader separation. The moment-cumulant inversion
used here follows recursively from the same finite partition formula
(the one-block term isolates the highest cumulant); it introduces no
independent conditioning theorem as an unverified premise.

The complete fine partitions are:

| Block sizes | Partitions | Resulting outer operation |
|---|---|---|
| 4 | 1234 | E C_1234 |
| 3+1 | 123\|4; 124\|3; 134\|2; 234\|1 | Four covariances of a conditional third cumulant and a mean |
| 2+2 | 12\|34; 13\|24; 14\|23 | Three covariances of conditional covariances |
| 2+1+1 | 12\|3\|4; 13\|2\|4; 14\|2\|3; 23\|1\|4; 24\|1\|3; 34\|1\|2 | Six third cumulants |
| 1+1+1+1 | 1\|2\|3\|4 | Fourth cumulant of conditional means |

Each partition appears once with coefficient one when expressed as an outer
cumulant. These fifteen entries match (P6) term by term. The underlying
moment signs and multiplicities are contained in each outer cumulant, not
silently discarded. Distinct labels remain distinct when the random
variables coincide.

**A bounded discriminator against dropping the conditional-covariance terms.**
Take Y equally likely 1 or 2, and X conditionally equally likely +Y or -Y.
Set all four labelled X_i=X. The conditional means and third cumulants
vanish, C_2=Y^2, and C_4=-2Y^4. Thus E C_4=-17,
Var(C_2)=9/4, and the full fourth cumulant directly from unconditional moments
is E X^4-3(E X^2)^2=17/2-3(5/2)^2=-41/4.
The three 2+2 terms restore -17+3(9/4)=-41/4. Dropping them would give -17,
which is false. This four-state bounded-law example tests the algebraic
conditioning identity, not an additional physical model premise. It also
checks the equal-function/independent-label convention.

For the actual denominator c,d must be exterior coordinates so that the four
random variables are fixed functions of H while conditioning on Y=V_J.
The author imposes exactly that restriction. The disintegration then says
the unconditional cumulant is under rho_J and the outer law is the full
source-dependent p_J. In particular, at y0=I_J the response is the conditional
fourth cumulant at y0 minus every term in (P6); it is not merely that
conditional fourth cumulant minus its outer expectation. The integration
in (P6) still ranges over the complete released compact group domain.

### Endpoint and original-source checks

- J empty: Q=N, p=1 on the empty terminal product, and rho=pi. Formula (P5)
  subtracts identical cumulants. Y is constant, so every outer cumulant of
  order two or higher vanishes and (P6) reduces to the same fourth cumulant.
- J all terminal edges: Q=Z_glob, independent of every terminal coordinate.
  Formula (P5) has only its numerator term. There are no surviving terminal
  scores to which the denominator specialization of (P6) applies, although
  the general conditioning identity remains valid for other fixed variables.
- A zero relevant coupling gives a zero score and hence zero distinct-link
  mixed response. F=G, overlapping readers, constant arguments, and bounded
  measurable noninvariant sources cause no algebraic exception. Fewer than
  two terminal coordinates makes the distinct-link assertion vacuous.
- The original forest map is independent of sources and terminal parameters.
  For arbitrary original sources it gives the exact conditional orbit factor
  A_st(a)=integral exp(sF(a,h)+tG(a,h))dh and conditional density eta_st.
  Because the unsourced density is root-fixed-gauge invariant, this factor
  multiplies both the fixed-terminal and released-terminal quotient weights.
  It cannot in general be replaced by exp(s E_h F+t E_h G). Differentiating
  its logarithm gives Cov_eta(F,G), reducing to the Haar conditional orbit
  covariance at zero sources. Terminal integration removes normalized output
  kernels, not this source covariance or the source dependence of p_J.

No mismatch was found between these exact laws and the necessary premises
read from compact-forest-exchange §§1,2,5 and full-connected-four-response
§§1,5,6. The separately cited one-step note was not needed as a quantitative
premise: this gate verifies the finite identities directly from the explicit
normalized-kernel hypotheses restated in the draft. Its content and hash
have not been independently authenticated by this gate.

## Proof-map scope check and resolved finding

The parent additionally authorized a complete read of PROOF_TREE.md after
the mathematical checks, limited to consistency with the checked material;
the twenty old suppliers were not rederived. The first map read had SHA-256
`7087555604768632d963986f78b255f35c8ceb5f6a91f04cec0d1fadfe472da8`.

One narrow scope omission was reported: the map's residual-gauge eigenvalue
summary did not explicitly retain the theorem's zero-source and V_O=I
hypotheses. This is a meaningful qualifier. For example, a bounded smooth
quotient singlet F(a)=w(a_e)=cos|z_e|, with e crossing terminal components,
adds -sF to the negative log tilted density; its Hessian adds s times the
coordinate projection at e. A displayed gauge vector with v_e nonzero
then need not retain eigenvalue 2/(3u). The proof itself already stated the
correct domain; no proof correction was requested.

The parent restored the qualifier and updated the two new nodes' check
metadata. The complete revised map was then read at SHA-256
`d6073b88bcde640ec558c90f261d4a53c8eba79383a581d9367ad3b89ee5a812`.
Its lines 129–132 now explicitly state zero sources and V_O=I before the
component count and eigenvalue. The new check-completed entries and report
link accurately describe this gate and do not assert retained status. The
map keeps the seven-edge denominator bound open, distinguishes the eight-
edge witness, and marks the route toward iteration, continuum construction,
and a physical spectral gap as proposed dependencies with open hypotheses.
No remaining scope mismatch was found against the material checked here.

The parent also added the eventual positive-finite-mass target wording and
reported visual inspection of the official problem statement and of
Brillinger's primary conditioning paper. This gate does not independently
authenticate those external inspections. The finite proofs above do not
rely on them. The map's summaries of prior quantitative suppliers and prior
gate history remain carried records, not newly certified by this report.

## Final finding and verification limits

Both supplied proposals are mathematically confirmed within their explicit
finite-model domains at the source hashes above. The new independent content
of this gate is the Ward-identity Hessian-kernel derivation, the direct
normalized-law derivative check, and the finite moment-partition regrouping
of all fifteen conditioning terms, including a bounded omission witness.
No scientific defect requiring a source edit was found.

The exact remaining quantitative obligation is a uniform estimate for the
released-terminal denominator cumulant (or for the complete outer terms and
conditional laws that reconstruct it), for the specified seven-edge
geometry and admitted source class. An identity-terminal numerator bound
alone does not provide such control at all released backgrounds. The
unchanged-slice eight-edge gauge witness does not decide the seven-edge
case. These are open obligations, not evidence of a no-go or physical
gaplessness. Arbitrary backgrounds, repeated blocking, and physical continuum
identification are not certified here.

This is same-provider checking with shared mathematical inputs; fresh context
and a different derivation reduce but cannot eliminate correlated errors.
No outside-provider gate was available in this bounded task. The old
quantitative estimates, dependency closure, main status, author model metadata,
and literature attribution beyond the supplied text were not independently
verified. No formal audit, landing operation, physical-axiom edit, editable
prompt change, numerical job, or public posting was performed.

Final source recheck: all five proof/premise hashes above remained unchanged.
Finalized UTC: 2026-11-09T19:55:06.887950+00:00.
