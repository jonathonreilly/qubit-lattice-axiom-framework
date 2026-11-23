lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-24T11:05Z

# Lean design of the conditional gap chain on the YM4 Lean library (row 1457)

Worker: Claude Fable 5.2, high, Mac mini worker 1. Started 2026-11-23T23:05Z (`date -u`). Pin: aefd4ca20.
Status of this file: a design note. No Lean text here was built. Each claim carries one mark:
**proved** (argument on file and checked, row cited), **sketched** (argument on file, unchecked, or my own outline),
**guessed** (my estimate), **read** (I opened the declaration in the release and quote it).

Credit. The Lean library is Ethan Sussman and Levent Alpoge's `YM4 Lean` release at 3932084a9b82 (with Claude and
Codex as authors of their text). The chain to formalize is the lane's (rows cited at each step). Mathlib is cited
by declaration name.

## 0. Plan (written first, per the save protocol)

1. Read the row's named inputs: `library/sa-ym4-lean-trajectory-check-astra62.md` (statement of (M-neutral-all)),
   checks 1450 and 1453, `library/gap-os-equiv.md` Statement (5), and the files of Lemma DT, Proposition BP,
   P-ev, P'-ev, Corollary M2 (row 1356), Lemma FE.
2. Inventory the release: file list, the final theorem, the definitions of the trajectory, the continuum
   hierarchy, the OS data, any transfer operator. Declaration names with file and line.
3. Inventory Mathlib (at the release's pin, read from the release's `.lake` if present; else by name, marked guessed).
4. Write the Lean statement of (M-neutral-all) and of the conditional theorem.
5. Dependency list of lemmas with size estimates; the hardest step.
6. What to state and check first.
7. The next two rows and their decisive outcomes.

Status log (times from `date -u`):

- 2026-11-23T23:05Z file created with the plan.
- 2026-11-23T23:20Z inputs read: row 1457 brief; rows 1449 (`prior/sa-ym4-lean-inputs-opus.md`, whole), 1450
  (`sa-ym4-lean-faithful-astra62.md` L14-93), 1453 (`sa-ym4-lean-trajectory-check-astra62.md`, whole);
  `gap-mini-branch-fable.md` L167-336 (A-cl, L3-ev, P-ev, P'-ev, BP); `gap-mini-mneutral-fable.md` L76-125 (M1, M2).
  Section 1 written.

## 1. The chain to formalize, as it stands on file (no new claim)

Notation. b = the release's odd blocking factor (their `L`); a_K = b^(-K); l = the physical side of the seed
cube (in 4N); n_K = l b^K; beta_K = g_K^(-2) the least-root Wilson coupling of the release at cutoff K and
response parameter g_0; nu_j = the release's infinite-volume lattice state at the extracted cutoff K_j; S = the
release's continuum limit (a mixture). A = centre-blind local functions (`gap-mini-branch-fable.md` 5.0).

The hypothesis (check 1453, L101-105; proved there to be the right target given BND, BND-1, BND-2):

(M-neutral-all). For the constructed b, M, delta and a fixed 0 < g_0 < delta there are l in 4N and K_0 such that
for every K >= K_0 there are an integer 1 <= w_K <= n_K/1024, a unit vector phi_K and c_K > 0 with
norm_HS(c_K^(-1) P_0 T_K^(w_K) - |phi_K><phi_K|) <= 2/5, where T_K is the Wilson transfer operator of the
n_K^3 spatial slice at beta_K and P_0 the electric-neutral projection.

The chain from it to the gap, in the order of use. Each node is a hand statement on file; "std" marks whether
the node is lattice-only (L), soft functional analysis (F), or reads the release (R).

| Node | Statement (short) | Where | Checked by | Kind |
|---|---|---|---|---|
| N1 | Lemma M1, Corollary M2: the 2/5 test at time w holds iff s(2w) <= 4/21 | `gap-mini-mneutral-fable.md` 2.1-2.2 (row 1356) | row 1359 | F (finite spectral) |
| N2 | (N-phys) with u = max(3, 2w) <= n/512, s_+(u) <= 1/2 | M2 (ii) | row 1359 | L |
| N3 | Explicit finite-aspect theorem: (N-phys) gives S_kappa(n/2; n^3) < 2^(-18) in either flux alternative | `gap-solve9-astra62.md` L146-148, L213-227 (row 1161) | check 1162 | L, 64 twists |
| N4 | (TM-tw): twisted transfer operators, sector sums | `gap-transfer-twisted.md` Theorem TW-T (row 1004) | check 1008 | L |
| N5 | (S): Lemmas K, X, E, E', Theorem S; Lemma W, Theorem S-w, Corollary EV: a seed S_w(N; (2N)^3) <= s < 1/5041 gives m_ev(L^3) >= log(1/(5041 s))/N for every L >= 2N | `gap-crux-restate.md` 3.x (row 697), `gap-flux-exercise.md` 8.4 (row 731) | rows 698, 699, 732 | L, doubling induction |
| N6 | Lemma FE, Lemma RPc, Theorem L3 (a), (c); Lemma CB, MX, L1-ev, Theorem EV-L (c), (d): limit states of periodic tori cluster on A at rate m_0 | `gap-seed-limit.md` 4.2-4.3 (row 700), `gap-flux-exercise.md` 8.2 | rows 703, 723, 732 | L + limit |
| N7 | Lemma A-cl, Theorem L3-ev: D_nu is a reflection datum, unique vacuum, transfer gap on H_A(nu) | `gap-mini-branch-fable.md` 5.1 (row 1179) | (row 1179's check) | F + L |
| N8 | Proposition P-ev, Theorem BP (i)-(ii): at each cutoff, rate M_* in physical units | same file 5.2, 6 | same | L |
| N9 | Statements (1), (3), (5a)-(5c), Lemma E of `gap-os-equiv.md`: Hilbert space of a reflection datum; decay on a total class gives the gap; the gap passes to limits | `gap-os-equiv.md` (row 668) | on file as checked | F |
| N10 | Lemma DT (dense times suffice) and literal (H2) by a diagonal argument | row 1449 L97-99; check 1450 L48-50 | check 1450 | F |
| N11 | Continuum datum from S: (P1)-(P4), class C, maps iota_j into V_A, (TOT), Borel admission by Lemma FE | row 1449 Step 2 table; check 1450 L27-36 | check 1450 | R |
| N12 | Proposition P'-ev: unique vacuum and spec(H_S) in {0} union [M_*, infinity), M_* = (2/l) log(2^18/5041) | `gap-mini-branch-fable.md` 5.3; check 1450 L56-62 | check 1450 | F + R |
| N0 | BND, BND-1, BND-2: beta_K exists and is bracketed at every late K (only needed to state the target and to read it as the right one) | check 1453 L24-55 | check 1453 | R |

Reading of the table for the design (my own, **sketched**): the chain splits at one interface.

- **Interface (CL-nu), "uniform lattice clustering on the tr F^2 class".** For the release's states nu_j and the
  maps iota_j: there is M_* > 0 with u_j(iota_j F, iota_j F; t) <= C_F(j) e^(-M_* t) for every F in C, every
  late j and every lattice time t >= t_F (the constant may depend on j and F; only the rate is uniform). This is
  hypothesis (H1) of Statement (5) in the weak diagonal form that Statement (3) consumes at each j.
- **Upper half (U): (CL-nu) gives the gap of S.** Nodes N9-N12. Soft. It reads the release (the limit S, its
  axioms, nu_j, moment convergence). No transfer operator on a finite slice is needed here.
- **Lower half (W): (M-neutral-all) gives (CL-nu).** Nodes N1-N8. Lattice only. It needs the finite-slice Wilson
  transfer operator, the 64 twists, the doubling induction, and the passage from periodic tori to nu_j. It reads
  the release only through the definition of the finite Wilson law and of `IsInfiniteVolumeLimit`.

The size and the hardest step are decided by (W). Sections 2-3 inventory what exists for each half.
