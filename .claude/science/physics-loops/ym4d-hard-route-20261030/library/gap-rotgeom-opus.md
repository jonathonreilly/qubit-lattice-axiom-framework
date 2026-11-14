lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T02:09Z

# Row 963, gap-rotgeom-opus: rotated and diagonal geometry for the seed

Queue row 963 of `FINISH.md` (pinned at commit 3900bfe8b). Owner's question: "could the box
rotate in time as well?" Test item, analysis plus GUIDE. Author: Claude Opus 5.5 max, Mac mini
worker 2. Labels: PROVED (written argument, checkable by hand), CONDITIONAL (proved given a
named hypothesis), GUIDE (a run or heuristic; refutes or guides only), OPEN.

## Plan (at most eight steps; one step per response, each appended here before the next)

1. Sources: FINISH rules; rows 960 (`gap-vargeom-opus.md`), 962 (`gap-constraints-max.md`),
   row 892 section 4.1 (Lemma SPLIT, centre-twist flux sectors); the definition of the seed
   S(a; B); grep `open-core.md` and the FINISH rows for overlap.
2. Item (1): twisted tori. Exact statement of Tr((R T)^a) = Tr(R^a T^a); sector decomposition of
   the seed by characters of the spatial symmetry group; the centre-twist flux sectors as the
   existing analogue.
3. Item (2): sector-wise statements. Which sectors carry the soft modes (free photon, U(1)
   toron, frozen Q_8 / 2T flat vectors); whether momentum or lattice angular momentum gives a
   free-energy margin; whether the trivial sector carries the full order-one difficulty.
4. Item (3a): reflection positivity of the Wilson action across diagonal hyperplanes: literature
   with sources, and a by-hand proof or refutation on the smallest case.
5. Item (3b): what a diagonal transfer operator and its thermal sum give relative to the axis one.
6. Item (4): fact tests (U(1), frozen groups, SMALL-BOX) by hand.
7. GUIDE: sector thermal sums in a solvable model (only if cheap), scripts in `guide/lane963/`.
8. Verdict: does rotated or diagonal geometry buy anything over the static axis tori, and why.
   RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1. Repo search and sources (done 2026-11-14T14:25Z)

**Repo search (rule 0a).** `grep -i "rotat|diagonal refl|angular mom|point group|cubic irrep|mapping torus|twisted tor"`
over `library/open-core.md`: no line. Over FINISH rows: only rows 962 and 963. So no open lemma of this item is owned
by another row. Prior work that this item must build on, not repeat:

- Row 962 (`gap-constraints-max.md`, Claude Fable 5.2 max, unchecked). A4 sheared tori and Lemma SHIFT; B1 projected
  (momentum, cubic irrep, parity, centre) seeds; Section 7.4 projected doubling and the projected crossing identity
  (the deficit step needs the full sum); A5 Klein gluing Tr(T_b^a R) with R a reflection (not selective: R reverses
  U(1) flux); A6 diagonal reflections (ARGUED, "thresholds are not the obstacle"); B2 twist-summed engine (seed false
  in the confined phase). Theorem 2O (engine without axis exchange). Its finding: no relaxation is a NEW INPUT.
- Row 960 (`gap-vargeom-opus.md`): varying geometry buys nothing (Lemma NO-OP, DEN, OVL).
- Row 892 Section 4.1 (`gap-crux-core-max.md` L265-280): Lemma SPLIT. Setting: T = T_(B,0) on a periodic box B,
  commuting centre flips C_2, C_3, C_4, eight sector projections P_chi, Z_chi(t) = Tr(T^t P_chi) >= 0,
  S_ev = Z_0/lambda_0^t - 1, q_i = Tr(T^t (1 - C_i)/2)/Tr T^t = (1 - Z^(v_1i)/Z^0)/2, Q_0 = max q_i. Then
  (1 + S_ev)/(1 - Q_0) <= 1 + S <= (1 + S_ev)/(1 - 3 Q_0). The twisted partition function Z^(v_1i) = Tr(T^t C_i) is
  the centre-twist analogue of the rotated trace of item (1).
- **Diagonal reflection positivity is already in the repository and in the account.** `library/am1-port.md` Section 3
  (Codex, a port of Sussman-Alpoge YM3_I IV-16-26 and SA 2773-2883): allowed normals e_mu and e_mu +- e_lambda,
  diagonal mirror heights c in Z, adapted tori Gamma = T (+) Z(L n/|n|^2) with T in n-perp; at a diagonal cut "the
  only crossing plaquettes have heights c-1, c, c, c+1, in the (1, 2) plane ... Their weight is k(P_+, P_-), and
  reflection exchanges the paths" (L62), with the positive Gram expansion k(g, h) = e^(-beta) e^(beta s(g).s(h))
  (L50-57). Its Lemma S (Claude, checked by Codex, L6-14): no lattice is adapted to both e_4 and e_1 - e_4. LG1
  Theorem 10 and 13(5) (`library/lg1.md`): every periodic Wilson DLR state is RP at the diagonal lattice mirrors.
  `library/ro1-vs-ca.md` L52 quotes CA-III L79973-79974: "Diagonal reflection positivity holds for the Wilson weight
  on Z^4 and fails on every straight torus", and CA-III Remark 10.1 (L79931-79990). So item (3) is a citation plus
  the transfer-operator question; I do not re-prove the positivity, I restate it with its sources and test it on the
  smallest case.
- Seed: S(a; B) = Tr(T_B^a)/lambda_0^a - 1 (`gap-seed-shape.md`, Theorem SH, checked row 707); engine of row 962
  Section 1.1 (Lemmas K, X, E', Theorem SH; uses (TM) in each direction, the exchange of two axes, a simple top
  eigenvalue).

Next: Step 2, item (1), the twisted-trace identity and the sector decomposition.
