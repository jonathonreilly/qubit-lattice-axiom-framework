# Check of library/m3.md

- File checked: library/m3.md (1139 lines; research text by Codex, gpt-6-astra; repository
  revision 0234b7d135 in its header; FINISH row 471, LAYER-M).
- Task: one line-by-line check of the claimed supplier of premise M of the frozen layer part
  (layer-thm-part.md 1440–1475), against the brief prior/m3.md §5.1–5.3 and the (M3) verdict in
  gates/layer-part-ref.md 187–274.
- Date: 2026-11-08.
- Status: complete.

Sources read for this check: prior/m3.md 62–181 (consumer census), 235–376 (§4–§5);
gates/layer-part-ref.md 187–274; layer-thm-part.md 1430–1479; m3.md in full, by ranges;
layer-pkg.md 93–135 ((1.4), (S5), (1.5)), 655–700 (§5.1), 770–792 (c_ζ, (5.9));
walks-gw.md 40–92 (theorem, (T1)–(T3)), 480–492 (cutoff reads), 560–600 (cube count),
700–730 (Θ'_J); print-inverse-r2.md 313–328, 721–754, 889–931, 989–992 (footprints, q_0);
CA-I 13686–13726 (c^(1), c^(2), j_J, k_J, m_J), 14400–14412 (chart current), 14436–14495
(representation identity, 𝒦_1), 14722–14728 (native P_1), 15262–15340 (K10), 15676–15700 and
15790–15860 (K6), 72373–72470 (exempted-set lemma), 72530–72580, 72700–72730, 72828–72862
(link, second entry), 72918–72980 (first-stage expansion), 94978–94996, 111380–111410,
111530–111550, 112608–112626; CA-II 39314–39336, 39634–39650; SA 10540–10600.
Imports PI, GW, GW1 and the frozen layer part are used as given and are not re-checked.

## Verdict summary

| Section | Verdict | One line |
|---|---|---|
| 1.1 Pairings, carriers, scales (37–123) | ADVANCE | Spaces = layer-pkg; footprint = PI (r̂ = (2L+2)M_t); tag (5) = CA-I 72384–72391 and K10's rule. |
| 1.2 Bare mass words (125–215) | ADVANCE | (10) is exact by (4); every surviving word has its whole carrier in F_τ ⊂ one component; (9) and the transpose bound are correct. |
| 2.1 Dictionary at one (219–304) | ADVANCE | Words at one only; q_0 = PI (a); Neumann forms = layer-pkg (1.4) and GW 742. |
| 2.2 Two new primitives (306–381) | ADVANCE | Table sums to 𝒦_1 of CA-I 14447 at one; one union tag per complete word; (18)–(19) are CA-I 111397–111399 and 111542–111543. |
| 2.3 Theorem M (383–418) | ADVANCE | All six items of prior/m3.md §5.1 are stated. |
| 3 Imports and scope (420–467) | REVISE (wording) | The remark on SA 10578 states the outline's fact but not why (6) is compatible with it (R1). |
| 4.1 Physical absolute algebra (475–609) | ADVANCE | Scale table correct; (22)–(25) correct; no cancellation used. |
| 4.2 Tags, tails, constants (611–669) | ADVANCE | (26)–(27) follow from GW; e^{16κ_1} with spare e^{μt}; holomorphy with κ_1^+ room. |
| 4.3 Exact component restriction (671–707) | ADVANCE | Kernel locality and identical restriction from complete footprints; (28) at site (T). |
| 4.4 Intertwiners, total at one (709–761) | ADVANCE | Gauge, reality, transport per word; P = I − R used only at one. |
| 5.1 Current of the layer (765–801) | ADVANCE | (29) = (S5); the definition change is explicit. |
| 5.2 Bounds, locality, source-free (803–877) | ADVANCE | (32) = layer-pkg (5.3); (33) = (5.9); (0,0,1) proved; zero-switch test passes. |
| 5.3 Agreement at one (879–918) | ADVANCE | (34) and 𝒦_1 recover CA-I 14444–14448; K6 gives (35). No continuation in switches. |
| 6.1 Cut tails and amplitudes (922–976) | ADVANCE | (37) correct; product-profile premise kept as an input; (38) correct. |
| 6.2 Readers and derivatives (978–1020) | ADVANCE | Matches CA-I 72945–72980 exactly (same r = e^{κ_1} − 1). |
| 6.3 Use-by-use record (1022–1058) | ADVANCE | Every row of the digest census is matched; no consumer needs K10's old off-one current. |
| 7 Constant order (1060–1105) | ADVANCE | Non-circular; consistent with CA-I 15266–15322 and SA's order (κ̄ before ℓ_P). |
| 8 Scope (1107–1139) | REVISE (wording) | Stale "not checked" header line 3; name the partition-covering hypothesis of line 106 among the external inputs (R2). |

## 1. Definitions and the first hard step (lines 35–215)

### 1.1 Pairings, carriers and scales (37–123) — ADVANCE

- (1) is the norm pair of layer-pkg.md 57–91 and of SA 10562 ff. (‖·‖_ϖ, |·|^♯_ϖ). Full
  stencils, admitted weights with ratio rate δ, no derivative of p. Correct.
- (2): Q per unit length with fine measure η^4, Q^* with row measure m_c^4. This is the
  physical bilinear pairing of SA 10587 ("fine volume η^4 and row volume ξ_c^4"). The
  transpose of (2) is correct.
- (3): density |q| ≤ C_Q m_c^{-4} is the averaging density of a per-unit-length row (an average
  over a double block of volume ~m_c^4). The remark at 83–88 (dimensionless derivative has density
  m_c^{-3}; divide by m_c) is correct. n_av and c_av are fixed by the averaging input; they are
  used only as fixed constants.
- (4): Σ_τ h_τ² = 1 at the base point of each row is PI's partition identity read at one point.
  Exact.
- F_τ: PI's footprint has half-width r̂ ℓ_τ with r̂ = (2L+2)M_t (print-inverse-r2.md 989–990).
  h_τ is supported in half-width M_t ℓ_τ, and every stencil and row read set that meets it lies in
  half-width (M_t + 2L)ℓ_τ (PI 753–754). The margin (2L+1)M_t − 2L ≥ (2L+1)4L − 2L (M_t ≥ 4L,
  PI 745) also holds c_av = 4dL = 16L. So E_c ⊂ F_τ when h_τ(c) ≠ 0, as claimed at 98–104. The
  denominator reads of h_τ are inside F_τ by GW 484–490. Correct.
- (5): t_F(s) = Π_{Δ ∈ π_0, Δ∩F≠∅} s_Δ and Y(s) = K ∪ ⋃_{s_Δ≠0} Δ. These are literally
  (4.21:eq-exempted-set-1) and Y(σ) of CA-I 72384–72391, and the rule of K10 (CA-I 15288–15301,
  quoting CMP 116 after (1.7)). Cubes off π_0 are the exempted set K, with no factor. Components
  through (d−1)-walls, as at CA-I 72437–72438. Correct.
- Line 106: "an admitted full decoupling partition π, covering the ambient read domain". This is a
  geometry hypothesis. It is needed: a word that reads outside ⋃π carries no factor for that part.
  K10's own primitives need the same hypothesis. It is in scope through "the furnished GW geometry"
  (line 1117), but it is not in the list of §3 (R2).

### 1.2 The bare mass words (125–215) — ADVANCE

The word. (6) A_τ b(x) = −Σ_c m_c^4 q(c,x)^T m_c^{-3} h_{τ,B}(c)² b(c). With a = ℓ^{-2}
(layer-pkg (1.4)) and ℓ^{-1} = m_c^{-1} on row c, this is −Q^* a h_{τ,B}² ℓ^{-1}. The h² factor
sits on the row side, before Q^*. The word keeps its whole averaging row E_c. Its tag t_{F_τ}
reads the cubes met by F_τ, and F_τ ⊃ E_c ∪ {base point of c}. This is a complete-word tag,
not an endpoint tag.

Sum at one. (10) follows from (4) row by row. It is a finite identity at a fixed lattice. There
is no remainder. Correct.

Count. F_τ has span 2r̂ ℓ_τ ≤ 2r̂ ℓ_k. The floor M_dec ≥ 4r̂ + 8L gives half a cube side
≥ (2r̂ + 4L)ℓ_k (GW 54–58, 560–571: cube side in units of the largest scale). So F_τ meets at
most two grid intervals per coordinate, hence at most 2^4 = 16 cubes, and |t_{F_τ}| ≤ e^{16κ_1}
on |s_Δ| ≤ e^{κ_1}. This is the account's "m ≤ 2^4" case (CA-I 72458–72460). Correct.

Majorant (9). For fixed x, only rows with x ∈ E_c contribute (at most n_av). Each term is at most
C_Q m_c^{-3} h_τ(c)² |b(c)|. Use m_x^3 m_c^{-3} ≤ L^3, |b(c)| ≤ p(c)|b|_p,
p(c)/p(x) ≤ e^{δ d(x,c)} ≤ e^{δ c_av}, and Σ_τ |t_{F_τ}| h_τ² ≤ e^{16κ_1}. This gives
C_A = C_Q n_av L^3 e^{δ c_av}, as written. It is an absolute word bound; the sign is not used.
The powers are those required by (7): B_0 → F_3. Correct.

Transpose (187–196). ⟨A_τ b, f⟩_fine = Σ_c m_c^4 b(c)·[−h² m_c^{-3} Σ_x η^4 q(c,x) f(x)].
This is the displayed A_τ^T. Bound: m_c^4 |A_τ^T f(c)| ≤ C_L C_Q m_c sup_{E_c}|f|, then scale
comparison and weight ratio. Correct, without a counting transpose.

Two legs and reads (199–209). A surviving word has no zero factor. So F_τ meets no deleted cube.
F_τ is a closed box with connected interior, inside Y(s), so it lies in one wall component. It
contains the output bond x, the input row c and all of E_c (contour transports, frame reads,
coefficient and boundary reads). Restriction: tile, partition denominator and averaging row are
the same in two settings that agree on F_τ (PI §9 and the averaging input). Correct.

Holomorphy. Finite sum, polynomial in s, holomorphic in the base. Correct.

Site (T). K = ∅ and all s = 0: every F_τ meets a cube, so every word dies. No bare diagonal
survives. Correct.

No post hoc indicator. The partition h_τ is fixed by geometry before tagging. The tag is a
monomial whose cube set is fixed by geometry. Correct.

The SA remark (SA 10578) is answered in §3 below and in answer 1.

## 2. The full words and the theorem (lines 217–418)

### 2.1 The unswitched dictionary (219–304) — ADVANCE

- Line 221–222 says that every expression here generates words at one only. This is the correct
  status. No identity between switched sums is used later.
- (11)–(12): patch words and their entries are PI's. q_0 = −m^{-3}[W^{(5)}]_{νν} m matches
  Theorem PI (a), print-inverse-r2.md 328 and 895. The sign comes from the νν block of the
  bordered inverse. Correct.
- 249–251: every exposed identity is I = Σ_τ h_τ² I, with R's signed words h_τ² I_s and −P_ω.
  This is the GW/GW1 identity convention. It is a word choice made before tagging.
- (13): Λ = G'(I_s − P)D_0^T. At one this is CA-I 14403 (Λ = G'RD_U^*) with R = I − P. Used only
  to generate words. Correct.
- (14): c^{(1)}, c^{(2)} match CA-I 13698–13700 (R_b written as Ad_{W_b}); j_J, k_J, m_J by
  pairing with J as at CA-I 13704–13709. J is not differentiated. Correct.
- (15): G_π^J = Σ(G_0Θ'_J)^nG_0 is layer-pkg (1.4) (I − G_0Θ'_J)^{-1}G_0. q_J = Σ(−E_J)^r q_0
  with E_J = q_0Q(G_π^J − G_0)Q^* is (QG_π^JQ^*)^{-1}, since
  QG_π^JQ^* = q_0^{-1}(I + q_0Q(G_π^J − G_0)Q^*) (also GW 742). H = G_π^JQ^*q_Jℓ^{-1} is
  layer-pkg H^J. The form Θ'_J = k_JΛ + Λ^Tj_J + Λ^Tm_JΛ is GW 711–719 in word form
  (ψ = k_J(ΛA), the D_URG' terms are Λ^T terms since G', R are transpose-symmetric at one).
  The n ≥ 1 tail in E_J removes the G_0 − G_0 cancellation before tagging. Correct.
- 300–304: Δ' is kept as one stencil. Correct (GW source norm).

### 2.2 Two new primitives (306–381) — ADVANCE

- (16) B_ω = D_0P_ωD_0^T, differences taken before tagging; the stencils are inside PI's endpoint
  margins (GW 484–490). Correct.
- Mass table. At one the branches sum to
  −Q^*aℓ^{-1} + Q^*q_Jℓ^{-1} + D_0G'^Tj_JH − D_0P^TG'^Tj_JH − Δ'H
  = Q^*(q_J − a)ℓ^{-1} + Λ^Tj_JH − Δ'H.
  With k = (q_J − a)ℓ^{-1} this is 𝒦_1 of CA-I 14447 term by term. Signs agree with
  Λ^J and 𝔍 at CA-I 14405–14408. Correct.
- 337–345: F_w is the union of all complete footprints and local carriers; fixed by geometry and
  labels; independent of W, J, s. Nonzero words have connected interior: a shared leg means a
  shared endpoint margin of positive size (for the j,+ word, h_τ ≠ 0 at a site of the G'_u
  endpoint region puts a box of positive size in F_τ ∩ F_u). Correct.
- (17): one union tag per complete word. 352–356 states that (17) is not the composite and not
  obtained from R(s) = I − P(s). Correct, and this is the brief's requirement (prior §5.3, second
  bullet).
- 358–364: the layer keeps its own tags, its G̃^J(s), H_0, V'_s, and its product-tagged lift
  H(s). Correct and necessary: (18) uses this H(s) in h, and (19) uses it in the commutator.
- (18)–(19) are CA-I 111397–111399 (4.25:eq-current-partner-1) and 111542–111543
  (4.25:eq-cut-layer-partner-1) with 𝖪 = K_W, D^*_WD_W = D_1^TD_1, ℍ = h. Correct.
- 379–381: no bare −a and no exposed I_s − P is left in the coefficient assignment. The untagged
  D_0D_0^T inside Δ_W + K_W is a local stencil of the rider itself, as in the account's form
  (Δ_W − P_1(σ) + 𝖪). It is not a use of R = I − P after tagging. Correct.

Note on lines 322–328, branch q. The word Q^*q_{J,w}ℓ^{-1} keeps the whole left averaging carrier.
The Q, Q^* vertices inside E_J keep their E_c (line 297). Correct.

### 2.3 Conditional theorem M (383–418) — ADVANCE

The six items match prior/m3.md §5.1 items 1–6:
1. holomorphy with tails on a larger polydisc (item 3);
2. (7) with the permitted dependence e^{16κ_1} stated (item 4);
3. exact two-leg locality, coefficient reads, identical restriction, transpose (item 5);
4. intertwiners and the endpoint decay reserve (item 3, last sentence);
5. (20), the value at one (item 1);
6. (18)–(19) as current slots, the outside-multiple convention preserved, value at one, and K6
   only on its physical domain (items 2 and 6).
The product-profile estimate is kept as a separate input (416–417), as the brief requires
(prior 307–312).

## 3. Named imports and scope of the implication (lines 420–467) — REVISE (wording)

- PI, GW, GW1, averaging, layer, rider/readers, and the two at-one identities are listed as
  hypotheses. Each exists at the cited place with the stated content (checked for PI (a), GW
  (T1)–(T3) and 560–600, layer-pkg (S5) and §5, CA-I 14439–14493, K6). Correct.
- 431–433: GW's full-word alternative (GW 88–89: "the same assertion holds if a whole composite is
  instead tagged by its union, without identifying that alternative with the account") is the
  right licence for union tags on new primitives. Correct.
- 455–458: the at-one identities are used only at one, and K6 only on its own domain. Correct.
- 462–466: the outline passages are read. SA 10578 is the sentence "Since the member −𝖺 is
  diagonal and is carried by no proper set, the splitting is built around this member." Line 465
  reports this fact but does not say why the new tagged mass (6) does not conflict with it.

**Why it is compatible (my reading of SA 10562–10578).** The sentence closes the paragraph on
system (II), the fixed point for (T, λ). −𝖺 is a member of the operator of that system. The
fixed-point map is organised around that untagged diagonal. On a deleted cube it is the only
member left, and it forces the unknown to vanish there. So the outline must keep it untagged.
In the account and in m3 the corresponding object is the layer's equation (29) = (S5). It keeps its
untagged a inside k in V'_s, behind the tagged G̃^J(s) (layer-pkg (1.5); GW 846–850). m3 does not
change that equation (lines 358–362, 443–448, 767–777). The bare mass −Q^*aℓ^{-1} of m_H is
different. It is a coefficient of the current output and is never inverted. The locality clause at
CA-I 72720–72728 requires its kernel to vanish unless both arguments lie in one component of Y(σ).
An untagged block-local diagonal fails this at site (T) (prior/m3.md §4). So the current
coefficient must be tagged, and the system member must not be. These are two roles of one symbol.
The account's expansion needs only a function that is C^1 (here holomorphic) on the polydisc, with
the account's value at one (CA-I 72541–72545, 72945–72952). Hence (6) is a legitimate new
definition. It is not a contradiction of the outline.

**R1 (§3, replace line 465 "SA 10578 leaves `-a` globally carried. They do not give (6) or (17).").**
Replace by:

> SA 10578 keeps the diagonal member `-a` of system (II) untagged ("carried by no proper set") and
> builds that fixed point around it. That member is part of an operator which the fixed point
> inverts. This note does not change it: equation (29), its `V'_s` and every inverted operator keep
> their prescribed members and tags. The bare mass `-Q^*a ell^{-1}` in `m_H` is a coefficient of the
> current output. It is never inverted. The locality clause at I 72720–72728 requires its kernel to
> vanish off `Y(sigma)`, and an untagged copy fails this at site (T) (`prior/m3.md`, §4). So (6)
> tags it. The account's expansion uses only holomorphy on the polydisc and the value at one
> (I 72541–72545, 72945–72952). The outline gives neither (6) nor (17).

**R2 (part of §3/§8).** Add to the list of §3, after the PI item: "**Geometry:** the decoupling
partition `pi` covers the ambient read domain, boundary reads included (§1.1, line 106). This is
part of the furnished GW geometry; it is not proved here." Also replace line 3 "**Research text by
Codex; not checked.**" by "**Research text by Codex; checked line by line by Claude in
`gates/m3-check.md` (R1–R2).**" when R1–R2 are applied.

## 4. Proof of the coefficient theorem (lines 469–761)

### 4.1 The physical absolute algebra (475–609) — ADVANCE

- k_w(y,z): cell-to-cell majorant with source measure and smooth cell partition; no sharp cut of a
  first-order field. This is GW (T3) form. Correct.
- (21)–(22): strong-reserve weight e^{λd}e^{2μt} with λ ≤ μ/4 (GW1). At a junction
  d(y,z) ≤ d(y,x) + d(x,z) and t_{uv} ≤ t_u + t_v + 17c_ι, so e^{2μ·17c_ι} = e^{34μc_ι}. (22)
  follows; summing in z gives the product of row bounds. No cancellation. Correct.
- Scale table (518–529). Checked each row against (1) and the scale of each operator:
  ℓ^{-1}: B_0 → B_1; q_J: B_1 → B_3 (a = ℓ^{-2} scale); Q^*: B_3 → F_3; H: B_0 → E_1;
  j_J: E_1 → S_4 (one m^{-1} field times one m^{-3} current); G'^T: S_4 → S_2 with derivative
  output; P^T: S_2 → S_2; D_0: S_2 (with derivative) → F_3; Δ': E_1 → F_3; D_0^T: E_1 → S_2.
  The chains close: P_1 word E_1 → S_2 → S_2 → F_3; q branch B_0 → B_1 → B_3 → F_3; j branches
  B_0 → E_1 → S_4 → S_2 → F_3; curvature B_0 → E_1 → F_3; bare mass (9). Correct.
- 531–536: D_0 rows are full first-difference readouts, not a derivative bound on a bounded scalar.
  D_0^Tu is bounded by m²|∇_Wu| and the value part. Correct.
- (23): with ηD_0λ(b) = Ad(W_b)λ(b_+) − λ(b_-) and h scalar,
  D_0(h²v)(b) = h(b_+)²(D_0v)(b) + η^{-1}(h(b_+)² − h(b_-)²)v(b_-). Exact. The difference is
  O(m^{-1}) with bounded overlap, so both terms have power −3 from power −2. Correct.
- (24): kernel density of q_J of order m_c^{-2}m_{c'}^{-4}; the ratio m_c/m_{c'} is the one GW pays
  in B_1 → B_3. No hidden η^{-1}. Correct.
- 586–592: bare-mass words in (21): local distance ≤ c_av, tree length ≤ 17D_X (length-zero PI
  tree, GW 578). Factor e^{λc_av + 34μD_X}, independent of κ_1. Correct.
- (25): sum of absolute branch majorants. Neumann ratios ≤ 1/4 on |J| ≤ 2j_* from GW/GW1. The two
  signed j branches are bounded separately. Correct.

### 4.2 Tags, tails and the account's constants (611–669) — ADVANCE

- (26) is GW's cube count (GW 571–573) on the tree of the full branched word, including identity
  and averaging carriers (GW 574–596). With M_dec ≥ 64κ_1/μ: κ_1 n(F_w) ≤ 16κ_1 + μt_w. Deleting
  switch variables only lowers the count; this is CA-I 72447–72452 (m ≤ m^π). Correct.
- (27): (21) gives e^{2μt}; the tag uses e^{μt}; e^{μt} is left. Correct. δ ≤ λ gives (7).
- 641–646: one union tag, so e^{16κ_1}, as the primitives at CA-I 15322–15324 (B_0e^{16κ_1});
  the layer's product-tagged lift keeps e^{32κ_1} (GW1 (5)), a composite bound
  B_0e^{c_Kκ_1} as at CA-I 15324–15325. The two assignments are not equated. Correct.
- 648–656: tails. Truncate degrees, then word lengths; (22) bounds a product tail by factor tails.
  This justifies regrouping at one. Correct.
- 658–669: each finite word is holomorphic; κ_1^+ = κ_1 + 1 gives a strictly larger polydisc; locally
  uniform limits are holomorphic. Correct. The analytic room is real, not inferred from a boundary.

### 4.3 Exact component restriction (671–707) — ADVANCE

- A word meeting a deleted cube has a zero monomial. A surviving word has its connected complete
  footprint in Y(s), so both kernel arguments, all internal legs, averaging carriers, stencils and
  cutoff reads lie in one wall component. This is a kernel statement, as CA-I 72720–72728 and
  72831–72838 require ("keep both legs in C", "reads the configuration there only"). Correct.
- Identical restriction: the component construction is defined by the same labelled words with
  complete footprints in the component, not by a new partition. PI §9 gives equal values; tags are
  equal because their cube sets are equal. Correct.
- (28): at site (T) with K = ∅, every word has a nonempty footprint, so P_1(0) = m_H(0) = 0.
  Correct. 705–707 keeps never-cut cubes and hubs in Y for exempted families. Correct.

### 4.4 Intertwiners and the total at one (709–761) — ADVANCE

- Gauge: local operators intertwine; inverses by multiplying the identity by two inverses; scalar
  cutoffs and scale factors commute; bilinear trace transposes intertwine with contragredient
  actions; (14) by covariance of a commutator; scalar tags preserve the identity. Correct.
- Reality: t_F(s̄) = conj t_F(s); no positivity at complex switches claimed. Correct.
- Transport: grids, tiles, bumps, frames and switch labels are carried with the data; the cube set
  of F_w is carried bijectively. 740–748 states that no covering-quotient identity is proved and
  none is needed by the census. This is an honest scope limit; SA 10552–10560 (mechanism (i)) puts the
  all-tori assignment in the construction of the word families, which is the EQ/PI input here.
- 750–759: at one all tags are 1; sums give D_0PD_0^T = D_U P D_U^* (CA-I 14727) and 𝒦_1. P = I − R
  is used only here, at one. Correct.

## 5. The current of the actual layer (lines 763–918)

### 5.1 The assignment is made after solving the prescribed equation (765–801) — ADVANCE

- (29) expands (S5): z = −Tj + ΓH_0b − GV'(z + H_0b), A' = z + H_0b with T = I + Γ, Γ = GΘ_J.
  So A' = −j + H_0b + GΘ_J(−j + H_0b) − GV'_s(A'). At j = 0 this is K10's G̃ form, CA-I
  15310–15313. Correct.
- (30) is the link map of CA-I 72716–72718, (e^{iη𝒴}K, J_K + 𝒥[𝒴]), with 𝒥 = J^♯_s[1]
  defined by (17)–(18). The field-cut, datum-affine and outside-multiple variants are the three
  conventions of the census. Correct.
- 790–801 state the definition change plainly: (30) replaces the off-one current coordinate only
  where the later reduced package is realised; no claim that K10's old formula at s ≠ 1 gives (18).
  This is what prior/m3.md §5.3 (fourth bullet) demands. Correct.

### 5.2 Bounds, locality and source-free components (803–877) — ADVANCE

- Holomorphy of (18)–(19) from the furnished solution and §4.2; intermediate-image admission kept
  as an input (807–809). Correct.
- (31)–(32): the four linear terms cost 1 + 1 + 18d + 1 = 3 + 18d; the remainder difference 9K_J;
  N_y(δA') ≤ N_y^Δ(δA') in the K_W term. This is layer-pkg (5.3) exactly, and the four entries are
  those of CA-I 111403–111406. Correct. The last two entries from (7) with C_Pe^{16κ_1}K_A and
  C_Me^{16κ_1}K_X. Correct.
- (33): c_ζ = 2(2+4ϑ)(d−1) = 2c_d with c_d of layer-pkg (5.6); fifth entry as at CA-I 111536.
  The commutator uses the unchanged H(s). Correct. χ stays outside m_H; no commutator of m_H with χ
  is used. Correct.
- Source-free component (860–870). On a zero-wall component C: the layer, its full stencils and the
  base depend only on C (layer input, CA-I 72827–72829, 72841–72842); P_1(s), m_H(s) keep both legs
  in C (§4.3). If b↾C = 0 the fields and their stencils vanish on C (layer clause (a) and locality),
  so each linear term is zero and F(W,0) = 0. The gauge map gives 1. The triple is (0,0,1). This is
  the argument of CA-I 72845–72862, now with operators that satisfy its locality clause. Correct.

**Zero-switch test at site (T)** (872–877). K = ∅, s ≡ 0, j = 0. (29) gives A' = X = h = 0 on the
small branch. (28) gives P_1(0) = m_H(0) = 0. So J^♯_0[1] = 0, and the kernels vanish for the empty
retained region, as the locality clause requires. The old value −Q^*aℓ^{-1}b belongs to K10's
continuation (M2), not to (30). The test passes. It is the decisive difference from (M1): there
m_c(0) = −Q^Taℓ^{-1} ≠ 0 (layer-part-ref.md 232–237).

### 5.3 Agreement at one (879–918) — ADVANCE

- At j = 0, s = 1, (29) is the chart equation; small-branch uniqueness (layer input) identifies
  A', X, h with A_G, X_G, 𝓗^J(B).
- (34): Δ_W + K_W − P_1(1) = D_1^TD_1 + D_0D_0^T − D_0PD_0^T = D_1^TD_1 + D_0RD_0^T
  = Δ_a − Q^*aQ − Δ', with Δ_a = 𝒟(W) + D_0RD_0^T + Q^TaQ and 𝒟(W) = D_1^TD_1 + Δ'
  (layer-pkg (1.4); layer-part-ref.md fact 2). Correct.
- m_H(1) = 𝒦_1 by (20) and CA-I 14447. So (18) at one is the right side of
  (4.5:eq-response-chart-2), CA-I 14444–14448: 𝔍(B) = (Δ_a − Q^*aQ − Δ')A_G − 𝒦_1X_G + F(U,𝓗^J).
  The account proves 𝔍(B) equals its definitional current at CA-I 14455–14493 at every pair in 𝔖,
  using the P_0G_0 form, valid at s ≡ 1. So (18) at one is the account's chart current. Correct.
- (35): on K6's domain, RD^*_{U_0}A_G = 0 (CA-I 15689, 15799–15801) and 𝒦_1X = D^*D(HX)
  (CA-I 15802–15810, which needs RD^*H = 0, QH = ℓ^{-1}, ΛH = 0). Then
  J^♯_1[1] = D_1^TD_1A' − D_1^TD_1HX + F = D_1^TD_1h + F(W,h), and CMP 109 (3.11), quoted at
  CA-I 15831–15846, gives J(e^{iηh}W) − J(W). This is K6 (b). The affine datum family is K6 (c),
  CA-I 15847–15859. Correct.
- 913–918: no continuation in the switches; no physical claim at s ≠ 1. Correct.

## 6. Matching the consumers (lines 920–1058)

### 6.1 Cut tails and amplitudes (922–976) — ADVANCE

- (37): for z ∈ S, e^{δ_P d(y,S)} ≤ e^{δ_P d(y,z)} and p(z) ≤ p(y)e^{δ_w d(y,z)}; the sum is then
  bounded by the (27) majorant at rate δ_w + δ_P ≤ λ. Correct.
- 953–957: with the weight p_s(y) = a_s e^{−δ_P d^∧(y,F)}, the ratio rate of p_s is δ_P, so δ_w = δ_P
  there and the condition is 2δ_P ≤ λ. Step 5 of §7 (each rate ≤ λ/4) meets it. Observation only.
  The product of the two distance factors is kept. Correct.
- 958–961: the η_p f(y) U_L form at CA-I 112621–112624 needs its own metric comparison, reader
  location and amplitude admission; m3 keeps these as premises. Correct, and it does not advertise
  (7) as that estimate (brief, prior 307–312).
- (38): on a stencil off the bump, χ = t locally, so all local terms and χm_H(s)X are independent of
  τ, the commutator vanishes, and the only τ-dependence is −τP_1(s)(χ̂A'). Exact by linearity.
  This is the "exactly one member non-local in χ" of CA-II 20794–20828. Correct.

### 6.2 Readers, brackets and differentiation (978–1020) — ADVANCE

- Brackets use (18) or (19) at their own base, switches and datum. Correct.
- Component independence and (0,0,1) give zero switch derivatives on unread or source-free
  components, as an identity on the switch subspace. This is the argument of CA-I 72950–72969.
  Correct.
- Cauchy bound with r = e^{κ_1} − 1 ≥ e^{κ_1−1}: identical to CA-I 72971–72976. Correct.
- Own level: CA-II 39320–39332 is (Δ_𝕌 − P_1^ℓ(σ) + 𝖪)(A'_ℓ + τδA'_ℓ) − m_H^ℓ(σ)(X_ℓ + τδX_ℓ)
  + F(𝕌, ℍ_ℓ + τδℍ_ℓ); fixed bounded operators let the difference quotients pass, as CA-II
  39634–39637 says. The entries at 39641–39647 then follow from (7) and the layer bounds; the
  constant 4B_♯² there is a layer constant that absorbs C_{P}e^{16κ_1}, C_Me^{16κ_1} (allowed to
  depend on κ_1, step 7 of §7). Correct.

### 6.3 Use-by-use record (1022–1058) — ADVANCE

I compared the table with the census prior/m3.md 103–139 row by row. Every row is present. I read
the primary text for these rows:

| Consumer | What it consumes | Matched by m3 |
|---|---|---|
| CA-I 72373–72438 (exempted-set lemma) | K(σ) by (4.21:eq-exempted-set-1) for operators with a walk expansion; the count m(ω) | (17) is of that form with dom w = F_w; (26) and m ≤ m^π. Yes. |
| CA-I 72714–72728 | second slot = rider; both legs in one component; reads there only | (30), §4.3. Yes. |
| CA-I 72828–72862 | P_1(s)A'↾C from A'↾C, m_H(s)X↾C from X↾C; zero on source-free C | §4.3, §5.2. Yes. |
| CA-I 72918–72980 | holomorphy on |s| ≤ e^{κ_1}, locality, (0,0,1), Cauchy | §4.2, §6.2. Yes. |
| CA-I 94978–94996 | reduced form at σ ≡ 1, two operator entries | (20), (34). Yes. |
| CA-I 111391–111410 | (18) at one fixed kernel; four entries | (18), (31)–(32). Yes. |
| CA-I 111530–111550 | (19), five entries | (19), (33). Yes. |
| CA-I 112608–112626 | cut P_1 tail in product form | premise kept; (36)–(37) transfer only. Yes. |
| CA-II 39314–39336, 39634–39650 | own-level affine family, τ-derivatives | §6.2. Yes. |

The other rows (112072–112104, 112181–112194, 112708–112738, 115389–115407, II 610–628,
II 20794–20828, 21125–21144, 21950–22080, 23160–23169, 23993–24005, U27) consume only linearity,
locality, the χ-outside position of m_H, (38), and the profile premise. The digest's description of
them is matched by the cited sections of m3. I did not reread all of them in the primary text;
their required properties are those listed in the digest, and each is supplied above.

No consumer needs equality with K10's off-one current. Every reduced consumer reads the operators
P_1(σ), m_H(σ) through (18)/(19) and their stated properties. 1049–1058 states the boundary
plainly: if equality with K10 off one is imposed, the zero test refutes it, and no choice of the two
linear coefficients repairs it (all linear riders vanish at A' = X = h = 0). Correct.

The older chart rows (CA-I 19637–19685, 29381–29412) keep their native K10 functions. m3 does not
claim equality with (30) there. Correct boundary.

## 7. Constant order (lines 1060–1105) — ADVANCE

| Step | Fixed | Depends on |
|---|---|---|
| 1 | group, odd L ≥ 3, Hölder ceiling, exponent gap, spaces | — |
| 2 | PI/GW flat constants, M_t, r̂, D_X, θ_Z, μ, floors | 1 |
| 3 | C_Q, n_av, c_av, identity constants, c_ι, e^{34μc_ι}, GW1 reserve constants | 1–2 |
| 4 | j_* (Neumann ratios ≤ 1/4 on |J| ≤ 2j_*), C_A^*, C_q^*, C_Λ, C_j, C_H^*, C_Δ', C_P, C_M | 1–3 |
| 5 | λ ≤ μ/4, δ_w, δ_P ≤ λ/4, GW summation floors | 1–4 |
| 6 | κ_1, κ_1^+ = κ_1 + 1, M_dec ≥ max{4r̂ + 8L, c_ι, 64κ_1^+/μ} | 1–5 |
| 7 | layer radii, RJ smallness, cut amplitudes, reader images | 1–6 (may depend on κ_1) |

Each constant depends only on earlier ones. The word majorants do not read the decoupling grid, so
C_P, C_M precede κ_1 and M_dec. j_* precedes κ_1 because the series are expanded, not re-summed at
s (CA-I 15283–15285: "no condition couples a_γ to κ_1"). Non-circular.

Consistency with CA-I 15266–15322: switches |s(Δ)| ≤ e^{κ_1} (15317); primitives e^{16κ_1}
(15322–15323), here the two new primitives; composites e^{c_Kκ_1} (15324), here the layer's
retained objects; δ_1M ≥ κ_1 (15317) is replaced by the stronger explicit floor 64κ_1^+/μ on
M_dec with the tree reserve. Consistent with SA 10582 (κ̄ is chosen before ℓ_𝖯; ℓ_𝖯 comes
after it) and with SA 10558 (e^{16κ̄} is left over).

## 8. What this proves and what it does not cover (lines 1107–1139) — REVISE (wording)

- The scope list is honest: no admission of all classes, no graph/FM/FD, no reader room, no product
  profile without its inputs, no repair of K10's off-one current or of CA-I 15450–15451, no
  physical meaning off one. Correct.
- The account lines named at 1124–1130 exist with the stated content (I checked 72720–72728,
  72831–72851, 111394–111399, 111538–111545, II 39320–39332, 14439–14493, 15676–15860).
- R2 (above): add the partition-covering hypothesis to §3, and update the stale header line 3.

## The six answers

1. **First hard step.** Yes. Each word A_τ = −Q^*a h_{τ,B}²ℓ^{-1} carries its whole row carrier E_c,
   the output bond and the input row inside the PI footprint F_τ (PI 753–754, margin
   (2L+1)M_t − 2L ≥ c_av). A surviving word has no zero factor, so F_τ ⊂ Y(s), and F_τ has
   connected interior, so all legs and coefficient reads lie in one component. The family sums to
   −Q^*aℓ^{-1} exactly at one by Σ_τ h_τ² = 1 (10). The majorant (9) is correct with
   C_A = C_Q n_av L^3 e^{δc_av} and the factor e^{16κ_1}; its (21) version adds
   e^{λc_av + 34μD_X}. SA 10578: the outline keeps −𝖺 untagged as a member of system (II), an
   operator the fixed point inverts. m3 leaves the corresponding layer equation (29) and its V'_s
   unchanged, and tags only the current coefficient, which is never inverted and must satisfy the
   locality clause. This is legitimate: m_H(σ) is undefined off one in the account, and the
   account's expansion needs only holomorphy, locality and the value at one (CA-I 72541–72545,
   72945–72952). m3 states the SA fact but not this reason (R1).
2. **Zero-switch test.** Yes. At site (T), K = ∅, s ≡ 0, j = 0: (28) gives P_1(0) = m_H(0) = 0,
   and (29) gives A' = X = h = 0, so J^♯_0[1] = 0 and the kernels vanish for the empty region, as
   CA-I 72720–72728 requires.
3. **Forbidden moves.** None found. No switched inverse identity (the layer keeps the G̃ form;
   QH(s) = ℓ^{-1} is never used). R = I − P is used only to generate words at one (2.1) and to sum
   at one (4.4); after tagging each completed word has one tag. No continuation from s = 1
   (913–915). No post hoc indicator: the partition and the cube sets are fixed by geometry before
   tagging; the indicator in (33) is the consumer's own fifth entry, a bound.
4. **Agreement at one.** Yes. (34) and m_H(1) = 𝒦_1 make (18) the reduced form of CA-I
   14444–14448, which the account's proof at 14455–14493 identifies with the definitional chart
   current. On K6's domain, RD^*A_G = 0 and 𝒦_1X = D^*D(HX) give (35) = CMP 109 (3.11), i.e.
   K6 (b), and K6 (c) for the affine family.
5. **Definition change and consumers.** Stated plainly (24–28, 790–801, 1049–1058). Each consumer
   I read (CA-I 72373–72438, 72714–72728, 72828–72862, 72918–72980, 94978–94996, 111391–111410,
   111530–111550, 112608–112626, CA-II 39314–39336, 39634–39650) reads only the properties m3
   supplies. None needs equality with K10's off-one current.
6. **Constant order.** Non-circular (table in §7). Tag constants agree with CA-I 15317–15324:
   |s| ≤ e^{κ_1}, e^{16κ_1} for the two new primitives, e^{c_Kκ_1} for the retained layer
   composites, and the floor 64κ_1^+/μ in place of δ_1M ≥ κ_1.

First failing step: none. (R1–R2 are wording repairs; no mathematical step fails.)

## Overall verdict

**ADVANCE, with wording repairs R1–R2. No BLOCK.** Under the named imports (PI, GW, GW1, averaging,
layer, RJ/readers, profile, geometry), m3.md supplies premise M of the frozen layer part as the
brief prior/m3.md §5.1 specifies: a reduced tagged assignment with holomorphy, (7) with e^{16κ_1},
exact component locality including the bare mass, agreement at one through CA-I 14439–14493 and K6,
and consumer matching. It is a new definition off one, stated as such; it does not repair K10's
off-one current.

1. R1 (§3, line 465): explain why tagging the current's bare mass is compatible with SA 10578's
   untagged system member (text in §3 above).
2. R2 (§3 list and line 3): name the partition-covering hypothesis of line 106 as an input; update
   the "not checked" header.

Observation, no repair: in §6.1 the source-location weight has rate δ_P, so (37) there needs
2δ_P ≤ λ; step 5 of §7 already gives it.

Checked line by line by Claude (Opus 5.5).
