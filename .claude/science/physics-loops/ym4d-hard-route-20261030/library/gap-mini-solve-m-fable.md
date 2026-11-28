lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:25Z

# gap-mini-solve-m-fable: four-dimensional SU(2) Yang-Mills mass gap (row 1212)

Started 2026-11-20T05:25Z (date -u). Pinned commit b8c2bc658, branch
claude/ym4d-hard-route. Model: Claude Opus 5.5, max reasoning (the row's Fable
model hit its weekly limit; see the lead note in row 1212). No earlier text of
this item was on file at the pinned commit.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Step 0. Reading (written after 2026-11-20T05:36Z, the last `date -u` reading before it)

Read for this row (bounded reads; no whole part file): GOAL.md in full; FINISH.md L1-85 and L299-352 (rules,
efficiency, joining); the RESULT text of rows 916, 917 and 1179-1227; `parts/gap.md` L1-104 (state of attack, routes
tried, lead rules); `library/gap-mini-branch-fable.md` L167-366 (Theorem L3-ev, Propositions P-ev and P'-ev,
Theorem BP, the statement of (N-phys)); the plan and stopping sections of the sibling rows of today,
`gap-mini-solve-n-fable.md` (L28-41, L83-140), `-o-` (L41-81), `-q-` (L1-102, L261-285). A grep of 28 further tool
names over `library/*.md` and `parts/*.md` (Bourgain, Kazhdan, expander, uncertainty principle, the x^2 y^2 potential,
Lieb-Thirring, NSVZ, low-energy theorem, anomaly matching, Georgi-Glashow, adjoint Higgs, Banks-Zaks, conformal
window, bootstrap, Kazakov, Kruczenski, spin foam, Lojasiewicz, Gaiotto, theta = pi, Elitzur, Bianchi, monopole,
Gopfert-Mack, Debye, Witten index, Kogut-Susskind, spin network): every name except "expander", "Banks-Zaks" and
"Witten index" has hits, and the conformal-window and Georgi-Glashow families are in the comparison tables
(`parts/gap.md` L293; `gap-outside-box-max.md` I11; `gap-compact-rigidity-max.md` A16).

**Where the problem stands on file (cited, not re-derived).**

1. The gap clause of the Jaffe-Witten target reduces to one lattice input, (N-phys), plus the continuum datum.
   Statement (row 1179 L304-310, from row 1161 L146-148): at one admissible physical side L, for every cutoff index
   j >= j_0, with n_j = L/a_j and 4 | n_j, some integer u_j with 3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where
   s_+ is the periodic centre-neutral excited trace of the spatial cube in units of its vacuum. The reduction is
   Theorem BP of row 1179 (checked across providers in row 1183, HOLDS AFTER CORRECTION). The branch selection (BS)
   is not an input of the gap clause.
2. The continuum datum ((H2), (TOT), (P1)-(P4)) on the tr F^2 sector is PROVED GIVEN the account's premises: row 916
   Theorem E, checked by gpt-6-astra in row 917 (HOLDS AFTER CORRECTION). It stays open with the T0 chain. (UNIV-K)
   of row 916 is open but is needed only for the one-K form; row 1180 notes that for one continuum datum a liminf
   along a subsequence suffices.
3. (N-phys) is open. In physical terms it asks for a dilute glueball gas at Euclidean time about 25/M in a box of
   side about 1.25e4/M (row 1219 Section 2, GUIDE arithmetic). About twenty plain-brief rows (1188-1225) and the
   astra chain (rows 1143-1227) end at the same statement: an estimate at one physical scale where the running
   coupling is of order one, uniform in the cutoff, that fails for massless comparison models. Rows 1219 and 1224
   recommend that a new row take one precise question with a consumer instead of another blind search.

## Step 1. How to attack it (written between the `date -u` readings 2026-11-20T05:36Z and 05:47Z)

**Judgement (ARGUED; a judgement, not a theorem).** No attack available to this session can close (N-phys). The
reasons, each with its place on file:

1. (N-phys) is not weaker than the gap. By row 1180 (corollary checked in row 1187) it holds iff every fine coupling
   has a finite one-cube seed size nu(beta_j) with limsup a_j nu(beta_j) finite, that is, a lattice gap at each
   coupling with the asymptotic-freedom scale. The fixed-coupling lattice gap is itself open for every beta above
   the strong-coupling range (about 0.35-0.36 for 4D SU(2) Wilson by hand: row 1218 reading of A Theorem 9.5 and B
   Theorem 3; row 1219 Section 3 (c)).
2. A proof must contain an estimate at the scale where the running coupling is of order one. In perturbation theory a
   dimensionless thermal ratio such as p/p_SB differs from its free value by a fixed multiple of g^2 at leading order
   (recalled, not proved here), so its change between two scales is of the size of the change of g^2, and that is of
   order one only once g^2 is. No perturbative step carries the bound across (row 998 6b; row 1200 Steps 5-7: every
   neutral quantity moves by order g^2 per doubling).
3. At that scale there is no small parameter and no exact structure on record. Positivity in plaquette variables
   fails (EP-NO, row 744; FKG-NO, row 1213); the bracket gain of the 2D O(N) proofs needs a continuous global
   symmetry, and pure SU(2) has only the centre (Lemma CEN+, row 1016; Lemma PC, row 1188; row 1197); the
   asymptotic-freedom-selective quantities found so far (twist ratios, theta sectors) are ratios in which an
   independent free photon cancels, so they cannot see every neutral level (Lemma PT, Proposition NP, row 1003;
   row 1200).
4. Every engine on file is blind, so its seed fails for a gapless model of its class and sits in the band (row 998
   6b; row 1219 Section 3 (a), one-line proof). The published one-scale criteria of row 1218 ask for the same
   physics at the same Euclidean time (row 1219 Section 2; row 1224 Section 3).

**Choice.** By FINISH "How we work" item 0 (name the item it closes or kills, and what changes either way), another
screening of routes has no such item: rows 1188-1225 each found the map again. This row therefore does two bounded
things and stops.

- Step 2. The lead note on row 1219 asks that its reading of the continuum datum be confirmed against rows 916-917
  before it is relied on. This is the second input of the gap clause beside (N-phys). Step 2 reads the statement of
  row 916 Theorem E and the corrections of check 917 and says whether they give exactly what Theorem BP (iii) and
  Proposition P'-ev of row 1179 consume. If not, the gap clause has a further open input.
- Step 3. One structural fact, stated and proved in the form the lane can use, if it is not on file.

## Step 2. The continuum datum under (N-phys): does rows 916-917 give what Theorem BP consumes? (written after 2026-11-20T05:47Z, `date -u`)

**Why this needs saying.** Row 916 Theorem E (`gap-chain-ce-opus.md` L172-251) built the continuum datum under
(SEED-FP), the periodic seed. Its members D_j are the data of Theorem L3 (e) of row 700, on ALL local functions,
whose reflection positivity row 700 takes from the periodic seed (G1) (row 1179 L297-300 says so). Under (N-phys)
only the centre-blind data of Theorem L3-ev exist (row 1179 Section 5.1). Row 1219 cites rows 916-917 for the datum
under (N-phys); the lead asked for that reading to be confirmed. Read for this step: `gap-chain-ce-opus.md` L172-251
(Step 5, Theorem E), `gap-chain-ce-check-astra.md` L107-211 (the check of Theorem E), and row 1179 Sections 5.1-5.3 and
6 (above). The account's lines were not re-read; they are cited as rows 916 and 917 read them.

**Proposition D (ARGUED: a reading check, each step cited; not a line-by-line check of the account).** Assume
(N-phys) at an admissible side L along the account's first-passage trajectory, the account's hypotheses (CA
L1748-1754, as check 917 L109-113 lists them) and the account statements READ in row 916 (CA L1690, L1692, L1709,
L1724, L1726, L1785, L99150-99156, L99284-99294, L115120-115205). Then every volume-first limit S at g (in the
account's sense) has ker H = C Omega in H(S), and spec(H) lies in {0} union [M_*, infinity) with
M_* = (2/L) log(1/(40328 eps)) (the constant of Theorem BP (ii)). H(S) is the account's Hilbert space of the scalar
curvature-density (tr F^2) sector.

Proof, as a list of the places where Theorem E reads its member data, with the substitute under (N-phys).

1. Members. Theorem E takes D_j = the Theorem L3 (e) datum of the account's state nu_j (L182-184). Substitute
   D_A(nu_j) of Theorem L3-ev (e-ev), on V_A. The account's nu_j are lane limit states along symmetric integer-sided
   tori (Lemma C, row 916 Step 4; HOLDS in check 917), so restricted to A they are the states of Proposition P-ev (b),
   which holds at each cutoff of the trajectory by Theorem BP (i)-(ii).
2. Lattice versions lie in V_A. Theorem E's iota_j X is a product of centred account observables O_j(f) - nu_j(O_j f)
   with time range in (0, infinity) (E1, L189-191; HOLDS in check 917 L127). O_j(f) is a function of plaquette
   holonomies (the scalar curvature density, check 917 L188; account L99284-99294, not re-read here). A function of
   plaquette holonomies is in A: under (g.U)(x, mu) = g(x) g(x + mu) U(x, mu) with g valued in {+1, -1}, each site of
   a plaquette contributes g(x)^2 = 1, so every U_p is unchanged. So iota_j X is in V_A. (PROVED, one line, given that
   reading of O_j.)
3. Pairings. b_j(iota_j X, tau_s iota_j Y) is the expectation in nu_j of a product of functions in A. It is the same
   number whether the member is D(nu_j) or D_A(nu_j). So E2, E3 and the items (H2), (P2), (P4), (TOT) of Theorem E,
   which read only these numbers and the account statements, transfer unchanged, with check 917's two corrections
   (E2's domain notation, L134-148; the partition-sum constants in (P4), L150-173, L187).
4. (P1) of D_inf. Theorem E uses (P1) of each member (L220-222). Substitute (c-ev) of Theorem L3-ev: nu_j(conj(Theta F) F)
   >= 0 for F in V_A. Since every iota_j F is in V_A (item 2), the Gram matrices of check 917 L184 are positive.
5. (P3) of D_inf. Theorem E uses the member contraction norm(T_j^s) <= 1 (L226-228; check 917 L186). Substitute (e-ev):
   on H_A(nu_j) the transfer operator is 1 on Omega and has spectrum in [-exp(-m_0), exp(-m_0)] on its complement, so
   its norm is at most 1.
6. (H1). Theorem E uses Proposition P (c) under (SEED-FP) with m_j = M_* (L238). Substitute Proposition P-ev (c) with
   the rate of Theorem BP (ii), on S_j = the complement of Omega_j in H_A(nu_j); each vacuum-subtracted vector of
   iota_j X lies there (check 917 L189 for the same point).
7. Conclusion. Proposition P'-ev (row 1179 Section 5.3, which applies `gap-os-equiv.md` Statement (5a)-(5c)) with
   items 1-6 gives ker H = C Omega and, with (P4), spec(H) in {0} union [M_*, infinity). QED (as an implication).

**Relation to check 1183.** The cross-provider check of Theorem BP (row 1183) lists "the continuum datum, (H2), (TOT)"
as OPEN and asks for "a matched continuum RP datum with (P1)-(P4), (H2) and (TOT) on the intended physical Hilbert
space". Proposition D supplies that datum given the T0 chain, matched to the account's defining sequence, on the
tr F^2 sector's space H(S). Check 1183's correction of L3-ev (e) ("a one-dimensional invariant subspace" in place
of "a unique vector") does not change items 4-6.

**Verdict.** Row 1219's reading holds after one precision: rows 916-917 supply the datum for (SEED-FP) members, and
the transfer to the centre-blind members of (N-phys) is items 1-6 above. Nothing in Theorem E reads a flux sector,
so no new open input appears. The gap clause therefore stands as: (N-phys) along the account's trajectory, plus the
account's hypotheses and READ statements (the T0 chain), gives the gap on H(S).

**Precisions for the lead (no verdict change).**

- Admissible side. (N-phys) asks 4 | n_j with n_j = L/a_j along the account's spacings. Choosing L as 4 m times the
  coarsest spacing makes every n_j a multiple of 4 whatever the blocking factor (ARGUED, arithmetic); row 1161's own
  admissibility clause was not re-read here.
- Sector. (TOT) is totality in the tr F^2 sector only (check 917 L188). A gap on a larger space of local
  gauge-invariant fields needs their convergence and totality; this is on file as outside the present target
  (`gap-assume-opus.md` L40, item 12; `gap-crux-exercise-astra.md` L340, A1).
- (UNIV-K) of row 916 stays open; it is needed only for the one-K form (row 916 Step 7), not for one datum along one
  defining sequence.

What Step 2 does not do: it does not check the account's statements, and it is not a line-by-line check of row 916
or of check 917. It moves nothing on (N-phys).

## Step 3. A structural fact not on file? (written after 2026-11-20T05:48Z, `date -u`)

None found; no new statement is claimed. The candidates this row formed while choosing the attack, each with its
match on file:

| Candidate formed here | Match on file |
|---|---|
| (N-phys) is a lattice gap with the asymptotic-freedom scale, open at fixed coupling above about 0.36 | row 1180 corollary (check 1187); row 1219 Section 3 (c) |
| Selective quantities (twist ratios, theta sectors) are ratios in which an independent free photon cancels, so they cannot see every neutral level | Lemma PT and Proposition NP (row 1003, lead rule W2 in `parts/gap.md` L97); row 1200 Steps 5-7 |
| Perturbative running changes a quantity by order one only once the coupling is of order one | row 998 6b; row 1200 ("order g^2 per doubling") |
| (N-phys) as a pressure bound at temperature 1/u, by the integral method over the coupling | row 931 (ANOM), `gap-direction-max.md` L186-232; row 1198 Remark TH |
| A neutral gap dominated by charged decay, as in the 2D O(N) singlet half | (SING), (K4-N) (rows 1115, 1194); Theorem BP shows the flux half is not needed; rows 1193, 1213 |
| Positivity in temporal gauge (row 1213, fourth way) | a Haar moment of gauge-invariant functions does not depend on the gauge, so EP-NO (row 744) stands in every gauge for fundamental plaquette monomials; the centre-blind form is row 1213's way 3, OPEN with no consumer |
| A refutation device for (K-flow) inside class K | `parts/gap.md` L97 (none exists in a single model); conformal-window and Georgi-Glashow families are outside class K (L293; `gap-outside-box-max.md` I11) |
| The gap only on the tr F^2 sector | `gap-assume-opus.md` L40; check 917 L188 |

The temporal-gauge remark in the table is one line and elementary (PROVED): Haar measure on the links left after an
axial gauge fixing is the product Haar measure, and a gauge-invariant function has the same Haar integral in any
gauge, so the negative moment of EP-NO (given NS0, row 744) is the same number in temporal gauge. It does not decide
row 1213's centre-blind fourth way.

## For the lead (evidence only; this row edits no other file)

1. Rows 1219, 1224 and this row, all Claude Opus 5.5 max on plain briefs today, reach the same judgement: no attack
   available to a session closes (N-phys), and a further screening has no item it closes or kills. These are three
   runs of one model family, not independent evidence.
2. Step 2 confirms row 1219's reading of the continuum datum, with the precision that the member data change from
   Theorem L3 (e) to Theorem L3-ev under (N-phys) (items 1-6). The gap clause's open inputs are (N-phys) and the T0
   chain (through the account's READ statements and hypotheses); there is no third.
3. Since the gap clause needs the T0 chain anyway, bandwidth not spent on a new (N-phys) mechanism goes to the gap
   clause's other input only through T0's open statements (`library/open-core.md`). The lead decides.

## Summary

- PROVED here: one line in Step 2 item 2 (plaquette-holonomy functions are centre-blind) and one line in Step 3
  (Haar moments of gauge-invariant functions are gauge-fixing independent). Both are elementary and not selective.
- ARGUED (a reading check, each step cited): Proposition D, the continuum datum of row 916 Theorem E transfers to the
  centre-blind members that (N-phys) provides, so the gap clause has exactly two open inputs, (N-phys) and the T0
  chain.
- OPEN: (N-phys); the T0 chain; the mass gap. Nothing disproved.
- No numeric run was made. No home-directory path is written in this file.

RESULT: Mass gap NOT proved, nothing disproved; (N-phys) and the T0 chain stay OPEN. Judgement (ARGUED): no attack available to a session closes (N-phys), which is a lattice gap with the asymptotic-freedom scale at order-one coupling where no small parameter, positivity or bracket gain is on record. ARGUED (reading check): Proposition D, row 916 Theorem E with check 917's corrections transfers to the centre-blind members of (N-phys) (Theorem L3-ev, P-ev, P'-ev of row 1179), so the gap clause on the tr F^2 sector has exactly two open inputs, (N-phys) and the T0 chain; row 1219's reading of the continuum datum holds with that precision. PROVED (elementary, not selective): plaquette-holonomy functions are centre-blind; EP-NO's negative Haar moment is independent of gauge fixing. Claude Opus 5.5 max, Mac mini worker 2; author only, checked by no one. Output library/gap-mini-solve-m-fable.md.
