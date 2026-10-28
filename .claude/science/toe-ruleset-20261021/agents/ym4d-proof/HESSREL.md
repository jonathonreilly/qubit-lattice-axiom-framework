# HESSREL.md — (HESS-rel): the unwalked route from the flat chain Hessian to (GAP-Z) (target T55-L)

## §H0 PRE-STATED (FIRST EDIT of this file, 2026-10-28 21:40:12 UTC; STATEMENTS ONLY)

This is the first edit of this file. It is written before any derivation, before any criteria file and
before any script. It cites **no result produced in session 25** except the *name and verbatim wording of
the route* that defines my target, which was handed to me in my scope prompt and which I quote so that a
reader can see exactly what I set out to decide; every mathematical object below is pinned to a
pre-session file:line.

### H0.1 Scope and ownership
I may WRITE ONLY `HESSREL.md` and `checks/hr1_*`. I read anything. No git, ever. Anything I want changed
in another file goes in "## FOR OTHER FILES (not edited)" at the end of this file. Appends only.

### H0.2 The object under test, quoted
The route is named **(HESS-rel)** in `NBG_A.md` §A4.3 (a concurrent session-25 file; I quote it as the
*definition of my target*, not as an input to any argument):

> **(HESS-rel) [named there; GAP].** There is `C < ∞` depending only on `(N, L, κ_±)` such that for every
> `k`, every torus and every `V` of the class, the difference of the composite chain Hessians
> `Hess𝔉_k(Z(V)) − Hess𝔉_k(1)` admits the **slot-wise** decomposition of BFT_B §41.2 (c) — `E = Σ_l e_l·𝒪_l`
> with `𝒪_l` the operator already present in that slot and `e_l ≤ CL^{−2(k−l−1)}f_k` — so that
> `‖E‖_{𝔐→Y} ≤ C f_k ‖Hess𝔉_k(1)‖_{𝔐→Y}` with **no weight penalty and no factor k**.

and the claim attached to it is: *given (HESS-rel), (GAP-Z) follows from the flat `(G♯_0-field)` by a
Neumann series in the weighted pair.*

Pre-session anchors for every symbol in it:
- `𝔉_k(U_0, …, U_{k−1}; V_k) := S_W(U_0) + Σ_{j=0}^{k−1}κ_jΣ_cφ̂_c(M̄^{(j)}_c(U_j); U_{j+1})` — **PROOF.md
  l.6605** (Lemma TOWER-VAR). `U_k := V_k`; `M̄^{(j)}` the S4′ average of the pair `(j, j+1)`.
- `Hess𝔉_k` on the composite slice `S_k`, and the composite covariance `𝔊_k` — **PROOF.md l.6631**.
- **BFT_B §41.2 (c)** — `BFT_B.md l.4549-4553` (Theorem BGD (c), PROVEN-HERE there, UNREVIEWED: §38-§43).
  Its two defects: **(B1)** the exactness defect `d_Zd_Z ≠ 0`, `BFT_B.md l.4533-4538`; **(B2)** the
  root-covariance defect, `BFT_B.md l.4540-4545`.
- **§41.5 (i)** the no-go — `BFT_B.md l.4587-4588`; **§41.5 (ii)** the split and `(GAP-Z)` —
  `BFT_B.md l.4589-4593`; `(GAP-Z)` first stated at `BFT_B.md l.4334`.
- **(G♯_0-field)** — "(G♯) for the chain Hessian at the **trivial** chain in the §33 pair, with the
  weighted constants; OPEN, lane A's `U = 1` package" — `BFT_B.md l.3840`.
- The `(G)`-slot weight of lane A's `Y`: `ω_l = L^{θ(k−l)}` — `BFT_B.md l.4364`.
- `𝒦(ε)`, `f_j ≤ C_Nf_k` gauge-invariantly with no global gauge — Theorem N2 (N2-0)(a), `BFT_B.md l.4529`.
- `𝒞_glob(ε)` (the global-small-gauge subclass) — `BFT_A.md l.27`; Theorem BA on `𝒞_glob` — `BFT_A.md
  l.89, l.205`; outside `𝒞_glob` — `BFT_A.md l.232-256`.
- SF's **BNA-F4** (no global gauge makes `log Z` small; holonomies accumulate) — `SF.md l.702, l.724`.

**Symbol discipline (lane defect 1).** I carry **my own** exponent symbols `ϑ^c`, `ϑ^r`, `ϑ^Y` and do
**not** write `θ_w` anywhere except when quoting a file, with its file:line. I do not inherit
`NBG_A`'s `θ_w^c`, `θ_w^r`, lane A's `θ` in `ω_l = L^{θ(k−l)}` (BFT_B l.4364), or NORMS' `θ_w^c = 2`,
`θ_w^r = 3`; where I need a relation to one of them I state it as a hypothesis with the file:line of the
object I am relating to.

### H0.3 Pre-stated targets
- **TL1.** State (HESS-rel) precisely, with all quantifiers: *which* difference, in *which* norm pair,
  uniform in *what* (`k`? `T`? the background `Z`? the level `l`? the gauge representative of `Z(V)`?),
  *given what*. Enumerate the inequivalent readings and say which one the Neumann series needs.
- **TL2.** **Re-derive** BFT_B §41.2 (c)'s bound for B1 and B2 from (41.1) and (41.3) rather than cite it,
  and test each of the three adjectives **independently**: (a) *slot-wise* — is `E = e_l·𝒪_l` with `𝒪_l`
  an operator already present **and bounded** in that slot? (b) *weight-free* — is the cost `max_l e_l`
  rather than `Σ_lω_le_l`, and does that survive when the input slot and the output slot carry different
  weights? (c) *factor-k-free* — does a factor `k` enter from the level sum, from the number of defect
  families, or from the number of slots?
- **TL3.** Decide whether the bound **extends from the two defects to the whole difference**
  `Hess𝔉_k(Z) − Hess𝔉_k(1)`. If it does not, localise the failure to a named term and say whether the
  failure is in the combinatorics, in a factor growing with the defect count, or in a weight that was
  free for a local object and is not for a global one.
- **TL4.** Run the Neumann series in the weighted pair. State (i) the two norms the series needs, (ii) the
  exact convergence condition in my own exponent symbols, (iii) the exponent window, and (iv) whether the
  window is compatible with, wider than, or narrower than the window the consumer already assumes.
- **TL5.** Determine **lane B's reason** for not taking this route, or establish that there is none. Read
  §41.5 in full, the sessions-10/11 material around it, and `BFT_B_LOG.md`. A recorded decision counts;
  an absence of record is reported as an absence.
- **TL6.** Give the honest status of **(GAP-Z)** at the end: unchanged, reduced, or proven.

### H0.4 Pre-registered outcomes (exactly one will be recorded)
- **O1.** (HESS-rel) as stated is TRUE and the Neumann series closes: **(GAP-Z) REDUCED** to the flat
  `(G♯_0-field)` plus an explicit smallness condition.
- **O2.** (HESS-rel) as stated is FALSE, by an explicit counterexample, and no repair survives:
  **(GAP-Z) UNCHANGED**, and the route is recorded as dead with the reason.
- **O3.** (HESS-rel) as stated is FALSE but a **repaired** statement (HESS-rel′) is available, at the
  price of a flat input strictly larger than `(G♯_0-field)` at `U = 1`: **(GAP-Z) localised, not reduced**;
  the enlarged flat input is named.
- **O4.** §41.2 (c)'s bound fails one of its three adjectives **already for B1/B2**: a correction to lane
  B, reported as such, independently of O1-O3.

### H0.5 Pre-stated failure modes (if one occurs it is reported as having occurred)
- **HR-F1 (the currency mismatch).** The difference `Hess𝔉_k(Z) − Hess𝔉_k(1)` contains a part whose size
  is the background **connection** `|log Z|`, not the background **curvature** `f_k`, so no bound of the
  form `C f_k·‖Hess𝔉_k(1)‖` can hold in any global gauge. *Test:* evaluate the difference at a background
  with `F_Z = 0` exactly; a curvature-relative bound must give `0`.
- **HR-F2 (the pair mismatch).** `Hess𝔉_k(Z)` acts between the **background-covariant** spaces `𝔐^∇_Z`,
  `Y_Z` (BFT_B §12.0; §41.4's (B3) reading: "every Campanato oscillation taken of values transported to
  the box corner along fixed axial paths in `Z`", `BFT_B.md l.4583`), while `Hess𝔉_k(1)` acts between
  `𝔐^∇`, `Y`. The *difference* is then not an operator between one fixed pair, and the identification
  carries its own constant.
- **HR-F3 (no shared slot).** §41.2 (c)'s weight-freeness argument is "the weights act on the slots, which
  `E` and `𝒪` share". For B1 the flat counterpart `dd` is **identically zero**, so there is no `𝒪` whose
  slots `E` shares; the honest cost is a **weight ratio** between the input and output slots.
- **HR-F4 (the level sum).** A factor `k` enters not from one defect but from summing one defect per
  level, if the geometric decay `L^{−2(k−l−1)}` is not available in the slot that actually carries it.
- **HR-F5 (lane B declined, with a reason).** The route was considered in lane A or lane B and set aside
  for a recorded reason that is **not** §41.5 (i)'s symbol no-go.
- **HR-F6 (the route is not new).** "Neumann series from the trivial chain to `Z(V)`" is already the
  existing route of one of the lanes, with its own recorded domain of validity; the unwalked part is not
  the series but the hypothesis that makes it converge.

### H0.6 Criteria and controls (Rule 2, Defect 3)
If I run any check: `checks/hr1_criteria.md` is written **before** any script, contains no constant
derived in this session, and pre-registers PASS/FAIL. **Every gate gets a designed-FAIL control** — an
input for which the gate must NOT fire — and the control's result is reported. For the HR-F1 test the two
controls are (i) a **constant** chain gauge (the difference must be exactly `0`) and (ii) an **abelian**
structure group (the difference must be exactly `0`, matching bb11's C1 at `BFT_B.md l.4538`), so that a
refutation which fires on them is known to be an artefact of my own arithmetic.

### H0.7 Method
Exact integer/rational arithmetic in plain python only; no BLAS, no numeric lock (brief rule 6). No new
axioms. Imports re-verified. I treat every "PROVEN-HERE" in BFT_B §38-§43 as **evidence, not a
certificate** (brief, defect 4) and re-derive the load-bearing step.

### H0.8 Dead routes I will not re-walk
Per `SESSION24_RESULTS.md` and my scope: per-level induction in any norm; both axial gauges; gluing via
Theorem RW; thin-cluster escape; finite funnel truncation; (NEUT-box); route (ii)/GT-ell; (CovLift) at
`θ > 0` for every lift; the gauge escape. I will **not** lean on GREENT.

---
