# Assumptions and imports

## Positive simple-turning-point Airy module — 2026-09-24

| Input | Role | Status / boundary |
|---|---|---|
| Five-residue scalar Jacobi recurrence and its exact link coefficients | Defines the finite-spin transfer and its frozen limit | Imported from the local transfer note; its identification with the supplied one-vacancy physical model remains conditional. |
| Compact energy set `Lambda subset (0,4)` | Keeps `a_lambda=sqrt(1-lambda/4)` and `w_a=lambda/4` uniformly away from 0 and the physical endpoints | The estimate is not uniform as lambda approaches 0 or 4. |
| Positive turning point `u=a_lambda` with `cos(k)=-1` | Produces a simple parabolic five-site cell and the Airy scale `S^-2/3` | The proof covers a fixed neighborhood containing no other `sin(5k)=0` root; other Bragg layers are handled by separate bounded notes. |
| Fixed Jordan basis, fixed edge similarity, and cell sign | Fixes the sign and orientation of the Airy generator | Exact for the displayed transfer; the symbolic runner independently checks the lower-left coefficient and rejects a factor-of-two mutation. |
| Taylor, Euler-product, and WKB homological estimates | Control the inner fixed window and its allowed-side overlap | Proved locally in the note. Remote forbidden propagation, finite-endpoint selection, the negative turn, quantization, and prepared overlaps remain open. |

No framework axiom, approved primitive, measured datum, or fitted parameter
enters this scalar-transfer calculation. No axiom or primitive update is
proposed.

The proof candidate is conditional on the supplied six-site one-vacancy construction and its 15-residue integer-spin link table in `docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md` and `docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`. Their exact main-revision hashes are pinned in the scientific notes and runners; current main at campaign start was `c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6`.

| Input | Status | Consequence if absent or changed | Check |
|---|---|---|---|
| Integer-spin path (I_S=[-5S,5S-4]) and hop factors | Supplied condition | Changes the Jacobi coefficients, path reflection, and asymptotic estimates | Exact coefficient reconstruction in paired runner; source hash pin |
| First-mark preparation \(|0\rangle\) in the selected winding component | Supplied physical identification | Changes initial spectral amplitudes and the scalar (q_S) | Upstream fast-vacancy and zero-mode notes |
| Generator (G_S=N_S^2-CN_S), (C=S(S+1)) | Supplied dynamics plus exact algebraic reduction | Changes the fast phase (tCN_S) and prepared profile | Small dense exponential check and exact factorization |
| Period-three readout (O=(I+V+V^*)/3) | Supplied observable | A different readout selects a different Fourier mode | Exact projector-character identity in runner |
| Integer (S\to\infty), fixed (t=1/4) | Target domain | Shrinking-time or moving-time results do not answer the question | Goal contract |
| Strong profile \(\eta_S\to\eta_\infty\) | Proved upstream at fixed time; strengthened here to explicit (O(S^{-2})) bound | Without it, scalar reduction has only qualitative (o(1)) error | Weighted tridiagonal difference estimate and Duhamel proof |
| Jacobi spectral theorem, Fourier Parseval, Cauchy contour shift, Duhamel formula | Standard mathematics under their stated hypotheses | Omitted hypotheses could invalidate quantitative bounds | Full proof in exact-side note; finite dense checks corroborate identities |

The four framework axioms and registered primitives do not supply the quantum state space, this Hamiltonian, its spin realization, or this preparation. No import is retired, and no axiom or primitive change is proposed on present evidence.

## Current transfer-phase block — source and primitive check

The block is developed at base `origin/main` revision
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`, on the child source chain
through `c734332ca227c4371f3c188f96227c494b43f533` (#9091) and the
observable-phase checkpoint at `20251000c51`.

| Input | Role in this block | Status / check |
|---|---|---|
| Exact five-site Casimir coefficients in `POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md` | Supplies `r_a`, the offsets, and exact Jacobi entries being transferred | Conditional on the supplied path and signed labels; the new proof carries those hypotheses unchanged |
| `N_S` Jacobi recurrence and its spectral parameter `lambda` | Defines the transfer vector and exact transfer matrix | Exact algebraic rewrite where each off-diagonal is nonzero; determinant is checked directly |
| `u=h/S` in a compact subset of `(-1,1)` | Keeps `w=1-u^2` and all square-root links uniformly positive | Explicit analytic domain of the uniform Taylor remainder |
| `k` in a compact set with `|sin(5k)|>=kappa>0` | Keeps the local cell eigenphase simple | Explicitly excludes repeated-root/Bragg arcs; no conclusion is made on those layers |
| Approved primitives in `axiom_premise_nodes.json` | Baseline check for physical-premise classification | `minimal_axioms` is relevant and its source was read. Scale reference, kinetic isotropy, and realized-state primitive supply none of this Hamiltonian, transfer coefficient, phase, or readout; they are not used as premises. |

The exact second-order coefficient is a derivation from the supplied Jacobi
family, not a new axiom, primitive, fitted selector, or observed-value input.
The local phase remainder does not bound the accumulated phase over a number
of cells growing with `S`.

## Bragg and turning transport imports and counterfactuals

The five-note transfer block remains conditional on the same exact integer-spin
Jacobi family. It adds no premise about the physical state space or the four
framework axioms.

| Assumption | Exact role | If varied or false |
|---|---|---|
| Fixed energy and compact `u=h/S` interval | Keeps all link square roots and the one-site principal frame analytic | Near `|u|=1` or spectral energy endpoints, the compact transfer expansion and its constants fail; endpoint or turning analysis is required |
| Simple Bragg root with `k'(u_B) != 0` | Gives gap `|sin(5k)| ~ |u-u_B|` for the `S^-2/3` layer | Multiple or coalescing roots need a different layer; the theorem explicitly excludes them |
| Central energy `lambda_m=2(1-cos(m*pi/5))`, `m=1,...,4` | Gives a double Bragg contact at `u=0` | Detuned energies move or split the contact; no energy-uniform central estimate follows |
| Exact five-residue coefficient arrays and fixed-cell similarity `D(u)` | Produce the exact `A1(0)=0` cancellation and principal-frame phase | Changed residues can remove the cancellation and restore an order-one connection mechanism; the central rate cannot be transferred without rederivation |
| Phase gauge `R0=(r0+, conjugate(r0+))` and fixed physical `lambda` under `u` differentiation | Fixes the sign of the geometric phase correction | A different gauge changes endpoint phases; varying `lambda` during differentiation changes `k'` and invalidates the displayed identity |
| Exact path boundaries and period-three preparation/readout are supplied | Connects these scalar transfer notes to the intended physical question only conditionally | A changed boundary, preparation, or readout changes overlap weights and alias selection even if the scalar Jacobi transfer remains the same |

Counterfactual route check: if the central coefficient identity `A1(0)=0`
failed, the scaling `A1=O(u)` and the `O(S^-1/2)` central estimate would
fail. If the local energy approached 0 or 4, the principal frame would
lose its uniform flux normalization and the ordinary turning-point route
would take priority. These cases are not hidden imports: they are the next
explicitly open proof obligations.
