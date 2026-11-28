# Check of `gap-loop-pos-astra.md` (Codex gpt-6-astra max, FINISH row 760)

- Checker: Claude Opus 5.5 (one session, alone). Date: 2026-11-12.
- The checked note is by Codex (other provider). The
  inputs `gap-loop-eq-opus.md` and `gap-seed-sc-check.md` are Claude Opus 5.5
  work, so where this check leans on them it is not independent of them.
- Read in full: `library/gap-loop-pos-astra.md` lines 1–620 (Sections 1–5).
- Read for inputs: `gap-loop-eq-opus.md` Section 1 (lines 35–69) and
  Section 5 (lines 143–188); `gap-loop-eq-check.md` verdict table and
  Sections 1, 3, 4 (lines 39–150, 232–390); `gap-skeleton-final.md`
  13.18–13.19 (lines 604–628); `gap-crux-fp.md` 3b.3 (lines 270–288);
  `gap-seed-sc.md` Section 1 (lines 28–62) and Section 4 (lines 156–200);
  `gap-seed-sc-check.md` Theorem 2 verdict (lines 84–116).
- Not read: `gap-es1-opus.md` (Theorem V). The sentence about Theorem V in
  Section 1 is not checked.
- Method: by hand. One GUIDE script (pure Python, `python3 -I`, < 50 MB):
  `guide_star.py` in this folder (one link, six Haar staples, conditional
  law exp(s h)). It decides nothing.

## Verdict table

| # | Statement (lines) | Verdict |
|---|---|---|
| 1 | Hat normalization, cancellation of 6s\|B\| (66–69) | HOLDS |
| 2 | delta = 48a^4 ∫(w_a − w_2a) ds (77–80) | HOLDS |
| 3 | log(1+eps) = 6a^4 ∫(w_ev^ins − w_a) ds (77–80) | HOLDS |
| 4 | Integrals ≥ 0, no pointwise sign, tolerances 10^-7 and log(1+10^-7) (82–84) | HOLDS (tolerance source: loop-eq-opus 5.1, loop-eq-check §3; 13.18–13.19 do not print it) |
| 5 | Theorem V sentence (84–85) | NOT CHECKED (source not read) |
| 6 | (2.1), 0 ≤ u ≤ 36, \|h\| ≤ 6, v ≥ 0 (91–106) | HOLDS |
| 7 | m = E h_e = 6 w̄, no time–space exchange (114–119) | HOLDS |
| 8 | (2.3); loop lengths 6, 12, 24 (121–134) | HOLDS |
| 9 | a ≥ 7 embedding; 24/a < 1 iff a ≥ 25 (136–139) | HOLDS (a ≥ 7 is sufficient, = 2r+3 at r = 2) |
| 10 | Twist: B_i → sigma_i B_i, m = 6 w_ev^ins (141–146) | HOLDS |
| 11 | (2.6) Δh = −3h, Γ(h,h) = v, d_j u = 0 | HOLDS |
| 12 | (2.7) | HOLDS |
| 13 | (2.8) | HOLDS |
| 14 | (2.9) with F = 1, h, v, hv, v^2, uh, uv | HOLDS |
| 15 | (2.10) and the closed form of U_s; m ≥ 0, m ≤ 6, m(0) = 0 | HOLDS |
| 16 | The three nonzero entries of L_s; (2.11); (2.12) | HOLDS |
| 17 | Local sum-of-squares origin of every positivity used | HOLDS |
| 18 | Theorem P, (2.5), all s ≥ 0 | HOLDS |
| 19 | Corollary P-shift (2.13), factors 8a^4 and a^4 | HOLDS |
| 20 | (P-small) right sides 10^-7/(8a^4), log(1+10^-7)/a^4 | HOLDS (arithmetic) |
| 21 | "P-small at order-one coupling: OPEN" (310, 576, 594, 604–611) | FAILS as a live target: P-small is false for β above about 0.03/a (exact reduction PROVED below; one continuity input ARGUED) |
| 22 | K_r(s), "same result when constraints are omitted", class (3.1) | HOLDS |
| 23 | Wilson witnesses on n^4, (2n)^4, n = 2r+4, lie in K_r(s); (3.3) | HOLDS |
| 24 | (3.4)–(3.6) | HOLDS (given Theorem 2 of gap-seed-sc, checked there by Claude Opus 5.5) |
| 25 | Real analyticity; J_r(I) > 0 on every interval incl. [1,2]; (3.2) | HOLDS |
| 26 | (3.8) | HOLDS |
| 27 | Corollary O-seed (3.9), (3.10) | HOLDS |
| 28 | Quantifiers and listed exclusions (496–509) | HOLDS (remark: signed cancellation alone is a narrower escape than it reads) |
| 29 | U(1): Δh = −h, Γ = u − h^2, (4.1), m = sA_1, 2A_1 + s^2A_2/3 = M | HOLDS |
| 30 | s = 0 hand check (4.2); unmodified U_s fails for U(1) | HOLDS |
| 31 | Link to T1–T3 (554); compatibility; ARGUED assessment; OPEN list | HOLDS |
| 32 | Section 5 table and RESULT line | HOLDS AFTER CORRECTION (row of item 21) |

## 1. Section 1

**Item 1 — HOLDS.** With Ẑ = ∫exp(sΣx_p) and the imported
Z = ∫exp(−sΣ(1−x_p)), Ẑ = e^{6st|B|}Z, so ê = e + 6s|B|. In
delta = a(8e(a^3) − e((2a)^3)) the added terms are a(8·6s a^3 − 6s·8a^3) = 0;
in log(1+eps) = log Z_0 − a e(a^3) they are 6s a^4 − a·6s a^3 = 0.
Credit: the author, after `gap-loop-eq-check.md` §3 first correction.

**Item 2 — HOLDS.** ê'(B) = 6|B| w̄ (Lemma 5.1 as corrected in the check).
delta' = a(8·6a^3 w_a − 6·8a^3 w_2a) = 48a^4(w_a − w_2a), and delta(0) = 0.
Sign of the integrand as printed. Matches check (3.2).

**Item 3 — HOLDS.** d/ds log Ẑ_0 = 6a^4 w_ev^ins (check (3.1), the signed
insertion), and a·ê'(a^3) = 6a^4 w_a; Ẑ_0(0) = 1 with the 1/8. Coefficient 6a^4.

**Item 4 — HOLDS.** delta ≥ 0 (Lemma K) and eps ≥ 0 give nonnegative
integrals; the note asserts no pointwise sign, as the check requires. The
tolerances are for delta and log(1+eps) themselves; the integral tolerances
(P-small) divide by 8a^4 and a^4 after the factor 6 is moved into m = 6w̄.
The value 10^-7 is the one used in `gap-loop-eq-opus.md` 5.1 and
`gap-loop-eq-check.md` §3; 13.18–13.19 name (ES) but do not print it.

## 2. Section 2

**Item 6 — HOLDS.** In quaternion coordinates each B_i is a unit vector of
R^4, H = ΣB_i, u = \|H\|^2 ≤ 36, h = Re(U_e H) = ⟨U_e^*, H⟩ so
\|h\| ≤ \|H\| ≤ 6 and h^2 ≤ u. Each of the 2(d−1) = 6 plaquettes at e is read
with e first, which fixes B_i; trace-inversion invariance makes x_p
orientation-free. Credit: the author.

**Item 7 — HOLDS.** Σ_e h_e = 4Σ_p x_p (each plaquette has four links);
#links = 4\|Λ\|, #plaquettes = 6\|Λ\|; so the uniform link average of h_e is
6 × (uniform plaquette mean) = 6w̄, the same orientation-averaged w̄ as
Lemma 5.1. No axis exchange used.

**Item 8 — HOLDS.** u = Σ_{i,j}½tr(B_iB_j^*) = 6 + 2Σ_{i<j}W(B_iB_j^{-1}),
loops of length 6. All B_i run between the same two vertices, so all loops
B_iB_j^{-1} share a base point and 2W(A)W(B) = W(AB) + W(AB^{-1}) (the
SU(2) trace identity in half-trace units) applies: u^2 → length 12. Note:
v = u − h^2 contains h^2, whose terms are single traces of length 8
(W(U_eB_iU_eB_j) and W(B_iB_j^{-1})). So A_1 needs length 8, v^3 needs
24 = 3·8, uv^2 needs 22. The ceiling 24 holds as stated; "M needs ≤ 6, N ≤ 12"
holds.

**Item 9 — HOLDS.** The star occupies a 2×3×3×3 vertex block; it embeds
without identification already for sides ≥ 3; a ≥ 7 = 2r+3 at r = 2 is the
VB margin and is sufficient. 24/a < 1 iff a ≥ 25. Correct.

**Item 10 — HOLDS.** In twisted measure k the one-link weight is
exp(s½tr(U_eΣσ_iB_i)), so H^k = Σσ_iB_i; σ_iB_i is again Haar at s = 0.
The q_k(s) = Ẑ^k/ΣẐ^e are positive, so the mixture is a probability
measure on (k, U): Ward identities pass by linearity and Jensen/positivity
pass. The link average of Σ_iσ_i x_{p_i} is 6·w_ev^ins of check (3.1).

**Items 11–12 — HOLD.** On S^3 ⊂ R^4 the fields d_j: U ↦ iσ_jU are an
orthonormal left-invariant frame, so Σd_j^2 is the round Laplacian and a
linear function satisfies Δh = −3h; Γ(h,h) = \|grad_tan h\|^2 = \|H\|^2 − h^2.
d_j is divergence-free for Haar, so E[d_j g + s g d_j h] = 0; with
g = F d_j h, summed: E[v∂_hF + ∂_uF·Γ(u,h) + FΔh + svF] = E[v∂_hF − 3hF + svF] = 0.
Credit: the author, with `gap-loop-eq-check.md` §1.

**Item 13 — HOLDS.** F = v^k: ∂_hF = −2khv^{k−1} gives
−(2k+3)E(hv^k) + sEv^{k+1} = 0. F = hv^k: v∂_hF = v^{k+1} − 2kh^2v^k; adding
−3h^2v^k and h^2 = u − v gives (2k+4)Ev^{k+1} − (2k+3)E(uv^k) + sE(hv^{k+1}) = 0.

**Item 14 — HOLDS.** F=1: 3m = sA_1. F=h: 4A_1 + sE(hv) = 3M; F=v:
5E(hv) = sA_2; so 4A_1 + s^2A_2/5 = 3M. F=hv: 6A_2 + sE(hv^2) = 5B_1;
F=v^2: 7E(hv^2) = sA_3. F=uh, uv: u is U_e-independent, so these are the
k=0 identities times u: 4B_1 + sE(uhv) = 3N and 5E(uhv) = sB_2.

**Item 15 — HOLDS.** For s > 0, A_1 = 3m/s and A_2 ≥ A_1^2 give
3M ≥ 12m/s + 9m^2/5, i.e. 3sm^2 + 20m ≤ 5sM. The positive root
(−20 + √(400+60s^2M))/(6s), rationalized, is 10sM/(20 + √(400+60s^2M)).
m ≥ 0 from A_1 ≥ 0; m ≤ 6 from \|h\| ≤ 6; s = 0 gives m = 0.

**Item 16 — HOLDS.** (6−h)v ≥ 0 gives E(hv) ≤ 6A_1, so 3M ≤ (4+6s)A_1 and
m = sA_1/3 ≥ sM/(4+6s). A_3 ≥ 0 gives A_2 ≤ 5B_1/6; (36−u)v ≥ 0 gives
B_1 ≤ 36A_1, so A_2 ≤ 30A_1, and 3M ≤ (4+6s^2)A_1 gives the second entry.
B_2 ≥ 0 gives B_1 ≤ 3N/4, so A_2 ≤ 5N/8. (2.12): m = (s/3)(3M − s^2A_2/5)/4
= sM/4 − s^3A_2/60; with A_2 ≤ 5N/8, m ≥ sM/4 − s^3N/96.

**Item 17 — HOLDS.** v = Σ(d_jh)^2; Lagrange: 6Σ\|B_i\|^2 − \|ΣB_i\|^2 =
Σ_{i<j}\|B_i − B_j\|^2 = 36 − u; \|U_eB_i − 1\|^2 = 2 − 2x_{p_i}, so
½Σ\|U_eB_i − 1\|^2 = 6 − h. Products of sums of squares are sums of squares.

**Items 18–19 — HOLD.** Theorem P follows. P-shift:
delta = 8a^4∫(6w_a − 6w_2a) ≤ 8a^4∫[U_s(M_A) − L_s(M_B,N_B)];
log(1+eps) = a^4∫(6w_ev^ins − 6w_a) ≤ a^4∫[U_s(M_E) − L_s(M_A,N_A)].
Cylinder moments: the finite-time limits exist for local functions on a
fixed spatial box (simple top eigenvalue of T), and finitely many linear
identities and inequalities pass to the limit.

Small-s sanity check (by hand): at s = 0, M = 6, N = 36 + 4·15·¼ = 51,
E v = ¾·6 = 4.5, E v^2 = (5/8)·51 = 31.875 (c = ⟨U, Ĥ⟩ is independent of H
with Ec^2 = ¼, Ec^4 = 1/8). Then U_s = sM/4 − 3s^3M^2/320 + O(s^5) and the
last entry of L is sM/4 − s^3N/96; both bounds are exact at first order,
and L's s^3 term is exact at s = 0 since A_2 = 5N/8 there. GUIDE
(`guide_star.py`, 2×10^5 samples): Haar values M = 6.00, N = 51.0,
A_1 = 4.49; L ≤ m ≤ U at s = 0.3, 1, 2, 4.

**Item 20 — HOLDS.** 10^-7/(8a^4) and log(1+10^-7)/a^4 are the P-shift
factors applied to the tolerances.

### Item 21 — P-small is not a live target (new; FAILS as stated "OPEN")

**Lemma (PROVED here).** In any state where Theorem P applies and U_s < 6,

  U_s(M) − m = s^3 Var(v) / (3(20 + 3s(U_s + m))) ≥ s^3 Var(v)/(60 + 108 s).

Proof. From (2.9), 12m/s + s^2A_2/5 = 3M with A_2 = A_1^2 + Var(v) and
A_1 = 3m/s: 3sm^2 + 20m = 5sM − s^3Var(v)/3. Subtract from
3sU^2 + 20U = 5sM: (U − m)(3s(U+m) + 20) = s^3Var(v)/3. Use U, m ≤ 6. QED
(GUIDE agrees: at s = 1, 2, 4 the script gives U − m = 0.120, 0.444, 0.907
against 0.124, 0.442, 0.864 from the formula.)

**Reduction (PROVED here).** Pointwise U_s(M_A) ≥ m_A and m_B ≥ L_s(M_B,N_B),
and ∫(m_A − m_B) = δ/(8a^4) ≥ 0. Hence

  ∫_0^β[U_s(M_A) − L_s(M_B,N_B)] ds ≥ ∫_0^β s^3 Var_A(v)/(60 + 108 s) ds,

which is nondecreasing in β. The same holds for the second line with state E
(at s = 0 every twisted measure is Haar, so Var_E(v) = 93/8 too).

**Consequence (ARGUED at one step).** At s = 0, Var(v) = 31.875 − 4.5^2 =
93/8 = 11.625. If Var_s(v) ≥ 5 on [0, 0.05], uniformly in the side (a local
expectation, continuous at s = 0 uniformly in volume under the convergent
strong-coupling expansion — this uniformity is the ARGUED step), then for
s ≤ 1/9 the integrand is ≥ 5s^3/72 and the left side is ≥ 5β^4/288. The first
P-small then fails for every β > (7.2×10^-7)^{1/4}/a ≈ 0.029/a, and the second
for every β > (5.8×10^-6)^{1/4}/a ≈ 0.049/a. For a = 7 that is
β > 0.0042 and β > 0.0070.

So the Theorem P certificate can reach the ES tolerance only for β of order
10^-2/a, inside the range β < 1/18 already covered by Theorem DOB. The note
correctly does not assert P-small; but "P-small at order-one coupling: OPEN",
"prove P-small for some specified a and coupling regime" (576) and "the next
decision is to fix that size and patch, then seek a hand certificate for the
displayed integrated tolerance" (610–611) should be corrected: P-small is
false at order-one coupling for every a ≥ 7 (given the ARGUED uniformity). Any
successor certificate must control the variance term exactly; the gap
Var(v) > 0 is the Jensen gap the certificate keeps (A_2 ≥ A_1^2 is the only
place the upper bound uses positivity). This sharpens the author's own
"bound is not asserted to reach either seed tolerance" (307–308) into a
negative statement specific to Theorem P, independent of Theorem O.

## 3. Section 3

**Item 22 — HOLDS.** Omitting constraints enlarges K_r(s); the witnesses
stay inside, so the lower bound survives. (3.1) quantifies over all pairs of
K_r(s), with b_a allowed to depend on a: this is exactly the VB conclusion as
corrected in `gap-loop-eq-check.md` §4.

**Item 23 — HOLDS.** n = 2r+4 ≥ 2r+3, so the patch and stencils embed in
n^4 and (2n)^4. Ward: Haar integration by parts in the actual measure.
Positivity and localizing inequalities: an actual probability measure.
Symmetries: the symmetric tori have all hypercubic symmetries, which contain
those shared by the targets. Temporal RP: with T ≥ 0 self-adjoint,
Tr(A^*T^vAT^u) = Tr((T^{v/2}AT^{u/2})^*(T^{v/2}AT^{u/2})) = ‖T^{v/2}AT^{u/2}‖_HS^2 ≥ 0;
the half-torus has length r+2 > r, so the reflected support stays off the
antipodal cut. Credit: the author, after check §4.

**Item 24 — HOLDS.** Translation invariance and orientation averaging give
p(ω_n) = torus mean plaquette, so d/ds log Ẑ_n = 6n^4 p_n and
d/ds log Ẑ_2n = 96n^4 p_2n; Φ_n' = 96n^4 f_n. log Ẑ_n = log Z_n + 6sn^4, and
16·6sn^4 − 6s·16n^4 = 0, so Φ_n is the seed-sc Φ(n; s). Theorem 2 (n ≥ 5;
here n ≥ 8): Φ_n = 192n^3 4^{-4n}s^{4n} + O(s^{4n+1}), so
f_n = 192n^3·4n·4^{-4n}s^{4n−1}/(96n^4) = 8·4^{-4n}s^{4n−1} + O(s^{4n}).
Theorem 2 is marked HOLDS in `gap-seed-sc-check.md` (Claude Opus 5.5, same
provider as the seed-sc author); I read its proof (Lemmas 4.1–4.3,
Proposition 4.4) and found no defect, but did not recount it.

**Item 25 — HOLDS.** Ẑ_n is entire (bounded action on a compact space),
positive on the real axis, so log Ẑ_n and f_n are real analytic on R. f_n is
not identically zero, so its zeros are isolated and ∫_I\|f_n\| > 0 for every
nondegenerate I, including [1,2]. Both orders in (3.1) give
b_a(s) ≥ \|f_n(s)\|. J_r(I) depends on r (through n) and I only.

**Item 26 — HOLDS.** For 0 < s ≤ η_n, f_n ≥ 4·4^{-4n}s^{4n−1}; integrating to
t = min(β, η_n) gives 4·4^{-4n}t^{4n}/(4n) = (1/n)(t/4)^{4n}.

**Item 27 — HOLDS.** delta ≤ 48a^4∫b_a and the estimate is ≥ 48a^4 J;
48a^4J > τ iff a > (τ/(48J))^{1/4}. Likewise 6a^4J > log(1+τ). The condition
a ≥ 2r+3 makes the targets members of K_r, so the method applies at all.

**Item 28 — HOLDS, with a remark.** The quantifier "fixed r and β, all large a"
is what is proved; J_r is not uniform in r (the bound (3.8) decays like
(β/4)^{8r}), so r = r(a) is not excluded, and no r ≈ a/2 is implied.
Winding constraints, joint relations and global-state information are not in
K_r and are outside (3.1). Remark on signed cancellations: Theorem O indeed
does not cover them. But a certificate that bounds ∫_0^β(p(ω_s) − p(ν_s)) ds
over every s-family whose premises the witness families (ω_n(s), ω_2n(s))
also satisfy must still exceed ∫_0^β f_n = Φ_n(β)/(96n^4), which is
nonzero except at isolated β (real analyticity) and positive at small β
(Theorem 2). So the escape is information that the witness families violate,
not cancellation as such. This does not change any statement of the note.

## 4. Section 4

**Item 29 — HOLDS.** U(1): h = Re(e^{iθ}H), d²/dθ² gives Δh = −h,
(dh/dθ)^2 = \|H\|^2 − h^2. The analogue of (2.7) is E{v∂_hF − hF + svF} = 0;
F = v^k gives (2k+1)E(hv^k) = sEv^{k+1}; F = hv^k gives
(2k+2)Ev^{k+1} − (2k+1)E(uv^k) + sE(hv^{k+1}) = 0. Hence m = sA_1 and, with
3E(hv) = sA_2, 2A_1 + s^2A_2/3 = M. The cosine product identity is the same
as the SU(2) trace identity, so only the Casimir distinguishes. Coefficient
−h, not −3h: correct, consistent with `gap-loop-eq-opus.md` lines 63–67.

**Item 30 — HOLDS.** At s = 0, distinct plaquette cosines are uncorrelated
(integrate a link of one plaquette only), so d/ds E h at 0 = 6E cos^2 = 3;
M(0) = 6 since each cos(φ_i − φ_j) has mean 0. Cross-check with (4.1):
A_1(0) = 6 − 3 = 3, m = sA_1 ≈ 3s. The SU(2) bound gives U_s ≈ sM/4 = 1.5s
< 3s for small s > 0: Theorem P's upper bound is false for U(1). The step that
fails is Δh = −3h.

**Item 31 — HOLDS.** By T1/T3 of `gap-crux-fp.md` 3b.3 (lines 270–288) the
valid test asks whether the tool's hypothesis holds in the comparison model;
here it does not (the inequality (2.5) is violated by U(1)), so the tool is
not blind to SU(2)/U(1) and the test does not refute it. Theorem O's
argument is model-agnostic, as the note says; it claims no gap. The ARGUED
assessment and the OPEN list are accurate, except for the P-small item (21).

## 5. Section 5

**Item 32 — HOLDS AFTER CORRECTION.** Every PROVED mark checks, except that
the row "P-small at order-one coupling … OPEN" should read: P-small is
false for β above about 0.03/a (exact reduction PROVED; uniform continuity
of Var_s(v) near s = 0 ARGUED), so Theorem P cannot give (ES) beyond the
range of Theorem DOB. The final "next decision" for this certificate should
be dropped; a successor must control the Jensen gap Var(v) along the path.

RESULT: Sections 1–4 of gap-loop-pos-astra.md check line by line (Codex gpt-6-astra max as author): the two shift formulas with 48a^4 and 6a^4, Theorem P (all seven Ward tests, both bounds), P-shift with 8a^4 and a^4, Theorem O with its witnesses, J > 0 on every interval, O-seed and its quantifiers, and the U(1) coefficients −h and the s = 0 failure all HOLD; one correction: U_s(M) − m = s^3 Var(v)/(3(20+3s(U+m))) exactly, so P-small is false above β ≈ 0.03/a (one uniformity step ARGUED) and is not a live open target; no mass gap is proved.
