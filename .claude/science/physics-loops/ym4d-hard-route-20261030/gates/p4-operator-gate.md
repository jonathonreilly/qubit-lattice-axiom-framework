# P4 operator port: one line-by-line check (A4, A3, A9)

Object: `library/port/p4-operator.md` (901 lines), checked against
`scratchpad/sa/ca_I.tex` (identical to `/tmp/sa_ca_I.tex` by `cmp`; 166711 lines).
Checked line by line by Claude (fresh session). One reading; not a hostile reading.

## A4 — 4.5:thm-operator-bounds (port 17–287; CA-I 19578–19867)

### Statement
- Port 24–189 is byte-identical to CA-I 19578–19743 (`diff`, empty). Faithful.

### Inputs table (port 192–212)
- Label lines check: 13144, 13177, 13200, 13681, 14712, 14803, 15669, 16993, 17519, 18478,
  19267, 19376 all match the cited ranges (±2 lines for the label line). Standings agree with
  the source headings (uniform-increment lemma is "Stated; proof incomplete at (∗)", CA-I 16019;
  the port keeps it as an assumed input via ui.md, not checked here).

### Proof, step by step
- (O), port 218: matches CA-I 19745–19752. Holds.
- (F1), port 220–224: matches 19754–19766 (|J|_(-3) ≤ L^{-3}α0 < a_γ; K3 at α2/3). Holds.
- A4-F1, port 226–237. Affine part holds (r = α2/(3q), each first-order term ≤ α2/3, total
  2α2/3). **Gap in the filled justification of the Taylor bound (port 232).** The port says
  "The chart's second-derivative bound, in the norms and admitted segment of K4, gives the
  source's bound C_F'α2²." No such bound is printed. K4 says at CA-I 14838–14839 "No second
  derivative of a response is taken." The map in question is the curvature remainder
  F(U,A) of `4.5:lem-curvature-remainder` (CA-I 14083–14096); it prints only
  |F| ≤ C_F(a0+a1+N(A))N(A) and |∂_A F[f]| ≤ C_F'(a0+a1+N(A))N(f). The source's own phrase
  "C_F' is the second-derivative constant of F" (19773–19774) is the same looseness. The
  first-derivative bound alone gives a remainder of first order with factor (a0+a1), not
  C_F'α2². Repair (route unchanged): the same term-by-term argument as in that lemma's proof
  (CA-I 14128–14130: every summand of order ≥ 2 in (A,∇A) has its second derivative bounded on
  N(A) ≤ 1; summands linear in A drop out) gives |∂²_A F[f,f]|_(-3) ≤ C_F'' N(f)²; enlarge C_F'
  to max{C_F', C_F''} in the constant order (it is listed there, CA-I 19411, before the
  ceiling 19480), and the printed ceiling α2 ≤ 1/(4C_F') then gives the port's 11/12 line.
  This is the first failing step. It is a constant-naming repair, not a route change.
- A4-C2, port 239: correct. r q = α2/3 has no solution at q = 0; reading the disc as
  |t|q ≤ α2/3 is the natural reading and all variations vanish on X there. Holds.
- (F1) continued, port 241–243: the source (19781–19786) says the lemma gives "(i), (ii), the
  first member of (1.14), and condition (iv) in the uniform form". The port says "(i), (ii),
  (iii)'s curvature half and both halves of (iv)". This is a relabelling the port does not
  justify from the source (I cannot check CMP 109 (1.14) here). Use the source words. Minor.
- A4-F2, port 245: holds. C_IV ≥ 4C_14 and C_14 = 9(2d+2) (CA-I 16032, 16041);
  α2 ≤ α0/C_IV (16051); L ≥ 27 is in the constant order (19435). So
  L^{-3}α0 + α2 < α0. (The consumer at CA-I 29430 imports C_IV ≥ 4(4d+2); this is weaker
  than 4C_14 = 36(2d+2), so it is consistent.)
- Activity bound and analyticity, port 245–247: matches 19787–19794. Holds.
- (F2), A4-F3, port 249–260: matches 19796–19809 (K4, K8, P1 ∈ K_{-2}). c_* fixed in K10
  (CA-I 14511, 14949). The inversion r ≥ α2 e^{c δ0 D}/(3CL^jη|ζH|) is right. Holds.
- (F3), port 262–263: matches 19811–19813 (K6(c) with CMP 109 (1.9)). Holds.
- (F4), port 265: matches 19815–19816 with the scope printed in (F4). Holds.
- (F5), port 267: matches 19819–19824. K10 (`4.5:prf-chart-walk-localisation`, CA-I
  15265–15340) item 2 gives K1, K3–K5, K8 at s with B0 → B0 e^{c_K κ1}; it does not list K6.
  CA-I 15338–15339: "The identity (chart-structure-a) and the exactness statements
  (diagonal-exactness-a) are asserted at s≡1 only." CA-I 15449–15452 gives the reason: the
  explicit formulas enter only those identities. The port's cite "15338–15340" is right.
  One point the port leaves implicit: C_F' is a constant of the curvature remainder F, a local
  function of the field that does not depend on s. So the ceiling α2 ≤ 1/(4C_F') needs no
  e^{c_K κ1} factor at s; only the K3 base bound (via the ε1 ceiling, CA-I 19989) does. With
  that, (F1), (F2), (F4) at s hold as the port says.
- A4-C3, port 269: **correct.** As printed, (F5) "The same statements hold" includes (F3) at
  every s. The source proof (19819–19824) reaches (F3) only through K6(c), which K10 withholds
  at s ≠ 1. So the source statement overstates what its proof gives.
  Consumers of (F5) checked: CA-I 29409–29412 (names (F5) "the versions at s of the far
  clauses"), 29469–29506 (the constant C_s: (F5) is used only for bounds linear in |B'|),
  29354 ("holds both at s≡1 and at s", the shift-field bounds), the cluster-expansion read at
  30575–30600 (bounds (1.24), (1.29), (1.36) of CMP 116 only), and the not-asserted remark
  20132–20149 (item 4: pieces at s are not claimed to coincide with Balaban's; "their sum at
  s≡1 and their values on the diagonal" coincide). No consumer reads (F3) at s ≠ 1. The
  cluster expansion needs only analyticity and bounds at s, separation at s = 0 (K10 item 3),
  and the value at s ≡ 1 (K10 item 4 plus (F3) at s ≡ 1). So **A4-C3 exposes no gap
  downstream**; it fixes an overstatement in their (F5). One small loose end in their text:
  the phrase "their values on the diagonal" in item 4 of `4.5:rem-not-asserted` (20148–20149)
  is ambiguous; read at s ≢ 1 it would be the same unsupported claim. It is a remark, not a
  premise, so nothing rests on it. Suggest the port note this phrase next to A4-C3.
- A4-F4, (F6), port 271: matches 19826–19836; the tower caveat is the source's own
  (19830–19831). Holds, with the A4-C3 scope.
- (N-a), A4-F5, port 273–282: matches 19838–19856. Orbit class `4.5:eq-admissible-pairs-a`
  (CA-I 12981–12986) has 𝔎 = 4 and radius c9/𝔎 = c9/4; 2|B'| < c9/4 fits. K5 item 3
  (CA-I 15018–15019) gives N^{U^u}_β(R(u)f) ≤ ‖Ad_u‖N^U_β(f), so the output gauge costs ≤ 2.
  These give N_β ≤ 2·C9^K·2|B'| = 4C9^K|B'|. The source's further factor 4 is slack (any
  factor ≥ 1 keeps the bound true). The port calls it "the allowed chart norm allowance four";
  better to say it is slack. The printed bound 16C9^K|B'| holds. Wording only.
- (N-b), port 284: matches 19858–19863. Check of the port's arithmetic: b' = B_b^f M α0'''
  (CA-I 18526) with α0''' = (1+2β)α0 (17068) gives b' = 𝔟 M α0 with 𝔟 = B_b^f(1+2β). Right.
  The BCH ceiling α2 + max{b,b'} ≤ 1/(4C_BCH) is at CA-I 19981–19983. Holds.
- (N′), port 286: matches 19865–19866. Holds.
- A4-C1, port 214: **correct.** CA-I 19386–19388 and 19459–19472 cite (cf1), (cf4), (cf5) of
  `4.5:eq-fine-axial-frame-a`; the display (18517–18529) has only (cf1), (cf2), (cf3).
  (cf4) = (cf3) (has b'/L ≤ α1^(98), 18525); (cf5) = (cf2) (the α0'''+C14α1''' bounds,
  18521–18524). The same stale labels recur after the A4 range at CA-I 19967–19976, 20040,
  20058, 20082 (proof of the constant order). There the printed (cf1) reads
  14d(M/L)(α1'''+c12 L M B^109 α0''') ≤ 1/10 and the display's (cf1) reads 7d𝖬 c̄ ≤ 1/10; I did
  not check that these agree. The port's "use the whole actual fine-frame display" covers it.
  Suggest the port extend A4-C1's line list to 19967–20082.

### A4 verdict
Faithful with repairs. Repairs: (1) A4-F1 Taylor bound needs a named second-derivative
constant for the curvature remainder F (first failing step, constant-level repair);
(2) (F1) wording of what the increment lemma supplies should follow the source; (3) A4-F5
factor-4 wording. A4-C1, A4-C2, A4-C3 are right.

## A3 — 4.4:cor-localised-independence (port 289–423; CA-I 9615–9670, proof 9680–9791)

### Statement
- Port 296–351 is byte-identical to CA-I 9615–9670 (`diff`, empty). Faithful.

### Inputs (port 354–373)
- Label lines check: 4427, 5218, 5580, 6219, 6959, 8110, 8912, 9356, 9476. Right.
- A2 = `4.4:prop-local-real-base` has the heading "Proof outstanding" (CA-I 8110). The port keeps
  it as a named input. Right. Note on their text: A3 is unmarked ("proved in full") but its
  proof (9775–9777) uses A2 through "that proposition together with a standing hypothesis".
  It is not one of A3's hypotheses (i)–(v). So A3's unmarked status leans on an outstanding
  proposition. The port handles this correctly.
- Small reference slip in their text, not flagged by the port: the statement cites
  "the local class P_{ρ,X} (Definition 4.4:def-local-data-classes)" (9623, 9659, 9666). That
  definition (4427–4503) defines P'_D. The polydiscs P_ρ, P_{ρ,D} are in
  `4.4:def-regular-backgrounds` (4608–4697). The port's table cites both ranges, so nothing
  is lost. The class P_{1+β,X} and "the domain inclusion for this class" appear only in A3
  (9665, 9774); the port keeps the inclusion as a named hypothesis (table row "Hereditary
  domain inclusion"). Right.

### Proof, step by step
- Step 1, port 377: matches 9681–9686. Holds.
- A3-F1, port 379–385: this is the proof of `4.4:lem-vertex-formula` (CA-I 5236–5262)
  repeated. It holds (f is C¹ in each variable; E¹−E⁰ commute; summing gives E¹). W' ⊂ W
  matches 9692–9694. Holds.
- Port 387: matches 9696–9702. Interior sufficiency (9476–9497) states "no point of S0
  extending u is used". Holds. One domain detail neither text shows: that lemma needs
  u ∈ P'_W for the constituents in L1 and u ∈ P_{ρ,W} for those in L2 (9488–9490). For the
  second and third parts (L1 operators inside V_k) this asks that the hereditary-class
  representatives lie in P'_X. Neither source nor port says so. Suggest the port add it to
  the named "hereditary domain inclusion" hypothesis. Minor.
- Step 2 and A3-F2, port 389–405: the scalar identity and the integral
  log(R+λ0) − log λ0 − log(R+a) + log a are right; the limit gives
  `4.4:eq-localised-independence-1`. The complex extension (principal branch, Re a > 0,
  identity theorem) is right. The Jordan-block argument is right. Accretivity is warranted:
  `4.4:lem-form-coercivity` gives Re⟨v,Av⟩ ≥ γ_*|v|² (CA-I 5950; used for the compression at 6349)
  keeps it. The port says "accretive" without citing this; add the cite. The trace formula
  −½ log det A^Y = −½ dim·log λ0 − ½∫Tr[(A^Y−λ0)R^Y]/(λ+λ0) is right; the constant
  −½ dim log λ0 does not depend on the configuration (it depends on Y only). Matches
  9705–9730. Holds.
- Port 407–410: matches 9732–9745. Holds.
- A3-F3, port 412–417: `4.4:lem-cell-resolvent` (ii) gives |||R^Y(x)|||_θ ≤ 4S/(x+γ_*/2)
  (CA-I 6265–6267), and (v) gives the same for local families (6294–6296). The splitting
  of ∫ on [0,1] and [1,∞) is right. Holds. Matches 9747–9757.
- A3-F4 and Step 3, port 421–423: matches 9759–9789. Holds, with the domain note above.

### A3 verdict
Faithful. One minor addition suggested (P'_X membership of the representatives, as part of
the named domain-inclusion hypothesis) and one missing cite (coercivity for accretivity).

## A9 — 4.14:thm-operator-theorem (port 426–824; CA-I 46035–46156, proof 47253–48140)

### Statement
- Port 431–553 is byte-identical to CA-I 46035–46156 (`diff`, empty). Faithful.

### Hypotheses (port 557–596)
- P4-H-prepared, port 561–573: right. `4.14:prop-prepared-data-admissible` (CA-I 45557–45600)
  asserts only (A1) for the prepared nest (last sentence, 45594–45596); 45622–45624 say (A2)
  is not among the quoted sentences and (A1), (A2) are assumed in the theorem. The port's
  displays match `4.14:eq-prepared-data-admissible-a` (45569–45578). Note: the theorem
  statement assumes (A1), (A2) directly, so the proposition is an application input, not an
  input of the implication. The form-walk lemma (47255–47258) lists the proposition among
  "the hypotheses of the operator theorem" anyway. Keeping P4-H-prepared is conservative and
  harmless.
- Constants check: γ1, γ±, ε1, m1, δ0, B0, B_J = B_Q at CA-I 45324–45327; μ1 at 47698.
  All match port 688–693 and 761–765.
- P4-H-core: (E), (F), (G), (K) cite "the operator theorem at free current with the hulls
  \widehat\square" (46097, 46107, 46110, 46128). No such statement is printed in CA-I, CA-II,
  CA-III or the sketch (searched). The port keeps its clauses F, G, K and the core lemma as a
  named input. Right.
- **The "unprinted four-condition assembly reference" (P4-H-assembly).** CA-I 47580–47584:
  "The radius a0^⊕ is the largest number satisfying the four smallness conditions displayed
  there; these conditions are the only place where the size of c_𝔤 is constrained", with
  "there" = `4.14:eq-block-size-conditions-d` (45804–45811). That display prints only the
  a1^⊕ minimum and the order of choice. The prose after it (45812–45813) says only "The second
  radius a0^⊕ is the companion radius fixed together with a1^⊕; it is the only place at which
  the constant c_𝔤 enters." I searched all four source files for a0^⊕ (every spelling) and for
  "four smallness": no display defines a0^⊕ by four conditions. What it refers to:
  (1) a0^⊕ is the current-direction radius of U(1); 4.4 (CA-I 5830–5838, 5862–5867) says
  a1^⊕, a0^⊕ are "formed by the recipe of the corollary on representatives" from radii
  (a1^♭, a0^♭). That corollary (also called "the corollary to the operator theorem at free
  current", 4675) is cited by description only and is not printed. (2) In A9, a0^⊕ enters only
  through the vertex constant ν_J = 2c_𝔤 a0^⊕ of the multiplication vertex M_J (47539–47540;
  M_J defined 45424–45425). The stages of the assembly that carry a J-vertex are four: stage 1
  (G_π, series (q1)), stage 2 (branching of Δ^(2)[j0]), stage 3 (G_1, series (q2)), stage 4
  (branching of J[j]). So the four conditions are, on the evidence, the smallness of ν_J
  needed for these four stages to converge in the alphabet's norms. That is an inference; the
  conditions themselves are not printed. (3) The only printed four-member display that names
  both a0^⊕ and c_𝔤 is the 4.4 "halved ceilings" `4.4:eq-radius-ceilings-1` (5846–5851). It
  is not the referent: it bounds the primed radii and a_U given a0^⊕, and there c_𝔤 is the
  Lie-bracket constant (6771, 10468), not "a constant of the assembly". The phrase at 47580
  looks like a stale reference left after the display was shortened (same kind of slip as
  A4-C1). Effect: the existence of a positive a0^⊕ and the convergence of the J-vertex stages
  rest on unprinted conditions. The port's treatment (named hypothesis P4-H-assembly, "do not
  claim that this display proves it", port 590) is right. Suggest the port record findings
  (1)–(2) next to P4-H-assembly, so a reader knows where the conditions would come from.

### Proof, step by step
- Part 1 (i)–(vi), port 600–681: matches 47287–47584 in order (elementary sheets, local
  operators with n_w ≤ 3(2dL+1)^d at 47331, unit-lattice operators, singular word,
  constrained inverse with N_d = 2·5^d, λ♯, w♯ at 47413–47414, five-stage assembly at
  47533–47577 with δ_Q = δ_𝔏/32). Holds as an ordered use of named inputs.
- A9-F1, port 653–659: checked against (t2)(α)–(η), 47428–47500. Schwarz: f analytic on
  |z| < r♯, f(0) = 0, |f| ≤ 2K_T gives |f(1)| ≤ 2K_T/r♯ ≤ m/6 under r♯ ≥ 12K_T/m (47485).
  m − m/12 − m/6 − m/12 = 2m/3; minus IMS m/6 gives m/2 = m0. Right; this fills the source's
  one-line (η).
- (vii), port 683: matches 47602–47622 (four conditions of the coercivity proposition —
  a different "four", fully printed). Holds.
- Part 2, port 687–743: matches `4.14:prf-positivity-inversion` 47686–47892 line by line.
  Box constants 2^d, 36d²/M, M/48d, M/4 (47734–47736); M ≥ 144dρ_Q (47740); IMS ≤ γ0/6
  (47771–47773); tail ≤ γ0/12 (47783–47785); r_reg = a1^⊕/(2a_Q), ceiling gives
  r_reg ≥ 12γ1/γ0 (47797–47821); Schwarz loss 4a_Qγ1/a1^⊕ ≤ γ0/6 (47831–47834); total γ0/2
  (47843–47848). Holds.
- A9-F3, port 703: right. It fills "For the same reason there is a cube Q" (47751–47753):
  points of an M-cube through the 5ℓ-hull are within 5ℓ+1+M < 6M of Ω_t. The port's "Since
  d = 4" is not needed (5ℓ = 5M/(12d) ≤ 5M/12 for every d ≥ 1); harmless.
- A9-F4, port 733–736: right. 2γ1ε1 = γ0/4, so Re Q ≥ γ0/2 − γ0/4 = m1; the source gets the
  same radius from the sector lemma (47851–47860). Kernel argument for invertibility right.
- Inversion output, port 738–743: matches 47876–47881 exactly. Holds.
- Part 3, port 747–822: matches `4.14:prf-block-identities` 47895–48140.
  A9-F5 (cofactor, C^T = C): right. A9-F6 (square completion): I recomputed it with the
  complex-bilinear pairing and AC = 1, C^T = C; right. (B): right with γ− = 1/γ1, γ+ = 2/γ0.
  (C): matches 47986–47991. (E)–(G): match 47993–48017; the factor (1+2x/m1)^{−(n+1)} is
  48015–48017. A9-F7: matches 48019–48040 ("enlarging a list lowers τ"). (H), A9-F8: matches
  48042–48054; the filled collar argument and product rule (needs 2L/M < 1, i.e. M > 2L) are
  right. (I), A9-F9: the order list matches 48066–48075 exactly, including the bare x. Small
  inconsistency in their text, not flagged by the port: display d (45808–45810) orders
  "M1 → M1♯ → (d,L)-constants", but 48068–48075 puts B_el, δ_el, a1^el, ρ0, B_T, δ_T, m^flat,
  r♭ between M1 and M1♯ (needed, since M1♯ > 2Lρ0). The port follows the expanded order.
  Right. (K): matches 48093–48101. Symmetry, A9-F10: matches 48103–48107. Λ_t dependence:
  matches 48109–48114. Schur, A9-F11: matches 48115–48131. All hold.
- Port 824: `4.14:rem-supply-scope` at 49496 onward ("The five points below concern the
  application of the operator theorem"). Right that application needs more.

### A9 verdict
Faithful. No step fails. The four-condition reference is a real gap in their text
(unprinted constant-fixing for a0^⊕), correctly kept as P4-H-assembly.

## Summary

First failing step: A4-F1, port line 232 (the Taylor remainder bound C_F'α2² is attributed
to a "second-derivative bound ... of K4" that is not printed; K4 says no second derivative is
taken, and `4.5:lem-curvature-remainder` prints only a first-derivative bound). Repair: a
second-derivative constant for F from the same term-by-term series argument, and C_F' taken
at least that large in the constant order. Route and printed ceiling unchanged.

Findings, one line each:
1. A4, A3, A9 statements are byte-identical to the source ranges.
2. A4-F1 Taylor bound: misattributed; constant-level repair (above).
3. A4 (F1): "(iii)'s curvature half and both halves of (iv)" should use the source words
   "(i), (ii), the first member of (1.14), and (iv) in uniform form" (19781–19786).
4. A4-F5: the factor 4 in 2·C9^K·2|B'|·4 is slack, not an "allowance"; the bound holds.
5. A4-C1 is right; the same stale (cf4)/(cf5) labels also occur at 19967–20082.
6. A4-C2 is right.
7. A4-C3 is right: their (F5) overstates (F3) at all s; every consumer found (29409–29506,
   29354, 30575–30600, 20132–20149) uses (F5) only for bounds, so no downstream gap. Phrase
   "their values on the diagonal" (20148) is ambiguous; remark only.
8. A3: holds; add the coercivity cite for accretivity (5950) and add P'_X membership of the
   hereditary representatives to the named domain-inclusion hypothesis (interior
   sufficiency needs it for L1 constituents, 9488).
9. A3 in their text leans on A2 ("Proof outstanding") through a standing hypothesis; the port
   keeps A2 named. Right.
10. A9: all filled steps hold. The four-condition reference (47580–47584) points to no
    printed display; a0^⊕ comes from the unprinted "corollary on representatives", and the
    four conditions are, on the evidence, the ν_J = 2c_𝔤a0^⊕ smallness for the four J-vertex
    assembly stages. Kept as P4-H-assembly. Right.
11. A9: the "original-hull" operator theorem cited in (E)–(G), (K) is not printed anywhere;
    kept as P4-H-core. Right.

Verdicts: A4 — faithful with repairs (items 2–4). A3 — faithful (two small additions).
A9 — faithful.

Checked line by line by Claude (fresh session).
