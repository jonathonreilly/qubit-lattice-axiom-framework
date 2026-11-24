lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T03:58Z

# Check of row 1475 (gap-k2-pivot-environment-astra62): queue row 1484

Started 2026-11-24T15:58Z (date -u), Mac mini worker 2, Claude Opus 5.5 high. Cross-provider check of
`library/gap-k2-pivot-environment-astra62.md` (gpt-6.2-astra max), pinned at df2c44d91.

## Plan

1. Read row 1475's output in full; read row 1348 (`library/gap-blockstep3-astra62.md`) line 30 class
   definition and check 1350; row 1345/1347 centre-sign map; row 1471 end class (457/625).
2. Membership of the beta = 23/10 counterexample in the iterable class.
3. Conditional covariance >= 371/432 at large separation.
4. Purity <= 41/81 on m = 512 v families, even v >= 4.
5. Invariance of the sixteen masses under pivot and centre-sign steps, with twists.
6. delta > 1/6 and > 1/10 numbers.
7. Continuous-law robustness (radius 1/32, 13 balls, eps = 2^-64, covariance > 5/6).
8. Pure Wilson family outside the counterexample?
9. Verdict.

## 0. Sources read and conditions (16:04Z, date -u)

Read in full: `library/gap-k2-pivot-environment-astra62.md` (176 lines, the text checked; cited below as
"1475 line n"), `library/gap-blockstep3-astra62.md` lines 1-238 (row 1348; the class is line 30, the sizes
(2) are line 25), check 1350 section 7 entry for line 30 (`gap-blockstep3-check-opus.md`), row 1471
sections 4.2-4.3 (`gap-k2-end-class-fable.md` lines 163-273, 394-400), row 1468 section 3.1 and Lemma TW
(`gap-k2-tool-design-fable.md` lines 99-175), row 1345 lines 1-123 (`gap-blockstep2-astra62.md`).
Not re-read: the Sussman-Alpoge outline ranges that 1475 cites in section 1 and for GL8 / AM2 (1475 lines
19, 114, 129). They are credited there for the transfer-matrix construction; every step of it that the
refutation uses is re-derived below, so nothing rests on them.

No numeric run: `memory_pressure` showed 39 percent free at the start of this run, below the 50 percent floor. All
checks below are by hand, exact fractions written out. No Lean.

## 1. Membership in the iterable class of row 1348 line 30 (1475 lines 21-60). HOLDS.

The class (1348 line 30, check 1350 section 7 "Line 30, iteration. HOLDS"): a positive finite
environmental measure, arbitrary real symmetric edge matrices and four-linear plaquette tensors in the
form (1) of 1348, Z = integral d(env) integral exp(sum_E v_E^t Q_E v_E + sum_P T_P[...]) prod dv_E. No
locality, size or product condition is part of line 30; 1475 imposes three more (product reference,
nearest-neighbour coefficient dependence, the sizes (2) at B = 2), which only makes the member stricter.

Checked one by one:

- Environment: s_x (fair signs), h_x, l_e, r_e (Haar), b_e (coin) are independent of each other and of
  the link Haar. Positive finite measure. HOLDS.
- T_p = beta q(U_1 U_2 U_3^-1 U_4^-1) with the twist sign on seam representatives. Inversion on unit
  quaternions is conjugation, real linear, so T_p is four-linear, sup norm beta <= 4 beta = beta B^2. HOLDS.
- Q_e in (1): u -> l u r is orthogonal, so the first term is O^t H_e O, traceless since tr D = tr D' = 0.
  q(h_x^-1 U h_y) = Re(h_x^-1 U h_y) = U . (h_x h_y^-1) = U . w with |w| = 1, so the bracket is
  U^t (w w^t - I/4) U, traceless with eigenvalues 3/4, -1/4 (x3); times gamma = 1/8 its norm is 3/32.
  ||Q_e|| <= ||b_e D'|| + 3/32 = 12 + 3/32 < 12 beta = 27.6. HOLDS.
- Gauge covariance under U_xy -> g_x U g_y^-1, h_x -> g_x h_x, l_e -> l_e g_x^-1, r_e -> g_y r_e: both
  l U r and h_x^-1 U h_y are unchanged; Haar reference invariant. Edge reversal: r^-1 U^-1 l^-1 =
  conj(l U r) negates components 1,2,3; diag(1,1,-1,-1) and diag(2,0,-1,-1) are even in each. HOLDS.
- A = integral e^{6(2x-1)} dx = (e^6 - e^-6)/12 = sinh 6 / 6, with x = |z_1|^2 uniform on S^3 (the
  Archimedes property in C^2). Series terms 1, 6, 10.8, 9.26, so A > 26. B_1 <= e^{max u^t D' u} = e^2 < 9.
  D = (D' + D'')/2 with D'' = diag(0,2,-1,-1) conjugate to D' by a coordinate swap; Jensen pointwise
  e^{3a+3b} <= (e^{6a} + e^{6b})/2, strict where u_0^2 != u_1^2 (positive measure), so A < B_6. So
  0 < p < 1 and p B_6 + (1-p) B_1 = A. HOLDS.
- Local read (2): ++ gives eigenvalues 6,6,-6,-6; -- gives 2b, 0, -b, -b with b in {1,6}; +- gives 0.
  Perturbation norm <= 3/32 < 1/2, Weyl's inequality: counts 2, 1, 0. The ramp version: eigenvalues
  within 3/32 of {6,-6}, {>=2, 0, <=-1}, {0}; ramps sum to 2, 1, 0; the map 0,1,2 -> 0,-1,1 (const 1
  above 2) is continuous with |f| <= 1. HOLDS.
- Edge integration (3): at fixed U, l U r is Haar, so the frame/coin integral is A (++), E_b B_b = A (--),
  1 (+-) = sqrt(A) e^{J eta_e}, J = (log A)/2. Fubini on a positive integrand. HOLDS. Per-site scalars:
  (sqrt A)^{|E|} = A^{2|Lambda|} and e^{-beta |P|} = e^{-6 beta |Lambda|}. HOLDS.

Remark (not an error). The member is not a direct product: the spin coupling K_e depends on U through
the gamma term, and centre signs leave it invariant (q^2 is even). Row 1475's repo search credits the
direct-product version (Proposition NP, gap-crux-exercise4-max.md 383-419) and the Ising film (row
gap-solve19-astra62). The coupled version is what keeps the reference a product.

## 2. Conditional covariance >= 371/432 at large separation (1475 lines 62-98). HOLDS.

- (4): 2K_e >= log A - 2 gamma/4 = log A - 1/16; e^{-1/16} >= 15/16; 26 . 15/16 = 24.375 > 23; w_e > 22.
- FK: e^{K s s'} = e^{-K}(1 + w 1[s = s']); summing fair signs gives weight 2^{k(S)} prod w_e and one
  free sign per cluster; E[s_x s_y | U, h] = P(x <-> y). Single-edge odds w_e or w_e/2, so
  P(closed | rest) <= 2/(2 + w_e) < 1/12, and k distinct edges are all closed with probability <= 12^-k.
- Separation: the edge boundary of the open cluster of x in the plane is a cut; its planar dual is an
  even subgraph, a union of edge-disjoint simple dual cycles; a primal path x -> y crosses it oddly, so
  either a dual cycle is noncontractible or a contractible one separates x from y. HOLDS.
- Noncontractible: length k >= m, at most 4 m^2 3^{k-1} walks, sum (4m^2/3) sum_{k>=m} 4^-k =
  (16/9) m^2 4^-m; at m = 4 this is (16/9)(16/256) = 1/9, and the ratio (m+1)^2/(4m^2) < 1. HOLDS.
- Contractible around a given site: the ray crosses within k/2 bonds (width <= k/2); 1475 uses k bonds,
  2 . 3^{k-1} walks per crossed edge, giving (2/3) sum_{k>=4} k 4^-k per site, (4/3) sum for both sites.
  sum_{k>=4} k t^k = t^4 (4/(1-t) + t/(1-t)^2) = (1/256)(16/3 + 4/9) = 13/576 at t = 1/4; times 4/3 is
  13/432. So 13/432 covers both sites, with a factor 2 to spare. HOLDS.
- 1 - 1/9 - 13/432 = (432 - 48 - 13)/432 = 371/432 > 360/432 = 5/6. HOLDS.
- (6): the spin law (3) depends on s only through s_x s_y, so E[s_x | U, h] = 0; f(Q_e) = (s_x + s_y)/2
  exactly, so Cov = (1/4) sum of four connection probabilities >= 371/432. HOLDS.
- Down to the pivots V (functions of U): Cov(X, Y | V) = E[Cov(X, Y | U, h) | V] + Cov(E[X|U,h],
  E[Y|U,h] | V); the second term is 0 since the inner means vanish. HOLDS.
- Is f(Q_e) a one-block environmental function after the pivot? For e internal to a 2^4 box, the
  old quadratic becomes an environmental constant (1348 line 30) and the new environment contains the
  old one (s, h, l, r, b). f(Q_e) reads s_x, s_y with x, y in that box. HOLDS. The tested estimate of
  1475 section 1 (C e^{-d/xi} uniform in volume) therefore fails for this member.

## 3. Purity <= 41/81 on m = 512 v, even v >= 4 (1475 lines 100-146). HOLDS.

- Spin twist: e^{K a s s'} = e^{-K}(1 + w 1[s s' = a]); for a given S the number of consistent sign
  assignments is 2^{k(S)} if every circuit of S has product of a equal to +1, else 0. So Z_F/Z at fixed
  (U, h) is P(S consistent). HOLDS.
- In an m x v spatial-time plane, a consistent S has a sign field s with all frustrated edges
  (a_e s_x s_y = -1) closed. Each plaquette of the plane has both temporal edges at the same time step,
  so its a-product is +1 and its frustrated count is even: the dual is an even subgraph. A temporal
  circle has a-product -1, so the dual subgraph meets it oddly; by the Z_2 intersection pairing some
  simple dual cycle has odd spatial winding, length >= m. Count with m v starting dual vertices:
  d_{m,v} = (16/9) m v 4^-m <= (16/9) m^2 4^-m <= 1/9 for 4 <= v <= m. Integrating against the positive
  gauge weight of each twist z: 0 <= Z_F^z <= d Z^z. HOLDS.
- Transfer kernel: per slice 4 m^3 edges and 6 m^3 plaquettes give A^{2 m^3} e^{-6 beta m^3}. Symmetry:
  with a -> a^-1, q(u_e a_y u'^-1_e a_x^-1) equals q of its inverse, cyclically rotated, which is the
  swapped term; the site term likewise. Real symmetric bounded kernel on a compact product: Hilbert-
  Schmidt, self-adjoint; T^v >= 0 for even v (positivity of T, also proved there via the Gram kernel
  (h.k)^2 - 1/4 = tr(M(h)M(k)) and the gauge-averaging projection, is not needed for even v). HOLDS.
- Traces: Tr(C_z T^v) = integral T^v(C_z X, X) dX. C_z flips the spatial i-links on the i-cut of one
  slice; in the temporal plaquettes at the seam this flips exactly the (0,i) plaquettes on the cut,
  i.e. the twist z with its seam representative; spatial plaquettes contain 0 or 2 flipped links; K_e
  is even. F flips site spins; every term is even in s. So C_z, F commute with T and with each other.
  HOLDS.
- A_+- = Pi_+- T^v Pi_+- with commuting projections Pi_+- = P_c (I +- F)/2: positive, orthogonal ranges,
  traces (Z_+ +- Z_{+,F})/2, Z_+(2v) = Tr A_+^2 + Tr A_-^2 <= (Tr A_+)^2 + (Tr A_-)^2 =
  (Z_+^2 + Z_{+,F}^2)/2. With 0 <= Z_{+,F}/Z_+ <= d: P <= (1 + d^2)/2 <= (1 + 1/81)/2 = 41/81. HOLDS.
- 41/81 < 457/625: 41 . 625 = 25625 < 37017 = 457 . 81. HOLDS. At m = 512 v, d is below 2^-1000 for
  v >= 4, so P is at most 1/2 + 2^-2000 there.

Mechanism, for the reader: this is the ordered phase of a Z_2 spin with an exact symmetry F commuting
with T. On a slab of spatial side m much larger than its time side the F-even and F-odd sectors have
nearly equal traces, so the neutral transfer operator is effectively doubly degenerate and the purity is
near 1/2, as in Fact PUR of row 1468 3.1 with s near 1.

## 4. Invariance of the sixteen masses, and the bounds delta > 1/6, delta > 1/10 (1475 lines 148-163). HOLDS.

- Pivot step (1348 line 30): a change of variables plus Fubini on a positive integrand, applied to each
  torus; each unnormalized mass is kept with its scalars (check 1350, line 30 HOLDS). Centre-sign step
  (1345 line 11-24, check 1347): an identity for the unnormalized mass "on each torus separately",
  for arbitrary bounded plaquette coefficients, so for the twisted coefficients too. Q2 steps of row
  1468: Lemma TW and the probability release kernel (row 1468 line 162, 204). HOLDS.
- The refutation uses only the sixteen NUMBERS. Whatever densities a chain of mass-preserving steps
  produces on the sixteen tori, END-K2 (b) (row 1471 line 206) applies to any family that realizes an
  end-class rule, and its masses equal the original ones up to a per-site scalar, which cancels from P
  since |Lambda_2v| = 2 |Lambda_v|. So the twist-compatibility paragraph (1475 line 150) is correct but
  not needed for the refutation. Checked anyway: the fine twisted plaquettes (0-coordinate and
  i-coordinate both on the last bond) have all four links crossing a cut, so they are exactly the B^2
  double-cut plaquettes of the coarse twisted plaquette, all with the same sign, and no single-cut
  plaquette is twisted. HOLDS. Sizes: k pivot steps at B = 2 map fine tori (2^k m, 2^k v) to (m, v);
  the fine sides keep m = 512 v and even v >= 4, so (8) applies at the fine level. HOLDS.
- Forest remark (1475 line 152): with zero transverse corner, the pivot of the interface from box x in
  direction mu runs from 2x + e_mu to the corner 2(x + mu); its leaves have odd mu-coordinate, so the
  stars at the corners are vertex-disjoint, a forest; a gauge-invariant law (here after integrating h)
  has product Haar marginal on forest links. HOLDS. (This is equally true for the pure Wilson model; the
  remark shows that the normalized pivot marginal carries no information about P.)
- delta > 1/6: if |log Z^z(tau) - c|Lambda_tau|| <= delta on all sixteen tori then
  P >= e^{-delta}/e^{2 delta} = e^{-3 delta}; with P <= 41/81, delta >= (1/3) log(81/41); (81/41)^2 =
  6561/1681 > 3 > e, so log(81/41) > 1/2. HOLDS.
- delta > 1/10: same algebra against an end-class family with P-hat >= 457/625 gives
  3 delta >= log(37017/25625); 37017 . 7 = 259119 > 256250 = 25625 . 10, so the ratio exceeds 10/7 >
  e^{3/10} (e^x < 1/(1-x) on (0,1)). HOLDS. Attainment for the relaxed set (scale short periods by
  e^{-d}, long by e^{d}, P -> e^{3d} P): HOLDS.
- Reading of the sentence "so the 1/100 wrap budget fails" (1475 line 154, FINISH row 1475): the bulk-
  pressure fit delta and END-K2's wrap error eta are different quantities. The rigorous form is the
  contradiction through END-K2 (b): eta <= 1/100 and (E-v) give P >= 457/625 > 41/81. The conclusion is
  right; the sentence is a shorthand. Not a repair, a reading note.

## 5. Continuous-law robustness (1475 lines 165-169). HOLDS.

- Mixture of normalized Lebesgue measure on the operator-norm balls of radius 1/32 (weight 1 - eps)
  and 13 (weight eps = 2^-64) in the 9-dimensional space of traceless real symmetric 4 x 4 matrices:
  invariant under O(4) conjugation, so E e^{u^t R u} is the same for every unit u; integrating R_e
  gives a common per-edge factor, (8) is unchanged exactly. ||Q_e + R_e|| <= 12 + 3/32 + 13 < 27.6.
  HOLDS.
- Density and support: Q_e + R_e has a density (convolution with a density); joint density by
  independence; support = closure of the union of products of balls B(Q_e, 13), each convex and
  containing 0 (||Q_e|| < 13), so star-shaped about 0, connected. HOLDS.
- Large-ball posterior at fixed U and base variables: odds <= eps e^{13} / ((1 - eps) e^{-1/32}) <
  2^-64 4^{13.04} (1 + 2^-63) < 2^-37 < 2^-11 = b. HOLDS (very loose).
- Small ball: total perturbation <= 3/32 + 1/32 = 1/8, the ramps (1/4 to 3/4) still read 2, 1, 0
  exactly (eigenvalues near 6 / -6; >= 15/8, in [-1/8, 1/8], <= -7/8; all <= 1/8). HOLDS.
- Moments: |f~ - f| <= 2 off the large-ball events, so |E[f~ | V]| <= 2b and
  |E[f~ f~' | V] - E[f f' | V]| <= 2 . 2b; with E[f | V] = 0 and E[f f' | V] >= 371/432:
  Cov(f~, f~' | V) >= 371/432 - 4b - 4b^2. 11/432 > 0.025 > 4b + 4b^2. HOLDS. (1475 writes "after
  conditioning on the pivots"; the direct computation conditional on V, as here, is the valid route; the
  law of (U, h, s, l, r, b) is unchanged by the R integration, since that integration is a constant.)

## 6. Is the pure Wilson family really outside the counterexample? (1475 line 171)

**Outside the construction: yes. Outside the conclusion: not proved; that is the open consumer itself.**

- Construction. The Wilson family starts at Q_e = 0, and its blocked matrices (1348 lines 13-28) are
  built from open-box Wilson laws and relative Haar links. It has no environment variable with an exact
  symmetry like F that commutes with the transfer operator and keeps the matrix spectrum visible. So the
  member of 1475 is not in that family, and neither failure in 1475 (conditional mixing, purity) is
  shown for Wilson. 1475's scope sentence is correct.
- Conclusion. The purity obstruction uses only the sixteen masses (section 4). So for ANY starting
  member X and ANY chain of mass-preserving steps, entry into END-K2 with eta <= 1/100 implies that X's
  own purity at the fine sizes satisfies P_X >= 457/625. For Wilson at beta = 23/10 this is (PUR-io) of
  row 1468 3.1 at those sizes, which by Fact PUR gives the seed. Row 1471 lines 394-400 already says
  the same thing for the strength-zero entry ("the purity statement itself"). The point is not new; I
  cite it.
- What is proved for Wilson does not separate the two cases. At fixed m the Wilson neutral transfer
  operator has a strictly positive kernel, so by Jentzsch's theorem its top eigenvalue is simple, and
  P_W(v) -> 1 as v -> infinity. **The member of 1475 has the same property**: its kernel L is strictly
  positive, and its F-odd top eigenvalue lies strictly below the F-even one at each fixed m. The two
  differ only in whether the neutral gap is uniform in m at the aspect ratio m = 512 v, i.e. in the
  mass-gap question. Physics expectation, not evidence: at beta = 2.3 with time side v >= 165 the SU(2)
  Wilson theory is deep in the confined, zero-temperature regime with a unique vacuum, so P_W is
  expected near 1. No proved statement on file gives this.
- Consequence for a proof on the narrower family (GUIDE). Any such proof has to use a property of
  Wilson that fails for an ordered environment: uniform-in-m non-degeneracy of the neutral top
  eigenvalue, or a local criterion that implies it. 1475's next row 1 (interface transmission, row-sum
  criterion < 1) does reject the member of 1475: its same-plane interface reads have pairwise
  correlation >= 371/432, so seven exits give a row sum above 1. So the guessed criterion is aimed at the
  right property. Turning a passed test into a mass bound is still row 2 (gluing).

## 7. Verdict

**HOLDS.** No line is wrong. No repair is needed. Four reading notes, none of which changes a claim:

1. The 13/432 bound for a contractible separator covers both sites. It counts k crossed bonds where
   k/2 would do, so it has a factor 2 to spare (section 2).
2. The twist-compatibility paragraph (1475 line 150) is correct but not used. The refutation needs only
   the sixteen numbers, because END-K2 (b) applies to any realizing family (section 4).
3. "The 1/100 wrap budget fails" is shorthand. The rigorous form is: eta <= 1/100 and (E-v) give, by
   END-K2 (b), P >= 457/625 > 41/81. A bulk-pressure fit delta and the wrap error eta are different
   quantities (section 4).
4. In the robustness step, compute the covariance directly, conditional on the pivots V, with
   |E[f~ | V]| <= 2b. That route is valid, and it gives 371/432 - 4b - 4b^2 > 5/6 (section 5).

| Claim (1475) | Lines | Verdict |
|---|---|---|
| member of 1348 line 30, sizes (2) at B = 2, gauge covariance | 21-60 | HOLDS |
| 0 < p < 1, edge integral sqrt(A) e^{J eta}, read (2) | 25-58 | HOLDS |
| w_e > 22, FK closed-edge bound 12^-k | 64-70 | HOLDS |
| conditional covariance >= 371/432 > 5/6, down to pivots | 72-98 | HOLDS |
| Z_F^z <= d Z^z, d = (16/9) m v 4^-m <= 1/9 | 100-112 | HOLDS |
| transfer kernel, traces with C_z and F | 114-136 | HOLDS |
| P <= (1+d^2)/2 <= 41/81 < 457/625 | 138-146 | HOLDS |
| mass invariance with twists; forest remark | 150-152 | HOLDS (twist part not needed) |
| delta > 1/6, delta > 1/10, relaxed-set distance exact | 154-163 | HOLDS |
| continuous-law robustness, covariance > 5/6 | 165-169 | HOLDS |
| Wilson family outside | 171 | outside the construction; the conclusion for Wilson is (PUR-io), open |

Provenance: checker Claude Opus 5.5 high (Anthropic). The author was gpt-6.2-astra max (OpenAI), so
the provider differs. My derivations are by hand. For the FK coupling, the Peierls counts and the
trace inequality they follow the author's route, because these steps are short and standard. They are
not an independent derivation in the sense of the working rules. The arithmetic was redone exactly by
hand. No numeric run (39 percent free memory). No Lean.

Credits: Tadeusz Balaban (the block-average structure behind 1348's pivot); Roland Kotecky and David
Preiss (the polymer theorem behind END-K2 via Lemma KP-F of row 1471); Ethan Sussman and Levent Alpoge,
with Claude and Codex (the two-slice transfer GL8, outline 2313-2335; the positivity argument AM2,
2775-2795; the mass-versus-law distinction, outline 394-416, revision 31a47c543775). The Fortuin-
Kasteleyn / Edwards-Sokal coupling and the Peierls contour count are classical tools used by 1475.

Finished 2026-11-24T16:06Z (date -u).

RESULT: Row 1484 (Claude Opus 5.5 high, cross-provider check of row 1475, by hand, no numerics, no Lean): HOLDS. The beta = 23/10 member belongs to row 1348's iterable class (line 30, sizes (2) at B = 2). Its conditional edge-matrix covariance is at least 371/432 > 5/6 at every separation, down to the pivots. Its purity is at most (1+d^2)/2 <= 41/81 < 457/625 on m = 512 v, even v >= 4. The sixteen masses are invariant under the pivot, centre-sign and Q2 steps; the refutation needs only those numbers, so twist compatibility, though true, is not used. delta > 1/6 and delta > 1/10 hold. Continuous-law robustness holds (eps = 2^-64, radii 1/32 and 13, covariance > 5/6). Four reading notes; no repair. The pure Wilson family is outside the construction but not provably outside the conclusion. For Wilson, entry by any mass-preserving chain is equivalent to (PUR-io) at the starting sizes, as row 1471 already noted. Finite-m Perron-Frobenius does not separate the cases, because the member of 1475 has it too. Open: uniform-in-m non-degeneracy of the Wilson neutral vacuum (the consumer itself), and 1475's next rows (interface transmission, which correctly rejects the member, and gluing).
