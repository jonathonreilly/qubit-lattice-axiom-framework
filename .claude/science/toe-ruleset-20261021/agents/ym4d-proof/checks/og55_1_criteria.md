# og55_1 — pre-registered criteria (written before the script og55_1_route.py exists)

Owner: OFFGLOB55.md (Opus 5.5 worker, claude-opus-5-5). Exact rational arithmetic only (Python fractions; no floats, no numpy).

## What is tested
OFFGLOB55 §3.2 Lemma HR_U (covariant hierarchical routing) and §3.4 Proposition LOC-cc_U (exact local cc-decomposition) at a
**generic curved composite configuration** U, in small composite models with su(2) ≅ R³ and Ad-matrices in SO(3) ∩ Q^{3×3}
(Cayley transforms of rational skew matrices; det = 1 and R^T R = I verified exactly).

Conventions (as in OFFGLOB55 §3.1): level-l sites = level-0 sites with every coordinate ≡ (L^l − 1)/2 mod L^l; level-l links
b = (y → y + L^l e_μ); (Ξ_Uλ)_l(b) = Ad_{U_l(b)}λ(y′) − λ(y); D_U(S)(z) = Σ_l[Σ_{b: y′=z}Ad_{U_l(b)}^T S_l(b) − Σ_{b: y=z}S_l(b)];
roots of the level-(j+1) blocks are block centres; γ(Z) = the level-j axial path from R(Z) to Z, coordinate 1 first, then 2, …;
backward steps carry the link current −Ad_{U(b)}J (§3.2 convention derived for reversed links).

Models: M1 d=2, L=3, k=2, T=1; M2 d=2, L=3, k=2, T=2; M3 d=2, L=3, k=3, T=1; M4 d=3, L=3, k=2, T=1. Random seeds fixed in the script.

## PASS criteria (all must hold exactly, in every model)
- A0 (adjointness): ⟨S, Ξ_Uλ⟩ = ⟨D_U(S), λ⟩ for 3 random S, λ.
- A1 (HR_U (i)): D_U(P_U^T u) = u − Σ_X V^U_k(X) δ_{r_X} for 3 random charge distributions u; in particular D_U^⊥(P_U^T u) = u^⊥.
- A2 (HR_U (ii), covariance): P_{U^g}^T(Ad_g u) = M_g P_U^T u for a random rational gauge g (all level-0 sites), 2 random u.
- A3 (LOC-cc_U (a)): for S := P_cc^U(S_raw) (S_raw random on all levels), D_U^⊥S = 0, and Σ_□ P_cc^U(M_{χ_□}S) = S for a rational
  partition of unity {χ_□} (≥ 2 pieces, non-constant) acting link-wise.
- A4 (LOC-cc_U (b)): D_U^⊥(P_cc^U(M_{χ_□}S)) = 0 for every piece.
- A5 (flat limit): at U = 1 the general code reproduces KFACTOR_OFF55 HR's flat P^T u = Σ_Z V_j(Z)γ(Z) exactly.

## Controls (each must FIRE, i.e. the displayed identity must FAIL, in every model where it is run)
- C1: flat routing at curved U (transports set to 1, divergence still D_U): some piece (1 − P_1^T D_U^⊥)(M_{χ_□}S) is not cc_U.
- C2: D_U^⊥(P_1^T u) ≠ u^⊥ at curved U.
- C3: a source S_bad with D_U^⊥S_bad ≠ 0: Σ_□ P_cc^U(M_{χ_□}S_bad) ≠ S_bad.
- C4: backward steps with the wrong sign (+Ad_{U(b)}J): A1 fails.
- C5: transport on the wrong side (Ad_{T^{-1}} in place of Ad_T when accumulating V^U_{j+1}): A1 fails.

## Verdict rule
OVERALL PASS iff every A-item holds in every model and every control fires in every model where it is run. Any A failure → FAIL
(the lemma or its stated convention is wrong). Any non-firing control → FAIL (the check could not have decided).

## What this check cannot decide (stated before running)
No norm bound (HR_U (v), CCL_U's sizes) is tested — only identities. The G-slot and residual-slot charges of Lemma CCL_U are not
modelled (only plain currents). No Hessian, criticality, d = 4, or k-/T-uniformity is tested. The models are tiny; an identity
that holds for generic random rational data in them is an algebraic identity of the construction, not a proof for all sizes.
