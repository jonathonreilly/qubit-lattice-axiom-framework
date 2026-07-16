# SU(3) Wigner Intertwiner Engine — Block 1: (1,1) ⊗ (1,1)

**Date:** 2026-05-03

**Claim type:** positive_theorem

The representation-theoretic decomposition and all-\(g\) equivariance
statement are exact mathematical claims. The supplied matrices,
diagonalization, and residual checks are finite `complex128` numerical
witnesses. Independent re-audit owns ratification.

**Primary runner:**
[`frontier_su3_wigner_intertwiner_engine.py`](../scripts/frontier_su3_wigner_intertwiner_engine.py)

**Pinned output:**
[`frontier_su3_wigner_intertwiner_engine.txt`](../logs/runner-cache/frontier_su3_wigner_intertwiner_engine.txt)

## 1. Exact statement

The SU(3) adjoint tensor square decomposes as

```text
V_(1,1) ⊗ V_(1,1)
  ≅ V_(0,0) ⊕ V_(1,1)_s ⊕ V_(1,1)_a
    ⊕ V_(3,0) ⊕ V_(0,3) ⊕ V_(2,2)
  ≅ 1 ⊕ 8_s ⊕ 8_a ⊕ 10 ⊕ 10bar ⊕ 27.
```

The dimensions are

```text
1 + 8 + 8 + 10 + 10 + 27 = 64 = 8 × 8.
```

The Littlewood–Richardson decomposition gives the displayed irreducible
summands. Exchange of the two adjoint factors splits them as

```text
Sym²(8) = 1 ⊕ 8_s ⊕ 27,       dimensions 1 + 8 + 27 = 36,
Λ²(8)   = 8_a ⊕ 10 ⊕ 10bar,   dimensions 8 + 10 + 10 = 28.
```

The Littlewood–Richardson decomposition, canonical SU(3) Casimir formulas,
and Casimir invariance are standard representation-theory inputs. No
measured, fitted, observational, or lattice quantity enters this theorem.

## 2. Casimir convention and corrected channel labels

The runner uses the standard Gell-Mann normalization

```text
t_a = λ_a/2,     Tr(t_a t_b) = δ_ab/2.
```

For Dynkin label \((p,q)\), the canonical eigenvalues in this convention are

```text
C2(p,q) = (p² + q² + pq + 3p + 3q)/3,
C3(p,q) = (p-q)(2p+q+3)(p+2q+3)/18.
```

The sign is anchored independently of the tensor-product eigensolver by
directly contracting \(d_{abc}t_at_bt_c\) in the fundamental and
antifundamental representations:

```text
C3(1,0) = +10/9,       C3(0,1) = -10/9.
```

Consequently,

```text
C3(3,0) = +9  for the decuplet 10,
C3(0,3) = -9  for the antidecuplet 10bar.
```

With

```text
H = C2_total + α E + β C3_total,
α = √2,        β = √3/7,
```

where \(\alpha,\beta\) are auxiliary channel-separation coefficients with no
physical content. The executable channel table is:

| Channel | Dynkin label | Rank | Exchange | C2 | C3 | H |
|---|---:|---:|---:|---:|---:|---:|
| `1` | (0,0) | 1 | +1 | 0 | 0 | 1.4142136 |
| `8_a` | (1,1) | 8 | -1 | 3 | 0 | 1.5857864 |
| `8_s` | (1,1) | 8 | +1 | 3 | 0 | 4.4142136 |
| `10` | (3,0) | 10 | -1 | +6 | **+9** | **6.8127089** |
| `10bar` | (0,3) | 10 | -1 | +6 | **-9** | **2.3588640** |
| `27` | (2,2) | 27 | +1 | 8 | 0 | 9.4142136 |

This corrects the former reversal of the `10` and `10bar` rows.

## 3. Exact projectors and numerical construction

Let the exact \(C_2\) spectrum on \(8\otimes8\) be
\(\{0,3,6,8\}\), and define its Lagrange spectral polynomials

```text
L_c(C2) = ∏_(c'≠c) (C2-c'I)/(c-c').
```

Let \(S_\pm=(I\pm E)/2\). The six exact joint spectral projectors can be
written as

```text
P_1     = L_0(C2) S_+,
P_8a    = L_3(C2) S_-,
P_8s    = L_3(C2) S_+,
P_10    = L_6(C2) S_- (I + C3/9)/2,
P_10bar = L_6(C2) S_- (I - C3/9)/2,
P_27    = L_8(C2) S_+.
```

These expressions are exact on \(8\otimes8\). The quadratic and cubic
Casimirs commute with the diagonal SU(3) action because they arise from
central invariant tensors, and exchange commutes with the equal action on
the two factors. Functional calculus therefore gives

```text
[D(g)⊗D(g), P_channel] = 0
```

for every \(g\in SU(3)\), exactly.

The factors \((I\pm C_3/9)/2\) are not standalone projectors on the full
space: every zero-\(C_3\) sector would receive eigenvalue \(1/2\). They are
used only after \(L_6(C_2)S_-\) restricts to the 20-dimensional decuplet
pair, where the cubic spectrum is exactly \(\{-9,+9\}\).

The runner also diagonalizes the finite `complex128` matrix \(H\), groups its
eigenvectors by the six expected eigenvalues, and forms numerical projectors
\(P=VV^\dagger\). Floating-point diagonalization supplies reproducible
matrix witnesses and an orthonormal CG basis; it is not described as
numerically exact and numerical residual size is not the proof of the
arbitrary-\(g\) statement.

## 4. Executable validation

The runner reports

```text
SUMMARY: THEOREM PASS=12 FAIL=0
```

with explicit tolerances

```text
operator/projector tolerance = 1e-10,
eigenvalue matching tolerance = 1e-8,
equivariance witness tolerance = 1e-10.
```

The checks include:

1. Gell-Mann structure-constant symmetry and normalization.
2. Hermitian adjoint generators and the SU(3) Lie algebra.
3. \(C_2(1,1)=3\) and \(C_3(1,1)=0\).
4. Independent fundamental/antifundamental confirmation of the canonical
   cubic-Casimir sign.
5. Hermiticity and pairwise commutation of \(C_2\), \(E\), and \(C_3\),
   together with agreement between the total \(C_3\) and an independently
   expanded coproduct formula.
6. Six separated \(H\) clusters with ranks `1,8,8,10,10,27`.
7. Orthonormality of the returned numerical eigenbasis.
8. For every channel projector: Hermiticity, idempotence, rank, and the
   expected scalar \(C_2,E,C_3\) actions.
9. Pairwise projector orthogonality and completeness.
10. Agreement between the eigensolver projectors and the independent
    invariant-polynomial construction.
11. Hostile controls:
    - the former swapped `10`/`10bar` labels miss the observed \(C_3\) values
      by 18;
    - a global \(C_3\) sign flip disagrees at order one with the independent
      coproduct expansion;
    - the wrong antifundamental convention \(+t_a^*\) gives the fundamental
      rather than conjugate cubic sign and violates the SU(3) Lie algebra
      with residual 1;
    - using \((I+C_3/9)/2\) on the full space gives rank 54 and idempotence
      residual \(1/4\), while restricting first to \(C_2=6,E=-1\) gives the
      rank-10 decuplet projector;
    - omitting \(C_3\) leaves only five clusters and one rank-20
      \(C_2=6,E=-1\) projector whose restricted \(C_3\) spectrum is
      \([-9,+9]\).
12. For deterministic seeds `11,29,47,83,101`,
    \(D(g)\otimes D(g)\) commutes numerically with \(C_2\), \(E\), \(C_3\),
    and each of the six projectors.

The observed decuplet blocks printed by the runner are

```text
10bar (0,3): H=2.3588640, (C2,E,C3)=(6,-1,-9),
10    (3,0): H=6.8127089, (C2,E,C3)=(6,-1,+9).
```

## 5. Importable API

The runner preserves the original primitive API and adds executable channel
projectors:

| Function | Result |
|---|---|
| `gellmann_basis()` | eight standard Gell-Mann matrices |
| `structure_constants()` | numerical `f_abc, d_abc` arrays |
| `adjoint_generators(f)` | eight adjoint generators |
| `adjoint_matrix(g, lam)` | adjoint representation matrix \(D(g)\) |
| `random_su3(seed)` | deterministic seeded SU(3) element |
| `adjoint_casimir(T)` | adjoint quadratic Casimir |
| `cubic_casimir(T, d)` | cubic Casimir for supplied generators |
| `tensor_product_casimir(T)` | total \(C_2\) on \(8\otimes8\) |
| `tensor_product_cubic_casimir(T, d)` | total \(C_3\) on \(8\otimes8\) |
| `tensor_product_cubic_casimir_coproduct_expansion(T, d)` | independently expanded total \(C_3\) |
| `exchange_operator(dim)` | tensor-factor exchange |
| `cg_decomposition(C2, E, C3)` | numerical \(H\) eigenvalues/eigenbasis |
| `spectral_channel_projectors(...)` | six eigensolver spectral projectors |
| `invariant_polynomial_projectors(...)` | independent exact-polynomial projectors evaluated numerically |
| `canonical_su3_casimirs(p, q)` | exact rational \(C_2,C_3\) formula values |

## 6. Downstream boundary

The downstream
`SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md` uses only the
unordered conjugate pair `10 + 10bar` in its fusion-counting rank
calculation, and its runner re-bundles its own primitives rather than
importing this runner. The label correction therefore changes no Block 2
formula, rank, or API call. Block 3 and later cube/tensor-network blocks
carry only dependency references and do not pin either corrected eigenvalue
label. The filename is deliberately backticked here because this is a
downstream context pointer, not a load-bearing dependency of Block 1.

## 7. Scope and audit handoff

In scope:

- the exact SU(3) decomposition of \(8\otimes8\);
- exact joint channel identification by \(C_2,E,C_3\);
- finite numerical construction and validation of matrix representatives.

Out of scope:

- the four-fold Haar projector beyond its use as a downstream consumer;
- cube geometry, tensor-network contractions, and plaquette values;
- any audit verdict or retained-grade assignment.

```yaml
claim_id: su3_wigner_intertwiner_block1_theorem_note_2026-05-03
note_path: docs/SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md
runner_path: scripts/frontier_su3_wigner_intertwiner_engine.py
claim_type: positive_theorem
deps: []
```

## 8. Reproduction

```bash
python3 scripts/frontier_su3_wigner_intertwiner_engine.py
```

The SHA-pinned cache linked above is regenerated from the runner. Its stdout
payload must match live stdout after excluding the cache writer's delimiter
newline.
