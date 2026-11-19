lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-b-fable (queue row 1189)

Pinned at commit f7e5907e5 of `claude/ym4d-hard-route`. Research-stage working state. It grants no status. Nothing here is a public claim.

**The problem (row 1189).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

**Labels.** Each statement below carries one of: PROVED (every step written here or in a cited checked note), ARGUED (an argument with a named unproved step), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

**Process.** One step per response. Each step is appended here before the next one starts.

## Step 0. Plan (written before reading the earlier work)

1. Read the earlier work on the gap: the FINISH.md RESULT lines for the gap rows, `parts/gap.md`, `library/open-core.md`, and the notes the newest gap rows name. Record what is established and what is open. No duplicate attack (rule 0a).
2. Choose one line of attack on the first open statement the gap needs. Say why it is not a repeat.
3. Carry it through, or name the first step that fails, with the explicit failure.

(Steps follow.)

## Step 1. What the earlier work fixes (read, not re-derived)

Sources read at this pin: `FINISH.md` rows 1007-1018 and 1179-1187 (RESULT lines), `parts/gap.md` L1-104 and the route registry L223-267, `library/gap-council-synthesis.md` in full, `library/gap-mini-branch-fable.md` L300-312. None of these is evidence by itself. Each says where a proof and its check are.

1. **The target splits in two (rows 1179, 1065; check row 1183: main chain HOLDS AFTER CORRECTION).** The Jaffe-Witten gap clause follows from (i) the continuum datum of the T0 chain (existence, with (H2), (TOT)), which is OPEN, and (ii) one lattice estimate, (N-phys), which is OPEN. The Wilson branch selection (BS) enters only the wall (W) as worded (confinement on tori), not the gap clause.
2. **(N-phys) (row 1161, `gap-solve9-astra62.md` L146-148).** At one admissible physical side L, for every cutoff index j >= j_0, with n_j = L/a_j, there is an integer u_j with 3 <= u_j <= n_j/K and s_+(u_j; n_j^3) <= 1/2. Here s_+ is the periodic centre-neutral excited trace of the cube n_j^3 in units of its vacuum. Rows 1180 and 1184 (two independent attacks, unchecked at this pin; check row 1187 running): (N-phys) is a neutral lattice gap at arbitrarily weak coupling together with an upper bound of asymptotic-scaling type on the seed size. Nineteen routes ended at steps already on file.
3. **The map.** Route families RA-RG, LC, BR-2, (T-pin), (DS-W), (A) and methods 1-36 of `parts/gap.md`. The common verdict (row 998 6b): every engine found is blind, and no input excludes the massless branch beyond first passage. Comparison cases that a proof must fail on: compact U(1) at weak coupling, frozen Q_8 and 2T, the K7 endpoint (mixed action), the free photon, a product with a massless factor.
4. **The 2D precedent (rows 1007-1010, reading only).** The posted 2D O(N) proofs cross the band by a stiffness iteration on pinned cells. The gain per scale is a commutator (curvature) term. Rows 1011, 1016, 1018 (Fable 5.2 max, with gpt-6-astra checks): the direct port fails in the class of all pins (Propositions B, B', Theorem BH). SU(2) has the bracket and no symmetric continuous twist. Compact U(1) has the twist and zero gain.

So the open lattice statement is one sentence: **a selective gain at order-one response**. Step 2 chooses the attack.
