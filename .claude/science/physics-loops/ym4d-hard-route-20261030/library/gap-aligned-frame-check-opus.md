lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T12:19Z

# Check of row 1026, `library/gap-aligned-frame.md` (row 1027)

Check by Claude Opus 5.5 max, Mac mini worker 2, of the note written by Claude Fable 5.2 medium. Same provider, so this is not an independent check in the sense of the working rules. Branch `claude/ym4d-hard-route` at 730539c63. Started 2026-11-16T00:19Z (from `date -u`). No new attack: verdicts only.

## Plan (at most eight steps)

1. Read the note in full, and its inputs: `parts/gap.md` (the parts it reads), `library/gap-short-step-max.md` Sections 4.1-4.5 (FLOW, PROJ, FR+, SPLIT, route (ii)), check `library/gap-short-step-check-opus.md` L220-290, Lemma FR of `library/gap-pinned-cell-gauge-max.md` 7.3. Fix the definitions: current j, Jacobian current d, aligned frame, reducible.
2. Test first (a): the sign and normalisation of Psi = - sum theta_l (j_l - d_l), against Lemma FLOW.
3. Test first (b): whether the abelian base point lies in the non-reducible configurations the theorem needs.
4. Test first (c): Lemma RANK by hand on the smallest case.
5. Check the one-cube construction (n orthogonal to the outgoing forces, j = 0), line by line.
6. Check Theorem E: the implicit function theorem at the abelian point, the open gauge-invariant set, positive Wilson measure.
7. Check the cost identity and its link to FLOW, and the cube example (alignment does not give a curl form).
8. Judge the ARGUED (SYM) step; write verdicts (HOLDS, HOLDS AFTER CORRECTION, FAILS with first failing line) and the RESULT line.

## Step log

(Each step appends its result below before the next starts.)

### Step 1 (done): sources read, definitions fixed, overlap

Read in full: the note `library/gap-aligned-frame.md` (304 lines; its author pinned fe79776a6; last relayed in ad923e265, unchanged at 730539c63, which is the text checked here); `library/gap-short-step-max.md` 4.1-4.5 (L213-277); `library/gap-short-step-check-opus.md` L215-292 (D2 at L227, L281); `library/gap-pinned-cell-gauge-max.md` 3.1-3.2 (L131-182), 4.3 (Lemma CEN, L263-292), 7.3-7.4 (L460-501); `parts/gap.md` L130-142.

Definitions used below (conventions of row 1011 3.1-3.2).
- SU(2) = unit quaternions, su(2) = Im H = R^3, t(g) = Re g, s(g) = Im g. Link l = (x -> y), gauge U_l -> g_x U_l g_y^(-1). Plaquette p = (x; mu, nu), U_p = U_1 U_2 U_3^(-1) U_4^(-1).
- A link field b acts by U_l -> e^(eps b_l) U_l. X(b) = d/d eps A(e^(eps b) U) = - sum_l b_l . N_l. So N_l is minus the gradient of A in link l, in the frame of the tail.
- Frame: unit vectors n_x(U), gauge covariant. j_l = n_tail(l) . N_l. D_l n = n_tail - Ad(U_l) n_head. (div j)(z) = sum over tail z minus sum over head z.
- d_l = sum_a R_(l,a) n^a_tail(l), with R_(l,a) f = d/d eps f(U_l -> e^(eps e_a) U_l). Each R_(l,a) is divergence free for Haar measure.
- Aligned frame: div j = 0 at every free site (AF-1). Reducible: some frame has D n = 0. By Lemma FR this forces all plaquette axes at each site to be parallel. So "non-reducible" holds wherever |s_p x s_q| is non-zero for two plaquettes p, q based at one site.

I re-derived the Gauss law PROJ (ii) and PROJ (iii) from these conventions (gauge generator at z: b_l = lambda a on links with tail z, b_l = - lambda Ad(U_l) a on links with head z). The identity (div j)(z) = - sum over head z of (D_l n) . N_l (note L43) holds. Direct proof: n_z . (sum over tail z of N_l) = n_z . (sum over head z of Ad(U_l)^(-1) N_l) = sum over head z of (Ad(U_l) n_z) . N_l.

Overlap (rule 0a). This row is a check, and no new lemma is attacked. Grep of `library/open-core.md`, `library/l17c.md` and the FINISH rows for "aligned", "(SYM)", "j - d conserved", "Jacobian current": the only hits are rows 1022, 1026 and 1027. The other hits are LaTeX `aligned` environments and unrelated rows. Grep of `library/sa-index/` for abelian projection, colour field, Faddeev and Cho: 4 files. The hits are Faddeev-Popov identities (CA 7660-7681, 21103-21111, 51742-51750) and the account's "one-colour fields" (CA 7215-7234, 7428, 12947-12956). None of them is a unit colour frame with a conserved projected current. So the Sussman-Alpoge account has no statement that this check could port or cite. The note's own statement on this (L294-295) holds.
