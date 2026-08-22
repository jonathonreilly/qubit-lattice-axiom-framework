---
claim_id: gauge_vacuum_plaquette_common_integral_class_sector_convolution_classification_narrow_theorem_note_2026-08-22
claim_type: positive_theorem
claim_scope: "For a supplied finite two-slice SU(3) Wilson measure, removal of the two marked spatial half-weights defines an exact common-integral middle form Q and the full marked character form satisfies C=M_beta Q M_beta before normalization, or C=N(M_beta Q_hat M_beta) after Q_hat is normalized by its trivial entry. On every finite character box, the class-sector compression is realizable by convolution with a finite central character polynomial if and only if its character matrix is diagonal. The quadratic/cubic Casimir pair separates B_5 and gives one exact nonnegative scalar defect that vanishes if and only if that B_5 matrix is diagonal. A finite positive real self-adjoint irrep-swap-commuting counterexample proves that those properties alone do not imply diagonality. The result neither proves nor rejects diagonality of the physical Wilson Q, selects the Wilson action, derives beta=6, or retires a TOE obligation. The bundled Monte Carlo path uses burned seeds and is non-certifying."
depends_on:
  - minimal_axioms
  - gauge_vacuum_plaquette_transfer_operator_character_recurrence_note
  - gauge_temporal_gauge_mixed_kernel_spatial_link_factorization_narrow_theorem_note_2026-05-10
  - su3_character_diagonal_convolution_equivalence_narrow_theorem_note_2026-05-10
runner: scripts/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.py
runner_cache: logs/runner-cache/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.txt
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Common-Integral Middle Operator and Class-Sector Convolution Classification

**Date:** 2026-08-22

**Role:** exact operator interface and analytic selector for the open
gauge-vacuum compression seam

**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.py`](../scripts/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.py)

**Cached receipt:**
[`logs/runner-cache/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.txt`](../logs/runner-cache/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.txt)

## Result up front

The physical two-slice marked observable and its middle operator can be
estimated in one common Wilson ensemble without importing the rejected static
environment identification.  Removing exactly the two marked spatial
half-weights gives an exact change-of-measure identity

```text
C_tilde = M_beta Q_tilde M_beta.                                      (1)
```

After normalizing the middle form by its trivial entry, the corresponding
normalized identity is

```text
C = N(M_beta Q_hat M_beta),  N(A)=A/A_(0,0).                          (2)
```

Equations (1)-(2) hold on the complete character space.  They do not state
that `Q_tilde` is diagonal.

The diagonal question has an exact finite answer.  On a finite character box
`H_N`, the class-sector matrix `Q_N` is the compression of a central
convolution operator if and only if `Q_N` is diagonal in the irreducible
character basis.  On `B_5`, the joint quadratic/cubic Casimir defect

```text
Delta_5(Q) = ||[D_2,Q]||_F^2 + ||[D_3,Q]||_F^2                        (3)
```

vanishes if and only if `Q` is diagonal.  This replaces a 20-versus-350
parameter model comparison by one exact structural scalar.

Positivity, real self-adjointness, slice exchange, and irrep-conjugation swap
do not imply that scalar is zero.  An explicit positive finite counterexample
proves the logical separation.  It does not prove that the actual Wilson
middle operator is non-diagonal; direct analysis of (3), or a stronger
regular-translation theorem, remains capable of establishing diagonality.

## 1. Exact common-integral setup

Let `W_0` and `W_1` be the incoming and outgoing marked spatial plaquette
holonomies in a finite two-slice Wilson integral.  Put

```text
X(W)      = Re Tr(W)/3,
m_beta(W) = exp[(beta/2) X(W)] = exp[(beta/6) Re Tr(W)],
r_beta    = 1/[m_beta(W_1)m_beta(W_0)].                                (4)
```

Let `E_full` denote expectation in the normalized full two-slice Wilson
measure, including both marked half-weights.  For irreducible characters
`chi_lambda`, define the two sesquilinear forms

```text
C_tilde_(lambda,mu)
  = E_full[conj(chi_lambda(W_1)) chi_mu(W_0)],

Q_tilde_(lambda,mu)
  = E_full[r_beta conj(chi_lambda(W_1)) chi_mu(W_0)].                    (5)
```

Every other spatial and mixed Wilson factor remains in the common measure.
Thus (5) changes no link identification and performs no literal deletion of
an unmarked environment.

Let `M_beta` be multiplication by `m_beta` on the complete class-function
space.  Its character matrix is Hermitian because `m_beta` is real.

## 2. Theorem 1: exact forward identity

For every pair of finite character polynomials `f,g`,

```text
<f,C_tilde g>
  = E_full[conj(f(W_1)) g(W_0)]

  = E_full[r_beta
      conj((m_beta f)(W_1)) (m_beta g)(W_0)]

  = <f,M_beta Q_tilde M_beta g>.                                       (6)
```

The second equality follows pointwise from
`r_beta m_beta(W_1)m_beta(W_0)=1`.  Hence (1) holds as a form identity on the
dense character-polynomial domain.  On a finite lattice the Wilson weights
are bounded and positive, so the form extends to the corresponding bounded
class-sector operator.

Define

```text
Q_hat = Q_tilde/Q_tilde_(0,0).                                         (7)
```

Since `(M_beta Q_tilde M_beta)_(0,0)=C_tilde_(0,0)=1`, substituting (7)
into (1) and dividing by the output trivial entry gives (2).  No fitted scalar
is introduced.

This theorem is independent of whether `Q_tilde` is diagonal, low rank, or a
central convolution.

### Exact finite closure control

Exponential multiplication has an infinite character expansion, so a finite
`B_5 -> B_1` exponential forward calculation is a cutoff approximation.  The
runner separately uses

```text
g_a(W)=1+aX(W),  a in {-9/10,9/5}.                                     (8)
```

Because `X` is the six-neighbor character recurrence, multiplication by
`g_a` maps `B_1` into `B_2` exactly.  Also `X(SU(3))` lies in `[-1/2,1]`, so
both choices in (8) obey `g_a>=1/10`.  The runner evaluates the pointwise
identity `C_g=G_a Q G_a` on actual SU(3) plaquette holonomies and rejects a
mutated boundary multiplier.  This is an exact implementation control, not a
statistical claim about physical diagonality.

## 3. Theorem 2: finite class-sector convolution equivalence

Let normalized Haar measure be understood and set

```text
H_N = span{chi_lambda: lambda in B_N},
Q_N = P_N Q P_N.                                                        (9)
```

The following are equivalent:

1. `Q_N` is diagonal in the character basis, with entries `q_lambda`.
2. There is a finite central character polynomial

   ```text
   k_N(g)=sum_(lambda in B_N) d_lambda q_lambda chi_lambda(g)           (10)
   ```

   whose convolution satisfies `P_N C_(k_N) P_N=Q_N`.

For `(1) -> (2)`, Schur orthogonality gives

```text
integral k_N(xy^(-1)) chi_mu(y) dy = q_mu chi_mu(x).                    (11)
```

For `(2) -> (1)`, (11) states that every character is an eigenvector of the
compressed convolution.  Character orthogonality also makes the coefficient
list in (10) unique.

This is a theorem about `P_N Q P_N`.  It does not imply that a raw two-boundary
kernel is itself a function only of `xy^(-1)`.

### Infinite-space convergence boundary

If `sum_lambda d_lambda^2 |q_lambda|^2 < infinity`, (10) converges in `L^2`
to a central kernel and the same equivalence holds for the Hilbert-Schmidt
convolution operator.  Without a summability premise, the compatible finite
polynomials define only finite compressions or a formal central distribution.
No infinite-volume or all-character convergence is claimed here.

## 4. Theorem 3: full-kernel regular translations

For an integral kernel

```text
(Qf)(x)=integral K(x,y)f(y)dy,                                         (12)
```

the two identities

```text
K(xa,ya)=K(x,y),
K(ax,ay)=K(x,y)                                                        (13)
```

for every `a,x,y` are equivalent to `K(x,y)=k(xy^(-1))` with `k` central.
Indeed, the first identity with `a=y^(-1)` produces the difference form, and
the second then gives conjugation invariance of `k`.  The converse follows by
direct substitution.

Thus full central convolution requires both regular-translation identities.
Simultaneous conjugation,

```text
K(hxh^(-1),hyh^(-1))=K(x,y),                                          (14)
```

is strictly weaker.

On any box containing `(0,0)` and `(1,1)`, let

```text
v = chi_(0,0)+chi_(1,1),
A = I+|v><v|.                                                          (15)
```

Then `A` is positive definite, real, self-adjoint, and commutes with the irrep
swap `(p,q)<->(q,p)`, but
`A_((0,0),(1,1))=1`.  It is therefore not character-diagonal.  The associated
finite character kernel is separately conjugation invariant in both
arguments, which is stronger than (14).  This exact witness proves that the
listed positivity and symmetry properties do not entail central convolution.

The mixed temporal Wilson kernel has a retained linkwise convolution theorem.
The full source environment also contains spatial plaquette factors coupling
the nonmarked link integrations.  The retained mixed-kernel theorem explicitly
excludes that dependent case.  Consequently it cannot, without another
argument, establish (13) for the full stripped kernel.  This is a boundary on
that proof route, not a result against accidental diagonality after all link
integrations.

## 5. Theorem 4: one exact joint-Casimir selector

For `lambda=(p,q)`, define

```text
c_2(lambda) = [p^2+q^2+pq+3p+3q]/3,

c_3(lambda) = [(p-q)(2p+q+3)(p+2q+3)]/18.                              (16)
```

The ordered pair `(c_2,c_3)` separates every highest weight in `B_5`.
Let `D_i=diag(c_i(lambda))`.  Direct expansion gives

```text
Delta_5(Q)
 = sum_(lambda,mu in B_5)
   [(c_2(lambda)-c_2(mu))^2+(c_3(lambda)-c_3(mu))^2]
   |Q_(lambda,mu)|^2.                                                   (17)
```

Every coefficient in (17) is nonnegative and is zero exactly when
`lambda=mu`.  Therefore

```text
Delta_5(Q)=0  iff  Q is character-diagonal on B_5.                      (18)
```

Equation (18) is deterministic and action-independent.  Applying it to a
physical estimated `Q` still requires a separately frozen statistical
resolution or equivalence margin.  The current burned pilots do not supply
that decision.

## 6. Relation to the preceding finite discriminator

[`GAUGE_VACUUM_PLAQUETTE_FULL_TWO_SLICE_STATIC_RHO_IDENTIFICATION_NARROW_NO_GO_NOTE_2026-08-22.md`](GAUGE_VACUUM_PLAQUETTE_FULL_TWO_SLICE_STATIC_RHO_IDENTIFICATION_NARROW_NO_GO_NOTE_2026-08-22.md)
rejects the particular `D_loc diag(rho_static)` forward ansatz on one finite
surface.  It does not establish a non-diagonal physical `Q`.

The present theorem removes that ansatz entirely: `Q_tilde` is measured from
the same full Wilson integral as `C_tilde`.  The exact identity (1) therefore
closes the estimator/interface construction requested by the preceding
packet.  It does not close the separate structure-selection problem.

The bundled `L_s=3`, `beta=6` Monte Carlo path now uses only burned pilot
seeds.  The former 2400-measurement fresh protocol was disabled after the
four-dimensional polynomial-null pilot failed to establish credible power at
the declared `10^-3` rejection level.  Pilot outputs exercise code and expose
diagnostics; they assign no positive-law or diagonal-no-go verdict.

## 7. Axiom and TOE decision

No axiom change is justified.  Equation (1) is a consequence of the supplied
Wilson measure and exact reweighting.  Equations (11), (13), and (18) are
representation-theoretic classifications.  None selects the Wilson action,
the coupling, a dynamics generator, a thermodynamic limit, or a physical
diagonal law from the Minimal Axioms.

Accordingly:

- the common-integral operator interface is a positive finite-theory result;
- no TOE obligation is retired;
- TOE lane percentages do not change;
- the gauge lane's next analytic discriminator is (17), not a larger replay
  of the underpowered polynomial-null design; and
- the main TOE portfolio may move to an axiom-facing root without losing this
  exact gauge result.

## 8. What is and is not established

Established:

- exact common-measure construction of the full middle form;
- exact forward identity before and after trivial-entry normalization;
- exact finite class-sector diagonal/convolution equivalence;
- exact full-kernel regular-translation characterization;
- exact counterexample separating the known finite symmetries from
  diagonality; and
- exact joint-Casimir scalar selector on `B_5`.

Not established:

- diagonality or non-diagonality of the actual Wilson `Q`;
- full-kernel regular-translation invariance of the Wilson environment;
- an equivalence bound for a numerically estimated `Delta_5`;
- removal of exponential character cutoff;
- coupling or volume transport, the thermodynamic plaquette value, or an
  action/dynamics selector; or
- any new axiom or TOE root closure.

## 9. No-Go Discipline Gate

The only negative statement in this note is the finite logical separation:
the properties exhibited by (15) do not, without an additional premise,
entail character diagonality.  No physical Wilson no-go is asserted.

### N1 - alternative route enumeration

The route families are normalized by mathematical object, mechanism, and
terminal obligation.

| Marker | Family | Mechanism and terminal obligation | Outcome |
|---|---|---|---|
| ATTEMPTED | Spectral decomposition of a positive self-adjoint matrix | Use positivity to select an eigenbasis and then identify it with characters. | (15) is positive definite but its eigenbasis mixes `chi_(0,0)` and `chi_(1,1)`, so positivity does not complete the character-basis identification. |
| ATTEMPTED | Commutant of irrep-conjugation swap | Decompose into the swap-even and swap-odd blocks and require each block to be one-dimensional. | The even block contains both characters in (15), so swap commutation permits their mixing. |
| ATTEMPTED | Simultaneous-conjugation kernel invariance | Use (14) to force dependence on `xy^(-1)`. | The kernel from (15) is separately class-invariant yet off-diagonal, so (14) is insufficient. |
| ATTEMPTED | Central-convolution reconstruction | Reconstruct a central `k_N` and use Schur orthogonality to force the matrix. | Theorem 2 succeeds exactly only after diagonality is supplied; treating reconstruction as its proof would be circular. |
| ATTEMPTED | Wilson-specific Ward identity or direct integration | Add (13), prove the joint-Casimir defect vanishes, or show off-diagonal cancellations directly. | This remains a valid route to physical diagonality, but it adds Wilson-specific content absent from the narrow implication tested by (15). It defeats a broad physical no-go, which this note therefore does not make. |

Five materially different families were checked.  The last remains open and
is preserved as the next gauge campaign rather than rhetorically retired.

### N2 - wall-independence audit

There are not two independent diagonal gates:

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| full-kernel regular translations / finite class-sector diagonality | yes | no | no |

Regular translations are the stronger sufficient condition.  Finite
class-sector diagonality alone is the exact obligation for the supplied
finite diagonal interface.  The note does not inflate these into two
independent walls.

### N3 - hidden-condition scan

The proof uses only the explicitly supplied finite Wilson measure, normalized
Haar measure, SU(3) characters, and the displayed finite-box definitions.
The diagnostic lattice, coupling, seeds, truncation, and normalization are
all explicit.  A phrase scan for the methodology warning list found no silent
physics premise.  The Wilson-specific statements are either linked context or
named as unproved continuation routes.

### N4 - residual matching

| Cited source | Source residual | Residual used here | Match and use |
|---|---|---|---|
| [`SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md), lines 1-12 and 37-50 | Algebraic equivalence for a supplied diagonal finite operator | Theorem 2 after diagonality is supplied | yes; positive algebra only |
| [`GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md`](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md), lines 107-136 and 254-265 | Independent mixed-link factorization; residual environment excluded | Why that theorem does not prove (13) for the spatially coupled full kernel | yes; proof-route scope only |
| [`GAUGE_VACUUM_PLAQUETTE_FULL_TWO_SLICE_STATIC_RHO_IDENTIFICATION_NARROW_NO_GO_NOTE_2026-08-22.md`](GAUGE_VACUUM_PLAQUETTE_FULL_TWO_SLICE_STATIC_RHO_IDENTIFICATION_NARROW_NO_GO_NOTE_2026-08-22.md), lines 240-259 and 462-465 | Static-rho plus local-factor forward conjunction | Physical common-integral `Q` structure | no; cited only as preceding context, never as evidence for nondiagonality |
| [`GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_CHARACTER_MEASURE_THEOREM_NOTE.md), lines 142-190 | Static boundary data versus stripped two-slice operator | Common-integral construction | no; not used as a negative witness |

Dropping the two nonmatching context citations leaves the exact witness (15)
and Theorems 2-4 self-contained.

### N5 - rhetoric and resolution audit

| Resolution | Executed? | Exact statement |
|---|---|---|
| per element | yes | The marked-weight cancellation and degree-one forward identity are checked pointwise. |
| per site | no | The diagnostic averages 81 faces and makes no site-resolved physics claim. |
| per mode | yes | The finite `B_1` counterexample and `B_5` joint-Casimir separation are exact. |
| per block | yes, diagnostic only | Burned-seed blocked calculations exercise covariance and resampling paths but do not certify diagonality. |
| lattice wide | no | Nothing is inferred across beta, volume, or the thermodynamic limit. |

The cached runner receipt carries the five matching required execution lines.

### N6 - partial-closure paths

The supplied-diagonal interface remains usable whenever a consumer explicitly
supplies diagonal coefficients.  Theorem 2 neither discards that partial
closure nor renames a general matrix as a diagonal vector.  Theorem 1 retires
the estimator-construction subproblem without adding physics: it replaces the
static comparator by an exact same-measure operator.  Theorem 4 converts the
remaining finite structure question into one scalar equality.  None of these
steps requires an axiom edit, and no proposed primitive is treated as active.

### N7 - strongest steelman

The counterexample says only that a short symmetry list is insufficient.  The
actual Wilson integral has locality and shared-link structure absent from
(15), and cancellations after all unmarked links are integrated could still
make every off-diagonal character element vanish.  A direct proof of the two
regular translations, an exact strong-coupling/tensor contraction, or a
resolved zero bound on (17) would establish the desired finite diagonality.
That is a concrete unclosed mechanism and terminal obligation, so any claim
that physical Wilson diagonality is impossible would be premature.  The note
is narrowed accordingly.

### N8 - cross-cycle echo

The gauge spatial-environment campaign previously tried to identify a static
boundary vector with a stripped source residual.  That route was reopened by
changing the primary object: Block 30 tested the full forward conjunction,
and this packet constructs the general same-measure operator instead of
renaming the vector.  The mechanism applies here and is executed in Theorem 1.
The earlier supplied-diagonal notes were also repaired by narrowing them to
conditional algebra rather than physical identification.  This packet keeps
that repair and adds the exact selector; it does not repeat the old universal
claim.

**No-Go Discipline status:** PASS for the narrow finite nonimplication in
(15); FAIL for any broader physical diagonal no-go, which is not shipped.

## 10. Verification

Run:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_general_middle_operator_common_integral_actual_l3_2026_08_22.py
```

The default path uses burned seeds and ends with `TOTAL: PASS=... FAIL=0`.
Its stochastic output is implementation evidence only.  The load-bearing
claims are the exact identities and counterexample above.
