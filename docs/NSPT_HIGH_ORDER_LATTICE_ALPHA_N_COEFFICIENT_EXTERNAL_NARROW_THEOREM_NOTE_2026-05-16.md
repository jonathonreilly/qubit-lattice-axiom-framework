# NSPT High-Order Lattice α^N Coefficient — External Narrow Theorem

**Date:** 2026-05-16
**Claim type:** positive_theorem
**Scope:** the toy formal-series algebra actually checked by the paired
runner (per the 2026-05-18 auditor repair target). The NSPT-style
high-order perturbative formalism (Di Renzo-Onofri) and the n=20 SU(3)
Wilson-plaquette computation are recorded as context-only published
references in `## Demoted to future work` below and are **not** part of
this row's audited claim. No framework substrate identification,
hierarchy closure, scale ratio derivation, or α_LM^16 substitution is
claimed.
**Status authority:** source-note proposal only; independent audit sets any
audit result and pipeline-derived status.
**Runner:** [`scripts/frontier_nspt_high_order_lattice_alpha_N_coefficient_external_narrow.py`](../scripts/frontier_nspt_high_order_lattice_alpha_N_coefficient_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_nspt_high_order_lattice_alpha_N_coefficient_external_narrow.txt`](../logs/runner-cache/frontier_nspt_high_order_lattice_alpha_N_coefficient_external_narrow.txt)

## Narrowed claim (per auditor repair target 2026-05-18)

Per `notes_for_re_audit_if_any` on the 2026-05-18 audit verdict ("narrow
the claim to the toy formal-series algebra actually checked by the
runner"), this row's audited claim is restricted to the **toy
formal-series algebra of integer-order α^N coefficients** as actually
exercised by the paired runner. The published NSPT n=20 SU(3)
Wilson-plaquette computation and the Di Renzo-Onofri NSPT formalism as
applied to physical lattice gauge theory are recorded only as
context-only external references in `## Demoted to future work` below
and are **not** part of the audited claim.

The narrowed audited claim:

> On a formal power series `O = Σ_{n≥0} c_n α^n` over `Fraction`
> rationals, with each `c_n` admitted as a determinate input
> coefficient, the following toy formal-series algebra closes:
> (i) every partial sum `Σ_{n=0}^{N} c_n α^n` is a determinate
> `Fraction` at any finite `N` and any `α ∈ Q`;
> (ii) scalar arithmetic at integer order satisfies
> `α^16 = (1/10)^16 = 10^{-16}` exactly under the test evaluation
> point `α = 1/10`;
> (iii) the Cauchy product `(Σ a_n α^n)(Σ b_n α^n) =
> Σ_n (Σ_{k=0}^{n} a_k b_{n-k}) α^n` evaluates correctly on the worked
> example `[1,2,3] * [4,5,6] = [4,13,28,27,18]`;
> (iv) the Cauchy-product structure depends only on the input
> coefficient values, not on any underlying gauge theory or substrate;
> (v) the geometric surrogate `c_n = 1` reproduces the exact
> closed-form truncation error at `α = 1/10` through order 20;
> (vi) the discrete-time Langevin update on a Fraction-valued
> truncated series preserves order-by-order Fraction structure on the
> truncation; and
> (vii) `(1 + α)^3` decomposes as `[1, 3, 3, 1, 0, 0]` by iterated
> Cauchy product.

These are pure algebraic facts about `Fraction`-coefficient formal
series; the runner exercises each one. No physical SU(3) Wilson-plaquette
computation, no NSPT formalism applied to a physical gauge action, and
no published n=20 coefficient is verified by the narrowed claim.

## Demoted to future work (not part of the narrowed claim)

The following NSPT/lattice-physics content is **not** part of this
row's audited claim, pending retained-grade upstream dependency
packets:

- The Di Renzo-Onofri NSPT formalism as applied to physical SU(N_c)
  lattice gauge theory (stochastic Langevin equation
  `∂_t U_x,μ(t) = - i (∇_x,μ S[U(t)]) U_x,μ(t) + i η_x,μ(t) U_x,μ(t)`
  with `U_x,μ ∈ SU(N_c)` and Wilson plaquette action). The narrowed
  claim does not import this formalism as an audited dependency.
- The published n=20 SU(3) Wilson-plaquette computation of
  Horsley/Perlt/Rakow/Schierholz et al. (arXiv:0910.2795,
  arXiv:1205.1659) producing explicit `c_n` for `n = 1, ..., 20`. The
  narrowed claim does not import these published coefficients as an
  audited dependency.

Closing either of these would require a separate, independently
audited upstream dependency packet for the NSPT formalism and/or the
n=20 Wilson-plaquette computation. The published papers referenced in
`## External References` below are recorded as context-only
literature pointers and not as load-bearing dependencies on the
narrowed claim.

## Boundary

This note records, in its narrowed form, a toy formal-series algebraic
theorem on `Fraction`-coefficient power series, exercised by the
paired runner. It does **not** claim, under the narrowed claim:

- that the NSPT lattice substrate is identified with the framework's
  substrate (lattice cell, taste, blocking, or any project-specific
  structure);
- that any published `c_n` for the Wilson plaquette is a framework
  hierarchy coefficient or a project-specific coupling;
- that any published `c_n` for the Wilson plaquette is consumed as a
  load-bearing input to the narrowed claim (the published n=20
  computation is demoted to future work; see `## Demoted to future
  work` above);
- that the NSPT formalism as applied to physical SU(N_c) lattice gauge
  theory is consumed as a load-bearing input to the narrowed claim
  (same demotion);
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- closure of the α_LM^16 substitution or any framework `α^N` hierarchy
  at integer `N`;
- any v/M_Pl or other dimensional scale ratio (formal series in `α`
  are not scale ratios);
- any numerical prediction or comparison with observation beyond the
  scope of the toy formal-series algebra checks themselves;
- any new framework axiom or repo-wide premise.

Any later framework use must separately import a retained-grade NSPT
formalism packet, separately identify the framework substrate with
NSPT iterates, identify a framework observable with an NSPT lattice
observable, and verify the substrate-specific bridge.

## External References

- F. Di Renzo, A. Mantovi, V. Miccio, F. Onofri, "Numerical Stochastic
  Perturbation Theory in the Schrödinger Functional", arXiv:hep-lat/0406001
  (2004).
- F. Di Renzo, L. Scorzato, "Numerical Stochastic Perturbation Theory for
  full QCD", arXiv:hep-lat/0408015 (2004).
- R. Horsley, G. Hotzel, E.-M. Ilgenfritz, R. Millo, H. Perlt, P. E. L.
  Rakow, Y. Nakamura, G. Schierholz, A. Schiller, "Wilson loops to 20th
  order numerical stochastic perturbation theory", arXiv:0910.2795 (2009).
- R. Horsley, H. Perlt, P. E. L. Rakow, G. Schierholz, A. Schiller,
  "Perturbative determination of the Wilson loops in lattice gauge
  theory using NSPT", arXiv:1205.1659 (2012).
- G. Parisi, Y.-S. Wu, "Perturbation theory without gauge fixing",
  Scientia Sinica 24 (1981), 483.

## Verification

The paired runner checks the toy formal-series algebra of the narrowed
claim only:

1. the discrete-time Langevin update on a `Fraction`-valued truncated
   series preserves order-by-order Fraction structure on the
   truncation (toy surrogate, not a physical SU(N_c) iterate);
2. the coefficient series `O = Σ c_n α^n` is a determinate `Fraction`
   at every finite order on scalar / polynomial surrogates;
3. partial-sum closed-form check at small coupling: at `α = 1/10`,
   the partial sum to order 20 of a geometric surrogate matches the
   exact closed-form truncation;
4. order-16 scalar arithmetic: `α^16 = (1/10)^16 = 10^-16` exactly in
   Fraction arithmetic;
5. Cauchy product: the product of two coefficient series follows the
   standard convolution formula `(a * b)_n = Σ_k a_k b_{n-k}`;
6. substrate-independence of the formal-series algebraic structure:
   the algebra depends only on the input coefficients, not on any
   underlying gauge theory;
7. integer-N structure: each coefficient `c_n` is a determinate
   computation at order `n`, demonstrated on the worked toy series
   `(1 + α)^3 = [1, 3, 3, 1, 0, 0]` reconstructed via iterated Cauchy
   product;
8. source-note boundary checks excluding framework-substrate
   identification, hierarchy closure, scale ratio derivation, and
   α_LM^16 closure overclaims.

Expected runner result: `PASS=N`, `FAIL=0`.

## Upstream authority (context only under the narrowed claim)

Under the narrowed claim above, the only load-bearing upstream is
ordinary `Fraction`-coefficient formal-series algebra (standard
algebraic computation, no external lattice-physics authority
imported). The literature citations below are recorded as **context
only** — not load-bearing on the narrowed claim. Closing the demoted
n=20 Wilson-plaquette and Di Renzo-Onofri formalism claims would
require independently audited upstream dependency packets for each;
see `## Demoted to future work` above.

- **Context only — Di Renzo-Onofri NSPT framework**: F. Di Renzo, E. Onofri, G. Marchesini, P. Marenzoni, "Four-loop result in `SU(3)` lattice gauge theory by a stochastic method: Lattice correction to the condensate," *Nucl. Phys. B* **426**, 675 (1994); F. Di Renzo & L. Scorzato, "Numerical Stochastic Perturbation Theory for full QCD," *JHEP* **10**, 073 (2004). Listed for orientation only; not consumed by the narrowed claim.

- **Context only — high-order NSPT Wilson-plaquette computation**: F. Di Renzo et al. (the Parma NSPT program). The specific `n = 20` SU(3) Wilson-plaquette computation referenced for context is reported in the Parma NSPT lineage; see C. Bauer, G. S. Bali, A. Pineda, "Compelling evidence of renormalons in QCD from high order perturbative expansions," *Phys. Rev. Lett.* **108**, 242002 (2012) and follow-up Parma-collaboration high-order Wilson-loop computations. Listed for orientation only; not consumed by the narrowed claim.

- **Background textbook authorities (not load-bearing)**: G. Parisi & Y.-S. Wu, "Perturbation theory without gauge fixing," *Sci. Sin.* **24**, 483 (1981) — original stochastic-quantization paper. P. Damgaard & H. Hüffel, *Stochastic Quantization*, *Phys. Rept.* **152**, 227 (1987) — background review.

The framework-side admissions (whether any framework-specific
α value corresponds to the Wilson-plaquette `α` at any particular
order) remain explicitly out of scope, both under the narrowed claim
and in any later use.
