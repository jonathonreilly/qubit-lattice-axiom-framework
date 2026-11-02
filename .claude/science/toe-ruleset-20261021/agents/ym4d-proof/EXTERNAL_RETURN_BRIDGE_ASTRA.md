# External stopping-scale comparison and the original-law return

**Author literature bridge, pending independent review.** The 27 October
Cauchy draft in MathePhysics/4D_Wilson_Loop_RG supplies a concrete accounting
scheme for positive whole-integral large-field weights at a fixed stopping
volume. Its section 11 replaces an earlier *fixed-exterior* quotient by that
whole-volume comparison; it does not prove the earlier quotient. Neither
statement has been identified with our normalized Wilson/Decision-4 return
at fixed original data and unchanged history.

The useful transfer is the allocation of history costs before entropy,
together with carrying unnormalized marked kernels until their terminal
use. The external mixed-domain argument still requires the interacting
localization estimate that our return also needs. This is a comparison of
specified interfaces, not a verdict on the external programme or a theorem
that any return construction is impossible. Full four-dimensional SU(N)
continuum existence and the physical continuum mass gap remain **OPEN**.

    actual_current_surface_status: open
    target_claim_type: open_gate
    trace_class: upstream_support
    reachability_to_target: supports
    artifact_role: literature_bridge
    independent_review: pending
    conditional_surface_status: null
    hypothetical_axiom_status: null
    admitted_observation_status: null
    claim_type_reason: primary-source hypothesis map; no gauge theorem imported
    audit_required_before_effective_retained: true
    bare_retained_allowed: false

## 1. Sources, target and reading boundary

The external repository is the programme of Martin Peev and Akshunna S.
Dogra. Its [pinned README](https://github.com/MathePhysics/4D_Wilson_Loop_RG/blob/70d9a772fc9c7b47e36fd5e384fe42e07e7ccded/README.md)
distinguishes author judgments, generated drafts, verification qualifications
and open targets. Those status labels locate the argument; they are not our
mathematical evidence. The actual arguments read below determine this map.

All external reads are pinned to commit
70d9a772fc9c7b47e36fd5e384fe42e07e7ccded, committed 2026-10-29 11:56:26 UTC.
The full UTF-8 bytes were obtained through read-only GitHub connector calls
and checked against the Git-tree blob identities. Exact SHA-256 hashes,
original line windows and limits are in the
[receipt](checks/external_return_bridge_receipt.json).
Complete third-party sources and PDFs are not included in this packet.

- [Cauchy estimate, section 11](https://github.com/MathePhysics/4D_Wilson_Loop_RG/blob/70d9a772fc9c7b47e36fd5e384fe42e07e7ccded/drafts/WILSON_IT1_CAUCHY_ESTIMATE_2026_10_27.md#L891-L944):
  blob 82f7bd9b9b147096d2a2a78f207750257f18de5c; all of section 11(a–d),
  its opening assumptions, and its source inventory were read.
- [Continuum note, section 7](https://github.com/MathePhysics/4D_Wilson_Loop_RG/blob/70d9a772fc9c7b47e36fd5e384fe42e07e7ccded/drafts/WILSON_IT1_CONTINUUM_LIMIT_CLOSURE_2026_10_26.md#L90-L114):
  blob e66d0b34f9bb5c7fa5f51ffe6d6cd9b60837b9f4; this identifies the
  earlier residual local quotient and the margin it lacked.
- [Large-field gamma note, sections 16 and 18–23, selected windows](https://github.com/MathePhysics/4D_Wilson_Loop_RG/blob/70d9a772fc9c7b47e36fd5e384fe42e07e7ccded/drafts/WILSON_IT1_LF_GAMMA_REPAIR_ATTEMPTS_2026_10_28.md#L1154-L1673):
  blob 5c129d4e65723be6ac6750177bc32a0ee4ed06aa. The complete sections
  16, 18–21 and 23, section 12.1 and section 22.8 were read. The full
  Gaussian derivation in sections 22.1–22.7 was not reviewed.
- The external Bałaban-label dictionary was read for bibliography only.
  This pass did not read or certify the original Bałaban theorem proofs,
  the external D2.6/D2.7 induction, its other drafts, or its full repository.

One provenance qualification matters: the gamma note names a *starting*
Cauchy SHA-256 8f7a3e6cc5c78419326fd1a650b1c18c485e8d61cdf94f353b664ec5c9ef5c34.
The Cauchy bytes at our pinned commit instead hash to
8b42e1e7397aedd3145e20e5388f3d8518f060765f15c76f7165d6f05aaad2d7.
Consequently this pass makes no claim that the cross-note dependency was
reviewed at one common source identity. The mismatch is provenance evidence,
not by itself a mathematical defect.

The local consumer is [RD4](RD4.md), equations (4.1)–(4.2), sections 3–6:
N>=2, original Wilson coefficient sources, fixed real kernel parameters,
the exact Haar chain, all retained failure/completion readers, and

    D_h(z)=O_h(z)^(-1) integral chi_B Xi_h W(z,x) dmu(x),
    N_h(z)=O_h(z)^(-1) integral zeta_B Xi_h W(z,x) dmu(x).

The required logarithm has connected *full original-reader* supports,
including inactive and source-only readers, and a fixed original-source
radius on the specified complex coarse domain, uniformly in the admitted
volume/level/history family. RD4 also distinguishes these local quotients
from its fully integrated R_h/Z_A and terminal reference-weighted objects.
A bound for one is not a bound for the others. Zero-reference histories
are never divided by their mass.

[Outside-chart return](OUTSIDE_CHART_RETURN_ASTRA.md), especially OC23–OC32,
provides real comparisons and raw complex envelopes at its stated domains.
[Shifted-chart return](SHIFTED_CHART_RETURN_ASTRA.md), SC19–SC22 and section 8,
provides mixed Gaussian prices and partial reader decorations; it explicitly
retains the covariance-reader connected assembly and original-cut/history
return. Those scopes are used here, without re-reviewing their proofs.

## 2. What section 11 actually asks its suppliers to provide

At a fixed stopping lattice T_a with V_s=N_s^4 sites, the external terms are
positive real densities rho_l(V). After division by one common all-small-field
constant, set Z_l=integral rho_l(V)dV and let l0 be the all-small-field term.
The stopping field V is integrated in its entirety. The index l denotes
the external determining sets and R-operation labels, not our Xi_h.

The section proposes the following chain.

1. Complete the small-field action, with the terms removed from its
   complement retained inside the appropriate large-field operations.
   Integrate the gauge-fixing delta factors before using the whole-integral
   upper bound. An equivalent gauge-fixed density is not asserted equal
   pointwise against arbitrary additional test factors.
2. Bound Z_l0 below using a product Haar ball of radius proportional to g_a
   on *every stopping bond*, plus the regularity and action bounds of the
   corresponding minimizer. Bound each other whole integral above using
   action positivity, the small-field exponent, component-operation bounds
   and all normalization/vacuum terms.
3. Charge the inner-layer terms at their own scales. With

       P(X)=sum_(n<=k) L^d |Z_n intersect X|_n,
       P^c(X)=sum_(n<=k) c_n L^d |Z_n intersect X|_n,
       c_n=C_E+C_lambda(1+log g_n^(-2)),

   retain an exact history exponent kappa^tr, including a nonnegative
   contribution discarded in one preparatory case of the simpler bound.
   The proposed half-gain/increased-cost recurrence gives

       kappa^tr=kappa_hat+G+H,  kappa_hat>=0,
       P^c+C_P P <= H+G/2.                              (E1)

   Here G has coefficient gamma_0 A_1^2/4 in front of the birth sum,
   half of the available coefficient in (1.79), and H pays the increased
   scale-dependent propagation cost. The remaining kappa_hat
   must still supply its stated future-scale lower bound.
4. Use the remaining component decay to sum shapes, classes and histories,
   keeping any later weighted mark within the reserved factor.

The outputs claimed under that construction are

    Z_l0 >= exp(-F),
    Z_l <= M_l = exp(F) product_X
                   [e sup(T'_k(X)1) exp(P^c(X))],
    F=C_fs V_s(1+log g_a^(-1)),                         (E2)

and, for allowed history weights omega,

    sum_(l!=l0) M_l product_X omega(X)
       <= delta_LF Z_l0,
    delta_LF=exp(2F)(exp(s)-1),
    s <= 2 V_s (M R_k)^(-4) exp[-3 p_0(g_a)/2].        (E3)

Allowed omega satisfy
1<=omega(X)<=exp(C_P P(X)+G(X)/2), after the displayed allocations.

The scalar arithmetic is checkable without importing a gauge theorem.
If the already-counted nonempty pattern majorants sum to at most exp(s)-1,
their contribution to E2 is at most exp(F)(exp(s)-1).
Since Z_l0>=exp(-F), this is at most E3. For positive terms, E3 implies

    Z_l0 / sum_l Z_l >= 1/(1+delta_LF).

Likewise E1 yields
exp(-kappa^tr+P^c)<=exp(-kappa_hat-C_P P-G/2) by subtraction.
These are conditional bookkeeping identities. They prove neither E1's
model-specific recurrence nor E2's hypotheses nor the pattern majorant.

The exact additional conditions are consequential. The section's (H)
pays the point count at every scale, including zero-length components
through their birth gain. T2-i and T2-ii pay surviving and kept shapes.
The raised propagation cost has a logarithmic g_n dependence; extending
the original recurrence with that cost and halved gain is a substantive
claim to verify, not merely changing the name of an absolute constant.
The stated exponent choice includes p_0>r(d+2)+1. Smallness
delta_LF<=1/2 additionally uses T2-v,

    8 exp(2F) V_s (M R_k)^(-4) exp[-3 p_0(g_a)/2] <= 1.

It depends on the loop through the stopping volume; the source derives
a fixed-loop/fixed-torus small-coupling regime, with p_0>4r+1 for that
comparison. Cutoff uniformity at that fixed V_s is distinct from volume
uniformity.

The load-bearing source claims were identified as follows; none is imported
as proved here.

| External supplier | What section 11 uses | What this pass verified |
|---|---|---|
| CRE (2.18), (2.23), Theorem 2, (2.43)–(2.50) | Term representation and bounds for E/R/boundary/vacuum terms at each layer | Exact use and scale counts in the external section; original proof not read |
| VAR Theorem 1 and CRE (2.16)–(2.17) | Haar-ball data produce minimizers passing all stopping tests | The proposed radius and margin argument; no transfer to our different kernel/cuts |
| LFR II (1.68)–(1.75), pp.377–380 | Completed action, normalizers, gauge integration and component operations | Location of every stated cost; no pointwise test-factor equivalence assumed |
| LFR II (1.79)–(1.89), pp.383–387 | History entropy, growth recurrence and half-rate reserve E1 | Conditional allocation arithmetic only; original recurrence and its extension unverified |
| Continuum section 7 and Cauchy section 11(c) | Shape count and fixed stopping-volume/loop restrictions | The displayed scalar summation under its component hypotheses |

Bałaban's original publications are identified by the external
[dictionary](https://github.com/MathePhysics/4D_Wilson_Loop_RG/blob/70d9a772fc9c7b47e36fd5e384fe42e07e7ccded/drafts/BALABAN_PAPER_LABELS.md).
Dimock's [Part II](https://arxiv.org/abs/1212.5562) and
[Part III](https://arxiv.org/abs/1304.0705) are constructive antecedents
already credited in RD4; this pass adds no independent read coverage or
theorem import from those papers.

## 3. Producer/consumer match

| Needed local return property | External output actually inspected | Matching obligation still required |
|---|---|---|
| Original Wilson/Decision-4 action, paired-contour compact normalizers and exact Haar/gauge factors | Bałaban determining sets, constrained minimizers and R-operations | An exact action/measure/normalizer dictionary; naming both objects Yang–Mills does not provide it |
| Fixed original coarse data, arbitrary admitted unchanged Xi_h, including its completion/size readers | Whole stopping V integral and sum over the external labels l | A fixed-data, history-resolved construction retaining those exact predicates and later integrations |
| Correct local reference D_h, or the separately specified R_h/Z_A reference | Z_l/Z_l0 against one common all-small-field whole-torus mass | Equality of reference objects and exact boundary/sea cancellation before absolute values |
| Fixed complex source/coarse domain with nonvanishing | Real action positivity and a Haar-ball lower bound | Complex denominator/total-variation control on that same domain |
| Connected coefficients in the full original-reader cardinality norm | Whole-integral scalar bound, external component shape/history estimates | Local analytic representation with covariance, background, inactive and source-only readers charged |
| Uniform budget as volume/level/history vary | exp(2F) with F proportional to N_s^4, uniform only in ultraviolet cutoff at fixed stopping volume | A local comparison or vacuum cancellation eliminating that whole-volume loss |
| Original complement and all contour/cut interfaces | Stopping-scale external large-field terms | Actual G minus Omega, G^c, original shifted cuts, contour sides and retained histories, without replacing any one by an easier defect event |
| Stable next-step output and physical continuum decay | A proposed term-weight input to a loop cutoff comparison | RD4 B3b plus the remaining common-theory existence and infrared estimates |

This distinction already exists inside the external sources. Continuum
section 7's Q_l fixes the exterior and asks for a lower bound for the
remaining all-small-field integral with a valid test margin. Cauchy
section 11 explicitly bypasses Q_l by paying the whole-volume factor F.
It therefore does not repair that local margin estimate. Our OC29 is
already a real comparison with the actual selected sector on its narrower
curvature window, while retaining an explicit volume factor. Importing
another scalar whole-volume comparison would not supply its absent local
analytic coefficients.

## 4. The later marked-history attempt reaches the same analytic task

The gamma note makes the useful distinction between an entire preliminary
logarithm and its localized pieces.

- Sections 16 and 18 retain composed **unnormalized** kernels, primitive
  marks, their common variables, cutoffs and future test envelopes.
  Ordered telescoping gives a sum of mark counts multiplied by the
  actual kernel costs. A reserve exp(-c P) can pay a terminal mark count
  because P exp(-c P)<=1/(e c). It is used once, not again at every
  intermediate conditional normalization or component re-entry.
- Section 19 corrects the inference from whole-integral unwinding to a
  partial localized logarithm. Terms assigned to V(X-neighborhood)
  inside a component and to V(Y) outside it are different parts of the
  logarithm. Exponentiating only one part does not reconstruct the
  original preliminary integral. Keeping a physical denominator also
  matters when an additional test factor is present.
- Sections 20–21 instead keep a marked connected inner expansion inside
  the outer expansion. At fixed exterior data, the proposed active
  integration support P and the complete spatial/background support Y
  have different jobs. Product-reference factorization uses P; later
  original-data locality still needs Y. The Gaussian reference must be
  localized before assigning its active supports.

In particular (G.109) is a weighted unmarked activity criterion and
(G.112) is the primitive marked local-norm estimate. The rooted-tree
argument in (G.110) assumes those two analytic inputs. Its graph arithmetic
does not produce them from a bounded real insertion or a Gaussian moment.
Section 21.4 leaves their construction for the full mixed A_j,B_j integral
open at the inspected source.

The latest section 23 retains

    Z_n=N_j integral chi_A chi_B exp(V_n(A,B))
                         dmu_A(A) dmu_B(B),

with N_j containing both determinants, the actual scalar normalization and
all prescribed Jacobians. Every inherited mixed interaction remains in V_n.
A non-small mixed quadratic term must be included in a proved joint
reference or treated through the exact conditional Gaussian; it cannot be
absorbed just because the separate Gaussian blocks are controlled.
Section 23 still asks for the mixed-domain potential majorant and its
localization with the full marked subtraction. The root-dimension
calculation of section 22.8 has a separate mixed-domain identification
condition. This pass does not certify that Gaussian calculation.

These are structurally the same tasks as RD4 L2/L7's matching and gluing,
and SC section 8's complete covariance-reader composition followed by the
original-cut/history return. This is a comparison of required properties;
the two model-specific estimates are not asserted mathematically equivalent.

## 5. What can be used next

No new bounded Yang–Mills lemma is claimed from this search. The scalar
comparison and exponent-allocation arithmetic above are already covered in
scope by RD4's L2–L9 accounting and the original-law OC comparisons.
Publishing them as another completed return lemma would duplicate support
while leaving the target unchanged.

The useful next specification is more precise: after the selected nonlinear
connected construction, keep every complementary or history region attached
to its original **unnormalized** kernel; preserve the unchanged predicates,
both covariance tails, all source vacuum and determinant factors, and the
actual later test functions. Before the history/entropy sum, prove an
absolute joint bound for these kernels on the common complex original-data
domain, with their full readers and the inherited interaction included.
Any amplification per integration must be allocated to that same history's
unspent cost ledger. Then construct the connected matched-reference
expansion required by RD4, cancelling remote vacuum clusters before taking
absolute values. None of these missing analytic inputs is supplied by a
price for test 1 or by a real rare-event probability alone.

That is an upstream research direction, not a proved consumer. An independent
review may assess this source map and conditional accounting; the frozen
receipt supplies no theorem certificate. No new physical axiom, primitive,
audit grade, front/register edit, numerical experiment, Git mutation or
external message is part of this unit.

This source is used as a non-derivation analogy and a precise hypothesis
map; it does not provide derivation closure for the normalized original-law
return, full continuum existence, or the physical continuum mass gap.

