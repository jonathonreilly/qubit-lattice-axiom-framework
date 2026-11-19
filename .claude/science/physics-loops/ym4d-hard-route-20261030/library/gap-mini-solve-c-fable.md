lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-c-fable (queue row 1190)

Worker: Claude Fable 5.2, max effort, Mac mini worker 3, single session, no subagents.
Pinned commit: f7e5907e5 on `claude/ym4d-hard-route`. Started 2026-11-19T22:59Z.

The problem as the row states it: prove that four-dimensional SU(2) Yang-Mills theory has a
mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (a written argument, checkable by hand, in this file or cited by
path), ARGUED (an argument with a named hole), GUIDE (heuristic or numeric; never a proof
step), OPEN (not established).

Status of this file: in progress. Sections are appended one step at a time.

## 0. Log of steps

- Step 0 (22:59Z): file created; reading FINISH.md, GOAL.md, `parts/gap.md`, `library/open-core.md`.
- Step 1 (23:25Z): orientation read finished (list below). Attack not yet chosen.

## 1. Orientation: what the record holds (read in this run; statements about the record)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-356; `parts/gap.md` L1-104 and L213-322
(formulation, methods 19-36, lead rules, route registry, test table, exact price);
`library/gap-council-synthesis.md`; `library/prior/gap-o4-pinned-cell-read-opus.md` L57-201
(the digest of OpenAI's pinned-cell stiffness iteration for the 2D O(4) model);
`library/gap-mini-free-fable.md` plan, steps 2 and 5. RESULT lines read: rows 720, 1011,
1013, 1016, 1018, 1161, 1174, 1179, 1180, and the briefs of rows 1181-1189.

What I take from it (each item is the record's statement, not mine):

1. The lane reduces the Jaffe-Witten gap clause to one lattice input plus the continuum
   datum: the one-cube physical neutral bound (N-phys) of row 1161 (Theorem BP of row 1179,
   unchecked at this pin; check row 1183 running). By row 1180's corollary, (N-phys) is a
   lattice gap for centre-neutral states at arbitrarily weak coupling with a lower bound of
   asymptotic-scaling type. The continuum datum (the T0 chain) is itself not proved
   (`FINISH.md` L11: "Existence is not proved").
2. The wall in plain words (`parts/gap.md` L33-35): a selective inequality at every scale
   between first passage and the seed size; selective means false for a massless factor.
3. Constraints a route must meet (row 1181 step 2, from `parts/gap.md`): it reads the group
   at order-one response; it cancels between supports before bounding (method 35); it reads
   the whole state space (Lemmas FAC, PT); it averages over the actual Wilson law, because
   every worst-case form is false (Theorem D2, Lemma SHEET, method 36, Theorem BH).
4. The one mechanism on file that crosses the band in a model of the same type is OpenAI's
   2D pinned-cell iteration: stiffness = direct cost minus current variance; a lower bound
   on the current variance comes from the bracket term of a non-abelian Ward identity, by
   Cauchy-Schwarz against a test functional; only an upper bound on stiffness is carried.
   Its direct port to 4D SU(2) fails in the class of all pins (rows 1011, 1016: Propositions
   B, B', Theorem BH), because pure gauge theory has no rigid non-abelian symmetry on the
   link variables (Lemma CEN+) and a lab-frame twist has a mass-form cost (Lemma WN,
   Lemma 5.1a of row 1181).
5. Three earlier Fable seats and row 1181, starting from their own fields, each found the
   lane's map again. So a fresh start from a standard field is expected to add nothing.

