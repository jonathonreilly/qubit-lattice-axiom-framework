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

## §H1 (HESS-rel) stated with its quantifiers (TL1)

§A4.3's wording leaves four things unfixed. Pinning each one gives four inequivalent statements, and they
do not stand or fall together, so they are separated before anything is attacked.

**What is fixed in every reading.** `𝔉_k` is the composite functional of PROOF.md l.6605; its Hessian is
taken on the composite slice `S_k` in the composite displacement variable `X` (`Z = e^XZ^lift`,
PROOF.md l.6631-6634), so **both Hessians in the difference act on one and the same real vector space**
and the difference is well defined as a linear map. `f_k` is the own-unit top-level curvature of the
background; `f_j ≤ C_Nf_k` on all of `𝒦(ε)` (Theorem N2 (N2-0) (a), BFT_B.md l.4529).

**(q1) Which difference?** `Hess𝔉_k(Z(V)) − Hess𝔉_k(1)`, where `1` is the **trivial chain** (the chain all
of whose links are the identity), because that is the chain at which `(G♯_0-field)` is stated
(BFT_B.md l.3840: "the chain Hessian at the **trivial** chain"). Not: the Hessian at a gauge transform of
the trivial chain, and not the Hessian conjugated to the background's frame.

**(q2) Which `Z(V)`?** §A4.3 names no representative. The two candidate readings are
- **(R-any)** every chain `Z` whose curvature is `≤ ε` — i.e. the statement is about the class, which is
  **gauge invariant**; or
- **(R-lift)** only the lane's own lift `Z^off(V)` (BFT_B §25.5), one representative per `V`.

These are not independent: `(CovLift)` (i)-(iii) give **the covariance of `Z^off` on `𝒦(ε)` for every
gauge** (BFT_B.md l.3845), i.e. `Z^off(V^g) = (Z^off(V))^g`, and `𝒦(ε)` is closed under gauge. So (R-lift)
already quantifies over whole gauge orbits of lifts, and the distinction between (R-any) and (R-lift)
does **not** protect the statement. This matters in §H3 and is the reason the refutation there is not a
quibble about representatives.

**(q3) In which norm pair?** `𝔐 → Y`, the §33 pair (SF's Hölder `X_c` paired with a divergence-form `Y`
carrying level weights `ω_l = L^{θ(k−l)}`, BFT_B.md l.4364; the pair exists because the **unweighted**
sup-norm statement is false at the trivial chain with `‖𝓛^{−1}‖_{ℓ^∞→ℓ^∞} ≳ L^{2(k−1)}`, PROOF.md
l.6656-6658). **Carrying my own symbols (§H0.2):** `𝔐` carries level weights `ϖ_l = L^{ϑ^𝔐(k−l)}`, `Y`
carries `ω_l = L^{ϑ^Y(k−l)}`. I write `ϑ^Y` where lane A writes `θ` at BFT_B.md l.4364, and I assert no
relation between `ϑ^Y`, `ϑ^𝔐` and NORMS' `θ_w^c`, `θ_w^r` or NBG_A's `θ_w^c`, `θ_w^r`.
**A second, unflagged ambiguity lives here.** `Hess𝔉_k(Z)` is naturally an operator `𝔐^∇_Z → Y_Z`, the
**background-covariant** spaces, whose Campanato oscillations are taken "of values transported to the box
corner along fixed axial paths in `Z`" (BFT_B.md l.4583, §41.4's (B3) reading), while `Hess𝔉_k(1)` lives
on `𝔐^∇ → Y`. The *underlying vector spaces* coincide, so the difference is defined; the *norms* do not,
so "`‖·‖_{𝔐→Y}`" must name one of four pairings. **This is pre-stated failure mode HR-F2, and it
OCCURS** — but it is not what kills the statement, because the refutation of §H3 gives a nonzero operator
against a right-hand side that is exactly `0`, and that holds in every one of the four pairings.

**(q4) Uniform in what?** The only reading that serves the consumer is: `C = C(N, L, κ_±)`, **uniform in
`k`, in the torus side `T`, in the level `l`, and over the whole class of admissible backgrounds `Z`** —
in particular uniform over the gauge orbit of each `Z`, by (q2). Non-uniformity in any of these makes the
Neumann series of §H5 useless, since `M_0` and `Λ_0` there are themselves `k`-, `T`-uniform constants.

**(q5) Given what?** §A4.3 quotes §41.2 (c)'s bound as if it were unconditional. It is not: of the two
defects §41.2 (c) prices, **(B1)'s size is unconditional** (BFT_B.md l.4536, from (N2-0) (a)) while
**(B2)'s size is CONDITIONAL on `(C_g-θ)`** (BFT_B.md l.4547: "Status of (41.4): **CONDITIONAL on
(C_g-θ)**", whose own status is Proposition Cg-lin PROVEN-HERE for the linear lift and Proposition Cg-NL
**first order PROVEN, BCH remainder ARGUED**). So even the two-defect base case of (HESS-rel) carries an
ARGUED input, which §A4.3's quotation drops.

### H1.1 (HESS-rel), fully quantified — the statement actually under test

> **(HESS-rel).** There is `C < ∞` depending only on `(N, L, κ_±)` such that: for every `N ≥ 2`, every odd
> `L ≥ 3`, every `κ_j ∈ [κ_−, κ_+]`, every `k ≥ 1`, every torus of side `T ≥ T_0`, every level-`k` field
> `V ∈ 𝒦(ε)` with `ε ≤ ε_0`, and the background chain `Z = Z(V)` **in any gauge representative admitted by
> the class**, the operator `E := Hess𝔉_k(Z) − Hess𝔉_k(1)` on composite displacements satisfies
> `‖E‖_{𝔐→Y} ≤ C f_k(Z)·‖Hess𝔉_k(1)‖_{𝔐→Y}`,
> where `f_k(Z)` is the own-unit top curvature of `Z` and the norms are the §33 weighted pair.

Two consequences of this form, both used below. **(i)** The right-hand side is **homogeneous of degree 1
in the curvature**: at `f_k = 0` it is exactly `0`, so (HESS-rel) asserts `Hess𝔉_k(Z) = Hess𝔉_k(1)` at
every zero-curvature background in the class. **(ii)** The right-hand side involves
`‖Hess𝔉_k(1)‖_{𝔐→Y}`, a **forward** bound on the flat Hessian in the weighted pair. That quantity is not
part of `(G♯_0-field)`, which bounds only the **inverse** (BFT_B.md l.3840). I name it

> **(FWD-0).** `‖Hess𝔉_k(1)‖_{𝔐→Y} ≤ Λ_0 < ∞`, uniformly in `k` and `T`.

and record that **I found it stated nowhere in the lane**. It is presumably intended to hold by the
design of the §33 pair, but the Neumann series needs it explicitly (§H5), because the quantity that
controls the series is the **condition number** `Λ_0M_0`, not `M_0` alone.

---

## §H2 Lane B's reason (TL5) — done first, as instructed. **There is a reason, it is recorded three times, and it is not §41.5 (i).**

§A4.3's caveat is that §41.5 (i)'s no-go "is about *conjugation* and the symbol method, which a Neumann
series does not use — but lane B did not take this route and may have declined it for a reason I cannot
see". The caveat's first half is **right** and its second half is **answerable from the files**.

### H2.1 §41.5 (i) is indeed only about the symbol method, and it is narrower still than §A4.3 says
Read in full (BFT_B.md l.4587-4588), the no-go is: Theorem 4.2/4.2′ proves `M` and `M_f` by analytic
continuation of the **momentum-space symbol** into a strip, *"That requires exact translation invariance
of the operator. No gauge makes a background with `F_Z ≠ 0` translation invariant"*. Two readings follow
that §A4.3 does not draw:
1. A Neumann series is not a symbol argument, so §41.5 (i) does not refute it. **Confirmed.**
2. The no-go's own premise is `F_Z ≠ 0`. It says **nothing** about a background with `F_Z = 0` and
   non-trivial holonomy, whose operator *is* exactly translation invariant (its coefficients `Ad_{h_μ}` do
   not depend on the site). This is used in §H6 and is, as far as I can see, new.

### H2.2 Lane B did not decline the Neumann series. Lane B **uses** it, twice, and recorded its domain.
- **BFT_B.md l.4578, Lemma FR-price step 4:** *"**Neumann series.** For `8c_NC_1f_k ≤ 1/2`, the normal
  operator `d_Z^{*,Ñ}d_Z^{Ñ}` is an invertible perturbation of `d^{*,Ñ}d^{Ñ}` …"*. This is exactly the
  device (HESS-rel) proposes — applied **on a frame box `Ñ_X` of coarse side 4**, where Corollary CL-iv
  has made the background connection small.
- **BFT_B.md l.4591, §41.5 (ii):** the Combes-Thomas half *"invert by a Neumann series for `m` small"*.
So the device is not refused anywhere. What is recorded is **where it can be applied**.

### H2.3 The recorded reason, in three places, and it is the same reason each time
1. **Pre-stated failure mode S11-F6 (BFT_B.md l.4377), session 11, verbatim:** *"(GAP-Z) is not the only
   Tier-C obstruction: LES-div at a background **needs more than a Neumann series because the background
   connection is small only in the frame** and LES-div is applied on the periodic lift."* Status at
   BFT_B.md l.4746: **"OCCURS as pre-stated, and it is answered"** — answered by replacing the periodic
   lift with the **box** form, i.e. by staying local. The obstruction to a *global* Neumann series was
   written down, in advance, by lane B itself.
2. **The route already exists and is lane A's, with its domain fixed. BFT_B.md l.103, verbatim:**
   `(H-𝔊_w)_k :=` lane A's `(H-lin^∇)` with exponential weight *"plus (H-rem^∇) in the same weighted pair
   **(Neumann series from the trivial chain to Z(V))**"*, and immediately: *"Outside `𝒞_glob`, (H-𝔊_w)
   inherits lane A's **(UHL) + (SL-cov)** through BA-11 patching."* `𝒞_glob(ε)` is the subclass of fields
   admitting **one global small gauge** (BFT_A.md l.27).
3. **The same split in lane A's own file.** Theorem BA proves BFT-0/1/2 **on `𝒞_glob`** from
   `(H-lin^∇) + (H-rem^∇) + (FP♯′)` (BFT_A.md l.89-90, l.205, l.306) — that *is* the Neumann-from-the-
   trivial-chain route. §3.10, headed *"Outside `𝒞_glob` (BNA-F4)"* (BFT_A.md l.232), reduces the outside
   case to `(G♯-patch)` and names what it still needs: **(UHL)**, a lattice local Coulomb (Uhlenbeck-type)
   gauge, and **(SL-cov)**; *"Both OPEN"* (BFT_A.md l.250-255; status line l.309; PROOF.md l.6835 carries
   it as "off `𝒞_glob`: (UHL), (SL-cov), `Z^sm`").

**So the answer to TL5 is: the route is not unwalked. It is walked, it is the lane's main route, and its
domain of validity is `𝒞_glob` (globally) or a frame (locally). `(GAP-Z)` is precisely the part that lives
outside that domain.** Lane B's reason for not taking the Neumann series *to* `(GAP-Z)` is that **the
series needs the perturbation to be small, and outside `𝒞_glob` the perturbation is not small in any
global gauge** — SF's BNA-F4 (SF.md l.702, l.724; BFT_B.md l.4529: *"`‖log Z‖` is not small in any global
gauge on a large torus"*). **Pre-stated failure modes HR-F5 and HR-F6 both OCCUR.**

**The unwalked item is therefore not the series. It is the gauge that makes the series converge**, and
that gauge has a name already — `(UHL)` — and is OPEN.

---

## §H3 BFT_B §41.2 (c) re-derived for B1 and B2, and the three adjectives tested one at a time (TL2)

Per the brief's defect 4, nothing below cites §41.2 as an authority; the identities and the bound are
rebuilt from the definitions, and the three adjectives are then tested **separately**, because they have
separate proofs and one of them has a wrong stated reason.

### H3.1 (B1), the exactness defect: identity re-derived, **confirmed exactly**
Conventions as in `checks/hr1_criteria.md`: `(d_Zλ)(b) = Ad_{Z(b)}λ(y') − λ(y)` for `b = (y → y')`, and on
1-forms, at the plaquette `p` based at `z` with `μ < ν` and far corner `c = z + e_μ + e_ν`,
`(d_Zu)(p) = u(z,μ) + Ad_{Z(z,μ)}u(z+e_μ,ν) − Ad_{Z(z,ν)}u(z+e_ν,μ) − u(z,ν)`.
Substituting `u = d_Zλ` and writing `U_1 := Ad_{Z(z,μ)}Ad_{Z(z+e_μ,ν)}`, `U_2 := Ad_{Z(z,ν)}Ad_{Z(z+e_ν,μ)}`:

| term | expansion |
|---|---|
| `u(z,μ)` | `Ad_{Z(z,μ)}λ(z+e_μ) − λ(z)` |
| `Ad_{Z(z,μ)}u(z+e_μ,ν)` | `U_1λ(c) − Ad_{Z(z,μ)}λ(z+e_μ)` |
| `−Ad_{Z(z,ν)}u(z+e_ν,μ)` | `−U_2λ(c) + Ad_{Z(z,ν)}λ(z+e_ν)` |
| `−u(z,ν)` | `−Ad_{Z(z,ν)}λ(z+e_ν) + λ(z)` |

Four single-transport terms cancel in two pairs; the two double-transport terms survive **at the far
corner**:  `(d_Zd_Zλ)(p) = (U_1 − U_2)λ(c)`. **(41.1) re-derived, exact.** The Frobenius identity is also
exact: `U_1, U_2` are orthogonal, so `‖U_1 − U_2‖_F² = 2dim 𝔤 − 2tr(U_1^TU_2) = ‖Ad_{W_p} − 1‖_F²` with
`Ad_{W_p} := U_1^TU_2` the `Ad`-action of the plaquette holonomy of `Z`. **So (B1) is genuinely a
curvature object:** it is bounded by `c_N|log W_p|` and vanishes identically when `F_Z = 0`
(independently confirmed in `checks/hr1_out.txt`: B1 nonzero at **0** of 64 plaquettes on the flat
configuration, and at **2** plaquettes on the curved control — gate hr1-C3 FIRED).

### H3.2 (B2), the root-covariance defect: identity re-derived, **confirmed exactly**
With `T_i := Ad` of the straight transport from the root `c_Y` to `y_i` and `b_i = (y_i, y_{i+1})`, one has
`T_iAd_{Z_l(b_i)} = T_{i+1}`, so the transported covariant differences telescope:
`Σ_iT_i[Ad_{Z_l(b_i)}lam_l(y_{i+1}) − lam_l(y_i)] = T_mlam_l(y_m) − T_0lam_l(y_0)
 = Row_l(Y,μ)lam_l(c_{Y+e_μ}) − lam_l(c_Y) = Row_l(Y,μ)lam_{l+1}(Y+e_μ) − lam_{l+1}(Y)`,
using the root-composition identity `lam_l(c_Y) = lam_{l+1}(Y)`. **(41.2) re-derived.** Subtracting
`(d_Z^{(l+1)}lam_{l+1})(Y,μ) = Ad_{Z_{l+1}(Y,μ)}lam_{l+1}(Y+e_μ) − lam_{l+1}(Y)` gives
`(Row_l(Y,μ) − Ad_{Z_{l+1}(Y,μ)})lam_{l+1}(Y+e_μ)`. **(41.3) re-derived**, and with it BFT_B's reading
that root covariance is **exact iff the background is a straight-row tower**. Independently confirmed in
`checks/hr1_out.txt`: B2 nonzero at **0** pairs on the flat (hence straight-row) configuration and at
**2** pairs on the curved control.

### H3.3 The three adjectives, tested separately

**(a) "slot-wise".** §41.2 (c)'s formulation is `E = e_l·𝒪` "with `𝒪` the operator already present in
that slot and bounded in `𝔐`".
- For **(B2)** this is literally right: the defect is a *relative* error on `Q_l` (or on `d_Z^{(l+1)}`), an
  operator `𝔐` already carries, with input and output both at level `l+1`. **Adjective holds.**
- For **(B1)** it is **not** literally right, and the stated reason is wrong: the operator "already
  present" would have to be `d∘d`, which is **identically zero**. There is no `𝒪` for `E_{B1}` to be a
  relative error of. The correct statement, which I supply, is: `E_{B1} = e_j·(ι_j∘ev_c)` where
  `ev_c` evaluates a level-`j` 0-form at the far corner and `ι_j` includes the value into the level-`j`
  2-form slot, and `‖ι_j∘ev_c‖ = 1` in every sup-type norm. **Adjective holds in substance, with a
  corrected reason.** This is not cosmetic: the corrected form shows that the cost is a **ratio of the
  weight on the 0-form slot to the weight on the 2-form slot**, which (b) must then supply.

**(b) "weight-free".** §41.2 (c)'s argument is *"the weights act on the slots, which `E` and `𝒪` share"*.
For (B2) they do share slots. For (B1) they do not — by (a) there is no `𝒪`, and `E_{B1}` maps the
**0-form** slot to the **2-form** slot. So the honest cost of (B1) in the weighted pair is
`(weight on the level-j 2-form slot)/(weight on the level-j 0-form slot) · e_j`, and the conclusion
`max_le_l` holds **iff the weight family is indexed by level only and not by form degree**. Lane A's
weight `ω_l = L^{θ(k−l)}` (BFT_B.md l.4364) is level-indexed, so the ratio is `1` and the adjective holds
— **but it holds by a property of the weight family that §41.2 (c) does not state and that a different
weight family would break.** Recorded as a **hidden hypothesis**, not a refutation:

> **(W-lev).** The weight families on `𝔐` and on `Y` are functions of the level alone, not of the form
> degree or of the slot type within a level.

Both defects are **level-diagonal** (B1: level `j` in, level `j` out; B2: level `l+1` in, level `l+1`
out), which I confirm from the re-derived (41.1)/(41.3), so given (W-lev) no `Σ_lω_le_l` appears.
**Adjective holds, given (W-lev).** Lane B reached the same distinction independently and later:
**§43.4** (BFT_B.md l.4778-4782) says §41.2 (c) *"is right **about the defect operators** and must not be
read as a claim about every place they appear"*, and prices the one level-crossing composition
(Lemma SPLIT's `ev^{(0→l)T}`) separately in §41.3. My reading agrees with §43.4 and extends it: the
0-form-to-2-form slot change of (B1) is a second place where "they share slots" is not literally true,
though (W-lev) repairs it.

**(c) "factor-`k`-free".** For a single defect at a single level, trivially. For the whole collection,
one defect per level, the cost is `Σ_{l=0}^{k−1}e_l` with `e_l ≤ Cρ_{l+1}²f_k = CL^{−2(k−l−1)}f_k`; the
sum is `≤ Cf_k·L²/(L²−1)`, **bounded uniformly in `k`** — the geometric decay in the depth does the work,
exactly as §41.2 (c) says, and the decay is in own units at the same level on both sides, so it survives
the level-diagonal weighting of (b). **Adjective holds.** (The one place it would fail is a
level-crossing composition, where the unit conversion costs a further `ρ_l²`; §41.3 isolates the single
such place in sessions 9-10 and routes it to (TENT-Q). Consistent.)

### H3.4 What H3 changes, honestly
**Pre-registered outcome O4 does NOT occur:** none of the three adjectives fails for B1/B2. What the
re-derivation does produce is three corrections to the way §A4.3 quotes the bound, all of which weaken
the quotation and none of which alone kills the route:
1. **(B1) has no `𝒪`**; "slot-wise" needs the corrected form `e_j·(ι_j∘ev_c)` (H3.3 (a)).
2. **"Weight-free" is conditional on (W-lev)**, an unstated hypothesis about the weight family (H3.3 (b)).
3. **(B2)'s size is CONDITIONAL on `(C_g-θ)`** (BFT_B.md l.4547), whose nonlinear half is
   *first order PROVEN, BCH remainder ARGUED*. §A4.3 quotes the bound as unconditional.

**Status of §41.2 (c) for B1/B2 after re-derivation: PROVEN, as lane B states, given (W-lev) for the
weight-freeness and `(C_g-θ)` for (B2)'s size; the stated reason for (B1)'s slot-wise form is wrong and
is repaired here.**

---

## §H4 The extension to the whole Hessian difference: it FAILS, and here is exactly where (TL3)

This is the mathematical content of the route, and the answer is negative. The failure is not in the
combinatorics, not in a factor growing with the defect count, and not in a weight that was free locally.
**It is a currency failure: the two priced defects are CURVATURE objects and the Hessian difference is a
CONNECTION object.** Pre-stated failure mode **HR-F1 OCCURS**.

### H4.1 Lemma HR-1 (the Hessian difference at a pure gauge): PROVEN-HERE
> **Lemma HR-1.** Let `G` be a chain gauge and `Z := G·1` the pure-gauge chain `Z_j(b) = G(y)G(y')^{−1}`
> (so `F_Z ≡ 0` at every level and `f_k(Z) = 0`). Then, **exactly**,
> `Hess𝔉_k(Z) − Hess𝔉_k(1) = [M_G, Hess𝔉_k(1)]∘M_G^{−1}`,
> `M_G` the pointwise `Ad_{G}`-action on composite displacements. In particular the difference is `0` **iff
> `M_G` commutes with `Hess𝔉_k(1)`**, which fails for every non-constant `G` not valued in the centre.

*Proof.* `𝔉_k(U_0, …, U_{k−1}; V_k) = S_W(U_0) + Σ_jκ_jΣ_cφ̂_c(M̄^{(j)}_c(U_j); U_{j+1})` (PROOF.md l.6605) is
invariant under chain gauge transformations: `S_W` is a sum of traces of plaquette holonomies, and
`φ̂_c` is a function of `|ρ_c|` with `ρ_c` the soft fluctuation of the pair, which transforms by `Ad` of
the root gauge — this is exactly what Lemma CONJ (ii)-(iii) (BFT_B.md l.4519-4521, PROVEN-HERE) records
for the operators built from it. Hence `𝔉_k(G·U) = 𝔉_k(U)` for every chain `U`. Differentiating twice in
the displacement variable, and using that the chain gauge acts on displacements by the **linear** map
`M_G`, gives `Hess𝔉_k(G·U) = M_G∘Hess𝔉_k(U)∘M_G^{−1}` exactly. Put `U = 1`. Then
`Hess𝔉_k(Z) − Hess𝔉_k(1) = M_GHess𝔉_k(1)M_G^{−1} − Hess𝔉_k(1) = [M_G, Hess𝔉_k(1)]M_G^{−1}`. ∎

### H4.2 Corollary HR-2: **(HESS-rel) as stated in §A4.3 is FALSE.** PROVEN-HERE
The pure gauge `Z = G·1` of Lemma HR-1 has `f_k(Z) = 0` **exactly**, so (HESS-rel)'s right-hand side is
`C·0·‖Hess𝔉_k(1)‖_{𝔐→Y} = 0` **in every one of the four pairings of (q3)**, while its left-hand side is the
norm of a nonzero operator. Hence (HESS-rel) forces `[M_G, Hess𝔉_k(1)] = 0` for every chain gauge `G`,
which is false.

**The configuration is inside the class, and it is the lane's own lift.** Take `V := 1^g`, the gauge
transform of the trivial level-`k` field: `max_P|log V_P| = 0 ≤ ε`, so `V ∈ 𝒦(ε)`. By `(CovLift)`
(i)-(iii), `Z^off` is covariant on `𝒦(ε)` **for every gauge** (BFT_B.md l.3845), so
`Z^off(1^g) = (Z^off(1))^g = 1^g`, a pure gauge. **So the counterexample is not an artefact of leaving the
representative unfixed in (q2): it is the lane's own lift, at a field in the lane's own class.**

**Exhibited witness (exact integer arithmetic, `checks/hr1_flat.py`, output `checks/hr1_out.txt`).**
`N = 2` (adjoint, `dim 𝔤 = 3`), `T = 8`, `G(y) = g^{y_1}` with `Ad_g` the quarter turn about the 3-axis.
Gate **hr1-D PASS**: `0` of `64` plaquettes are non-flat, i.e. `f = 0` exactly. Gate **hr1-A FAIL (route
refuted)**: the level-0 block `E = d_Z^*d_Z − d^*d` has **512 nonzero integer entries**, with the explicit
witness `‖Eλ‖² = 4` against `‖(d^*d)λ‖² = 20` for a standard basis vector (gate **hr1-C4** fires: the
comparison operator is not zero). So the difference is not a small relative perturbation either — it is
`1/√5 ≈ 0.447` of the operator it perturbs, at **zero** curvature.
Both designed-FAIL controls fired: **hr1-C1** (constant gauge) gives `E = 0` exactly, and **hr1-C2**
(abelian, `Ad ≡ 1`) gives `E = 0` exactly — so what hr1-A detects is **nonabelian** content, matching
bb11's **C1** control for the B1 defect at BFT_B.md l.4538.

### H4.3 Where exactly the extension dies, in one line
`(d_Z − d)λ(b) = (Ad_{Z(b)} − 1)λ(y') =: (δλ)(b)` — this is §41.4 step 3's own `δ` (BFT_B.md l.4576). Hence
  **`d_Z^*d_Z − d^*d = δ^*d + d^*δ + δ^*δ`,  `‖δ‖ ≤ c_N sup_b|log Z(b)|_{own}`,**
and the same computation gives the soft blocks with `Q^Z − Q` in place of `δ`. **Every term is governed
by the background CONNECTION `log Z`, not by the background CURVATURE `F_Z`.** By contrast (41.1) and
(41.3) are governed by `|log W_p|` and by the straight residual — both curvature. **So the two defects do
not sit inside the difference as its leading part; they sit inside the *second-order algebra* built on an
already-replaced `d_Z`, measuring the failure of two flat identities (`dd = 0`, root covariance) among
the replaced operators.** The replacement itself is unpriced by §41.2 (c), and the replacement is the
whole of `E`.

Gate **hr1-B FAIL (extension does not hold)** is the exact statement of this, mechanically: on the flat
configuration, **B1 is nonzero at 0 plaquettes and B2 at 0 pairs**, while `E` has **512** nonzero entries.
A bound on the two defects cannot bound `E`, because the two defects are `0` where `E` is not.

### H4.4 The sentence in §A4.3 that is wrong, named
§A4.3's reason (1) for not banking the route says the unenumerated part is benign because *"the rest is
the replacement of `d, Q` by `d^Z, Q^Z`, which is what B1/B2 price"*. **That clause is false.** B1 prices
`d_Zd_Z − 0`; B2 prices `Q^Z_{str}d_Zev − d_Zev`. Neither prices `d_Z − d`. The enumeration §A4.3 says
"is the work" would have found this at its first term. This is not a small correction: it is the
difference between a curvature-sized and a connection-sized object, i.e. between `O(f_k)` and `O(1)`.

### H4.5 And it is not rescued for the curved lift either
One might hope that for a genuinely curved `Z^off(V)` the connection is small even though the pure-gauge
case is degenerate. It is not, globally: **SF's BNA-F4** — *"`‖log Z‖` is not small in any global gauge on
a large torus … holonomies accumulate"* (BFT_B.md l.4529, SF.md l.702, l.724). The only statement the
lane has is **frame-local**: Corollary CL-iv gives `sup_j‖log Z^off_j‖_{C^{1,α}} ≤ C_1f_k` **on a frame**
`Ω^{(−r)}` (BFT_B.md l.4573, needing coarse side `≥ 16`, `T ≥ 17`), which is precisely why Lemma FR-price
can run a Neumann series on a box of coarse side 4 and nowhere else. **So the honest size of `‖E‖` for
`Z^off(V)` is `O(1)`, not `O(f_k)`, outside `𝒞_glob`** — and inside `𝒞_glob` the route is already
Theorem BA (§H2.3).

**TL3 verdict: the bound does NOT extend from two defects to the whole difference. It dies at the very
first term of the enumeration, `d_Z^*d_Z − d^*d`, on a currency mismatch — not in the combinatorics, not
in the defect count, not in the weights.**

---

## §H5 The Neumann series in the weighted pair: it converges, it is free, and that is the problem (TL4)

Run anyway, because the route's value depends on *where* its weight sits, and the answer is that none of
it sits in the series.

### H5.1 Proposition HR-3 (the series): PROVEN-HERE, as an implication
Write `𝓛_1 := Hess𝔉_k(1) + Γ^TΓ` and `𝓛_Z := Hess𝔉_k(Z) + Γ_Z^TΓ_Z` for the gauge-fixed composite
Hessians, `E := 𝓛_Z − 𝓛_1`, both read as maps `𝔐 → Y`.
> Assume **(G♯_0-field)**: `‖𝓛_1^{−1}‖_{Y→𝔐} ≤ M_0`, uniformly in `k`, `T` (BFT_B.md l.3840; OPEN).
> Assume **(FWD-0)** of §H1.1: `‖𝓛_1‖_{𝔐→Y} ≤ Λ_0`, uniformly in `k`, `T`.
> If `M_0‖E‖_{𝔐→Y} < 1` then `𝓛_Z` is invertible and
> `‖𝓛_Z^{−1}‖_{Y→𝔐} ≤ M_0/(1 − M_0‖E‖_{𝔐→Y})`, uniformly in `k`, `T`. **That is `(GAP-Z)`.**

*Proof.* `𝓛_Z = 𝓛_1(1 + 𝓛_1^{−1}E)` with `𝓛_1^{−1}E : 𝔐 → 𝔐` of norm `≤ M_0‖E‖_{𝔐→Y} < 1`; the Neumann
series `Σ_{n≥0}(−𝓛_1^{−1}E)^n` converges in `B(𝔐)` with norm `≤ (1 − M_0‖E‖)^{−1}`, and
`𝓛_Z^{−1} = (Σ_n(−𝓛_1^{−1}E)^n)𝓛_1^{−1} : Y → 𝔐`. ∎

**So the device works and costs nothing.** Its entire content is the hypothesis `M_0‖E‖_{𝔐→Y} < 1`.
Substituting (HESS-rel) would give `‖E‖ ≤ Cf_kΛ_0`, hence the condition

  **`C·Λ_0M_0·f_k < 1`,  i.e. `ε < 1/(C_NCΛ_0M_0)`** (using `f_k ≤ C_Nε`, Theorem N2 (N2-0) (a)).

The controlling quantity is `Λ_0M_0 = ‖𝓛_1‖·‖𝓛_1^{−1}‖`, the **condition number of the flat gauge-fixed
Hessian in the weighted pair**. §A4.3 asserts that the weights remove the `L^{2k}` amplification; the
anchored version of that assertion is `(G♯_0-field)` **plus** `(FWD-0)`, and `(FWD-0)` is **stated
nowhere in the lane** (§H1.1). Without it the series' threshold is not known to be `k`-uniform at all.

### H5.2 The exponent window (my own symbols; `θ_w` not inherited)
The series is a two-norm Banach argument and **imposes no exponent condition of its own**. An exponent
condition appears only if `E` is supplied slot-wise rather than as a single bounded operator. Suppose,
counterfactually, that `E` were level-diagonal with own-unit relative sizes `e_l ≤ CL^{−2(k−l−1)}f_k`
(§41.2 (c)'s shape). With `ϖ_l = L^{ϑ^𝔐(k−l)}` on `𝔐` and `ω_l = L^{ϑ^Y(k−l)}` on `Y` (§H1.1 (q3)), the
weighted operator norm is
  `‖E‖_{𝔐→Y} ≤ C L²f_k·sup_{0≤l<k}L^{−(2 − ϑ^Y + ϑ^𝔐)(k−l)}·sup_l‖𝒪_l‖`,
which is bounded uniformly in `k` **iff**

  **`ϑ^Y − ϑ^𝔐 ≤ 2`.**

That is the whole window, and it is **wide**: lane A's `Y`-weight is `ϑ^Y = θ` with `θ > α > 0` required
by Theorem GU and `θ < 1` in Theorem Cg-nr's range (BFT_B.md l.4741, l.4661), and `ϑ^𝔐 ≥ 0`, so the
window is satisfied with a margin of more than `L²`. For comparison — and this is a comparison of
*windows*, not an inheritance of symbols — NORMS' pair for BFT-1 is quoted at BFT_B.md l.4661 as
`(θ_w^c, θ_w^r) = (2, 3)`, and NBG_A's Theorem NB-4 reports `(N-bg)` itself needing only
`θ_w^c > 7/4, θ_w^r > 1`. **The Neumann series needs less than either.**

### H5.3 Reading
**The convergence is free; 100% of the content is `(HESS-rel)`; and `(HESS-rel)` is false (§H4).** The
window result is therefore true and useless on its own: it says that *if* someone produces a
curvature-sized, level-diagonal bound on the Hessian difference, the rest is three lines. Nobody can,
because the difference is not curvature-sized. **Pre-stated outcome O1 does NOT occur.**

---

## §H6 Can the route be repaired? Yes, partially — and the repair names what the real input is

The failure of §H4 is that the comparison point is wrong: `Hess𝔉_k(1)` is the Hessian at a chain whose
**connection** is zero, while the class is only controlled in its **curvature**. The repair is to compare
against the nearest **flat** chain rather than against the trivial one. At a flat comparison point
Lemma HR-1's obstruction vanishes identically, by construction.

### H6.1 The repaired statement and its inputs
> **(HESS-rel′) [named here; GAP].** There is `C < ∞` depending only on `(N, L, κ_±)` such that for every
> `k`, torus and `V ∈ 𝒦(ε)`, with `Z = Z(V)` and `Z^♭ = Z^♭(V)` as supplied by (FLAT-REF) below,
> `‖𝓛_Z − 𝓛_{Z^♭}‖_{𝔐→Y} ≤ Cf_k·Λ_0`.
>
> **(FLAT-REF) [named here; OPEN].** For every `V ∈ 𝒦(ε)` there are a **flat** chain `Z^♭` (every
> contractible holonomy exactly `1` at every level) and a chain gauge `g` with
> `Z(V) = g·(Z^♭e^{a})`, `|a_j(b)|_{own} ≤ Cρ_jf_k` at every level, uniformly in `k` and `T`.
>
> **(G♯_0-flat) [named here; OPEN].** `(G♯_0-field)` holds **uniformly over the flat chains**:
> `‖𝓛_{Z^♭}^{−1}‖_{Y→𝔐} ≤ M_0` for every flat `Z^♭`, uniformly in `k`, `T` and in the holonomy.

**Proposition HR-4 (the repaired reduction): PROVEN-HERE, as an implication.** `(FLAT-REF)` +
`(G♯_0-flat)` + `(HESS-rel′)` + `(FWD-0)` ⟹ **`(GAP-Z)`**, with the same three lines as Proposition HR-3
and the same window `ϑ^Y − ϑ^𝔐 ≤ 2`, provided `C_NCΛ_0M_0ε < 1`. (`Z^♭` and `g·Z^♭` give the same
inverse bound, since `M_g` is an isometry of the covariant norms by Lemma CONJ (iii).) ∎

### H6.2 What the repair costs, stated plainly — and why **"(N-bg) adds no paper" is not supported**
1. **`(FLAT-REF)` is `(UHL)`-strength, and it is the wall.** It is a *global* lattice Uhlenbeck/Coulomb
   statement with a flat reference. Lane A's `(UHL)` is its **frame-local** version — *"a lattice local
   Coulomb (Uhlenbeck-type) gauge on a coarse box of side `3ℓ`"* — and is **OPEN** (BFT_A.md l.250-255,
   status l.309; PROOF.md l.6835). `(FLAT-REF)` is strictly weaker than membership of `𝒞_glob` (which
   demands `Z^♭ = 1`) and strictly stronger than nothing, and it is exactly the content SF's BNA-F4 says
   is missing. **The route therefore does not avoid `(UHL)`; it re-derives the need for it.**
2. **`(G♯_0-flat)` is strictly larger than `(G♯_0-field)`.** `(G♯_0-field)` is at the trivial chain
   (BFT_B.md l.3840); `(G♯_0-flat)` is a family of statements indexed by the flat moduli, with uniformity
   over that family. So even granting everything else, **the paper is not "the flat `(G♯_0-field)`"**:
   it is `(G♯_0-field)` over the flat moduli space, plus `(FLAT-REF)`.
3. `(HESS-rel′)` is the only genuinely session-scale piece, and §41.2 (c)'s slot-wise machinery (with the
   corrections of §H3.3) is the right tool for it, since `a` is now `O(f_k)`.

### H6.3 One thing the repair gains, and it is new: **§41.5 (i) does not block `(G♯_0-flat)`**
§41.5 (i)'s no-go is stated for backgrounds with `F_Z ≠ 0` (BFT_B.md l.4587: *"No gauge makes a background
with `F_Z ≠ 0` translation invariant"*). A flat chain on the torus can be written with **constant** link
variables `Z^♭(y, μ) = h_μ` with commuting holonomies, and then the gauge-fixed Hessian `𝓛_{Z^♭}` has
site-independent coefficients — it **is** exactly translation invariant. So LINEAR_PACKAGE Theorem 4.2 /
4.2′'s momentum-space continuation applies to it verbatim, with the lattice difference operators
`e^{ip_μ} − 1` replaced by `Ad_{h_μ}e^{ip_μ} − 1`. **`(G♯_0-flat)` is therefore in reach of the frozen
linear package's own method rather than of a new paper** — and the lane already has a device pointed at
exactly this case: *"the flat classes with non-trivial holonomy are covered separately by N2-a's constant
lift, failure mode BNA-F4"* (PROOF.md l.3345), with Lemma N2-a PROVEN-HERE and *"vanish[ing] on every
flat class"* (PROOF.md l.473).
**The honest caveat, and it is real:** the strip conditions (S1)-(S7) must hold **uniformly in the shift
`h`**, and the gauge-fixed operator's near-kernel changes dimension as `h` approaches the centre (the
covariantly constant modes are the centraliser of the holonomy group). Uniformity across that
stratification of the flat moduli is a genuine analytic hypothesis, not bookkeeping, and I do **not**
claim it. Status of H6.3: **ARGUED** (that the no-go's premise does not cover the flat case: that part is
PROVEN-HERE, being a statement about the hypothesis of a read proof), **with the uniformity in `h` OPEN**.

---

## §H7 Check record

Criteria `checks/hr1_criteria.md` (2026-10-28 21:44:36 UTC), written after §H0 and **before**
`checks/hr1_flat.py` existed. Script `checks/hr1_flat.py`, output `checks/hr1_out.txt`, stderr
`checks/hr1_err.txt` (empty). Pure python, exact integer arithmetic, no numpy/BLAS, no numeric lock
needed (brief rule 6). Nothing was rerun and no criterion was edited after the run.

| gate | pre-registered verdict rule | result | reading |
|---|---|---|---|
| **hr1-D** | PASS iff every plaquette of the MAIN configuration is exactly flat | **PASS** (0 of 64 non-flat) | the precondition holds; `f = 0` exactly |
| **hr1-A** | PASS iff `E = d_Z^*d_Z − d^*d = 0` | **FAIL (route refuted)** — 512 nonzero integer entries; witness `‖Eλ‖² = 4` | **(HESS-rel) is FALSE**; HR-F1 OCCURS |
| **hr1-B** | PASS iff B1 or B2 is nonzero wherever `E ≠ 0` | **FAIL (extension does not hold)** — B1 nonzero at 0 plaquettes, B2 at 0 pairs | §41.2 (c) cannot bound `E` |
| **hr1-C1** control | fires iff `E = 0` for a constant gauge | **FIRED** (`E = 0`) | hr1-A is not an arithmetic artefact |
| **hr1-C2** control | fires iff `E = 0` in the abelian case | **FIRED** (`E = 0`) | what hr1-A sees is **nonabelian** content |
| **hr1-C3** control | fires iff B1 `≠ 0` on a curved background | **FIRED** (B1 nonzero at 2 plaquettes; B2 at 2 pairs) | hr1-B is not a blind test |
| **hr1-C4** control | fires iff `‖(d^*d)λ‖² > 0` for the witness | **FIRED** (`= 20`) | the witness is not compared against zero |

**All three designed-FAIL controls fired as designed, and the two substantive gates failed as
pre-registered.** No gate was added after seeing a result; no probe here is post-hoc.
**What the check does not show** is restated from the criteria: it tests the level-0 Wilson block only
(sufficient to refute a bound on the whole difference, insufficient to size it); it says nothing about
the repaired statement of §H6; and the claim that the same failure occurs for a genuinely curved
`Z^off(V)` is **argument** (§H4.5, from BNA-F4 and CL-iv's frame-locality), **not** check output.

---

## §H8 Outcome, against §H0.3-§H0.5

**Pre-registered outcome: O2 occurs for the route as stated, and O3 occurs for its repair.** O1 does not
occur. O4 does not occur (§H3.4).

| target | result | status |
|---|---|---|
| **TL1** | (HESS-rel) restated with all five quantifiers (§H1.1); two hidden inputs surfaced — **(FWD-0)** and the conditionality of (B2) on `(C_g-θ)` | **done** |
| **TL2** | §41.2 (c) re-derived for B1 and B2 from (41.1)/(41.3); identities **confirmed exactly**; *slot-wise* holds with a **corrected reason for B1**, *weight-free* holds **given the unstated (W-lev)**, *factor-k-free* holds | **PROVEN, with 3 corrections** |
| **TL3** | the bound does **not** extend; it dies at the first term `d_Z^*d_Z − d^*d`, a **connection**-sized object | **Corollary HR-2: (HESS-rel) PROVEN FALSE** |
| **TL4** | the Neumann series converges; condition `C_NCΛ_0M_0ε < 1`; window **`ϑ^Y − ϑ^𝔐 ≤ 2`**, wider than any the lane assumes; **no exponent condition of its own** | **Proposition HR-3 PROVEN-HERE as an implication** |
| **TL5** | lane B did not decline it: it **uses** the series (§41.4 step 4, §41.5 (ii)) and recorded its domain three times (S11-F6; BFT_B l.103; BFT_A §3.10). The route is lane A's Theorem BA route, valid on `𝒞_glob`; outside, it needs **(UHL)** + **(SL-cov)**, OPEN | **answered** |
| **TL6** | see below | **(GAP-Z) UNCHANGED** |

**Failure modes:** **HR-F1 OCCURS** (the currency mismatch — this is the kill). **HR-F2 OCCURS** (the
pair mismatch `𝔐_Z` vs `𝔐_1`) but is not load-bearing. **HR-F3 OCCURS in the weak form** (B1 has no `𝒪`;
repaired by (W-lev), §H3.3). **HR-F4 does NOT occur** (geometric level decay; §H3.3 (c)). **HR-F5 OCCURS**
and **HR-F6 OCCURS** (§H2).

**(GAP-Z): UNCHANGED — still OPEN, and not reduced.** What changed is that it is **localised**:
`(GAP-Z) ⟸ (FLAT-REF) + (G♯_0-flat) + (HESS-rel′) + (FWD-0)` (Proposition HR-4), with `(FLAT-REF)` of
`(UHL)` strength and `(G♯_0-flat)` strictly larger than the flat `(G♯_0-field)`.

**The claim in §A4.3 that "(N-bg) adds no paper: the paper is the flat (G♯_0-field)" is NOT SUPPORTED**,
on three independent grounds: (HESS-rel) is false (§H4); the repair needs `(G♯_0-flat)` over the flat
moduli, not `(G♯_0-field)` at `U = 1` (§H6.2 item 2); and it needs `(FLAT-REF)`, which is the OPEN
`(UHL)`-strength global gauge (§H6.2 item 1). The one piece of good news is §H6.3: §41.5 (i)'s no-go
does **not** cover the flat-with-holonomy case, so `(G♯_0-flat)` is plausibly inside the frozen linear
package's own method rather than outside it — **ARGUED**, with uniformity over the flat moduli OPEN.

**Tally added by this file: 0 items closed. 2 PROVEN-HERE (Lemma HR-1, Corollary HR-2 — a refutation),
2 PROVEN-HERE as implications (Propositions HR-3, HR-4), 1 ARGUED (§H6.3), 3 new named OPEN items
((FLAT-REF), (G♯_0-flat), (HESS-rel′)) and 2 new named hypotheses surfaced in existing work ((FWD-0),
(W-lev)). Nothing here is counted in PROOF's tally by this worker.**

---

## FOR OTHER FILES (not edited)

1. **`NBG_A.md` §A4.3 (owner: the T55-D worker).** The route **(HESS-rel)** is **REFUTED as stated**
   (HESSREL.md §H4, Corollary HR-2, with an exact integer witness in `checks/hr1_out.txt` and all three
   designed-FAIL controls fired). The specific sentence that fails is reason (1)'s clause *"the rest is
   the replacement of `d, Q` by `d^Z, Q^Z`, which is what B1/B2 price"* — B1 prices `d_Zd_Z`, B2 prices
   the root-covariance identity; **neither prices `d_Z − d`**, which is connection-sized and is the whole
   of the difference. §A4.3's own honest caveat ("I have not enumerated the difference term by term, and
   that enumeration is the work") was right: the first term of the enumeration kills it. The concluding
   claim *"(N-bg) adds no paper: the paper is the flat (G♯_0-field)"* should be withdrawn or replaced by
   the reduction of HESSREL §H6.1. **The rest of NBG_A is not touched by this**: Theorem NB-5's reduction
   of (N-bg) to (H1)+(H2)+(H3) and the vertex count of §A3 are independent of §A4.3.
2. **`BFT_B.md` §41.2 (c) (owner: lane B).** Three refinements, none of which changes the verdict
   PROVEN-HERE for B1/B2 (HESSREL §H3): (i) for **(B1)** the phrase *"`𝒪` the operator already present in
   that slot"* has no referent — the flat `d∘d` is identically zero; the correct form is
   `E_{B1} = e_j·(ι_j∘ev_c)` with `‖ι_j∘ev_c‖ = 1`, and **(B1) changes slot** (0-form in, 2-form out),
   so (ii) the weight-freeness argument *"the weights act on the slots, which `E` and `𝒪` share"* needs
   the unstated hypothesis **(W-lev)**: the weight families are indexed by **level alone**, not by form
   degree. Lane A's `ω_l = L^{θ(k−l)}` satisfies it. This is the same genus of distinction §43.4 already
   drew for level-crossing compositions, and should be added there. (iii) §41.2 (c)'s unqualified
   `e_l ≤ Cρ_{l+1}²f_k` is unconditional for (B1) only; for (B2) it is **CONDITIONAL on `(C_g-θ)`**
   (l.4547), and downstream quotations drop that.
3. **`BFT_A.md` §3.11 / lane A (owner: lane A).** A forward bound is needed and appears nowhere:
   **(FWD-0)** `‖Hess𝔉_k(1)‖_{𝔐→Y} ≤ Λ_0`, `k`-, `T`-uniform. Every perturbative transport off the
   trivial chain is controlled by the **condition number** `Λ_0M_0`, not by `(G♯_0-field)`'s `M_0` alone.
   If `(FWD-0)` is already implicit in the §33 pair's construction it should be stated; if it is not
   `k`-uniform, every Neumann-series transport in both lanes inherits that.
4. **`PROOF.md` / the master ledger (owner: the lead).** Nothing needs recounting: `(GAP-Z)` is
   **UNCHANGED, OPEN**. One optional note, if the lead wants the route recorded as walked:
   *"[S25] (HESS-rel) (NBG_A §A4.3) REFUTED (HESSREL §H4, PROVEN-HERE with an exact witness): the
   composite chain Hessian difference is connection-sized, not curvature-sized, and vanishes nowhere that
   BFT_B §41.2 (c)'s two defects vanish. The repaired route is `(GAP-Z) ⟸ (FLAT-REF) + (G♯_0-flat) +
   (HESS-rel′)`, all OPEN; `(FLAT-REF)` is `(UHL)`-strength."*
5. **`SESSION24_RESULTS.md` dead-route list (owner: the lead).** Add: **(HESS-rel) as stated in NBG_A
   §A4.3 — refuted at zero curvature; do not re-walk.** Do **not** add "Neumann series from the trivial
   chain" as dead: it is the live route on `𝒞_glob` (BFT_A Theorem BA) and frame-locally (Lemma FR-price
   step 4); what is dead is applying it **globally outside `𝒞_glob` without a gauge**.
6. **For whoever owns `THETAW.md` (concurrent).** The Neumann series of HESSREL §H5 needs **no** `θ_w`.
   Its only exponent condition is `ϑ^Y − ϑ^𝔐 ≤ 2` between the `Y` and `𝔐` level weights (my symbols,
   §H5.2). So the `θ_w` repair, whatever it concludes, does not constrain this route and this route
   should not be cited as a consumer of `θ_w`.

---

## §H9 CORRECTIONS (appended 2026-10-28 21:55:52 UTC; §H0-§H8 stand unaltered as the record)

Two corrections. The first is **to my own check**, found by me. The second is **to the input my brief
named**, delivered mid-flight by the lead from `NBG_ADJ.md` (T55-K). Neither changes the verdict of §H4;
the second strengthens it by removing a second leg the route was standing on.

### H9.1 A defect in MY OWN criteria, and the corrected gate. Disclosed.
Gate **hr1-A** (§H7) computed `d_Z^*d_Z − d^*d` with `d_Z` acting on **0-forms**. That is the
Faddeev-Popov / chain-gauge block — a real lane object (it is exactly the normal operator of §41.4 step
4's Neumann series, BFT_B.md l.4578) — but it is **not** the Wilson block of `Hess𝔉_k`, which has `d_Z`
acting on **1-forms** (`½‖dB_0‖²`, PROOF.md l.6613). **So hr1-A as pre-registered tested an adjacent
operator.** The amendment at `checks/hr1_criteria.md` (2026-10-28 21:53:48 UTC) records the defect and
pre-registers the corrected gates **before** `checks/hr1_wilson.py` was written; `checks/hr1_flat.py` and
`checks/hr1_out.txt` were **not** rerun and are **not** edited. The corrected gates are **POST-HOC**
relative to the first run and are labelled so here.

| gate (post-hoc) | rule | result |
|---|---|---|
| **hr1-D′** | PASS iff the configuration is exactly flat | **PASS** (0 of 64 non-flat) |
| **hr1-A′** (Wilson block, 1-forms) | PASS iff `E_W := d_Z^*d_Z − d^*d = 0` | **FAIL (route refuted)** — **1536** nonzero integer entries; witness `‖E_Wu‖² = 8` against `‖(d^*d)u‖² = 10` |
| **hr1-A″** (Feynman-fixed shape) | PASS iff `E_H := (d_Z^*d_Z + d_Zd_Z^*) − (d^*d + dd^*) = 0` | **FAIL (route refuted)** — **1024** nonzero entries |
| **hr1-C1′** control | fires iff both are `0` for a constant gauge | **FIRED** |
| **hr1-C2′** control | fires iff both are `0` in the abelian case | **FIRED** |
| **hr1-C4′** control | fires iff `‖(d^*d)u‖² > 0` | **FIRED** (`= 10`) |

Output `checks/hr1_wilson_out.txt`, stderr `checks/hr1_wilson_err.txt` (empty). **The corrected gate
fails harder than the original**: on the Wilson block the "perturbation" has norm `√(8/10) ≈ 0.894` of
the operator it is supposed to perturb, **at exactly zero curvature**. §H4's verdict is unchanged and is
now exhibited on the right operator.

### H9.2 The flat input named in my brief is the wrong object, and I say so rather than re-label
`NBG_ADJ.md` **Finding A6** (ARGUED there) rules, against NBG_A §A4.3, that a Neumann series stated in
the **𝔐 → Y** pair needs the flat inverse **in that same pair and on the composite slice**, whereas
**`(G♯_0-field)` is stated "in the §33 pair" (BFT_B.md l.3840) on the per-level slice**. The required
object is a **fourth** object — the adjudication's *flat 𝔐-pair composite-slice bound* — whose status is
**recorded nowhere**, and which `FLATZ.md` (T55-Q) was launched to pin down. `FLATZ.md` did not exist
when I checked (2026-10-28 21:54 UTC); I did not wait on it and I have not duplicated that work.

**Stated plainly, as asked.** §H5's **Proposition HR-3 is structurally correct and its proof is
unaffected** — it is the ordinary two-norm Neumann estimate and uses only that the forward and inverse
bounds live in matching pairs. **But the input I named in it, `(G♯_0-field)`, does not exist in the pair
the proposition is stated in.** I built the series against it because my brief named it; I am not
re-labelling it silently. The correct reading of HR-3 is:

> **Proposition HR-3′ (the correction).** Proposition HR-3 holds verbatim with `(G♯_0-field)` replaced
> throughout by **(FLAT-𝔐)**: *the `Z = 1` composite-slice chain-Hessian inverse bound
> `‖𝓛_1^{−1}‖_{Y→𝔐} ≤ M_0`, in lane B's own `𝔐 → Y` pair, `k`- and `T`-uniformly* — `NBG_ADJ.md` Finding
> A6's fourth object, **status unrecorded**. Likewise **(FWD-0)** of §H1.1 is a statement about that same
> operator in that same pair.

**This correction does not rescue, weaken or alter §H4.** §H4 is a statement about the **left-hand side**
of (HESS-rel) — the operator `E` — and is therefore **independent of which flat bound sits on the right**.
Lemma HR-1 and Corollary HR-2 use no flat inverse bound at all. So:

> **Even if T55-Q finds (FLAT-𝔐) PROVEN, the route still fails**, because `‖E‖` is not `O(f_k)` in any
> pair, on any slice, for any comparison chain whose connection is zero. The two failures are
> independent, and mine is the one that does not depend on an unrecorded status.

Correspondingly, in §H6: **(G♯_0-flat)** must be read as *(FLAT-𝔐) uniformly over the flat chains* — the
fourth object over the flat moduli — and the sentence in §H6.2 item 2 becomes stronger, not weaker: the
repaired route needs an object that is not merely larger than `(G♯_0-field)` but **is not `(G♯_0-field)`
at all**. §H6.3's observation survives intact and gains force: it says the *method* of LINEAR_PACKAGE
Theorem 4.2′ (momentum-space continuation) is not blocked at a flat background with non-trivial
holonomy — a statement about the method, not about which pair the conclusion is read in.

### H9.3 NBG_A §A4.2's "two independent derivations": I never used it, and it is false
The lead reports that NBG_A §A4.2's second leg is cited verbatim from BFT_B l.4594/l.4737 — the very
claim under refutation — so the collapse is **single-sourced**. **Nothing in this file rests on NBG_A
§A4.2.** §H2's answer to TL5 is sourced directly to BFT_B.md l.103, l.4377, l.4746, l.4578, l.4591 and
BFT_A.md l.27, l.89-90, l.232, l.250-255, l.306, l.309 and PROOF.md l.6835, each read in place. §H4 rests
on PROOF.md l.6605 and BFT_B.md l.4517-4527 (Lemma CONJ) plus my own re-derivation and arithmetic. The
only thing I take from NBG_A is the **wording of the target** (§H0.2), which I quote in order to refute.

### H9.4 Two further items from the concurrent files, checked against my own result
1. **`THETAW.md` (T55-J).** `θ ≤ 1 − α` is **not** a proven constraint (`BFT_A.md` l.560-561, l.833-834;
   the `¾` ceiling of l.396-397 is superseded), and `(α, θ)` are universally quantified over
   `0 < α < θ < 1`. **I inherited no `¾` cap**: §H5.2's window is `ϑ^Y − ϑ^𝔐 ≤ 2` in my own symbols, and
   with `ϑ^Y = θ < 1` and `ϑ^𝔐 ≥ 0` it holds with more than `L²` to spare. THETAW's warning that **θ is
   three objects and α is two** does not bite here, because §H5.2 never reads a `θ` out of a file: it
   derives the condition from the weight exponents it defines itself. The window stands.
2. **`NBG_ADJ.md` §4.2.** (N-bg)'s live consumer needs only an `O(k)`-uniform (GAP-Z), not an
   `O(1)`-uniform one. **This does not help the route.** The Neumann condition is `M_0‖E‖_{𝔐→Y} < 1`;
   with `M_0 = O(k)` it becomes `‖E‖ ≲ 1/k`, and §H4 gives `‖E‖ = O(1)`, which fails for every `k`. A
   weaker target does not repair a perturbation that is not small.

### H9.5 Status after the corrections — unchanged where it matters
**(GAP-Z): UNCHANGED, OPEN.** **(HESS-rel) as stated in NBG_A §A4.3: REFUTED** (Corollary HR-2,
PROVEN-HERE; exhibited on the Wilson block by the corrected post-hoc gate hr1-A′, with both controls
firing). **The route now fails for two independent reasons** — the perturbation is not curvature-sized
(mine, §H4, independent of any unrecorded status), and the flat input it names is the wrong object in the
wrong pair on the wrong slice (`NBG_ADJ.md` A6, ARGUED). The repaired reduction of §H6.1 stands with
`(G♯_0-flat)` re-read as *(FLAT-𝔐) over the flat moduli*:

> **(GAP-Z) ⟸ (FLAT-REF) + (FLAT-𝔐 over the flat moduli) + (HESS-rel′) + (FWD-0)**, all OPEN or
> unrecorded, with **(FLAT-REF)** of `(UHL)` strength and therefore the wall.

**Additions to the FOR OTHER FILES list below, from §H9:** item 2 of that list is unaffected; items 1 and
4 should be read with `(G♯_0-field)` replaced by `(FLAT-𝔐)`; and for **`FLATZ.md` (T55-Q)**: *the object
you are pinning down is needed by this route only on the right-hand side; HESSREL §H4 refutes the route
on its left-hand side, so a PROVEN verdict from you does not revive (HESS-rel) as stated. It does revive
the §H6.1 repaired reduction, whose remaining wall is then (FLAT-REF), a global `(UHL)`-strength gauge.*
