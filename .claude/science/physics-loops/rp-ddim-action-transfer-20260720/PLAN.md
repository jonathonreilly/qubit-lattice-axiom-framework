# d-dimensional action-level many-body transfer identity — plan

> **SUPERSEDED 2026-07-24 (review-loop round 2, PR #5549).** This is
> the round-0 planning record, preserved unedited as provenance. Its
> framing — "action-level", "the RP note derives the full many-body
> identity from the action", and `C = 1` "DERIVED" — was RETRACTED
> before landing. The landed claim is narrower: grade (A) the
> d-dimensional CLASSICAL two-step algebra, derived; grade (B) the
> Fock assembly, CONDITIONAL on a supplied selection prescription and
> a supplied exponential coherent-kernel form. The action-to-Fock
> operator identification is NOT discharged — supplying that kernel
> form IS the coherent-state form of the identification. See
> `REVIEW_HISTORY.md` "Round 2" and the landed note's Non-Claims.

Date: 2026-07-20. Supervisor plan + ground truth, recorded BEFORE
reading any worker deliverable.

## The item

Block11 (PR #5547) constructs `T̂²_d := Γ(t_d)` and honestly labels
it a CONSTRUCTION under the vacuum normalization convention (its
steelman (a): a d-dependent scalar is not excluded; the action-level
identity named open). The landed corner-note names the free-surface
operator identification as the supplied input at `1+1d` only; the
landed dispersion note is one-particle-only by its own boundary; the
RP-positivity note (AXIOM_FIRST_RP_TWO_STEP..., 2026-05-28) derives
the full many-body identity from the action — at `1+1d` only
(Steps 1-4 + 3b). Nothing in the repo derives the d-dim many-body
two-step transfer from the d-dim action. This block does exactly
that, at free `U = 1`, on the dispersion note's own surface.

Non-collision: the owner's bridge campaign (draft #5523) named
discriminators (overlap menus, NN normalization, multi-edge response
transfer) are untouched; PR #5546 (kcpt census) untouched.

## Ground truth (mine, pre-worker)

1. **Template = RP note Steps 3b-4.** Per mode: classical two-step
   block -> spectral split -> forward (decaying) channel by the
   finite-norm/finite-action argument -> one-mode coherent-state
   kernel `<z̄'|T₂|z> = exp(z̄' λ z)` -> induced exterior operator
   EXACTLY `diag(1, λ)` -> assembly over modes.
2. **C = 1 is DERIVED, not conventional, on this route:** the
   coherent kernel's vacuum matrix element is exactly 1 per mode
   (constant term of `exp(z̄'λz)`), so the assembled operator fixes
   the vacuum with coefficient 1 — discharging block11's scalar
   caveat on the free surface.
3. **d-dim structure expectation:** with `η_0 = 1` and spatial
   phases carrying the `(−1)^t` alternation, the full spatial hop at
   fixed reduced momentum `k` is a `2^d x 2^d` corner-block matrix
   `S(k)` mixing the taste corners `p_r = k + πr`; the two-step
   block depends on `S(k)²` (whose eigenvalues are `Σ_μ sin² p_μ`,
   taste-degenerate since `sin²(k+π) = sin² k`), so per
   `S`-eigenvector the recursion is IDENTICAL to `d = 1` with
   `sin² p -> Σ_μ sin² p_μ`, eigenvalues `e^{±2E_d}`,
   `E_d = arcsinh(sqrt(m² + Σ sin²))`. MUST be verified against the
   dispersion note's actual algebra, not assumed (never write from
   memory).
4. **Assembly authorities already landed:** the corner-note's
   finite-mode theorem (canonical intertwiner uniqueness; positive
   log; trace `Tr Γ = det(1+t)`; `Γ(⊕) = ⊗Γ`). The new work is the
   ACTION-side derivation per mode + the forward-channel selection
   at general d + C = 1 + the assembly statement.
5. **Result displays expected:** `T̂²_d = Γ(t1⁽²⁾_d) = B†B`,
   `Ĥ_d = −log(T̂²_d)/(2a_τ) = dΓ(E_d-diag) ≥ 0` (the d-dim P2),
   `Tr T̂²_d = det(1 + t1⁽²⁾_d)`, mode count `(L/2)^d 2^d = L^d`.
6. **Gates:** exact sympy. d = 2, L = 2 full Fock (4 modes, 16-dim)
   everything dense-exact; d = 3, L = 2 (8 modes, 256-dim)
   STRUCTURED (diagonal/occupation-basis products, intertwiner via
   action on basis vectors, not dense 256x256 products); classical
   blocks REBUILT from the action (phases included) at d = 2 and
   d = 3 small L, eigenvalues vs `e^{±2E_d}` symbolic; forward
   projector identities; per-mode coherent->exterior bridge
   symbolic; vacuum element = 1 exact; trace = det instance.
7. **Pitfalls:** dispersion-note conventions must be quoted (phase
   ordering, fold definition, reduced-momentum domain, even
   periods); L = 2 per direction means `k = π/2` only (sin² = 1) —
   fine for instances, but classical rebuild should also run one
   L = 4 spot at d = 2 one-particle level; no gauged claims; no
   single-step no-go claims at d dims unless actually derived; no
   U-integrated; Euclidean ≠ real time; no audit verdicts.

## Worker split (Opus 4.8 max, disclosed)

- Worker A (scout): verbatim extraction from the dispersion note
  (+ the landed corner-note + RP note): conventions, corner algebra,
  per-k block, eigenvalue derivation, positivity window,
  one-particle-boundary sentences, even periods; precise gap list.
- Worker B (math): execute the derivation per ground truth items
  1-5 with exact-gate designs per item 6; flag every deviation.

Supervisor grades both against this file, then note + runner +
battery + codex lens + cap evaluation + PR (stacked on main).
