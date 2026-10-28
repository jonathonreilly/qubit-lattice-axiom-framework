# PRE-STATED

UTC: 2026-10-28 23:01:31 UTC. Independent hostile review of the two reversals in REVIEW55_BFTB.md and the additional COF-crit objection. This section is recorded before reading the scientific arguments under review.

Refutation criteria, fixed in advance:

1. **CO-fun reversal:** an exact source/operator mismatch in the claimed dipole decomposition; a LIN0/GU hypothesis or norm mismatch that prevents a uniform estimate for either piece; or a coarse-torus charge/flux obstruction (including periodic seams and harmonic/winding currents) that defeats the stated supremum bound. A valid identity alone does not prove the response estimate. A failed old counterexample alone does not prove the entire positive theorem.
2. **Supporting check:** a PASS that follows from defining both sides identically, a negative control incapable of detecting a real defect, inexact numerical evidence presented as exact, or a check whose operators differ from the written definitions. Reproduction and independent algebra will be distinguished from proof of all scales.
3. **GZ-FALSE reversal:** TOWER-VAR actually contains weighted curvature contributions at positive levels, or the actual g_Z/CovLift statement requires such contributions even if the action does not, or a residual-slot argument still needs an unproved curvature identification. Conversely, an explicit substitution of a different functional into GZ-SLOT refutes its application to the lane, even if the resulting abstract algebra is correct.
4. **COF-crit:** the claimed Ward identity must provide the full charge cancellation required by the cited CO-fun version, not merely vanishing against root-pinned gauge variations. A legal critical-point identity extending to root values would refute the proposed second defect. Any surviving level-count factor must be retained.

Method and scope: no git; no writes outside this report; large source files read only through searches and bounded sed ranges; exact rational/integer arithmetic for executed checks; verdicts CONFIRMED / NOT-VERIFIED / REFUTED tied to files and locating strings. Lane-A inputs are conditional inputs, not independently certified construction theorems. Final disposition will state precisely what can be banked.

Additional check criteria, recorded before the independent implementation: construct the four-dimensional L=3 dipole with all 24 axial orders and all 81 starting sites; fill each closed path by signed unit-square swaps, independently of r55b's Gaussian elimination. Require the exact boundary of the averaged filling to equal path minus Q-transpose-delta, with support in the two lifted boxes. Project to coarse tori T=1,2,3, including seam translations, and require equality to survive. Deleting the filling must produce a nonzero defect on an explicitly chosen basis 1-form. Independently check the face-sum coarse-flux identity and its capacity bound on exact rational currents, including a constant winding current. These checks concern finite combinatorial identities; analytic uniformity is proved conditionally below.

Additional critical-point falsification criterion, before its numerical enumeration: at k=1, L=3, T=2, use the fine boundary link e=((2,0,0,0),0). Its endpoints are not block roots. Test the predicted exact full-S4' identity Q(delta_e)=delta_((0,0,0,0),0)/27 by enumerating every coarse link, order and starting site. If this fails, do not use the proposed pure-gauge critical-point counterexample without diagnosing the failure. The counterexample itself will use an exact nonzero Taylor coefficient, not numerical logarithms.

## Scope, source identity and verdicts

Review completed: 2026-10-28 23:21:26 UTC.

One independent review pass; no git, source edits, commits, workers, audit-state changes or writes outside this file. The local review-loop procedure supplies evidence discipline only. The user's narrower read/write contract controls. This is a conditional mathematical review, not certification of a constructive Yang–Mills theory or of the quoted lane-A estimates.

All science paths below are relative to this directory. Sources inspected by locating strings and bounded sed ranges include `REVIEW55_BFTB.md` Findings 3–6 and 16; `BFT_B.md` §§9.0, 12.0–12.2, 21.0, 22.8–22.10, 25.5, 27.1, 29.1–29.2, 31.2, 34.1, 35.1–35.7 and 42.1–42.3; `BFT_A.md` §§1.1–1.4, 7.1–7.3, 8.4, 26.0–26.1, 28.7–28.8, 31.0–31.1 and 33.3–33.4; `LINEAR_PACKAGE.md` §§1.1–1.2; `PROOF.md` TOWER-VAR and NA-alg; `REVIEW_BFT_B_S9_S10.md` S10-6, S10-10 and S10-11; `REVIEW55_LEAD.md` H15; the dipole script, criteria and recorded output. Older `CODEX_REVIEW_COFUN.md` findings were compared after the independent derivation. X1 is reserved for the end-of-review reconciliation.

Observed source metadata (UTC; no claim of a git revision): `BFT_A.md`, 351969 bytes, 2026-10-28 12:03:19; `BFT_B.md`, 662171 bytes, 14:17:44; `PROOF.md`, 725837 bytes, 22:55:48; `REVIEW55_BFTB.md`, 69410 bytes, 22:59:20. Locating strings below are authoritative if line numbers subsequently move.

| Reviewed assertion | Verdict | Exact scope |
|---|---|---|
| Root-dipole identity | **CONFIRMED** | Full linearised S4′ map, all orders, d=4; also across periodic seams and on small coarse tori |
| `r55b_dip.py` supporting algebra and controls | **CONFIRMED** | Reproduced exactly; three in-memory mutations rejected by its recorded criteria; it does not test analytic response bounds |
| LIN0/GU applicability to the dipole pieces | **CONFIRMED** | Trivial background, m=0, fixed 0<α<θ<1; no co-closedness condition on the residual coefficient |
| Coarse flux with sup bound Σ_l π_l(j_l) | **CONFIRMED** | Direct face-sum construction, including vector currents and periodic/harmonic cases |
| Whole-class CO-fun reversal | **CONFIRMED** | Conditional on precisely the analytic inputs used by COF; retain the top-response term in the Hölder estimate |
| §35.7's falsity verdict and `[S10-fix 1]` restriction | **REFUTED** | The purported large isolated term is not a lower bound on the full response |
| GZ-SLOT's identification of the lane functional; GZ-FALSE as applied to it | **REFUTED** | TOWER-VAR has Wilson curvature only at level 0, whose G-slot weight is 1 |
| Withdrawing CURV-dec as a required input of this g_Z argument | **CONFIRMED** | Does not close nonlinear CovLift or certify its remaining BCH estimates |
| H15's fixed-representative / infimum repair as the lane's correct conclusion | **REFUTED** | It preserves the erroneous higher-level curvature slots |
| CD gives CC-0 at every critical point | **REFUTED** | Wrong gauge domain; an explicit small pure-gauge critical family below has nonzero pointwise root charge |
| S10-6's unremoved level-count loss | **CONFIRMED** | A loss of the available upper estimate, not a proved lower bound on actual nonlinear responses |

## 1. Dipole identity and the exact checks

**CONFIRMED.** Sources: `LINEAR_PACKAGE.md`, locating `T^σ_y = P^σ(c_X → y)` and `Linearisation`; `BFT_A.md`, locating `7.1 Setting LIN` and `r_l(x) := Q_lx_l - x_{l+1}`; `REVIEW55_BFTB.md`, Finding 5, locating `The counterexample to the falsity claim (exact)`.

Let e=(X,μ) be a level-k link and p_e its straight L-edge path between the corresponding level-(k−1) roots. Write Q=Q_(k−1). The column Q^Tδ_e is the average of the **entire** root-to-root contour currents, including the two axial handles, over all y and coordinate orders. Thus

    v_e := p_e − Q^Tδ_e,       d*v_e = 0.

More is true than zero divergence. Lift the two neighboring boxes to the integer lattice. Both paths have identical lifted endpoints and remain inside the rectangle of dimensions 2L × L × L × L. Their difference is the boundary of a plaquette chain inside that rectangle. One explicit construction sorts the coordinate steps of the closed path by adjacent swaps; each swap contributes its signed unit square. The sorted closed path has zero edge current. The sorting preserves each coordinate's sequence of signs, so its partial coordinate sums stay within the original rectangle. Averaging these fillings gives

    d*G_e = p_e − Q^Tδ_e,
    supp G_e ⊂ B(X) ∪ B(X+e_μ),       ||G_e||_∞ ≤ C(L,4).

For example the loop length is at most M=2L+4(L−1), and M(M−1)/2 bounds the number of square swaps before averaging. This crude bound is independent of k and T. Projecting the filling to the torus proves the identity at seams as well. For T=1 the two lifted boxes overlap after projection; the multiplicity is at most 2. The individual paths can wind, but their **difference has zero lifted displacement** and remains a projected boundary. Zero divergence alone would not have established this.

For x_k=0, pairing with x_(k−1) gives exactly

    <q p_e, x_(k−1)> = <q δ_e, r_(k−1)(x)> + <q G_e, d x_(k−1)>.

The sign is positive in both source slots. There is no κ factor in this identity: κ belongs to the quadratic energy, whereas the source term is −<s,r>. For nonzero fixed data an additional constant q x_k(e) appears in the functional equality; it does not change the source response. CO-fun below concerns the homogeneous-data response.

### Reproduction and control audit

Ran, without redirection or bytecode writes:

    python3 -B .claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/r55b_dip.py

Observed: D1, both D2, D3, D4 and D8, and D5–D7 all PASS; final text `VERDICT r55b_dip: ALL PASS (D4 controls fired)`. Both orientations give max|G|=1/3. The support sizes are respectively |supp v|=27,13 and |supp G|=10,6. These match the recorded output.

The check is not a test of an analytic estimate. Its stated model is d=2, L=3, k=2, T=3 with one axial order. Within that model it genuinely checks existence of a filling with restricted support: it constructs Q from contours, forms v, builds the plaquette-boundary matrix separately, solves over the rationals, checks all touched links and excludes nonzero v outside them. Solving for G is appropriate to an existence claim; it is not an assumption that the constrained system is solvable. The random pairing checks are supplementary; D8 is algebraically redundant with D2(d).

D4 is a meaningful non-vacuity control. Once v≠0, choose a basis 1-form supported on any edge where v is nonzero. Deleting G then gives discrepancy v(e)≠0. The original seeded trials detect this in both orientations. It would be wrong to treat D4 alone as a verification of Q or of a uniform response estimate.

Three **in-memory** mutations were run; the original file was unchanged:

| Mutation | Observed rejection |
|---|---|
| Replace Qmap's L^d divisor by L^(d−1) | D1, both D2 and both D8 fail |
| Discard the constructed G | Both D2, D3 and D8 fail |
| Disable the branch that fires the deletion control | Both D4 fail |

In every case `allpass` was False. A runner limitation remains: the script prints failure but does not set a nonzero process exit status. Any future automated gate must inspect/assert `allpass` or parse the verdict; exit code 0 alone is insufficient.

### Independent full-S4′ check

The separate implementation used integer coordinate-word swaps and rational averaging, not the supplied Gaussian solver or any imported check code. It checked all 24 orders × 81 y-values for each of four directions, verified the boundary of **each** contour filling, then the averaged identity and support. It projected the result at X=0 and at X=(T−1,…,T−1), for T=1,2,3. Every case passed. The unequal filling sizes reflect the chosen coordinate-sorting algorithm, not unequal operators.

| μ | Contours | Nonzero filling plaquettes before projection | max|G_e| | Periodic/seam cases | Nonzero deleted-G basis discrepancy in last case |
|---|---:|---:|---:|---:|---:|
| 0 | 1944 | 298 | 1/3 | 6 | −1/36 |
| 1 | 1944 | 298 | 1/3 | 6 | −1/324 |
| 2 | 1944 | 294 | 2/9 | 6 | −1/324 |
| 3 | 1944 | 270 | 13/81 | 6 | −1/324 |

These finite checks corroborate the all-L combinatorial argument above; they do not replace it.

## 2. LIN0/GU really cover the two pieces

**CONFIRMED conditionally on those estimates.** Sources: `BFT_A.md`, locating `7.2 Norms`, `Theorem BL-5`, `Theorem GU ((G♯-up)`, `28.7 Theorem GU`, `28.8 Corollary LIN0`, and `Lemma BL-C`.

LIN0's restriction is **level-wise co-closed plain currents**. There are no plain currents in the dipole's rewritten (s,G) source. The residual s_(k−1)=qδ_e is explicitly allowed without d*s=0; BL-5(a) covers arbitrary residual coefficients. The G-piece enters as d*G and is automatically co-closed. GU explicitly permits arbitrary level-l 2-forms and uses only their sup norm for l≥1. No root-charge restriction is being evaded.

For k≥2 the nonzero slots are a fixed single scale below the top:

    ||s||_R = L^θ |q|,
    ||G_(k−1)^c||_∞ ≤ L² C(L,4)|q|,
    ||j||_Pc = L^(3+θ)|q|.

If the full G-slot norm is wanted, its lattice spacing in coarse units is 1/L, so a sup bound gives a Hölder bound with only a factor depending on L and α. GU's single-level factor is (k−(k−1)+1)² L^α = 4L^α. Hence the response satisfies

    ||x(q p_e)||_inv ≤ C(L,κ_±,α,θ)|q| ≤ C' ||j||_Pc,

uniformly in k,T. BL-C converts the Campanato output to the required pointwise Hölder output with no k-dependent factor. For k=1, use W0 on G_0 and BL-5 on s_0; the plain source is priced by ||j_0^c||, and all conversion factors still depend only on L,α,θ.

This directly rules out the alleged L^(2k−3) growth **for this canonical source** under the accepted lane-A estimates. It does not, by itself, settle every composite source; that requires the next two steps.

## 3. Coarse flux: an explicit construction, including winding

**CONFIRMED.** Source under review: `REVIEW55_BFTB.md`, Finding 5, locating `The general case (derivation)`; geometric definitions: `LINEAR_PACKAGE.md`, locating `The levels are nested`.

Consider first the plain-current part j of a composite-co-closed source. Its divergence D_j:=Σ_l ev_l^T d*j_l is supported on the level-k roots and has total zero. This remains true even in the presence of a top residual slot, because that slot has only root-supported divergence; the other non-plain slots have zero divergence off the roots. Write q(X)=D_j(c_X), and

    J := Σ_(l=0)^(k−1) π_l(j_l),       π_l(j_l)=L^(3(k−l))||j_l||_∞.

At level l let m_l=L^(k−l), and partition its sites into boxes

    C_l(X)=m_l X+{0,…,m_l−1}^4.

Define b_l(X,μ) to be the sum of j_l(z,μ) over the m_l³ positive μ-links exiting the μ-face of C_l(X). Define b=Σ_l b_l. The discrete divergence theorem, with d* equal to incoming minus outgoing flux, gives

    (d*b)(X) = Σ_l Σ_(z∈C_l(X)) (d*j_l)(z)
              = Σ_(z∈C_0(X)) D_j(z) = q(X),
    ||b||_∞ ≤ Σ_l m_l³ ||j_l||_∞ = J.

The middle equality uses the actual nested-root placements: a level-l root lies in the level-0 box C_0(X) exactly when its level-l site lies in C_l(X). The final equality uses root support of D_j. The construction works directly for Lie-algebra-valued currents in any fixed norm; no scalar max-flow theorem is needed to infer a vector capacity bound.

For scalar currents this also verifies the reviewer's max-flow premise. For every coarse set A, |Σ_(X∈A)q(X)|≤|∂A|J, including sets crossing the periodic seam. Together with total neutrality this is the finite network feasibility condition for an antisymmetric flow of capacity J. At T=2, keep the distinct periodic bonds as parallel edges. At T=1 the coarse links are loops and q=0, so there is no feasibility obstruction.

Harmonic/winding currents do not need to be gradients or plaquette boundaries. Their divergence is zero. The explicit b may retain their winding, or a different feasible b may leave it in j−P(b). Either is allowed. Only p_e−Q^Tδ_e, whose zero winding was proved separately, is filled by plaquettes. Thus this argument never applies a contractible-box filling theorem to an arbitrary torus cycle.

Independent exact face-sum checks used two rational current components. For d=2, scales m=3,9 and T=1,2,3, the bound was J=116/7; all 2,16,512 coarse cuts respectively passed. For d=4, m=3 and the same three T, J=261/7; every coarse-site divergence and face capacity passed. Constant winding currents with components (2/3,−4/5) produced nonzero coarse flux (8,−48/5) in the d=2 two-scale tests and (18,−108/5) in the d=4 tests, with exactly zero divergence. All arithmetic used integers and `Fraction`; no floating-point feasibility or optimization was used.

## 4. Whole-class CO-fun and the exact error in the old refutation

**CONFIRMED as a conditional theorem.** Sources: `BFT_B.md`, locating `The named open item (CO-fun), stated precisely`, `35.3 Lemma DF-cc`, `35.4 Proposition COF-size`, and `35.5 Theorem COF`; `REVIEW55_BFTB.md`, Findings 4–5.

First correct the terminal-slot error in the old proof. With the top field fixed, arbitrary unpinned λ changes the top residual by d ev_k λ. Consequently, as full level-0 functions,

    D(S^G)=0,
    D(S^s)=ev_k^T d*s_(k−1),
    D(S)=D_j+ev_k^T d*s_(k−1).

Lower residual slots cancel telescopically. The top term need not vanish. `BFT_B.md`, locating `35.2 Lemma SPLIT`, is **REFUTED pointwise** but remains correct as a statement of annihilation on the permitted pinned gauge space. In particular CC-0 for the total source does not imply CC-0 for its plain part. D5–D7 reproduce that exact defect. Also use ĵ_0=j_0+h_0^Tψ_0 in the regrouping; the exception `ĵ_0 := j_0` in §27.1 must not silently delete this term.

It suffices to use COF's proof on a **strict plain-only** source. There the corrected DF identities are valid without the SPLIT mistake. Writing A(j)=Σ_l(Q_str^(0→l))^T ĵ_l, strictness gives C(j)=A(j), d*C(j)=0 and the intermediate-level analogues. FT gives

    Σ_l π_l(ĵ_l) ≤ [1+2d/(1−L^(−3))] Σ_l π_l(j_l).

At d=4,L=3 the bracket is exactly 121/13. COF step (c) pairs C(j) against the unconstrained gauge-minimal representative legitimately, using d*C=0 and YH's N(Y^p)≤C_YN n. Its units are n²·n^(−3)·n=1. The residual pairings use PW-cc and, with m=l−1−a, carry

    L^(k−l+a) L^(−3a) L^(−3(k−l)) = L^(−2(k−l)) L^(−2a).

Both sums are bounded by the same Σ_l π_l(ĵ_l), uniformly in k,T. Thus the strict plain-only sup bound costs C J, with no top-response term. Step (d), using LES-div, LE and BL-C, adds only κ_+||r_(k−1)^c|| for the Hölder bound. The quoted dependencies are YH, W0/LES-div/LE/BL-C, GU, LIN0/BL-5 and PW-cc's residual bounds; this review does not promote those inputs beyond their own conditional scope.

Now let b be the flux from §3 and put P(b)=Σ_e b(e)p_e at level k−1. Then

    j'=j−P(b),       D(j')=0,
    P(b) ≡ (s_(k−1)=b, G_(k−1)=Σ_e b(e)G_e).

The straight root paths of a fixed orientation partition their root rows, so ||P(b)||_∞≤||b||_∞. Therefore

    Σ_l π_l(j'_l) ≤ (1+L³)J.

The fillings have bounded overlap, independent of T,k, including the projected small-torus case. Hence ||Σ_e b(e)G_e||_∞≤C(L,4)||b||_∞. LIN0/GU, or W0 at k=1, bound the entire response to P(b) by C J. Superpose this response, the strict j' response, and the original G and s responses. No assertion that the original S^j is CC-0 is needed.

Write

    N := ||G_0^c||_∞+[G_0^c]_α+||G||_Y+||s||_R+J.

The resulting estimates are

    ||f_0(S)||_∞ ≤ C N,
    ||f_0(S)||_∞+[f_0(S)]_α^∞
        ≤ C [N+κ_+||r_(k−1)^c(x(S))||_∞].                 (C2-COF)

The top residual initially belongs to the strict response. The difference from the full response consists of the LIN0/GU-bounded pieces, so replacing it by the full response's top residual adds at most C N. Finally

    J ≤ ||j_0^c||_∞ + ||j||_Pc Σ_(t=1)^(k−1)L^(−θt)
      ≤ ||j_0^c||_∞ + ||j||_Pc/(L^θ−1).

This is the original §31.2 CO-fun estimate on the **whole** composite-co-closed class, at m=0, trivial background and fixed 0<α<θ<1, with constants independent of k,T. Its sup half has the stronger form without the top-response term. It is not a nontrivial-background or m>0 result, nor does it give a source-only bound for the full invariant norm.

### Why the previously reviewed refutation was wrong

**REFUTED.** `BFT_B.md`, locating `35.7 Proposition COF-res`, `with every other term bounded as in Theorem COF`, and `[S10-fix 1]`; `REVIEW_BFT_B_S9_S10.md`, locating `S10-11`.

The identity for the regrouping defect, involving n²Σ_XD_j(c_X)Φ_k(Y_0^p)(c_X), survives. Its interpretation as the **only** unbounded contribution does not. When the root charges are nonzero, the companion object paired with Y_0^p is not shown co-closed; COF step (c)'s replacement by the unconstrained gauge-minimal representative is unavailable for that object. The decomposition has representative-dependent pieces whose large values can cancel in the invariant response. A nonzero single-root coefficient also does not supply a lower bound on the neutral dipole difference.

S10-10 had already withheld the assertion that all other terms were bounded. S10-11 nevertheless certified falsity from the very isolated term whose separation had not been justified. That is the precise logical failure of the original review. The dipole identity supplies an explicit bounded-response decomposition for its canonical proposed obstruction, and (C2-COF) supplies the positive whole-class implication. This is stronger than merely observing that the old refutation lacked a proof.

The earlier `CODEX_REVIEW_COFUN.md` F2 correctly withheld falsity, and F14/F15 correctly flagged the two domain/notation defects. Its OPEN conclusion was appropriately limited to that packet; the new decomposition closes the stated conditional curvature estimate. No conclusion here repairs off-composite-co-closed gauge-fixing estimates or proves a TENT-Q bound considered as a separate absolute pairing.

## 5. GZ-FALSE uses the wrong functional and the wrong level-0 weight

**REFUTED as a claim about the lane's g_Z.** Sources: `PROOF.md`, locating `Lemma TOWER-VAR` and `Wilson at level 0, one soft term per level`; `BFT_A.md`, locating `1.1 The composite problem`; `BFT_B.md`, locating `Setting GI (covariant centring)`, `(CovLift)`, `42.1 Lemma GZ-SLOT`, `𝔉_k = Σ_j F_j`, and `42.2 Proposition GZ-FALSE`.

The actual definition is

    𝔉_k(U_0,…,U_(k−1);V_k)
       = S_W(U_0)+Σ_(j<k) κ_j Σ_c φ̂_c(M̄^(j)_c(U_j);U_(j+1)).

It is **not** Σ_j [E_j^br(U_j)+κ_jΣ_cφ̂_c]. The E_j^br terms are effective lower-chain values used in the per-level recursion; TOWER-VAR telescopes their values at critical branches. Summing them as separate terms of the composite functional counts the lower action repeatedly. Moreover an effective E_j^br is not identified with a Wilson plaquette action at level j.

For variations u of the free levels, the exact derivative has the form

    D𝔉_k(Z)[u] = DS_W(Z_0)[u_0]
        + Σ_(j<k) κ_j Dφ̂_j(Z_j,Z_(j+1))[u_j,u_(j+1)],
    u_k=0.

The background Feynman term 1/2||D_Z^*x||² has derivative zero at x=0, so it adds nothing to g_Z. At the linear level the components are explicitly

    (g_Z)_0 = d*d Z_0+κ_0 Q_0^T r_0,
    (g_Z)_j = κ_j Q_j^T r_j−κ_(j−1)r_(j−1),       1≤j<k.

There is no independent d_j^*F_j(Z) term for j≥1. Nonlinear differentiation introduces the genuine soft-density and residual Jacobians, not new Wilson actions at these levels. In particular soft gradients vanish when their soft fluctuation vanishes: `PROOF.md`, locating `φ := N^{-1}[Re tr(W_0^{-1}M)` and `is stationary in M at V = W_0(M)`.

The remaining curvature slot is at level 0. Both `BFT_A.md` §1.4 and §7.2 explicitly set its weight to **ω_0=1**. Only positive-level G slots have ω_l=L^(θ(k−l)). The residual weights are different: ω_l^R=L^(θ(k−l)) **including l=0**. GZ-FALSE's displayed lower bound uses fictitious positive-level curvature slots and also replaces the exceptional G weight at l=0 by L^(θk). Neither step matches the definitions.

Consequently GZ-FALSE fails already for the natural fixed source representation of the actual functional. It is unnecessary to settle the separate question of an infimum over all representations to reject it. `BFT_B.md` §9.0 actually defines Y as **source representations**, with a map π:Y→X*; the later assertion that an infimum reading is "forced" is not a replacement for that definition. An arbitrary added tuple of higher-level curvatures cannot be treated as the actual g_Z without proving that it represents the same functional.

There is another logical defect in the claimed `for every lift`: a known uniform upper bound f_l≤C f_k does not prove a lower bound on every lift, and a maximal exponent established for another quantified class is not automatically a universal obstruction for all lifts. That point is secondary here because the slots and ω_0 are already wrong.

### What the replacement does, and does not, establish

**CONFIRMED:** the purported need for CURV-dec from this argument is removed. The level-0 Wilson source is priced by its unweighted curvature/Hölder size, using the frame regularity required in CovLift(iv)'s first clause. The θ-dependent soft-source requirement is the residual estimate

    κ_l L^(θ(k−l)) ρ_(l+1)^(−2) |r_l(Z)| ≤ C_g ||b||_∞,

locating `(C_g-θ)` in `BFT_B.md` §21.0, together with the stated local Jacobian/BCH estimates. `BFT_B.md` §22.8 proves the linear residual implication; §22.9 labels the nonlinear BCH remainder **ARGUED**. Those qualifications survive this review.

The wording "just C_g-θ" is safe as a statement of the remaining weighted soft-source obligation once the frame and local analytic estimates are supplied. It is **not** an unconditional proof of nonlinear CovLift, nor a proved equivalence between a norm of the total gradient and each separately chosen source component. The normalized soft density is not literally |r|²/2 at finite field. Its Jacobian corrections must remain in the accounting; `BFT_A.md`, locating `The soft gradient κ(∂ρ/∂x)^Tρ`, already records such rows. They are residual-dependent corrections, not the independent F_j curvature tower used by GZ-SLOT. This review does not certify the full nonlinear slot bound from the scalar C_g-θ inequality alone.

**Reconciliation with H15:** `REVIEW55_LEAD.md`, locating `r55l-H15`, is right that a fixed-representative estimate cannot by itself bound an infimum, but its proposed final lane status is **REFUTED**. Restricting GZ-FALSE to a fixed representative retains the wrong composite functional and wrong slots. Thus the correct conclusion on this target is REVIEW55_BFTB Finding 16's withdrawal, with the nonlinear qualification above, not H15's continued CURV-dec gate. CURV-dec can remain a separately posed curvature-approximation problem; it is not established here as necessary for CovLift.

## 6. COF-crit: the domain defect is real, and an exact critical counterexample exists

**REFUTED:** `BFT_B.md`, locating `35.6 Corollary COF-crit` and `as an identity of level-0 functions`. **CONFIRMED:** REVIEW55_BFTB Finding 6(a)'s objection to the use of CD.

`BFT_A.md` §31.0 defines K_x for `ξ = 0 at level-k roots`. Its §33.3 proof starts `For ξ vanishing at the level-k roots`. Thus CD proves annihilation on that test-function space, equivalently D^⊥(𝔑^0)=0 at criticality. It supplies no pointwise equation at the roots. Allowing the top data to transform would introduce its own boundary variation, not an additional stationary equation for the fixed-data problem.

The root value can be determined without CD. At a critical point, 𝔑^0=Hx−NB. Apply an **arbitrary** unpinned linear gauge variation to this quadratic form, keeping x_k=B fixed. Wilson and lower residual quadratic terms are invariant; the top residual changes by d ev_k λ. Therefore, as a level-0 function,

    D(𝔑^0)=κ_(k−1) ev_k^T d*r_(k−1)(x;B),

where r here is the **linear** residual. This term is not eliminated by nonlinear stationarity.

An explicit counterexample strengthens "not proved" to falsity of the asserted **every-critical-point** statement. Set k=1, d=4, L=3, T=2, B_1=0 and N=2. Let a=(2,0,0,0), a'=a+e_0=(3,0,0,0), e=(a,0), X=(0,0,0,0), Y=X+e_0. Neither a nor a' is a block root. Choose

    A = [[0,1],[-1,0]],       B = [[0,i],[i,0]],
    [A,B] = diag(2i,−2i) ≠ 0.

For real t sufficiently small put g_t(a)=exp(tA), g_t(a')=exp(tB), and g_t(z)=1 elsewhere. Let U_t(z,μ)=g_t(z)g_t(z+e_μ)^(−1). The gauge is 1 at every level-1 root. Hence every plaquette holonomy and every complete S4′ contour is 1, the coarse data is 1, and U_t is an **exact critical point** of the actual TOWER-VAR functional. Its logarithm x(t) lies in any specified small 𝔐 ball for sufficiently small t at this fixed lattice size.

Define ξ(a)=A, ξ(a')=B, ξ=0 elsewhere. Only e has two nonzero endpoint generators, so, exactly as a local analytic identity,

    x(t)=−t dξ+δ_e R(t),
    R(t)=log(exp(tA)exp(−tB))−tA+tB
        =−(t²/2)[A,B]+O(t³).

The edge e crosses a block face. All axial handles stay inside blocks and therefore give zero on δ_e. The straight averaging leg crosses e for exactly L choices of its longitudinal starting coordinate and one choice of each transverse coordinate. Thus

    Qδ_e=L^(−3)δ_(X,0)=δ_(X,0)/27,
    Qdξ=d ev ξ=0,
    D(𝔑^0(x(t);0))=(κ_0/27) R(t)(δ_(c_Y)−δ_(c_X)).

The t² coefficient at c_Y is **−κ_0[A,B]/54**, and at c_X its negative. These are nonzero exact coefficients. No numerical logarithm, floating-point limit, or unproved genericity claim is used. The full Qδ_e identity was independently enumerated over **all 64 coarse links × 1944 contours**: the only nonzero entry was exactly 1/27 at (X,0). This corroborates the direct counting proof.

The family has D^⊥=0 as CD requires, but fails CC-0 for sufficiently small nonzero t. It refutes the universal wording in COF-crit. It is not a claim that this pure-gauge representative is the slice-selected fixed point for trivial data; that additional restriction would require a separate statement. In any event CD alone cannot supply the missing root equation on that narrower set.

## 7. The level-count loss survives, with the right logical strength

**CONFIRMED:** `REVIEW_BFT_B_S9_S10.md`, locating `S10-6`, and REVIEW55_BFTB Finding 6(b), for failure of the stated uniform deduction. Sources for the input sizes: `BFT_A.md`, locating `28.12 Corollary NC` and `The remainders V_l`; `BFT_B.md`, locating `35.6 Corollary COF-crit`.

The given estimate π_l(V_l)≤C_0η² has **no level decay**. It implies only

    ||V||_Pc ≤ C_0 L^(θ(k−1))η²,
    Σ_(l=1)^(k−1) π_l(V_l) ≤ C_0(k−1)η².

These are upper bounds, not automatic asymptotic equalities. Direct use of (C2-COF), avoiding the exponentially weighted maximum, yields an O((k−1)η²) upper bound for the positive-level plain contribution to curvature sup; include the level-0 and other O(η²) slots to write O(kη²) for the full source. The Hölder conclusion still carries the full response's top residual unless independently bounded.

Removing the unnecessary CC-0 restriction removes one obstacle to applying the estimate; it does not add decay to the rows. Thus COF-crit's k-uniform O(η²) conclusion remains **NOT-VERIFIED**, and its proof is **REFUTED**. Conversely these size estimates do not prove that actual nonlinear responses grow linearly in k or that every alternative proof must lose k. The symbols `≍` in the two reviews must be read as bounds on a possible worst-case source-size budget, not a proved lower bound for realized remainder rows. A new level-decay/cancellation estimate is still needed for the desired uniform conclusion.

## End-of-review reconciliation

`CODEX_REVIEW_X1.md` was read **after the independent work above**, through its final verdict (lines 1–745; observed completed size 30554 bytes, modification time 2026-10-28 23:16:54 UTC). Sources: locating `Every cut is controlled; an explicit current proves more than max-flow`, `The remainder is in COF's class`, and `Exact statement that can be banked`.

The reviews agree on the sup theorem, the explicit face-sum flux, the terminal residual in D(S), periodic/harmonic cases, the defective old term-to-total inference and the surviving row-summability issue. X1 subtracts U(b)=Q^T b and identifies its response with a datum b/κ; the present proof instead subtracts the straight path source P(b) and uses its residual-plus-G decomposition. These are compatible identities, P(b)=U(b)+d*G(b), with independent ways of bounding the added piece.

X1 correctly distinguishes a **source-only** norm from COF's full right side, which includes a response-dependent top residual. The N in (C2-COF) is explicitly source-only. Its Hölder proof separately pays for changing the response whose residual is measured; it does not use the ambiguous comparison criticized in X1.

X1 banks **only the sup half** and marks the full Hölder statement NOT-VERIFIED by that review. There is no contrary Hölder counterexample there. This review's additional conclusion uses the extra checked step: the removed P(b), G and s responses have their entire invariant norms bounded by LIN0/GU; BL-C bounds their pointwise Hölder output, and their top residuals are bounded as well. COF step (d) applies to the strict plain-only remainder. The triangle inequalities then give precisely the second line of (C2-COF), with the original full response's top residual retained. Thus X1 corroborates the shared sup core; **it is not cited as independent confirmation of the additional Hölder extension**.

No verdict about other X1 dependencies or other findings in either Opus report is imported merely because these conclusions agree.

## Exactly what may be banked

1. **CONFIRMED — conditional whole-class CO-fun.** Fix d=4, odd L≥3, N≥2, 0<κ_-≤κ_l≤κ_+, and 0<α<θ<1. At the trivial background and m=0, for every k≥1, T≥1 and homogeneous-data Setting LIN^cc source S in the stated P0, Pl-c, G and R classes, bank (C2-COF), with C independent of k,T and dependent on the fixed parameters and the named COF lane-A input constants. Equivalently bank §31.2's original bound after J≤||j_0^c||+||j||_Pc/(L^θ−1). **Keep the top-response term in the Hölder estimate.** The stronger source-only sup bound is also confirmed. Withdraw §35.7's falsity verdict and `[S10-fix 1]`'s mandatory CC-0 restriction. Preserve the terminal-slot and ĵ_0 corrections when reusing the proof.
2. **CONFIRMED — exact supporting algebra.** Bank the full-S4′ dipole decomposition and the coarse face-flux construction, with the torus and winding qualifications proved above. Bank `r55b_dip.py` as an exact finite-model algebra check with working deletion controls, supplemented by this independent four-dimensional construction. Do not bank an analytic theorem from that runner, or use its exit status alone as a failure gate.
3. **REFUTED — GZ-SLOT/GZ-FALSE for TOWER-VAR.** Withdraw the claimed universal failure of CovLift(iv)'s g_Z clause and the alleged CURV-dec prerequisite arising from §42. The actual independent curvature source is at level 0 with ω_0=1. Bank the residual/soft-source formulation of the remaining θ obligation, **conditional on frame regularity and the genuine local Jacobian/BCH controls**. The full nonlinear CovLift bound remains NOT-VERIFIED here; Cg-NL's ARGUED remainder is not promoted. H15's proposed fixed-representative/infimum repair is not the correct lane disposition.
4. **REFUTED — CC-0 at every critical point; CONFIRMED — the narrower Ward statement.** Bank CD only on root-pinned test directions, hence composite co-closedness. The explicit pure-gauge family above refutes the stronger pointwise claim. The k-uniform nonlinear-row conclusion of COF-crit remains NOT-VERIFIED: the available sup estimate costs O(kη²), and its Hölder version also retains the top residual. Bank that as an unremoved estimation loss, **not** as a lower-bound/no-go theorem for all possible improvements.

