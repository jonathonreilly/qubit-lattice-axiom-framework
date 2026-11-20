lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T15:11Z

# gap-mini-solve-j-fable (queue row 1200)

Research-stage working state. Nothing here is a public claim, and nothing here grants status.

Item: FINISH.md queue row 1200, `gap-mini-solve-j-fable`. The problem as the row states it: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Pinned commit: 3c181a68c on `claude/ym4d-hard-route`. Start time (date -u): 2026-11-20T03:11Z.

Labels used below: PROVED (every step written here or in a cited checked file), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

## Step 0. Save protocol

This file was created before any proof work. Each step below was appended when it ended.

## Step 1. What was read before choosing an attack

Read at the pin, in this order (no proof work yet):

- `GOAL.md` in full; `FINISH.md` L1-84 (state, method), L299-360 (joining, efficiency, rules), the row of this item (L1281).
- `parts/gap.md` L1-104 (formulation, the wall (W), methods 19-36, lead rules) and L223-322 (route registry, test table, the exact price).
- The RESULT lines of the plain-brief rows 1188-1190, 1193-1195, 1197, 1199, 1201 (Claude Fable 5.2), rows 1205-1208 (Gemini Argon and its checks), rows 1209-1211, 1214, 1216-1218.
- `library/gap-mini-branch-fable.md` Sections 5-6: (N-phys) and Theorem BP (the gap clause given the one-cube neutral bound and the continuum datum).
- `library/prior/gap-o4-pinned-cell-read-opus.md` L57-200: the reading of OpenAI's pinned-cell stiffness iteration for the 2D O(4) model (credit: OpenAI, posted and unrefereed).
- The RESULT lines of rows 1007, 1009-1011, 1013, 1016 (the readings of the 2D proofs and the three gauge ports).

What this reading fixes for the present row (all on file, nothing new):

1. The lane's reduction ends at (N-phys): one bound s_+(u; n^3) <= 1/2 on the centre-neutral excited trace of one cube of fixed physical side, with u <= n/K, at every cutoff. With the continuum datum it gives the gap clause (Theorem BP, row 1179). (N-phys) is an infrared statement of the same strength as the gap.
2. Eight plain-brief rows screened about 100 route candidates and found each one on the lane's map. This row does not screen again.
3. The one mechanism that crosses the band in a comparable model is the 2D pinned-cell stiffness iteration. Its gauge ports stop at the same place each time: a link translation has no cost form that is a curl form in a rough non-abelian field (rows 1011, 1013, 1016, 1188, 1193, 1197).

## Step 2. Candidates derived in this row and their matches on file (GUIDE; no new route)

Each line is: the idea as I derived it, then the place where the lane already holds it. Every match was found by `grep -n` in `library/gap-*.md`, `parts/gap.md` or the FINISH rows before the idea was worked. Nothing in this step is new.

| Idea derived here | Where it stops | On file |
|---|---|---|
| Stiffness of a pinned 4D cell to an abelian boundary twist as the monotone of a 2D-type iteration | no curl-form cost in a rough field; pin supremum forgets colour coherence | rows 1011 (Propositions B, B'), 1013 (Lemma WN), 1016 (Theorem BH) |
| Two-sided torus action on each link, with corner defects | the corner defects of a constant-curl twist grow with the box | row 1013 C1, row 1193 Lemma PC-c |
| The start ("blind") bound is itself the sign of asymptotic freedom; a charged scalar gives the opposite sign | no mechanism for a size-uniform upper bound of a twist response | row 1051 (`gap-direction3-max.md` 5.3: (BDD-Delta), (BL), (BL-c), (L1); L554-560 names the diamagnetic inequality of Brydges, Frohlich and Seiler) |
| The exact variational form of the response with field-dependent extensions (score of a non-constant field, Bochner term) | needs a field-built frame whose Jacobian cancels the frame defect | row 1128 (NL-gen), row 1034 (STAR, PRIV), row 1141 (OPEN item) |
| Adapted (time-ordered) frames have unit Jacobian | frames decohere with depth; bound of order beta^(2/3) L | row 1051 (Lemma RM, RM-TREE; attempt 2 of 5.3) |
| Heat-kernel Hessian bounds in the time direction (Hamilton's matrix Harnack inequality on a compact group) as a pin-uniform blind bound for the electric part | it is the ambient convexity of the one-step kernel; the magnetic Hessian in lab directions is not a curl form | row 941 (exponential family, Hess Lambda), rows 944, 950 ((SC) and its guide-level failure) |
| Araki-Lieb-Thirring comparison of Tr T^L with a classical (dimensionally reduced) partition function | loses the vacuum normalization; extensive | rows 913, 1180 (Lemma R4), `gap-constraints-max.md` B6 |
| The non-central family Z(K), K a commutator of two constant colour twists, as a path from the periodic to the centre-twisted torus | the response at K = 1 is of area order | row 1013 C2, row 1051 Lemma K4 |
| (BDD-Delta) from monotonicity of the excess free energy in each side | only the volume-order bound e(2L) <= 16 e(L) follows | Lemma E of row 1217; Lemma ADD of row 1018 |
| Charged-to-neutral conversion in a twisted 2D O(4) sheet | frustrated abelian examples keep neutral order with charged decay | rows 1115, 1139, 1194 ((SING), method 36) |

Reading of the table (ARGUED, same as rows 1051 and 1197): in the 2D engine the start bound is free and each mode lowers the stiffness. In 4D the response to a background field has two one-loop parts of opposite sign (orbital and spin; Nielsen 1981, Hughes 1981). So an induction that carries only upper bounds on cell stiffness has no sign for the orbital part. This is the reason the direct ports stop, and it is on file.

