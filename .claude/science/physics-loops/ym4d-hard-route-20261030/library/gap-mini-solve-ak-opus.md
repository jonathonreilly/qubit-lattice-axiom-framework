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

