lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:47Z

# gap-mini-solve-ak-opus: the SU(2) mass gap, attack plan and steps

Queue row 1267 of `FINISH.md`. Started 2026-11-20T11:47Z (date -u), at commit a05f4c020 on branch claude/ym4d-hard-route.
Research-stage working state; grants no status. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Orientation and plan (written 2026-11-20T11:51Z by date -u)

**0.1 Read for this row.** `GOAL.md`; `FINISH.md` sections Where it stands, How we work, Joining, Working efficiently,
Rules, and the recorded RESULT lines of rows 1150-1265; `parts/gap.md` State of attack; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; row 1260 (`gap-mini-solve-ai-opus.md`) in full. Summaries are pointers, not evidence; each statement
used below is re-read at its source.

**0.2 Where the problem stands (pointers).**
- The Jaffe-Witten gap on the account's tr F^2 sector reads, beside the account's premises, one infrared input: (N-phys)
  (rows 1161, 1179), or on the one-cutoff carry of row 1233 a seed at one base datum; row 1258 (check 1265: HOLDS) gives a
  sufficient one-coupling form, (SL) or (RR) at one cutoff's couplings.
- Every route family to the infrared seed found by about ninety plain-brief rows is on file with a first failing step
  (`parts/gap.md` methods 19-36 and route registry; screening tables of rows 1189, 1194, 1199, 1237). The published
  sources of row 1218 do not supply it: A (Bhattacharjee et al.) gives a stronger one-scale thermal criterion with a
  conditional ascent; B's Corollary 166 is a weak-coupling bound for straight-path block variables of length b = 2^k at
  beta_W <= k + 2. GUIDE (my reading, not a proof): at that coupling the straight-path variables are close to Haar by
  ultraviolet noise (variance of order g^2 b along a straight path), so the bound holds for the same reason it would hold
  for compact U(1); it is blind in the sense of `parts/gap.md` (row 998 6b) and cannot carry the band.
- The one-cutoff carry on the pin route (rows 1233, 1255, 1256, 1260) has one named open input that no row has attacked:
  **(FC)**, row 1260 (G3): at one step and at the same weights, forming the unmarked coefficient on the frozen frame
  theta_r = X + c_0 r or on the run's own frame changes it by eta_k, with sum_k eta_k bounded uniformly in the cutoff.
  Row 1260 5.2 splits it (GUIDE) into a cut-comparison estimate for YM4_EM's all-small-field kernel and a partition
  matching.

**0.3 Plan (judgement).** The infrared seed is the open core. No session-sized route to it is on record, and row 998 9.5
asks for no further fresh-framing exercise, so I do not re-screen it. I take (FC).
Moves: (FC), the open input of the gap chain's ultraviolet carry (row 1260 4.3). Success: (FC) proved from statements
of Sussman and Alpoge's YM4_EM (their premises named), so the pin-route carry reads no (FI). Failure: the first EM
statement (FC) needs and EM does not state, or a counterexample (a frame-dependent discrete choice that moves the
coefficient by a non-summable amount).
Steps: 1 read EM's formation of the coefficient (actual step, kernel, cut, gauge weight, envelope theorem, slopes) and
pin down exactly what depends on the frame; 2 state (FC) precisely in EM's notation; 3 prove the cut comparison, or name
its first failing step; 4 the discrete choices; 5 status table and RESULT.

## Step 1. How the frame enters EM's coefficient (written 2026-11-20T11:54Z by date -u; READ unless marked)

Source: Sussman and Alpoge, `YM4/EM/YM4_EM.tex` at c7fef8b21b58 ("Iteration of regular interactions on prescribed
coupling prefixes", working draft of 9 November 2026), 2001 lines, read in full through L1456; fetched by URL into a
scratch folder outside the repository. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text; the construction is Balaban's (CMP 109, 116 as EM cites them). EM:n is a TeX line.

**1.1 What the frame fixes.** "The frame fixes the lattice partitions, Gaussian references, real fluctuation coordinates
and tests. The variable x_k does not change those choices" (EM:503-506). The actual step (EM:556-561) is
E_(k+1)[x_k, f](W) = log int K_(k,theta_k)(W, dV) exp(-x_k A(U_k(V)) + S_f(U_k(V))) + x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W)),
with K_(k,theta_k) "the fixed all-small-field kernel on M(V) = W. It uses the given fibre density, gauge weight and
fluctuation cut" (EM:544-546). Inside one frame, the weight enters the Gaussian part only through tau_k = x_k/theta_k
(EM:584-589), and "the gauge compensation on the right is still a factor on the cut" (EM:594-595).

**1.2 The output and its coefficient.** One step gives E_(k+1) = N_(k+1) + G_(k+1,tau_k) + F_(k+1)[f] with
||F|| <= K(delta(theta_k) + s N_k + exp(-c theta_k delta(theta_k)^2)) (EM:679-684), N_(k+1) normalized by
sum N_(k+1) = log Z_k(W) - log Z_k(1), Z_k "the supplied actual constrained reference Gaussian normalizer without a
fluctuation cut" (EM:694-700). The scalar coefficient is the second moment of the polarization kernel at the trivial
datum, b_j(E) = sum_u Pi_(E,mu nu)(u) u_mu u_nu (EM:1191-1193); "It is unchanged by admitted restriction of the same
functions around P_o and by changing coherent localizations of the same physical total" (EM:1202-1204), and
|b_j(E)| <= C a^(-2) A for a family of norm A on a pair ball of radius a (EM:1201). Theorem `em:thm-coefficient-envelope`
(EM:1338-1376): b_(k+1) = b^0_(k+1) + f_(k+1)(z_0, ..., z_k) + q_(k+1) with b^0 = b(N), f = b(F^u), q = b(E^m); the
Gaussian mismatch has coefficient zero by the action-gauge splitting of GI Proposition 4.3 (EM:1326-1335); the unmarked
residual lives on the absolute core of fixed radii, "so the extraction bound costs a fixed constant for f_(k+1)"
(EM:1383-1384), and |f_(k+1)| <= C theta_k^(-1/2) (log theta_k)^(p_0).

**1.3 Consequence for (FC) (PROVED, elementary, from 1.2).** In row 1260's notation the unmarked total at frame phi and
weights w is U_(k+1)(phi; w) = b(N^phi_(k+1)) + b(F^(u,phi)_(k+1)[w]). So
U_(k+1)(phi; w) - U_(k+1)(w; w) = [b(N^phi) - b(N^w)] + b(F^(u,phi)[w] - F^(u,w)[w])          (1.3a)
by linearity of b (EM:1202), provided both families are read on one common absolute pair core (fixed radii, so a fixed
extraction constant C_x):
|b(F^(u,phi)[w] - F^(u,w)[w])| <= C_x || F^(u,phi)[w] - F^(u,w)[w] ||_(abs).                     (1.3b)
Bounding the two frames separately does not work: each |f| is at most C theta_k^(-1/2) (log theta_k)^(p_0), and along a
pin run theta_k is about X + c_0 (n - k), so sum_k theta_k^(-1/2) grows like n^(1/2). So (FC) needs (i) the Gaussian
part, b(N^phi) = b(N^w), and (ii) a *difference* bound for the unmarked residual under a change of frame at fixed
weights, summable in k.

**1.4 What can move with the frame (READ, EM:544-546, 611-656).** At fixed weights and list: the fluctuation cut ("a
fixed Borel restriction in the real free variables"), the gauge weight ("invariance of an arbitrary gauge-fixing weight
is not assumed"), the fibre density, the Gaussian reference (a presentation of the same integral, EM:580-581), the real
fluctuation coordinates, the localization and its partitions, and the creation radius c_e epsilon(theta_k). The
localization does not move the coefficient (EM:1202-1204), and the radius moves only where a function is read. EM states
the one-step inputs for one frame and does not say how K_(k,theta) depends on theta. So the remaining items are the
cut, the gauge weight, the fibre density and the normalizer Z_k; Step 2 reads them in the companion manuscripts GI
(Gaussian block integration) and RT (trajectories and partition stability).

## Step 2. The Gaussian part of (FC) vanishes exactly (written 2026-11-20T12:01Z by date -u)

Sources (READ; credit Sussman and Alpoge, with Claude and Codex as authors of their text): `YM4/GI/YM4_GI.tex` ("Gaussian
block integration and free action-density correlations") at c7fef8b21b58, L606-1170, and `YM4/RT/YM4_RT.tex` L491-760,
L1809-2024, same commit. GI:n, RT:n are TeX lines.

**2.1 READ.** GI Theorem `gi:thm-relative-gauge` (GI:661-679): the relative normalizer
J(B, Q, R, G) = sqrt(det R R^*) |det(G D_0)| I(B + G^* G, Q), with I(T, Q) = int delta_F(Q x) exp(-<x, T x>/2) dx (GI:627-630),
does not depend on the residual gauge coordinate G. GI (gi:eq-axial-constant, GI:898-909): for the actual axial coordinate,
sqrt(det R_0 R_0^*) |det(G_ax D|ker R_0)| = c_(eta,j) does not depend on the background. GI Proposition
`gi:prop-physical-normalizer` (GI:968-1006): the background dependence of the plain-fibre Gaussian normalizer is the
difference of two saddle log-determinants built from B_fib, Q, R, D. GI Proposition `gi:prop-action-gauge-powers`
(GI:1062-1078) is the convention "scaling the action while keeping the gauge weight": K_tau = tau K_A + K_G. EM uses it as
"[GI, Proposition 4.3]" for the Gaussian mismatch family G_(k+1,tau), whose total is "a background-free number" (EM:1326-1335).
RT input (2) (RT:713-732) requires "The actual one-loop data are independent of the initial weight, admissible torus and
unused finer horizon", and RT:570-579 says that in the self-calibrated convention the free-link coordinates are scaled by
x_(j-1)^(-1/2) and that the cut and every gauge-compensation factor stay inside the integral.

**2.2 Hypothesis (A1)** (the reading of EM's "Gaussian references" that EM:694-700 and GI:968-1033 describe). At step
k -> k+1 and frame entry theta = theta_k, the reference Gaussian normalizer Z^theta_k(W) of EM:694-700 is the plain-fibre
normalizer c_Haar c_soft I(theta B + G^* G_theta, Q_0) (no cut), where B = B_fib(W) - Q^* H_c Q is the fibre Hessian of the
unit-weight Wilson action at the constrained background U_k(W) (as in GI (gi:eq-given-complete-hessian)), Q_0, D, R are the
constraint and gauge maps at that background, and the gauge coordinate G_theta is either theta^(1/2) G (gauge weight scaled
with the frame, GI Proposition 4.3's convention in frame-normalized coordinates) or G (fixed in field units); B, Q_0, D, R,
G do not depend on theta, and c_Haar, c_soft do not depend on W. (The background U_k(W) is the constrained minimizer of the
Wilson action, which is the same for every positive weight; the Lagrange multiplier scales with the weight, so
B_fib for weight theta is theta B_fib.)

**Lemma A (PROVED given (A1) and GI's standing hypotheses of Theorem `gi:thm-relative-gauge`).** For any two frame
entries theta, theta' > 0 there is a constant c(theta, theta') with Z^theta_k(W) = c(theta, theta') Z^(theta')_k(W) for
every admitted physical datum W. Hence the normalized Gaussian families of EM (eq-rs-formation) formed on two frames have
the same total on physical data,
    sum_(X,z) N^phi_(k+1)(X, P_(k+1)(W), z) = log Z^phi_k(W) - log Z^phi_k(1) = sum_(X,z) N^psi_(k+1)(X, P_(k+1)(W), z),
and the Gaussian number b^0_(k+1) = b_(k+1)(N_(k+1)) of EM Theorem `em:thm-coefficient-envelope` does not depend on the
frame: b^0_(k+1)[phi] = b^0_(k+1)[psi] for every two frames phi, psi.
*Proof.* Case G_theta = theta^(1/2) G. The precision is theta (B + G^* G). Substitute x = theta^(-1/2) y in
I(theta T, Q) = int delta_F(Q x) exp(-theta <x, T x>/2) dx. Then dx = theta^(-dim E/2) dy and
delta_F(Q theta^(-1/2) y) = theta^(dim F/2) delta_F(Q y), since delta_F is homogeneous of degree -dim F on F. So
I(theta T, Q) = theta^(-(dim E - dim F)/2) I(T, Q), with an exponent that does not depend on W.
Case G_theta = G. By Theorem `gi:thm-relative-gauge` the relative normalizer does not change if G is replaced by
theta^(1/2) G. Writing r = dim ker R, so that |det(theta^(1/2) G D_0)| = theta^(r/2) |det(G D_0)|,
    sqrt(det R R^*) |det(G D_0)| I(theta B + G^* G, Q) = J(theta B, Q, R, G) = J(theta B, Q, R, theta^(1/2) G)
        = sqrt(det R R^*) theta^(r/2) |det(G D_0)| theta^(-(dim E - dim F)/2) I(B + G^* G, Q),
by the first case applied to T = B + G^* G. The factors sqrt(det R R^*) |det(G D_0)| are the same on both sides and
nonzero, so I(theta B + G^* G, Q) = theta^((r - dim E + dim F)/2) I(B + G^* G, Q). (By (gi:eq-axial-constant) the factor
|det(G_ax D_0)| does not depend on W either, but the cancellation does not need this.)
In both cases log Z^theta_k(W) - log Z^theta_k(1) does not depend on theta. The normalization of N_(k+1) (EM:694-697) is
exactly this difference, so the totals agree. The coefficient b_(k+1) depends only on the total (EM Proposition
`em:prop-companion-coefficient`, EM:1202-1204: "unchanged ... by changing coherent localizations of the same physical
total"), so b^0_(k+1) agrees. QED

**Lemma Z (PROVED, from EM:1326-1335 and Lemma A).** Let phi, psi be two frames, admitted with the same weight prefix
x_(<= k). Then on physical data, including the complex continuation along physical backgrounds on a connected domain that
meets the real slice:
(a) the vacuum-subtracted total of each Gaussian mismatch family G_(j,tau) is zero, in either frame;
(b) N^phi_j - N^psi_j has vacuum-subtracted total zero;
(c) the Wilson counterterm coefficients of the level-j regular members in the two frames differ by
    b_j(F^phi_j) - b_j(F^psi_j) only.
*Proof.* (a) EM:1330-1333: the total of G_(j,tau) "is a background-free number" throughout the admitted physical chart; its
vacuum-subtracted total is therefore zero on real physical data; the composed total is holomorphic and vanishes on an
open real set, so it vanishes on the connected complex domain (identity theorem; EM uses the same continuation at
EM:748-753 and RT at RT:1915-1919). (b) Lemma A and the same continuation. (c) b_j is linear (EM:1202), b_j(G_(j,tau)) = 0
(EM:1333), and b_j(N^phi_j) = b_j(N^psi_j) by Lemma A. QED

**2.3 What Lemma Z does to (FC).** The integrand of step k+1 reads the list f only through its total S_f(U) on physical
backgrounds (EM:538-561). By Lemma Z, for the unmarked lists f^phi, f^psi of the two frames,
    S_(f^phi)(U) - S_(f^psi)(U) = sum_(j <= k) [ Tbar(F^phi_j) - Tbar(F^psi_j) ](U) - sum_(j <= k) [ b_j(F^phi_j) - b_j(F^psi_j) ] A_j(U),
where Tbar is the vacuum-subtracted total and A_j(U) the level-j Wilson action pointed by the tents (EM:276-283). The
Gaussian families N and G drop out exactly. This matters for summability: G_(j,tau) has pointed norm up to B_G |1 - tau_j|
(EM:690), and between the frozen frame and the run's own frame |1 - tau_j| can be of order theta_j^(-1/2) polylog (row 1260
2.1); charged through a one-step comparison with factor s_k of order theta_k^(-1/2) polylog, it would give a per-step load
of order theta_k^(-1) polylog, whose sum over a pin run diverges. By Lemma Z this load is absent: it is an artefact of
measuring a list difference in pointed norm when the total is zero.

**2.4 Which frame-dependent choices the unmarked chain reads (READ).** The unmarked list "uses only its own regular
outputs, from levels 1, ..., k. Both lists begin with no entries" (EM:535-536); its localization cubes have the fixed side M
(EM:176-178); the age gate with R-check_j = R(min theta_i) (EM:364-380) selects remainders, which enter only the full
chain (EM:524-528); the absolute chain has fixed radii a_* (EM:506-510); the creation radius c_e epsilon(theta_k)
(EM:653-656) fixes where covariance is read, not the function. So, beside the Gaussian reference (Lemma A), the unmarked
chain reads the frame only inside the actual kernel K_(k,theta_k): its fluctuation cut, its gauge weight and its real
fluctuation coordinates (EM:544-547, 619-621; RT:708-712). The fibre density does not depend on the frame (GI:926-966:
central Haar factors depend on the meshes only). **So the partition matching of row 1260 5.2 (iii) is not needed for the
unmarked total**; what is left of (FC) is a comparison of two kernels at the same weights and list.

## Step 3. From one-step kernel comparisons to (FC): the chain (written 2026-11-20T12:06Z by date -u)

**3.1 A seminorm on totals.** For a level-j physical total T (a function of the physical datum near the trivial datum
P_o on each compatible torus and on the companion), put
    |||T|||_j := inf { ||H||_(j,kappa;a_*) : H a regular pointed family at level j on the absolute core whose total is T + const },
where "regular" means the companion, covariance and response hypotheses of EM Propositions `em:prop-physical-polarization`
and `em:prop-companion-coefficient` (inf of the empty set = infinity). Regular families form linear spaces (EM:215-218), so
|||.|||_j is a seminorm that ignores additive constants. The coefficient depends only on the total (EM:1202-1204) and
|b_j(H)| <= C a_*^(-2) ||H|| (EM:1201), so
    |b_j(T)| <= C_x |||T|||_j,   C_x := C a_*^(-2), a fixed constant on the absolute core.                 (3.1)

**3.2 Setting.** Fix n and two frames phi = (phi_0, ..., phi_n), psi = (psi_0, ..., psi_n) above the floor, and one real
weight prefix x = (x_0, ..., x_n) with |x_j/phi_j - 1| and |x_j/psi_j - 1| below sigma_*/2. For theta in {phi, psi} let
E^theta_(k+1) := E^(u,theta)_(k+1)[f^theta_k] be the unmarked output of EM Proposition `em:prop-prefix-formation` on the
frame theta at the weights x, with f^theta_k its unmarked list (the regular outputs of levels 1, ..., k, vacuum
subtracted, each with its own counterterm; f^theta_0 empty). Write T(.) for the total and Tbar_i(f) for the total of the
i-th member of a list (vacuum and counterterm subtracted). By EM Theorem `em:thm-coefficient-envelope` the unmarked total
coefficient of row 1260 is U_(k+1)(theta; x) = b^0_(k+1) + f_(k+1) = b_(k+1)(T(E^theta_(k+1))).

**Hypotheses.**
- (H1) EM's one-step inputs (EM:611-716) and the conclusions of EM Proposition `em:prop-prefix-formation` hold on both
  frames at the weights x, on the absolute cores, with the same constants.
- (H2) Cross-admission: each unmarked list f^psi_k is an admitted list for the step k of the frame phi (cores, companions,
  covariance balls, norm cap E_0).
- (H3) The one-step list comparison in total form, on the frame phi: for lists f, f' admitted in its step k,
      |||T(E^phi_(k+1)[f]) - T(E^phi_(k+1)[f'])|||_(k+1) <= K s_k sum_(i <= k) omega_(k+1-i) |||Tbar_i(f) - Tbar_i(f')|||_i.
  (ARGUED from EM input (4), EM:707-716. Given localizations h_i of Tbar_i(f) - Tbar_i(f'), the list f'' with members
  f_i - h_i has the totals of f', hence the same integrand (the step reads a list only through its total on physical
  data, EM:538-561, continued to the decoupling contours by the identity theorem as in EM:800-808), hence the same total
  output; input (4) bounds ||F[f] - F[f'']|| by K s_k sum omega ||h_i||; take the infimum over h_i. This needs f'' to be
  admitted.)
- (H4) **= (FC-1), the one-step frame comparison**: for each k < n and each list f admitted in both frames' step k,
      |||T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f])|||_(k+1) <= nu_k.
- (H5) K s_* (1 + C_x C_A) Omega <= 1/2, with s_* := sup_k s_k (absolute chain, s_k = delta(phi_k)/a_(*,0), EM:686-688),
  Omega = sum_n omega_n (EM Lemma `em:lem-age-kernel`), and C_A the pointed norm of the tent Wilson insertion
  (EM:1302-1311).

**Proposition FC-chain (PROVED, an implication from (H1)-(H5)).** Put u_i := |||T(E^phi_i) - T(E^psi_i)|||_i. Then
    u_(k+1) <= nu_k + K s_k (1 + C_x C_A) sum_(i=1)^k omega_(k+1-i) u_i   for 0 <= k < n,                (3.2)
    sum_(i=1)^n u_i <= 2 sum_(k=0)^(n-1) nu_k,                                                             (3.3)
and the unmarked coefficients of the two frames at the same weights satisfy
    eta_k := |U_(k+1)(phi; x) - U_(k+1)(psi; x)| <= C_x u_(k+1),   sum_(k<n) eta_k <= 2 C_x sum_(k<n) nu_k.   (3.4)
*Proof.* Split
T(E^phi_(k+1)[f^phi_k]) - T(E^psi_(k+1)[f^psi_k]) = [T(E^phi_(k+1)[f^phi_k]) - T(E^phi_(k+1)[f^psi_k])] + [T(E^phi_(k+1)[f^psi_k]) - T(E^psi_(k+1)[f^psi_k])].
The second bracket is at most nu_k by (H4) at the list f^psi_k, admitted in both frames by (H2). For the first, (H3) on the
frame phi applies to the lists f^phi_k, f^psi_k. Their i-th members differ in total by
T(E^phi_i) - T(E^psi_i) - [b_i(E^phi_i) - b_i(E^psi_i)] A_i up to a constant, so by (3.1)
|||Tbar_i(f^phi) - Tbar_i(f^psi)|||_i <= u_i + C_A C_x u_i. The triangle inequality for |||.||| gives (3.2). For k = 0 both lists
are empty (EM:536), so u_1 <= nu_0. Sum (3.2) over k = 0, ..., n-1 and exchange the order of summation:
sum_(k<n) sum_(i<=k) omega_(k+1-i) u_i = sum_(i<n) u_i sum_(k=i)^(n-1) omega_(k+1-i) <= Omega sum_(i<=n) u_i.
So S := sum_(i<=n) u_i <= sum_k nu_k + (1/2) S by (H5), which is (3.3) since S is finite. Finally
eta_k = |b_(k+1)(T(E^phi_(k+1)) - T(E^psi_(k+1)))| <= C_x u_(k+1) by linearity and (3.1); sum with (3.3). QED

**Remarks (PROVED from Step 2 and 3.2).**
- By Lemma A and Lemma Z, u_i = |||T(F^phi_i) - T(F^psi_i)|||_i: the Gaussian families do not enter u_i, and in (H4) the
  difference of totals at one list is the difference of the two interacting logarithms only. Precisely, by EM:556-570 and
  Lemma A, for one list f and one weight x_k,
      T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f]) = log int K_(k,phi_k)(W, dV) e^(Phi(V)) - log int K_(k,psi_k)(W, dV) e^(Phi(V)) + const,   (3.5)
  with Phi(V) := -x_k A(U_k(V)) + S_f(U_k(V)) the same in both frames. So (FC-1) is a statement about the two kernels alone.
- The recurrence (3.2) is causal: u_(k+1) reads nu_k and u_1, ..., u_k only. So in Lemma GR of row 1260, whose induction
  places the prefix of the own-threshold run in the half tube of the frozen frame before reading (G3) at step k, (3.2)-(3.4)
  can be invoked at each k with phi = phi^A (the canonical scaffold prefix), psi = (w^B_0, ..., w^B_k) and x = psi.

**Corollary FC (PROVED GIVEN (H1)-(H5) along the pin runs, with sum_k nu_k <= V uniformly in n).** Row 1260's (G3) holds
with sum_k eta_k <= 2 C_x V. With Lemma GR, Corollary SC-pin holds with varpi_n <= e^Lambda (2 C_x V + 2 sum_k eps'_k),
bounded uniformly in n, and Lemma OFF' of row 1260 puts the first-passage depth of every pin a_n within a bounded distance
of n.

**3.3 Size bookkeeping: why soft bounds do not close (FC-1) (PROVED, elementary arithmetic on the account's envelopes).**
Along a pin run the frozen frame theta_r = X + c_0 r and the run's weights differ by |zeta_(r)|, which the account bounds by
order theta_r^(1/2) (log theta_r)^(p_0) (row 1260 2.1, III:69015-69017). Suppose (FC-1) were bounded only through the
account's envelopes: the residual has norm at most C theta_k^(-1/2) (log theta_k)^(p_0) (EM:1365), and a frame change of
relative size |zeta_k|/theta_k moves it, at best, by that norm times the relative size. Then
nu_k ~ theta_k^(-1/2) (log theta_k)^(p_0) * theta_k^(-1/2) (log theta_k)^(p_0) = theta_k^(-1) (log theta_k)^(2 p_0), and with
theta_k about X + c_0 (n - k), sum_(k<n) nu_k grows like (log n)^(1 + 2 p_0): not bounded in n. So (FC-1) needs structure:
either the frame enters the interacting integral only through events of Gaussian-tail weight, or two-loop-accurate
envelopes (a residual of size theta^(-1) and a drift of size log theta would give theta^(-2) log theta, summable; GUIDE:
these are the perturbative sizes, not proved). Step 4 shows the first alternative for the gauge weight, exactly.

## Step 4. What is left of (FC-1): only the small-field thresholds (written 2026-11-20T12:09Z by date -u)

**4.1 READ.** CA-I Proposition `4.35:prop-gauge-fixing` (I:157457-157600; index status CITED: parts (A), (B) are Balaban's
CMP 99 Theorem 2 and CMP 102 Theorem 1; part (C) is proved in the account). (C)(b): Balaban's representation of the step
"is written in the axial gauge [B-CMP119, (1.5)]; it uses the exponential gauge-fixing term of [B-CMP109, (1.5), (2.11)]
together with its normalisation; it uses the decompositions of unity of [B-CMP119, Section 3], refined by the additional
thresholds at the creation of large-field regions; the integrand of each piece is averaged over gauge transformations
wherever a representative after a reversed Faddeev-Popov step is read". The account's reason that (b) holds: "the
Faddeev-Popov Jacobian of the axial gauge on trees is 1, and ... the exponential gauge-fixing term ..., with its
normalisation, is an exact rewriting of the same integral" (I:157620-157627). (C)(ii): the total integrals "do not depend
on the axial gauge inside T, on the form G of the exponential gauge fixing, or on the representatives chosen at the
reversed Faddeev-Popov steps". The step T itself is the push-forward M_* (C)(b). RT:533-579 charges one truncated Haar
normalizer z(x_(j-1)) = int chi(U) exp(-x_(j-1)(1 - tr U/2)) dU per noncentral site gauge (RT Lemma `rt:lem-haar-normalizer`,
RT:497-531), at the frame's weight in the self-calibrated convention.

**4.2 Lemma AX (exact normalization of a soft axial gauge weight; PROVED, elementary).** Let S be a finite set of fine
sites, S_c a subset of fixed sites, S_nc = S \ S_c. Let T be a set of fine links with exactly one link l_y = (p(y), y) in
T for each y in S_nc, such that following parents y -> p(y) from any y in S_nc reaches S_c (no cycles). Let
G_res = (u : S -> SU(2), u = 1 on S_c) act on link configurations by (V^u)_(x,y) = u_x V_(x,y) u_y^(-1), with product
normalized Haar measure du on S_nc. Let mu be a finite positive measure on configurations (for example a fibre measure of
M) with mu(V^u in .) = mu(.) for all u in G_res; let F be mu-integrable and G_res-invariant; let 0 <= chi <= 1 be Borel;
let w >= 0 be Borel on SU(2) with z := int w dU in (0, infinity). Put
    pi_w[chi](V) := int du chi(V^u) prod_(y in S_nc) w((V^u)_(l_y))/z.
Then (i) int du prod_(y in S_nc) w((V^u)_(l_y))/z = 1 for every V, so 0 <= pi_w[chi] <= 1;
(ii) int mu(dV) F(V) chi(V) prod_(y in S_nc) w(V_(l_y))/z = int mu(dV) F(V) pi_w[chi](V);
(iii) if chi is G_res-invariant, pi_w[chi] = chi, and the left side of (ii) equals int mu F chi, whatever w is.
*Proof.* (i) Order S_nc so that every site comes after its parent (by the length of its parent chain). Integrate the site
variables in the reverse order. When u_y is integrated, all children of y have already been integrated, so u_y occurs
only in the factor w(u_(p(y)) V_(l_y) u_y^(-1)), with u_(p(y)) = 1 if p(y) is in S_c. For fixed a = u_(p(y)) V_(l_y),
the map u -> a u^(-1) preserves normalized Haar measure (inversion and left translation do), so this integral is z.
After |S_nc| such steps the integral is z^|S_nc|; divide. (ii) For each fixed u in G_res, substitute V -> V^u in the
left side: mu is invariant and F(V^u) = F(V), so the left side equals int mu(dV) F(V) chi(V^u) prod w((V^u)_(l_y))/z.
Average over u (Fubini; the integrand is bounded by |F| times a nonnegative product with u-integral 1 by (i)). (iii) If
chi(V^u) = chi(V), then pi_w[chi] = chi by (i). QED
Consequence: the precision and the truncation of a soft axial weight w_theta(U) = chi_theta(U) exp(-theta(1 - tr U/2)),
normalized by its own z(theta), both frame dependent, drop out exactly from every integral of a gauge-invariant integrand
over an invariant cut. This is the mechanism behind the account's 4.35 (C)(b) for the axial device, proved here without
citation; for Balaban's exponential (Landau-type) term of CMP 109 (2.11) the exactness is the account's cited claim.

**4.3 Proposition SPLIT (PROVED, an identity given the kernel form (K)).** Hypothesis (K): at step k the frame-theta
kernel is K_(k,theta)(W, dV) = c_theta mu_W(dV) chi_theta(V) prod_(y in S_nc) w_theta(V_(l_y))/z(theta), with mu_W the
G_res-invariant fibre measure (product Haar disintegrated along M; G_res preserves the fibres by CA-I 4.35 (C)(a) with
u-bar = 1), c_theta > 0 not depending on W, 0 <= chi_theta <= 1 the all-small-field characteristic function of the frame
(its decomposition of unity), and w_theta any soft axial weight with normalizer z(theta). Assume Phi(V) = -x_k A(U_k(V)) +
S_f(U_k(V)) is G_res-invariant (gauge covariance of U_k and invariance of A and S_f, EM:551-554). Then by (3.5) and
Lemma AX (ii), for two frames phi, psi at the same weight and list,
    T(E^phi_(k+1)[f]) - T(E^psi_(k+1)[f]) = log < pi_phi / pi_psi >_psi + const,   pi_theta := pi_(w_theta)[chi_theta],   (4.1)
where <.>_psi is the expectation in the probability measure proportional to mu_W(dV) e^(Phi(V)) pi_psi(V) on the fibre of
W. If the cuts are gauge invariant (for example curvature conditions on plaquettes), pi_theta = chi_theta and the right
side is log < chi_phi / chi_psi >_psi; if moreover the thresholds are nested, chi_phi <= chi_psi (the stricter cut of the
larger frame entry), it is log P_psi(V passes the cut of phi), the logarithm of the probability, in the psi
all-small-field measure, that no local variable lies between the two thresholds.
*Proof.* Insert (K) into (3.5); the factors c_theta are constants; apply Lemma AX (ii) to each frame with F = e^Phi and
chi = chi_theta; then log int mu e^Phi pi_phi - log int mu e^Phi pi_psi = log < pi_phi/pi_psi >_psi (on the set where
pi_psi > 0, which carries the psi-measure). The special cases follow from Lemma AX (iii) and chi_phi chi_psi = chi_phi. QED

**4.4 The full-measure reading (PROVED from CA-I 4.35 (C)(b)).** The step is the push-forward M_* of the previous full
measure, and the decomposition of unity is exact, so the full level-(k+1) measure (all small-field and large-field
pieces together) is the push-forward of the bare Wilson measure: it is the same for every frame. A frame changes only
(1) presentations (Gaussian references, coordinates, gauge devices), which are exact rewritings (Lemma A, Lemma AX, CA-I
4.35 (C)), and (2) the thresholds of the decomposition of unity, that is, which part of the one measure is booked as
all-small-field. So, at the same weights, **(FC) is a statement about moving mass across the small-field thresholds**:
on a small-field outer datum W, rho^(phi,small)(W) - rho^(psi,small)(W) = rho^(psi,large)(W) - rho^(phi,large)(W).

**4.5 What stays open: (FC-T), a two-threshold tail comparison (OPEN; GUIDE for the size).** (FC-1) of Step 3 holds with
summable nu_k if the totals log < pi_phi/pi_psi >_psi of (4.1), along the pin runs (phi = canonical scaffold,
psi = own weights), admit coherent localizations with |||.|||_(k+1) <= nu_k and sum_k nu_k bounded uniformly in n.
GUIDE: the two thresholds differ in relative size by |phi_k - psi_k|/(2 theta_k), at most of order
theta_k^(-1/2) polylog; a variable between them lies at a distance of order the threshold, (log theta_k)^(p_0) standard
deviations, from its Gaussian centre, so each local term should weigh about exp(-c theta_k delta(theta_k)^2) =
exp(-c A_1^2 (log theta_k)^(2 p_0)), which decays faster than any power of theta_k when 2 p_0 > 1 (the condition EM:873-876
already imposes). That is the size of the failure term of EM (eq-rs-formation). A proof needs the supplier's one-step
localization (Balaban's cluster expansion with the cut), applied to the ratio of two cuts; it is not in EM, RT or GI. If
the supplier's theorem is stated as "cut integral = cut-free analytic expansion + cut corrections of |||.||| at most
K exp(-c theta delta^2)", with the cut-free part depending on the kernel only through presentations that Lemma AX and
CA-I 4.35 (C) show to be exact, then (FC-T) follows with nu_k <= 2K exp(-c min(phi_k, psi_k) delta(min)^2) (ARGUED, not
checked against the supplier's text). Relation to the record: this is the one-step, outer-small-field instance of the
large-field rarity question that FINISH.md "State of our route" names as the most likely place for the route to fail; the
full-law form is not needed here, only the per-step suppression at a small-field outer datum.

## Step 5. Record check, labels, state after this row (written 2026-11-20T12:11Z by date -u)

**5.1 Record check (rule 0a).** Greps of `library/*.md`, `library/open-core.md`, `parts/*.md` and FINISH.md for "frame
independen", "Gaussian number", "soft gauge", "gauge weight", "site gauge", "4.35:prop-gauge-fixing", "decomposition(s) of
unity", "(FC)", "frame change", "frame comparison", "relative gauge normal", "one-loop data", "independent of the initial
weight". Matches and what they hold:
- Row 1256 (`gap-mini-solve-af-opus.md` L303-311) quotes the account's hypothesis (b) of `9.13:cor-coupling-shift`
  (x_k a function of (Lambda_n, x_0, k) only) and calls the two-frame comparison construction-level; not attacked there.
- Row 1260 (`gap-mini-solve-ai-opus.md`) named (FC) and split it (GUIDE) into a cut comparison and a partition matching.
- Rows 941-951 use the symbol (FC) for a different statement (a one-step Fisher-information contraction, row 941). Name
  collision only; this row's (FC) is row 1260's (G3).
- `b109.md`, `a3-balaban.md`, `b99*.md`, `descent*.md`: the hard core's readings of Balaban's gauge fixing (constraint
  straightening, axial bounds); none states the exact normalization of a soft axial weight against a cut (Lemma AX) or the
  frame independence of the Gaussian total (Lemma A). `port-map.md` has no port of CA-I 4.35 (C); `uses-old.md` L264 lists
  4.35 for its hypothesis (B) only.
- RT:725-727 takes "the actual one-loop data are independent of the initial weight" as an input; Lemma A proves the frame
  independence of the Gaussian total from GI's relative gauge theorem.
So Lemma A, Lemma Z, Proposition FC-chain, Proposition SPLIT and the reduction of (FC) to (FC-T) are new against the
record as far as these greps show. Lemma AX is new as a written proof; the fact for the axial device is the account's
stated reason in CA-I 4.35 (C)(b) ("the Faddeev-Popov Jacobian of the axial gauge on trees is 1"), so it is a rebuild of a
step the account cites, not a new fact.

**5.2 Labels.**

| Statement | Label | Rests on |
|---|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten) | OPEN; not proved, nothing disproved | |
| The infrared seed ((N-phys); (SL)/(RR) of row 1258) | OPEN; not attacked (0.3) | |
| 0.2: B's Corollary 166 (Bhattacharjee et al.) controls straight-path variables made near-Haar by ultraviolet noise, so it is blind | GUIDE (a reading, not a proof) | row 1218 |
| 1.3 (1.3a)-(1.3b): (FC) splits into the Gaussian-number difference plus the coefficient of a residual difference on the absolute core; separate bounds sum to order n^(1/2) | PROVED, elementary | EM:1191-1204, 1338-1390 |
| Lemma A: the Gaussian normalizer's background dependence, the totals of N_(k+1) and the Gaussian number b^0_(k+1) do not depend on the frame | PROVED given (A1) and GI's standing hypotheses | GI Theorem `gi:thm-relative-gauge`, GI:627-630, EM:694-700, 1202-1204 |
| Lemma Z: Gaussian mismatch and Gaussian-normalizer differences have zero vacuum-subtracted totals; counterterms differ by the residual coefficients only | PROVED | EM:1326-1335, Lemma A |
| 2.4: the unmarked chain reads no frame-dependent partition; row 1260's partition matching is not needed for (FC) | READ | EM:176-178, 364-380, 506-510, 524-536, 653-656 |
| Proposition FC-chain: (H1)-(H5) give sum_k eta_k <= 2 C_x sum_k nu_k | PROVED, an implication | (H3) ARGUED from EM input (4); (H2) cross-admission assumed |
| Corollary FC: with Lemma GR of row 1260, the scaffold comparison at the pins holds with bounded modulus if sum_k nu_k is bounded | PROVED GIVEN (H1)-(H5) along the pin runs | row 1260 Lemma GR, Lemma OFF' |
| 3.3: bounds through the account's envelopes alone give nu_k of order theta_k^(-1) (log theta_k)^(2 p_0), whose sum diverges like (log n)^(1 + 2 p_0) | PROVED, arithmetic (shows soft bounds cannot close (FC)) | EM:1365, III:69015-69017 |
| Lemma AX: a soft axial weight normalized by its own z is exact against gauge-invariant integrands; with a cut it acts through pi_w[chi] | PROVED, elementary | Haar invariance only |
| Proposition SPLIT (4.1): at fixed weights and list the frame enters only through the cut-pass probabilities, log < pi_phi/pi_psi >_psi | PROVED, an identity given the kernel form (K) | (K) from CA-I 4.35 (C)(b) (cited by the account from Balaban CMP 109, 119) and RT:533-579; READ, not checked against Balaban |
| 4.4: the full level-(k+1) measure is frame independent; a frame changes only presentations (exact) and the small-field thresholds | PROVED from CA-I 4.35 (C)(b) | account, cited part |
| (FC-T): the two-threshold tail comparison, |||log < pi_phi/pi_psi >_psi||| <= nu_k summable along the pin runs | OPEN; size GUIDE exp(-c A_1^2 (log theta_k)^(2 p_0)) | supplier's one-step localization (Balaban's cluster expansion with the cut) |

**5.3 The one-cutoff carry on the pin route after this row.** Row 1260 left (FC) as the input replacing (FI). After this
row: the Gaussian number, the Gaussian mismatch and normalizer families, the gauge weight (precision and truncation) and
the partitions are proved not to move the unmarked coefficient at fixed weights (Lemmas A, Z, AX, 2.4); the chain from
one-step to all levels is Proposition FC-chain. What (FC) still reads: (FC-T), a statement that moving the small-field
thresholds by a relative amount of order theta^(-1/2) polylog changes the all-small-field total by a summable, localized
amount; the bookkeeping hypotheses (H2) cross-admission and (H3) the total form of EM's input (4); the kernel form (K).
The other inputs of the carry are unchanged (row 1260 4.3): the base seed (OPEN, the infrared crux), the 9.1 hypothesis
(e) (OUTSTANDING in the account), (DET)'s inputs, (V9) at pins, the account's premises. Nothing here touches the T0 chain.

**5.4 What would change the plan.** If the supplier's one-step theorem (account chapter 4, Balaban CMP 109/116/119) is
found to state its failure term as a bound on cut corrections relative to a cut-free analytic expansion, (FC-T) follows
as in 4.5 and (FI) at pins leaves the input list (with (H2), (H3)). If instead the actual characteristic functions sit at
order-one thresholds for some variable (not in the Gaussian tail), (FC-T) fails as GUIDE'd and the pin route needs a
different matching (for example, row 1260 4.4: read the tuned family instead of first-passage data). A row that reads
CA-I chapter 4's decomposition of unity (thresholds, which variables, which units) decides between the two.

**5.5 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the complete account at
31a47c543775 (CA-I Proposition 4.35, cited by them from Balaban) and the component manuscripts YM4_EM, YM4_GI, YM4_RT at
c7fef8b21b58 (the two chains and their coefficient readout, the relative gauge normalizer, the action-gauge splitting,
the truncated Haar normalizer, the presentation matching on one frame). Tadeusz Balaban: the renormalization group and its
gauge fixing (CMP 99, 102, 109, 116, 119, 122 as the account cites them). The lane's rows 1233, 1255, 1256, 1260 for the
one-cutoff carry; row 1218 (gpt-6.1-sol) for the published-work reading; Bhattacharjee, Bhattacharya, Lockwood, Romanov
(B) for Corollary 166. Checked by no one; a cross-provider check of Lemma A, Proposition FC-chain, Lemma AX and
Proposition SPLIT is the natural next step.

No numeric run (none was needed). No subagent. Sources fetched by URL into a scratch folder outside the repository;
nothing fetched is committed.

