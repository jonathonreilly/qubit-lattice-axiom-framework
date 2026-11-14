# D4 gauged zoom rungs n = 1, 2, 3 from a Wilson seed in supplied U(1) backgrounds: on small tori the measured decay rate does not fall with roughness, and the Ginsparg-Wilson residual of one source column falls slowly with n; exact GW and the n -> infinity limit in a background are open

Date: 2026-10-26
This is working research on a supplied model. It has no audit-ledger row or audit status; landing grants no standing.
Verification: finite compute checks, with a truncated-solver control. Run `python3 research/d4-gauged-finite-rungs/gauged_rungs.py` from the repository root. The [runner](gauged_rungs.py) declares a 120-second cap and exits nonzero on a failed check. The [committed cache](../../logs/runner-cache/gauged_rungs.txt) records its exact source/input identities and output. The finite diagnostics do not verify the infinite-volume or infinite-rung claims listed below as open obligations.

Authorship and reading: the original source author family is not established by the available provenance. The computation was carried in Anthropic Claude's consolidation commit 899b749fedb05c696a625fabb66b30975c7824ce and repaired in d42ecd1d1d7d226fd80776da8591844a60feca5c, whose Provenance trailer records Anthropic Claude Opus 5.5. OpenAI supplied the present scope corrections and research packaging. A separate OpenAI gpt-6-astra/low session reviewed the source and compared the gauged operator with an independently assembled finite dense saddle system; the landing record carries that review's disposition and evidence. This provenance assigns no standing.

Historical pre-registration claim: the author reports criteria_pre_run.txt preceded computation; that file is not carried here and its timing is not independently verified.
Labels: [T] exact or theorem; [F] finite diagnostic; [A] external literature context; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Question
For the supplied finite-rung model below, how do fitted spatial decay, chirality residuals and the overlap index vary across the stated U(1) backgrounds? No dynamical links or loops are present. The results concern n <= 3 on finite tori, not a limit theory or an adopted matter law.

Supplied model and scope
Events are D4 = {x in Z^4 : sum x_i is even}. Each event carries four supplied complex spinor components with Hermitian Euclidean gamma matrices satisfying {gamma_mu, gamma_nu} = 2 delta_mu_nu. This is an auxiliary supplied model, not a derivation from the one-qubit-per-site axiom.
The 24 roots are the vectors +/-e_i +/-e_j, i < j. The Wilson seed is
D_NN(x,y) = 2 I delta_xy + sum_r U(x,x+r) (gamma.r - I) delta_(y,x+r) / 12,
with periodic/twisted identifications and straight-line U(1) transport as specified below. No uniqueness or physical selection of this seed is claimed.
The blocking mask is supplied: w(0)=1; w(r)=1/2 for roots; w(v)=1/8 for the 24 D4 vectors with |v|^2=4; zero otherwise. Its sum is 16 and sum_X w(x-2X)=1 for each fine site (the 16 residue classes of D4/2D4). alpha=1/2 is fixed throughout. The runner implements both this position-space construction and its free momentum-space reference; no result from a deferred companion note is a premise.

Construction
- [T] Gauged zoom: G_{l+1} - alpha = 8 B_l (G_l - alpha) B_l^dag.
  - B_l(X, x) = (1/16) w(x - 2X) T(2X -> x), with w = 1, 1/2, 1/8 (the supplied mask defined above).
  - T is the straight-line parallel transporter of a continuum background A. This is gauge-covariant blocking in the
    classically-perfect-action style [A: Hasenfratz-Niedermayer; Bietenholz-Wiese "blocking from a finer lattice"].
  - The seed is the supplied NN D4 Wilson operator defined above, gauged by the same A, on a 2^n-finer D4 torus.
  - D_n = G_n^-1 comes from the Woodbury form D_n = K^-1 - 8^n K^-1 B M^-1 B^dag K^-1, with
    M = D_NN + 8^n B^dag K^-1 B and K = alpha(1 - 8^n B B^dag).
  - For each one-step blocking matrix, unit-modulus transport and the mask partition give ||B_l||_infinity <= 1 and ||B_l||_1 <= 1/16, hence ||B_l||_2^2 <= 1/16. For the n-step product B this implies K >= alpha(1 - 2^-n) I > 0 for n >= 1; this is a Hermitian quadratic-form bound, not entrywise ordering of a complex matrix.
  - The inverse formula assumes M is invertible. When D_NN has zero modes, it is the continuous Schur-complement extension wherever M remains invertible; no general invertibility theorem for all backgrounds is claimed. Fine solves use GMRES with the recorded residual checks; success on the sampled right-hand sides is not a global invertibility certificate. No dense fine matrix is formed.
- [T] GW propagation identity: {g5, G_{l+1} - alpha} = 8 B {g5, G_l - alpha} B^dag, because B is spin-diagonal. GW for
  D = G^-1 with constant alpha is the statement {g5, G - alpha} = 0. So a seed that already satisfies {g5, G_0 - alpha} = 0
  gives an exactly GW D_n at every n.
- The Wilson seed used here does NOT satisfy it. The identity carries its breaking X_0 = {g5, G_0 - alpha} along as
  X_n = 8^n B X_0 B^dag (B the composite blocking). Whether X_n -> 0 as n -> infinity in a background needs a uniform
  bound that this note does not supply. So exact GW for the Wilson-seeded limit in rough backgrounds is an OPEN
  obligation. The runner measures the residual only at n = 1, 2, 3 (2a).
- Backgrounds on D4 tori with coarse box L_c = 2, 4, 6:
  - Q = 0, +-1 constant flux, with twisted transition functions;
  - "IR" Fourier modes, with wavelengths down to the coarse spacing (the fine field is a smooth interpolation, as for an
    HN minimising field);
  - "UV" modes, down to the finest spacing (rough at every level).
  - Roughness eps is the maximum over coarse triangle plaquettes of |1 - U_p|. eps = 1/30 is only an external comparison scale: the Hernandez-Jansen-Luscher sufficient bound concerns the standard hypercubic Wilson operator and square plaquettes, not this D4 operator or its triangular roughness. No D4 locality or admissibility theorem is imported from that bound. eps = 1.9 is near the maximum of 2.

Results
- [F] 0a. Free limit: the gauged position-space code at A = 0 equals the self-contained momentum-space blocking map R^n(G_NN) to 5e-12
  (L_c = 4, n = 1; L_c = 2, n = 2, 3).
- [F] 0b. Gauge covariance D_n[A + d lambda] = L^-1 D_n[A] L holds to 9e-16, and g5-hermiticity to 4e-11 (Q = 1, eps = 1.2).
- [F] 1a. Locality on L_c = 6, n = 1: decay rate of the envelope of ||D(x,y)||_F, in D4 units.
  - Free: 1.79/unit.
  - IR modes at the external comparison value eps = 1/30: 1.79.
  - Q = 1: 1.80.
  - IR modes, eps = 0.3: 1.80. IR modes, eps = 1.0: 1.82.
  - Q = 1 plus IR modes, eps = 1.0: 1.82.
  - UV modes, eps = 1.0: 1.81. UV modes, eps = 1.9: 1.88.
  - The rate does not decrease with roughness at all. It rises slightly. [S] Phase decorrelation of the tail is an untested interpretation of that increase.
- [F] 1b. Locality on L_c = 4, n = 2 (fine 16^4 D4 torus, 131k unknowns per solve): free 2.07; Q = 1 plus IR modes at
  eps = 1: 2.55; UV modes at eps = 1.9: 2.23. GMRES needs 68-78 iterations to converge to 1e-10. [S] Reading, not computed:
  the low-rank term 8^n B^dag K^-1 B of M lifts the smooth near-zero modes of D_NN; the gap of M was not computed.
- [F] Solver status (repair 2026-11-14, finding 4 of the 2026-11-13 hold). The source runner ignored the GMRES `info`
  flag and suppressed warnings, so a cache could pass on an unconverged solve. The runner now records every fine solve,
  requires info == 0 and an independent residual ||M x - b|| / ||b|| <= 1e-9 for each, and makes every check that uses
  solves depend on that. In the regenerated cache all 512 recorded solves have info == 0, and the largest independent residual prints as 1e-10.
  Control 0c: a solve cut to 5 GMRES iterations is flagged (info 1, residual 0.18). The numbers in 0a-3b did not change.
- Scope of 1a/1b. Each rate is a fit of the envelope of ||D(x, y)|| from one source site y over a finite distance window
  (1.3 to 4.6 on L_c = 6; 1.3 to 3.1 on L_c = 4). It is a finite diagnostic at n = 1 and n = 2, not a uniform
  exponential-locality bound, and not a statement about n -> infinity.
- [F] 2a. GW residual ||(g5 D + D g5 - 2 alpha D g5 D) e_0|| / ||D e_0|| for n = 1, 2, 3 (L_c = 2), on ONE source
  block-column e_0 (the four spinor columns at coarse site 0), not the full matrix:
  - free: 2.0e-2, 9.0e-4, 3.9e-5 (a factor of about 22 per step);
  - Q = 1: 0.19, 0.14, 0.088 (x1.4, x1.6);
  - UV, eps = 1: 2.9e-2, 1.9e-2, 1.8e-2 (x1.5, x1.1).
  - An IR background in a development run gave x2.1, x1.9 (dropped from the runner to save time).
  - The residual is monotone in every background, but the decrease is SLOW in a background.
- [F] 2b. Column change ratio ||v_3 - v_2|| / ||v_2 - v_1|| with v_n = D_n e_0 (same source column): free 0.05; Q = 1: 0.67;
  UV: 0.07. Correction (2026-11-14): the source text called this the full-matrix ratio ||D_3 - D_2|| / ||D_2 - D_1||; the
  runner computed (||v_3 - v_2|| / ||v_3||) / (||v_2 - v_1|| / ||v_2||) for one column. The regenerated cache prints
  both column forms, which agree to the two digits shown. The full-matrix ratio was not computed. Three rungs do not show
  convergence as n -> infinity; that is OPEN.
- [F] 3a. Overlap index -(1/2) Tr sign(g5(2 alpha D_n - 1)) = -Q for Q = 0, 1, -1. This holds for smooth backgrounds and
  for eps = 1.2, at n = 1 and 2. The spectral gap is >= 0.22; on this L_c = 2 torus, Q = 1 means a flux of pi/2 per
  coarse unit area.
- [F] 3b. In Q = 1, the lowest mode of D_n is real and chiral to the printed precision (g5 = -1.000). It sits at
  lambda_0 = 0.78 (n = 1) and 0.50 (n = 2), a ratio of 1.57: it moves toward 0. Whether it reaches 0 as n -> infinity
  is not computed.
- [S] Reading of 2a and 3b: in a background, the Wilson seed's chirality breaking is the dimension-5 Pauli term
  (a sigma.F). Blocking suppresses it only as 2^-n. In the free theory the leading breaking is a contact term that the
  zoom absorbs, so its residual falls about 16-23x per step. Expected background rate: about 2 per step. Observed:
  1.4-2.1. The UV case is slower, because the field stays rough at the n = 3 fine scale.

Verdict (pre-registered rule, read for the measured cases only)
- C1: PASS at the measured rungs. The fitted rates from one source site are 1.79-1.88 (n = 1, L_c = 6) and 2.07-2.55
  (n = 2, L_c = 4). They are >= 0.8 x free at the external comparison value eps = 1/30 and >= 1.0 up to eps = 1.9. In this tested range the rate
  does not fall with roughness, including above that comparison value; no sufficient D4 bound is asserted.
- C2: index PASS: index = -Q in smooth and rough backgrounds at n = 1, 2 on L_c = 2, and the chiral lowest mode moves
  toward 0. MISS on the pre-registered bar of a x1.5 decrease per step (Q = 1, n = 1 -> 2: x1.4; UV, n = 2 -> 3: x1.1).
  Exact GW is not established for the Wilson seed at any n or in the limit (see Construction).
- C3: PASS for the column analogue: every column ratio is <= 0.7 (worst 0.67, Q = 1). The pre-registered full-matrix ratio
  was not computed.

Interpretation of the finite diagnostics
- The measured finite-rung kernels (n = 1, 2) have fitted decay rates that do not fall across the tested roughness grid. The exact n -> infinity kernel in a background was not computed. This note decides no candidate-law adoption or withdrawal.
- The one-column GW residual fell by x1.1 to x1.6 per step in the sampled backgrounds, against about x22 in the free case. A 2^-n background scaling law is an untested interpretation, not a measured asymptotic law.
- Still open (walls move):
  - non-abelian backgrounds;
  - dynamical links and loops (the truly interacting case);
  - the HN fine field from minimisation, instead of a continuum interpolation;
  - larger tori, and more blocking steps on L_c >= 4;
  - a Combes-Thomas-type proof that the gap of M bounds the locality rate (suggested by 1b; not proven);
  - the n -> infinity limit in a background: convergence, uniform locality, and whether the GW residual of the Wilson
    seed vanishes (the identity alone does not give it);
  - the full-matrix convergence ratio and the full-matrix GW residual (only one source column was measured).

Smuggling gate
- (1) No fitted number. alpha = 1/2 is supplied and fixed; no parameter-independence claim is made. eps is a stress grid, not a fit. PASS.
- (2) No observed structure named. U(1) backgrounds are test inputs, not rules. PASS.
- (3) Untested predictions (no rule is proposed here):
  - the locality rate is independent of the background;
  - the finite-n chirality error falls as 2^-n times the coarse field strength.
  Both are UNTESTED beyond these tori.
- (4) The four spinor components, D4 events and finite blocking family are supplied model choices, not consequences or amendments of the framework axioms.
Gate: no framework law, axiom or primitive is adopted.

Smuggling review
- Supplied: the kernel weights. Exact conditional identities: the Woodbury form; K > 0; GW propagation under blocking; gauge covariance; the
  free-limit identity.
- Supplied:
  - the NN Wilson seed;
  - straight-line transporters and continuum-mode backgrounds (not HN minimisation);
  - the eps grid; the tori; n <= 3;
  - [A] HJL, HN and Bietenholz-Wiese.
- Fitted: none.

Sources and recovery
The construction follows the gauge-covariant blocking style of Hasenfratz-Niedermayer and Bietenholz-Wiese, but its definitions and finite calculations are given here and in the paired runner. Their general perfect-action/locality conclusions are not premises of these finite diagnostics.
Hernandez, Jansen and Luscher, "Locality properties of Neuberger's lattice Dirac operator" (arXiv:hep-lat/9808010), supplies only the explicitly external comparison value, not a theorem for this model.
Historical companion sources were #10098 (free fixed-point construction), #10111 (finite rungs), #10099 (slab/index work), and the consolidation in PR #10130. Those companions are deferred; no conclusion, candidate decision or unexported CANDIDATE_AXIOM_RULES.md text from them is adopted here. Their exact original content remains in PR #10130's recorded frozen-head recovery ref.

Review correction
The earlier entrywise K argument is replaced by the operator-norm bound above, invertibility is explicit, and the hypercubic HJL threshold is no longer labelled D4 admissibility. This note concerns only the supplied finite model and assigns no standing.

Deviations from pre-registration
- C2's bar of x1.5 per step was missed in 2 of 6 steps. Reported as MISS. The runner checks monotone decrease instead.
- Runtime is 68 s, against a 60 s target (AUDIT_TIMEOUT_SEC = 120 is kept). The IR background was dropped from 2a/2b to fit
  the time.
- Q = 1 cannot meet eps <= 1/30 on these tori: its own flux gives eps = 0.09 (L_c = 6) and 0.77 (L_c = 2). So the
  tested subset at the comparison value eps = 1/30 is Q = 0 plus modes. Q = 1 is tested only above that comparison value.
- The index was computed on L_c = 2 (n = 1, 2) rather than L_c = 4. Full D_n on L_c = 4 needs 512 fine solves, which is
  too slow.
- GMRES tolerance: 1e-10 (the free-limit agreement is 5e-12).
