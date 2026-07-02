# Review history — block04 branch (fresh action lane; blocks 01-03 history on their stack)

## block04 — supervisor line-by-line review (2026-07-02, pre-PR)

1. **F1 (verified, notable).** Worker independently caught that the fully
   image-periodized Gaussian (wrapped normal) has EXACTLY Gaussian character
   coefficients — i.e. it coincides with the HK family on U(1) — and therefore
   correctly used the principal-angle finite-window Manton action as the T3
   witness, with the distinction disclosed in the boundary section. Physics
   subtlety handled honestly.
2. **F2 (verified).** Interval arithmetic: disjointness is exact
   Fraction-endpoint comparison (a.hi < b.lo or b.hi < a.lo); pi enclosed by a
   Machin-certified rational interval; Bessel/exp series carry explicit
   ratio-test remainder bounds. Displayed equal-looking endpoints are
   sub-display-precision widths; checks compare exact endpoints.
3. **F3 (verified).** Runner re-run independently by supervisor: PASS=14
   FAIL=0; output cache regenerated from supervisor run. Hostile-witness
   positivity bound checked by hand (1 - 2(1/10 + 1/10^4 + 1/100) = 3899/5000).
4. **F4 (supervisor addition).** Header consistency: added the standard
   "Claim type: bounded_theorem" and "Status authority" lines to match sibling
   note conventions.
5. **F5 (scope).** Both cited context notes (relocation; ADM2 bi-invariance)
   are unaudited and cited conditionally with that fact stated inline — no
   authority laundering. T5 is naming-only; no bridge asserted.

Disposition: **pass-with-supervisor-addition**.

## block09 — supervisor line-by-line review (2026-07-02, pre-PR)

1. **F1 (verified).** The Z_5 jump witness: symmetric-step generator on the
   cyclic subgroup; positivity structural (exp of nonnegative series);
   characters exp(-t(1-cos(2 pi n/5))) by exact Fourier diagonalization.
   Identity 4 psi(1) - psi(2) = 2(cos theta - 1)^2 hand-checked; exact
   cos(2 pi/5) = (sqrt 5 - 1)/4 used. Semigroup closure trivial in t.
2. **F2 (verified).** Self-adversarial framing is explicit in Purpose; block04
   three-candidate conclusion correctly preserved (Wilson/Manton are not
   semigroups; the witness lives outside the three).
3. **F3 (verified).** Q-gen named as the exact missing condition
   (psi(n) = s n^2; first-level check psi(2) = 4 psi(1) ≡ block04's c_2=c_1^4
   within the class). Next-attack naming only (single-step record structure
   supplying Q-gen) — no bridge claimed.
4. **F4 (verified).** No literature: witness constructed directly on Z_5;
   runner re-run independently 39/0 with certified tail bounds.

Disposition: **pass**.

## block10 — supervisor line-by-line review (2026-07-02, pre-PR)

1. **F1 (verified).** T3 ratio identity hand-checked: (1-cos(4pi/N))/(1-cos(2pi/N))
   = 4 cos^2(pi/N); deficit 4 sin^2(pi/N) > 0 for all finite N >= 3; limit
   behavior named honestly (deficit -> 0), not used as authority.
2. **F2 (verified, notable).** T2's finding exceeds the spec: full-step Q-gen
   matching on Z_N requires SIGNED weights for every tested N
   (5,7,8,9,12; e.g. N=5: w_2 = 1 - 3 sqrt(5)/5 < 0). Claim level correct:
   stated as a generator/linear-span obstruction ("not yet a positive-rate
   step semigroup"), no unproven semigroup-positivity (Metzler) step.
3. **F3 (verified).** T4 trichotomy horns exact; no horn selected; continuum
   flavor of horn (b) flagged conditionally via block04's quoted context.
4. **F4 (verified).** Runner re-run independently: 52/0.

Disposition: **pass**. Named for the queue: proving the Metzler-equivalence
step (generator-signed ⟺ kernel non-positivity at small t) would upgrade the
T2 obstruction from generator-level to semigroup-level — future block if the
action lane reopens.

## block13 — supervisor review: T1(⇒) remainder bound hand-checked (-t0(169/1000) + 2 t0^2 10^2 = -69/2000000 < 0 at t0 = 1/2000); T1(⇐) nonneg-series argument sound; N=5,7 witnesses explicit; wrapped-Gaussian deviations certified with tail bound 2e-95; all-N claims correctly avoided. Runner 37/0 re-run. Disposition: pass.
