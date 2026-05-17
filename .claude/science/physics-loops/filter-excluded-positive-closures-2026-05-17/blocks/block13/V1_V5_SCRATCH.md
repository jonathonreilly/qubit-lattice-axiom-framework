# Block 13 V1-V5 Scratch — GVP infinite-hierarchy obstruction

Row: `gauge_vacuum_plaquette_infinite_hierarchy_obstruction_note`
Brief-stated state: 630 desc, unaudited.
Audit-ledger actual state: `audited_clean` / `effective_status=retained_no_go`
(audit_date 2026-05-12), claim_type `no_go`.

## Re-grounding under audit-ledger reality

The brief asks for "POSITIVE closure on the infinite-hierarchy obstruction
— derive it OR prove a tight no-go on the proposed escape." The parent
no-go is already retained_clean. The constructive target is therefore a
**sharpened structural theorem** layered on top of the parent no-go:
not "K_1 is not a polynomial of any finite order" (parent), but the
much stronger structural property that **every even-order Taylor
coefficient of K_1(t) on U(1) is strictly nonzero with alternating
sign**, and the odd-order coefficients vanish identically.

This is a tight positive theorem (not a no-go) that uses only A_min
admitted inputs (U(1) Bessel structure already in the parent's BA-1—BA-3
list and elementary ODE).

## Distinct angles considered

### V1 — Direct quantitative bound on the rate at which K_1 fails to truncate

Bound `||K_1 - T_N K_1||_∞` (uniform error of the order-N truncation on
some compact β-window) by a closed expression in N. Reject reason:
duplicates the existing `hierarchy_obstruction_lemmas` content (polynomial
growth bound L4). The lemmas already give a non-truncation conclusion;
adding a uniform-norm bound is a decoration not a distinct theorem.

### V2 — Multi-group sharpening: extend to SU(2), SU(3)

Prove a density-of-nonzero-Taylor-coefficient theorem for SU(2) and
SU(3) generators. Reject reason: requires bringing in SU(N) Haar-character
machinery that is in the parent's BA-1 only as an existence statement
("non-trivial character integrates to zero"). Computing the recurrence
for log Z_{SU(N)}(t) requires additional ODE structure (Weingarten /
character orthogonality at higher orders) that is **not** admitted at
parent BA precision. Out of scope for A_min.

### V3 — Recurrence for the full Wilson lattice K_L(t)

Derive a global generating recurrence for K_L on a finite L^4 lattice
under diagonal source. Reject reason: requires the explicit
finite-volume Wilson cumulant generator, which is exactly the unsolved
analytic gap the parent no-go names. Solving it would close P(6) and
is far out of scope.

### V4 — Sign of the parent's contradiction strengthened to "K_1(t) > 0 strict for t > 0"

Refine the parent claim to: `K_1(t) > 0` strictly for `t > 0` (not just
K_1(t) → ∞ as t → ∞). Reject reason: trivial (Z_1(t) > Z_1(0) = 1 by
monotone convergence on positive measure → log Z_1(t) > 0). Already
implicit in (L2.b) of the lemma companion. Decoration not a new theorem.

### V5 — Riccati-derived density and sign-alternation theorem on U(1) (CHOSEN)

The U(1) one-plaquette generator `K_1(t) = log I_0(t)` has derivative
`r(t) = I_1(t)/I_0(t)` satisfying the Riccati ODE

    t r' + r + t r² = t,  r(0) = 0,  r'(0) = 1/2.

This ODE follows directly from the Bessel ODE `I_0'' + I_0'/t - I_0 = 0`
(elementary; standard textbook; already implicit in BA-3 entire-function
representation of Z_1).

Substituting `r(t) = Σ_{n≥0} a_n t^(2n+1)` (odd power series, forced
because I_1 is odd) gives the explicit recurrence

    a_0 = 1/2,
    a_n = -(1/(2(n+1))) · Σ_{j+k=n-1, j,k≥0} a_j a_k    for n ≥ 1.

**Claim (D1-D3) — Density and Sign-Alternation on U(1):**

(D1) **Parity**: `c_n[K_1] = 0` for all odd n ≥ 1.

(D2) **Density on even orders**: `c_{2k}[K_1] ≠ 0` for all k ≥ 1.

(D3) **Sign alternation**: `sign(c_{2k}[K_1]) = (-1)^(k+1)` for all k ≥ 1.

**Proof sketch (induction on n for a_n):**

Base: a_0 = 1/2 > 0, sign (-1)^0 = +. ✓

Step: Assume sign(a_m) = (-1)^m and a_m ≠ 0 for all 0 ≤ m < n. Then
each summand a_j a_k in `Σ_{j+k=n-1} a_j a_k` has sign
`(-1)^j · (-1)^k = (-1)^(j+k) = (-1)^(n-1) = -(-1)^n`. All summands are
strictly nonzero (by IH) and share the same sign, so the sum is
strictly nonzero with sign `-(-1)^n`. Then

    a_n = -(1/(2(n+1))) · [sum with sign -(-1)^n]
        = (1/(2(n+1))) · (-1)^n · (positive)

so sign(a_n) = (-1)^n and a_n ≠ 0. ✓

Since `c_{2k}[K_1] = a_{k-1}/(2k)`, the sign of c_{2k} is `(-1)^(k-1) =
(-1)^(k+1)`, confirming (D2)–(D3). (D1) follows from K_1 being even
(because Z_1(t) = I_0(t) is even in t, which itself follows from
Z_1 = ∫ exp(t cos θ) dθ/(2π) and the shift θ → θ + π takes
cos θ → -cos θ but leaves the integration measure invariant).

## V5 distinct from parent

Parent claim: "K_1 is not a polynomial of any finite degree N".
V5 claim: "Every even-order Taylor coefficient of K_1 is strictly
nonzero with sign (-1)^(k+1), and every odd-order coefficient vanishes."

V5 is strictly stronger:
- Parent: ∃ k arbitrarily large with c_{2k} ≠ 0. (Negation of finite truncation.)
- V5: ∀ k ≥ 1, c_{2k} ≠ 0 with explicit sign and nonvanishing recurrence.

The escape hatch the parent leaves open ("maybe even-order coefficients
have gaps and sparse truncation works") is ruled out: there are no gaps,
all even-order coefficients are nonzero and sign-alternating.

## V5 distinct from companion `hierarchy_obstruction_lemmas`

The lemma companion (BA-1)–(BA-4) gives endpoint identities and the
finite-Taylor-support ⟺ polynomial bridge. V5 gives the **density**
and **sign-alternation** at every even order via an explicit recurrence.
The lemmas conclude "K_1 cannot truncate"; V5 concludes "every even-order
coefficient is strictly nonzero with alternating sign and the recurrence
is explicit". Different theorem, different proof structure (lemmas use
compact Laplace concentration; V5 uses the Bessel ODE and an inductive
sign argument on the Riccati recurrence).

## A_min check

- A1 (Cl(3) local algebra) and A2 (Z^3 substrate) suffice for the
  ambient gauge framework.
- U(1) plaquette `F(U) = cos θ` and `Z_1(t) = I_0(t)` are admitted in
  the parent's BA-1, BA-3.
- Bessel ODE `I_0'' + I_0'/t - I_0 = 0` is elementary; the Riccati
  equation `t r' + r + t r² = t` for `r = I_1/I_0` follows by a
  one-line calculation from the Bessel ODE and `I_0' = I_1`,
  `I_1' = I_0 - I_1/t` (both standard Bessel identities).
- No new admissions, no new primitives. Within A_min.

## V5 chosen.

Deliverable: positive narrow theorem on the row, sharpening the parent
no-go. Type: `positive_theorem`, narrow scope. Does NOT change the
parent's `retained_no_go` status, and does NOT close analytic `P(6)`,
`chi_L(beta)`, or an explicit nonpolynomial hierarchy solution.

## Runner plan

1. Compute the Taylor expansion of `K_1(t) = log I_0(t)` symbolically
   using `sympy` to high order (N = 60). Verify (D1) odd coefficients
   vanish, (D2) even coefficients nonzero, (D3) alternating signs.
2. Independently compute `r(t)` via the recurrence and verify the
   recurrence matches the symbolic Taylor of `I_1/I_0`.
3. Verify the sign induction explicitly: for each n, check
   sign(a_n) = (-1)^n and a_n ≠ 0.
4. Cross-check: compute the same coefficients from
   `log I_0(t) = Σ_{m≥1} (-1)^(m+1) g(t^2)^m / m` where
   `g(s) = Σ_{k≥1} s^k / (4^k k!^2)`, and verify identical c_{2k}.
5. Numerical sanity: confirm the sign-alternation persists for very
   high order (N ~ 100) using floating-point Taylor.

Hard rules: A_min only.
