lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:58Z

# gap-mini-neutral-fable: the one-cube physical neutral upper bound

FINISH row 1180 (`gap-mini-neutral-fable`). Status marks: PROVED, ARGUED, GUIDE, OPEN. No subagents.

**Provenance of this file.** An earlier run of this item (Claude Opus 5.5 at max effort, started
2026-11-19T21:48Z by its own `date -u`, pinned at commit 0d6295dd9) wrote only a header and the plan
below; its header lines were `lead: anthropic/claude-opus-5-5/max mac-mini-worker` and
`lease_until: 2026-11-20T09:48Z`. This session (Claude Fable 5.2 at max effort, started
2026-11-19T21:58Z by `date -u`, pinned at commit 3b1d5e14f on branch `claude/ym4d-hard-route`)
keeps that plan and continues from it. All mathematical content below is from this session.

## Plan (earlier run, kept; written before reading the chain)

1. Read the row's required sources: `library/gap-council-synthesis.md`, `parts/gap.md` (methods 1-36,
   route registry), RESULT lines of FINISH rows 1143-1177, and the defining texts of the "one-cube
   physical neutral upper bound" in rows 1161, 1175, 1177 (`gap-solve9-astra62.md`,
   `gap-solve16-astra62.md`, `gap-solve17-astra62.md`).
2. Write down the exact statement of the bound (call it N1) with every quantifier, and record what is
   already on file about it (grep open-core.md and FINISH rows; stop if another row covers it).
3. Attack: try to prove N1, or disprove it, or prove the strongest true statement toward it; for
   every route tried, record the precise obstruction.
4. One RESULT line at the end.

Each step below is appended as it finishes.

## Step log (this session)

### Step 1. The exact statement, and what is on file (reading only; no new claim)

Written 2026-11-19T22:04Z (`date -u`).

**Setting (row 1161, `gap-solve9-astra62.md` L13-63; credit: the positive transfer and trace identity GL8 of
Sussman and Alpoge, with Claude and Codex as authors of their text; Balaban for the ultraviolet trajectory).**
Wilson SU(2) at coupling beta on the periodic spatial cube n^3, 4 | n. F is the symmetric magnetic sandwich
(the positive transfer operator on gauge-invariant functions of the spatial links), lambda_0 = ||F||, G = (Z/2)^3
the centre flips. X_{m,q}(u) = Tr_q (F_m/lambda_0)^u for static magnetic twist m and electric character q, in
units of the periodic vacuum. The periodic neutral excited sum is

    s(u; n) = X_{0,0}(u) - 1 = sum over excited neutral levels of (lambda_i/lambda_0)^u.

**(N-phys), the one-cube physical neutral upper bound** (row 1161 L146-148 and L215; in the wording of row 1179,
`gap-mini-branch-fable.md` Section 6): there is one admissible physical side L and an index j_0 such that for
every j >= j_0, with n_j = L/a_j and 4 | n_j, there is an integer u_j with 3 <= u_j <= n_j/K and

    s_j(u_j; n_j) <= 1/2.

K is the aspect of row 1161's finite-aspect statement; the explicit version is K = 512 with n_j >= 2^70
(row 1161 L215). Rows 1175 and 1177 read the same premise (row 1175 L59 "row 1161's short-period periodic
neutral premise at one permitted physical side"; row 1177 RESULT "given the one-cube physical neutral bound").
So the three rows need one statement, (N-phys).

**In plain words.** With H_n = -log(F/lambda_0) on the cube n^3, (N-phys) says Tr_neutral exp(-u H_n) <= 3/2 at
u = n/512: the centre-neutral thermal partition function at temperature 512/L on the box L^3 is at most 3/2 in
vacuum units, uniformly in the cutoff. GUIDE: for a free massless field the same trace is exp(c 512^3); for a
theory with lightest neutral mass m it is about 512^3 (x/2 pi)^(3/2) exp(-x) with x = m L/512, so the bound asks
for m L of order 10^4. It is a statement at one large physical size, not a small-volume statement.

**What is on file about (N-phys)** (each line read at this pin):

1. Consumer, PROVED in row 1161 (checked by Opus 5.5 max in row 1162): (N-phys) gives a cutoff-uniform
   Pfaffian seed S_kappa < 2^(-18) at time n/2, and one of two flux alternatives (9).
2. Row 1179 (`gap-mini-branch-fable.md` Theorem BP, PROVED GIVEN rows 697, 700, 731, 1161; checked by no one):
   (N-phys) alone gives a cutoff-uniform gap on the centre-blind sector and, with the continuum datum, the
   Jaffe-Witten gap clause in both flux alternatives. So (N-phys) is the whole gap clause in this lane.
3. Necessity, PROVED in row 1161 L150: (W) implies (N-phys) on all large dyadic sizes.
4. Equivalent forms over physical sizes, PROVED in row 1161 (26) and L389-400: a cutoff-uniform Pfaffian seed
   iff S^+_ev(L) -> 0 on dyadic sizes iff (S^+_ev bounded and the neutral dimensionless gap z^-_+ unbounded),
   where S^+_ev(L) = limsup_j s_j(n/2; n) is the neutral excited sum at aspect two.
5. Lower bounds, PROVED in row 1161 (17), (19): s(u) >= c n^3 exp(-C u) at every beta >= 1, so u = o(log n)
   is excluded. Row 1153: the short-period trace is a free gluon gas.
6. Abstract obstructions, PROVED: the sign-product comparison (row 1161 L375), the finite-moment construction
   (row 1161 L404), the local neutral spectator (row 1175 (29)), the centre-spectator principle of the council
   (rows 1128-1134), Lemma PT and Proposition NP (rows 998, 1003).
7. The glue-half engine: rows 1124-1125 ((GLUE-STEP), found-again, no first leaf), row 731 ((G_ev), (EV-STEP)),
   route RE. No published theorem gives an order-one four-dimensional non-abelian glue-half seed (row 1124).

**Rule 0a.** `grep -i neutral library/open-core.md` returns nothing. FINISH rows that name the neutral bound:
1161-1177 (the chain that states it as OPEN), 1178 (`gap-solve18-astra62`, the chain's general continuation on
(W), running now), 1179 (branch selection, not this bound), 1181 (free method). No other row is assigned the
neutral bound; row 1180 (this row) is. I proceed.

**Kind of statement (lead rule W2).** (N-phys) is selective: it is false for the free photon and for compact
U(1) in its Coulomb phase (massless neutral states at every size), and it is violated by a product with a
massless or slowly cooling neutral spectator (item 6). A proof must read the non-abelian group at a scale of
order one in the coupling. It is (K-flow) in the lane's terms if proved along the trajectory, (K-one) if proved
at one bare coupling with a carry to finer cutoffs.

