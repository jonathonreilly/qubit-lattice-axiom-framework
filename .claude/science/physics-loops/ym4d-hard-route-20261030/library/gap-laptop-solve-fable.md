lead: anthropic/claude-fable-5-2/medium laptop-subagent

# Row 1217 gap-laptop-solve-fable

Status: file created; work starts below. Each step appends.

Row 1217, Claude Fable 5.2 (medium), laptop subagent, 2026-11-20. Author only; checked by no one. No numeric run. No outside search.

## Step 1. What was read (statements about the record, not mine)

- `parts/gap.md` L1-60 (formulation, the wall (W), the blockage sentence) and its headings.
- RESULT lines of rows 1188-1190, 1193-1195, 1201, 1204 (check 1210), 1209, 1211; the briefs of rows 1188-1217.
- `library/gap-mini-solve-c-fable.md` Sections 1, 2 head, 3.2, 4; `library/gap-mini-neutral-fable.md` R2-R5; `library/gap-crux-restate.md` Lemma A and Lemma K (statements only).
- Not read: the proofs behind rows 720, 1161, 1179, 1180 (the reduction of the gap clause to (N-phys) plus the continuum datum). I rely on their RESULT lines as pointers only.

The record's own summary: the Jaffe-Witten gap clause is reduced to (i) the continuum datum (existence; `FINISH.md` says "Existence is not proved") and (ii) one lattice input, (N-phys): for the transfer operator F of the periodic cube of side n on centre-neutral gauge-invariant states, s(u) = Tr F^u / lambda_0^u - 1 is at most 1/2 for some u at most n/512, at a physical size n along the weak-coupling trajectory.

## Step 2. How best to attack it (GUIDE)

A proof needs two things that no public work holds: the continuum limit with the Osterwalder-Schrader axioms (Balaban's programme gives ultraviolet stability, not the full construction), and a lower bound exp(-c beta) on the lattice gap at weak coupling. The second is the crux. Any proof of it must fail for compact U(1) at weak coupling in four dimensions (massless photon; Guth; Frohlich and Spencer) and must read the non-abelian group at order-one effective coupling, because Balaban's small-field control ends there and the strong-coupling expansion (Osterwalder and Seiler) starts later. I looked for a statement of one of two kinds: (a) an inequality between tori of different shapes that forces the excess free energy to shrink on doubling, or (b) a new form of (N-phys) with a usable average. I chose (a), because reflection positivity holds in all four directions for the Wilson action and gives exact inequalities at every coupling.

## Step 3. The argument tried, and what it gives

Notation. phi(L) = log Z of the periodic torus with sides L = (L1, L2, L3, L4), Wilson action, normalised Haar measure. T_i = the transfer operator in direction i for the cross-section of the other three sides; T_i is positive and trace class and Z = Tr T_i^(L_i).

**Lemma E (PROVED; elementary; a restatement, on file, see below).**
(a) For each i, L_i -> phi(L)/L_i is non-increasing. (b) p = lim phi(L)/|L| exists along all sides to infinity and phi(L) >= p |L|; write e(L) = phi(L) - p |L| >= 0. (c) e(L)/L_i is non-increasing in L_i; so doubling one side at most doubles e. (d) For the cube of side n and time extent u, 0 <= log(1 + s_all(u)) <= e(n, n, n, u), where s_all is s over all gauge-invariant states; the centre-neutral s is at most s_all.

Proof. (a) (Tr T^k)^(1/k) is the l^k norm of the eigenvalue sequence of T >= 0, which is non-increasing in k. (b) Apply (a) in direction 1 and let L1 go to infinity: phi/L1 >= log lambda_0(L2, L3, L4). The right side over L2 is a pointwise limit of functions non-increasing in L2, so it is non-increasing in L2; repeat for directions 3 and 4. The limit of a bounded monotone net exists; phi/|L| is bounded by the plaquette count times a constant. (c) e/L_i = phi/L_i - p |L|/L_i, and the second term does not depend on L_i. (d) log(1 + s_all(u)) = phi(n, n, n, u) - u log lambda_0(n^3), and log lambda_0(n^3) = lim over T of phi(n, n, n, T)/T >= p n^3 by (b). The neutral sector is an invariant subspace that holds the vacuum, so its excited sum is a sub-sum. QED

On file: (a)-(c) are Lemma A and Lemma K of `library/gap-crux-restate.md`; (d) is the content of R2 of `library/gap-mini-neutral-fable.md` and Lemma Z of row 720. Nothing here is new.

**What it gives.** (N-phys) follows from e(n, n, n, u) <= log(3/2) with u <= n/512. Lemma E (c) bounds e from above on doubling by a factor 2. A proof needs the opposite: a factor below 1 at some scale.

**The first failing step (ARGUED).** Every inequality I can derive from reflection positivity in the four directions, positivity of the transfer operators and the Z_2 flux decomposition (Z_twisted <= Z; sector weights in [0, 1]) also holds for the free Maxwell field and for Villain U(1) at weak coupling. For those, e(n, n, n, u) with u = n/512 is of the order of the Stefan-Boltzmann value, about 512^3 times a constant, at every n. So this family of inequalities cannot give e <= log(3/2). The missing input is non-linear in the group and is the same one the record names: the thermal pressure at inverse temperature u must be exponentially small once u exceeds the physical scale. This is R2 and R5 of row `gap-mini-neutral-fable` and Lemma FLOOR of row 988. I found no way past it.

**Kind (b), checked against the record.** The chi-square form of s(u) over vacuum-typical starts is 3.2 of row 1190. The cross-channel reading of the torus is R2 above. I produced no form that is not on file.

## Step 4. What failed and what is left

- Failed: route (a). It reproduces Lemmas A, K, Z of the lane and stops at the massless floor.
- Not attempted: a (K-flow) statement (an inequality carried from first-passage data through the band). I have no candidate step that fails for U(1) and that I can prove.
- OPEN, unchanged: (N-phys); (W); the continuum datum (existence); the mass gap of four-dimensional SU(2) Yang-Mills in the sense of Jaffe and Witten.
- This run adds no new proved statement to the lane. It is a fourth-or-later independent recovery of the same map from reflection positivity alone, at lower effort than the Mini seats; it should not be counted as new evidence, since the same model family wrote the earlier seats.

Credits: Balaban (ultraviolet stability and effective actions); Osterwalder and Seiler (reflection positivity and the strong-coupling gap); Sussman and Alpoge, with Claude and Codex as authors of their text (the account the lane ports); Chatterjee (probabilistic formulation of the problem); Tomboulis and Yaffe (twist inequalities); Jaffe and Witten (the problem statement); the lane rows cited above.

RESULT: Row 1217 (Claude Fable 5.2 medium, laptop subagent; author only, checked by no one; no numeric run, no outside search). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved. Attack chosen: shape inequalities for the periodic torus from reflection positivity in all four directions. PROVED, elementary, already on file (Lemmas A and K of gap-crux-restate, Lemma Z of row 720, R2 of gap-mini-neutral-fable): Lemma E, the excess free energy e(L) is non-negative, e/L_i is non-increasing, and log(1 + s(u)) <= e(n, n, n, u). ARGUED: the route stops at the massless floor, because every inequality of this family holds for the free photon, whose excess does not shrink. No new proved statement. OPEN, unchanged: (N-phys), (W), the continuum datum, the mass gap. Output library/gap-laptop-solve-fable.md.
