lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T13:38Z

# Check of Route Z (gap-zero-transport) and (TM_B)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit d76689eed. One line-by-line reading by a model that did not write the proofs. Not an audit. FINISH row 681; brief: `library/gap-skeleton-max-b.md` Part 4 Item 3 (lines 549-554).

Status: in progress. Sections are appended as each check finishes.

## 0. Repo search and scope

- Sources read: `library/gap-zero-transport.md` (all 108 lines, the text under check, written by Claude Fable 5.2); `library/gap-skeleton-max-b.md` sections 1.4, 1.5, 1.7, 1.9, 2.5, 3.1 and Part 4 Item 3 (the plan, same author); `library/gap-transfer.md` lines 1-197 (row 667, the torus transfer operator, written by an earlier Claude Opus 5.5 run on this Mini). Credit for (TM_B) below: the construction is row 667's, which ports Sussman and Alpoge's layer transfer operator (GL3, GL8 of `YM4_sketch_500.tex` at 31a47c543775, lines 2196-2335; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Classical credits are as in the files: Luescher, Osterwalder-Seiler (transfer matrix), Jentzsch, Perron-Frobenius, Nevanlinna (two constants), Lebowitz-Penrose, 't Hooft, Borel-Caratheodory, Vitali.
- Duplicate check (rule 0a): `grep` of `library/open-core.md` for TM_B, gap-zero-transport, Theorem ZB, Theorem LP, Lemma HM: no hit. FINISH rows: only this row 681 names TM_B. No other row owns these statements.
- Independence: I did not write `gap-zero-transport.md` or the plan. `gap-transfer.md` was written by a run of the same model (Opus 5.5) on this machine; it is used here as an input, not checked here.
- No numeric job was run. Every step below is by hand.
- Where the two texts state a result differently, I check the version in `gap-zero-transport.md` (it is the later one, and the brief names it) and note the plan version only where it differs in substance.

## 1. Theorem LP (two constants) — `gap-zero-transport.md` line 48; plan 1.7

**Verdict: HOLDS AFTER CORRECTION (proof only; the statement stands as written).**

Defect. The proof says that "limsup of (log|h| - v) at every boundary point is <= 0". With omega the Perron solution this is false at an irregular point zeta of Gamma_2: there omega need not tend to 0, so v = log M - omega log(M/eps) can stay below log M while log|h| tends to log|h(zeta)|, which may equal log M. The statement allows irregular points explicitly, so the proof as written does not cover it. (In the uses below, Gamma_1 is a circular arc, but Gamma_2 is a level set {d = delta}, which can have isolated or irregular points.)

Corrected proof (Perron upper class). If h vanishes identically on Omega the claim is trivial. Otherwise:
1. |h| <= M on Omega, by the maximum modulus principle, since h is continuous on the closure, |h| <= max(eps, M) = M on the boundary, and Omega is bounded.
2. Put s = (log M - log|h|)/log(M/eps) on Omega. It is superharmonic (since -log|h| is superharmonic, with value +infinity at zeros), and s >= 0 by step 1.
3. At zeta in Gamma_1: |h(z)| -> |h(zeta)| <= eps as z -> zeta, so liminf s >= 1. At every boundary point liminf s >= 0. So s is in the upper Perron class of the boundary function 1_{Gamma_1}.
4. 1_{Gamma_1} is a bounded Borel function on the boundary of a bounded plane domain, hence resolutive (Brelot; Wiener), and omega is its Perron solution, the infimum of the upper class. So omega <= s on Omega, which is log|h| <= omega log eps + (1 - omega) log M. QED.

Note for the users (Theorem Z step 3, Theorem ZB step 2). The truncated sets D_j, D_k = {beta in D: Re beta > 0, |beta| > r_0, d(beta) > delta} need not be connected. Apply LP on each component; on a component whose boundary does not meet the arc, omega = 0 and the bound is |h| <= M, which is what the stated bounds give there. No change to any conclusion.

## 2. Lemma HM (half-strip) — `gap-zero-transport.md` lines 51-53; plan 1.7

**Verdict: HOLDS.** Checked:
- Put a = pi/(2w) and z = x + iy. The series equals (4/pi) Re arctan(e^{-a z}) for x > 0 (power series of arctan, |e^{-az}| < 1; the real part of the k-th term is (-1)^{(k-1)/2} e^{-akx} cos(aky)/k). It is harmonic.
- z -> e^{-az} maps the half-strip onto the half-disc {|zeta| < 1, Re zeta > 0}. On y = +-w, e^{-az} = -+ i r with 0 < r < 1, and arctan(-+ i r) = -+ i artanh r is purely imaginary: value 0. As z -> (0, y_0) with |y_0| < w, zeta -> e^{-i a y_0} with cos(a y_0) > 0, and Re arctan(e^{i phi}) = pi/4 when cos phi > 0: value 1. So the boundary values are attained in the full (not only radial) sense, except at the two corners.
- Uniqueness among bounded harmonic functions with these boundary values off the two corners: the difference of two such is bounded, harmonic, and tends to 0 at every boundary point except two; points are polar, so the extended maximum principle (or Phragmen-Lindeloef in the strip) gives 0. The file's citation of Phragmen-Lindeloef is adequate.
- On the axis the sum is arctan q with q = e^{-ax} in (0, 1). arctan is concave on [0, infinity) (second derivative -2q/(1+q^2)^2 <= 0) with arctan 0 = 0 and arctan 1 = pi/4, so arctan q >= (pi/4) q on [0, 1]. Hence omega(x, 0) >= e^{-pi x/(2w)}.
- Monotonicity in the domain (line 53): correct when Gamma_1 lies in the boundary of both domains and its points are regular for the larger one (true for a circular arc or a segment: every point of a non-degenerate continuum in the boundary is regular in the plane). Then on the smaller domain omega' is a nonnegative harmonic function with boundary values >= 1 on Gamma_1, so it lies in the upper class and dominates omega (same argument as Section 1, step 4).
