---
claim_id: native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_bounded_theorem_note_2026-09-03
claim_type: bounded_theorem
claim_scope: "For the explicitly defined reduced Lie-type A2 polynomials H=x y(x+y)/2 and Q=x^2+xy+y^2, constant-coefficient operators R=partial_x+partial_y and L=(partial_xx-partial_xy+partial_yy)/3, formal S=exp(L/2), and the declared diagonal-multiplier coefficient T2_diag=S M_[P2 exp(-Q)] S: the exact polynomial identity P2 exp(-Q)=(1/2)R^2[H exp(-Q)]+3H exp(-Q) gives T2_diag=(1/2)[R,[R,T0]]+3T0 for T0=S M_[H exp(-Q)] S. In any finite real-symmetric realization with real-skew R and a simple eigenvalue mu_i, the diagonal double-commutator contribution cancels the ordinary second-order mixing contribution, leaving mu_i^(2)=3mu_i. The relative statement requires mu_i nonzero, and the real log-ratio statement requires positive compared eigenvalue branches. This concerns only the declared diagonal P2/similarity sector; heat terms, any full saddle coefficient, continuum/domain transfer, uniform gaps, and physical mass gaps are outside scope."
upstream_dependencies: []
runner: scripts/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.py
---

# Reduced Lie-type A2 diagonal similarity-sector cancellation

**Date:** 2026-09-03

**Type:** bounded_theorem

**Audit:** unset; independent audit remains a separate lane

**Status:** proposed_retained

**Primary runner:**
[`scripts/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.py`](../scripts/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.py)

**Runner cache:**
[`logs/runner-cache/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.txt`](../logs/runner-cache/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.txt)

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exact polynomial identity and a finite-dimensional perturbation lemma for one explicitly isolated diagonal-multiplier/similarity sector."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Independently check the polynomial identity, commutator signs, perturbative denominator signs, nonzero-eigenvalue boundary, and omitted-term fence."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope boundary

The object proved here is deliberately named `T2_diag`. It is the diagonal
`P2` multiplier, equivalently the displayed similarity-sector coefficient. It
is not a complete second-order saddle coefficient. In particular, no heat-side
term is included or asserted to vanish. Questions about a total second-order
sign, a continuum or operator-domain realization, a uniform half-line gap, an
infinite-volume limit, and a physical Yang--Mills mass gap remain outside this
theorem.

The relative correction `mu_i^(2)/mu_i` is asserted only for `mu_i != 0`. A
real log-eigenvalue ratio additionally requires the compared eigenvalue
branches to remain positive near the expansion point. The unnormalized
identity `mu_i^(2)=3mu_i` is the statement that survives without division.

## Imports and assumptions

There are no load-bearing repository or empirical inputs. All polynomials and
operators used in the claim are defined below, and the runner reads no mutable
repository file. Constant-coefficient differentiation and finite-dimensional
nondegenerate Rayleigh--Schrodinger perturbation theory are standard
mathematical methods. The latter formula is displayed and reduced directly,
so no numerical eigenfunction or fitted coefficient is imported.

The finite perturbation lemma assumes:

1. `T0` is real symmetric;
2. `R` is real skew-symmetric;
3. the eigenvalue under consideration is simple;
4. the perturbation coefficients are exactly `T1=[R,T0]` and
   `T2_diag=(1/2)[R,[R,T0]]+3T0`.

These are mathematical hypotheses, not claims about a particular continuum
realization.

## Exact target and obligation graph

The target has two proved leaves and one scope fence:

```text
P0  declared H, Q, P2, R, L, S, T0, and T2_diag
 |-- P1  exact polynomial/differential identity
 |    `-- P1a  [R,L]=0, hence R commutes formally with S
 |-- P2  finite real-symmetric perturbation lemma
 |    |-- P2a  double-commutator/mixing cancellation
 |    `-- P2b  common relative correction for nonzero eigenvalues
 `-- P3  omitted heat/full-saddle/continuum terms remain outside target
```

Runner Part 1 checks `P1` over exact symbolic expressions and all monomials of
total degree at most eight for the commutator test. Part 2 checks every sign and
factor in a nontrivial exact five-dimensional realization, the similarity
expansion, all ten pairwise relative cancellations, and three adversarial
mutations.

## The polynomial identity

Define

```text
H = x y (x+y)/2,
Q = x^2 + xy + y^2,
W = H exp(-Q),
R = partial_x + partial_y,
L = (partial_xx - partial_xy + partial_yy)/3,
S = exp(L/2).
```

Also set

```text
u  = x+y,
G1 = (u^2+2xy)/2,
P2 = (3/2)u - 3u G1 + (9/2)u^2 H.
```

Direct differentiation gives

```text
R H = G1,
R Q = 3u,
P2 exp(-Q) = (1/2) R^2 W + 3W.                 (1)
```

Because `R` and `L` have constant coefficients, `[R,L]=0`; therefore `R`
commutes formally with `S`. For any multiplier `M_f`,
`[R,M_f]=M_[Rf]`. Define only

```text
T0      = S M_W S,
T2_diag = S M_[P2 exp(-Q)] S.
```

Equation (1) then yields the exact isolated identity

```text
T2_diag = (1/2)[R,[R,T0]] + 3T0.               (2)
```

No broader object is assigned the symbol `T2_diag`.

## Finite-dimensional cancellation lemma

Let `T0 Phi_i = mu_i Phi_i` be a simple eigenpair in a finite real-symmetric
realization, with `R` real skew-symmetric, and define

```text
T1 = [R,T0],
T(eps) = T0 + eps T1 + eps^2 T2_diag + O(eps^3).
```

The ordinary second-order eigenvalue coefficient is

```text
mu_i^(2) = <Phi_i|T2_diag|Phi_i>
           + sum_(k != i) |<Phi_k|T1|Phi_i>|^2/(mu_i-mu_k).   (3)
```

In the eigenbasis of `T0`,

```text
<Phi_k|T1|Phi_i> = (mu_i-mu_k) R_ki.
```

Using `R_ik=-R_ki`, the sum in (3) equals

```text
-(1/2)<Phi_i|[R,[R,T0]]|Phi_i>.
```

Substitution of (2) cancels the diagonal double-commutator term and leaves

```text
mu_i^(2) = 3mu_i.                                (4)
```

For `mu_i != 0`, the relative coefficient is therefore three. For two positive
simple eigenvalue branches the contribution of this isolated sector to the
second-order coefficient of their log ratio is zero:

```text
mu_1^(2)/mu_1 - mu_0^(2)/mu_0 = 0.              (5)
```

Equivalently, the first two commutator terms are the expansion of the
orthogonal similarity transform `exp(eps R) T0 exp(-eps R)`, while `3T0` is a
common scalar correction. Similarity preserves eigenvalues, and the common
relative correction cancels in (5).

## Falsifiers and limits

The runner requires nonzero exit if any check fails and explicitly detects:

- changing the factor `1/2` in (1);
- changing the scalar `3` in (1);
- reversing the double-commutator sign;
- reversing the perturbative denominator sign; or
- replacing the common `3T0` remainder by a nonuniform diagonal remainder.

The last mutation makes the pairwise relative cancellation fail. This shows
that the result depends on the isolated similarity structure and common scalar;
it does not license a statement about additional second-order terms.

## Reproduction

```bash
python3 scripts/precompute_audit_runners.py \
  --runners scripts/native_gauge_transfer_reduced_lie_type_a2_diagonal_similarity_sector_cancellation_check_2026_09_03.py \
  --force --push-mode none --allow-non-main
```

The machine-written cache must pin the runner SHA-256, carry the declared
120-second timeout, record successful exit, reproduce every exact check, and
end with zero failures. No audit verdict is created or changed here.
