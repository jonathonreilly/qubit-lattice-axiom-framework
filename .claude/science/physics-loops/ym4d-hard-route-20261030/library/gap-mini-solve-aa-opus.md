lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:01Z

# gap-mini-solve-aa-opus: mass gap for 4D SU(2) Yang-Mills (FINISH row 1244)

Started 2026-11-20T09:01Z on the Mac mini worker, branch `claude/ym4d-hard-route`, pinned at commit e3efb7b0d.
Labels: PROVED (written argument complete here), ARGUED (argument given, a step not fully written), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## 0. Status of this file

Step 0 (reading) done 09:25Z; Step 1 (judgement) done 09:27Z; Step 2 (the stiffness split at one loop) in progress.

## Step 0. Reading log (reading only; no new claim; written 2026-11-20 about 09:25Z by date -u)

Read at the pin e3efb7b0d: GOAL.md in full; FINISH.md L1-85 and L299-352 (state, how we work, joining, working
efficiently, rules); row 1244 (this row) in full; the RESULT lines of rows 1188-1202, 1212-1213, 1219-1220, 1224-1225,
1228-1229, 1233, 1237-1238, 1243 (files `library/gap-mini-solve-a-fable.md` to `-z-opus.md`); `parts/gap.md` L1-104
(formulation, the wall, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-mini-solve-z-opus.md` Steps 0-1 (row 1243); the plans of the running sibling rows 1234 (v-opus, Section 2)
and 1241 (y-opus, Step 0) as they stand at this pin.

Where the problem stands on file (cited, not re-derived):

1. Consumer side. Beside the premises of Sussman and Alpoge's complete account, the Jaffe-Witten gap on the
   account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1179 Theorem BP, check 1183; row 1225
   Theorem E-N, check 1232).
2. (N-phys) (row 1161; row 1179 L304-310): at one physical side L, for every cutoff j >= j_0, some u_j with
   3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where s_+ is the centre-neutral excited trace of the
   vacuum-normalised periodic transfer matrix on the spatial cube n_j^3, and K is fixed first.
3. Modulo the ultraviolet carry (UNIV-K), the crux is a finite seed for Wilson SU(2) at one fixed coupling in the
   account's window, where the running coupling is of order one (rows 1225, 1229, 1233, 1237, 1238).
4. About 45 engine families are screened with named failing steps (methods 1-36 of `parts/gap.md`; rows 1189, 1194,
   1199, 1200, 1229, 1237). This includes the orbit-space curvature route (Singer, Feynman; O'Neill's term), which is
   item 27 and G9 of `library/gap-brainstorm-max.md` and input 10 of row 1003's check.
5. Row 1218's published inputs (A: Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy; B: the
   first four authors; C: Zeng Chunping) give a full thermal one-scale seed with a proved conditional ascent (A),
   cube-dynamics criteria and a weak-coupling Poincare bound for straight-path block variables (B, Corollary 166;
   not selective by row 1220), and common-rate criteria (C). None proves the Wilson estimate at weak coupling.

Siblings on the same brief at this pin: rows 1234 (v: the thermal count at one coupling), 1241 (y: Step 1 not yet
written), 1243 (z: the sign of the non-abelian frame response, reduced to (S-V)), 1246 (gpt-6.2-astra), 1248-1249
(queued). This row keeps its item distinct from theirs.

## Step 1. How best to attack it (judgement; ARGUED; written 09:27Z by date -u)

**1.1 What a proof has to contain (cited, not new).** Beside the T0 chain, the gap clause reads one lattice estimate,
(N-phys) (Step 0, item 1). Modulo the ultraviolet carry, (N-phys) is a finite seed for Wilson SU(2) at one fixed weak
coupling beta_0, on a box of side of order exp(c beta_0) lattice units (rows 1180, 1225, 1233, 1238). The 2D analogue
shows the shape of a possible proof: OpenAI's 2D O(3) construction needs, at one bare coupling, only a non-sharp
mixing length X(b) = C exp((4 pi - eta) b), and its renormalization group carries that one bound to every finer
cutoff (rows 1009, 1010). So in 4D the crux is the classical open problem in its weakest useful form: exponential
clustering, at any rate, of 4D lattice SU(2) at one weak coupling, with a thermal count. The seed box sits where the
running coupling is of order one.

**1.2 What kind of input can do it (cited).** Lead rule W2 of `parts/gap.md`: (K-one), a property of the measure at
one scale in the band, or (K-flow), a step carried through the band by an identity that fails for U(1), for frozen
groups and for products with a massless factor. A (K-one) seed needs a number at the band, and no hand expansion
reaches the band (character ratio about 0.48-0.52 there, about 0.045 at the hand-proved strong-coupling edge, row
1229); GOAL.md forbids a computed certificate. A (K-flow) step needs an exact identity with a non-abelian sign at
order-one response; the identities on file do not give one (row 1243 Step 2.2: gauge Ward identities move no
gauge-invariant datum, link symmetries are central (CEN, CEN+), lattice symmetries are finite, Schwinger-Dyson
equations need a small parameter, reflection positivity is blind).

**1.3 My own screening, each candidate grepped before any work (rule 0a).** I listed the band-crossing ideas I know
and searched the lane folder for each. Counts are files under `library/` and `parts/` that name the idea.

| Candidate | What it would use | On file |
|---|---|---|
| Curvature of the orbit space (Singer; Feynman 1981; O'Neill's term) | positive curvature added by the gauge quotient, zero for U(1) | yes: `gap-brainstorm-max.md` items 27, G9; input 10 of row 1003 (check row 1006): its consumer (Bakry-Emery) stops near beta 1/8; uniform curvature forces a trivial limit (row 1237 Proposition UNI) |
| Non-abelian unwinding of abelian flux (no conserved integer flux in SU(2)) | a 2 pi abelian flux is contractible in SU(2), not in U(1) | as a property: row 878 C4; as the flux and w_2 picture: brainstorm items 47, G18, rows 809-810; as the twist stiffness: rows 1011-1018, 1228, 1243 |
| Paramagnetic sign of gluon spin (Nielsen-Hughes split 11/3 = 4 - 1/3; Nielsen-Olesen unstable mode) | the spin term of the fluctuation operator | yes: row 1011 L496 (RECALLED), row 1195 (HM), brainstorm item 11 ("no step from saddle to free energy") |
| Topological charge, theta dependence, self-dual 't Hooft-symbol identification of Lambda^2_+ with su(2) | pi_3(SU(2)) = Z, absent for U(1) on R^4 | instantons in 43 files; theta dependence in 2 (rows 1200 and one other); the 't Hooft-symbol identification in 0. I found no inequality it yields: the identification is a fixed linear map, U(1) has the same spacetime group, and the non-abelian gauge-invariant cubic tr(F[F,F]) enters no exact identity I know |
| Dual weak coupling, as in Gopfert and Mack's 3D U(1) proof | a dual description that stays weakly coupled at all scales | yes: rows 859 (item 34), 1201 table item 8, 1237 Step 1.2 (dilute defect gas). In 4D SU(2) the defects at the physical scale are not dilute (their fugacity exp(-c/g^2(L)) is of order one at the band), so no small parameter is left |
| Conformal-window comparison (AF with a gapless infrared) | a test, not an engine | yes: row 998 C18 (outside the class K; BELIEF) |
| Loop equations, Nishimori line, positivity, chessboard, Lee-Yang, continuity in beta, Migdal-Kadanoff, Tomboulis, thin twisted torus, five-dimensional test | | all on file with a named failing step (methods 1-36 of `parts/gap.md`; rows 754-760, 797, 842, 1017, 1084, 1190, 1213) |

**1.4 Judgement.** I found no engine of a new kind. The one structure I found unused, the identification of
self-dual 2-forms with su(2), gives no inequality that I can see (row of 1.3), so I do not open it as a route. This
agrees with rows 1219, 1225, 1229, 1237, 1238 and 1243. Row 1243 (Step 3.4) counted 59 solve-type rows between 1141
and 1246 and 53 RESULTs, all with the gap open; the missing (K-flow) identity is the same object since row 1013.

**1.5 What this row does.** Rule 0a forbids attacking a listed open lemma ((S-V), (DEC), (HM), (GC), (CAS) and the
rest are listed). An off-map engine is not available. So this row spends its effort on one question that is not
listed, is decidable in a session, and bears on every future (K-flow) row: **where, in the exact stiffness split of
Lemma FLOW (row 1018), does the one-loop asymptotic-freedom decrement of 4D SU(2) sit, compared with the 2D O(N)
models whose band-crossing proofs exist?** If the decrement sits in the variance term for every extension of a
given class, a Jensen-type (direct-term) argument with that class cannot capture asymptotic freedom even at weak
coupling, and (S-V) is impossible in that class; if it can sit in the direct term, the lane gets a weak-coupling
model of the extension it needs. I first check that this exact question is not on file (Step 2.0).
