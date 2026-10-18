# Neutral finite-range source review

Disposition: PASS for the scoped exploratory mathematical block after the synthetic-quadrature correction. No unresolved material formula, sign, index or metric finding. This is not a formal audit, complete campaign review, retained-grade decision or scalar-particle identification.

Read complete HANDOFF.md, finite_range_mode.py, finite_range_verify.py, resolvent_limit.py, filter_atom_control.py and all associated JSON rows; loaded every saved NPZ array and inspected shapes/finiteness. Also read the new NEUTRAL_FEATURE_DERIVATION.md. Source identities below bind this review. No repository edits by the reviewer.

## Finding resolved in this session

The original synthetic Gaussian tau=256 output reported exactly zero standard deviation for both the continuum and atom-plus-continuum fixtures. Adaptive quadrature of x^2 exp(-tau^2 x^2) missed the narrow peaks. The author changed variables to y=tau*x, added positive-width controls and analytic Gaussian-variance controls, then regenerated output. I read the correction and replayed it in a relocated temporary directory: all 24 controls pass and output is byte-identical. Independent analytic uniform-Gaussian moments give std=0.0027621358640099515 without the atom and 0.00028003647704518395 with atom weight .25, agreeing with corrected output. The original zero-width result must not be reused as evidence of a pole.

## Main mathematics and implementation

For O_q=sum c_(k+q)^dagger M(k)c_k, the CAR commutator gives h(k+q)M-Mh(k). Its coefficient convolution, exp(i q.s)B_s M_r-M_r B_s at r+s, has the correct shift and sign. The implemented adjoint has conjugated phase and left/right Hermitian matrices in the correct positions. Each fixed-shift destination index map is injective, so NumPy advanced-index accumulation does not silently discard repeated-index contributions. Output through R+1 is retained; no projected-boundary false eigenmode is introduced.

The solve is the positive regularized normal equation (A^dagger A+eta I)x=s. Normalizing its solution gives a source-accessible construction, not the minimum residual over all unit vectors or a dark-mode exclusion. Mean and variance correctly retain the norm of output outside the input support. Source and coefficients use the HS Parseval metric. The support radius measures relative endpoint separation, not a center-of-mass envelope or self-bound size.

The independent momentum implementation correctly integrates the squared Laurent polynomial when N>2(R+1). N8 at R3 can alias the output norm and is expressly exempted; N16/N24 checks are legitimate. I independently reconstructed all twelve saved operators on an additional N10 half-shifted grid using explicit phase sums: HS norm, residual, mean and standard deviation agree with stored coefficients to at most 7.2e-15.

Transition indexing and the positive thermal norm are correct: w_ba=f_a(k)[1-f_b(k+q)], Delta_ba=E_b(k+q)-E_a(k). Both signs of frequency are included. I independently used matrix covariance Tr[M^dagger(1-f(hq))M f(h)] and its cross-source version; the overlap agrees with the transition implementation to 3e-15 for R3 eta=.001. HS and thermal source overlap are intentionally different metrics and cannot be relabeled as physical canonical couplings.

The unrestricted resolvent filter applies eta/[(Delta-omega)^2+eta], whose overall eta cancels after normalization. Its reported overlap is |integral F dmu|^2/integral F^2 dmu. The smooth positive-density asymptotics overlap^2~2*pi*s0*sqrt(eta), residual^2~eta follow from the standard rescaled integrals. The general K-bound is weighted Cauchy-Schwarz, and the spectral-window bound follows by splitting inside/outside the window and using ||(1-P)v||<=r/epsilon. The no-atom implication is conditional on one fixed source spectral measure and the stated limit order; no atom absence for the physical model is established.

## Momentum, parity and physical boundaries

All finite-range examples here use fixed q=Q and omega=.2. They supply no dispersion law, propagation speed or q->0 mass inference by themselves. The even grid sizes make k+Q a permutation of the shifted momentum mesh, so the finite-box momentum assignment is consistent. A frequency-centered operator generally is not Hermitian even at Q=-Q modulo reciprocal lattice vectors; a Hermitian observable requires pairing its adjoint/frequency component. Number neutrality alone gives neither scalar symmetry nor a new field.

The numerical structure weights are grand-canonical. In an exact finite-box parity-projected encoding, their values need the separate parity correction and sector/box assumptions; an unrelated continuum quadrature mesh is not automatically that physical box. This review does not promote the grand-canonical computation to an exact even-parity finite-box result. The handoff acknowledges that distinction and separate parity checks. Finite positive-temperature metrics can be handled on their support/quotient; numerical occupation underflow is not a proof of exact null weight.

The supplied source is pseudoscalar, Hamiltonian and ensemble remain inputs, and the note preserves the distinctions between selected preparation, pole, thermal overlap, canonical normalization and cosmological coupling. Finite-grid narrowing with decreasing overlap does not prove a global no-go for other channels or higher composites. The synthetic atom fixture supplies the relevant counterexample to such an inference.

## SHA-256 identities

```text
4eeae52e30b493fd529846d3ecd0fb468b84a1e2305e0ddbcbe2f5b98a7e3522  .claude/science/physics-loops/neutral-composite-24h-20261018/HANDOFF.md
b4f0c2fe277a00cbb7a9f7c7454bf64d4279db425e1a41ec62e4bd7807451f36  .claude/science/physics-loops/neutral-composite-24h-20261018/NEUTRAL_FEATURE_DERIVATION.md
b4c2bc8c25dafa7c529a96f3109331924eb428d2b363ec765f66fd1efc1e0588  data/collective_corner_response/candidate.json
e8bdf57a0ff9e654b6808157bc1cd4528144067f77b37c2769380975d4f2eaab  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_mode.py
fb41791a92f5368e663ecb84654a4e990792a424a0aebec3af61bba7e5233294  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_mode.json
3397f9c4a32b3f56991ea10bb80c50bea94587625963bee7ae68932640cb58ad  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_modes.npz
81ecd6a21477ed35743c4d55bf4940363b6bdc33e4e8bcd7c293669bedc243c7  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_verify.py
afff19880c7e9098d98de64421b3d429c3ffeafa5dbe83ef668215a6e01ee4d5  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/finite_range_verify.json
7d32cac6753fe6aaa2fc0eb19ccccfb50645669160f0937c7df581312846d1d7  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/resolvent_limit.py
b901480cf3d2764ee4390eeaf23239bdaea81fe18c1a66439fe607e92b767d7e  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/resolvent_limit.json
a9e94e387049b78d3429f5224954d99403cf116cbd724c5a2bda35606a400982  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/filter_atom_control.py
a54fa285ea37515df9da4f7d72a89b9af2e76d6de6844a651f3abb2475013008  .claude/science/physics-loops/neutral-composite-24h-20261018/probes/filter_atom_control.json
```
