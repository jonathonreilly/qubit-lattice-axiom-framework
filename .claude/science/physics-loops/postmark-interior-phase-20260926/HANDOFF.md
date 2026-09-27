# Post-mark interior-phase campaign handoff

**Checkpoint:** 2026-09-26
**Base reviewed:** origin/main at e37967e326c2bdb429bd3106d34158bd5420e9c0
**Working branch:** physics-loop/postmark-interior-phase-20260926
**Status:** campaign remains open; this checkpoint adds a conditional exact rate-transform lemma and route-pruning evidence. No fixed-time readout limit, discrepancy, axiom update, independent audit, or formal retained status is claimed.

## Exact target and current wall

For the supplied finite-spin one-vacancy model and its specified preparation and period-three output, the electric readout at \(t=1/4\) is reduced in the main-source chain to

\[
\langle O\rangle_{S,1/4}=\frac13+\frac23\operatorname{Re}q_S(1/4)+o(1).
\]

The remaining target is to prove a limit for this actual scalar, prove another limit, or certify separated subsequences of the actual readout. The exact-side note reduces its profile contribution to a fixed weighted quadratic form of the long-time kernel on 49 sites; the profile truncation radius \(R=24\) has a stated error below \(6\times10^{-12}\), and the prepared-state electric-end contribution is controlled in the stated double limit. The interior phase interference remains open. Here \(T=C/4\), \(C=S(S+1)\), so the required evolution time is order \(S^2\).

Allowed premises are the supplied integer-spin path, its exact two-hop factorization and signed Casimir labels, the supplied initial state and output map, and the explicitly cited main theorems. Forbidden weakenings include replacing the actual scalar by entrywise kernel decay as a necessary condition, treating finite-spin scans as an asymptotic certificate, or treating the supplied model as derived from the framework axioms. A completion witness must control the weighted scalar itself or provide a rigorous subsequence witness for the actual observable.

## What this checkpoint proves

The new note docs/POSTMARK_ELECTRIC_REVERSIBLE_RATE_TRANSFORM_BOUNDED_THEOREM_NOTE_2026-09-26.md proves an exact finite-dimensional identity conditional on the supplied path and row factorization. Conjugation by the positive zero mode turns the staggered Jacobi operator into a reversible nearest-neighbor Laplacian whose directed rates are the individual Casimir factors, with the reversible conductance given by detailed balance. Missing endpoint rates are defined to be zero because those edges are absent.

The runner reconstructs the matrix independently from the physical legal-hop enumeration and compares it with the signed-label recurrence for spins \(1,2,3,5,8,12,20,32\). The largest operator-identity residual is \(1.99\times10^{-15}\); the largest zero-mode residual is \(5.55\times10^{-17}\); the largest detailed-balance residual is \(1.39\times10^{-17}\). A deliberate change \(f(0)\mapsto f(0)+1\) is rejected, with the identity error rising to \(0.329\) and the zero-mode residual to \(9.95\times10^{-3}\). Full records are in:

- .claude/science/postmark_interior_phase_20260926/REVERSIBLE_RATE_TRANSFORM_RESULTS.json
- .claude/science/postmark_interior_phase_20260926/PERTURBATION_REJECTION.json

The fixed-index Gegenbauer limit does not extend as an exact full-spectrum formula. Direct double-precision diagonalization of the independently reconstructed matrices at the eight sentinel spins rejects the candidate \(\lambda_j=j(j+5)/(25S(S+1))\) at growing index; at \(S=32\), its largest-mode error is \(0.146\), while the first nonzero-mode error is \(2.01\times10^{-7}\). This is only a finite diagnostic. It preserves, and does not weaken, the proved fixed-index convergence. The data are in .claude/science/postmark_interior_phase_20260926/FINITE_SPECTRUM_CANDIDATE_CHECK.json.

The formal degree-one five-residue polynomial ansatz \(F_s(h)=h+c_s\) also fails narrowly: the \(h^2\) equations force offsets \((0,1/5,2/5,3/5,4/5)\) up to a common constant, while the \(h^1\) equations force incompatible values \(E=2/5\) and \(E=0\). This does not rule out matrix-valued polynomials, other exact spectra, or WKB.

## Assumptions and axiom boundary

| Layer | Supplied or derived content | Boundary |
|---|---|---|
| Framework | Current four axioms and registered primitives, read at the base above | They do not provide this finite-spin generator, the preparation, or the period-three output rule. |
| Conditional finite model | Integer-spin one-vacancy path, two-hop row factors, signed Casimir labels, first-mark state, and output map | These are inputs to this campaign's conditional theorems, not consequences of the current axioms. |
| New exact lemma | Positive-zero-mode conjugacy, reversible rates and conductances | Derived from the supplied factorization and labels; it is an operator identity, not a physical stochastic law. |
| Desired observable | The actual \(t=1/4\) readout or rigorous separated subsequences | Still open because the moving-index phase/overlap contribution is uncontrolled. |

No axiom is changed or proposed here. A broad admissibility-law/axiom-sufficiency chain already exists on current main, including docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md and docs/ADMISSIBILITY_RULE_INTERACTION_THROUGH_THE_ODDS_OF_UNFORMED_SITES_FIELD_EQUATION_MASSLESS_SURFACE_CONTENT_CHARGE_NO_FIRST_ORDER_MASS_CHANNEL_AT_NEUTRAL_SCALE_BOUNDED_THEOREM_NOTE_2026-09-20.md. Repeating a generic pair of local probability laws would duplicate that line and would not settle this fixed supplied-model scalar. Reopen the axiom route only with a construction that satisfies the complete same-premise framework models and changes the relevant electric prediction, or with a derivation of this supplied generator from those premises.

## First-principles exercise and literature map

The simplification begins from the exact path factorization rather than a continuum guess. The positive zero mode removes square roots from the nearest-neighbor recurrence and exposes a reversible conductance form, an exact edge-flux balance, and a constant same-eigenvalue Wronskian. The five-site periodicity remains, so this does not make the coefficients constant and does not reduce \(T\sim S^2\) propagation to the fixed-index Gegenbauer sector.

The consulted adjacent literature suggests methods, not a theorem for this operator and time scale. Kuijlaars–Van Assche derive weak zero-distribution results for varying recurrence coefficients, which do not supply phase-accurate weighted propagation. Sukhatme–Sergeenko treat periodic WKB near band edges, and Baldino develops all-order finite-difference WKB connection tools; these are method templates for the five-cell crossings, not direct coverage of the coupled central and moving-index sum here. Ismail–Letessier–Valent study quadratic birth-death families; the present five-residue rate pattern has not been identified with one of their solvable families. See [Kuijlaars–Van Assche](https://doi.org/10.1006/jath.1999.3316), [Sukhatme–Sergeenko](https://arxiv.org/abs/quant-ph/9911026), [Baldino](https://arxiv.org/abs/2410.14628), and [Ismail–Letessier–Valent](https://doi.org/10.1137/0520050). The claim of non-applicability is a scope comparison, not a literature no-go.

The useful reframing is to prove only the 49-site weighted scalar, not every kernel entry. A reversible-rate transfer equation and its discrete flux/Wronskian may support that reduction; any local band calculation still needs transport terms from the varying ground-state gauge. A naive frozen rate-symbol correction is not interchangeable with the Hermitian five-cell correction already in the main note.

## Next campaign ranking

See APPROACH_REGISTRY.md for the exact-family table. The next best mathematical route is a gauge-corrected block transfer built directly from the reversible rates, with one discrete Wronskian and uniform matching through the central and same-fiber Bragg layers. Its decisive check is a phase/overlap estimate accurate after multiplication by \(C\), followed by a bound for the actual fixed weighted scalar. If this stalls at a target-equivalent global quantization lemma, switch to the 49-site Feshbach/Schur or weighted-lag formulation, which may expose cancellation without proving entrywise decay. Keep endpoint control from the exact-side theorem and do not reopen the generic model-pair route unless its construction is specific to this observable.

## Source identities and recovery

- Current main at review: e37967e326c2bdb429bd3106d34158bd5420e9c0; fetch confirmed origin/main equaled this revision before edits.
- New exact-rate runner inputs: scripts/core_derivation.py SHA-256 e282bbe1a92afdd8306892a95b537caa5222ea189a4f74a2ab8cac86f743b9c5; scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py SHA-256 f5a4330c7cf4bccb393bddb0e1170380c4a33261fb729092fc949ef543dc88ec; zero-mode note SHA-256 b697aecbc9c8551df69eea76ea2e2aeb404dc0478fdc32e4dd1554b26a08fec8.
- The previous campaign packet remains recoverable at branch physics-loop/postmark-electric-validity-20260923, head ce2ffa3be7838c3321f78642ee9185eee9812d7c; its checkpoint before this refresh is a82d245904a22c2942718d4115ffedea390c2b19.
- The separate Airy/phase-correlation route remains recoverable at branch physics-loop/postmark-electric-phase-correlation-20260924, head 935932e262f21993a7b0122e1f9aeb4474255403.
- No post-mark PR was open at this checkpoint before packaging. No audit verdict or formal retained grade is claimed.

This exact-rate result is a support checkpoint and does not close the campaign's target scalar. No post-mark PR was opened or flipped out of draft in this pass. Push the checkpoint branch to preserve the work, then remove this scratch worktree using the user's Physics repository procedure. Preserve the pushed branch as a recovery path. Never touch archive or archive_unlanded, and do not run git gc.
