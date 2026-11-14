lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T19:05Z

# gap-fctest-opus (FINISH row 946): GUIDE refutation test of (FC) for the vacuum slice chain

Status: in progress. Started 2026-11-14T07:05Z on Mac mini worker 2, at commit 77fc50935
(branch claude/ym4d-hard-route). Everything here is GUIDE unless marked otherwise: a run can
refute (FC) at a coupling, it cannot prove it. No statement of the chain rests on this file.

## Plan (at most eight steps; one per response)

1. Read row 941 (`library/gap-lsivac-max.md`) Steps 1, 5, 6: the exact definitions of the slice
   chain, P, nu, (A3), (FC), (GC), theta_GC, r_1; FINISH efficiency rules; grep open-core and
   FINISH rows for overlap. Record the definitions here verbatim with line references.
2. Write the estimator R(f) and the pass/fail criteria BEFORE any run (what counts as REFUTES,
   what counts as GUIDE-only, error and autocorrelation method).
3. Write code (lane946): SU(2) heat-bath + overrelaxation on a small periodic 4D lattice; frozen
   slice x; resampling of the rest; covariance estimator for grad P f via (A3).
4. Fact-check the code: (a) free photon / Gaussian chain, R = e^(-2 omega) per mode;
   (b) one-plaquette chain, theta_GC near r_1^2 as in row 941.
5. Run beta = 2.3 on the small lattice for the four observables (plaquette, smeared plaquette,
   odd function of (1/2) tr U_p, spatial Wilson line odd under the cut flip). About 45 min cap.
6. If time: beta = 2.6; exact one-cube chain (12 links, 6 plaquettes).
7. Report R(f) per f with error bars and integrated autocorrelation times; verdict per f.
8. RESULT line.

## Step log

(appended as each step completes)

### Step 1: objects, duplicate check, scope (READ; no new claim)

**Read at commit 77fc50935:** FINISH.md (opening, How we work, Joining, Working efficiently, Rules, rows 930,
936, 941, 943, 946-949), GOAL.md, `library/gap-lsivac-max.md` (row 941) Steps 0, 1, 5, 6 and Result,
`library/gap-oddgap-max.md` (row 930) notation and Lemma CUT (for the cut flip).

**Duplicate check (rule 0a).** `grep -i -E "\(FC\)|\(GC\)|fisher.information contract|slice chain"` on
`library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows naming (FC)/(GC):
941 (states it), 946 (this row, a GUIDE test), 947 (the proof attack on (FC), queued after this row). I do not
attack (FC) as a proof. I run only the refutation test that row 946 assigns.

**Sussman-Alpoge account.** `library/sa-index/` has no heat-bath or Monte Carlo text (grep "heat.bath|monte
carlo|kennedy.pendleton|overrelax": no hit). Their account enters this row only through the transfer frame
(outline (GL8), as located by checks 927, 933, 938; credit: Ethan Sussman and Levent Alpoge, with Claude and
Codex as authors of their text). The chain P, (A1)-(A3), (FC), (GC), Theorem C0 are row 941's (Claude Fable 5.2).

**Objects (row 941, Step 1 (A1)-(A3), Step 5.1, Step 6; quoted in short).**
- Spatial box B, periodic; slice space M = (S^3)^L, L = 3|B| spatial links; a link is a unit quaternion;
  <a, b> is the R^4 inner product, so (1/2) tr(a b^(-1)) = <a, b>. V(x) = -beta sum over spatial plaquettes of
  (1/2) tr x_p.
- (A1) T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2), temporal links set to 1. Omega its top eigenfunction
  (gauge invariant), lambda_0 its eigenvalue. Vacuum slice law nu = Omega^2 dx. One-step law
  pi_x(dw) = T_0(x, w) Omega(w) dw / (lambda_0 Omega(x)). P f(x) = E_(pi_x) f. P is self-adjoint on L^2(nu).
- (A3) For a tangent vector z at x: z . grad(P f)(x) = beta Cov_(pi_x)(<z, w>, f(w)). So
  grad_l (P f)(x) = beta Cov_(pi_x)(Proj_l w_l, f(w)), Proj_l v := v - <v, x_l> x_l (tangent space at x_l).
- grad is the Riemannian gradient of M with the metric induced from R^(4L); |grad f|^2 = sum over links.
- (GC)_theta: E_nu |grad P f|^2 <= theta E_nu |grad f|^2 for all smooth gauge-invariant f, theta < 1.
  (FC)_theta: E_nu[|grad P g|^2/P g] <= theta E_nu[|grad g|^2/g] for smooth positive g. (FC)_theta implies
  (GC)_theta (put g = 1 + eps f, second order in eps). So R(f) := E_nu|grad P f|^2 / E_nu|grad f|^2 >= 1 for
  one f refutes (GC) and hence (FC) on that box at that coupling.
- Row 941 GUIDE numbers to reproduce: one-plaquette SU(2) chain, theta_GC = 8.23e-4 (beta 2.3) and 1.15e-3
  (beta 2.6), r_1^2 = 8.02e-4 and 1.12e-3. One Gaussian mode: R = e^(-2 omega).
- Row 930 cut flip J: the centre flip (w -> -w) of the direction-1 links of one cut x_1 = const of a slice.
  J commutes with T_0 (each spatial plaquette meets a cut in 0 or 2 links). A gauge-invariant function is odd
  under J iff it crosses the cut an odd number of times: the spatial Wilson line winding once in direction 1.

**Scope of a verdict (fixed before any run).** The target box of rows 941 and 947 is the seed box (24a)^3 with
a about 20 or more at beta 2.3, side about 500 lattice units. This row runs boxes of side 4 and 6. So:
- a run with R(f) >= 1 beyond errors refutes (GC), hence (FC), **on the run's box at that coupling**;
- it is evidence (GUIDE) against (FC) on the seed box only if f is local (support small against the box) and
  R(f) does not fall when the box grows from 4 to 6;
- an f that winds around the box (centre-odd under J) probes SMALL-BOX physics (torelon / flux states, whose
  energy grows with the box in the confined phase). A winding-line R near or above 1 on side 4 says nothing
  about the seed box. It is reported as a SMALL-BOX probe, apart from the verdict.
