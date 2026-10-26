# J:derive:review-20260929-wall-gravity-source-and-equivalence:a1

Worker: Claude Sonnet 5.5. Same model family as the source packet's attackers and kill-checkers; unrefereed. `python3 check.py` ends `TOTAL: PASS=51 FAIL=0` (about 13 s, 83 MB).

**Read first.** I read the complete `docs/MINIMAL_AXIOMS_2026-06-29.md` and the complete `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (current main `a77a3449c9`), and the node list of `docs/audit/data/axiom_premise_nodes.json`. Nothing in the four axioms or the three primitives (`scale_reference`, `kinetic_isotropy`, `realized_state`) supplies a dynamics, a time metric, a source/action, or a gravitational coupling (`docs/MINIMAL_AXIOMS_2026-06-29.md:114-130`, `:185-190`). Everything below is therefore a statement about a **supplied** action. Nothing is adopted.

**Source packet.** Branch `claude/toe-walls-20260929` at `4bd42747e5…`: all 22 listed objects fetched and their sha256 equal the SOURCE_MAP values (see `RECOVERY_STATUS.json`). I read SUMMARY, the T60-T63 and T67-T72 attack/kill pairs in full, and searched for "helicity", "radiation power", "pulsar", "residue": none occurs in these 22 objects. The task's helicity and radiation wording comes from the exploratory packet's framing, not from these sources; its binary-pulsar exclusion is not used.

## What obligation I chose, and why it is distinct

The packet's T68/T72 attack-kill pairs fix: light bending = 1 + (matter speed / gravity speed)^2 for G-invariant tensors (kills/T68.md "Corrected plain-language verdict"); the repository's own member bends by the Einstein amount at any wave speed; fall is W = 1 per body class and the composite part stands (kills/T72.md); `G = 1/(16 pi K)` is already landed (kills/T70.md error 1). What none of them computes is **the radiation side**: a static helicity weight fixes only a stiffness, and the task asks which further ingredients (residue, inertia, speed, conserved source law) a radiated power needs. Related tasks `bound-bodies-and-the-two-far-fields` and `moving-records-and-the-balance-of-the-two-charges` treat the far fields of bodies and P = Q (probes `bound-bodies-and-the-two-far-fields` a1/a2); the scalar-only quadrupole power of a delayed rate field is `a-delay-for-the-rate-field` a4 (`work/derive/a-delay-for-the-rate-field/w-jonathonsmac4f50-j519d/ATTEMPT.md:25-26`, "1/6 of the comparator's"); the TT emission **sign** is `the-travelling-disturbances-source-by-species` a1. A quadrupole **power** for the tensor member and its separation from the static weights is not in those, and not in main (`git grep -i "quadrupole formula|radiated power" docs/ADMISSIBILITY_RULE_*` returns nothing; open-PR title search for quadrupole/graviton speed finds no match). The canonical-gravity-changed-carriers task (a separate J unit) is not touched.

## The one source action (ASSUMED, supplied)

Continuum symbol (p_j -> p), per unit volume, symmetric h_ij, rate log u, energy density e, stress Theta_ij:

L = [alpha tr(h'^2) + beta (tr h')^2]/wbar + K wbar (u R1 + R2) - e u + (1/2) Theta_ij h_ij,
R1 = p^2 tr h - p.h.p, R2 = -(p^2/4) tr h^2 + |hp|^2/2 - (p.h.p)(tr h)/2 + p^2 (tr h)^2/4, K, alpha, wbar > 0.

The first four terms are block 101 as landed (`docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_…_2026-09-23.md:25-26`); the stress coupling is block 62's, added in `docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_…_2026-09-24.md:61`. Premises I add and label: (S1) h_ij is a length-squared strain, lengths^2 = 1 + h (READING, used only in Step 12); (S2) the source is compact and the radiation is at leading order in size/wavelength; (S3) no lattice-symbol corrections (p_j = 2 sin(k_j/2) replaced by p_j); (S4) beta = -alpha for Steps 6-11 (the closing ratio of the landed constraint-algebra note).

## Steps

1. **PROVED + CHECKED (A1).** R1 and R2 are unchanged under h -> h + p xi^T + xi p^T for generic p, h, xi (exact, 9-variable sympy). This is landed (block 101 T1); reproduced.

2. **CHECKED (A2, A2b).** With p along z and h = [[phi+a, b, cx],[b, phi-a, cy],[cx, cy, 2 xi]]: R1 = 2 p^2 phi and R2 = p^2 (phi^2 - a^2 - b^2)/2. The full Hessian of L in (fields, velocities) is block-diagonal in helicity {phi, xi, u | cx, cy | a, b} for every beta, a and b are uncoupled, and **only a and b carry a gradient term**. So the only propagating sector is the two TT polarisations; the helicity-1 pair (cx, cy) obeys cx'' = (wbar/4alpha) Theta_xz with no spatial propagation, and the helicity-0 sector (phi, xi, u) has phi fixed by the u-constraint and xi, u carrying a free function (the gauge freedom of the landed constraint-algebra note T2).

3. **CHECKED (A3). Static helicity projector weights.** On unit-normalised tensors (tr T^2 = 1) R2 = -(1/2) F_EH exactly, with weights TT -1/4, helicity-0 trace-free +1/12, helicity-1 0, against F_EH weights 1/2, -1/6, 0 of `docs/TENSOR_HELICITY_RATIONAL_CERTIFICATES_…_2026-09-29.md:72-76`. Reproduction of the landed weights in the member's normalisation, not new.

4. **PROVED + CHECKED (B1, B2). Static response.** Static equations of cx, cy, xi force Theta.p = 0 (block 62 T5). Then phi = e/(2 K wbar p^2), a = (Theta_xx - Theta_yy)/(2 K wbar p^2), b = Theta_xy/(K wbar p^2), and **u = -(e + Theta_xx + Theta_yy)/(4 K wbar p^2)**: the static lapse is sourced by e + Theta_ii, not by e alone. Eliminating everything,
   L_eff = (e^2 + 2 e Theta_ii)/(8 K wbar p^2) + Theta_TT:Theta_TT/(4 K wbar p^2).
   Weights: scalar (e e) 1/(8 K wbar), TT 1/(4 K wbar): ratio 1 : 2, both independent of alpha. Two static energies attract with V = -G_E E1 E2 / r, **G_E = 1/(16 pi K wbar)** (Fourier pair checked). `G = 1/(16 pi K)` at wbar = 1 is landed (`docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_…_2026-09-25.md:102`); the explicit 1/wbar is the premise kills/T70.md (R3 row) says is missing from the packet. I did not locate the e + Theta_ii form of the lapse source or the scalar:TT weights 1:2 in the notes I read (not an exhaustive search).

5. **PROVED + CHECKED (B4). Virial.** For a stationary compact stress (d_j Theta_ij = 0) int Theta_ii = 0 and int x_k Theta_ii = 0 (integration by parts; checked exactly on a Gaussian-polynomial family). So the far lapse of a stationary body, and its pull in an external gradient to first order in the gradient, are set by int e with every binding contribution counted in e; the stress does not enter. (Kept within this action; the composite *fall rate* is Step 14.)

6. **PROVED + CHECKED (C1-C3). TT inertia, speed, residue.** L_TT = (alpha/wbar) tr h'^2 - (K wbar p^2/4) tr h^2 gives inertia I = 2 alpha/wbar, gradient stiffness K_g = K wbar/2, speed **c^2 = K wbar^2/(4 alpha)**, equation h'' + c^2 p^2 h = (wbar/4alpha) Theta^TT. Static value of the TT propagator 1/(K_g p^2) (alpha-free); pole residue at omega = c p is -1/(2 I c p) (alpha-dependent). Outgoing flux = c x energy density = (K wbar/2c)(h')^2 (exact). Landed frequency (block 101 T2) reproduced.

7. **PROVED + CHECKED (D1). The action's own source identity.** At beta = -alpha the xi-equation contains no xi: -8 alpha phi''/wbar = Theta_zz; with the u-constraint phi = e/(2 K wbar p^2) this is **e'' = -c^2 p^2 Theta_zz**, i.e. e'' = c^2 d_i d_j Theta_ij in space, with the same c as Step 6. This is the landed identity (constraint-algebra note T3, :37-39); reproduced. Reading: it is a conservation law demanded of the content, and it says the content's energy-flux/momentum-density ratio equals the TT speed squared.

8. **PROVED + CHECKED (D2).** At alpha + beta != 0 the same equation is xi'' = [wbar Theta_zz - 8 beta phi'']/(8(alpha+beta)): solvable for any (e, Theta). There is then no identity linking e and Theta, and the content's own ratio kappa = J/P is free of the TT speed.

9. **PROVED + CHECKED (D3).** For compact Theta, int x_i x_j d_k d_l Theta_kl = 2 int Theta_ij (exact on three random Gaussian-polynomial tensors; general by two integrations by parts). With Step 7: **Q''_ij = 2 c^2 A_ij**, Q_ij = int e x_i x_j, A_ij = int Theta_ij. If instead the content obeys continuity e' = -d_i J_i, momentum balance P_i' = -d_j Theta_ij and J = kappa P (a matter law, not the action's), the same step gives Q'' = 2 kappa A.

10. **CHECKED (E1-E4). Radiated power, two routes.** (a) Poynting: far field h = (wbar/4alpha)(1/(4 pi c^2 r)) A^TT(t - r/c), flux (K wbar/2c)(h')^2, sphere integral of the TT-projected square = (8pi/5)(A:A - (tr A)^2/3) (exact, sympy). (b) Mode sum with disjoint machinery: polarisation tensors built from theta-hat, phi-hat, each polarisation an oscillator with mass I = 2alpha/wbar driven by A_lambda/2, absorption line delta(omega_p - omega) pi F^2/(4I) (the Lorentzian-to-delta weight checked numerically with mpmath), integrated over momentum space. The two agree exactly iff c^2 = K wbar^2/(4 alpha); both give <P> = wbar omega^2 (A:A - (trA)^2/3)/(160 pi alpha c^3) for A = A0 cos omega t. They disagree if c is not the TT speed (negative control in the script).

11. **CHECKED (E5). Result at beta = -alpha.** Using Step 9, in the long-wavelength limit
    **P = <Q'''^TF : Q'''^TF> / (80 pi K wbar c^5) = (G_E / 5c^5) <Q'''^TF : Q'''^TF>**, c^2 = K wbar^2/(4 alpha),
    the quadrupole formula with G_E from the *static scalar* weight (Step 4). Equivalent: P = W_TT <Q'''^2>/(20 pi c^5) with the *static TT weight* W_TT = 1/(4 K wbar). So at beta = -alpha the ratio to the quadrupole formula is exactly 1 for every alpha/K. The role of each ingredient: stiffness K (static weights, alpha-free) fixes G_E; the inertia alpha enters only through the speed, as c^-5 (one power from flux and residue, four from the source identity Q'' = 2 c^2 A); the source law ties the speed in the flux to the speed in the source.

    **Scoped counterexample to "static weights fix the radiation" (F1).** Hold K, wbar, hence G_E, the static weights, u, phi, and the bending (Step 12) fixed; take alpha = 1/4 and alpha = 1. Then c = 1 and c = 1/2 and, for the same energy-quadrupole history, the powers differ by exactly 32 (P scales as alpha^(5/2)).

    **Without the identity (F2), at alpha + beta != 0** and matter law J = kappa P: P = G_E <Q'''^2> / (5 c kappa^2), i.e. P / P_quad(c_m = sqrt(kappa)) = c_m / c. Here the radiation depends on both speeds, c^-1 from flux and residue, kappa^-2 from the source law, which is where a speed comparison could bite. Its status: at beta != -alpha the landed constraint-algebra closure fails (note T1), so this is a mode-level sensitivity formula, not an endorsed model. No binary-pulsar or other speed exclusion is derived or used.

12. **CHECKED (G1-G3). Bending in the same coordinates.** At Theta = 0, u = -phi/2, so h_ij = 2 lambda delta_ij with lambda = -u; with lengths^2 = 1 + h (S1, READING) and the ray's coordinate speed c_m e^u / sqrt(1 + h), the index is n = 1 - 2u and the deflection is **4 G_E E / b = E/(4 pi K wbar b)** (exact integral); the clock alone gives half. It contains no alpha and no c, while c^2 = K wbar^2/(4 alpha) does. So in this action bending (gamma = 1) and the TT speed are separate numbers, confirming kills/T68.md's statement for the campaign member, here in an explicit action; they merge only in a G-invariant tensor with a shift (not this action).

13. **CHECKED (B5). Sign.** V_ee = -e1 e2/(4 K wbar p^2) is attractive iff K wbar > 0; TT frequency^2 > 0 iff K/alpha > 0. One sign datum (K, alpha > 0) covers TT stability and attraction in this action; so "the sign is the healthy-graviton datum" (kills/T71.md) is reproduced here, not circumvented.

14. **Reduction and first unresolved step (not a proof of fall).** For a bound state with total momentum P and energy E0, velocity V = dE/dP; with the energy centroid D, "law holds for the composite" J_tot = kappa P_tot is the statement P = E0 V / kappa, i.e. inertia = E0/kappa (READING; tautological from definitions). The fall weight W = E0 d^2E/dP^2 of kills/T72.md equals J_tot/(kappa P_tot). So composite fall is exactly the question whether the content (bonds included) obeys the member's local source law of Step 7. **UNRESOLVED:** a compact native content whose (e, P, Theta) obeys e'' = c^2 d_i d_j Theta_ij. The landed note shows the walker's frame response fails it (`…CONSTRAINT_ALGEBRA…:42`, T4); the two-step content meets it only at alpha = K/4 (landed, own, unrefereed: `docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_…_2026-09-25.md:30`). So Steps 7-11 are conditional on a source nobody has exhibited, and T72's composite deficit is not re-derived or repaired here.

## What is new, what is not

Not new: the action; the TT speed (block 101 T2); the source identity (constraint-algebra note T3); G = 1/(16 pi K) at wbar = 1; the weights 1/2, -1/6; gamma = 1 of the member; the TT emission sign; the scalar-only quadrupole power of a different model (a-delay a4, 1/6 of the comparator); packet verdicts on T68-T72.

Possibly new, within the supplied action and the stated scope (same family, unrefereed): (i) the static lapse source e + Theta_ii and the static weight ratio scalar : TT = 1 : 2 with their alpha-independence (Step 4); (ii) the quadrupole power of the beta = -alpha member, equal to the quadrupole formula with G_E and c at the TT speed, by two disjoint routes (Steps 10-11); (iii) its dependence on inertia, alpha^(5/2) at fixed K, wbar and energy history, and the explicit counterexample to inferring radiation from static weights (Step 11); (iv) the form c_m / c at alpha + beta != 0 (Step 11).

## Limits and what is not claimed

- No negative claim is promoted; no N1-N8 gate is invoked. "Not found" statements are about search of the listed paths only.
- Not claimed: a native source, a physical identification of K, alpha, or wbar; nonlinear or strong-field results; the dynamical Newtonian potential (u contains a free xi'' at beta = -alpha, so only TT and the static lapse are gauge-free); orbital dynamics or a binary comparison; lattice corrections (S3); composite fall at O(binding).
- Controls: two mutations of check.py (halved flux coefficient; changed TT weight) are caught (`controls/`).

## Remaining obligations

1. A compact native source obeying Step 7's identity (first unresolved step, Step 14).
2. Lattice-symbol corrections to the TT dispersion and to the multipole expansion.
3. Gauge-fixed dynamical lapse and an orbit-level comparison; no speed exclusion is implied.
4. Composite fall at O(binding) in the same fields (T72 stands).
5. A referee that is not the same model family.
