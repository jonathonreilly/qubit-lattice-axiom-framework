lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T12:45Z

# gap-unit-max (FINISH row 988): the unit-scale inequality (U1) or (U2), direction item, crux lemma

Worker: Claude Fable 5.2, max effort, Mac mini worker 1, one session, no subagents. Pinned commit 708bcda9e.
This is research-stage working state. Nothing here is a claim that the mass gap or any part of it is proved.
Marks used: PROVED (every step written here, by hand), ARGUED (argument written, a step is not complete),
OPEN, RECALLED (a literature statement quoted, not rebuilt here), GUIDE (numeric, can refute or guide, never prove).

## 0. Plan (at most eight steps; one step per response; each step appends its result here before the next)

1. Scope: the object and the goal as stated in row 982 Section 4.1-4.3 (statement only, no route text);
   duplicate check (rule 0a) against `library/open-core.md` and the FINISH rows.
2. At least three approaches of my own, written from the goal and the object before any route file or digest is read.
3. Fact tests on each approach, one verdict each: Lemma CAP, Lemma COUNT (row 982, checked in row 984);
   Theorem D2 (row 977, checked in row 979); Lemma META (row 975); the square-root test (row 978 5.7);
   free photon; compact U(1); frozen Q_8 and 2T; K7; FT-FK.
4. Attack on the crux lemma of the best approach, stage 1.
5. Attack, stage 2 (or the second route if stage 1 fails).
6. Attack, stage 3 (or the third route; a GUIDE run only with criteria written first and under the numeric lock).
7. Read rows 720, 970, 975-986; say per approach whether it is already there.
8. Verdicts, marks, what stays open, the next step, one RESULT line.

## Status log (UTC, read from `date -u`)

- 2026-11-15T00:45Z: session start; row 988 read (FINISH.md line 1065); output file created. No earlier run of this
  item exists at the pinned commit (`library/gap-unit-max.md` and `library/guide/lane988/` were absent).

## Step 1. Scope, object, goal, duplicate check

**Read so far (statement only):** GOAL.md; FINISH.md lines 1-84 and row 988 (line 1065); `library/gap-hcphys-max.md`
lines 1-22 and Section 4.1-4.3 (lines 117-163). No route text (its Steps 5-7) and no digest was read before Step 2.

**Object.** B is the cube of physical side 2 ell. The gauge-invariant transfer operator on B at the unit-scale
effective weight has energies E_0 = 0 < E_1 <= E_2 <= ... . For real t > 0 (lattice units of time):
S(t) = sum over i >= 1 of e^(-E_i t), X(t) = log(1 + S(t)) = log Z(B x t) - t * (vacuum rate), U(t) = -X'(t).
By (EX) of row 982 4.1, X is the same number for the fine weight and for the blocked weight.
The family: bare couplings g_0 with first-passage cutoff K, unit coupling in the window [g^(-2), g^(-2) + B_sharp]
(CA-I 631-683, Definition 1.2). The cube has e^(c/g^2) unit cells per side if masses scale by asymptotic freedom.

**Goal (row 988).** One of:
- (U1): ||P^(mT) g||_2 <= ||g||_(1 + e^(-2 alpha_* m)) for g = p_s(u, .), all integers m >= 0, alpha_* > 0 free of the cutoff;
- (U2): X(t + 2mT) <= (1 - tanh(alpha_* m)) X(t) at t = tau_0/a_iota, all m.
(U3) is not a goal form: row 984 corrected row 982, (U3) implies (U2) and not the converse.

**What (U2) says in plain terms (my reading, PROVED from the definitions).** 1 - tanh(alpha m) = 2/(e^(2 alpha m) + 1).
So (U2) is: the excess free energy X of the periodic box decays by a rate 2 alpha_* per unit of time, starting at the
time tau_0 where X is still of the order of the volume, Theta(ell). The gap alone gives decay only after the time t_c
where S(t_c) <= 1 (Lemma EE (d)). Between tau_0 and t_c the statement is about the number of states of the box
(Lemma COUNT). Row 988 says row 982 failed there three times: "the thermal sum of the cube between the hot end and
the cold range".

**Duplicate check (rule 0a).** `library/open-core.md` (564 lines): no line with (UNIT), (U1), (U2), unit scale,
HC-phys, LSI-traj-seed, Z-UNB or BDD-Delta. FINISH rows with (UNIT), (U1) or (U2): 982 (the source), 984 (its check),
988 (this row); row 635 matches only by a different (U1). Named matches stated by row 982 itself: (Z-UNB) and
(BDD-Delta) of row 720 Theorem ZD; (LSI-traj-seed) of row 970. Row 988 assigns this lemma to this lane, so the attack
is not a duplicate; rows 720, 970, 975-986 are compared in Step 7.

