# CG16-S referee closure RC-W: one check

Checker: Codex gpt-6-astra, reasoning effort low, read-only, laptop, 2026-11-07 (run log ~/toe-lap/prior/check_rcw.log). One check of one proof: CG16S_REFEREE.md closure RC-W, including its variation identity (step 3) and Bloch-form constant (step 6), as the referee asked. The lead (Claude Opus 5.5) copied the checker's final message below unchanged.

| Step | Status | Check |
|---|---|---|
| 1. Trace facts | CORRECT | The compressed derivation is a finite-matrix commutator. The boundary commutator has rank \(O(L^2)\). Both trace statements follow. |
| 2. Local path | CORRECT | Block logarithms have uniform norm at most \(\pi\). Their exponentials retain block support. Products and derivatives have uniformly bounded propagation and norms. For the displayed commutator bound, choose \(c\) at the midpoint of the block’s coordinate range. |
| 3. Variation identity | CORRECT | Both differentiation identities have the stated signs. Maurer–Cartan gives the two antisymmetrized terms \(-\Omega\) and \(+\Omega\). After extracting the two displayed commutators, the three remaining terms each equal \(\epsilon_{abc}\theta_a\theta_b\delta_c\eta\). Their sum is \(3\epsilon_{abc}\delta_c(\theta_a\theta_b\eta)\). The identity is exact before taking traces. |
| 4. Box traces | CORRECT | The derivation term has exactly zero box trace. Each commutator contributes \(O(L^2)\), uniformly in \(t\). Division by \(L^3\) and integration give the stated \(C/L\) bound. No intermediate trace-per-volume limit is needed. |
| 5. Periodic endpoint | CORRECT | Translation covariance makes every diagonal cell block of \(\Omega(V)\) identical. Thus \(f_L(1)=\tau(\Omega(V))\) exactly. The bound forces this value to vanish. |
| 6. Bloch constant | CORRECT | With Fourier kernel \(e^{-iK\cdot\beta}\), \(\delta_a=i\partial_{K_a}\). Hence \(\tau(\Omega)=-\frac{3i}{\pi}W_3[V]\). The opposite convention gives \(+\frac{3i}{\pi}\), with consistent orientation. The antisymmetric sum already supplies the wedge-product coefficient; no extra \(3!\) is missing. |

The application to the free reading is valid under E. Even gates preserve each one-site content-parity sector. Apply RC-W to \(V_\sigma\), then use \(W_3[V_\sigma]=16W_3[W_\sigma]\). The stated pairing follows from Theorem 7 for finite node sets consisting entirely of the specified Weyl points. This check does not independently re-prove Theorem 7.

Read only. No edits, git commands, or numerical checks.

VERDICT: RC-W holds