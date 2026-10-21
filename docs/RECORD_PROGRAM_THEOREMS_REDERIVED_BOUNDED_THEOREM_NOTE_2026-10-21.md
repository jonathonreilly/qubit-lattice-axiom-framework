---
claim_id: record_program_theorems_rederived_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Symbolic and finite rederivations of the theorems the record program relies on: the field operator compatible with a conserved symmetric source, universality of coupling, the static weak-field solution and ray deflection, the path-marker duality relation, the Dirac scalar-density identity, and the conditioning chain rule; no physical field equation, coupling value or empirical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_program_theorems_rederived_2026_10_21.py
---

# Theorems used by the record program, rederived

Claim type: bounded_theorem.
Primary runner: `scripts/record_program_theorems_rederived_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, uses several standard results. This note rederives each one under the hypotheses actually used, rather than citing it. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the ansatzes below.

## Field operator for a conserved symmetric source

**Ansatz.** The general local, Lorentz-covariant, second-order linear operator on a symmetric tensor h, in momentum space with eta = diag(-1,1,1,1), is

    O(h)_mn = a k^2 h_mn + b (k_m k^p h_pn + k_n k^p h_pm) + c k_m k_n h + d eta_mn k^p k^q h_pq + e eta_mn k^2 h.

**Divergence condition.** A field equation O(h) = kappa T with a conserved T (k^m T_mn = 0) imposes no extra condition on h exactly when k^m O(h)_mn vanishes for every h and k. Collecting coefficients gives b = -a, d = a and c = -e, so one parameter remains beyond the overall scale.

**Self-adjointness.** A lossless field needs a self-adjoint operator under the pairing h'_mn h^mn. Imposing that fixes e = -a, which is the linearised Einstein operator. It annihilates pure-gauge fields k_m xi_n + k_n xi_m.

**Mass term.** A mass term m^2(h_mn - eta_mn h) makes the divergence nonzero for generic h. A massive field therefore cannot meet the divergence condition.

**What the hypotheses cover.** The derivation assumes a symmetric rank-two field, which matches a symmetric source. It does not exclude an additional scalar field coupled to the trace.

## Universality

Suppose two species couple with strengths kappa1 and kappa2 and exchange momentum at rate J, so that k.T1 = J and k.T2 = -J. The source's divergence is then (kappa1 - kappa2) J. The divergence condition forces kappa1 = kappa2 whenever the species interact.

## Static source and deflection

For a static source T_00 = M, solving the Einstein operator together with the harmonic condition gives h_ij = h_00 delta_ij and h_0i = 0. The spatial and temporal potentials are equal, so gamma = 1.

Rays were integrated in the metric g_00 = -(1+2 Phi), g_ij = (1 - 2 gamma Phi) delta_ij with Phi = -M/r. They deflect by (2M/b)(1/v^2 + gamma) to within 0.1 percent over the finite path. Light therefore gets 4M/b for gamma = 1, against 2M/b for a lapse-only metric (gamma = 0).

## Other results used

**Path markers.** For path weights w1, w2 and pure markers chi1, chi2, the trace distance is D = sqrt(1 - 4 w1 w2 |<chi1|chi2>|^2) and the visibility is V = 2 sqrt(w1 w2) |<chi1|chi2>|, so D^2 + V^2 = 1. For mixed markers, V is bounded by the fidelity, and the runner finds D^2 + V^2 <= 1 on 400 random draws. The readable-trail model of the CL-3 evidence exceeds this bound.

**Dirac scalar density.** With H = alpha.p + beta m and E = sqrt(p^2 + m^2), the positive-energy projector P = (1 + H/E)/2 satisfies P beta P = (m/E) P. So psibar psi / psi^dag psi = m/E for every positive-energy spin state. This is the identity behind the coherent clock.

**Conditioning.** When the record R is a function of X, H(X) = H(X,R) = H(R) + H(X|R). A controlled flip onto a record qubit leaves the branches orthogonal, so the record qubit's reduced state is diag(1-p, p), with entropy H(R).

## Scope

The operator ansatz, metric form, ray setup and random seeds are supplied. No physical field equation, coupling value, exclusion of an extra scalar or empirical identification is established.
