# K1 pre-registration (written 2026-10-14 15:14Z, before any K1 script was run or any K1 web source was read)

Kill-round agent K1 (Claude Opus 5.5, same family as supervisor and route agents; not an independent referee).
Targets: X2 (combos/X2), F1-R1 walker branch (routes/F1), F6-tC anomaly gate (routes/F6).
Scripts: `scripts/` in this folder; one process at a time, OMP_NUM_THREADS=2, < 0.3 GB.

## Test A: mixed anomaly classes of the symmetries the mirror must keep

Content: walker H = sum_a sigma_a sin p_a on the site qubit, times an on-site 16 of Spin(10) (and, as control,
the 15 of G_SM without nu^c, with Z4^X). Light = hw1 corners; mirror = hw0 + hw2 + hw3.
Symmetries: lattice translations (emanant Z2^3 on corners), the 24 proper cubic rotations about a site with
SU(2) spin lift (emanant permutation action), fermion parity, Spin(10) (centre Z4 = Z4^X on the 16), G_SM.

**Hypothesis to be tested (my "absorption lemma", stated before running):** every Weyl fermion at corner c
transforms under the emanant group G_em as Ind_{Stab(c)}^{G_em}(chi_c (x) 16) with chi_c a scalar character of
the stabiliser. If every chi_c takes values in {+1, -1, +i, -i} (consistent with chi((-1)^F) = -1), then chi_c can
be absorbed into the centre Z4 of Spin(10) (or into Z4^X for G_SM), so the anomaly of every corner set is a
transfer of a pull-back of the anomaly alpha_16 of a single 16; it vanishes in every class (cyclic and mixed)
iff alpha_16 = 0.

- **A1 (exact, script `a1_emanant_reps.py`).** Construct the emanant action R_lat R_cont^{-1} of all 24 spin-lifted
  rotations and 8 corner translations on the 8 corner Weyl doublets of the walker. For each corner: is the
  stabiliser action a scalar on the Weyl doublet, and are its values in {+-1, +-i}?
  - PASS (lemma applies): all stabiliser characters scalar with values in {+-1, +-i}.
  - FAIL (lemma does not apply): any non-scalar action or any value outside {+-1, +-i}; then the offending
    cyclic classes are computed directly and reported as found.
- **A2 (literature gate).** A primary source states that one 16 of Spin(10) is free of all anomalies with
  Spin x_{Z2} Spin(10) structure (e.g. Omega_5 of that structure vanishes, or Dai-Freed freedom stated for it).
  - PASS: such a statement found and read (abstract/text). FAIL: not found, or a nonzero class for the 16 is
    stated; then the conclusion of A is conditional on alpha_16 = 0 (named).
- **A3 (explicit cross-check, same script).** For every element u of (emanant group) x (centre Z4) with
  u^2 = (-1)^F on fermions, the Z16 index nu_u = sum of left-handed charges, mod 16, on: light set, mirror set,
  every single corner, with d = 16. **Prediction:** all 0. **Control A4:** the 15 (no nu^c) with Z4^X must
  reproduce F6-tC's nonzero mirror value (3 mod 16) and C1's d = 1 obstructions; if the control fails the
  script is wrong and A3 is void.

**Kill readings for A (fixed now):**
- If A1 PASS and A2 PASS and A3 all 0 with A4 control passing: **the mixed-anomaly kill fails**: no anomaly of
  the listed symmetry group forbids symmetric gapping of the 5-corner mirror (or of the 3-corner light set).
  X2 / F1-R1 / F6-tC survive this test; F6-tC's named residual ("global bordism classes beyond Z16 and Witten")
  is closed for this group.
- If any class is nonzero for the mirror with d = 16: **X2 killed** (and F1-R1 walker branch), price = breaking
  that symmetry or adding content.
- If A1 FAIL: report the offending classes; verdict decided by their explicit values.
- Scope statement fixed now: a null result covers only the listed group (translations, proper rotations about
  a site, fermion parity, Spin(10) or G_SM x Z4^X). It says nothing about whether a gapped phase exists.

## Test B: does the Golterman-Petcher-Rivas intermediate SSB apply to X2's filtered quartic?

- **B0 (exact arithmetic).** Decompose the 10 of Spin(10) under G_SM. PASS for "SSB is fatal": the 10 contains
  no G_SM singlet, so any 10-vector condensate breaks G_SM at the lattice scale.
- **B1 (mean-field / large-N gap equation, script `b1_meanfield_10channel.py`).** Uniform 10-vector pairing
  condensate Phi coupling psi(k) psi(-k) with form factor f(k)^2 (both legs filtered), walker dispersion |h(k)| =
  |sin k|. Onset coupling g_c from 1/g_c = <f(k)^4 / |h(k)|>_BZ (common normalisation). Variants: X2 with f_F1,
  X2 with f_NN, and the unfiltered control f = 1 (EP-like channel on the walker); also the light-sector check
  (f = 0 at hw1 keeps the light massless in the broken phase).
  - Reading "GPR channel survives the filter": g_c(X2) finite and g_c(X2)/g_c(control) < 3 (same order).
  - Reading "filter suppresses the channel": g_c(X2)/g_c(control) > 10.
  - In between: "partially suppressed", reported as such.
  - Fixed scope: mean field always predicts SSB above g_c and cannot produce a symmetric gapped phase, so B1
    can only show whether the SSB instability is present at a comparable coupling; it cannot decide whether a
    symmetric strong-coupling phase pre-empts it.
- **B2 (strong-coupling structure, same script).** Overlap kernel K(r) = {psi_S(x), psi_S(x+r)^dag} for each
  filter. Reading: if max_{r != 0} |K(r)| / K(0) >= 0.2, the W -> infinity limit is not atomic (the hopping
  expansion that produced GPR's strong-coupling symmetric phase has no small parameter in X2); recorded as a
  structural difference, not as evidence for or against a symmetric phase.
- **B-literature.** Read GPR's abstract/text for method (mean field / large N / strong coupling) and the current
  4D lattice evidence on whether an intermediate bilinear-condensate phase appears in 4D SMG models.

**Kill readings for B (fixed now):**
- "GPR applies (X2 wounded)" if B0 PASS and B1 "channel survives": X2's filtered quartic carries the same
  leading mean-field instability as EP, any condensate breaks G_SM, and the decisive many-body test must show
  its absence; the filter does not remove the objection.
- "GPR defused" only if B1 shows strong suppression AND B2 shows an atomic strong-coupling limit; otherwise
  not defused.
- "X2 dead by GPR" requires a non-mean-field demonstration of SSB in X2's model (not available in this budget);
  mean field alone never kills.

## Dated follow-ups (added after A1-A4 ran, 2026-10-14 15:18Z by `date -u`; the readings above are unchanged)

- **A5 (illustration of a framing point, not a kill test; added before running it).** Two Majorana chains,
  H = sum_j i(chi1_j chi1_{j+1} + chi2_j chi2_{j+1}) + i m sum_j chi1_j chi2_j (translation-invariant, on-site,
  fermion parity kept). The emanant Z2 (translation acting as (-1)^{F_L}) carries nu = 2 mod 8 in the IR.
  Prediction: single-particle gap opens for |m| > 2 (nodes leave the corners and annihilate at k = -pi/2), so an
  emanant-only anomaly does not by itself forbid lattice-scale symmetric gapping; only its pull-back to the UV
  group (lattice translations Z) does. PASS of the illustration: gap = |m| - 2 for |m| > 2, 0 for |m| <= 2.
- **B3 (B-script extension, added before running B).** Filter non-orthogonality bound: for each filter report
  sqrt(sum_{r != 0} |K(r)|^2) / K(0) = sqrt(<f^4> - <f^2>^2) / <f^2> (exact Parseval), same 0.2 threshold as B2.
- **B4 (added ~15:19Z, after B1 ran, in the same shell command just before B4 ran; header time corrected from a mistyped 15:20Z).** B1 only tested a uniform (Q = 0) condensate.
  The 2026 4D lattice study (Butt-Catterall-Hartshaw-Hasenfratz, arXiv:2608.18239) reports an intermediate
  *anti-ferromagnetic* phase, so test staggered 10-vector pairing too: condensate at corner momentum Q pairs
  psi(k) with psi(Q - k), form factor f(k) f(Q - k), spin structure i sigma_y, full BdG coherence factors.
  Mean-field susceptibility chi(Q) = -d^2 E_0 / d Delta^2 at 0 (finite difference), all 8 corners Q, for the
  control and both X2 filters; normalised to chi_control(0).
  - Reading: "staggered channel leads" if argmax_Q chi_X2(Q) != 0; "channel survives at Q" if
    chi_X2(Q) / chi_control(0) >= 1/3 for some Q; "strongly suppressed" only if chi_X2(Q)/chi_control(0) < 0.1
    for every Q. Consistency: chi(0) ratios must match B1's I[f] ratios to 2%.
- **C1 (added ~15:21Z, just before running; header time corrected from a mistyped 15:23Z).** Independent recheck of X2-L3 (F1:108 selection rule false for
  the walker 3-light split): enumerate corner labels; PASS for X2-L3 if some light*mirror^3 and some
  light^3*mirror label sum is 0 for light = hw1, mirror = hw0+hw2+hw3; FAIL if none.
