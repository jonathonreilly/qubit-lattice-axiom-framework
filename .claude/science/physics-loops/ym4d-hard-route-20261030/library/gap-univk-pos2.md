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
| The support S_omega | "(Xi_omega, mu_omega, S_omega) is exterior-free, that is, it is determined by (X, omega), k, g_0, ..., g_k and p." So it can depend on the run through the couplings. | I 156911-156915 | as above |
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
