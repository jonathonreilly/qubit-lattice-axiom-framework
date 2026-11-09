# Partial terminal normalization and the complete fourth cumulant

Pure-proof author draft, 2026-11-09. Finite-model identities below are derived
here; independent checking and retained status are not asserted. The assigned
scope is two blocking steps, arbitrary subsets of terminal links, and distinct
terminal differentiation coordinates. No decay theorem is proved here.

## 1. Source identities and premises

Assigned detached source revision: `4a3f6be4cf4ea0321bb5042c2969fc035479e7c2`.
SHA-256 identities of the mathematical inputs read:

- `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`
  §§1–2: `94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c`.
- `parts/full-connected-four-response.md` §§1,5,6:
  `04ef141738a356dd914608421a1d2cd135ff0f3cfbc1ac5f1ece81a71f0825c7`.
- `parts/compact-forest-exchange.md` §§1,2,5:
  `b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2`.

The latter two paths are relative to this pack. The first supplies normalized
Haar kernels and the one-step conditional convention; the second supplies the
two-step law and distinct-link score; the third supplies compact forest
coordinates and the exact source-dependent orbit law. Their quantitative
estimates are not premises of this derivation.

Let H=(U0,U1) range over the finite hidden product of SU(2), with probability
Haar dH. Use the supplied original Wilson weight q_u(U0), with no intermediate
Wilson action, and the complete normalized first kernel K0(U1|U0). For every
terminal edge e in E2, put

    k1,e(V_e|U1) = exp(lambda_e <V_e,M1,e(U1)>)/Z(lambda_e |M1,e(U1)|).

All lambda_e are finite and nonnegative; the response source uses
lambda_e=kappa u. Every displayed kernel includes its input-dependent radial
normalizer. F(H),G(H) are bounded real measurable functions independent of V;
no separation, gauge invariance, or quotient measurability is assumed. Real
sources s,t are finite. Compactness, positivity and boundedness justify Fubini
and every finite derivative below, locally uniformly in the real parameters.

Write b_st(H)=q_u(U0) exp(sF(H)+tG(H)) K0(U1|U0). For J subset E2 set
O=E2\J; V_O is held when defining the conditional density of V_J. Define

    N_V(s,t) = integral b_st(H) product_(e in E2) k1,e(V_e|U1) dH,
    Q_J(V_O;s,t) = integral N_(v_J,V_O)(s,t) dv_J,
    p_J(v_J|V_O;s,t) = N_(v_J,V_O)(s,t)/Q_J(V_O;s,t).

By integral k1,e(v|U1) dv=1, one factor at a time,

    Q_J = integral b_st(H) product_(e in O) k1,e(V_e|U1) dH.       (P1)

This deletion applies to the entire integrated output kernel, numerator AND
normalizer together. It never deletes an input normalizer of a surviving
kernel. All K0 factors, all source factors and all terminal kernels in O
remain in (P1).

Define probability laws on the same hidden space:

    pi_V;st(dH) = b_st(H) product_E2 k1,e(V_e|U1) dH / N_V,
    rho_J;st(dH) = b_st(H) product_O k1,e(V_e|U1) dH / Q_J.       (P2)

For every fixed V_O the following joint-measure equality proves the actual
posterior disintegration, rather than a separately chosen marginal:

    rho_J;st(dH) product_J k1,e(v_e|U1) dv_J
          = p_J(v_J|V_O;s,t) dv_J pi_(v_J,V_O);st(dH).           (P3)

In particular rho_J;st = integral p_J(v_J|V_O;s,t)
pi_(v_J,V_O);st dv_J. The mixing weights depend on both sources.

To make global normalization explicit, let

    Z_glob(s,t) = integral N_V(s,t) dV = integral b_st(H) dH.

The normalized joint terminal density is N_V/Z_glob and its exterior density
is Q_J/Z_glob. Their ratio is exactly p_J=N_V/Q_J. Thus both occurrences of
log Z_glob cancel BEFORE differentiation. One must still subtract log Q_J;
global cancellation does not make Q_J source- or exterior-independent. A
constant normalization already included in q_u cancels in the same ratio.
If F,G depend only on U0, normalization of K0 gives
Z_glob=integral q_u(U0) exp(sF(U0)+tG(U0)) dU0, the original Wilson source
integral in the chosen q_u convention. This reduction is not asserted for
general sources on U1.

## 2. Complete distinct-terminal response

For a tangent curve V_e(epsilon) with V_e(0)=V_e, define
A_e(H;V_e)=D_e log k1,e(V_e|U1)=lambda_e <D_e V_e,M1,e(U1)>.
It is independent of s,t and of all other terminal coordinates. At V_e=I
with V_e(epsilon)=exp(i epsilon v_e dot sigma_Pauli), this is exactly

    A_e(H;I)=kappa u <i v_e dot sigma_Pauli,M1,e(U1)>,            (P4)

the R2 score. The radial factor is retained in the measure; it gives zero
output derivative because it depends only on the input.

For any normalized integral whose logarithmic weight has independent linear
source insertions F,G and separate terminal coordinates c!=d, its mixed
(s,t,c,d) logarithmic derivative is kappa_4(F,G,A_c,A_d). Indeed, give each
coordinate an independent increment. In the coefficient square-free in the
four increments, the exponent is their linear combination: nonlinear terms
in any one terminal increment cannot contribute. The logarithm of the
normalized exponential moment has precisely the joint-cumulant coefficient.
This argument also shows why D_d A_c=0 and terminal-independent F,G matter.

Consequently, at any base s,t,V, with the scores evaluated there,

    D_c D_d partial_s partial_t log p_J
      = kappa_4,pi_V;st(F,G,A_c,A_d)                  if {c,d} meets J,
      = kappa_4,pi_V;st(F,G,A_c,A_d)
          - kappa_4,rho_J;st(F,G,A_c,A_d)            if c,d are both in O. (P5)

In the first case Q_J is independent of the integrated coordinate, so its
mixed coefficient is zero even when the other coordinate lies in O. This
is not a claim that its source derivatives vanish. In the second case both
scores are surviving kernels' scores in rho_J. At (V,s,t)=(I,0,0), (P4)
gives the requested identity-terminal specialization. Repeated-link
second derivatives contain derivative-of-score terms and are excluded.

## 3. Full law of total cumulance at order four

Fix s,t,V_O and distinct c,d in O. Under the joint law (P3) let Y=V_J,
and take the FOUR FIXED hidden random variables

    (X1,X2,X3,X4)=(F,G,A_c(.;V_c),A_d(.;V_d)).

Here "fixed" means that auxiliary cumulant parameters do not change these
functions or the base laws. They are not projected means substituted for
original observables. Their unconditional hidden law is rho=rho_J;st and
the conditional hidden law given Y=y is pi_y=pi_(y,V_O);st. Outer expectations
and cumulants below use p=p_J(.;V_O;s,t).

For every nonempty B subset {1,2,3,4}, define the conditional cumulant
C_B(y)=kappa_pi_y(X_i:i in B); write m_i=C_{i} and C_ij,C_ijk,C_1234
for the corresponding quantities. Joint cumulants are defined by

    kappa_mu(Z1,...,Zr)
      = partial_(z1)...partial_(zr)
          log E_mu exp(sum_i z_i Zi) evaluated at z=0.

Thus kappa_1 is expectation, kappa_2 is covariance, and higher cumulants
include all partitions with their signs. Equivalently,

    kappa_mu(Z1,...,Zr)
      = sum_(P partition of {1,...,r})
          (|P|-1)! (-1)^(|P|-1) product_(B in P) E_mu product_(i in B) Zi.

Labels remain distinct even if two random variables are equal. The complete
identity is

    kappa_4,rho(X1,X2,X3,X4)
      = E_p C_1234
      + Cov_p(C_123,m4) + Cov_p(C_124,m3)
      + Cov_p(C_134,m2) + Cov_p(C_234,m1)
      + Cov_p(C_12,C_34) + Cov_p(C_13,C_24) + Cov_p(C_14,C_23)
      + kappa_3,p(C_12,m3,m4) + kappa_3,p(C_13,m2,m4)
      + kappa_3,p(C_14,m2,m3) + kappa_3,p(C_23,m1,m4)
      + kappa_3,p(C_24,m1,m3) + kappa_3,p(C_34,m1,m2)
      + kappa_4,p(m1,m2,m3,m4).                                  (P6)

These are exactly the 15 set partitions: one of type 4, four of type 3+1,
three of type 2+2, six of type 2+1+1, and one of type 1+1+1+1. In
particular "averaged conditional fourth cumulant plus fourth cumulant of
means" omits thirteen terms, including covariance of conditional covariances.

Proof without importing a conditioning theorem. Introduce four independent
auxiliary variables z1,...,z4 and let

    H_y(z)=log E_pi_y exp(sum_i z_i Xi).

All Xi are bounded at the fixed finite parameters. The conditional moment
series and its logarithm converge uniformly for sufficiently small z: the
moment generating function is uniformly close to 1 there. Conditional
expectation can therefore be interchanged with the finite coefficient
operations. Disintegration gives

    log E_rho exp(sum_i z_i Xi)=log E_p exp(H_Y(z)).              (P7)

The coefficient of z_B=product_(i in B) z_i in H_y is C_B(y), with no
factorial, since each label occurs once. Terms containing a repeated z_i
can never contribute to z1 z2 z3 z4 in subsequent products. Also H_y(0)=0.
Expand the right side of (P7), treating H_Y(z) as a single bounded random
variable with zero constant term:

    log E_p exp(H_Y(z))
      = sum_(r>=1) (1/r!) kappa_r,p(H_Y(z),...,H_Y(z)).

Only r<=4 contributes to the square-free fourth coefficient. By
multilinearity, a contribution consists of an ordered list of r nonempty,
pairwise disjoint blocks B1,...,Br covering {1,2,3,4}, with value
kappa_r,p(C_B1,...,C_Br)/r!. Each unordered set partition has exactly r!
orderings, and cumulants are symmetric, so that coefficient equals

    sum_(P partition of {1,2,3,4}) kappa_|P|,p(C_B:B in P).

The left side coefficient is kappa_4,rho by definition. Enumerating the
partitions yields every term in (P6), proving the identity. This coefficient
argument also proves the displayed moment-partition convention, by expanding
log(1+(E exp(sum z_i Zi)-1)): the r-th log term has coefficient
(-1)^(r-1)/r and the r! ordered block lists give (-1)^(r-1)(r-1)!.

Credit and search record: David R. Brillinger, "The Calculation of Cumulants
via Conditioning" (1969), is the primary published source for the general
conditioning identity ([primary PDF](https://www.ism.ac.jp/editsec/aism/pdf/021_1_0215.pdf)).
The targeted source URL was opened during this task; text extraction returned
no readable lines. Its theorem text is therefore not asserted as inspected.
The proof (P7) above is self-contained, not an acceptance of an unchecked
citation. The specified repository sources were searched by their requested
sections; their closest results are total covariance and R24, rather than
the enumerated four-variable law. Parent-level route-search records and
independent review remain outside this bounded worker's deliverable. No
novelty claim is made for the conditioning identity.

Combining (P5) and (P6), when c,d are in O the response at a specified y0 is
C_1234(y0) minus the ENTIRE right side of (P6). This is a pointwise
conditional cumulant minus an unconditional cumulant, not merely its
fluctuation around E_p C_1234. At V=I, y0=I_J and V_O=I_O, the outer
integral nevertheless ranges over every y in SU(2)^J.

## 4. Endpoints, source law, and remaining quantitative task

For J empty, Q_empty(V;s,t)=N_V(s,t). The conditional terminal space is a
one-point empty product, p_empty=1, and rho_empty=pi_V. Every pair c,d is
in O, so (P5) gives zero by exact subtraction. In (P6), Y is constant;
all outer cumulants of order at least two vanish and the first term equals
the unconditional cumulant, as required.

For J=E2, O is empty and Q_E2=Z_glob. Every distinct terminal pair is in J,
so only the numerator cumulant appears in (P5). If F,G depend only on U0,
Q_E2 is exactly the original Wilson source integral derived in §1.
For general hidden sources it remains integral q_u exp(sF+tG) K0 dU0 dU1.
Formula (P6) as applied to retained-kernel scores has no c,d in O in this
endpoint; the general conditioning theorem remains true for any four fixed
hidden variables. With fewer than two terminal edges, the distinct-pair
response assertion is simply vacuous. Zero couplings give zero corresponding
scores and hence zero response, consistent with (P5).

Overlapping sources and F=G are allowed: labels in the generating functions
are distinct even when functions coincide. Noninvariant sources also need
no modification of (P1)–(P7). In the forest coordinates of the compact input,
the exact orbit source factor is

    A_st(a)=integral exp[sF(a,h)+tG(a,h)] dh,
    eta_st(dh|a)=exp[sF(a,h)+tG(a,h)] dh/A_st(a).

It remains inside every quotient numerator and marginal. In general it is
not exp[s integral F dh+t integral G dh]. Its mixed logarithmic derivative
is Cov_eta_st(F,G); at zero sources this is the Haar conditional orbit
covariance, which may be nonzero for overlapping orbit readers. Integrating
terminal variables does not justify removing it. This statement concerns
the exact source law; the weaker regularity needed here (bounded sources)
does not assert the quantitative C^2 estimates from the input note.

The unresolved quantitative task is to control the rho_J cumulant and/or
all the outer terms in (P6) uniformly in the desired parameters and geometry.
An identity-terminal estimate for pi_I alone does not control pi_(y,I_O)
for released y over its full integration domain; nor does it bound the
outer cumulants of conditional means/covariances. Those are exact missing
estimates, not evidence that they cannot be proved. This note claims no
uniform decay, no no-go theorem, no physical mass gap, and no continuation
to unbounded depth. It closes the finite-model normalization and conditioning
algebra under the stated hypotheses.

## 5. Worker checkpoint and verification limits

Only this deliverable was changed. No Git writes, numerical job, editable
prompt changes, audit operations or public posting occurred. The parent
reported preflight passed at 19:35 UTC; this task uses the shared host rather
than a new sandbox and launches no worker or numeric job. Provenance supplied
by parent: host subagent, `fork_turns=none`, `reasoning_effort=medium`, model
inherited with no override; concrete model identifier is not exposed and is
unknown. Lower effort was explicitly authorized by the user. Source HEAD was
checked against the assigned revision. Author checks consist of the explicit
coefficient proof, endpoint checks and all 15 partition terms above; these
are not an independent proof check. Parent review and a fresh-context check
are pending. No mathematical step in the stated exact identities is left
as an assumed lemma beyond the explicitly supplied finite normalized model.
