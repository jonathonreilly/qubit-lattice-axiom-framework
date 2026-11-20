lead: anthropic/claude-opus-5-5/max laptop-subagent

# Check of row 1301 (`library/gap-owner-tiling3-astra62.md`), FINISH row 1305

Status: done (Steps 1-8). Counts: 35 PROVED statements, 35 HOLDS, 0 FAILS; RESULT L308 HOLDS AFTER CORRECTION; verdict table and RESULT line at the end.

## Plan (eight steps)

1. Read row 1301 in full. List every PROVED statement and every numbered display.
2. Read the cited rows (1273 with check 1279; 1286 with check 1287; 1285 with check 1292) and (N-phys) in `library/gap-mini-neutral-fable.md` lines 35-55.
3. Check positive claims 1 (eight magnetic sectors cancel the leading vacuum defect at weak coupling) and 2 (the separately neutral product undercounts the doubled trace by more than 2^(9/2)).
4. Check positive claims 3 (fifteen exponentially soft neutral excitations with only diagonal neutrality) and 4 (half-time separate-block upper comparison).
5. Check claim 5 (bounding the signed seam integral (14) for all large times is exactly what remains for the fixed gap fraction (15)). Decide whether (14) restates (N-phys).
6. Check every remaining statement.
7. Numeric guidance run (guide only; under 1 GB, BLAS threads 1, outside the repository).
8. Counts, verdicts, not-checked list, meaning for the owner's tiling idea, RESULT line.

## Step results

### Step 1. Inventory of row 1301 (read in full, 308 lines)

Pin: the file as read at the start of this check (308 lines; RESULT at L308). Labels in the file: PROVED, GUIDE, OPEN; no ARGUED.

PROVED statements, numbered here S1-S35 by their headed blocks (proof paragraphs are counted with the statement they prove):

| # | lines | statement |
|---|---|---|
| S1 | L27-29 | flat colour characters: characters of every flat in flux m != 0 are m^perp \ {0} |
| S2 | L31-42 | one doubling, (1): lim [E_0(2b) - sum_m E_m(b)] = 0 |
| S3 | L44-49 | size of the cancelled term: lim [E_0(2b) - 8E_0(b)] = 15A/(2b) + O(b^-3) |
| S4 | L53-60 | (2): neutral ratio limit 2^(9/2) prod Q_m/P_m > 2^(9/2) |
| S5 | L62-67 | (3): D_0(t;b) ~ C beta^(3/2) log beta (b/t)^(9/2) Q_0(t;b) |
| S6 | L69-75 | twisted factors: D_m -> P_m, 1 < Q_m/P_m < 4 |
| S7 | L77-81 | parity identity Q_0(t;2b) = Q_0(t;b) prod Q_m(t;b); proof of (2) |
| S8 | L87-91 | (4): dyadic hierarchy ratio |
| S9 | L93-98 | (5): coefficient-one comparison needs periodic time t/N |
| S10 | L100-115 | (5a): R_N(t) < 1, increasing to one; occupation identity |
| S11 | L117 | sharpness: twisted neutral trace starts at 2 omega; alpha <= 1/2 |
| S12 | L119 | last hierarchy level: twenty two-quantum levels, excess > 1/2 |
| S13 | L125-127 | joint range beta >= (2b)^32: b Delta_mix -> 0 with divergent trace |
| S14 | L129-133 | full traces: D_m^all -> 2Q_m, D_0^all/D_0 -> 8 |
| S15 | L135 | full-trace ratio -> 2^(-5/2) |
| S16 | L139-146 | (6): one exact fold and its averaging consequence |
| S17 | L148-161 | anisotropic two-dimensional counterexample to the mixed product |
| S18 | L165-176 | (7), (8): flat seam measures miss the translation characters |
| S19 | L178 | exact link multiplication impossible |
| S20 | L180 | the split misses the p-p interaction |
| S21 | L182-186 | no local sign repair |
| S22 | L190-194 | exponentially soft charged state in each twisted block |
| S23 | L196 | fifteen soft neutral excitations (diagonal neutrality) |
| S24 | L198 | loss of the one-block gap |
| S25 | L200-207 | (9): time window, 1 versus 128 |
| S26 | L211-215 | soft states persist for tile-flip-preserving interactions W |
| S27 | L217 | locality condition for W to preserve tile flips |
| S28 | L221-230 | (10): conditional microscopic gap ratio O(n^(-1+o(1))) |
| S29 | L234-238 | polynomial multiplicities do not repair |
| S30 | L242-260 | (11): uniform twisted neutral lower bound |
| S31 | L262-268 | explicit width B_j = o(beta_j^(1/11)) |
| S32 | L272-285 | seam identity J_0(t;2b) = sum J_m(t;b) + K_beta; (12) |
| S33 | L287-292 | (13): K_beta as a signed seam integral |
| S34 | L294-298 | (14) and its weak-coupling limit 2 log R_2(t) - log R_2(2t) < 0 |
| S35 | L300-304 | (15): K_beta <= sum W_m for all large even t gives the gap fraction |

OPEN: L19, L306. RESULT: L308. GUIDE: L3-17, L23, L25, L83, L121, L232.

Cited earlier rows on which a step depends: 1215 (L42, L67, L75, L117, L119, L125-127), 1143/1145 (L62-67), 1227 (L198, L200, L230), 1147 (L247, L262), 697 (L15, L144), 1273/1279 and 1286/1287 (L13), 1285/1292 and 1291 (L15), (N-phys) for the comparison asked in the brief.

### Step 2. Cited statements read (the parts the steps of row 1301 use)

| cited | where read | content used by row 1301 | check status on file |
|---|---|---|---|
| row 1215, (1)-(4) | `gap-solve23-astra62.md` L17-88 | Wilson transfer F = M C M with normalized C; lambda_0 -> max over flats of L(D_A) = exp[-1/2 sum omega(sigma^2)]; per colour character theta the curl has squared singular values l(q), l(q), 0; periodic limit e^{-3S_n(0)}; S_n(theta) > S_n(0) for theta != 0 | row 1215 checked by Opus 5.5 max, every statement HOLDS (`gap-solve23-check-opus.md` L231) |
| row 1215, (5)-(8) | same file L90-159 | periodic neutral levels coalesce; twisted convergence on invariant normal directions (orbit O = KA, stabilizer {+-1,+-i,+-j,+-k}, Hilbert-Schmidt convergence); first twisted neutral level 2 mu_n; (7) Fourier coefficient -1/(pi^2 |v|^4) + O(|v|^-6); (8) twisted neutral trace (1/4) sum over sign triples of product one; multiplicity twenty | same |
| row 1215, (16)-(19) | same file L267-315 | joint range beta >= n^32: n log-error of the Perron eigenvalue -> 0; distance to an exact flat via comb and rectangle filling; (19) n E_m -> c_m and n log(lambda_0/lambda_j) -> 0 | same |
| row 1145, (5), (11) | `gap-solve2-astra62.md` L56-180 | coefficient of beta^{-(9V-3)/2} log beta on the rectangle (n,n,n,T): C_* n^{9/2} T^{-9/2} [A^{n^3} e^{-3 sum omega_p}]^T prod (1 - e^{-T omega_p})^{-6}, same C_* on every rectangle with sides >= 3; each electric sector has fraction 1/8 | row 1146 (`gap-solve2-check-opus.md` L396-427): (5) on rectangles HOLDS, (11) HOLDS, neutral-sector step HOLDS |
| row 1227, (10), (11), (14) | `gap-solve25-astra62.md` L132-182 | charged energies <= C_n e^{-c_n sqrt(beta)}; first periodic neutral level >= e^{-C_n beta^(1/4)(1+log beta)}; at m = floor(exp(beta^gamma)), 1/4 < gamma < 1/2, U^m -> projection on eight states, one per electric sector | row 1230 (`gap-solve25-check-opus.md` L260): every statement HOLDS |
| row 1147, (13) | `gap-solve3-astra62.md` L149-175 | periodic full gap m(b, beta) >= exp[-C(b^8 + b^(11/2) sqrt(beta))] for b >= 3, beta >= 1; the good-set Dirichlet argument of its section 1 | row 1148 (`gap-solve3-check-opus.md` L277, L578): HOLDS |
| row 697, Lemmas K, X, E | `gap-crux-restate.md` L174-190, L332-334 | kappa non-negative, convex, non-increasing; (b - a) kappa(b) <= log(1 + S(a;b)) for a < b; 1 + S(a;2b) <= (1 + S(a;b))^(2b/(b-a)) | checked by rows 698 and 699 (L328 of that file) |
| rows 1273/1279, 1286/1287, 1285/1292, 1291 | FINISH RESULT lines | L13 and L15 of row 1301 restate these RESULT lines correctly (single block gap kappa g^(2/3)/l for n >= 2; sewn gap kappa_r g^(2/3)/(N l); check 1292 FAILS the closure of the tiling route; 1291 unchecked) | as stated in those RESULT lines |
| (N-phys) | `gap-mini-neutral-fable.md` L35-59 | s(u;n) = X_{0,0}(u) - 1 = D_0(u;n,beta) - 1 in row 1301's notation; (N-phys): one admissible physical side L, all large j, some integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j;n_j) <= 1/2 | the statement itself (OPEN) |

The notation agrees: row 1301's f(k) = 2 arsinh sqrt(sum sin^2(k_j/2)) is row 1215's omega(l(q)) and row 1145's omega_p; row 1301's D_0(t;n,beta) is row 1215's D^0_+ and (N-phys)'s 1 + s(t;n).

### Step 3. Positive claims 1 and 2 (S1-S7)

**S1 (L27-29), flat colour characters. HOLDS.** For m != 0 both B_m(v,w) = det(m,v,w) and p wedge q (with p, q a basis of m^perp) are alternating forms vanishing on m, hence forms on the plane D/<m>, whose alternating forms over F_2 are {0, det}; both are nonzero, so they agree. With h_k = i^{p_k} j^{q_k}: i^a j^b i^c j^d = (-1)^{bc} i^{a+c} j^{b+d}, so the commutator sign of h_v, h_w is (-1)^{p(v)q(w)+q(v)p(w)} = (-1)^{B_m(v,w)}. Ad(i) fixes i and negates j, ij; Ad(j) fixes j and negates i, ij; so the colours i, j, ij carry characters q, p, p+q. Uniqueness: two anticommuting unit quaternions x, y satisfy x y x^-1 = -y, so Re y = 0, likewise Re x = 0, and xy + yx = -2 x.y = 0 gives perpendicular axes; the word for the radical vector m commutes with x and y, hence is +-1. Every seam is +-x^{a_k} y^{b_k}; its adjoint characters on x, y, xy are b, a, a+b; a(m) = b(m) = 0 because h_m is central; a wedge b = B_m != 0 gives a, b independent. So the characters are exactly m^perp \ {0}. For m = 0 the central-holonomy maximum is row 1215 L84 (strict inequality S_n(theta) > S_n(0)).

**S2 (L31-42), equation (1). HOLDS.** Row 1215 (3) is proved for an arbitrary sign field eta with nonempty compact flat set (L50-61 there use only eta_p A_p = 1 and the local Taylor bounds); the corner placement of the stacks for each plane with B_m(e_k,e_l) = 1 is a choice of representative (a central change of variables moves stacks within their class). By S1 every flat in flux m != 0 has the same L(D_A) = exp[-sum_{p in m^perp \ 0} S_b(pi p)] (two transverse singular values l(q) per colour and mode, row 1215 L82). Each nonzero p lies in m^perp for exactly three nonzero m (p^perp has four elements), so sum_m lim E_m(b) = 3 sum_{p in D} S_b(pi p). Writing h = 2h' + p on the side-2b grid gives S_{2b}(0) = sum_{p in D} S_b(pi p). The normalized convolution leaves no constant; the link counts 3(2b)^3 = 8 * 3b^3 agree. So the limit in (1) is exactly 0 at every fixed b >= 3.

**S3 (L44-49), the cancelled term 15A/(2b). HOLDS.** Poisson summation on the b-grid: S_b(0) = b^3 sum_{v in Z^3} fhat(bv). With row 1215 L131, fhat(v) = -1/(pi^2|v|^4) + O(|v|^-6), so 3S_b(0) = 3b^3 fhat(0) - A/b + O(b^-3), A = 3 pi^-2 sum_{z != 0}|z|^-4. Then lim[E_0(2b) - 8E_0(b)] = [24 b^3 fhat(0) - A/(2b)] - 8[3b^3 fhat(0) - A/b] + O(b^-3) = 15A/(2b) + O(b^-3). Independent route (row 1215 L141): 3 sum_{p != 0}[S_b(pi p) - S_b(0)] = (3/(pi^2 b)) sum_z 2 #{p: z.p odd}/|z|^4 = (24/(pi^2 b)) sum_{z not in (2Z)^3} |z|^-4 = (24/(pi^2 b))(15/16) sum_{z != 0}|z|^-4 = 15A/(2b). The two routes agree. Also sum_{m != 0} c_m/b with row 1215's c_m (generalized: each m != 0 contributes (2/(pi^2 b)) sum_z #{p in m^perp \ 0 : z.p odd}/|z|^4) gives the same total, since sum_{m != 0} #{p in m^perp \ 0: z.p odd} = 3 * 4 = 12 for z not in (2Z)^3. Positivity of each S_b(pi p) - S_b(0) is row 1215 L84.

**S5 (L62-67), equation (3). HOLDS.** Row 1145 (11) on the rectangle (b,b,b,t): coefficient C_* b^{9/2} t^{-9/2} [A_h^{b^3} e^{-3 sum omega_p}]^t prod_{p != 0}(1 - e^{-t omega_p})^{-6} of beta^{-(9b^3 t - 3)/2} log beta, with A_h = h_0^3 (2 pi)^{9/2} and the same C_* for every rectangle with sides >= 3 (row 1146 L396-410). The one-link integral I_beta = h_0 (2 pi/beta)^{3/2}(1+o(1)) (row 1215 L50) gives I_beta^{3 b^3 t} = A_h^{b^3 t} beta^{-9 b^3 t/2}(1+o(1)) at fixed (b,t); dividing leaves beta^{3/2} log beta. lambda_0^t -> e^{-3t S_b(0)} (row 1215 (4)) and sum_{p != 0} omega_p = S_b(0) (f(0) = 0). The neutral fraction 1/8 is row 1145 L176-180 (checked). So (3) holds with C = C_*/8, independent of (b,t).

**S6 (L69-75), D_m -> P_m. HOLDS.** The inputs of row 1215's proof of (8) hold for every m != 0: (i) the flat set is one orbit of gauge x flips (two seams with B_m = 1 are conjugate to (i,j); the third is forced up to sign: e.g. m = (1,1,0) gives h_3 anticommuting with h_1, h_2 commuting, so after conjugation (h_1,h_3) = (i,j) and h_2 = +-i; flips absorb signs); (ii) the stabilizer is {+-1, +-i, +-j, +-ij} with compensating flips in m^perp, acting on the colours (characters q, p, p+q) by the four sign triples of product one; (iii) no colour has a zero momentum (every character in m^perp \ 0 shifts the grid by pi p/b), so ker D_A is the gauge orbit tangent and D_A restricted to the normal space is injective. Row 1215's tube, Hilbert-Schmidt and trace convergence argument then applies verbatim; the averaged Hermite traces give P_m. Each Q_m(epsilon) > 0 and (1+x)^-2 < (1-x)^-2 give Q_m/4 < P_m < Q_m.

**S7 (L77-81), parity identity and (2). HOLDS.** h = 2h' + p on the side-2b grid: p = 0 gives Q_0(t;b); for p != 0 the momentum (2 pi h' + pi p)/b is never 0 mod 2 pi, and each p != 0 occurs in three of the m^perp with exponent -2, giving exponent -6. Then by (3) and S6, D_0(t;2b)/prod_m D_m(t;b) -> [(2b/t)^{9/2} Q_0(t;2b)]/[(b/t)^{9/2} Q_0(t;b) prod_{m != 0} P_m] = 2^{9/2} prod_{m != 0} Q_m/P_m. The factor C beta^{3/2} log beta cancels between the two periodic boxes because C is rectangle independent.

**S4 (L53-60), positive claim 2. HOLDS.** It is S5 + S6 + S7. Strictness: each Q_m/P_m > 1. The unnormalized ratio has the same limit since the exponent t[E_0(2b) - sum E_m(b)] -> 0 at fixed t by (1). Subtracting one from numerator and from the whole product leaves the limit because both diverge like beta^{3/2} log beta. Scope, as the file says: fixed (b,t), beta -> infinity first.

Positive claim 1 (eight sectors cancel the leading vacuum defect) HOLDS in the order stated: at each fixed b the beta-limit of E_0(2b) - sum_m E_m(b) is exactly zero, and the term cancelled is 15A/(2b) + O(b^-3) > 0. Positive claim 2 HOLDS: the limiting neutral ratio is 2^{9/2} prod_{m != 0} Q_m/P_m > 2^{9/2}, i.e. the separately neutral product is smaller than the doubled neutral trace by more than 2^{9/2}. Source of the factor (my reading, consistent with row 1215 (20)): the doubled box has the nine-dimensional constant-field phase volume (2b/t)^{9/2}, the half box only (b/t)^{9/2}, and the seven twisted boxes have no constant modes.

### Step 4. Positive claims 3 and 4 (S22, S23, S10, S11)

**S22 (L190-194), soft charged state in each twisted block. HOLDS.** Without flips the eight seam sign patterns modulo the four conjugation patterns (which are the flips z with m.z = 0) leave two gauge orbits O_+, O_-; a flip with m.z = 1 swaps them. U_+-, the open d/4-neighbourhoods in the bi-invariant metric, are gauge invariant, so s = 1_{U+} - 1_{U-} is gauge invariant with flip character z -> (-1)^{m.z}. Checked line by line: (a) ||1_{U^c} psi|| = ||1_{U^c} M C M psi||/lambda_0 <= e^{-beta v/2}/lambda_0, v = min of V_m off U_+ cup U_- > 0 (V_m vanishes exactly on O_+ cup O_-); lambda_0^m has a positive limit (S2). (b) A pair X in U_+, Y in U_- has product distance >= d/2; 1 - cos r >= 2r^2/pi^2 gives sum_e (1 - cos theta_e) >= d^2/(2 pi^2), so the normalized kernel is at most I_beta^{-3b^3} e^{-beta d^2/(2 pi^2)} <= C_b beta^{9b^3/2} e^{-c' beta}; with M <= 1 and ||psi||_1 <= ||psi||_2 = 1 the jump probability is exponentially small. (c) For F psi = lambda_0 psi with a symmetric positive kernel, <s psi,(1 - F/lambda_0) s psi> = (1/2) E |s(X) - s(Y)|^2 under psi(X)F(X,Y)psi(Y)/lambda_0, whose marginals are psi^2. Hence the form is <= 2[P(X not in U) + P(Y not in U) + P(jump)] = O_b(e^{-c_b beta}) and ||s psi||^2 -> 1. Min-max in the character-m sector and -log(1 - x) <= 2x give the bound. This is the lattice form of the 't Hooft electric-flux splitting e = m in a box of magnetic flux m.

**S23 (L196), fifteen soft neutral excitations. HOLDS.** The map {subsets of D \ 0} -> D, I -> sum_{m in I} m, is linear F_2^7 -> F_2^3 and onto (it contains e_1, e_2, e_3), so its kernel has 2^4 = 16 elements; 15 nonempty. Product eigenstates with distinct individual block charges are orthogonal; energies add, so each is at most 7 C_b e^{-c_b beta}. Relabelling the diagonal flips by invertible maps per block keeps rank <= 3, so >= 15. The all-vacuum product is the product's unique positive vacuum.

**S10 (L100-115), equation (5a). HOLDS.** By (3) at sides Nb (time t) and b (time t/N): (Nb/t)^{9/2} = (b/(t/N))^{9/2}, so the singular factors cancel. Iterating S7 gives Q_0(t;Nb) = Q_0(t;b) prod_{j<k, m != 0} Q_m(t;b_j); with S6 at time t/2 this gives the displayed R_N(t). Occupation identity, checked: for real normal modes h with frequency omega_h and stabilizer character chi_h (order two), P_m(u) = (1/4) sum_g prod_h (1 - chi_h(g) x_h)^{-1} = sum over occupations with prod chi_h^{n_h} = 1; with n_h = 2v_h + delta_h this is Q_m(2u) sum_{delta: prod chi^delta = 1} e^{-u sum omega_h delta_h} (finitely many masks, 6b^3 real modes). So P_m(t/2) > Q_m(t) (two quanta of one colour give a nonzero invariant mask). Q_0(t/N;b)/Q_0(t;b) = prod over nonconstant modes of (sum_{d=0}^{N-1} e^{-d omega t/N})^6 > 1, decreasing to 1. Every factor of R_N increases to 1, so R_N(t) < 1 and increases to 1. Since B_N -> infinity and D_0/B_N -> R_N < 1, D_0 - 1 < B_N - 1 for beta > beta_0(b,N,t). Hypotheses: t a multiple of N, t/N >= 3 (rectangle sides >= 3 for (3)), t/2 >= 2 for row 1215 (8).

**S11 (L117), sharpness. HOLDS.** Every colour of a twisted block has a nontrivial stabilizer character (for each colour some sign triple of product one negates it), so one quantum is never invariant and two quanta in one lowest real mode are; the neutral trace starts at 2 omega. Q_m(t) - 1 ~ d e^{-t omega} against P_m(alpha t) - 1 ~ d' e^{-2 alpha t omega} forces alpha <= 1/2; alpha = 1/2 with C = 1 is the occupation identity. lim m_{m,+}(b,beta) = 2 omega is S6's eigenvalue convergence (row 1215 (6) generalized).

Positive claim 3 HOLDS: with only diagonal neutrality the seven twisted tiles carry at least fifteen neutral excitations of energy O_b(e^{-c_b beta}). Its reach: it concerns the independent tensor product, and (S26) products coupled by interactions that preserve each tile's own flips; it does not concern the sewn Wilson cube, whose cross-seam plaquettes break the separate tile flips (the file says so at L215). Positive claim 4 HOLDS: for N = 2 and every fixed b >= 3 and even t >= 6, D_0(t;2b) - 1 < prod_{m in D} D_m(t/2;b) - 1 for all beta > beta_0(b,t). The threshold beta_0 may grow with t; nothing in the file bounds it.

### Step 5. Claim 5: the seam integral (14), the gap fraction (15), and (N-phys)

**S32 (L272-285), seam identity and (12). HOLDS.** log A(t) = log Z_{0,+}(t;2b) - sum_m log Z_{m,+}(t;b), so 2 log A(t) - log A(2t) = J_0(t;2b) - sum_m J_m(t;b): the identity is the definition of K_beta. J is unchanged by Z(t) -> c^t Z(t), so normalization and vacuum energy drop out, as stated. (12): by S4 (unnormalized ratio = normalized ratio in the limit, by (1)) lim K = (9/2) log 2 + sum_{m != 0}[2 log r_m(t) - log r_m(2t)], r_m = Q_m/P_m. P_m/Q_m = (1/4) sum over the four sign triples of prod over negative signs of prod_h [(1 - x_h)/(1 + x_h)]^2, which increases in t; so r_m > 1 decreases in t and each bracket is >= log r_m(t) > 0.

**S33 (L287-292), equation (13). HOLDS.** With sites (x,d), x in (Z/b)^3, d in D, the bijection of links is exact (4 * 8 b^3 t links on each side); interior plaquettes coincide; B_t is a finite signed sum over plaquettes touching a sheet change or a twist stack. With the auxiliary twists z in D^8 averaged uniformly: s = 0 gives prod_d Z_{d,+}(t;b); s = 1 gives (1/8) sum_{z_0} Z^{z_0}(t;2b) = Z_{0,+}(t;2b) because the unused labels average to one. Z(s) is a finite positive smooth function of s, so log A(t) = -beta int_0^1 <B_t>_{s,t} ds, and (13) follows.

**S34 (L294-298), equation (14). HOLDS.** (14) is J_0(t;2b) - sum_m J_m(t/2;b) = K - sum_m W_m, immediate from S32 and the definition of W_m. W_m >= 0: g(x) = log sum_i e^{-x E_i} is convex, J'(x) = 2g'(x) - 2g'(2x) <= 0. Weak limit: the left side equals 2 log[D_0(t;2b)/B_2(t)] - log[D_0(2t;2b)/B_2(2t)] with B_2(t) = prod_{m in D} D_m(t/2;b), so its limit is 2 log R_2(t) - log R_2(2t) = log R_2(t) + [log R_2(t) - log R_2(2t)] < 0 by S10 (even t >= 6). This holds at fixed (b,t) only.

**S35 (L300-304), (15). HOLDS as an implication; its hypothesis is equivalent to its conclusion apart from the equality case.** The asymptotic J(x) = 2 d_1 e^{-x m_1}(1 + o(1)) is correct (compact positive transfer, simple vacuum, finite multiplicity d_1; tail bounded by a fixed-time trace times e^{-(x - x_0) E_2}). Put a = m_{0,+}(2b,beta), c = min_m m_{m,+}(b,beta). By (14) the hypothesis K <= sum W_m is exactly J_0(t;2b) <= sum_m J_m(t/2;b). The left side is 2 d_0 e^{-ta}(1+o(1)); the right side is 2 d_* e^{-tc/2}(1+o(1)) with d_* >= 1 the multiplicity summed over the sectors attaining c (each J_m >= log D_m >= 0). Hence: if a > c/2 the ratio tends to 0 and the hypothesis holds for all large even t; if a < c/2 it fails for all large even t. So

    a > c/2  ==>  [K_beta <= sum_m W_m for all large even t]  ==>  a >= c/2 = (15).

**Verdict on claim 5. HOLDS AFTER CORRECTION.** Bounding (14) for all large times is "exactly what remains" for (15) only in the trivial sense: it is (15) itself rewritten through the identity (14), equivalent to (15) except when equality holds in (15). It is not a reduction, and the signed-integral form (13) adds no estimate. Correction to L300, L308 and the FINISH RESULT: state the open step as "(15) itself, equivalently J_0(t;2b) <= sum_m J_m(t/2;b) for all large even t at fixed (b, beta)". The file's own caveat (L304: (5a) keeps t fixed while the hypothesis of (15) needs all large t at fixed beta) is correct; the weak-coupling sign in S34 does not reach it, because the threshold beta_0(b,t) may grow with t.

**GUIDE (where (15) sits at weak coupling; not a proof step).** At fixed b and beta -> infinity the minimum c is the periodic block gap (twisted gaps tend to 2 omega > 0, the periodic one to 0, row 1215 (5)). Row 1215 (20) shows that the periodic low-level counting measure, divided by beta^{3/2} log beta, depends on the side n only through nE (density proportional to n^{9/2} E^{7/2} dE = (nE)^{7/2} d(nE)); the reduced constant-mode model of rows 1273/1286 gives a gap kappa g^(2/3)/side. Both say the low periodic spectrum scales exactly as 1/side at leading order, so m_{0,+}(2b)/m_{0,+}(b) -> 1/2 at leading order. That is the equality case of (15). In the one regime where the quantities are computed, (15) is decided by subleading terms, which nothing on file controls.

**Is (14) a restatement of (N-phys)? No; it is genuinely different, and in neither of its uses is it (N-phys) restated.**
1. (14) itself is an algebraic identity (definitions of K, W, J); it asserts nothing.
2. Its large-time sign condition is a restatement of (15): a gap ratio at fixed lattice side and fixed beta, between the doubled periodic box and the eight half-side flux blocks. (N-phys) (`gap-mini-neutral-fable.md` L44-59) is a thermal count at one time u_j <= n_j/512 along the trajectory. Neither implies the other. (15) at every doubling, even granting the twisted blocks, gives only z(2b) >= z(b) for z = side x gap, i.e. a non-decreasing dimensionless gap; (N-phys) needs D_0(n/512;n) - 1 <= 1/2, hence z >= 512 log(2 d_1) (the same threshold check 1287 records), which (15) cannot produce from a small start. Conversely (N-phys) bounds the large box only and says nothing about the twisted half-blocks, so it does not give (15).
3. The single-time use at L306 (time t'_j = 2 floor(n_j/1024)) is a sufficient condition for (N-phys) that is strictly stronger than (N-phys): it needs J_0(t'_j;n_j) <= sum_m J_m(t'_j/2; n_j/2) <= log(3/2), i.e. the seam inequality plus a bound on the product of all eight half-side neutral traces at the same aspect 512 (t'_j/2 = floor(b_j/512)). The arithmetic of L306 checks: log D <= J <= 2 log D; (9/2) log 2 - 2 log(3/2) = 2.308 > 0. GUIDE: in a theory with infinite-volume gap M the half-side traces at time L/1024 have excess about e^{-ML/1024}, larger than the excess e^{-ML/512} that (N-phys) bounds at side L, so this test transfers a harder statement at L/2 to an easier one at L and cannot be iterated down to small physical sizes.

### Step 6. Every remaining statement

**S8 (L87-91), (4). HOLDS.** Volumes: b^3 + 7 sum_{j<k} 8^j b^3 = 8^k b^3. Iterating S7 telescopes the periodic Q_0 factors; (3) gives the ratio N^{9/2} of the two singular prefactors. Fixed hierarchy only, as stated.

**S9 (L93-98), (5). HOLDS.** At fixed t both traces diverge, so the limit is D_0(t;Nb)/B = (Ns/t)^{9/2} Q_0(t;Nb)/[Q_0(s;b) prod P^{powers}]; as t -> infinity all oscillator factors tend to one and Ns/t -> N alpha. The powers are on the twisted factors only (one periodic block, as stated), so beta^{3/2} log beta cancels. The consequences (C_N >= (N alpha)^{9/2}; alpha <= 1/N at coefficient one; c N^3 forces alpha <= c^{2/9} N^{-1/3}; no periodic tile gives a bounded denominator) follow.

**S12 (L119). HOLDS** (fixed-side weak limit). At side L/2 the elementary twist has mu = 2 arsinh sin(pi/L) and twenty levels at 2 mu (row 1215 L159). At u = floor(L/512) >= 3: 20 e^{-4u arsinh sin(pi/L)} >= 20 e^{-4 pi/512} = 19.51 > 1/2; all other normalized traces are >= 1.

**S13 (L125-127). HOLDS.** Row 1215 (16) gives n|log lambda_0^eta - log Lambda_eta| -> 0 uniformly for beta >= n^32, for the periodic and the elementary sign fields; its proof (L278-299) uses the sign pattern only in the "distance to an exact flat" step (L284). L127 supplies that step for every m != 0: after the anticommuting pair is moved within O(s) to (i,j), the third word h satisfies ||(Ad i - e_1)h|| + ||(Ad j - e_2)h|| = O(s); Ad i, Ad j are the commuting involutions diag(+,+,-,-), diag(+,-,+,-) on (1,i,j,ij), each joint eigenspace is one real line, and ||(1 - P_1)h|| = (1/2)||(Ad i - e_1)h|| with commuting projections gives distance O(s) to the line, hence to +-(its unit word). The cap, Taylor and electric estimates (17)-(18) do not see the signs. With the exact identity 3 S_{2b}(0) = sum_m (-log Lambda_m(b)) this gives b Delta_mix -> 0 for beta >= (2b)^32 (which is >= b^32). Row 1215 (19) at n = 2b gives (2b) m_{j,+}(2b,beta) -> 0 for each fixed j, so at time floor(2b/512) any fixed number of levels contributes about one each.

**S14 (L129-133). HOLDS.** Without flips the gauge stabilizer of a twisted flat is {+-1} (a constant fixing i and j exactly is central), acting trivially on normal coordinates; two tubes, each with the unprojected Gaussian trace Q_m(+,+,+); cross terms vanish exponentially; so D_m^all -> 2Q_m. Consistency check (mine): projecting with the eight flips, the four with m.z = 1 swap the tubes and contribute nothing to the trace, the four with m.z = 0 contribute 2 Q_m(epsilon_z), and (1/8) * 2 * sum = P_m, as in S6. D_0^all/D_0 -> 8 is row 1145's fraction 1/8.

**S15 (L135). HOLDS.** 8 D_0(t;2b)/[8 D_0(t;b) prod_{m != 0} 2 Q_m] -> 2^{9/2} Q_0(t;2b)/[Q_0(t;b) 2^7 prod Q_m] = 2^{-5/2} by S7.

**S16 (L139-146), (6). HOLDS.** For T >= 0 commuting with the flips: Tr(P_q T^{2b}) <= [Tr(P_q T^b)]^2 (sum of squares of nonnegative numbers); character orthogonality gives (1/4) sum_z Z_z^2; |Tr(C^z T^b)| <= Tr T^b because C^z is a commuting involution. The averaging consequence: a retained term w Z_0(t;b^3)^8 normalized by the large vacuum grows at rate E_0(2b) - 8E_0(b) = 15A/(2b) + o(1) > 0 (S3), so such bounds cannot produce the cancellation (1). Stated as the file states it (for averages retaining the all-periodic term).

**S17 (L148-161). HOLDS.** With only 12-couplings the 3- and 0-links appear in no weighted plaquette; each (x_3, x_0) slice is an independent two-dimensional Wilson torus: bt slices of area A = b^2 per block, 2bt slices of area 4A for the doubled box. Character expansion: e^{gamma Re U} has coefficient d r_d (normalized), edges give 1/d, vertices d, so Z = sum_d d^{V-E+F} r_d^F = sum_d r_d^A on the torus; one negative face gives (-1)^{d-1}. r_2 ~ gamma/4, r_3 ~ gamma^2/24, r_d <= e^{1/4}(gamma/2)^{d-1}/d! (from I_d(gamma) <= (gamma/2)^d e^{gamma^2/4}/d! and I_1 >= gamma/2). z_+ z_- = (odd)^2 - (even)^2 = 1 + 2 r_3^A - r_2^{2A} + O(gamma^{4A}), so the limit 2(16/24)^A - 1 = 2(2/3)^A - 1 < 0 for A >= 2. Four fluxes have m_3 = 0 and four m_3 = 1, so the mixed product is [z_+(A) z_-(A)]^{4bt} < 1 < z_+(4A)^{2bt}. Continuity in the omitted couplings is fine on a finite lattice.

**S18 (L165-176), (7), (8). HOLDS.** Commuting triple: characters 0, theta, -theta, so mu({0}) >= 1/3 >= (1/2) mu(H^c); noncommuting projectively flat triple: three order-two characters (S1), mu(H^c) = 0; linear in mu. The periodic cover of side Nb resolved by one cell gives phases 2 pi r/N, r in (Z/N)^3, uniformly; d^3 of them lie in H. phi = 1_{0} - (1/2)1_{H^c} has range length 3/2, int phi d mu >= 0, int phi d nu_N = (2 + d^3 - N^3)/(2N^3) < 0 for N >= 3; |int phi d mu - int phi d nu| <= (3/2) sup_A |mu(A) - nu(A)| gives (8). For a twisted parent every child phase is +-pi/2 in a direction where the parent character is odd, so nu(H^c) = 1 and the distance is >= (1/2)/(3/2) = 1/3.

**S19 (L178). HOLDS.** Ideals of su(2)^K are sums of simple factors, so a Lie-algebra isomorphism permutes factors; conjugating a transitive permutation of K > 1 factors into an action fixing every factor is impossible.

**S20 (L180). HOLDS** (local action calculation). Re(A B A^-1 B^-1) = 1 - 2|Im A x Im B|^2 for unit quaternions (check: A = i, B = j gives -1); with Im A = +-sin v i, Im B = +-sin v j the action is 2 sin^4 v on every sheet. A character p carries one colour axis in a block with p in m^perp \ 0, none otherwise, none in the periodic block; so the two p-components commute blockwise, while [chi_p i, chi_p j] = [i,j] has trivial character.

**S21 (L182-186). HOLDS.** X(s) and Y(s) = +-X(s) commute on each sheet. In the block: q + eta and p + eta are not in m^perp (eta is not, p, q are), so X keeps only its p-component and Y only its q-component, on perpendicular colour axes; the block action is 2 sin^2 sin^2 > 0 at small nonzero amplitude.

**S24 (L198). HOLDS** given row 1227 (11) (checked): 7 C_b e^{-c_b beta}/exp[-C_b beta^(1/4)(1+log beta)] -> 0.

**S25 (L200-207), (9). HOLDS** given row 1227 (14) (checked): each periodic electric sector has trace -> 1 at t_beta = floor(exp(beta^gamma)); in a twisted block the charge-m level (S22) has t_beta E <= C exp(beta^gamma - c beta) -> 0, and the two-tube Gaussian limit gives a uniform gap above the first two levels. Diagonal neutrality fixes the periodic charge to sum_{m in I} m for each of the 2^7 subsets I: limit 128; side 2b neutral: limit 1; separate neutrality: limit 1.

**S26 (L211-215). HOLDS.** Cap test: (c beta^{-3/2})^E volume, kernel >= (c' beta^{3/2})^E on cap pairs, beta V <= C on the cap (W <= C dist^2 at its zero), so lambda_0 >= c_{b,W}. W >= 0 keeps V >= V_m off the good neighbourhoods; the electric kernel factorizes over links, so the tail and jump bounds of S22 hold tile by tile. The sixteen trials s_I psi have distinct characters under the separate tile flips, which commute with F, so they are exactly orthogonal in norm and form; min-max gives fifteen levels within O(e^{-c beta}) of the vacuum in the diagonally neutral sector.

**S27 (L217). HOLDS.** On the links a term reads, a flip is an edge-sign cochain whose product around each cycle is (-1)^{winding}; with no odd-winding cycle it is a coboundary g(x)g(y) on each component; the central gauge g reproduces the flip there; gauge invariance of the term finishes.

**S28 (L221-230), (10). HOLDS** (conditional on the stated witness). G(s_2) = sum c_i e^{-s_2 E_i} <= e^{-(s_2 - s_1) m_+} G(s_1) for a centred vector, so m_{+,j} <= L log(1/rho)/(tau n_j). Denominator: row 1227 (11) for m = 0; for m != 0 the gap is positive at every beta (simple vacuum in a compact positive operator), continuous in beta, with positive limit 2 omega, hence bounded below for all large beta; finitely many (b,m). With beta_j = O(log n_j), exp[C_B beta_j^(1/4)(1+log beta_j)] = n_j^{o(1)}.

**S29 (L234-238). HOLDS** (conditional on the witness). D_0(u_j) - 1 >= e^{-u_j m_+} >= exp[-L log(1/rho)/(512 tau)]. Tr(MCM) <= Tr C = I_beta^{-3b^3} (polynomial in beta); the excited trace at s is <= e^{-(s-1)d_j} Tr(F/lambda_0); with s >= eta u_j and d_j >= n_j^{-o(1)}, it is e^{-n_j^{1-o(1)}} times a polynomial; prod(1 + x_i) <= exp(sum x_i).

**S30 (L242-260), (11). HOLDS.** Checked line by line: cap test lambda_0 >= e^{-C_0 b^3}; D_* tail ||1_{D_*^c} phi||^2 <= e^{-H} 4/lambda_0^2 = 1/8 with H = 2C_0 b^3 + log 32; chord error u = sqrt(2H/beta); comb and rectangle filling give link errors C b^2 u and commutation errors b^2 u, so r = C' b^{7/2}/sqrt(beta) is small for beta >= C b^7; S13's projection moves the triple O(r) to a flat, and gauge plus flip bring it to one representative A_m (the flips are needed, since without them there are two orbits); gauge caps cost (c beta^{-3/2})^{b^3}/8; electric cost beta E (r + beta^{-1/2})^2 <= C b^{10}; ||psi||_inf <= e^{C_0 b^3}(C beta^{3/4})^E, whose square cancels the (c beta^{3/2})^E of the kernel bound; Dirichlet integral on D_*^2 >= (7/8)^2 - (1/8)^2 = 3/4. The use of the averaged kernel is legitimate because phi and psi are invariant under gauges and flips.

**S31 (L262-268). HOLDS.** Row 1147 (13) bounds the full periodic gap, which is <= the neutral one. For b <= B_j = o(beta_j^(1/11)): b^8, b^(11/2) sqrt(beta), b^10 and b^3 log beta are all o(beta_j), and beta_j >= C b^7 holds eventually, so (11) applies; with beta_j = O(log n_j) the minimum is n_j^{-o(1)}.

**Labels.** L19 and L306 are correctly OPEN; the arithmetic of L306 is checked in Step 5. GUIDE L25 restates row 1215 L26 correctly; GUIDE L83 and L121 are accurate readings (L121's "inverse-total-side rate" is the 1/N of S9-S10, the same scale-invariant rate that rows 1286/1287 found for sewn blocks). L13 and L15 match the RESULT lines of rows 1273, 1279, 1285, 1286, 1287, 1291, 1292 and row 697's Lemma X. **RESULT L308: HOLDS AFTER CORRECTION.** Its first four sentences hold as checked. Its last sentence should read: the all-large-time bound in (14) is (15) itself restated (equivalent apart from equality in (15)), and it is open at every fixed lattice width, not only at positive physical width.

### Step 7. Numeric guidance run (GUIDE only; never a proof step)

`python3 -E -P`, numpy 2.4.4, BLAS/OpenMP threads 1, outside the repository in a fresh directory under /tmp (script `guide_run.py`, log `run.log` there). Peak resident memory 44 MB; run time under one second. One first attempt had a wrong exponent in my Ewald formula (t^{-1/2} for t^{-3/2}) and two double-precision cancellations; they were fixed before the readings below, which are from the corrected run.

| reading | result | supports |
|---|---|---|
| (a) sum_m lim E_m(b) against 3 S_{2b}(0), b = 3, 4, 5 | equal to 1e-12 relative; each nonzero p lies in exactly three m^perp | S2 |
| (b) sum'_{Z^3} abs(z)^-4 by Ewald | 16.53248, so A = 5.02527 (the 5.025 of row 1285) | S3 |
| (b) b^3 [3S_{2b}(0) - 24S_b(0) - 15A/(2b)], b = 4, 8, 16, 32 | 95.9, 66.0, 59.9, 58.5 (bounded, so the error is O(b^-3)) | S3 |
| (c) log Q_0(t;2b) against log Q_0(t;b) + sum_m log Q_m(t;b), (b,t) = (3,3), (4,5) | equal to 12 digits | S7 |
| (d) log R_2(t), b = 3, t = 6, 8, ..., 60 | all negative, strictly increasing (-1.47 at t = 6, -6.0e-6 at t = 20) | S10 |
| (d) 2 log R_2(t) - log R_2(2t), t = 6, ..., 30 | all negative | S34 |
| (e) lim K_beta at b = 3, t = 3, 4, 6, 10, 20 | 12.96, 6.06, 3.42, 3.124, 3.11916, each above (9/2) log 2 = 3.11916 and decreasing to it; Q_m/P_m in (1, 4) | S32, S6 |
| (f) (z_+ z_- - 1)/r_2^{2A}, A = 4 and 9, gamma = 0.2, 0.05, 0.01 | -0.6036, -0.6049, -0.6049 (predicted -0.6049); -0.9476, -0.9480, -0.9480 (predicted -0.9480); z_+(4A) > 1 | S17 |
| (g) kernel of F_2^7 -> F_2^3 | 16 | S23 |
| (h) 20 e^{-4 pi/512}; (9/2) log 2 - 2 log(3/2); (N^3 - 3)/(3N^3) at N = 3 | 19.515; 2.308; 0.296 | S12, L306, (8) |

No reading disagrees with the file. The run tests the bookkeeping and the limiting formulas; it does not test the Wilson limits themselves (rows 1145, 1215), which rest on their checked proofs.

### Step 8. Counts, verdicts, what was not checked, meaning for the owner's idea

**Counts.** 35 PROVED statements (S1-S35) checked line by line by hand: 35 HOLDS, 0 HOLDS AFTER CORRECTION, 0 FAILS. The RESULT line L308: HOLDS AFTER CORRECTION (its last sentence, which is positive claim 5). Labels: the two OPEN paragraphs are correctly labelled; GUIDE paragraphs read, three of them not checked (listed below). Brief items: claims 1-4 HOLD; claim 5 HOLDS AFTER CORRECTION; (14) is not a restatement of (N-phys).

| # | lines | verdict |
|---|---|---|
| S1 flat colour characters | L27-29 | HOLDS |
| S2 (1), eight sectors cancel the vacuum defect | L31-42 | HOLDS |
| S3 cancelled term 15A/(2b) | L44-49 | HOLDS |
| S4 (2), undercount > 2^(9/2) | L53-60 | HOLDS |
| S5 (3) | L62-67 | HOLDS (input row 1145 (11), checked in row 1146) |
| S6 D_m -> P_m | L69-75 | HOLDS (row 1215 (8) generalized to all seven fluxes; inputs verified here) |
| S7 parity identity | L77-81 | HOLDS |
| S8 (4) | L87-91 | HOLDS |
| S9 (5) | L93-98 | HOLDS |
| S10 (5a), half-time comparison | L100-115 | HOLDS |
| S11 sharpness | L117 | HOLDS |
| S12 last hierarchy level | L119 | HOLDS |
| S13 joint range beta >= (2b)^32 | L125-127 | HOLDS |
| S14 full traces 2Q_m | L129-133 | HOLDS |
| S15 full ratio 2^(-5/2) | L135 | HOLDS |
| S16 (6) and its consequence | L139-146 | HOLDS |
| S17 anisotropic counterexample | L148-161 | HOLDS |
| S18 (7), (8) | L165-176 | HOLDS |
| S19 no exact link multiplication | L178 | HOLDS |
| S20 missed p-p interaction | L180 | HOLDS |
| S21 no local sign repair | L182-186 | HOLDS |
| S22 soft charged state | L190-194 | HOLDS |
| S23 fifteen soft neutral excitations | L196 | HOLDS |
| S24 loss of the one-block gap | L198 | HOLDS (given row 1227 (11), checked) |
| S25 (9), 1 against 128 | L200-207 | HOLDS (given row 1227 (14), checked) |
| S26 interacting class W | L211-215 | HOLDS |
| S27 locality condition | L217 | HOLDS |
| S28 (10) | L221-230 | HOLDS (conditional on the stated witness, as labelled) |
| S29 polynomial multiplicities | L234-238 | HOLDS (same condition) |
| S30 (11) | L242-260 | HOLDS |
| S31 explicit width | L262-268 | HOLDS (input row 1147 (13), checked) |
| S32 seam identity, (12) | L272-285 | HOLDS |
| S33 (13) | L287-292 | HOLDS |
| S34 (14) | L294-298 | HOLDS |
| S35 (15) | L300-304 | HOLDS as an implication; its hypothesis is equivalent to (15) apart from equality (Step 5) |
| RESULT | L308 | HOLDS AFTER CORRECTION: replace the last sentence by "The all-large-time bound in (14) is equivalent to the gap fraction (15) itself, apart from equality in (15); it is open at every fixed lattice width, including positive physical tile width." The same correction applies to the FINISH row 1301 RESULT ("named as the one remaining step"). |

**Verdict on (14) against (N-phys).** Genuinely different, not a restatement. (14) is an identity. Its all-large-time sign condition is (15) restated (a gap ratio at fixed b and beta), not (N-phys) (a thermal count at time n/512 along the trajectory); neither of (15) and (N-phys) implies the other. The single-time test of L306 is a sufficient condition strictly stronger than (N-phys) at that size: it needs the seam inequality and a bound on all eight half-side neutral traces at the same aspect 512.

**Not checked.** (i) GUIDE L3-7 (repo and PR search, registry): not re-run. (ii) GUIDE L17 and L232: the Sussman-Alpoge outline and complete-account line citations, and row 865 with its check (the witness hypotheses and the values of rho, tau): not opened; S28-S29 are checked only as conditional on the stated witness. (iii) The deep inputs were read as statements with their on-file checks and not re-derived: row 1145 (11) and row 1143's limiting integral (behind (3)), row 1215 (3), (8), (16)-(19), row 1227 (11), (14), row 1147 (13). The extensions of these inputs to all seven fluxes were re-derived here (S6, S13, S14). (iv) The GUIDE remark that (15) sits at its equality case at weak coupling is a reading of row 1215 (20) and rows 1273/1286, not a proof. (v) The numeric run (Step 7) guides only.

**What this means for the owner's tiling idea (plain words).**
1. The idea works for the vacuum energy. Blocks turning about non-commuting directions (the seven 't Hooft fluxes) plus one periodic block reproduce the doubled box's ground energy exactly in the weak limit. That includes the Casimir defect 15A/(2b), A = 5.025, that identical tiles cannot pay (S2, S3).
2. It does not carry over to the neutral spectrum at the same time. The product of the eight neutral traces is too small by more than 2^(9/2): the doubled box has constant-field modes that the twisted blocks lack (S4). The comparison holds only at half the observation time, and only for fixed boxes at very weak coupling (S10).
3. Tilings that keep each tile's own centre flips have fifteen exponentially soft neutral states and lose the gap. This covers independent tiles and tiles coupled only through contractible observables (S23, S26, S27). Only genuine cross-face Wilson plaquettes, which break the separate tile flips, escape this.
4. The step that row 1301 names as remaining is not a reduction. At fixed lattice side and coupling, "the seam integral (14) is bounded for all large times" is the gap inequality (15) itself, apart from the equality case.
5. Even if (15) were proved at every scale, it loses a factor 1/2 per doubling. That is the same scale-invariant rate 1/N that rows 1286/1287 found for sewn blocks. It keeps side x gap from decreasing, but it cannot raise it to the size (N-phys) needs (at least 512 log 2). At weak coupling the binding block in (15) is the periodic one, not the non-commuting ones, and (15) sits exactly at its equality case there (GUIDE).
6. So the non-commuting directions fix the vacuum-energy bookkeeping, but not the gap. On the record now, no estimate carries a fixed fraction of a one-block neutral gap to the physical box, and the route's open step is equivalent to its goal. Nothing here proves that no tiling can work.

RESULT (2026-11-20 17:02Z, anthropic/claude-opus-5-5/max laptop-subagent): check of row 1301 (gpt-6.2-astra, owner's tiling route) by hand: 35 of 35 PROVED statements HOLD, 0 FAIL; positive claims 1-4 hold as stated (exact eight-sector cancellation of the weak-limit vacuum defect 15A/(2b); neutral undercount factor 2^(9/2) prod Q_m/P_m > 2^(9/2); fifteen soft neutral excitations under diagonal neutrality, also for tile-flip-preserving W; half-time comparison at fixed boxes and large beta); RESULT L308 HOLDS AFTER CORRECTION: the all-large-time bound on (14) is equivalent to the gap fraction (15) itself apart from equality, so it is not a reduction; (14) is not a restatement of (N-phys) (identity; large-time form = (15), single-time form strictly stronger than (N-phys)); the tiling route has no remaining reduction toward the gap; mass gap OPEN.
