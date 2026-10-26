---
claim_id: record_program_theorems_rederived_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Conditional symbolic identities and separate finite illustrations in supplied models: the field operator compatible with a conserved symmetric source, universality of coupling, the static weak-field solution and ray deflection, the path-marker duality relation, the Dirac scalar-density identity, and the conditioning chain rule; no physical field equation, coupling value or empirical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_program_theorems_rederived_2026_10_21.py
---

# Conditional identities and finite illustrations for the record program

Claim type: bounded_theorem.
Primary runner: `scripts/record_program_theorems_rederived_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, uses several standard results. This note gives conditional algebraic derivations under explicit supplied hypotheses; ray integration and mixed-marker sampling are separate finite illustrations. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the ansatzes below.

## Field operator for a conserved symmetric source

**Ansatz.** The supplied five-term local, Lorentz-covariant, homogeneous two-derivative constant-coefficient linear operator on a symmetric tensor h, in momentum space with eta = diag(-1,1,1,1), is

    O(h)_mn = a k^2 h_mn + b (k_m k^p h_pn + k_n k^p h_pm) + c k_m k_n h + d eta_mn k^p k^q h_pq + e eta_mn k^2 h.

**Divergence condition.** A field equation O(h) = kappa T with a conserved T (k^m T_mn = 0) imposes no extra condition on h exactly when k^m O(h)_mn vanishes for every h and k. Collecting coefficients gives b = -a, d = a and c = -e, so one parameter remains beyond the overall scale.

**Self-adjointness.** Self-adjointness under the pairing h'_mn h^mn is a supplied condition, not a consequence here of losslessness. Pairing interchanges the c and d terms, so c = d = a and e = -a. For a != 0, normalizing a = 1 gives the linearised Einstein operator; a = 0 gives the zero operator. It annihilates pure-gauge fields k_m xi_n + k_n xi_m.

**Mass term.** A mass term m^2(h_mn - eta_mn h) makes the divergence nonzero for generic h. This specified term fails the off-shell divergence identity; this is not an exclusion of massive tensor theories with additional constraints.

**What the hypotheses cover.** The derivation assumes a symmetric rank-two field, which matches a symmetric source. It does not exclude an additional scalar field coupled to the trace.

## Universality

Suppose two species couple with strengths kappa1 and kappa2 and exchange momentum at rate J, so that k.T1 = J and k.T2 = -J. The source's divergence is then (kappa1 - kappa2) J. The divergence condition forces kappa1 = kappa2 when J != 0 in this exact two-source exchange decomposition. Additional stress contributions and noninteracting sectors are outside this implication.

## Static source and deflection

For the supplied normalization O = -T and static Fourier source T_00 = M, at nonzero spatial momentum the harmonic-gauge particular solution has h_00 = h_ii = -M/(2|k|^2) and h_0i = 0. No homogeneous or boundary modes are selected by this rational solution. At k = 0 it cannot solve a nonzero source. Gamma = 1 follows only after the supplied metric identification; neither physical coupling nor asymptotic boundary conditions follow from the normalization.

Rays were integrated in the metric g_00 = -(1+2 Phi), g_ij = (1 - 2 gamma Phi) delta_ij with Phi = -M/r. The leading weak-field impulse along the unperturbed line integrates b/(x^2+b^2)^(3/2) to 2/b, giving (2M/b)(1/v^2 + gamma). The runner separately illustrates this coefficient within 0.1 percent in six finite cases: M = 1e-4, b = 1, initial x = -4000, integration duration 8000/v, v in {1, 0.5, 0.2}, gamma in {1, 0}. The finite results are not exact all-M/b geodesic identities. At leading order light has coefficient 4M/b for gamma = 1 and 2M/b for gamma = 0.

## Other results used

**Path markers.** For normalized marker states rho1, rho2 and nonnegative path weights w1 + w2 = 1, define weighted distinguishability D = ||w1 rho1 - w2 rho2||_1. This is not the ordinary state trace distance: identical states at w1 = 0.2 give D = 0.6 but ordinary trace distance zero. For normalized pure markers chi1, chi2, D = sqrt(1 - 4 w1 w2 |<chi1|chi2>|^2) and the visibility is V = 2 sqrt(w1 w2) |<chi1|chi2>|, so D^2 + V^2 = 1. For mixed markers, the supplied coherent-preparation visibility envelope is Vmax = 2 sqrt(w1 w2) ||sqrt(rho1) sqrt(rho2)||_1; the marginals alone do not determine an actual visibility. The runner finds D^2 + Vmax^2 <= 1 on 400 seeded random draws, not an exhaustive proof from sampling. No comparison with an unbound readable-trail model is asserted.

**Dirac scalar density.** With H = alpha.p + beta m and E = sqrt(p^2 + m^2), the positive-energy projector P = (1 + H/E)/2 satisfies P beta P = (m/E) P. This is a compression identity, not invariance of the positive-energy subspace under beta. At fixed momentum, E > 0 and nonzero positive-energy spinor psi, it gives psibar psi / psi^dag psi = m/E. A p = 2, m = 1 countercontrol has nonzero (I-P) beta P despite exact compression. Any physical clock identification remains separate.

**Conditioning.** When the record R is a function of X, H(X) = H(X,R) = H(R) + H(X|R). A controlled flip onto a record qubit leaves the branches orthogonal, so the record qubit's reduced state is diag(1-p, p), with entropy H(R).

## Scope

The homogeneous two-derivative operator ansatz, self-adjointness, nonzero-scale normalization, two-source exchange, static particular-solution selection, metric identification, marker preparation, Clifford algebra, ray setup and random seeds are supplied. No physical field equation, coupling value, exclusion of an extra scalar or empirical identification is established.
