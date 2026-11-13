# FINISH row 863, gap-crux-skeleton-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

## Header

- Row: FINISH 863. Author: Claude Fable 5.2, max effort. Date: 2026-11-12.
- Clone commit (read-only, branch claude/ym4d-hard-route): 2b6acd1732dde4e18293f0fe0e2814edbca36da3.
- Sussman-Alpoge account: YM4_1400 at 2bc0658f91d2; sources on disk at /Users/jonreilly/ym4d-lead/sa (commit 31a47c543775). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Credit Balaban for his estimates.
- Marks used: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE (numeric, never discharges), OPEN.
- Rule: one step per response; each step is appended here before the next starts.

## Target statement

Mass gap for four-dimensional SU(2) lattice Yang-Mills, uniform in the cutoff.
The Sussman-Alpoge renormalization steps reach a first-passage effective action at order-one effective coupling.
The crux is control at that coupling. Sharpest forms: the twist deficit 1 - Z^(m+v)/Z^m (centre-vortex free energy), or the seed (SEED-FP) on the first-passage effective action at one physical size, uniformly in the cutoff.
No fixed small coupling finishes the proof.

## Plan (eight steps at most)

1. Own skeleton S0: a numbered chain from the first-passage action to the gap, through the crux. Written before any lane file is read.
2. Split the crux node into single-estimate lemmas. Name the node that carries the difficulty.
3. Attack 1 on that node, one stage per response. Record exactly where it stops.
4. Reshape the skeleton so the difficulty moves to an attackable statement. Attack 2.
5. Attack 3 (and further stages) on the reshaped node.
6. Only then: read gap-assume-opus.md (row 838), gap-skeleton-final.md Section 13, FINISH rows 830-862 by grep. Compare node by node.
7. Correct the skeleton with what the lane already has. Say what is new here.
8. Final skeleton with statuses, the one or two next statements, and the RESULT line.

## Step 1. Own skeleton S0 (written before any lane file except gap-finishline-opus.md L38-172, which the brief names as the statement of the crux)

### 1.0 Reading state at this point

- READ D/library/gap-finishline-opus.md L38-172 only (sections 1 and 2). Every "READ lane" mark below points there.
- Not read yet: gap-assume-opus.md, gap-skeleton-final.md, FINISH rows. They come at Step 6.

### 1.1 Objects (fixed notation of this file)

- G = SU(2). Torus Lambda = Z_(n_1) x Z_(n_2) x Z_(n_3) x Z_(n_4). Weight exp(-S), S = beta * sum over plaquettes p of (1 - (1/2) tr U_p).
- Twist: z in H^2(Lambda; Z_2) = Z_2^6, one bit per coordinate plane. Z^z = integral of exp(-beta sum_p (1 - (1/2) z_p tr U_p)), with z_p = -1 on one co-closed stack of plaquettes per twisted plane. Z = Z^0.
- Time = direction 4. Spatial box B = n_1 x n_2 x n_3. H_B = L^2 of the spatial links, gauge-invariant part. T_B = transfer operator. Eigenvalues lambda_0 > lambda_1 >= ... > 0.
- Centre operators C_i (i = 1, 2, 3): multiply by -1 every link in direction i that crosses one fixed hyperplane. They commute with T_B. H_B = direct sum over e in Z_2^3 of H_e (electric flux e). "Even sector" = H_0.
- Thermal sums: S(t; B) = Tr T_B^t / lambda_0^t - 1. S_ev(t; B) = Tr_(H_0) T_B^t / lambda_0^t - 1.
- k in Z_2^3 = twist in the planes (4, i) ("temporal"). m in Z_2^3 = twist in the planes (i, j) ("spatial", a magnetic flux; it changes the operator to T_(B,m)).

### 1.2 The chain

N1. (READ lane 1.1-1.4; Sussman-Alpoge, with Claude and Codex.) First-passage data (K, beta), beta in W_K(g), bare spacing a_K = L^(-K). The unit-lattice density rho_K has total mass Z_(K,ell,beta) exactly. Its action is the Wilson action of the background at x_K in (g^(-2), g^(-2) + B_sharp], plus local terms, plus large-field terms. The reference coupling g is at most a small ceiling gamma_H. The last integral is known only to e^(O(ell^4)).

N2. (Standard theorem: Osterwalder-Seiler 1978, Luescher 1977; the lane's (TM), READ lane 2.1 as checked.) T_B is positive, self-adjoint, trace class. Z(t x B) = Tr T_B^t. For temporal twists: Z^k(t x B) = sum over e of (-1)^(k.e) Tr_(H_e) T_B^t. The vacuum lies in H_0 (Perron-Frobenius).

N3. (PROVED here, two lines.) Put p_0(t; B) = Tr_(H_0) T^t / Tr T^t. Then
  (a) p_0 = (1/8) sum over k in Z_2^3 of Z^k/Z, so 1 - p_0 = (1/8) sum over k of (1 - Z^k/Z): the mean temporal twist deficit;
  (b) 1 + S = (1 + S_ev)/p_0.
Proof. (a) Fourier inversion on Z_2^3 applied to N2. (b) Tr T^t = Tr_(H_0) T^t / p_0 and Tr_(H_0) T^t = lambda_0^t (1 + S_ev). QED.
So the seed quantity splits exactly into a flux part (p_0) and an even part (S_ev).

N4. (PROVED here, three lines.) Doubling form. For every t and B:
  Z(t x B)^2 / Z(2t x B) = (1 + S(t))^2 / (1 + S(2t)), and 0 <= S(2t) <= S(t)^2.
Hence 1 + 2S(t)/(1 + S(t)^2) <= Z(t)^2/Z(2t) <= (1 + S(t))^2. So S(t) is small if and only if D(t; B) := 2 log Z(t x B) - log Z(2t x B) is small: for D <= 1/10, S(t) <= D (from 2S/(1+S^2) <= e^D - 1 and S <= 1).
Proof. Z(t) = lambda_0^t (1 + S(t)). S(2t) = sum of r_i^(2t) <= (sum of r_i^t)^2 with r_i = lambda_i/lambda_0 in (0,1]. QED.
Same statement, other words: with rho_t = T^t / Tr T^t, Z(2t)/Z(t)^2 = Tr rho_t^2. The seed says the Gibbs state at inverse temperature t on the box B is pure to within 2 s.

N5. (PROVED here; identity.) Thermodynamic form. D(t; B)(beta) = integral from 0 to beta of [2 <A>_(t x B, b) - <A>_(2t x B, b)] db, A = sum over plaquettes of (1/2) tr U_p, because D = 0 at beta = 0 (Z = 1 for the normalised Haar measure and the weight exp(beta A - beta #p); the constant cancels in D). So D is the integrated finite-size shift of the mean plaquette, times the number of plaquettes.

N6. CRUX. (SEED-FP), READ lane 2.2: one physical size ell, s_* < 1/5041, and S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_* for every first-passage datum with K >= K_0. NEW, OPEN. Split in 1.3.

N7. (READ lane 2.1: Theorem S, Corollary S3', Theorem SH; checked rows 698, 699, 707.) A seed at one size gives gap >= log(1/(5041 s))/N on every larger cube, at the same cutoff. It uses only N2 and exchange of axes. It holds for every group.

N8. (READ lane 2.5 (a)-(f): PROVED/READ/ARGUED as marked there.) A seed uniform in the cutoff gives (GAP) for every volume-first limit: ker H = C Omega, spec H in {0} union [M_*, infinity), M_* = 2 log(1/(5041 s_*))/ell.

### 1.3 First split of the crux N6 (by content)

By N3 (b), (SEED-FP) at (t, B) = (ell/(2a_K), (ell/a_K)^3) follows from three statements. Each is one inequality on one quantity at one physical size, uniform in K >= K_0.

- C-a (FLUX). For each of the seven k != 0: 1 - Z^k/Z <= s_a. Then 1 - p_0 <= (7/8) s_a.
- C-b (EVEN GAP). In H_0: lambda_1/lambda_0 <= exp(-mu a_K), mu > 0 in physical units.
- C-c (EVEN MULTIPLICITY). At the earlier time t_0 = t/2: S_ev(t_0; B) <= M.
Then S_ev(t; B) <= M exp(-mu ell/4) (each ratio r_i^t = r_i^(t_0) r_i^(t - t_0) <= r_i^(t_0) r_1^(t_0)), and 1 + S <= (1 + M exp(-mu ell/4))/(1 - (7/8) s_a).

Physical reading (GUIDE, not used in a proof): with t = n, B = (2n)^3, log(1 + S) = (pressure at temperature 1/n) x 8 n^4. The seed asks p(T)/T^4 <= about 2.5e-5 at one temperature T. Glueball-gas value: T about m/11.5, near half the deconfinement temperature. C-c asks only p(T)/T^4 <= (log M)/64 at twice that temperature. The Stefan-Boltzmann value is 0.66, so M = e^42 is the natural a-priori size; then C-b needs mu ell >= 4 (42 + 9), a box of about 200 correlation lengths. C-a is the string-tension statement at that size.

### 1.4 Second split (by scale): where the difficulty sits

Along first passage the three quantities are functions of the physical size ell only (plus cutoff corrections). Three regimes.

- ENTRY (ell of the order of the first-passage unit, g <= gamma_H). The account controls the effective action here. The seed quantities are not small here: the theory looks like three free gluons plus zero modes, S is of order one or larger (ARGUED; the U(1) value is of order one: twelve lowest photon modes at weight e^(-pi)).
- WINDOW (from there up to the size where S < 1/5041). The running coupling goes from g to order one and beyond. Nothing is controlled. NEW, OPEN.
- EXIT (beyond). N7 carries the seed to every larger size. PROVED in the lane.

**The node that carries the whole difficulty: WINDOW.** In one sentence: prove C-b and C-c (and C-a) at one physical size where no parameter is small, for the measure that the renormalization steps deliver, uniformly in the cutoff.

Three structural facts that any proof of WINDOW must respect (ARGUED; they shape the attacks below):

- F1. Positivity of T (N2) and symmetry alone cannot give WINDOW. U(1) at weak coupling has N2 and no seed at any size. So a proof must contain one estimate of a quantity of the actual SU(2) measure at order-one coupling.
- F2. No statement of the form "the seed quantity improves under doubling" follows from N2 plus asymptotic freedom at the entry. Guide example (physics lore, not a theorem): SU(2) with two adjoint Dirac flavours is believed asymptotically free, reflection positive, centre symmetric, and scale invariant in the infrared. So the estimate must be made inside the window, not extrapolated from the entry.
- F3. In the window the bare Wilson correlation length is about one lattice spacing (GUIDE: beta_W 2.3 to 2.6), yet no expansion parameter is small: the character ratio I_2(beta)/I_1(beta) is about 0.5, the mean plaquette about 0.6. Worst-case criteria stop near beta = 1 because a frozen abelian background orders there (the brief's fact tests). So the estimate must be an average over the actual measure, not a supremum over backgrounds.

What SU(2) has that the test groups lack (to be used, per the fact tests): against U(1), a non-abelian Lie algebra and positive Ricci curvature of the group; against Q_8 and 2T, a continuous group (integration by parts on the group, Schwinger-Dyson identities, arbitrarily small rotations, characters of all spins; 2T agrees with SU(2) on all polynomial averages of degree at most 5).

## Step 2. Fine split of WINDOW into single estimates; the node chosen for attack

### 2.1 Four exact identities for the seed quantity (all PROVED here; each is a few lines)

Let B be fixed, T = T_B, r_i = lambda_i/lambda_0, Omega > 0 the vacuum, nu = Omega^2 dU the law of one time slice (mod gauge) under the infinite-time measure on Z x B.

I1 (slice chain). P f := Omega^(-1) T(Omega f)/lambda_0 is a self-adjoint Markov operator on L^2(nu) with P1 = 1 and spectrum {r_i}. Write T = e^(-V/2) K e^(-V/2), K = (product over spatial links of the one-link kernel k) composed with the gauge projection, V = -beta sum over spatial plaquettes of (1/2) tr U_p. With g := e^(-V/2) Omega one has K g = lambda_0 e^(V) g and
  P(U, dU') = K(U, U') g(U') dU' / (K g)(U).
So the slice chain is the product kernel K tilted by g at the arrival point (a Doob transform). Proof: substitute. QED.

I2 (chi-square form). Let p_s(U, U') be the density of P^s with respect to nu. Then
  S(2s; B) = integral of (p_s(U,U') - 1)^2 nu(dU) nu(dU') = chi^2( law of (slice 0, slice s) || nu x nu ) = E_(U ~ nu) [ chi^2( P^s(U, .) || nu ) ].
Proof: p_s(U,U') = sum over i of r_i^s phi_i(U) phi_i(U') in an orthonormal eigenbasis of L^2(nu), phi_0 = 1; integrate the square. QED.
So the seed S(n; (2n)^3) <= s_* says: two whole time slices at distance n/2 are independent to within chi^2 <= s_*. Equivalently: started from a nu-typical slice, the slice chain is within chi^2 <= s_* of stationarity after n/2 steps, on average over the start. The average is over the actual measure, not a supremum over starts.

I3 (swap twist). On H x H let SWAP exchange the factors. Then Z(2t x B)/Z(t x B)^2 = Tr((T x T)^t SWAP)/Tr((T x T)^t) = Tr rho_t^2, and 1 - Tr rho_t^2 = 2 Tr_(antisymmetric)(T x T)^t / Tr (T x T)^t. So the thermal part of the seed is a twist deficit too: the deficit of the temporal replica-swap twist of the doubled system. The flux part is the deficit of the temporal centre twist (N3). Both are "probability of the odd sector of a Z_2 symmetry in a thermal trace".

I4 (kernel-ratio form of the centre deficit). Take time along direction 1. For k = the twist of the plane (1,2): Z^k/Z = E[ k_orb([A], [C_2 A']) / k_orb([A], [A']) ], where (A, A') are two adjacent slices under the periodic measure, k_orb(A, A') = integral over gauge transformations h of the product over spatial bonds b of w(h_x A'_b h_y^(-1) A_b^(-1)) is the one-step kernel between gauge orbits, and C_2 flips the sign of the direction-2 links across one hyperplane. Proof: Z^k = Tr(T^(n_1) C_2); write the trace as an integral over slices and insert C_2 in one step. QED.
Read as a spin model: given the two slices, the links that join them form a three-dimensional SU(2) x SU(2) chiral model (an O(4) model) in the background (A, A'), and Z^k/Z is the mean of its antiperiodic-to-periodic ratio. The supremum over backgrounds is attained at pure-gauge backgrounds, where the model is the plain O(4) model; that is where the worst-case cap 4 G_3 of the brief comes from (ARGUED; the brief states the cap as checked in row 839).

### 2.2 The fine split

WINDOW at one physical size, uniformly in the cutoff, is the conjunction of:

- W-fl (centre deficit; one estimate). For each k != 0: E[1 - k_orb([A],[C_k A'])/k_orb([A],[A'])] <= s_a. (Form I4.)
- W-gap (one estimate). The slice chain P contracts on the even sector: ||P f||_(L^2(nu)) <= e^(-mu a) ||f|| for f even, nu(f) = 0. (Form I1.)
- W-hs (one estimate). The even part of the kernel of P^(s_0) is Hilbert-Schmidt with norm^2 at most 1 + M at s_0 = n/4. (Form I2 at a shorter time.)

W-gap and W-hs together give the even part of the seed (1.3). W-hs is not a soft statement: for a box much larger than the time s_0 it is the pressure at temperature 1/(2 s_0), so it sits in the window too.

**Node chosen for attack: the thermal part (W-gap with W-hs), in the single form I2: chi^2 between slices at distance n/2 is at most s_*.** Reason: U(1) fails it and Q_8, 2T pass it at large beta (they are gapped in the even sector); the flux part W-fl is where Q_8 and 2T fail. So the two fact tests separate the two parts: the thermal part needs the non-abelian input, the flux part needs the continuity input.

### 2.3 What an attack on the thermal part must contain (pre-registered)

By I1 the one-step law of the next slice given the present slice U is the Gibbs measure mu_U(dU') proportional to g(U') times the product over links of k(U_l^(-1) U'_l). The chain contracts if the map U -> mu_U does. Its linear response is beta times the covariance of the links under mu_U. For a free massless field the response at momentum q is e^(-omega(q)), which tends to 1 as q -> 0. So a proof must show that, for nu-typical U, the long-wavelength response of mu_U is bounded away from 1 by a non-abelian effect, at a size where nothing is small. Fact-test check of the target: for U(1) the response tends to 1 (no gap), so the bound must use the commutator terms; a bound that uses only a finite set of moments of degree at most 5 would hold for 2T as well, where the even sector is gapped anyway, so 2T does not test this part.

## Step 3. Attack 1 on the thermal part: integrate the seed along a path from a solvable seeded model

Idea. Split the coupling: beta_t on the time-like plaquettes (it enters K), beta_s on the space-like plaquettes (it enters V). At beta_s = 0 the model is solvable and seeded at every beta_t. Then move beta_s from 0 to beta_t and track the seed quantity. The path stays at the target beta_t all the way, so it never passes through small beta_t.

### 3.1 Lemma A1 (sector bound for the electric part; PROVED)

Normalise the one-link kernel k so that its eigenvalue on the spin-j functions is u_j = I_(2j+1)(beta_t)/I_1(beta_t) (u_0 = 1 > u_(1/2) > u_1 > ...). Let H_odd be the sector with electric flux 1 in direction 2, box side n_2 in that direction. Then K restricted to H_odd is at most u_(1/2)^(n_2) as an operator.
Proof. In the Peter-Weyl basis each spatial link carries a spin j_b and K multiplies by the product of u_(j_b). C_2 multiplies by (-1)^(sum of 2 j_b over the direction-2 bonds that cross one hyperplane x_2 = c), for each of the n_2 hyperplanes (all choices of c give the same operator on gauge-invariant states). On H_odd each hyperplane is crossed by at least one bond with j_b >= 1/2. The n_2 hyperplanes cross disjoint bond sets. QED.
Remark. A1 holds for every group with a Z_2 in its centre (U(1), Q_8, 2T included). So it cannot give W-fl alone: V moves flux and can lower the cost. It is the exact form of "electric flux costs electric energy".

### 3.2 Lemma A2 (the electric-only model is seeded at every beta_t; PROVED)

Let beta_s = 0. Then lambda_0 = 1, and for every box B (a torus with sides >= 4) and every t >= 1:
  1 + S(t; B) = integral over h in G^(sites of B) of the product over bonds <xy> of [1 + sum over j >= 1/2 of u_j^t chi_j(h_x) chi_j(h_y)].
Put eps_t = sum over j >= 1/2 of (2j+1)^2 u_j^t. If 10 e eps_t <= 1/2, then S(t; B) <= exp(6 (10e)^3 eps_t^4 |B|) - 1.
Proof. T = K Pi_G (Pi_G the gauge projection), K1 = 1, so lambda_0 = 1 and S = Tr(K^t Pi_G) - 1. The kernel of K^t on a bond is sum over j of (2j+1) u_j^t chi_j; Tr(K^t Pi_G) = integral over A and h of the product over bonds of that kernel at h_x A_b h_y^(-1) A_b^(-1); the A_b integral gives sum over j of u_j^t chi_j(h_x) chi_j(h_y) (orthogonality: integral of chi_j(a A b A^(-1)) dA = chi_j(a) chi_j(b)/(2j+1)). Expand the product over bonds into subsets Gamma. A site of degree 1 in Gamma integrates to 0. In Z^3 a bond set with all degrees >= 2 has at least 4 bonds per component (sides >= 4 exclude shorter winding cycles). Each factor is at most eps_t in absolute value. The number of connected bond sets with n bonds through a given bond is at most (10e)^(n-1) (each bond has 10 neighbours). So 1 + S <= exp(3|B| sum over n >= 4 of (10e)^(n-1) eps_t^n) <= exp(6 (10e)^3 eps_t^4 |B|). QED.
Numbers (by hand, Bessel values I_1(2.5) = 2.5167, I_2(2.5) = 1.2765): at beta_t = 2.5, u_(1/2) = 0.5072. At t = 15 and B = 30^3: eps_t is about 4 u_(1/2)^15 = 1.5e-4, and S <= 6 x 2.0e4 x 5.1e-16 x 2.7e4 = 1.7e-6 < 1/5041. For general beta_t, u_(1/2) is about 1 - 3/(2 beta_t), so the seed time is of order beta_t log beta_t.
Remark. The same holds for U(1), Q_8 and 2T at beta_s = 0. Along the path in beta_s, U(1) meets a Coulomb transition and 2T a freezing transition; SU(2) is believed to meet none. So the path statement below is exactly where the fact tests bite.

### 3.3 The path identity (PROVED; Feynman-Hellmann)

For fixed beta_t, t, B put G(b) = log(1 + S(t; B)) at beta_s = b. Then
  G(beta_s) = G(0) + integral from 0 to beta_s of Delta(b) db, Delta(b) = sum over the space-like plaquettes p of the t x B torus of [ <(1/2) tr U_p>_(t x B) - <(1/2) tr U_p>_(infinity x B) ],
both means at (beta_t, b). Proof: log Z(t x B) = t log lambda_0 + G; d/db log Z = sum of <(1/2) tr U_p> over space-like p; d/db log lambda_0 = nu-mean of the one-slice sum (T = e^(-V/2) K e^(-V/2), V linear in b). QED.
So the thermal seed at the isotropic point is: G(0) + integral of Delta <= log(1 + s_*). G(0) is A2. Delta(b) is the finite-temperature shift of the space-like plaquette, summed over the torus.

### 3.4 Where Attack 1 stops

(SHIFT). Needed: integral over b in [0, beta_t] of Delta(b) <= about 2e-4, for t x B = n x (2n)^3.
- For b <= b_0(beta_t) small, an expansion in b about the electric-only model gives Delta(b) exponentially small in t (ARGUED; anisotropic strong coupling; it converges when b times beta_t is small).
- For b in [b_0, beta_t]: Delta(b) small is "the n x (2n)^3 torus and the infinite-time cylinder have the same space-like plaquette mean to within 2e-4/(number of plaquettes)". This is decorrelation of slices at distance n/2 again, now at every coupling (beta_t, b) of the path. Nothing bounds it. STOP.
- What the attack gained: (i) an exactly seeded reflection-positive SU(2) model at the target beta_t (A2); (ii) the crux as absence of a transition along a one-parameter path, in quantitative form (SHIFT); (iii) the fact tests localised on that path.
- What it did not gain: any estimate inside the window. (SHIFT) is W-gap and W-hs in differential form. The difficulty did not move.

Fact tests on Attack 1: it does not prove the seed for U(1) or 2T (it stops before using any SU(2) property). It respects F1-F3. It does not finish.

