lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T05:13Z

# gap-univk-pos2: the two end densities of one good label (row 1404)

Provenance: Claude Fable 5.2, medium effort, Mac mini worker 2, pinned commit 80752772d, started 2026-11-22T17:13Z (date -u). One model, one session. Not an audit and not a check by another model.

## 0. Plan (written before any reading beyond FINISH.md, GOAL.md and row 1404)

Statements to settle, for an arbitrary fixed good aligned label, on both tori, at every required real centre:

- (ID) Identify the complete A and B-at-A chart densities on the same resolution, from the printed text.
- (POS-2) Both are nonnegative and their positive sets agree up to null sets. Or a refutation: a negative assembled end density on a set of positive reference measure, or one end density that vanishes on a set of positive mass for the other end.
- (LOG-V) The complete log ratio in last-lattice units, with repeated reads and normalizing terms, is O(V e_w^(1/2)) (age a_0 of check 1397). Or instead (MOM-G): two joint moments with an extensive end floor (check 1403 'Repaired 6.6'; outline 5215-5285 and Y 81779-81848).

Steps, one per response, each appended here before the next:

1. Read row 1400 (`library/gap-univk-sform.md`) and check 1403 in full. Record what they fix and what they leave.
2. Repo search: grep open-core.md and the FINISH rows for POS-2, MOM-G, end density, positive set. Cite matches.
3. Read the outline anchors (YM4_1400 5215-5285; Y 81779-81848) and the native reality and support rows (CV, PD-REST; `library/c1-repr.md`, `library/pd.md`). Cite, do not redo.
4. (ID): write the two densities factor by factor.
5. (POS-2): prove or refute.
6. (LOG-V) or (MOM-G).
7. Result, with the next two rows and their decisive outcomes.

Status: steps 1 to 3 done; see the sections below.

## 1. What rows 1400 and 1403 fix (read in full; written at step 1)

Credit: the charts, labels, ramps, the dial and the hybrid B-at-A are objects of the complete account (CA-I, II, III) and of YM4_1400.tex by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Lemma ENDS, Theorems G and R and Proposition TEL are row 1400's, as corrected by check 1403.

- Row 1400 Theorem R holds (check 1403 L25-L29). Its inputs are (POS-2) and a magnitude: (PW) with an extensive count, or (MOM-G) with an end floor and the load envelope.
- Check 1403 corrections that bind this row: (a) fixed tests and a fixed reference support do not fix the active set of the complete density (rank 3); (b) an additive change of a terminal entry is not automatically additive in the log density (rank 6); (c) the one-class discs do not give the joint moments (rank 1); (d) (PW) with free counts gives no rate (rank 2).
- Not printed, per both: the terminal formula P_h, and positivity of the B objects on the support fixed by the ramps of A.

## 2. Repo search (step 2)

- `library/open-core.md` (564 lines): zero hits for POS-2, MOM-G, "end densit", "positive set", B-at-A, hybrid.
- FINISH rows with POS-2 or MOM-G: 1400, 1403, 1404 only. Check 1403 L5 ran the five-ref search on the full checkout (no hits); `origin/main` is not a ref in this sparse checkout, so I did not repeat it.
- Native one-run reality and support: rows CV and PD-REST (`library/c1-repr.md`, `library/pd.md`, `library/cv-claude.md`). Cited, not redone. Related lane files seen by name: `library/gap-positivity-fable.md` and its checks; read in step 3 if they bear on two-run positivity.

## 3. (ID): what is printed about the two end densities (written 2026-11-22T17:19Z by date -u)

Sources read in this row. "III n" is line n of part III of the complete account (LOCAL:ym4d-papers/sa-ca). "Y n" is line n of YM4_1400.tex (LOCAL:ym4d-papers/sa1400). "I n" and "II n" are parts I and II, fetched by URL at revision 31a47c543775 into my scratch folder (166711 and 145624 lines, the counts on file). Read: III 398-412, 11845-12000, 17381-17535, 17631-17790; Y 81779-81882, 130223-130350; I 156837-156960. Rows 1400 and 1403 read the other passages they cite; I did not re-read those.

| Object | What is printed | Lines | Standing |
|---|---|---|---|
| A term | tau_h^c(v) "is the h-th term chi T^w e^(A^w - E^c) of that expansion, read as a complex Borel measure on V_w; here chi is the product of the characteristic functions of the label, T^w the large-field operation at the stop and A^w the effective action at the stop." Second-class components keep delta_(G_i). | III 11859-11865 | printed |
| Chart | Psi_h^c is "a triangular bondwise right translation" that "preserves the product Haar measure". The norm is "integral of the modulus d mu_h on the space (Omega_h, mu_h) of the label's common inner variables. This space is common to the two runs". delta_(G_i) "is a function of the chart variable V'". On V_w itself the two terms "are carried by different graphs and are mutually singular". | III 11867-11903 | printed |
| One-run positivity | "Every term of [(2.18) of CMP 119], equivalently of [(1.72) of CMP 122b], is a non-negative measure on real fields." T'_k(X, (U, J)) F = (2^d d!)^(-1) sum_omega integral_(S_omega) F e^(Phi_omega) mu_omega, with Phi_omega "finite on S_omega x D_k(X) and real on S_omega x Reg_k(X)". e^(Phi_omega) is "the product of all factors of omega other than its characteristic functions, delta-functions and integration measures". | I 156837-156925 | "Proof outstanding" there; rows CV and PD-REST own it here (`library/c1-repr.md`, `library/pd.md`) |
| Where a native weight is known positive | "a strictly positive real number at every point of S_omega x Reg_k(X)". So: on the run's own support S_omega only. | I 156868-156872 | as above |
| The support S_omega | "(Xi_omega, mu_omega, S_omega) is exterior-free, that is, it is determined by (X, omega), k, g_0, ..., g_k and p." So it can depend on the run through the couplings. | I 156907-156911 | as above |
| Labels | H_al "is one set for both runs". On the scaffold "every threshold, integer, partition and tree is read from theta_s. These are common to the two runs". | III 11932-11936, 11948-11949 | printed |
| B-at-A | "the term of B formed with the objects of B and with the ramps t^A of A in the common variables. This is the term at the end (lambda, eps) = (1, 0)". Also tau_h[x; t^A] := P_h[x], F(x) := sum_h integral phi_h d tau_h[x; t^A]. In Y: "the B term with these A ramps and production slots". | III 17397-17400, 17422-17427; Y 130240-130242 | printed in words only |
| Stop-level slots | "The slots concerned read V_k only [...] at most N_w^4 of them." "|eta^A + s (eta^B - eta^A)| <= (1 + 20 C_chi theta_chi^k |s|) 1{f^B < (1 + varpi_0) c}." "At s = 0 the ramps and the interpolated stop-level slot values are those of A and the objects those of B". | III 17679-17704 | printed; f^B and c are not defined there |
| Slots and runs | "The slots are functions of the integration variables only, and on common labels they are common to the two runs by the common-slot statement". | III 17779-17781 | the common-slot statement is an assumption (a) of that lemma and is not printed |

**3.1 What is NOT printed (one grep each, in parts I, II, III and Y).**
- The assembly formula P_h (rows 1398, 1400 and check 1403 found the same).
- How the ramps t enter a term. "ramp" in parts I and II means the transition layer of a coupling profile (I 21091, 23100-23102, 59789) or an unrelated trace (II 128409). In III it is the scaffold sequence theta_r (III 1270, 53962, as check 1403 L85 says).
- The alignment functional varpi(h). It occurs at III 11941-11946 only. Parts I and II have no "alignment functional" (the letter varpi there names other objects).
- The quantity f^B and the threshold c of III 17686-17692.
- Whether a stop-level slot value eta is real and nonnegative. III 17686-17692 bounds its modulus only.

**3.2 Two consequences that the printed lines do give.**
(i) At s = 0, III 17686-17692 reads |eta_i^A| <= 1{f^B < (1 + varpi_0) c}. So every stop-level slot of A vanishes outside the enlarged support of B. The hybrid evaluates the objects of B on the support of the slots of A. This support lies in the enlarged support of B, and it need not lie in the support of B itself.
(ii) The native weights of B are known positive and finite on the own support of B only (I 156868-156872 with (d2)). So the printed text does not say that the objects of B are positive, or even defined, at every point where the hybrid evaluates them.

**3.3 Verdict on (ID).** The A density is identified up to the native one-run rows: on the label's resolved space it is (tests of A) times e^(native real exponent of A). The B-at-A density is NOT identified by the printed text. Three definitions are missing (3.1). Sections 4 to 6 therefore do two things. Section 4 states exactly what the account's hybrid needs for (POS-2). Section 5 builds a hybrid from the two native runs alone, for which (POS-2) holds by construction and all lost mass is paid.

## 4. Resolution, and (POS-2) for the account's hybrid (PROVED as stated, elementary; unchecked)

**4.0 Setting.** Fix a label h. The chart is (Omega, mu), sigma-finite. A resolution is a sigma-finite space (I, nu) (inner integration variables and a counting measure on histories) with Xi := Omega x I and mu^res := mu x nu. A resolved density is a measurable real rho on Xi with integral of |rho| finite. Its chart density is r(v) := integral rho(v, i) nu(di), defined for mu-almost every v. The label mass is integral r d mu = integral rho d mu^res.

**4.1 Lemma RES (a finer resolution is a stronger statement).** Let rho^0, rho^1 >= 0 be resolved densities with {rho^0 > 0} = {rho^1 > 0} up to a mu^res-null set. Then:
 (a) r^0, r^1 >= 0 and {r^0 > 0} = {r^1 > 0} up to a mu-null set. So (POS-2) on a resolution gives (POS-2) on the chart.
 (b) If d_- <= log(rho^1/rho^0) <= d_+ almost everywhere on the positive set, then d_- <= log(r^1/r^0) <= d_+ almost everywhere on {r^0 > 0}.
 (c) For S >= 0: integral r^0 (r^1/r^0)^(-S) d mu <= integral rho^0 (rho^1/rho^0)^(-S) d mu^res, and integral r^1 (r^1/r^0)^S d mu <= integral rho^1 (rho^1/rho^0)^S d mu^res (integrals over the positive sets). So (MOM-G) on a resolution gives (MOM-G) on the chart.
 (d) The converses of (a) fail. With I = {1, 2}: rho^0 = (1, 0) and rho^1 = (0, 1) have r^0 = r^1 = 1 and disjoint resolved positive sets. rho^1 = (2, -1) has r^1 = 1 > 0 and a negative resolved value.
Proof. (a) r^m >= 0 is clear. r^m(v) > 0 holds exactly when nu{i : rho^m(v, i) > 0} > 0. The symmetric difference N of the two positive sets is mu^res-null. By Tonelli the slice N_v is nu-null for mu-almost every v. For such v the two slice sets differ by a nu-null set, so r^0(v) > 0 exactly when r^1(v) > 0. (b) e^(d_-) rho^0 <= rho^1 <= e^(d_+) rho^0 almost everywhere; integrate over the slice. (c) phi_S(a, b) := a^(1+S) b^(-S) (with phi_S(0, 0) := 0 and phi_S(a, 0) := infinity for a > 0) is the perspective of the convex function t^(1+S). So it is convex, lower semicontinuous and homogeneous of degree one on the closed quadrant, and it is the supremum of countably many linear functions alpha a + beta b. For each of these, alpha r^0(v) + beta r^1(v) = integral (alpha rho^0 + beta rho^1)(v, i) nu(di) <= integral phi_S(rho^0, rho^1)(v, i) nu(di). Take the supremum, then integrate in v. The second inequality is the same with the two densities exchanged. (d) is a direct check. QED

Consequences for this row. (1) A proof of (POS-2), of a pointwise log-ratio bound or of the moments may be given on any resolution that the two ends share. The finest one, where the integrand is a product of factors, is enough. (2) A refutation has to be made on the chart, or it has to show that the projection does not cancel the defect. This is the row's rule "A problematic single factor is not a refutation: trace its full product, cancellations and projection", in exact form. (c) is the data-processing inequality for the Renyi moments of row 1395 4.6.

**4.2 Proposition POS-A (the account's hybrid).** Let Theta^A >= 0 be the product of all tests, characteristic functions and stop-level slots of A on a common resolution of the label h. Assume
 (FAC-H) the resolved B-at-A integrand is Theta^A times w~, with w~ real measurable on {Theta^A > 0};
 (EXT) 0 < w~ < infinity almost everywhere on {Theta^A > 0}.
Assume the native row for A: the resolved A integrand is Theta^A w^A with 0 < w^A < infinity on {Theta^A > 0}. Then (POS-2) holds on the resolution with f_h = Theta^A, Phi^A = log w^A, Phi^B = log w~, hence on the chart (Lemma RES). Conversely, under (FAC-H) the resolved (POS-2) implies (EXT).
Proof. The two densities are Theta^A w^A and Theta^A w~. Their positive sets are {Theta^A > 0} and {Theta^A > 0, w~ > 0}, and the second density is nonnegative exactly when w~ >= 0 on {Theta^A > 0}. QED

**4.3 What (EXT) asks, and its standing.** w~ is the product of the weight factors of B. On {Theta^A > 0, Theta^B > 0} the native row for B gives 0 < w~ < infinity. On the part of {Theta^A > 0} where a test of B vanishes, nothing printed applies (3.2 (ii)). By 3.2 (i) that part lies in the enlarged support of B. So (EXT) follows from
 (PD-ENL) clause (a) of the positivity dichotomy and the finiteness in its clause (d2) hold for run B on the enlarged set {f^B < (1 + varpi_0) c} in place of S_omega.
(PD-ENL) is NOT printed, and it is a new native one-run statement: it is not part of rows CV and PD-REST as stated (check 1403 L6: "Neither covers the B objects evaluated with A ramps and A stop-production slots"). It is plausible, because the complex domains D_k(X) of the objects are open sets fixed before the tests. It is not proved here. I found no place where it fails.
**Verdict for the account's hybrid: (POS-2) is NOT DECIDED.** It is reduced to (FAC-H) and (PD-ENL), and (FAC-H) cannot be read from the text. No refutation was found: no printed line gives a negative assembled end density or an end density with a smaller positive set.

## 5. A hybrid built from the two native runs alone: Theorem CAP (PROVED GIVEN (FAC) and (COMMON); unchecked) (written 2026-11-22T17:21Z by date -u)

**5.0 Inputs.** G is a countable set of labels (here: the aligned labels with no live component of age a_0 or more, row 1395 6.2). Fix the torus and the real centre.
 (COMMON) For every h in G the two runs have one resolved space (Xi_h, mu_h^res), which projects to the common chart of III 11867-11903. Printed for the chart, the label set, and the thresholds, integers, partitions and trees (III 11889-11891, 11932-11936, 11948-11949). For the inner integration spaces of the histories it is an input (I 156907-156911 lets the triple depend on g_0, ..., g_k).
 (FAC) For m in {A, B} the native resolved density of run m, pulled back by its own chart map Psi_h^m, is rho^m = Theta^m w^m. Here Theta^m >= 0 is the product of all characteristic functions, tests and slot factors of run m, and w^m is the product of its weight factors, with 0 < w^m < infinity on S^m := {Theta^m > 0}. This is the native one-run statement of I 156837-156925, owned by rows CV and PD-REST. It is cited, not redone.
No formula P_h, no ramp and no alignment functional enters below.

**5.1 Definitions.** P_h := S^A intersect S^B. On Xi_h put
  rho^(A,P) := 1_P Theta^A w^A,   rho^H := 1_P Theta^A w^B,   rho^(B,P) := 1_P Theta^B w^B.
Masses, summed over h in G: F^A, F^B (native), F_P^A, F^H, F_P^B. Shell masses: D^A := F^A - F_P^A = sum_h integral over S^A minus S^B of rho^A, and D^B := F^B - F_P^B. Shell fractions: s^m := D^m / F_P^m. Assume 0 < F_P^A, F^H, F_P^B < infinity.
In words: rho^H has the tests of A and the weights of B, like the account's hybrid, but only on the set where both runs pass their own tests. Every weight is evaluated inside the own support of its run.

**5.2 Theorem CAP.**
 (a) ((POS-2) by construction) rho^(A,P) and rho^H are nonnegative and both are positive exactly on P_h. So (POS-2) holds for this pair on the resolution with f_h = 1_P Theta^A, Phi^A = log w^A, Phi^B = log w^B, and on the chart by Lemma RES. The log ratio is Delta_h = log w^B - log w^A on P_h. It contains weight factors only.
 (b) (all lost mass is paid) log F^B - log F^A = [log F^H - log F_P^A] + [log F_P^B - log F^H] + log(1 + s^B) - log(1 + s^A).
 (c) (tests) If e^(-d) Theta^A <= Theta^B <= e^d Theta^A on P_h for every h, then |log F_P^B - log F^H| <= d. For sharp tests (values 0 and 1) d = 0 and rho^H = rho^(B,P).
 (d) (total) | log F^B - log F^A | <= | log F^H - log F_P^A | + | log F_P^B - log F^H | + max( log(1 + s^A), log(1 + s^B) ).
 (e) (the native pair) (POS-2) holds on the resolution for the native pair (rho^A, rho^B) exactly when the symmetric difference of S^A and S^B is mu^res-null. Then D^A = D^B = 0 and P_h is everything.
Proof. (a) On P_h all four factors are positive and finite; off P_h both densities are 0. (b) F^m = F_P^m (1 + s^m); take logarithms and insert log F^H. (c) Multiply the inequality by 1_P w^B >= 0, integrate and sum. (d) log(1 + s^B) - log(1 + s^A) lies between -log(1 + s^A) and log(1 + s^B). (e) The positive sets of the native densities are S^A and S^B. QED

**5.3 What Theorem CAP decides.**
- For the native pair, (POS-2) FAILS on the resolution whenever the tests of the two runs differ on a set of positive measure ((e)). This is the row's second refutation route, and it is why a hybrid is needed at all. The failure costs exactly the two shell fractions.
- For the pair (rho^(A,P), rho^H), (POS-2) is a theorem given the native rows only. (PD-ENL) and (FAC-H) of Section 4 are not needed, because no object of B is evaluated outside the support of B.
- The row's rule "Restricting to a smaller common set [...] must pay all lost mass at both ends" is identity (b): the price is log(1 + s^B) - log(1 + s^A), with D^A a native mass of A and D^B a native mass of B.
- Relation to the account's hybrid. If (FAC-H) and (EXT) hold and w~ = w^B on P_h, then rho^H = 1_P rho^(B|A). The account's hybrid carries in addition the mass of Theta^A w~ on S^A minus S^B. Proposition TEL of row 1400 needs this off-support mass (its term T^-). Here D^A replaces it.
- Relation to Theorem R of row 1400. Theorem R applies to the pair of (a) as it stands. Its inputs (PW) or (MOM-G) are now statements about log w^B - log w^A on P_h.
- Uniformity. Nothing is estimated in (a), (b), (d), (e). They hold on both tori and at every real centre where (FAC) and (COMMON) hold.
- Not equivalent to the open target. (FAC) and (COMMON) are one-run and structural. They compare no cutoffs. The comparison content is now in three numbers: B_rec := |log F^H - log F_P^A|, the test term of (c), and the shell fractions.

**5.4 The shell fractions (OPEN; stated, not proved).**
 (SHELL) s^A <= e^(p_A) - 1 and s^B <= e^(p_B) - 1 with p_A, p_B = O(V theta_chi^k).
In words: in run A, the retained mass on configurations that fail a test of B is a fraction O(V theta_chi^k) of the mass that passes both; and the same with A and B exchanged. This is the relative form of the account's absolute bound C_test theta_chi^k A^sharp (III 17653-17664). It replaces (CUT-H) and (TEL-REL) of row 1400 5.3. It is a one-run statement at each end: it needs the two test quantities to be close (the printed factor 20 C_chi theta_chi^k of III 17686-17692 is of this kind) and no excess of native mass in the shell between the two thresholds. Check 1403 L49 notes that the printed disc bound gives the slot difference only as p_0 + 1/R; that loss is in the supply of (SHELL), not in Theorem CAP.

## 6. The magnitude of the complete log ratio: Theorem M (PROVED GIVEN (PW-C) and (CAP-M); unchecked)

**6.1 Theorem M.** Let G be countable. For h in G let rho_h^0, rho_h^1 >= 0 be densities on a measure space (Xi_h, mu_h) with one positive set P_h, and Delta_h := log(rho_h^1 / rho_h^0) on P_h. Let F^m := sum_h integral rho_h^m d mu_h be in (0, infinity), and <.>_m the mean in the probability measure F^m^(-1) sum_h rho_h^m mu_h on the disjoint union. Let I be a finite index set, n_i(h, xi) >= 0 measurable charges, and a, c_i >= 0 constants with
 (PW-C) | Delta_h | <= a + sum_(i in I) c_i n_i(h, xi) almost everywhere on P_h, for every h in G.
Then
 (a) | log F^1 - log F^0 | <= a + max_(m = 0, 1) log < exp( sum_i c_i n_i ) >_m .
 (b) If moreover, for some gamma > 0 and B >= 0,
   (CAP-M) < exp( gamma sum_i n_i ) >_m <= e^B for m = 0 and m = 1,
 and theta := max_i c_i / gamma <= 1, then | log F^1 - log F^0 | <= a + theta B.
Proof. (a) F^1 = sum_h integral rho_h^0 e^(Delta_h) d mu_h <= e^a sum_h integral rho_h^0 e^(sum_i c_i n_i) d mu_h = e^a F^0 < e^(sum_i c_i n_i) >_0. In the same way F^0 = sum_h integral rho_h^1 e^(-Delta_h) d mu_h <= e^a F^1 < e^(sum_i c_i n_i) >_1. (b) Since c_i <= theta gamma and n_i >= 0, e^(sum_i c_i n_i) <= ( e^(gamma sum_i n_i) )^theta. The function t^theta is concave for theta <= 1, so Jensen's inequality gives < e^(sum_i c_i n_i) >_m <= e^(theta B). QED

Remarks. (i) (a) needs no convexity, no moment at a large exponent S, no floor and no radius. It is Theorem R (a) of row 1400 with the supremum of the count replaced by an exponential mean at the small scale c. Check 1403 L58 asked for this: "prove the corresponding bound on the integrated tilted mean". (ii) (b) is the capacity criterion of the outline (Y 81779-81848; outline 5215-5285 as cited by check 1403 L43) in the form the end comparison needs: the charges n_i are the history charges W_(omega,z), the constants c_i are the loads times the number of reads, and gamma is the reserve c of that proposition. The criterion there gives a joint holomorphy domain; (b) gives the two-sided mass bound directly. (iii) (CAP-M) is a relative bound at each end. An absolute bound sum_h integral rho_h^m e^(gamma sum n_i) <= e^(E V) together with a floor F^m >= e^(-C' V) gives B = (E + C') V. (iv) By Lemma RES (b) and (c), the hypotheses may be checked on any common resolution.

**6.2 Last-lattice units, repeated reads and normalising terms.** Apply Theorem M to the pair of Theorem CAP (a), with k the stop level and V = N_w^4.
- Top zone b = k: at most V cells, one read level. This part of the bound is pointwise: a = K l_k V.
- Recent lower zones b in [k - a_0, k - 1]: n_b(h) := the number of cells of zone b in h, counted as level-b cells, and c_b := K (k - b + 1) l_b. The factor k - b + 1 is the number of read levels t in [b, k]; this is where the repeated reads are paid.
- Normalising terms: (PW-C) is a bound for the complete Delta_h. The run-dependent constants (vacuum constants, the z-pieces, s^0 and D^0, III 11973-11976) and the normalising entries must be inside it, each with its class. A term that is not bounded by a load times a cell count has to be named and paid separately (next row).
Then max_b c_b <= K q_a^(-(a_0 - 1)) Sigma_k^(q_a) and l_k <= Sigma_k^(q_a), because Sigma_k^(q_a) = sum_b (k - b + 1) q_a^((k-b-1)_+) l_b and q_a^((k-b-1)_+) >= q_a^(a_0 - 1) for b >= k - a_0. With (CAP-M) at B = E V, Theorem M (b) gives
  B_rec = | log F^H - log F_P^A | <= K V Sigma_k^(q_a) ( 1 + (E / gamma) q_a^(-(a_0 - 1)) ).
At the age of check 1397 L58 (q_a e_w^(1/2) < q_a^(a_0) <= e_w^(1/2)) and with Sigma_k^(q_a) <= C e_w, this is at most K C V ( e_w + (E / gamma) e_w^(1/2) ) = O(V e_w^(1/2)), when E / gamma is bounded and K C e_w^(1/2) <= gamma. This is the rate the row asks for. It is PROVED GIVEN (PW-C) with these charges, (CAP-M) with B = E V at both ends, the incidence of row 1395 6.2 (only classes with b >= k - a_0 move on G) and the load envelope.
The volume factor L^(4(k-b)) of row 1400 4.4 and of check 1403 L60-L67 does not appear. It is replaced by (CAP-M). The condition q_a L^4 / rho < 1 of check 1403 is not used.

**6.3 What (CAP-M) asks (ARGUED, not proved).** The crude count n_b <= V L^(4(k-b)) is reached only by labels whose level-(b+1) large-field region fills the torus. (CAP-M) says that the exponential moment of the count of lower-zone cells, in the two end measures, is extensive in the last lattice. A product heuristic (independent cells, each in a large-field region with weight eps_b) gives log < e^(gamma n_b) > of order V L^(4(k-b)) eps_b e^gamma. So E is bounded when L^(4 a_0) e^gamma max_b eps_b is bounded. With eps_b of the size e^(-p_0(g_(b+1))) this holds when a_0 grows like log K (the power rate Pi_K), and it can fail when a_0 grows linearly in K (a geometric rate with a slowly growing p_0). This is a heuristic. It is not a proof and not a counterexample. The printed reserves are per live component (the factor q_a^(a'+1) of III 17493-17499) and per component exponent (III 17719-17722), not per cell. So (CAP-M) is OPEN.

## 7. Verdicts (written 2026-11-22T17:21Z by date -u)

7.1 **(ID): DONE for A up to the native rows; NOT POSSIBLE for the account's B-at-A from the printed text.** P_h, the entry of the ramps, the alignment functional and the test quantity f^B are not printed in parts I, II, III or YM4_1400 (3.1). Printed and used: the slots of A vanish outside the enlarged support of B (3.2).

7.2 **(POS-2) for the account's hybrid: NOT DECIDED. No refutation found.** It holds given (FAC-H) and (EXT), and under (FAC-H) the resolved form is equivalent to (EXT) (Proposition POS-A). (EXT) follows from (PD-ENL), a new native one-run statement on the enlarged support, which is not printed.

7.3 **(POS-2) for the native pair of one label: FAILS on the resolution when the tests differ on positive measure (Theorem CAP (e)).** The cost is exactly the shell fractions.

7.4 **(POS-2) for a hybrid that serves the same consumer: PROVED GIVEN (FAC) and (COMMON) (Theorem CAP (a)), unchecked.** The pair is (A on P, tests of A with weights of B on P). All lost mass is paid by identity (b). No object is evaluated outside its own support.

7.5 **Resolution: PROVED (Lemma RES), unchecked.** (POS-2), pointwise bounds and the Renyi moments pass from any common resolution to the chart. The converse fails; a refutation must be made on the chart.

7.6 **Complete log ratio at the rate O(V e_w^(1/2)): PROVED GIVEN (PW-C) and (CAP-M) (Theorem M with 6.2), unchecked.** Repeated reads enter through the factor k - b + 1. The fine-cell volume factor is replaced by the capacity moment. (PW-C) and (CAP-M) are OPEN.

7.7 **Consequence for Theorem E in the repaired form of check 1403 ('Repaired 6.6').** Replace the pair (tau^A, tau^(B|A)) by the pair of Theorem CAP (a), and the ramp step by Theorem CAP (b) to (d). Then at each admitted edge
  | log Z~^B - log Z~^A | <= B_rec + d_test + max( log(1 + s^A), log(1 + s^B) ) + 2 C V r_K,
with B_rec from Theorem M. This is PROVED GIVEN (FAC), (COMMON), (PW-C), (CAP-M), (SHELL), the test term of 5.2 (c) or (TEL-REL) restricted to P, and the unchanged inputs (H3), (H4), the load envelope, the reached chain and the two-torus carry. It proves no unconditional Wilson estimate.

7.8 **Not shown.** (FAC) and (COMMON) for the inner history spaces; (PW-C); (CAP-M); (SHELL); the test term for smooth tests. Whether the account's hybrid equals rho^H on P is not shown, and it is not needed.

## 8. Next two rows and their decisive outcomes

**Row 1, `gap-univk-pwc` (reading and proof row, one label, weights only).** For a label of G on the common resolution, list the weight factors of the native term of one run (I 156837-156925; CMP 122b (1.71)-(1.72); in this lane `library/c1-repr.md` L40-55, 80-86, 213-218 and `library/pd.md` L989-996, 1443-1464). For each factor write log w^B - log w^A at a point of P, with the two chart maps, as slot differences at a common datum plus reading parts (III 12017-12056, 13106-13126, 13733-13739; Y 129655-129658). Decide (PW-C) with a = K l_k V and c_b = K (k - b + 1) l_b. Decide (COMMON) for the inner history spaces on the way.
 Decisive outcomes: (1) (PW-C) holds for every weight factor: B_rec is then a theorem given (CAP-M) and the load envelope, and the dial interpolation of the account is not needed for the recent retained estimate. (2) one factor (a normaliser quotient, a determinant, a Jacobian of the chart map) has a log difference that no load times cell count bounds: name it, and pay it by its own moment (Lemma RES (c) and Theorem R (b)) or show that it cancels between the label and the normalisation E^c.

**Row 2, `gap-univk-shellcap` (proof row, one run at a time).** Decide (SHELL) and (CAP-M) for the labels of G, on both tori. (SHELL): bound the native mass of A on {a test of B fails} by C V theta_chi^k times the mass on P, and the same with the runs exchanged; first find where the account defines the test quantity f and the threshold c (not in the passages of 3.1; try the scaffold chapters of III around 1270 and 53962 and the component manuscripts RT and SI at upstream HEAD). (CAP-M): bound the exponential moment of the lower-zone cell count at a fixed gamma by e^(E V), from the per-cube large-field factor of CMP 122b (the reserve read at II 104051) and the forgetting statement.
 Decisive outcomes: (1) both hold with constants free of the torus: Theorem E has only ell^4 terms and the recent rate e_w^(1/2). (2) the shell of one stop-level test carries a fraction of order one of the retained mass, or the count moment grows like V L^(4 a_0): then the restriction to P, or the age a_0, costs more than the rate; fall back to the full-end-point shortcut of check 1397 L74, or take a_0 of order log K only.
Order: Row 1 first. It decides whether the weights alone can carry the comparison. This row replaces the part of `gap-univk-rar` that concerned (TEL-REL); (PART), (TILE), (PROD) for the discarded classes stay with that row.

## 9. Status

| Statement | Mark |
|---|---|
| Section 3 table and 3.1, 3.2 | READ (lines cited; parts I and II fetched at 31a47c543775) |
| Lemma RES (4.1) | PROVED (Tonelli; convex degree-one function); unchecked |
| Proposition POS-A (4.2) | PROVED as an equivalence under (FAC-H); (FAC-H), (EXT), (PD-ENL) OPEN |
| Theorem CAP (5.2) | PROVED GIVEN (FAC), (COMMON); unchecked |
| Theorem M (6.1) and the rate of 6.2 | PROVED GIVEN (PW-C), (CAP-M), incidence, load envelope; unchecked |
| 6.3 | ARGUED (heuristic), not a proof step |
| (POS-2) for the account's own hybrid | NOT DECIDED; no refutation found |
| (PW-C), (CAP-M), (SHELL), test term, (COMMON) for inner spaces | OPEN |
| (RAR), term D, (GEO), hypotheses of III 9.1, (LOG), the seed | OPEN, untouched |

Repo search for the new names: `library/open-core.md` and the FINISH rows have no hit for RES, POS-A, PD-ENL, "Theorem CAP", CAP-M, PW-C or SHELL in this sense (one grep each, this lane folder). Row 1395 4.6 (Lemma RENYI), row 1400 (Theorems G and R, Proposition TEL) and check 1403 (the capacity route, the tilted mean) are the prior items; each is cited where it is used.

No numeric job was run; none was needed. Files written in the repository: this file only. Scratch: /tmp/ym4d-pos2-w2 (parts I and II of the complete account and the SI manuscript, fetched by URL; the SI manuscript has no "ramp" and was not used).

RESULT: (POS-2) for the account's own B-at-A hybrid is NOT DECIDED and not refuted: its formula, the entry of the ramps and the alignment functional are not printed; it is reduced to (FAC-H) and positivity of the objects of B on the enlarged support (PD-ENL), a new native statement. PROVED (elementary, unchecked): Lemma RES (positivity, pointwise and moment bounds pass from any common resolution to the chart; refutations must be made on the chart), Theorem CAP (the native pair fails (POS-2) exactly by the test shells; the pair "A on P" and "tests of A, weights of B on P", P the common test set, satisfies (POS-2) by construction from the native one-run rows alone, with all lost mass paid by the two shell fractions), and Theorem M (the complete log ratio is at most a + max over the ends of the log exponential mean of the charged cell count, which gives O(V e_w^(1/2)) with repeated reads paid and no fine-volume factor, given (PW-C) and the capacity moment (CAP-M)). OPEN: (PW-C), (CAP-M), (SHELL), the test term for smooth tests, (COMMON) for the inner history spaces, then (RAR), term D, (GEO); next rows gap-univk-pwc, then gap-univk-shellcap.
