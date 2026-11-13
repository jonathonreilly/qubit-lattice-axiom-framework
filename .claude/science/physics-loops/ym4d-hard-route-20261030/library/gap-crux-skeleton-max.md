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


## Resumed 2026-11-13 after the 03:06Z interrupt

- Clone commit now: 9f1e04272b03270994c98fb4b9716e071924bac4 (git pull --ff-only: already up to date). The header commit 2b6acd17 was the clone state of the first run.
- State found on disk: Steps 1, 2 and 3 are finished (skeleton S0, identities I1-I4, fine split, pre-registered requirements, Attack 1 with its stop at (SHIFT)). They are not redone.
- Remaining plan (one step per response, each appended before the next):
  - Step 4. Reshape the skeleton so the difficulty moves off (SHIFT) to a statement with a real handle. Attack 2 on that statement, one stage per response (4a, 4b, ...). Record exactly where it stops.
  - Step 5. Attack 3 on the next reshaped node (again staged), if Attack 2 stops.
  - Step 6. Only then: read D/library/gap-assume-opus.md (row 838), D/library/gap-skeleton-final.md Section 13, FINISH rows 830-862 by grep, and the RESULT lines of FINISH rows 860-875. Compare node by node.
  - Step 7. Correct the skeleton with what the lane has. Say what is new here.
  - Step 8. Final skeleton with statuses, the one or two next statements, the RESULT line.

## Step 4. Reshape R1 and Attack 2: the thermal part as a property of the slice law alone

Attack 1 put the difficulty on a path in the coupling (SHIFT). A path statement is circular: "the gap does not close along the path" is the claim itself (4.5 below makes this exact). R1 moves the difficulty to a statement about one measure at the target coupling: the law nu of one time slice.

Notation as in 1.1 and 2.1. beta_t sits in the one-link kernel w(g) = exp(beta_t (1/2) tr g) / c(beta_t); b = beta_s sits in V. k_orb is the orbit kernel of I4. N_b = 3|B| is the number of spatial bonds.

### 4.1 Lemma B1 (bridge form of the two-slice law; PROVED, uniqueness is a standard theorem)

The joint law of two adjacent slices under the infinite-time measure is
  pi(dU, dU') = a(U) k_orb(U, U') a(U') dU dU',  a = e^(-V/2) Omega / sqrt(lambda_0).
Both marginals are nu. Proof: pi = Omega(U) T(U,U') Omega(U') / lambda_0 and T(U,U') = e^(-V(U)/2) k_orb(U,U') e^(-V(U')/2). QED.
Standard theorem (Beurling 1960; Csiszar 1975): for a continuous strictly positive kernel on a compact space, a coupling of two given marginals of the form a x a' x kernel is unique. So pi is the static Schroedinger bridge from nu to nu with reference kernel k_orb.
Consequence. The whole spectrum {r_i} of the slice chain P is a function of the pair (k_orb, nu). The magnetic coupling b enters the thermal part only through nu. (k_orb depends on beta_t only.)

### 4.2 Lemma B2 (a gap bound that does not see the magnetic term; PROVED from Hopf's theorem)

Hopf's theorem (E. Hopf 1963; Birkhoff 1957): an integral operator with continuous kernel T(x,y) > 0 on a compact space, with cross-ratio bound kappa = sup T(x,y) T(x',y') / (T(x,y') T(x',y)), has |lambda| <= tanh((log kappa)/4) lambda_0 for every eigenvalue lambda other than lambda_0.
The cross-ratio of T(U,U') = e^(-V(U)/2) k_orb(U,U') e^(-V(U')/2) does not contain V. Each bond factor of k_orb lies in [e^(-beta_t), e^(beta_t)]/c, so kappa <= e^(4 beta_t N_b). Hence, for every b >= 0, every box B, and every compact group:
  r_1 <= tanh(3 beta_t |B|),  E_1 = -log r_1 >= 2 exp(-6 beta_t |B|).
Reading. In a fixed finite box the gap never closes along the whole path b in [0, infinity), with a bound uniform in b. The bound is extensive in the exponent, so it says nothing at the seed size (|B| = 27000 gives exp(-4 x 10^5)). It holds for U(1), so its decay with |B| is forced. It is the worst case over pairs of slices; an average over nu-typical pairs is what the seed needs (I2).

### 4.3 Lemma B3 (increment form of the gap; PROVED, standard)

P is self-adjoint and non-negative on L^2(nu). So
  1 - r_1 = inf over f with nu(f) = 0 of E_pi[(f(U') - f(U))^2] / (2 Var_nu(f)).
(INC). W-gap at rate mu is the statement: Var_nu(f) <= C E_pi[(f(U') - f(U))^2] for every slice function f in the even sector, with 1/(2C) = 1 - e^(-mu a).
In words: no gauge-invariant function of one slice has a variance much larger than its mean-square change over one time step. In temporal gauge U'_l = U_l W_l with W_l the time-like plaquette over the link l, so the change is a kick by the electric field.
Continuous-time form (standard, ground-state transform): gap(H) = (1/2) inf of (integral of |grad f|^2 d nu) / Var_nu(f). The gap is half the Poincare constant of nu for the electric Dirichlet form.
Gaussian check (PROVED by direct computation in one mode): for nu = N(0, sigma) and a Gaussian kernel of variance eps, the bridge has correlation r = sqrt(1 + (eps/(2 sigma))^2) - eps/(2 sigma). So E_1 is about eps/(2 sigma) for a soft mode. The gap is small exactly when the vacuum has a collective coordinate of large equal-time variance. For the photon sigma(k) = 1/(2|k|), which is unbounded; (INC) fails for U(1) through the long-wavelength modes, as it must.

### 4.4 Attack 2: prove (INC) from the curvature of SU(2)

What SU(2) has: Ricci curvature 1/2 per link in the units where the Casimir is j(j+1). U(1) has 0. Q_8 and 2T have no tangent space.
Standard theorem (Bakry-Emery 1985; Lichnerowicz): if nu = e^(-phi) on a manifold with Ric + Hess phi >= kappa > 0 at every point, then the Poincare constant of nu is at least kappa, with no dependence on the dimension.
- At b = 0: nu is Haar measure, phi = 0, kappa = 1/2. The criterion gives gap(H_el) >= 1/4 in every volume. (True value 3/2 on gauge-invariant states: four links at j = 1/2.)
- At b > 0: phi = -2 log Omega. Needed: Hess(-2 log Omega) >= -(1/2 - kappa) at every slice configuration, uniformly in the volume.
- STOP 1. No pointwise information on Hess log Omega is available away from small b. The same pointwise demand on the four-dimensional action fails at once: by direct computation (PROVED, for one plaquette p with holonomy cos(theta) + i sin(theta) n.sigma and tangent vectors x, y on two of its links, y' = y transported to the base point)
    Hess S_p (x, y) = (beta/4) [ cos(theta) x.y' - sin(theta) n.(x cross y') ],  Hess S_p (x, x) = (beta/4) cos(theta) |x|^2  (tangent vector X = i x.sigma/2, |x| the Euclidean norm; S_p = -(beta/2) tr U_p),
  the off-diagonal sum over the 18 neighbouring links is about 18 beta/4 = 11 at beta = 2.5 against Ric = 1/2. This is the known strong-coupling range of the Bakry-Emery argument (beta below about 0.1). It is a worst-case criterion.
- The averaged form of the criterion is exact but is not a handle: gap >= lambda if and only if the Witten Laplacian on exact 1-forms, nabla* nabla + Ric + Hess phi, is >= lambda. That is the same spectral problem.
- One trick tried and refuted. The commutator part of Hess S is weighted by sin(theta_p) n_p, which is the gradient of S_p along a link, so one may hope to integrate it by parts into a term without beta. It fails: the Gibbs measure integrates by parts only the full gradient (the sum over the six plaquettes at a link), and the Hessian contains each plaquette's own term. The remainder is of order beta times the field strength, about sqrt(beta) per link.
- STOP 2. A pointwise curvature bound is false in the window; an averaged one is the problem itself.

### 4.5 Why a path in the coupling cannot carry the difficulty (PROVED, a remark on Attack 1)

Feynman-Hellmann on the path of 3.3: d E_i / d b = <N>_i - <N>_0 with N = sum over the spatial plaquettes of one slice of (1 - (1/2) tr U_p) >= 0, taken in the eigenvectors of T. If |<N>_1 - <N>_0| <= C E_1 on [0, b_1] uniformly in B, then E_1(b; B) >= E_1(0; B) e^(-C b) by Gronwall, and E_1(0; B) = -4 log u_(1/2). Conversely a positive differentiable E_1 has such a C at each b. So the virial inequality with a locally bounded C is equivalent to the absence of a critical point; it is a restatement, not a reduction. Tree-diagram bounds of the Aizenman type would give d(m^2)/db >= -c at best, which allows m to reach zero at finite b.

### 4.6 Two tempting flux lemmas that are false (ARGUED; they close two side doors)

- "Electric flux costs at least the Coulomb energy g^2 n_2/(n_3 n_4)". False for SU(2): in a small periodic box the Z_2 flux energy is exponentially small in 1/g (tunnelling between toron valleys; Luescher, van Baal). So no Gauss-law lower bound on the flux energy exists; A1 cannot be upgraded this way.
- "Spread the centre twist over a thick sheet by a measure-preserving change of variables, at a cost of order beta times (sheet area)/(transverse area)". This is the abelian Mermin-Wagner construction. For SU(2) the rotation axis must be covariantly constant along the sheet and across it. The cost of the best axis is beta alpha^2 times the lowest eigenvalue of the adjoint covariant Laplacian of the background on a three-dimensional slab, which is of order one per site in a rough background. So the cost is extensive. Also, in four dimensions the classical cost at a symmetric box is scale-invariant (beta pi^2/2), so no logarithm helps.

### 4.7 Where Attack 2 stops, and what moved

- Gained: (B1) the thermal part depends on b only through nu; (B2) a b-uniform, finite-volume gap bound from the cancellation of V in cross-ratios; (B3) the exact variance-increment form (INC); (4.5) the path form is a restatement.
- Not gained: any volume-uniform estimate in the window.
- The difficulty did not shrink. It now sits in one sentence about one measure: nu has no gauge-invariant collective coordinate with equal-time variance much larger than its one-step increment. What is known about nu without the answer: it is the slice marginal of a reflection-positive measure. Step 5 uses exactly that.
- Fact tests: U(1) fails (INC) through soft photons (4.3). Curvature is absent in U(1), Q_8, 2T (4.4). B2 holds for all groups and is extensive, as it must be.

## Step 5. Reshape R2 and Attack 3: the whole seed as one number of the torus

R1 kept the split into a thermal part and a flux part. R2 removes the split. It uses only what is known about nu without the answer: reflection positivity in every direction and the symmetry of the action under exchange of axes.

### 5.1 Lemma T1 (symmetric form of the seed; PROVED)

For an isotropic reflection-positive action put p(n_1, n_2, n_3, n_4) = log Z(torus) / (n_1 n_2 n_3 n_4). Then:
 (a) p is symmetric in its four arguments;
 (b) p is non-increasing in each argument;
 (c) p_inf := inf over all tori = the limit as all sides grow, in any order;
 (d) with F(n) := log Z(n^4 torus) - n^4 p_inf >= 0:  S(n; (2n)^3) <= exp(8 F(n)) - 1.
Proof. (a) Relabel the axes. (b) Z = sum over j of lambda_j^(n_1) with lambda_j >= 0 (N2), so Z^(1/n_1) is an l^(n_1) norm of a fixed sequence, which is non-increasing in n_1; use (a). (c) A function non-increasing in each argument and bounded below has this property. (d) log(1 + S(t; B)) = log Z(t x B) - t log lambda_0(B) = t|B| (p(t, B) - p(inf, B)) <= t|B| (p(t, B) - p_inf). At t = n, B = (2n)^3 use (b) three times: p(n, 2n, 2n, 2n) <= p(n, n, n, n). QED.

(TORUS). F(n) <= (1/8) log(1 + 1/5041) = 2.48 x 10^(-5) for one n. By T1 it implies the seed of N6 at that size, flux part and thermal part together.
Doubling form (PROVED, telescoping): F(n) = sum over k >= 0 of 16^(-k) D_k, D_k = log Z((2^k n)^4) - (1/16) log Z((2^(k+1) n)^4) >= 0.
Coupling form (N5 again): F(n)(beta) = 6 n^4 times the integral over b in [0, beta] of (P_n(b) - P_inf(b)), P the mean plaquette.

### 5.2 The two fact tests are visible in the one function F (ARGUED)

- U(1), Coulomb phase: F(n) tends to a positive constant (the thermal sum of massless modes at aspect ratio one is scale invariant; twelve lowest modes weigh e^(-2 pi) per direction, and the toron sectors add more). (TORUS) fails.
- Q_8, 2T at large beta: the even sector is gapped, but F(n) tends to log(number of gauge classes of flat connections on the four-torus) > 0. (TORUS) fails through the flux part.
- SU(2), small physical size: F is large (toron valleys). SU(2), confined and gapped: F(n) is about 4 x (number of light states) x e^(-m n).
So F(n) -> 0 says "gapped and no topological sectors" in one line. A proof of (TORUS) must fail for a group with massless modes and for a group with isolated flat connections.

### 5.3 Lemma T2 (cut-and-reglue identity; PROVED)

Let mu_t be the Gibbs measure on t x B, and take two independent copies with slices U_0..U_(t-1) and U'_0..U'_(t-1). Then
  Z(2t x B) / Z(t x B)^2 = E[R],  R = k_orb(U_(t-1), U'_0) k_orb(U'_(t-1), U_0) / ( k_orb(U_(t-1), U_0) k_orb(U'_(t-1), U'_0) ).
Proof. Write each Z as the integral of the product over time steps of e^(-V(U_tau)) k_orb(U_tau, U_(tau+1)). Exchanging the two junction kernels turns the product of the two t-torus integrands into the 2t-torus integrand. QED.
The same holds in each direction, so e^(-16 D_0) is a product of four such means. E[R] = Tr rho_t^2 is the collision probability of the thermal ensemble (N4, I3): the seed says that two independent thermal samples are in the same state with probability at least 1 - 2 s_*.

### 5.4 Attack 3: bound F(n), or one doubling defect, from below-type estimates

The seed needs a LOWER bound Z(big torus) >= (1 - small) x Z(small torus)^(16). Lower bounds on a partition function are the easy direction (Jensen, restriction). So try them on T2.

- Stage 1, Jensen. E[R] >= exp(E[log R]) = exp(-2J), J = E_adjacent[log k_orb] - E_independent[log k_orb] >= 0. J is extensive: each of the 3|B| bonds gains about beta_t (0.65 - 0) (GUIDE numbers at beta = 2.5). So the bound is exp(-10^5). FAILS. Reason, exact: R is a likelihood ratio between "adjacent" and "independent" slices. It is almost zero on a set of probability almost one, and E[R] close to 1 comes from an exponentially rare set where two independent samples nearly agree up to gauge. No first-moment or typical-configuration estimate of R can see it.
- Stage 2, chessboard estimates as the source of averaged a-priori bounds (reflection positivity gives P(event on every plaquette of a set X) <= q^|X| with q a ratio of constrained to free partition functions). To use them at beta = 2.5 one needs the free energy per plaquette f(beta) = log Z / (number of plaquettes) to within about 0.1. By hand (PROVED bounds, Bessel values I_1(2.5) = 2.5167, I_1(7.5) = 249.7):
    lower: f >= (1/2) log(2 I_1(beta)/beta) = 0.350  (keep the three time-like orientations, which are independent in axial gauge; Jensen on the rest, whose mean is 0);
    upper: f <= (1/3) log(2 I_1(3 beta)/(3 beta)) = 1.40  (Hoelder over the three pairs of orthogonal orientations (12)(34), (13)(24), (14)(23); each pair is a product of independent two-dimensional models).
  The true value is about 0.78 (GUIDE: integral of the Monte Carlo plaquette 0.24, 0.50, 0.65 at beta = 1, 2, 2.5). With 0.35 <= f <= 1.40 every chessboard constant for a plaquette event comes out above 1. FAILS by hand. A warning recorded on the way: the "independent plaquette" value log(2 I_1/beta) = 0.70 is NOT an upper bound for f (the Bianchi constraint raises the plaquette); the valid Hoelder bound is the one above.
- Stage 3, what would close it. Because of Stage 1 the proof must control a collective, exponentially rare event, which is a spectral statement in disguise. Because of Stage 2 even the simplest averaged input costs two-sided free-energy bounds ten times sharper than the hand tools give. STOP.

### 5.5 What Attack 3 gained

- (T1) the seed, both parts, is one inequality on one scalar function F(n) of torus partition functions. No transfer operator, no sector language, no slice law is needed to state it.
- Because F is made of torus partition functions only, it is expressed directly by what the Sussman-Alpoge steps keep exactly: the total mass of the unit-lattice density (N1). In D_0 = log Z(l^4) - (1/16) log Z((2l)^4) every extensive local term of the renormalization steps cancels (ARGUED: local terms are translation invariant; terms that wrap the torus are exponentially small in the size over the step scale). What is left is the same doubling defect for the unit-lattice density at first passage. The statement "the last integral is known to e^(O(l^4))" is exactly the statement that D_0 is not known.
- (T2) and Stage 1: the exact reason why estimates of typical configurations cannot give the seed.
- Stage 2: a calibration of the hand tools at beta = 2.5.
- The difficulty did not move off the window. It is now the single statement (TORUS) for the first-passage unit-lattice density on N^4 and (2N)^4 sites, N = l / (unit spacing).

### 5.6 State before the comparison

Three attacks are on disk. Each stops at the same place in a different form:
 - (SHIFT): no finite-temperature shift of the space-like plaquette along a coupling path (Attack 1);
 - (INC): no soft collective coordinate in the slice law (Attack 2);
 - (TORUS): the torus free-energy excess F(n) below 2.48 x 10^(-5) at one size (Attack 3).
Proved on the way: N3, N4, N5, I1-I4, A1, A2, the path identity, B1-B3, 4.5, T1, T2, the two bounds on f. None of them is an estimate inside the window. I did not find a statement inside the window that I can prove.

## Step 6. Comparison with the lane (read only now, after three attacks were on disk)

### 6.0 What was read

- READ D/library/gap-skeleton-final.md Section 13 whole (L288-L644; lines cut at 1500 characters).
- READ D/library/gap-assume-opus.md (row 838): Part 1 whole (L21-L183, the 116-row ledger; rows cut at 520 characters), 3.6 to 3.9 and the report (L492-L548). Part 2 and 3.1 to 3.5 were NOT read; I use only their summary in FINISH row 838 and the report.
- READ FINISH rows 830-862: author rows whole, check and reading rows from their RESULT text. READ the RESULT text of rows 860-875 (row 875 has none yet; rows 876, 877 have none yet).
- GREP of D/library and FINISH for: anisotrop, Hopf, Birkhoff, Sinkhorn, Schroedinger bridge, cross-ratio, Doob, ground-state transform, electric-only, collision probability, conformal window. READ the hits at gap-brainstorm-max.md L317, gap-shape-exercise-astra.md L163-L212, gap-crux-fp.md L131, gap-compress-opus.md L20, prior/gap-lit-geom.md L12-L18 and L38-L52.
- Not independent of the lane's authors: rows 697, 708, 712, 720, 737, 860, 861 are by the same model as this file. Agreement with them is a second sample, not a check.

### 6.1 Node by node

| Mine | The lane | State in the lane | Verdict |
|---|---|---|---|
| N2 | (TM), (TM-c); rows 667, 671, 698, 699 | checked, two providers | same |
| N3 (flux/even split) | Identity FL (row 708, checked 709); ledger row 64 | checked | already there |
| N4 (doubling form, Tr rho^2) | Theorem D-shape (row 705, checked 707): seed = 2F(a,B) - F(2a,B) <= log(1 + t(r)); row 839 (checked 849): seed = chi-square information between slices, min-entropy, rank one | checked | already there |
| N5 (integrated plaquette shift) | Section 13.20: the two numbers of (ES) are integrated finite-size shifts of the plaquette; Proposition MIX (row 708) | checked | already there |
| N6 (SEED-FP) | row 837 | port, not checked | same node |
| N7, N8 | Theorem S, S3', SH, limit theorem, P, P' | checked | same; thresholds are better than my 1/5041: 1/1650 at ratio 2, 1/25 at ratio 4 |
| C-a / C-b / C-c | flux half / glue half; (NS-gap), (M5-H) for the state count | open | already there |
| F1-F3 (what a proof must respect) | Proposition T1 (valid form of a test), K6, K7, Proposition V, ceilings 2/3, 0.775, 4 G_3 | checked in part | mine are weaker; see 7.1 |
| I1, B3, (INC) | (M5-G): a uniform Poincare inequality for the Doob kernel of the even ground state (row 738; prior/gap-lit-geom.md) | open, "restates the gap variationally" | already there |
| I2 (chi-square between slices) | row 839 | checked | already there |
| I3 (swap twist, collision probability) | row 839 (min-entropy, rank one) | checked | same content, other words |
| I4 (layer model in the background of two slices) | Identity L (row 712); Lemma S and Theorem A (row 825, area law below 2/3); Durhuus-Froehlich 1980 (row 831) | checked | already there |
| A1 (flux costs electric energy) | Theorem HS and P1, P2 of row 860 (checked 864): the odd sector is an odd number of half-integer edges in the cut | checked | already there in stronger form |
| A2 (electric-only model is seeded at every beta_t) | named as an idea only: gap-brainstorm-max.md L317 (idea 32); gap-shape-exercise-astra.md L212 (varying "one common beta") | no statement, no proof | NEW as a proved lemma |
| path identity 3.3, (SHIFT) | Proposition MIX (row 708); (PATH) and PIN-MIX (row 861); Theorem TR, (VIR-log) (row 708) on the isotropic path | open | same wall; my path is the anisotropic one |
| 4.5 (virial = no critical point) | Theorem CRIT, (NOCRIT), (VIR-log), Theorem U (rows 708-715) | checked | already there, in sharper form |
| 4.4 (curvature stops) | Proposition BE (row 708, checked 709): curvature route ends at beta <= 1/3; lit pass 13.7 item 5; K7 shares the Ricci curvature | checked | already there; K7 is the stronger reason |
| B1 (bridge form: b enters only through nu) | no hit for Schroedinger bridge, Sinkhorn | absent | NEW (a structure, no estimate) |
| B2 (Hopf bound, V cancels) | "Birkhoff's projective-metric contraction is a lead the lane could not read" (gap-compress-opus.md L20) | absent | NEW: it answers that lead; the bound is extensive |
| 4.6 (two false flux lemmas) | small-volume flux degeneracy recalled in 13.15; row 867's exclusion of six separating structures FAILS its check (row 869) | partly | the Mermin-Wagner obstruction is NEW as an argument (ARGUED only) |
| T1, (TORUS), F(n) | Theorem D (b): 1 + s <= e^(Phi(n)), Phi(n) = 16 F(n^4) - F((2n)^4), (SEED): Phi <= 1.9e-4 (row 697, checked 698, 699); Proposition Delta: Casimir free energy Delta(a^4) <= 6.1e-4 (row 708); (BDD-Delta), (Z-UNB), (Z-SEED) (row 720) | checked | already there and sharper: Phi needs two tori, my F needs all scales |
| 5.2 (both tests in one function) | 13.15: in every comparison model the half that fails is (Z-UNB) | checked in part | already there |
| T2 (cut-and-reglue) and Stage 1 | Lemma M, Proposition MIX (row 708); row 845/852: annealed conditions are worst case in disguise | checked | same lesson; the identity itself I did not find stated |
| Stage 2 (hand bounds on f at 2.5) | row 842 Theorem BAD uses chessboard at large beta only | absent at order one | NEW as a calibration (numbers only) |
| F2 guide example (adjoint matter, conformal) | no hit | absent | NEW candidate test, GUIDE, recalled, not read |

### 6.2 What the lane has that my skeleton lacked

1. The limit half needs only the centre-even sector (Theorem EV-L, row 732). (GAP) on the tr(F^2) sector does not ask for confinement. Flux sectors enter only through the step.
2. The crossing step works for three sector sets (periodic, full, kappa), and by Theorem R (row 744) the crux has one form with no flux sector: the even seed (ES), two numbers. (ES-1) in linear form fails (rows 748-753).
3. The flux half has a cutoff-uniform physical form (E17-phys-CA) given the port (SD-cyl-CA) (rows 844, 848, 865, 868), and an exact topological form: the parity of half-integer edges is a wrapping 't Hooft surface (rows 860, 866, 867). Live inputs: (C2) and EXC (rows 871-874). All OPEN.
4. A second architecture for the window: (EXIT), exact block steps past first passage into an open zone where a proved block criterion holds (rows 846, 850). Row 861 shows that the size of the landed action is free and its locality is the crux (PIN-MIX, (PATH)).
5. Sharper tests than mine: K7 and Proposition V (the proof must see how far log w is from linear), Q_8 near 1.15 and 2T near 2.15 as the binding finite groups (row 838), the valid form of a test (Proposition T1).
6. Proved lattice ranges: seed and gap for beta_W below 0.3609 (rows 836, 841), area law below 2/3 (row 825), surface classes to 6/25 with the original Z_m (rows 833, 847).

### 6.3 What the comparison says about this run

Written before reading: three forms of the crux, (SHIFT), (INC), (TORUS). The lane has each one: (PATH)/Proposition MIX, (M5-G), (SEED)/Proposition Delta. The same model wrote both, so this is not an independent confirmation. It does say that a fresh start from the first-passage action, without the lane's files, lands on the same three statements and on no tool.

## Step 7. Corrections to my skeleton, and what is new here

### 7.1 Corrections (each replaces a sentence of Steps 1 to 5)

1. F3 (1.4) and the remark under I4 said that worst-case criteria stop "because a frozen abelian background orders". Wrong word. The proved ceiling is at the FLAT background: background-uniform layer twist bounds are false above 4 G_3 = 1.0109 there, given Froehlich-Simon-Spencer (READ FINISH row 839, Proposition TB2; checked, row 849).
2. F1 to F3 must be read in the valid form of a test (READ ledger row 90, Proposition T1 of row 712): a tool is refuted only by a model in its class where its hypothesis holds and the seed fails. F1 has that form. F2 rests on a recalled example with matter fields; it binds only tools whose class contains such models. It is a candidate test, GUIDE.
3. Thresholds. 1/5041 (N6, N7, 5.1) is the first threshold of the lane. Theorem SH gives 1/1650 at ratio 2 and 1/25 at ratio 4 (READ Section 13.11, 13.12; checked row 707). The finite form of (TORUS) to use is the lane's (SEED): Phi(n) = 16 F(n^4) - F((2n)^4) <= 1.9e-4 (Theorem D (b), checked rows 698, 699). My T1 is weaker: it needs p_inf, that is, every larger scale.
4. 5.5, second bullet, claimed that the extensive local terms of the renormalization steps cancel in the doubling defect. NOT available: the account's vacuum-energy density is torus-independent only up to a constant per unit cell (READ ledger row 27), the account controls log Z only up to C l^4 (READ Section 13.15), and exact cancellation of the bulk between two tori is named as missing weak-coupling work, (BASE-Phi) (READ Section 13.15, Part 4). Read my bullet as: "(TORUS) for the full theory needs (BASE-Phi) and then the doubling defect at first passage". Lemma FL (row 837; holds per check row 848) is the lane's exact form.
5. 5.4 Stage 2 said "every chessboard constant for a plaquette event comes out above 1". Proved only for the events {A_p <= a} on one orientation: the bound is q <= exp(beta a + (5/3) x 4.198 - 6 x 0.350) = exp(2.5 a + 4.9) at beta = 2.5, above 1 for every a >= -1. (The (5/3) comes from Hoelder on the five remaining orientations, grouped as (34), (13)(24), (14)(23).)
6. 2.2 said that Q_8 and 2T fail the flux part "at large beta". The binding couplings are about 1.15 (Q_8) and 2.15 (2T) (GUIDE, READ FINISH row 838). In the window 2.3 to 2.6 both are frozen, so both bind there; 2I does not (it freezes near 5.7).
7. 4.4: the stronger reason why no argument from curvature and reflection positivity alone can work at every coupling is test K7: the mixed fundamental-adjoint weight shares the group, the centre, reflection positivity and the Ricci curvature, and has a first-order line (READ Section 13.12 item 4; K7 itself is recalled there, GUIDE).
8. 1.4 named one architecture for the window (the seed at one physical size). The lane has a second: (EXIT), exact block steps into an open zone (rows 846, 850, 861). Its crux is locality of the landed action (PIN-MIX), the same wall.

### 7.2 What is new in this file, after the comparison (small; no estimate inside the window)

- A2 (PROVED, unchecked). The model with only the three time-like orientations is seeded at every beta_t, with an explicit bound: S(t; B) <= exp(6 (10e)^3 eps_t^4 |B|) - 1, eps_t = sum over j >= 1/2 of (2j+1)^2 u_j(beta_t)^t. It is a proved endpoint for the lane's idea 32 (gap-brainstorm-max.md L317). Limits, both exact: Theorem S does not apply at or near this endpoint (two couplings break the exchange of time with space; READ gap-crux-fp.md L131), and the path from it to the isotropic point is a restatement (4.5).
- B1 (PROVED; uniqueness is a standard theorem). The two-slice law is the Schroedinger bridge from nu to nu for the electric orbit kernel. The spectrum of the slice chain is a function of (k_orb, nu). No estimate follows yet.
- B2 (PROVED from Hopf's theorem, unchecked). r_1 <= tanh(3 beta_t |B|) for every magnetic coupling and every compact group. This answers the lead "Birkhoff's projective-metric contraction" that the lane could not read (gap-compress-opus.md L20): the magnetic term cancels in the cross-ratio, and the price is an exponent of the order of the volume.
  - B2 cannot be made uniform in the volume inside its class (ARGUED): at b = infinity the slices are flat and the chain is a walk on flat connections with step variance of order 1/(beta_t L), so inf over b of E_1 is at most C/(beta_t L). For Z_2 at large beta the flux sectors of the cube are split by an amount exponentially small in the area (ARGUED here: changing the holonomy class of a slice flips a full plane of links), so an exponential loss is forced in the class of all groups.
  - Consequence for the dominance form (DOM_B) of Section 13.6 (ARGUED): a real gap of 2 exp(-6 beta |B|) and analytic perturbation give dominance on a complex neighbourhood whose width shrinks exponentially with the box. Nothing uniform follows.
- T2 (PROVED, unchecked) and its reading: the doubling ratio is the mean of a likelihood ratio that is almost zero almost surely, so Jensen and every typical-configuration bound lose an extensive exponent.
- Two proved hand bounds: 0.350 <= f(2.5) <= 1.40 for the free energy per plaquette (5.4 Stage 2), with the warning that log(2 I_1(beta)/beta) is not an upper bound. Check of the lower bound (PROVED): a space-like plaquette has mean exactly zero in the time-like-only model, because multiplication by (1/2) tr U_P changes the spin of four links by 1/2 each and so has no diagonal element in the basis where K is diagonal.
- The Mermin-Wagner obstruction for the centre twist (4.6; ARGUED only).
- A candidate test for flow arguments (GUIDE, recalled, not read): a theory that is asymptotically free, centre symmetric, reflection positive, and scale invariant at large distance. It lies outside the class of one-plaquette weights.

### 7.3 What this run refuted of its own

- "Electric flux costs at least a Coulomb energy" (4.6): false for SU(2).
- "The commutator part of the Hessian integrates by parts into a term without beta" (4.4): false.
- "The independent-plaquette value bounds f from above" (5.4): false.
- "A coupling path from a seeded model carries the difficulty to an easier statement" (Attack 1): no; (4.5).

## Step 8. Final skeleton, the next statements, the result

**No mass gap is proved. No estimate inside the order-one window is proved. Nothing in this file is checked by another model.** Marks: PROVED = by hand in this file. READ = statement read at the cited place; "checked" is the lane's own record of who checked it.

### 8.1 The final skeleton (corrected by Step 7)

| Node | Statement | Status |
|---|---|---|
| K0 | First-passage data (K, beta); the unit-lattice density has total mass Z exactly; its action is Wilson at x_K in (g^(-2), g^(-2) + B_sharp] plus local and large-field terms; log Z of the account's tori is known up to C l^4. Sussman and Alpoge, with Claude and Codex; Balaban's estimates. | READ gap-finishline-opus.md L38-172; Section 13.15 |
| K1 | (TM), (TM-c): positive trace-class transfer operator on every box, simple top eigenvalue, centre flips. Osterwalder-Seiler, Luescher. | READ; checked (rows 667, 671, 698, 699) |
| K2 | Seed identities: flux/even split (N3), doubling form (N4), coupling form (N5), chi-square form (I2), symmetric form (T1). | PROVED here; each is already in the lane (6.1) |
| K3 | Theorem SH, Theorem S, Corollary S3': a thermal sum below a threshold on one box gives a gap on every larger cube. Holds for every group. | READ; checked (rows 698, 699, 707) |
| K4 | The limit theorem with Propositions P, P' and the continuum datum of the T0 chain: a seed at one physical size, uniform in the cutoff, gives (GAP). | READ; checked in part; the continuum datum is an open input |
| K5a | (BASE): the seed read on the account's objects. Lemma FL (one inequality on two of the account's tori). Exact cancellation of the bulk between two tori, (BASE-Phi). | Lemma FL READ (row 837, holds per row 848). (BASE-Phi) OPEN, weak-coupling work |
| **K5b** | **Glue half at one physical size, order-one coupling.** Exact forms: (INC) with a state count (B3, 2.2); the lane's (M5-G), (M5-H); (SHIFT)/(PATH); as part of (SEED)/(ES). | **OPEN. No tool.** The equivalences are PROVED or READ |
| **K5c** | **Flux half at one physical size, order-one coupling.** Exact forms: I4 = Identity L; the wrapping 't Hooft surface (rows 860, 867); (E17-phys-CA) given (SD-cyl-CA) (rows 844, 865, 868). Live inputs of the lane: (C2), EXC. | **OPEN** |
| K5' | One form for both halves: (SEED), Phi(n) <= 1.9e-4; or the even seed (ES), two numbers (Theorem R). | Forms READ, checked (rows 698, 699, 744). The inequality is OPEN |
| K5'' | Second architecture: (EXIT), exact block steps into an open zone, then Theorem HO. | Conditional theorem READ (rows 846, 850). OPEN at PIN-MIX (row 861) |
| E1 | Edge of the window, new: the time-like-only model is seeded at every beta_t (A2), with the path identity in beta_s (3.3). | PROVED here |
| E2 | Edge of the window, lane: seed and gap for beta_W below 0.3609; area law below 2/3. | READ (rows 836, 841, 825, 828) |
| E3 | In a fixed box the gap is at least 2 exp(-6 beta_t |B|) for every magnetic coupling and every group (B2). | PROVED here from Hopf's theorem |
| E4 | The slice chain is the Schroedinger bridge of (k_orb, nu) (B1). | PROVED here |

**The node that carries the whole difficulty: K5b and K5c together.** One sentence: on a box of about twenty correlation lengths, for the measure that the renormalization steps deliver, show that two time slices half a box apart are independent to within chi-square 1/1650, with no small parameter. Three direct attacks from this file stop there: (SHIFT), (INC), (TORUS).

A reading that sorts the tests (ARGUED; the lane's test tables already hold both kinds): the seed can fail in two ways. (a) Coexistence: an exponentially light state from tunnelling, as for frozen Q_8 and 2T, K7, the one-well weights of Proposition V. (b) A massless point: a soft collective coordinate, as for U(1) in its Coulomb phase. B2 bounds what either kind can do in a fixed box: no level comes closer to the vacuum than 2 exp(-6 beta_t |B|), which is the size of a tunnelling splitting. (INC) is the exact form of the absence of kind (b). A proof needs one input against each, or one input against both.

### 8.2 Statements for a next proof lane

I found no statement inside the window that I can prove, and I name no tool for K5b. I do not call any route the only one. Two statements follow; the first is provable now and is not on the crux, the second is the crux form to hand to an author when a tool exists.

**Statement 1, (KS-ZONE). Bounded; expected provable by hand; means: one small number.**
There is an absolute c_0 > 0 such that for every beta_t >= 1 and every beta_s with beta_s beta_t <= c_0, in the SU(2) model with weight beta_t on the three time-like orientations and beta_s on the three space-like ones, on every periodic box B with sides at least 4:
 (i) E_1(B) >= 2 |log u_(1/2)(beta_t)| (half of its value at beta_s = 0), flux sectors included;
 (ii) S(t; B) <= 1/1650 for t >= C beta_t log(beta_t) and |B| <= exp(t/(C beta_t)).
- Status: OPEN. A2 is the case beta_s = 0 (PROVED). 3.4 argues the expansion in beta_s. A second route to test: B1 with Bakry-Emery, since nu is close to Haar measure there (4.4 gives kappa = 1/2 at beta_s = 0).
- What it is: the Kogut-Susskind strong-coupling regime with the time cutoff free (beta_t unbounded). It closes idea 32 of row 859 with a theorem. It would be the lane's first proved regime in which one coupling is not small.
- What it is not: a step through the window. Theorem S does not apply there (no exchange of time with space). By the lane's own rule it counts for (GAP) only if a hand-off can reach it; a hand-off by blocking space alone keeps the transfer operator in time exact, but needs the same locality as PIN-MIX. I do not claim that it can.
- Fact tests: it holds for U(1), Q_8, 2T as well (small magnetic coupling), as every strong-coupling statement does.

**Statement 2, (INC-FP). The glue half in the form of this file; not queueable until a means is named.**
For first-passage data with K >= K_0, let nu_K be the law of one time slice of the periodic cube of physical side l (centre-even part), and pi_K the law of two slices at physical time distance delta. Then Var(f) <= C E[(f(U') - f(U))^2] for every gauge-invariant slice function f, with C independent of K. With a state count of the kind (M5-H) it gives the even thermal sum, hence K5b.
- Status: OPEN. It is the lane's (M5-G) in the form (B3); B1 adds that the left side and the right side depend on (k_orb, nu) only.
- A proof must (pre-registered in 2.3, corrected by 7.1): bound a collective coordinate, not a typical configuration (5.4 Stage 1); use the Wilson weight beyond its curvature and symmetries (K7); fail for U(1) through soft photons (4.3). Pointwise curvature (4.4), a coupling path (4.5) and a volume-blind positivity bound (B2) are shown here not to do it.
- On the flux half K5c this file adds no statement to the lane's live inputs (C2) and EXC (rows 871 to 875). A1 and 4.6 agree with the lane: it is an order-one confinement input.

### 8.3 What is proved and what is open (this file)

PROVED here, by hand, unchecked: N3, N4, N5; I1 to I4; A1; A2; the path identity 3.3; B1 (uniqueness quoted as a standard theorem); B2 (from Hopf's theorem, quoted); B3; the Hessian formula of 4.4; 4.5; T1; the doubling and coupling forms of F; T2; the bounds 0.350 <= f(2.5) <= 1.40.
ARGUED: the physical reading in 1.3 and 1.4; 4.6; 5.2; the sharpness remarks on B2 in 7.2; the sorting of the tests in 8.1.
GUIDE: all numbers for beta = 2.5 that are not Bessel values; the candidate test with matter fields.
OPEN: K5b, K5c (the crux); (BASE-Phi); (KS-ZONE); (INC-FP).
New against the lane (6.1, 7.2): A2, B1, B2, T2 as an identity, the two hand bounds on f, the argument of 4.6. Everything else was already in the lane, most of it in sharper form.

RESULT: PARTIAL, nothing proved inside the order-one window and no tool named for the crux. Own skeleton written before any lane file, then three direct attacks on the node that carries the difficulty; each stops at the same statement in another form: (SHIFT) along a coupling path, (INC) for the slice law, (TORUS) for one torus number. The comparison (Section 13, row 838, rows 830 to 875) finds all three already in the lane as (PATH)/Proposition MIX, (M5-G) and (SEED)/Proposition Delta, most in sharper form; same model as those rows, so a second sample, not a check. PROVED and new, unchecked: Lemma A2 (the time-like-only model is seeded at every beta_t, explicit bound), B1 (the two-slice law is a Schroedinger bridge, so the magnetic coupling enters the glue half only through the slice law), B2 (Hopf bound: gap at least 2 exp(-6 beta_t |B|) for every magnetic coupling and every group; it answers the Birkhoff lead and is extensive), T2 (cut-and-reglue identity; Jensen loses an extensive exponent), 0.350 <= f(2.5) <= 1.40 by hand. Refuted here: a Coulomb lower bound for the flux energy, integration by parts of the commutator Hessian term, a coupling path as a reduction (it restates the absence of a critical point). Corrections to my own text in 7.1 (flat, not abelian, background; bulk cancellation is not available from the account). OPEN: the glue half and the flux half at one physical size (K5b, K5c). Next statements: (KS-ZONE), a bounded strong-coupling-in-space theorem with the time coupling free, provable and off the crux; (INC-FP), the glue half in bridge form, not queueable until a means is named. No route is called the only one.
