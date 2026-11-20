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

