# Soldered Theorems 1 and 1′: Born, or a lattice coin

I ran no code and wrote no files.
- **EXACT**: a proof written here.
- **CHECKED**: exact hand arithmetic at the stated points.
- **ARGUED**: reasoning, or a reading of the text, that I have not verified.

"Full soldering" means the T1 action from the landed soldering-menu note (THE_SOLDERING_MENU_FOUR_ACTIONS…_2026-09-22): each of the 24 proper cubic rotations g ∈ O (signed permutation matrices with det = 1) acts on every Bloch vector as g itself.

**Summary**
1. [EXACT] The soldered binary law is one free function of five variables; unsoldered, it is a function of two. In the window l, l′ ≤ 5 that means 32 radial functions against 3. New pieces: terms even in s, and a state-blind l = 9 pseudoscalar K₉.
2. [EXACT] Lane A's "Schmidt axis along z without loss of generality" fails. Its Step 0 holds on lattice axes but fails on body diagonals.
3. [EXACT] Soldered Theorem 1 keeps Lane A's premises and adds one: P_LU, every two-qubit pure state in every pair of local frames. The survivors are Born, or a lattice coin F = (1 + K(p))/2, with K odd and O-invariant.
4. [EXACT] Soldered Theorem 1′ (aligned menus): on each axis, Born or a constant. The constant is ½ on the nine mirror planes.
5. [ARGUED] One sentence restores Born: centre indifference, F(0; p) = ½. It reads naturally as the law-level reading of "Possibilities are distinguished by the supplied algebraic structure alone."

## 1. General soldered binary law (Part 1)

Write F(s; p) = (1 + H(s; p))/2, for a part s in the Bloch ball and a menu {p, −p}. Then:
- H(s; −p) = −H(s; p);
- H(gs; gp) = H(s; p) for g ∈ O;
- |H| ≤ 1.

**Multiplicities [EXACT, character table].** n_l(Γ) is the number of copies of each O-irrep Γ in the degree-l harmonics H_l:

| l | decomposition of H_l |
|---|---|
| 0 | A1 |
| 1 | T1 |
| 2 | E + T2 |
| 3 | A2 + T1 + T2 |
| 4 | A1 + E + T1 + T2 |
| 5 | E + 2T1 + T2 |
| 9 | A1 + A2 + E + 3T1 + 2T2 |

**Form [EXACT].**
H(s; p) = Σ_{l odd} Σ_{l′≥0} Σ_Γ Σ_{i,j} c^Γ_{li,l′j}(|s|) ⟨K^{Γ,i}_l(p), K^{Γ,j}_{l′}(ŝ)⟩.
- Each pair (l, l′) carries N(l, l′) = Σ_Γ n_l(Γ) n_{l′}(Γ) free radial functions of |s|.
- Under SO(3) the count is δ_{ll′}, one per odd l.

N(l, l′) for l′ = 0 … 5:

| l | l′=0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 1 | 2 |
| 3 | 0 | 1 | 1 | 3 | 2 | 3 |
| 5 | 0 | 2 | 2 | 3 | 4 | 6 |

That is 32 radial functions against 3. In closed form: one function on (ball × sphere)/O, odd in p, so five variables; unsoldered it is a function of (|s|, ŝ·p).

**New features [EXACT].**
- **Terms even in s (l′ even):**
  - p·V(ŝ), with V_x = s_y s_z (s_y² − s_z²) and cyclic, at l′ = 4.
  - U(s, p) = Σ_cyc s_b s_c p_a (p_b² − p_c²), at l = 3, l′ = 2.
- **A state-blind term at l = 9, l′ = 0:** K₉(p) = p_x p_y p_z (p_x² − p_y²)(p_y² − p_z²)(p_z² − p_x²). It is the lowest odd O-invariant: xyz and the squared Vandermonde factor each carry the sign of the axis permutation, so their product is invariant.
- **Θ-odd terms:** terms with l′ even change sign under Θ: (s, p) → (−s, −p). Unsoldered laws are always Θ-even.
- **Mirror planes:** every odd O-invariant function vanishes on the nine mirror planes. For p on such a plane, some C₂ in O sends p to −p.

## 2. Soldered Theorem 1 (Part 2)

**Premises.**
- Lane A's: C1, C2, C3, C4a + C4b, the same law at both sites, antipodal normalisation, boundedness, every menu m at B, every probe p at A.
- **New, P_LU:** every pure state with Schmidt length r ∈ [0, 1) is preparable, in every pair of local frames. Unsoldered, the single family ψ_r was enough because covariance makes local frames free; soldered, it does not.

**Steering [EXACT].**
- Write s_A = r â and s_B = r b̂.
- B's local frame enters through a steering isometry O with det O = −1 and O b̂ = â. Under P_LU, O can be any such isometry.
- B's outcome ±m leaves A in
  n_± = [(r ± c) â ± √(1 − r²) m′_⊥] / (1 ± rc), where m′ = O m and c = b̂·m = â·m′.
- B's weights are w_± = (1 ± H(r b̂; m))/2.
- Write h(q, p) := H(q; p) for |q| = 1.

**Lane A's Steps 0 and 3 [EXACT].** Step 0's claim H(r, 0) = 0 needs some C₂ in O that fixes ŝ and reverses p ⊥ ŝ.

| Schmidt axis | Step 0 |
|---|---|
| Lattice axis | holds: the C₂ about that axis does it |
| Body diagonal | fails: O has no C₂ about [111] |
| Generic | no constraint |

The bounded law H = s·p/2 + U/3 is a body-diagonal counterexample: H(r ê₁₁₁; (1, 0, −1)/√2) = −r²/(9√2) ≠ 0. Lane A's Step 3 uses h(q·p), so it does not run as written. Steps S1–S5 below replace Steps 3–5.

**S1, frame decoupling [EXACT; uses C3, C4b, P_LU].**
- Fix 0 < r < 1, |c| < 1, and A's data (â, m′).
- Every B-pair (b̂, m) with b̂·m = c is realised with the same A data: exactly one det −1 isometry maps (b̂, m) to (â, m′).
- C4 reads ½[h(n₊, p) + h(n₋, p)] + ½ H(r b̂; m) Δ(p) = H(r â; p), where Δ := h(n₊, ·) − h(n₋, ·).
- If Δ(p) ≠ 0 for some p, then H(r b̂; m) = 𝓗(r, c). So B's mixed law takes the unsoldered form, and it is odd in c, so 𝓗(r, 0) = 0.
- C4a alone loses this comparison across frames.

**S2, dichotomy [EXACT].**
- At fixed (r, c), the pairs (n₊, n₋) form one SO(3) orbit with a fixed angle θ ∈ (0, π), since n₊·n₋ = (2r² − 1 − r²c²)/(1 − r²c²).
- If Δ ≡ 0 on that orbit, chains of steps of angle θ make h state-blind: h(q, p) = K(p).
- **(i) State-blind:** C4b then forces H(s; p) = K(p) at every part. This is the lattice coin.
- **(ii) Otherwise:** S1 holds at every interior (r, c), and by the same-law premise A's mixed law is 𝓗(|s|, ŝ·p).

**S3, chord Jensen [EXACT].**
- In case (ii) take c = 0, so both weights are ½. Every pair x ≠ ±y is a steering pair, with midpoint (x + y)/2 = s_A. So h(x, p) + h(y, p) = 2H((x + y)/2; p).
- If x − z = x′ − z′, then the pairs (x, z′) and (x′, z) share a midpoint. So h(x, p) − h(z, p) = δ_p(x − z) depends on the chord vector alone.
- For small non-parallel u, v there is a common middle point z: two planes meet the sphere. Then x = z + u and y = z − v give δ_p(u + v) = δ_p(u) + δ_p(v).
- δ_p is bounded by 2, so it is linear (bounded Cauchy).
- Hence h(q, p) = a(p) + b(p)·q at every q. No measurability is used; boundedness and P_LU take its place.

**S4 [EXACT].**
- The midpoint relation becomes a(p) + r b(p)·â = 𝓗(r, â·p).
- Taking â ⊥ p, at both ±â, gives a(p) = 0 and b(p) = β(p) p.
- At fixed t = â·p ≠ 0, r β(p) t = 𝓗(r, t) for every p, so β is constant.
- So every cubic piece is zero: K, and the l = 3, 5, … T1 parts of b. Mixtures of Born with K die here.

**S5, calibration [EXACT].**
- β ≠ 0 in case (ii).
- At c = 1, n_± = ±â, which gives H(r b̂; b̂) = r.
- At c = 0 with A's probe along â: β r = H(r â; â) = r, so β = 1.
- At r = 0, any n ⊥ p gives H(0; p) = 0.

**Result [EXACT under the premises].** The survivors are:
- **Born:** F = (1 + s·p)/2 on every part; or
- **a lattice coin:** F = (1 + K(p))/2, with K odd, O-invariant and |K| < 1. K = 0 is the plain coin.

**Lattice-coin check [EXACT/CHECKED].**
- Take K = κ K₉ with |κ| ≤ 3√3. Since |xyz| ≤ 1/(3√3) and each bracket is at most 1, |K| ≤ 1.
- At p = (2, 3, 6)/7, which lies off every mirror plane: K₉ = 155520/7⁹. With κ = 5, K = 777600/40353607.
- In every C4 instance — lattice-axis, body-diagonal or generic Schmidt axis, with any weights — w₊K(p) + w₋K(p) = K(p) = H(s_A; p) identically.
- K vanishes on the lattice axes, face diagonals and body diagonals. It is visible on generic axes.

**Which configurations do the work.**
- With lattice-axis Schmidt states plus relative phases, S1 gives axial symmetry about those axes and nothing more.
- The c = 0 midpoint test then admits the l = 3 functions 5q_a³ − 3q_a [EXACT].
- The first-order deformation h = q·p + ε Σ_a p_a(5q_a³ − 3q_a) passes every c = 0 lattice-axis instance. Its mixed extension is forced by that test. It fails at r = c = ½, p = e_z: the left side is −3/40 and the right side is −7/8 [CHECKED].
- Body-diagonal families give the analogous axial result about [111].
- Whether these symmetric families force Born without generic frames is not shown.

**Price of P_LU [ARGUED].**
- The SU(2)-invariant Heisenberg bond turns both frames together, so from product states it gives (R⊗R)ψ_r and not P_LU.
- Fields from recorded neighbours under compression, or soldered couplings (K/J, D/J ≠ 0; landed 9040), could supply the relative frames.

## 3. Soldered Theorem 1′ (Part 3)

**Setting.** Menus aligned with the excitation axis n̂, the state α|100⟩ + β|010⟩ + γ|001⟩, and u(p) = the odds of "1" at excitation probability p.

**The π-rotation step is not needed [EXACT].**
- Put a = 1 − c in the unify report's Step 3: u(1 − c) = u(c) x + (1 − u(c)) y, where x = u(0) and y = u(1).
- Using this at both c and 1 − c gives u(c)[1 − (x − y)²] = y(1 + x − y).
- **If (x − y)² < 1:** u is constant on (0, 1). The c = 0 instance gives x(x − y) = 0, and the main equation then makes u a constant κ on [0, 1]. Positive odds keep κ ∈ (0, 1).
- **(x, y) = (1, 0):** excluded, because x(x − y) = 1.
- **(x, y) = (0, 1):** this gives u(1 − c) = 1 − u(c), and the unify Steps 4–5 give u(p) = p.

**Result [EXACT].** On each axis the law is Born or a constant κ(n̂).
- κ(g n̂) = κ(n̂), and κ(−n̂) = 1 − κ(n̂) by relabelling outcomes. So κ = (1 − K(n̂))/2 with K odd and O-invariant.
- κ = ½ on the mirror planes, which contain the lattice axes, face diagonals and body diagonals.
- Aligned worlds never compare axes, so Born can hold on some orbits of axes and lattice coins on others. S2 rules out that mixing once off-axis menus and P_LU are present.
- Check at a = c = ⅓: κ against κ² + (1 − κ)κ = κ, so it passes for every κ.

## 4. Bottom line (Part 4)

**Does Born survive soldering? [EXACT]** Partly. Under the clause's inputs plus P_LU, soldering adds exactly one family of survivors: the lattice coins (1 + K(p))/2.
- They are state-blind and handed: K is odd under the inversion in O_h.
- D2 as worded ("varies with", read on the odds) does not remove them. Under a menu rule set by the neighbours, (1 + K(m))/2 moves with the neighbours through m. This is the same mechanism as the unify report's field-aligned coin.
- Without P_LU, Born under soldering is not shown.

**Restoring sentences [EXACT given the result above].** Each of (a)–(c) cuts the survivors to {Born, plain coin}; D2 then removes the plain coin. Sentence (d) does both jobs at once.
- **(a) Centre indifference:** "Where a site's part is unchanged by every automorphism of its domain, every possibility of a menu has the same odds", i.e. F(0; p) = ½.
- **(b)** Θ-covariance of the law.
- **(c)** Unsoldered SO(3) covariance for the law, with the generator still soldered.
- **(d)** Sharpened D2: "on a fixed menu, the odds vary with the site's part."

**Is the restoring sentence a reading of "No possibility is privileged"? [ARGUED]**
- **(a): yes, I think so.** It reads the next sentence, "Possibilities are distinguished by the supplied algebraic structure alone", at the law level, at the one part where that structure distinguishes nothing. The lattice coin favours p over −p there by lattice orientation alone. The weaker group reading, O-covariance, lets it through. Born pays nothing for (a), and unsoldered it is automatic.
- **(b):** a weaker reading, because Θ is antilinear. That puts it outside the complex-linear automorphisms the soldering menu uses.
- **(d):** a reading of "varies with", not of the possibility sentence.

**The D5 tension [EXACT/ARGUED].**
- EXACT: C4 plus P_LU remove every cubic term from the law except K.
- ARGUED: the photon lane's soldering sits in the generator and the link possibilities. So a soldered generator with a Born law is consistent, since Born is O-covariant.
- The added price is P_LU, plus (a) or (d).

**Follow-up spec (not run).**
- Linearise C4 about Born over all O-invariant deformations with l, l′ ≤ 9, in exact rationals, using lattice-axis and body-diagonal families with phases and no generic frames.
- If the kernel is span{K₉}: those families are enough and P_LU is unnecessary.
- If the kernel is larger: the extra vectors are anisotropic laws that need P_LU. The l = 3 vector must reproduce −3/40 against −7/8.