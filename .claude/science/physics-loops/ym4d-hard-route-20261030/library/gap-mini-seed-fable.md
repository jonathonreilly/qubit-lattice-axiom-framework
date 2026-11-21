lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T23:35Z

# gap-mini-seed-fable (queue row 1363): Mini Fable on the neutral seed

Pinned at commit 767a6b4e5 of claude/ym4d-hard-route. Started 2026-11-21T11:35Z (date -u). Nothing in this file is checked.

## Status log

- 2026-11-21T11:35Z (date -u): file opened; reading the queue row, GOAL.md and the FINISH.md rule sections.

- 11:36Z (date -u): read GOAL.md, FINISH.md L1-90 and L299-358 (rules), the queue row, the RESULT lines of rows 1340-1362, gap-phys-seed.md L296-326 (Theorems ZD, ZD-c, the two lead notes), row 1356 Sections 1-3 (Lemma M1, Corollary M2), row 1353 Sections 2 and 6 ((N-phys), Corollary BT2, (M-neutral)).
- 11:53Z (date -u): read `parts/gap.md` L1-104, the RESULT lines of rows 1318-1339; ran two registry greps (72 terms; counts in Section 1.2). Section 1 written.

## 1. Inputs, repo search, and the statement in plain terms (written 11:53Z, `date -u`)

### 1.1 The statement

Notation of row 1356, Section 2 (`library/gap-mini-mneutral-fable.md` L78-84): n^3 is the spatial box, T the Wilson
transfer operator on gauge-invariant functions of one time slice, P_0 the mean of the eight centre translations,
lambda_0 the vacuum eigenvalue, x_a = lambda_a/lambda_0 the relative neutral eigenvalues, s(u) = sum over a >= 1 of
x_a^u, Z_+(t) = Tr(P_0 T^t) = lambda_0^t (1 + s(t)).

- (M-neutral), row 1353 6.3: there are an admissible physical side L and, for all late j, an integer w_j <= n_j/1024,
  a unit vector phi_j and c_j > 0 with Hilbert-Schmidt norm(P_0 T_j^(w_j)/c_j - |phi_j><phi_j|) <= 2/5.
- By Lemma M1 and Corollary M2 of row 1356 (check 1359: hold) this is s_j(2 w_j) <= 4/21, that is
  lambda_0^(2w) >= (21/25) Z_+(2w).
- (N-phys), row 1342 L93-94: s_j(u_j; n_j^3) <= 1/2 with 3 <= u_j <= n_j/512, 4 | n_j, n_j >= 2^70.
- Coupling range: beta_0 <= beta_j <= B_0 log(L/a_j) (lead note after Theorem ZD-c, `library/gap-phys-seed.md` L322).
- Consumer: rows 1161, 1179, 1342 with checks 1162, 1183, 1349 (the Jaffe-Witten gap clause from (N-phys)).

### 1.2 Repo search (rule 0a, "Repo first")

`library/open-core.md`: `/usr/bin/grep -n -i -E "neutral|N-phys|M-neutral|mass gap|rank-one"` returns no line, as rows
1353 and 1356 found. The statement is owned by the gap lane: rows 895, 920 ((GLUE-FP)_sigma), 1161, 1180, 1184, 1342,
1353, 1354, 1356, 1358, 1360 and their checks. Row 1364 (`gap-mini-seed2-fable`) runs the same brief in parallel on
worker 2; I did not read it.

Before choosing an attack I counted lane files (`library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md`) that
contain each of 72 terms, one term per mechanism I considered. All mechanisms with a known name are on file:
log-Sobolev 92 files, Bakry 115, chessboard 113, Tomboulis 116, Villain 174, Seiler 194, Chatterjee 109, anisotrop 108,
string tension 87, small-volume 63, van Baal 57, Dobrushin-Shlosman 51, finite-size criterion 40, orbit space 39,
hypercontract 42, 1-form 32, Elitzur 31, trace anomaly 23, O'Neill 22, Koller 21, step scaling 21, Feynman-Hellmann 18,
interaction measure 16, Goldstone 12, Hagedorn 7, femto 5, tensor network 5, Karabali 4. Terms with 0 or 1 files:
"heat kernel action" 0, "cutoff phenomenon" 0, "warm start" 0, "Nash inequality" 0, "ultracontract" 1, "finitary" 1,
"entropy density" 1, "Lipschitz in beta" 1. So a new list of mechanisms is not a contribution (the lesson of rows
1188-1259), and this row does not write one.

Cross-branch search (main and the open YM4D pull requests): not repeated. Rows 1351 and 1353 record it for the same
statement on 2026-11-21 with no proof of the neutral seed found.

### 1.3 What the statement says in physical terms (GUIDE; arithmetic only, no claim)

For a theory whose lightest neutral state has mass m and a one-particle band of the usual form, in a box of side
n = r u at time u (lattice units), s(u) is about r^3 (u m/(2 pi))^(3/2) e^(-u m). At the least aspect ratio that
(N-phys) allows, r = 512, the bound s(u) <= 1/2 needs u m - (3/2) log(u m) >= 16.65, that is u m about 21.5 and a
box of side about 1.1 x 10^4/m. In thermal words: at the temperature T = m/21.5 the neutral pressure obeys
p/T^4 <= log(3/2)/512^3 = 3.0 x 10^(-9), against pi^2/15 = 0.66 for three free colours. So the statement is true for
any massive theory with a normal count, it is false by eight orders of magnitude for free gluons, and it sits at a
size 10^4 times the correlation length. Row 931 has the same reading for the periodic seed (`gap-direction-max.md`
L186-232, "(ANOM)").

