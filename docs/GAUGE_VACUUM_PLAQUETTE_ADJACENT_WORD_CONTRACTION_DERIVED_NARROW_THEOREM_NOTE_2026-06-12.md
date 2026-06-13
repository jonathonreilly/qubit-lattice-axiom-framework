# Gauge-Vacuum Plaquette Adjacent-Word Contraction Derived Narrow Theorem

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite derivation of the adjacent-word contraction and
finite-packet boundary readout used to re-read the tensor-word Perron ladder at
`beta = 6`, `NMAX = 4`, `MODE_MAX = 80`, with the existing source-sector
`NMAX = 7`, `MODE_MAX = 200` composition. This note does not compute the full
physical 3D unmarked spatial Wilson environment, the untruncated
tensor-transfer Perron state, an `L_perp` limit, a full rim-boundary
`eta_beta^env` evaluation, an analytic plaquette value, or a canonical
repinning.

**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [`scripts/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py`](../scripts/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.txt`](../logs/runner-cache/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.txt)

The earlier ladder measurement packet is context only, not a one-hop authority.

## One-Hop Authorities

- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the temporal-gauge same-link mixed Wilson kernel and its per-link
  matrix-coefficient convolution eigenvalue.
- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the tensor-transfer ingredient language and the open boundary-character
  law.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `tensor_word` packet and its explicit unit-vector
  boundary readout.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Schur-orthogonality and character-convolution dictionary.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the finite source-sector Perron machinery with `rho` supplied as input.
- [PLAQUETTE_SELF_CONSISTENCY_NOTE.md](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  for the admitted comparison/reuse number `0.5934` used only in the fenced
  distance block.

No literature value, new axiom, external citation, fitted selector, or new
comparator number is used. Existing finite inputs are restated on their scoped
surfaces.

## Derivation

The temporal-gauge mixed-kernel authority states that the mixed plaquette
holonomy reduces to

```text
U_p = U_(tau+1)(x, mu) U_tau(x, mu)^(-1).                                (1)
```

It also states the per-link convolution identity

```text
integral_G K_(x,mu)(U', U) lambda_(i,j)(U) dU
  = (c_lambda(beta) / d_lambda) lambda_(i,j)(U'),                         (2)
```

and, in the proof, the Schur step

```text
integral_G chi_mu(U' U^(-1)) lambda_(i,j)(U) dU
  = delta_(mu,lambda) (1 / d_lambda) lambda_(i,j)(U').                    (3)
```

The tensor-transfer authority says that one slice step expands the spatial
plaquette factors in characters and integrates the shared slice links by Haar
orthogonality / Peter-Weyl decomposition. Therefore two adjacent tensor words
added in the transverse direction do not merely share a label. They share the
same link variable with inverse orientation in the neighboring word.

The SU(3) convolution dictionary supplies the character form of the same
matrix-element contraction:

```text
integral chi_(p,q)(V W^(-1)) chi_(p',q')(W) dW
  = delta_((p,q),(p',q')) chi_(p',q')(V) / d_(p,q).                      (4)
```

After substituting `V = A B` and moving fixed factors into the two traces, this
is the shared-link identity

```text
integral_SU(3) chi_lambda(U A) chi_mu(U^dagger B) dU
  = delta_(lambda,mu) chi_lambda(A B) / d_lambda.                         (5)
```

By contrast, the unit-weight character-level identity is the special case with
no nontrivial matrix-element propagation through the shared link:

```text
integral_SU(3) chi_lambda(U) chi_mu(U^dagger) dU = delta_(lambda,mu).       (6)
```

Equation `(5)`, not `(6)`, is the adjacent-word situation in the cited
tensor-transfer construction because adding one transverse site leaves a
shared link variable inside the neighboring traces before Haar integration.

## Small Theorem

Let `lambda_i` and `lambda_(i+1)` be adjacent word labels in the finite
tensor-word packet. The adjacent bond factor derived from the quoted
shared-link Haar integral is

```text
b(lambda_i, lambda_(i+1))
  = delta_(lambda_i, lambda_(i+1)) / d_(lambda_i).                        (7)
```

For `k` words, using the in-flight ladder notation

```text
D_k(lambda_1, ..., lambda_k) = product_i D[lambda_i],
M_k = M tensor ... tensor M,
```

the derived finite transfer is

```text
T_k = D_k M_k D_mid M_k^T D_k,

D_mid(lambda_1, ..., lambda_k)
  = D_k(lambda_1, ..., lambda_k)
    * product_(i=1 to k-1) delta_(lambda_i, lambda_(i+1)) / d_(lambda_i).
                                                                            (8)
```

This is the matrix-element adjacent-word contraction. The character-level
bond would omit the factor `1 / d_(lambda_i)` and is not the shared-link Haar
integral in `(5)`.

## Boundary Readout

The tensor-transfer authority names the open full boundary-character target as

```text
z_(p,q)^env(beta)
  = <chi_(p,q), (T_beta^env,tensor)^(L_perp-1) eta_beta^env>,

rho_(p,q)(beta)
  = z_(p,q)^env(beta) / z_(0,0)^env(beta).                                (9)
```

It describes `eta_beta^env` as the exact positive boundary state induced by
the rim coupling, and explicitly leaves its full evaluation open.

The cited finite tensor-word packet supplies one explicit boundary vector
on its bounded surface:

```text
boundary0 = e_(0,0),
amp := tensor_word * boundary0.                                           (10)
```

It verifies nonnegative boundary amplitude under this unit-vector readout.
No quoted identity in the cited finite packet replaces `boundary0` by an
all-label summation functional. Therefore, on the cited finite packet, the
boundary readout corresponding to `(9)` fixes unmarked word boundary labels to
the trivial channel:

```text
rho_lambda^(k)
  = psi_k(lambda, (0,0), ..., (0,0))
    / psi_k((0,0), (0,0), ..., (0,0)).                                    (11)
```

This is the `trivial_slice` readout in the in-flight ladder runner. The
`marginal` readout would require an all-label boundary/counit for the other
word slots. That object is not supplied by the cited finite packet.

## Derived Re-Read

The runner re-reads the finite ladder under the derived branch only:

```text
adjacent contraction: matrix_element, same inverse-link orientation
boundary readout: trivial_slice
```

The one-word anchor is unchanged:

```text
one-word tensor Perron eigenvalue: 1.012369912748
rho_tw1(1,0): 0.378514922317
P_tw1(6): 0.434215413260
```

At the default finite box:

| words | derived branch | `rho_(1,0)` | `rho_(1,1)` | `P(6)` | direction vs one-word distance to `0.5934` |
|---:|---|---:|---:|---:|---:|
| 1 | one-word anchor | `0.378514922317` | not used here | `0.434215413260` | baseline |
| 2 | matrix-element / trivial-slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |
| 3 | matrix-element / trivial-slice | `0.211265869825` | `0.162259799480` | `0.429196712321` | away by `0.005018700938` |

The existing context-only matrix-element / marginal three-word value
`P = 0.592817119605` is not selected by this cited finite-packet boundary
derivation. It remains a convention-sensitive measurement, not the derived
re-read here.

## Fenced Comparator Distances

The canonical comparison number below is admitted only as a comparison/reuse
number, not as a derived value, fit target, or repinning input.

```text
P_tw1 = 0.434215413260
|P_tw1 - P_loc_reference| = 0.018191745785
|P_tw1 - P_triv_reference| = 0.011683673613
|P_tw1 - 0.5934| = 0.159184586740

two-word matrix_element trivial_slice:
P = 0.429196712321
|P - P_loc_reference| = 0.023210446723
|P - P_triv_reference| = 0.006664972674
|P - 0.5934| = 0.164203287679
direction_vs_one_word = away by 0.005018700938

three-word matrix_element trivial_slice:
P = 0.429196712321
|P - P_loc_reference| = 0.023210446723
|P - P_triv_reference| = 0.006664972674
|P - 0.5934| = 0.164203287679
direction_vs_one_word = away by 0.005018700938
```

This is a finite-packet negative for the `0.5928` marginal branch under the
cited boundary vector. It is not a statement that no future full
rim-boundary theorem could select a different positive `eta_beta^env`.

## No-Go Discipline Gate

This section scopes the negative boundary above. It does not claim that all
future rim-boundary routes fail.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Character-level adjacent bond | Does not match the shared-link identity `(5)` because the quoted Schur contraction carries `1 / d_lambda`. | ATTEMPTED |
| Matrix-element adjacent bond with marginal readout | The bond is derived, but the marginal readout is not the cited finite-packet boundary vector `(10)`. | ATTEMPTED |
| Conjugate-orientation bond | The inverse-link identity is same-label in `(4)`; conjugation-swap symmetry can make finite displayed values agree, but it does not supply a marginal boundary. | ATTEMPTED |
| Full positive rim state `eta_beta^env` | The tensor-transfer note names it as open and does not evaluate it; a later full-rim theorem would require a re-read. | NAMED RESIDUAL |
| Older finite witness `eta_packet` shape | That packet is not one of the one-hop authorities for this derivation and is itself scoped as a finite witness, not the actual Wilson environment. | NAMED RESIDUAL |

**N2 wall independence.** The collapsed residual set is: finite word count and
finite truncations; no full physical 3D environment computation; no
untruncated convergence / `L_perp` limit; no evaluated full rim-boundary
`eta_beta^env`. Closing the full rim-boundary evaluation would not by itself
remove finite-box and untruncated-limit residuals.

**N3 hidden-wall scan.** The phrases "by construction" and "standard" are
avoided as load-bearing proof steps here. "Canonical" appears only in the
fenced comparison/reuse-number context and in the named residual "no canonical
repinning"; it is non-load-bearing. The load-bearing steps are the quoted
identities `(1)`-`(6)` and the explicit boundary vector `(10)`.

**N4 residual matching.** The in-flight ladder residual was the unresolved
adjacent contraction and boundary readout convention. This note attacks that
same finite-packet residual only. It does not cite prior negative rows as
witnesses against the full physical rim problem.

**N5 rhetoric audit.** The negative statement is at finite-packet resolution:
the cited finite-packet boundary does not select the marginal readout. No
lattice-wide or full-environment negative is asserted.

**N6 partial-closure path scan.** A future full rim-boundary theorem or a
repo-ratified boundary convention could select a different `eta_beta^env`.
That path is not blocked here; it is a named residual.

**N7 steelman.** A hostile reviewer can argue that the true
`eta_beta^env` in `(9)` need not equal the finite packet's `boundary0`, and a
full rim-lift could produce a positive vector whose effective readout behaves
more like the marginal branch. This is a valid objection to any broader claim,
so the present note is narrowed to the cited finite packet and does not
promote the trivial-slice branch to the full physical boundary state.

**N8 cross-cycle echo.** Similar boundary-state residuals appear in the
spatial-environment transfer/tensor-transfer lane as open full-rim targets.
This note does not treat those residuals as retired.

Gate result: PASS for the bounded finite-packet negative only.

## Reviewer Addition (2026-06-12): the Two/Three-Word Stationarity Is a Measured Slice Identity

The exact agreement of the derived two- and three-word readouts is measured,
not yet derived, and the cheap explanation fails: the three-word Perron
vector is NOT rank-one across the outer word (second/top singular ratio
`2.4e-2` under the `(word0 word1 | word2)` reshape), so the outer word does
not factor off as a scalar at the vector level. What holds instead, at
machine precision, is SLICE PROPORTIONALITY: the all-trivial-except-word0
slice of the three-word Perron vector equals the two-word slice times one
common scalar (`0.025986536153` at this box; per-weight ratio spread
`1.4e-16`). The k-independence of the derived trivial-slice readout follows
from that proportionality. The closed slice eigen-identity that forces it —
presumably a fixed-point equation satisfied by the trivial-slice components
independently of word count under the matrix-element bond — is the named
follow-up lemma; until it is derived, the stationarity is carried here as a
machine-precision measurement with the factorization explanation excluded.

## Named Residuals

- finite word count only;
- finite dominant-weight box and finite Bessel mode support only;
- no physical 3D unmarked spatial Wilson environment computation;
- no all-weight or untruncated convergence proof;
- no `L_perp` limit;
- no evaluated full rim-boundary `eta_beta^env`;
- no analytic `P(6)`;
- no canonical repinning.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py
```

Expected tail:

```text
TOTAL: PASS=28, FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_adjacent_word_contraction_derived_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
