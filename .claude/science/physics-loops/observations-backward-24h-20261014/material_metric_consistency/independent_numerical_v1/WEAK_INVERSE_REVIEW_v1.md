# Focused independent critique of the weak metric inverse

The displayed weak shape, kinetic and potential identities are consistent on the stated regular nonconstant chart. The two ordered positive kinetic weights give at most one admitted eta; the potential determinant argument is valid under its stated Y>1 condition. Existence, a positive recovered candidate, full-interval field-equation membership and usable measurement precision are separate requirements. No author numerical implementation was read or run, and no numerical weak inverse was implemented here.

## Exposure and exact evidence

The complete source reviewed is `WEAK_DERIVATION_v1.md`, SHA256 `c00be0711a4eee7f9d36ff8a7055051441cc289a5781bc7519aad994e6f5c07c`, copied as `EXPOSED_WEAK_DERIVATION_v1.md`. `WEAK_PROBE_v1.json`, SHA256 `b50cd58cfcf23bdaeb6274d28f58d3e1640968d9abe96be9d79b3905e375e6a8`, was also exposed; its two reported checks are not counted as this reviewer's evidence. The earlier original M19 note and helper had already been exposed during the separate Einstein-generator check.

The independent proof and code were frozen at2026-10-15T20:26:12.290184Z in `WEAK_IMPLEMENTATION_FREEZE_v1.json`. The proof hash is `69da301f2d23bcc8a4dfc108ab9270f81a1ec3144d1bb6cbf929edc55e075962`; independent exact code `weak_exact_controls_v1.py` has SHA256 `fdfd81efd2697680ac00f81aa82f5f67fc7a06b5229e887212674cab6f9113d0`. It imports no author code. The single run completed with12 exact checks, zero failures and exit0 in0.433seconds of a120second subprocess cap. Source/results/stdout/stderr/receipt are retained. There were no failed attempts in this weak check.

## Shape recovery

Put e=ell', q=1/r-e. Direct substitution of the original geometric Gt and Ga gives

    u=(Ga-Gt)/(Bq)
     =-q'/q-B'/(2B)-2/r-e+1/(B r² q).

The displayed integrated h follows, normalized by h(r0)=1. On a connected D=Bq nonzero chart, q has a fixed sign, so q0/q is positive even on a negative-q chart. The other factors are positive; h is positive and h'/h=u. A constant rescaling of the lapse cancels between N0 and N. This recovers normalized F shape, not its absolute normalization and not a separately selected scalar boundary value.

The regularity statement is correctly limited: N in C3 and B in C2 give h in C2 and u in C1. The integral expression evaluates h using N,N',B, while evaluation of u uses N'',B'. It avoids direct N''' and B'' readouts in the moment formulas. It does not prove a lower-regularity metric theorem or make second derivatives observable without an error model.

## Kinetic weak equation and uniqueness

Define

    k0=2ell'/r-B'/(Br)-u²-(B'/(2B)-ell')u.

The exact geometric identity is H/B=k0-u'. Hence

    K[w]-integral w H/B = [w u] at the endpoints.

The claimed K is correct for compactly supported C1 weights because that boundary term vanishes. With X=s h/eta and Y=s(h/eta-1)>0,

    2(z')²/(lambda X)=u² h/[2lambda(h-eta)],

which yields K=A/(2lambda) in vacuum.

For fixed eta in the admitted interval, A is positive: its integrand has nonnegative w and strictly positive u²h/(h-eta) wherever w is nonzero. Moreover

    A'(eta)/A(eta)
      = weighted mean of 1/(h-eta),

using the positive measure w u²h/(h-eta) dr. If every h value on the first support is strictly smaller than every h value on the second, every value of1/(h-eta) in the first mean is strictly larger. Thus d log(A1/A2)/deta>0. There is at most one eta satisfying the observed moment ratio. The argument requires ordered ranges, not merely ordered average h values. Continuity and nonzero u on a connected chart make h strictly monotone and allow separated support choices.

This is a uniqueness result, not an existence result. The finite observed ratio K1/K2 must lie in the actual image of A1/A2 on the admissible eta interval. In particular, that ratio need not diverge when eta approaches inf h: both compact supports can lie away from that infimum. A numerical implementation must retain an actual admissible bracket/range check. The source already leaves existence and positive K1,K2 as checks. Recovery must also retain lambda>1, the implied k domain and all positive potential conditions.

The strict domain eta<inf h is a useful uniform margin, but stronger than merely Y>0 pointwise on an open annulus. A positive field can approach zero at an excluded annulus endpoint, giving eta=inf h. This is an excluded boundary case, not an algebra error; a claim covering every pointwise-positive open-annulus solution would need to distinguish it. Restricting to a compact interior subannulus supplies a strict gap for a continuous positive field.

## Potential integration by parts and determinant

Elimination of H gives

    W=-(Gt+Gr)/2-B(u'+u²)/2
      -(B'/4+B ell'/2+2B/r)u.

Because X'=uX, direct differentiation shows that the displayed T density is precisely

    w X W + (w X B u/2)'.

The stated sign and B'/4 coefficient are therefore correct. The compact-support qualification is essential. For endpoint weights the boundary [w X B u/2] must be retained.

The independent integration control uses nonconstant B=1+r/3, ell'=2r/7, X=3(1+r)², u=2/(1+r), on[1,2], with the compact C1 extension of w=(r-1)²(2-r)². It gives exactly

    T[w] = integral w X W = 69757/1960 - 54 log(2),

which is nonzero. This is an algebraic integration-by-parts fixture, not a vacuum solution. Replacing w with1 leaves the omitted boundary equal to7 exactly. Both the compact identity and the noncompact failure are retained in `WEAK_EXACT_RESULTS_v1.json`.

For A(Y)=3(s+Y²) and C(Y)=Y²log²Y/(4a),

    d(C/A)/dY
      =Y log(Y)[s log(Y)+s+Y²]/[6a(s+Y²)²].

This is positive for Y>1 and s,a>0. The integrated ratio (integral w C)/(integral w A) is a positive A-weighted mean of C/A. Strictly ordered Y ranges imply strictly ordered means and a nonzero two-weight coefficient determinant. Since Y is an increasing affine function of h for fixed positive s,eta, the stated support ordering transfers. The condition Y>1 is sufficient, not necessary. A range crossing Y=1 does not inherit this monotonicity guarantee and needs its own determinant check.

## Full weak identities versus finite moments

At the retained regularity, the relevant field residuals are continuous. Vanishing integrals against every compact test weight imply pointwise vanishing by the fundamental lemma. Nonnegative compact weights suffice as a testing cone. The shape identity supplies the angular-minus-time equation; the kinetic and potential identities then supply the remaining metric equations. The nonconstant branch and the same regularity allow the original Bianchi/scalar implication used by M19. This argument does not follow from two fitted moments and a finite list of later moments.

The independent exact limitation witness takes w1=(r-1)²(2-r)² on[1,2] and w2=(r-3)²(4-r)² on[3,4], each extended by zero. The nonzero C1 residual R=w1(r)(r-3/2) on[1,2], zero elsewhere, obeys both integral w1 R=0 and integral w2 R=0, while R(5/4)=-9/1024. This demonstrates incompleteness of those finite residual tests; it is explicitly not a constructed metric or action counterexample.

A finite implementation should consequently report fitted parameters and checked moments, preserving failed or unresolved additional moments. It cannot report exact local membership or a full-interval error bound from numerical moment agreement alone. Quadrature error, h and u readout errors, the ratio slope, the potential matrix conditioning, and any uncertain/adaptive support construction remain separate suppliers. No observation arrays, derivative uncertainties, vacuum evidence, sector selection, absolute scale or initial history are supplied by this probe.

Root retains authorship. This report covers only the frozen working derivation and the independent controls above, not later numerical source, canonical packaging, formal audit, empirical validation or landing approval. All writes were confined to the assigned independent numerical directory.
