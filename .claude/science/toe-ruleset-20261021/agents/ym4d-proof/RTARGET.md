# RTARGET: pre-stated target for the one-cube R-operation (session 7, 2026-10-27)

Written BEFORE any derivation of the one-cube step (REVIEW_S5_S6 (6).2, binding). Sections 0-3 are the pre-statement
and are not edited after the derivation starts. Section 4 is a pointer to the outcome, added afterwards and marked.

## 0. Does the LF-count wall appear in d = 2? (verified first)

Take the 2D lattice O(N) model, S = (1/g²) Σ_⟨xy⟩ (1 - n_x·n_y) = (1/2g²) Σ |n_x - n_y|², n ∈ S^{N-1}, N ≥ 3.
- Counting. Level-k M-cubes: N_k = (L^kε)^{-2} M^{-2}|T|. With the upper half of a two-sided AF flow
  1/g_k² ≤ 1/g² + β'(K-k) log L and w_k ≥ e^{-a/g_k²}: Σ_k N_k w_k ≥ e^{-a/g²} M^{-2}|T| Σ_{n=0}^K L^{(2-aβ')n}.
  This diverges as K → ∞ whenever aβ' ≤ 2 (geometrically if <, linearly if =). Conversely w_k ≤ e^{-a/g_k²} and the
  lower half with aβ > 2 give convergence. Same proof as LF-count with exponent d = 2. (Arithmetic: checked by hand.)
- Rate [m; standard one-loop, Polyakov 1975]: d(1/g²)/d ln μ = (N-2)/(2π) in this normalisation, so β' ≈ (N-2)/(2π)
  [inference: the lattice rate is assumed one-loop, as in LF-count].
- Cost of the cheapest excluded configuration for a single-bond cut |n_x - n_y| < ε_1: a = ε_1²/2, and a ≤ 2 for any
  cut (antiparallel bond). So aβ' ≤ (N-2)/π, which is ≤ 2 for 3 ≤ N ≤ 8: **for 3 ≤ N ≤ 8 every single-bond
  small-field threshold lies in the divergent window**; for N ≥ 9 every ε_1 ≤ (8π/(N-2))^{1/2} does.
- **[R78-fix] (annotation added in session 9; the pre-statement above is left as written).** The cost line above is
  WRONG (REVIEW_S7_S8 (2)). ε_1²/2 is the cut bond's own term, a *lower* bound on an excluded configuration's action;
  the divergence argument needs an *upper* bound on the cheapest one. Corrected: a ≈ ε_1²/(2R_eff) = ε_1² (linearised,
  R_eff = 1/2 between neighbours of Z²; the reviewer's computation gives cost/ε_1² = 1.0115, 1.0007, 1.0001 on 11²,
  41², 101² boxes); "a ≤ 2 for any cut" is deleted (an antiparallel bond costs ≈ 2 + π²/2 heuristically). The window
  is then every ε_1 ≲ (4π/(N-2))^{1/2} [linearised; inference on the one-loop rate], not "every cut for 3 ≤ N ≤ 8";
  the N ≥ 9 bound reads ≈ (4π/(N-2))^{1/2}. The qualitative verdict (the wall is present in d = 2 for small ε_1)
  stands.
- Instanton sanity check (O(3)): S ≥ 4π|Q|/g² [m, Belavin-Polyakov], so aβ' = 4π·(1/2π) = 2 = d, exactly marginal:
  the count diverges linearly. This matches the known UV log-divergence of the small-instanton gas / lattice
  topological susceptibility of the O(3) model [m, Lüscher NPB 200 (1982); not re-read]. In 4D, aβ' = 11N/3 > 4.
  **[R78-fix] caveat (session 9 annotation).** With the standard lattice action, lattice-scale Q = 1 configurations
  ("dislocations") have action below the continuum 4π [m, Berg-Lüscher 1981; not re-read]. On the lattice aβ' < 2
  strictly, so the divergence there is geometric, not marginal; "exactly marginal" holds for the continuum bound only.
- **Verdict: the same wall is present in d = 2, with the same mechanism (marginal coupling, polynomial cube count
  L^{d(K-k)} against only power-law decay e^{-a/g_k²} = e^{-a/g²}L^{-aβ'(K-k)}).** The 2D chiral models of CMP 109
  p.260 (G-valued sites, S = (1/g²)Σ[1 - Re tr U(db)]) have the same structure (π_2(G) = 0, so no instantons).

Literature correction found while checking: Balaban CMP 198 (1998) 493-534, "The large field renormalization operation
for classical N-vector models", belongs to his LOW-TEMPERATURE N-vector series (CMP 167, 182, 196, 198), which is an
infrared problem in d ≥ 3 [read-abs, Rutgers record + search snippets]; it is NOT a 2D asymptotically free UV
construction. As of 1999 the UV analysis of the full 2D O(N) model had "so far only [been] performed in the
hierarchical case" (Kopper, CMP 202 (1999) 89-126, arXiv:math-ph/9902020, introduction [read-skim]). So the 2D testbed
is itself an open construction, not a solved template.

## 1. The model for one cube, one RG step (2D)

- Fine lattice Z², L odd ≥ 3, block □ = {x : |x_1|, |x_2| ≤ (L-1)/2}; Γ = the 4L exterior nearest neighbours of □.
- Integration variables n_x ∈ S^{N-1}, x ∈ □, uniform measure dσ (total mass 1).
- Frozen background: m_y ∈ S^{N-1} (y ∈ Γ), and a block-spin value Φ ∈ R^N.
- Action, soft block-spin constraint with κ > 0:
  S(n; m, Φ) = (1/g²)[ Σ_⟨xx'⟩⊂□ (1 - n_x·n_x') + Σ_⟨xy⟩, x∈□, y∈Γ (1 - n_x·m_y) + (κ/2)|Φ - L^{-2}Σ_{x∈□} n_x|² ].
- Small-field indicator on interior bonds only: χ(n) = Π_⟨xx'⟩⊂□ 1{|n_x - n_x'| < ε_1}, 0 < ε_1 < 2.
- One-cube large-field weight: ρ(m, Φ) := ∫(1 - χ)e^{-S} dσ / ∫ χ e^{-S} dσ. The cube's contribution to the effective
  action is log(1 + ρ).
- Smooth background family: n : R² → S^{N-1}, C^4, with |∂^α n| ≤ 1 for 1 ≤ |α| ≤ 4;
  m_y(s) := n(sy), Φ(s) := L^{-2}Σ_{x∈□} n(sx), and ρ(s) := ρ(m(s), Φ(s)).
  Here s = L^{j-k} when a level-j cube is seen against a level-k background (s = 1 at its own level, with the
  background's bond differences small).

## 2. Target inequality (R2D)

Counterterms subtracted inside the cube: the vacuum energy ρ_0 (the value at a constant background) and a marginal
coupling shift δβ times the background's local lattice action A_B(m) := Σ_{⟨yy'⟩∈B}(1 - m_y·m_y') over a fixed
D_4- and reflection-symmetric bond set B around □.

**(R2D).** For every a < ε_1²/4 there are C, s_0 > 0 and g_0 > 0, depending on (L, N, κ, ε_1, a) only, such that for all
0 < g ≤ g_0, all backgrounds n as above and all 0 ≤ s ≤ s_0:
  ρ(s) = ρ_0(g) + δβ(g)·A_B(m(s)) + R(s), with
  (T1) 0 ≤ ρ_0(g) ≤ C e^{-a/g²} and |δβ(g)| ≤ C e^{-a/g²}, both independent of the background n;
  (T2) |R(s)| ≤ C e^{-a/g²} s⁴.
The same with ρ replaced by log(1 + ρ).

Why this is the needed form (consequence to be checked, not assumed):
- Field-dependent remainder: a level-j cube against a level-k background has s = L^{-(k-j)}; there are L^{2(k-j)}
  level-j cubes per level-k cell; so Σ_{j≤k} L^{2(k-j)}·C w_j L^{-4(k-j)} ≤ C' sup_j w_j, uniformly in k and K. This
  is the 2D form of "(L^jη)^{d+α} w_j" with α = 2, against LF-count's L^{d(K-k)}.
- δβ: Σ_j |δβ(g_j)| ≤ C e^{-a/g²} Σ_n L^{-aβn} < ∞ along the flow, and it is ≪ g_j⁴, so it does not disturb the AF
  flow.
- ρ_0: it depends on g_j and the fixed parameters only, not on the field. Σ over all cubes of log(1 + ρ_0(g_j)) is a
  field-independent number, which is moved into the normalisation constants (as Balaban does with log Z^{(j)}(1) and
  E^{(j)}(1) in CMP 109 (1.3)). This is uniform in K because it is not bounded at all: it is cancelled exactly in every
  normalised expectation and in Z_K/Z_K^ref when Z^ref carries the same constants. LF-count's divergence must then sit
  entirely in this constant; that is part of what (R2D) would show.

## 3. What counts as failure, and what does not count as success

Failure (each would be a precisely named wall):
- (F1) ρ(s) not C^4 in s with g-polynomial derivative bounds, e.g. through a non-smooth constraint or a branch set
  (hard normalised block spins, Balaban's δ-function with log-based M).
- (F2) Odd orders in s not vanishing (no reflection symmetry), leaving R = O(s³). That is still summable in d = 2
  (needs power > 2). In d = 4 the analogue is a remainder O(s^4) beyond the marginal F² term, i.e. a second
  marginal-order term, which would NOT be summable (needs power > 4).
- (F3) The second-order term not proportional to A_B (a second marginal operator), or (T1) needing constants that grow
  faster than e^{a'/g²} with a' < a.
- (F4) The bound only for s ≤ s_0(g) with s_0 → 0 as g → 0.
Not success:
- A bound for the isolated cube with a frozen exterior does NOT by itself give the R-operation in the full integral.
  The frozen exterior (W1: the sea fluctuates), nested or multi-scale large-field regions (W2) and the hard-constraint
  question (W3) must be stated as remaining walls, whatever the outcome of (R2D).

## 4. Outcome (ADDED AFTER the derivation; pointer only)
See PROOF.md, L5 [S7] "Proposition R2D-iso" and LOG.md session 7.

---

# Session 8 pre-statements (2026-10-27). Written BEFORE the session-8 derivations; sections 5-7 are not edited
# after the derivations start. Outcomes are pointers in section 8, added afterwards and marked.

## 5. W1 target (2D O(N): one or more large-field cubes in a FLUCTUATING small-field sea)

**Setting W1.** 2D O(N), N ≥ 3. Torus of T × T blocks (T odd), each block an L × L square of fine sites (L odd); the
block containing the origin is □_0. All fine spins n_x ∈ S^{N-1} are integrated (uniform measure). Block spins Φ_c ∈ R^N
(c ∈ block torus) are given; they are the background. Action
  S(n; Φ) = (1/g²)[ Σ_{all fine bonds} (1 - n_x·n_x') + (κ/2) Σ_c |Φ_c - L^{-2}Σ_{x∈c} n_x|² ].
Per-block cut χ_c := Π_{interior bonds of c} 1{|n_x - n_x'| < ε_1} (as in R2D-iso; crossing bonds are not cut).
Large-field expansion (exact): Z(Φ) = Σ_{Ω ⊂ blocks} Z_Ω(Φ), Z_Ω := ∫ Π_{c∈Ω}(1 - χ_c) Π_{c∉Ω} χ_c e^{-S}.
Regular background domain: D_reg(ε_0) := {Φ : 1/2 ≤ |Φ_c| ≤ 1, |Φ_c - Φ_c'| ≤ ε_0 for
neighbouring c, c'}, with 0 < ε_0 ≪ ε_1/L to be fixed by the proof.

**Target (W1), strong form.** There are ρ_0(g) ≥ 0 (field-independent) and activities K(X; Φ) on connected block sets X,
with K(X; ·) depending on Φ only through blocks within distance O(1)·diam X of X up to e^{-κ d}-tails, such that for
all T, all 0 < g ≤ g_0 and all Φ ∈ D_reg(ε_0):
  (W1-a) Z(Φ)/Z_∅(Φ) = exp( T²·log(1 + ρ_0(g)) + Σ_X K(X; Φ) );
  (W1-b) |K(X; Φ)| ≤ C e^{-a/g²} e^{-κ d(X)}, d(X) = tree length in block units, constants C, κ > 0, a > 0
         depending on (L, N, κ, ε_1, ε_0) only, uniform in T and in Φ ∈ D_reg(ε_0);
  (W1-c) renormalised form: for the smooth family Φ_c(s) = n(sc) (|∂^α n| ≤ 1, 1 ≤ |α| ≤ 4),
         Σ_{X ∋ □_0} |X|^{-1} K(X; Φ(s)) = k_0(g) + δβ(g)·A_B(Φ(s)) + R(s), |k_0|, |δβ| ≤ C e^{-a/g²},
         |R(s)| ≤ C e^{-a/g²} s⁴, for 0 ≤ s ≤ s_0 with s_0 g-independent (A_B: the block-lattice action on a
         D_4-symmetric bond set around □_0).
**Weak form (single defect).** F(Φ) := log Z(Φ) - log Z_{χ_0=1}(Φ) (release only □_0's cut, all other cubes cut)
obeys (W1-c) with K replaced by F, uniformly in T.
**Route.** Exact defect identity (Fubini) → R2D-iso's ρ averaged over the conditioned sea; a symmetry/locality lemma for
functions of the whole block-spin field; polymer/cluster expansion (Dimock I Thm 27, NOTES §1) for the multi-defect
form, with Dimock's per-level extraction (III Lemma 13) for the activities.
**Failure modes (each a named wall).**
  (W1-F1) no size bound on the defect ratio uniform over the fluctuating exterior (the frozen-exterior bound needs the
          collar near the background);
  (W1-F2) the sea's sensitivity ∂F/∂Φ_c not decaying exponentially in d(c, □_0) (needs clustering of the pinned
          nonlinear sea, i.e. the small-field cluster expansion), so no locality;
  (W1-F3) Dimock I Thm 27 not applicable (it needs an ULTRALOCAL measure; the sea is not ultralocal);
  (W1-F4) amplitude only e^{-a'/g²} with a' → 0, or s_0 → 0 as g → 0.
**Not success.** A frozen collar of any finite width; a Gaussian (linearised) sea; a statement only for Φ constant.

## 6. R4D-iso target (4D SU(N), isolated cube, frozen exterior)

**Setting.** Fine lattice Z⁴, L odd ≥ 3, cube □ = {x : |x_μ| ≤ (L-1)/2}, centre 0 a fine site. Integration variables:
the interior links (both ends in □), Haar measure. Frozen data D: every other link with at least one end in □ ∪ (its
nearest exterior layer) or in the contours below, and the coarse links V(c), c = (0, ±Le_μ). Action (tr over N × N,
Re tr 1 = N):
  S = (1/g²)[ Σ_{p ∩ int ≠ ∅} (1 - N^{-1}Re tr U_p) + κ Σ_{t} (1 - N^{-1}Re tr W_t) ],
W_t ranging over the B_4-symmetric family of closed words V(c)^{-1}·U(Γ ∪ [x,x'] ∪ -Γ') (Balaban's axial contour
families G(y,x), both ends, all orders; Γ inside □, Γ' in the neighbouring block, frozen). Cut on interior
plaquettes: χ = Π_{p ⊂ int} 1{||1 - U_p||_op < ε_1}. ρ := ∫(1-χ)e^{-S} / ∫χe^{-S}.
Background: a smooth su(N)-connection A on R⁴ in radial gauge x^μA_μ(x) = 0, with ||∂^αA_μ(x)||_op ≤ 1 for
1 ≤ |α| ≤ 6; rescaled A^{(s)}(y) := sA(sy); all data links and V(c) are the parallel transporters of A^{(s)} along the
straight segments. f(s) := ρ(D(s)). (Every smooth A is gauge-equivalent to a radial one, and ρ is gauge-invariant.)

**Lemma GT (gauge-invariant Taylor lemma), target.** For every C⁶ function F of the data that is invariant under all
lattice gauge transformations of the data, the point reflection ι and the hyperoctahedral group B_4 about 0:
  f(s) := F(D(s)) is even in s; f'(0) = f''(0) = f'''(0) = 0 (order s² vanishes); f^{(4)}(0)/24 = c_F Σ_{μ<ν}
  ||F_μν(0)||²_HS with c_F independent of A; |f(s) - f(0) - c_F s⁴ Σ||F_μν(0)||²| ≤ (s⁶/720) sup_{|σ|≤s}|f^{(6)}(σ)|.
**Target (R4D).** For every a < ε_1²/(4N) there are C, s_0, g_0 > 0 depending on (L, N, κ, ε_1, a) only such that, for
0 < g ≤ g_0, all such A and |s| ≤ s_0:
  ρ(s) = ρ_0(g) + δβ(g)·A_B(D(s)) + R(s), 0 ≤ ρ_0 ≤ Ce^{-a/g²}, |δβ| ≤ Ce^{-a/g²} (background-independent),
  |R(s)| ≤ C e^{-a/g²} s⁶; the same for log(1 + ρ). A_B := Σ_{p∈B}(1 - N^{-1}Re tr U_p), B a B_4- and ι-symmetric
  plaquette set of the data.
Consequence to be checked: remainder sum Σ_n L^{4n}L^{-6n} < ∞ (α = 2 against L^{4(k-j)}).
**Failure modes.** (R4-F1) a non-vanishing order-s² term (would be a relevant operator); (R4-F2) a second invariant at
order s⁴ (e.g. ε^{μνρσ} tr F_μνF_ρσ, or Λ² not absolutely irreducible under B_4); (R4-F3) a non-vanishing s⁵ term;
(R4-F4) s_0 → 0 as g → 0, or constants worse than e^{a'/g²}.
**Not success.** Frozen exterior (W1 stays), smooth background only (W2 stays), soft constraint only (W3 stays).

**Check c19 (criteria in checks/c19_criteria.md, written before the script):** B_4 character norm of Λ²R⁴; the
dimension of Ad × B_4-invariant quadratic forms on su(2) ⊗ Λ²; and Lemma GT on explicit gauge-invariant SU(2)
functions (incl. an exactly integrated single-link function) with B_4-broken and ι-broken controls.

## 7. W2 target (pre-stated only; not attacked in session 8)

**Setting.** As W1, two scales: a level-j large-field cube □ inside a level-(j+1) block that is itself large-field.
**Target (W2).** The renormalised bound of R2D-iso/R4D-iso holds for □ with the background replaced by the level-(j+1)
*large-field* configuration, with a remainder ≤ C e^{-a/g_j²} e^{-a/g_{j+1}²}·s^{d+2} (both suppressions kept), or
alternatively: nested large-field histories (Ω_1 ⊃ ... ⊃ Ω_k, Dimock II (145)-(148)) carry Π_j e^{-a|Ω_j^c|/g_j²}
with field-dependent parts renormalised level by level, uniformly in K.
**Failure modes.** (W2-F1) no smooth background inside a multi-scale large-field region, so no Taylor parameter;
(W2-F2) the inner cube's vacuum part ρ_0 depends on the outer large field (then it is not a constant and cannot be
moved into the normalisation); (W2-F3) the history sum's combinatorics grow faster than Π e^{-a/g_j²}.

## 8. Session-8 outcomes (ADDED AFTER the derivations; pointers only)
- §5 (W1): partial. Weak form reduced exactly to the OPEN item W1-loc (W1-LD + W1-cl) by Lemmas W1-def, W1-size,
  W1-sym (PROVEN-HERE); strong form not reached. Note: the decay rate written "κ" in §5 is called κ_d in PROOF.md, to
  keep κ for the constraint strength. See PROOF.md L5 [S8].
- §6 (R4D-iso, Lemma GT): met as pre-stated. Check c19 10/10 (checks/c19_out.txt).
- §7 (W2): pre-stated only.
- **[R78-fix] (session 9).** §5's weak form is ambiguous as pre-stated: its formula F = log Z - log Z_{χ_0=1} uses the
  full Z, while its parenthesis says "all other cubes cut". The session-8 proof adopted the second reading (every block
  ≠ □_0 cut), which is the easier one. This is recorded here; §5 itself is not edited.

---

# Session 9 pre-statements (2026-10-27). Written BEFORE the session-9 derivations of BG-reg and W1-loc (4D);
# sections 9-10 are not edited after the derivations start. Outcomes are pointers in section 11, added afterwards.
# Provenance note: these targets were formulated after reading REVIEW_S7_S8 and a short preliminary analysis in this
# session's reasoning. Pre-statement is a file-order fact, as REVIEW_S7_S8 (6) says.

Decision 4 (made this session by the lead, under delegated authority): the RG transformation is S4'-contour averaging
with a SOFT gauge-covariant constraint; Balaban's (0.4) with δ(M(U)V^{-1}) is a comparison branch. Both targets below
are for the soft-constraint RG.

## 9. BG-reg target (REVIEW_S7_S8 fix 4)

**Problem.** R2D-iso, GT and R4D-iso assume the frozen data are the lattice data of a smooth continuum field rescaled by
s. RG backgrounds are lattice fields. BG-reg = (a) a lattice replacement for that hypothesis + (b) the background
regularity it then needs.

**Target (BG-a), lattice Taylor lemma.** For data D on the R4D-iso data region define, gauge-invariantly, a size
parameter ε_2(D) (how far D is from gauge-trivial) and a variation parameter ε_3(D) (how far the parallel-transported
plaquette logs are from one constant curvature Φ ∈ su(N) ⊗ Λ²R⁴). Then, for every C³ function F invariant under gauge
transformations of the data and under B_4:
  |F(D) - F(1) - c_F Σ_{μ<ν}||Φ_μν||²| ≤ C (ε_2ε_3 + ε_3² + ε_2³),   with the same c_F as Lemma GT,
and R4D-iso holds in the form ρ(D) = ρ_0 + δβ·A_B(D) + R(D), |R(D)| ≤ Ce^{-a/g²}(ε_2ε_3 + ε_3² + ε_2³), with the SAME ρ_0
and δβ, for all D with ε_2(D) ≤ ε_* (ε_*, a, C g-independent). The analogous statement for R2D-iso.
**Target (BG-b), the regularity needed.** State, as a hypothesis on the level-k background seen on level-j cubes, the
weakest regularity under which the level-summed remainders are bounded uniformly in k and K; identify which part of L2
it is; try to prove that part for the soft-constraint S4' minimiser. Diagnostic: check c20 (criteria file first) on
the linearised abelian soft-constraint background built with the S4' contour family.
**Failure modes.** (BG-F1) the lattice remainder not controlled by gauge-invariant lattice parameters; (BG-F2) the
summation needing the full C⁶ regularity of the smooth families (then all of L2's regularity is needed); (BG-F3) the
S4' background's curvature too rough for the summation (in c20: mean oscillation over sub-cubes not summable over
scales), which would make BG-b false for our averaging.
**Not success.** A statement for smooth backgrounds only; "assume L2" without naming the part used.

## 10. W1-loc (4D) target, restated per REVIEW_S7_S8 (3).1-5

**Setting W1-4D.** One soft-constraint RG step for 4D SU(N) on a torus of T⁴ blocks (T odd), block side L. The block
□_0 is centred at 0. Every block ≠ □_0 carries the sea cut; □_0 is released and its large-field weight is R4D-iso's
ρ_□(D) (interior-plaquette cut ε_1), a function of its frozen data D = the sea links of R4D-iso's data region and the
coarse links V(c) at □_0. ⟨·⟩_cut: the probability measure with every block cut, □_0 included.
**Target.** There are a, κ_d, C_q, p_q, g_0 > 0 depending on (L, N, κ, ε_1) only such that, uniformly in T and g ≤ g_0:
  (LD) ⟨ρ_□⟩_cut ≤ C g^{-p} e^{-a/g²};
  (cl) for 1 ≤ q ≤ 6 and coarse links c_1, …, c_q, INCLUDING those at □_0 (the direct dependence of ρ_□ on its own
       coarse links), |∂_{c_1}···∂_{c_q} log(1 + ⟨ρ_□⟩_cut)| ≤ C_q g^{-p_q} e^{-a/g²} e^{-κ_d max_j d(c_j, □_0)}
       (Lie-algebra derivatives in V(c_j); a polynomial g-loss is allowed, no (g²/κ)^q gain is demanded);
  backgrounds: either lattice data obeying the BG-a hypothesis, or s-families that are constant outside a ball of radius
  R_0 with sR_0 < T/2 (periodic across the seam); for the s-families, s_0 ≲ δ_0 (the collar scale) is stated.
**Route (Dimock I template; NOTES §1).** (i) An exact size reduction that does not use the released measure P_rel;
(ii) the small-field sea in Dimock form: background + g·𝒞W with W under an ultralocal probability measure μ*, a
random-walk expansion of 𝒞, and a polymer interaction; (iii) concentration for the collar; (iv) localisation of ρ_□
and the cluster expansion with sources (Dimock I Thm 27).
**Failure modes.** (W4-F1) the Dimock-form representation of the soft-RG sea is not available from what is proven
(then it is the exact wall, and it is the small-field package L2/L3g/L4a-form); (W4-F2) the localisation step needs an
analyticity radius that shrinks with g (corridor width growing with 1/g); (W4-F3) Thm 27 is load-bearing but not
re-verified; (W4-F4) a or s_0 depends on g.
**Not success.** A frozen exterior; a Gaussian (non-interacting) sea only; a conditional statement whose hypothesis is
not named exactly.

## 11. Session-9 outcomes (ADDED AFTER the derivations; pointers only)
- §9 (BG-reg): (a) met. Lemma GT-lat + Proposition R4D-lat, with remainder C(ε_2(ε_3+ε_V) + (ε_3+ε_V)² + ε_2³). The
  parameters needed a third one, ε_V (the coarse-link mismatch), which §9 did not name. (b) The needed regularity is
  stated exactly (BG-b; Lemma BG-sum) and identified inside L2; it is not proven for the soft S4' minimiser. c20
  VALID, model SUMMABLE (BG-F3 not seen). BG-F2 avoided (C³ suffices). See PROOF.md L5 [S9].
- §10 (W1-loc, 4D): (LD) reduced exactly to the hypothesis (DF1-3') via Lemma W1-size' (with a reference weight
  w_ref, which §10's route did not anticipate) and Lemma AG; (cl) argued under (DF4) + Thm 27. W4-F1 and W4-F3 met;
  W4-F2 only as a polynomial loss; W4-F4 avoided. See PROOF.md L5 [S9].

# Session 10 pre-statements (2026-10-27). Written BEFORE the session-10 derivations and before any c21/c22 script;
# sections 12-14 are not edited after the derivations start. Outcomes are pointers in section 15, added afterwards.
# Provenance note: the targets were formulated after reading Dimock I App. B (pp. 37-44, from the arXiv PDF text) and
# PROOF.md L5 [S9], and after a short preliminary analysis in this session's reasoning (which already suggested two
# points recorded below as things to TEST, not as results: that c_0 in Thm 27 must depend on κ, and that the S4'
# funnel part of the soft current may cancel at critical points). Pre-statement is a file-order fact.

## 12. Target A: re-verify Dimock I Theorem 27 (cluster expansion) on our setting, including (323)

**Setting CE.** d = 4. A torus of unit (M = 1 after scaling) cubes □; a polymer X is a nonempty connected union of
cubes; d(X) := the length of the shortest tree in X meeting every cube of X (Dimock (119)); |X| := number of cubes.
Fields Φ = (Φ(x)) on the sites; every site lies in exactly one cube; μ = Π_x μ_x a product probability measure.
H(X, Φ) measurable (complex allowed), depending on Φ|_X only.
**Target statement (Thm 27 form).** There are constants κ_0, K_0, C_1 depending only on d = 4, given explicitly, and a
c_0 > 0, such that if |H(X, Φ)| ≤ H_0 e^{-κ d(X)} on supp μ, with κ > 3κ_0 + 3 and H_0 ≤ c_0, then
∫exp(Σ_X H(X)) dμ = exp(Σ_Y H#(Y)), H#(Y) depends only on {H(X) : X ⊂ Y}, vanishes unless Y is a polymer, and
|H#(Y)| ≤ C_1 H_0 e^{-(κ - 3κ_0 - 3) d(Y)}.
**Sub-targets.** (A1) the tree-graph inequality (323), |ρ^T(Y_1, …, Y_n)| ≤ #{spanning trees of the overlap graph},
with a complete proof (Penrose partition scheme or Brydges-Kennedy forest formula); (A2) the geometric lemmas used
(Dimock (122), (290), (294), (305)) with explicit d = 4 constants; (A3) the convergence/identity step (formal series →
analytic identity) written rigorously; (A4) a line-by-line comparison with Dimock's text, listing every discrepancy.
**Decision to make, not presume.** Whether c_0 can depend on d only (as Thm 27 states) or must depend on κ (as the
proof's "So c0 does depend on κ" on p.40 says). If a counterexample exists, Thm 27 is re-verified in the corrected
form and the discrepancy is recorded; that counts as success for A (the corrected statement is what W1-loc uses).
**Exact check c21 (criteria file before the script).** Penrose identity and (323) on all small connected graphs; the
Mayer/grouping identity (steps 1-2) and the cluster series (step 3) against the exact log on a tiny 2D lattice by
direct polymer enumeration; and the κ-dependence question on an exactly solvable Ising instance.
**Failure modes.** (CE-F1) (323) false or unprovable in the form used; (CE-F2) a geometric constant not finite in d = 4;
(CE-F3) the bound holds only with a weaker decay rate than κ - 3κ_0 - 3; (CE-F4) the series identity needs more than
absolute convergence on a polydisc.
**Not success.** Citing Penrose or Brydges-Kennedy without a written proof; constants "O(1)" without a value.

## 13. Target B: BG-b (sub-block regularity) for the soft S4' minimiser

**Setting.** The tree-level soft chain of decision 4: fine action + Σ_j soft S4' terms with the normalised kernel,
intermediate levels minimised. Linearisation around the trivial background: the abelian (colour-componentwise) chain
E = ½||dB_0||² + Σ_{j<k} (κ_j/2)||Q B_j - B_{j+1}||², B_k given (Q = linearised S4', own units per level, d = 4).
**Target (B-lin).** Prove BG-b ((b1) sup coarse-unit curvature, (b2) summable mean oscillation, Lemma BG-sum) for the
critical points of the linearised chain, uniformly in k and the torus, from hypotheses that are the soft analogue of
CMP 109 (1.2) (curvature small AND the current/residual small), via a written lattice elliptic step (Hölder or
log-Lipschitz oscillation decay for dF = 0, d*F = J on the lattice) and the Euler-Lagrange structure of the chain.
Name exactly which hypotheses remain.
**Target (B-NA).** A non-abelian perturbation bound transferring (B-lin) to SU(N) backgrounds with coarse curvature
≤ ε_0, using A1-NA(1) (positive averaging of plaquette logs with an O(φ²) error) and BCH; or the exact step that fails.
**Check c22 (criteria file before the script; feasibility-dependent).** A non-abelian SU(2) 4D small-torus instance of
the one-step soft minimiser (memory peak < 2 GB, one job), measuring the quantities the proof uses (curvature sup,
oscillation over cubes, the soft current's concentration on the S4' axial legs, the residual divergence), against a
linearised comparison and a control with power.
**Failure modes.** (BG-F4) the elliptic step needs J ≪ (coarse units) beyond what the chain gives (a current growing
with the depth k); (BG-F5) the soft current concentrates on the S4' axial lines (L3g-ob line part) and spoils the
oscillation bound; (BG-F6) the non-abelian corrections are not small relative to the linear terms at ε_0.
**Not success.** A statement for smooth backgrounds only; "assume L2" without naming the part used; a 2D-only check.

## 14. Target C (if time remains): (DF) as a dependency sub-DAG
Write (DF1)-(DF4) and Thm 27 as a sub-DAG in PROOF.md (nodes = precise statements; edges = "used by"), with each
node's status, and mark which nodes A and B discharge. Not success: a list without the dependencies.

## 15. Session-10 outcomes (ADDED AFTER the derivations; pointers only)
- §12 (A): met, in corrected form. Theorem CE (PROVEN-HERE) has explicit d = 4 constants (κ_0 = 324 log 12800,
  K_0 = e^{κ_0/4}/6400, C_1 κ-independent), Lemma TG = (323) via the Penrose partition, and a rigorous analytic-identity
  step. The "decision to make" came out as: c_0 MUST depend on κ (Proposition CE-κ, Ising instance; c21 I1).
  [R910-fix: the session-10 sentence "So Thm 27 as stated is false" is withdrawn.] Thm 27's statement says c0 depends
  on d only; its proof says (p.40) "So c0 does depend on κ". Proposition CE-κ shows the κ-dependence is necessary.
  This corrects the statement's quantifiers, as the author's remark does. Dimock's proof and his application (κ fixed)
  are unaffected. Theorem CE is the corrected form. Four textual discrepancies (1, 3, 4, 5) and one definitional
  difference (*-connected vs Dimock's face-connected polymers) are listed in PROOF L5 [S10].
  CE-F1/F2/F4 not met; CE-F3 is met only in this sense: the rate κ - 3κ_0 - 3 holds, but κ_0 ≈ 3064 is the honest
  constant of the touching-tree metric. c21: 13/13 PASS.
- §13 (B): B-lin met under named hypotheses. Proposition BG-b-lin proves BG-b ⇐ (H1) + (H2), the soft analogue of
  CMP 109 (1.2), via Lemma LES (Hölder-α), Lemma CR and Lemma J-str. BG-F4 avoided: the current is bounded in coarse
  units, uniformly in k. BG-F5 avoided: the funnel part vanishes at critical points. B-NA is argued, not written with
  constants. BG-F6 was not seen in c22 (deviations ≤ 8%). c22 VALID: Q1, Q2 PASS; Q3 FAIL (monotonicity
  sub-criterion). (H1) + (H2) themselves are not proven: soft-L2 node N2.
- §14 (C): met. The (DF) sub-DAG N1-N12 is in PROOF L5 [S10]. A discharges N1; B discharges N3 (linear). The (DF3')
  tilt argument is argued.

## 16. Session-11 target N2 (linear half): soft background bounded by the coarse CURVATURE (pre-stated 2026-10-27, before any session-11 derivation)

**Setting.** Setting SC of PROOF L5 [S10] (d = 4, linearised abelian soft chain, levels 0..k, κ_i ≤ κ_+, B_k given,
torus in own units per level, Q = linearised S4' map). E_k(B_k) := min over B_0, …, B_{k-1} of the chain energy.
Residuals r_i, fine curvature f_0 = L^{2k}dB_0 as in [S10]. For the SU(N) soft chain (tree-level exponent of the
normalised kernel, decision 4), the residual size is |log(V_{i+1,c}^{-1}polar M̄_c)|.
**First lemma (REVIEW_S9_S10 strategic verdict).** The top residual is bounded by the gauge-invariant coarse curvature,
not by the field size.
- **(N2-a) Gauge-orbit lemma.** Abelian: minimisers exist; r_i and dB_0 are the same at every minimiser, are linear in
  B_k, depend on B_k only through dB_k, and vanish when dB_k = 0 (including non-trivial flat classes on the torus).
  SU(N): at every global minimiser, every gauge-invariant quantity (residual sizes, plaquette curvatures) is a function
  of the coarse gauge orbit of V_k, and all residuals and the Wilson action vanish when V_k is flat.
- **(N2-b) Curvature energy bound.** E_k(B_k) ≤ C_E(1 + κ_+)||dB_k||², with C_E absolute (d = 4, L ≥ 3) and uniform
  in k and the torus. Corollaries: ||r_{k-1}||_2² ≤ 2C_E(1 + κ_+)κ_{k-1}^{-1}||dB_k||² and the coarse-normalised
  ℓ² norm of f_0 ≤ (2C_E(1 + κ_+))^{1/2}||dB_k||: the ℓ² forms of (H1) and (H2).
**Then, as far as it goes.**
- **(N2-c) Local energy bound (LED).** The chain energy of the minimiser inside a fixed coarse neighbourhood of any
  coarse cell is ≤ C sup|dB_k|², uniformly in k (e.g. from exponential decay of the response in coarse units, by
  Combes-Thomas or hole-filling). Attempt; if not proven, name the exact failing step.
- **(N2-d) Sup forms.** (H2) sup|r_{k-1}| ≤ C sup|dB_k| and (H1) sup|f_0| ≤ C sup|dB_k| ⇐ (N2-c) (with J-str and a
  sup version of LES).
**Failure modes.** (N2-F1) the residual depends on the field size beyond the curvature (then (H2) is not a small-field
condition, and N2 as posed fails); (N2-F2) the energy bound grows with k (d = 4 is marginal: each level could
contribute O(1)); (N2-F3) the response decay rate is not uniform in k.
**Not success.** A smooth-background-only statement; constants that depend on k or on the torus; "assume CMP 102".
**Check c23 (criteria file before the script).** (A) Abelian linear chain, d = 2 with k = 1..4 and d = 4 with k = 1:
gauge-orbit independence, closed data giving zero energy, the explicit test-configuration energy vs the true minimum
vs k, and (informational) the decay of the response to localised curvature vs k. (B) SU(2), d = 4, one step (c22
machinery): data = (large random coarse pure gauge) × (small curvature) and (large flat constant holonomy) × (small
curvature), against the small-curvature data alone: the residual must stay at the curvature scale, not the field-size
scale.

## 17. Session-11 target N4 (abelian): gauge fixing for the soft RG step (pre-stated, before the derivation)

**Setting.** One linearised abelian soft RG step: fine 1-forms A (Lebesgue), coarse b fixed, integrand
F(A)e^{-½||dA||² - (κ/2)||QA - b||²} with F invariant under the symmetry group of the integrand.
**Target.**
- (N4-a) A finite-dimensional linear Faddeev-Popov lemma: for a linear gauge action and any admissible linear
  gauge-fixing (δ-slices, Gaussian terms, or mixtures), the gauge-fixed integral equals an explicit A- and
  b-independent constant times the quotient integral.
- (N4-b) Identify the exact symmetry group at fixed b (fine gauge functions whose root values are constant) and the
  legitimate fixings: the δ(h) slice of L3g(a)-slice plus a Feynman term on the residual group, with the FP constant
  A- and b-independent.
- (N4-c) Decide whether L3g(a)-slice's "double gauge fixing" (δ(h) plus the full Δ = d*d + dd*) is legitimate at
  fixed b. If not, give the exact correction and the legitimate fluctuation operator on H_0, and state exactly what
  must be proven for its uniform gap.
**Check c24 (criteria first; small, dense).** The lowest eigenvalue on H_0 of the legitimate operator vs the Δ version,
d = 2, 3, 4 at small block sides; admissibility (strict positivity) at every size; trends informational.
**Not success.** "The FP factor is A-independent by linearity" without the group and the fixing written out.

## 18. Session-11 optional target: the sharper polymer-size bound and κ_0 (pre-stated, before the derivation)

**Target.** Under the touching-tree reading of Dimock (119) (a connected finite union of segments meeting every closed
cube of X), prove |X| ≤ 3^d(1 + d(X)) (Dimock's (122), quoted there without proof), or a stronger explicit bound, and
recompute Theorem CE's constants (κ_0, K_0, C_K, B, C_1, c_0(κ)) with it. This lowers the decay rate κ > 3κ_0 + 3
that node N6 must deliver (currently κ_0 = 324 log 12800 ≈ 3064, κ ≳ 9.2·10³).
**Check c25 (criteria first).** Exact cube counts for random and adversarial connected segment unions in d = 2, 3, 4
against the bound.
**Not success.** A bound for one reading of (119) presented as covering the other.

## 19. Session-11 outcomes (ADDED AFTER the derivations; pointers only)
- §16 (N2): the first lemma is met. N2-F1 is excluded: the top residual is a function of the gauge orbit and
  vanishes on flat classes (Lemma N2-a, abelian and SU(N)), and E_k ≤ C_E(1 + κ_+)||dB_k||² uniformly in k
  (Lemma N2-E, Whitney test chain), which gives the ℓ² forms of (H1) and (H2). N2-F2 is avoided at the ℓ² level.
  (N2-d) is met as Proposition N2-red, (H1) + (H2) ⇐ (LED). (N2-c) (LED) is NOT proven; the exact failing step is
  in PROOF L5 [S11]. c23: VALID (A and B); Q1, Q2, Q4, Q5, Q6 PASS; Q3 FAIL as pre-registered (a criterion-design
  flaw: the values decrease in k; not edited).
- §17 (N4): (N4-a) and (N4-b) are met as Lemma FP-ab and its application. (N4-c): the double fixing is not
  legitimate as an identity; the explicit weight W, the legitimate operator O_FP and the exact remaining statement
  (the physical gap on Phys) are given. c24: VALID; Q1 PASS.
- §18 (κ_0): met in stronger form. Lemma CE-geo' gives |X| ≤ 2^d + 2^{d-1}√d·d(X) ⇒ the upper inequality of (122) (Dimock: d = 3) [R1112-fix: was "⇒ (122)"; the lower inequality d(X) ≤ |X| is not proven or used]; κ_0 = 16 log 12800 ≈ 151.3;
  N6 must deliver κ > ≈ 457. c25: Q1 PASS.

## 20. Session-12 target (LED): the local energy bound for the linearised soft chain (pre-stated 2026-10-27 15:41 UTC, before any written session-12 derivation and before any session-12 script; the lead's exploratory reasoning in this session preceded it)

**Setting.** Setting SC of PROOF L5 [S10] (d = 4, L ≥ 3 odd, levels 0..k, κ_- ≤ κ_i ≤ κ_+, Q = Q_root of S4',
coarse torus side T). The minimiser's local energy E_loc(C) as in Proposition N2-red.
**Target.** (LED) sup_C E_loc(C) ≤ C_loc sup|dB_k|², with C_loc depending on (L, κ_±) only, uniform in k and T. Or,
failing that, the exact wall: which term, in which norm, with what scaling in k.
**Allowed routes** (any): (a) telescoping via the gauge-orbit structure (N2-a); (b) decay of the response map at each
level's own scale; (c) a Caccioppoli / Fourier-symbol argument for the Euler-Lagrange system. The chain is coarse
translation invariant, so a coarse Bloch/Fourier treatment is legitimate.
**Sufficient intermediate statements** (either is acceptable as a reduction step, not as success):
- the sup forms (H1) sup|f_0| ≤ C sup|dB_k| and (H2) sup|r_{k-1}| ≤ C sup|dB_k| directly (then (LED) is immediate);
- an ℓ¹ bound, uniform in k and T, on the coarse convolution kernel of the linear map dB_k ↦ r_{k-1} (and of
  dB_k ↦ f_0 at each fine offset).
**Failure modes.** (LED-F1) the kernel norm grows with k (the marginal count); (LED-F2) a non-summable tail (e.g.
|x|^{-4} in d = 4) in the dB_k ↦ f_0 map; (LED-F3) a constant that depends on T through the zero mode.
**Not success.** Bounds that hold only for smooth data, or that depend on k or T; symbol bounds asserted without
uniform-in-n derivative estimates; numerics in place of a proof.
**Check c26 (criteria file before the script).** (A) An exact identity check of any closed-form (dual/Fourier)
representation used, against the real-space LSMR minimiser of c23's chain (small d = 2, 3, 4 tori). (B) The ℓ¹ norms of
the response kernels in d = 4 versus k (k = 1..6), to see whether they stabilise. (B) is informational support only.

## 21. Session-12 target N4 (physical gap) (pre-stated 2026-10-27 15:41 UTC, same conditions as §20)

**Setting.** PROOF L5 [S11], N4: one linearised abelian soft step, d = 4, fine spacing ε = 1/n (n odd ≥ 3), unit blocks,
coarse torus side T ≥ 2, Q = Q_root (S4'), h the L3g(a)-slice functional, H_0 = {h = 0}, Λ_res, Phys.
**Target.** ||dA||² + κ||QA||² ≥ c||A||² on Phys, with c = c(κ) > 0 independent of n and T (explicit constants
preferred). Equivalently: for every A ∈ H_0, inf_{λ∈Λ_res}||A + dλ||² ≤ C(||dA||² + ||QA||²).
**Failure modes.** (PG-F1) the point (root) components of d*A on Phys cost a factor growing with n (the n² loss of the
naive ||d*A||² route); (PG-F2) the coarse-scale co-closed part is controlled only through the torus Poincaré
constant (T-dependence); (PG-F3) a line-trace estimate for h that loses a power of n.
**Not success.** A gap with ||d*A||² added (that is L3g(a)-slice); a constant depending on n or T; numerics.
**Check c27 (criteria first).** Exact identities and constants used by the proof (block-flux co-closedness, the
straight-vs-flux comparison, the orbit-minimum decomposition, the 3D Neumann point constant), on small tori.

## 22. Session-12 optional target: B-NA (i)-(iii) with explicit constants (pre-stated, same conditions)
**Target.** The non-abelian transfer of BG-b-lin / N2 with explicit constants, or a precise list of what is still
argued. Attempted only if §20 and §21 are finished.

## 23. Session-12 outcomes (ADDED AFTER the derivations; pointers only)
- §20 (LED): met in the stronger "sufficient intermediate" form. Theorem N2-lin (PROOF L5 [S12]) proves (H1) and (H2)
  in sup form, and then (LED), uniformly in k and T. The ℓ¹ kernel route covers the dB_k ↦ f_0 map only through the
  representative 𝒦̂_u + Π_coex. The naive extension shows LED-F2 (a |x|^{-4} tail) off closed data, which is
  irrelevant here. c26: A VALID; Q1-Q6, V3 PASS; Q7 FAIL as pre-registered (a T-ratio of 1.104 vs 1.1; the increments
  fit a summable c/T tail).
- §21 (physical gap): met. Proposition PG, c_PG = min(1, κ)/(3.5·10⁶), uniform in n and T; PG-F1-F3 are avoided as
  stated there. c27: E1, E2, E4-E6 PASS; E3 FAIL as pre-registered (a normalisation flaw in one sub-check; the absolute
  error is 1e-15).
- §22 (B-NA): not attempted.

## 24. Session-13 target N2-exp: exponential locality of the linearised soft-chain response (pre-stated 2026-10-27, before any written session-13 derivation and before any session-13 script; the lead's exploratory reasoning in this session, on paper only, preceded it)

**Setting.** Setting SC and the symbols of PROOF L5 [S12] (Lemma LED-symb): d = 4, L ≥ 3 odd, n = L^k, κ_- ≤ κ_i ≤ κ_+,
coarse torus side T. The linear maps are (i) F = dB_k ↦ r = r_{k-1} (symbol 𝓡̂, Lemma LED-symb) and (ii) the closed-data
maps to f_0 at each fine offset u. Because F is closed, (ii) has no unique F-kernel; the canonical closed-data object is
the map from the coarse field itself, B_k ↦ f_0 (and B_k ↦ r), i.e. the symbols composed with d̂.
**Target (N2-exp).** A rate m > 0 and a constant C, both depending only on (L, κ_±), such that, uniformly in k ≥ 1, T
and u, every entry K of the infinite-lattice kernels of (i) and of B_k ↦ (r, f_0) obeys |K(X)| ≤ C e^{-m|X|_1}; the
torus kernel is its periodisation. Route: show the Fourier symbol extends analytically to the complex strip
|Im p_α| < m with a uniform bound (Paley-Wiener), handling the p = 0 non-smoothness exactly; compute m explicitly.
**Also required.** State precisely which kernel is exponential and which (if any) has a power tail: the unrestricted
extension of (ii) to all 2-forms, the session-12 representative 𝒦̂_u + Π_coex, the B_k-kernels. State which one N6
consumes and how the rate enters N6's κ > 3κ_0 + 3 requirement.
**Failure modes.** (EXP-F1) a genuine non-analytic term at p = 0 on closed data (then a power tail is real, and decision
4's soft kernel cannot feed N6 without a change: flag for the lead, do NOT reverse decision 4 here); (EXP-F2) a strip
width that shrinks with k (n → ∞) or with T; (EXP-F3) complex zeros of the denominators approaching the real torus.
**Not success.** Numerics in place of a proof; a rate depending on k or T; a strip shown only for fixed n.
**Check c28 (criteria file first).** (A) exact identities for any closed form used, against c26's symbol code; (B) the
complex-strip inequalities used by the proof, sampled at complex points for several n; (C) measured decay rates of the
kernels (several T and k) against the proven m, and against the nearest complex singularity located numerically
(informational).

## 25. Session-13 short target (IT'): the physical gap for the composite root map (pre-stated, same conditions as §24)

**Setting.** PROOF L5 [S12] Proposition PG, with the one-step S4' root map replaced by the k-fold composite
Q^{(k)} = Q_root ∘ … ∘ Q_root from the fine lattice (ε = L^{-k}) to the coarse lattice, its slice functional h^{(k)}
(h^{(m+1)} = Mh^{(m)} + hQ^{(m)}), H_0^{(k)} := {h^{(k)} = 0}, and the corresponding Λ_res and Phys.
**Target.** ||dA||² + κ||Q^{(k)}A||² ≥ c||A||² on Phys^{(k)}, with c = c(κ, L) > 0 independent of k and T (explicit
preferred); equivalently the PG orbit bound for h^{(k)}. Expected route: the PG proof with PG-line replaced by a line
bound for h^{(k)}, uniform in k.
**Failure modes.** (IT-F1) the composite slice functional concentrates (trace loss growing with k); (IT-F2) the
composite residual group differs from PG's Λ_res.
**Not success.** A k-dependent constant; numerics.
**Check (optional, in c28 Part D, criteria first).** The unrolled formula for h^{(k)} and the line bound on a small
d = 4 example (k = 2), exact arithmetic up to float.

## 26. Session-13 outcomes (ADDED AFTER the derivations; pointers only)
- §24 (N2-exp): met. Theorem N2-exp (PROOF L5 [S13]): the response symbols are analytic in a strip of explicit width
  m_*(L, κ_±) > 0, uniform in k and T (m_* = 0.0111 at L = 3, κ ≡ 1), because the fine Green's function's 1/φ cancels
  exactly (Lemma EXP-id). Exponential: F ↦ r on all F; B_k ↦ r, B_k ↦ f_0. Power tail: the unrestricted f_0 extension and
  the 𝒦̂_u + Π_coex representative. N6 consumes the B_k-kernels. EXP-F1-F3 do not occur. c28: A VALID; B FAIL (float
  tie at the sharp point p = 0); C1, C2 PASS, C3, C4 FAIL (pre-asymptotic window; post-run fits agree with the located
  singularity, rate ≈ 0.98 at κ = 1, within 5-10%).
- §25 (IT'): met. Lemma IT-line and Proposition PG^{(k)}: C_IT(3) ≤ 3.6·10⁶, uniform in k and T; IT-F1, IT-F2 do not
  occur. c28 D PASS.

## 27. Session-14 target A (B-NA): the SU(N) soft chain as a perturbation of the linearised chain (pre-stated 2026-10-27 17:32 UTC, before any written session-14 derivation and before any session-14 check script; the lead's exploratory reasoning in this session, and two scratch arithmetic probes of a sharper strip constant (scratchpad dconsts*.py, used only for target D's feasibility, not a check), preceded it)

**Setting.** PROOF L5: Lemma N2-a (SU(N)), Setting SC, Theorems N2-lin and N2-exp, Lemma A1-NA(1), Lemma GT-lat. The
SU(N) chain energy E_NA = S_W(U) + Σ_i(κ_i/g²)Σ_cφ_c (normalised soft kernel, decision 4), coarse data V_k, levels in
their own units, n = L^k.
**Target (B-NA (i)-(iii) with explicit constants).** For data V_k with coarse curvature ≤ ε (or, as a first step, V_k =
exp(B_k) with sup|B_k| ≤ ε in a global gauge; state which), uniformly in k ≥ 1 and T:
- existence of a critical point of E_NA near the linear solution, unique in a stated ball modulo the chain gauge group;
- x_NA = x_lin + x_NL with an explicit bound on x_NL (second order in ε) in a stated norm;
- the response kernels of the gauge-invariant outputs (r, f_0) decay like e^{-m|X|}, m < m_* (stated loss);
- an explicit threshold ε_0(L, κ_±, N).
Route: Lie-algebra coordinates in a stated gauge; E_NA = E_lin + remainder; a contraction / implicit-function argument in
an exponentially weighted norm with weight e^{m|x|}, using the linear kernels.
**Failure modes to watch.** (BNA-F1) the proven linear kernels (B_k-data kernels of N2-exp) do not control the response
to the general sources that the non-linear remainder produces; (BNA-F2) the contraction does not close in a sup norm
uniformly in n (the fine-level Wilson non-linearity is marginal, and the linear inverse may not be bounded between the
norms the remainder needs); (BNA-F3) the gauge fixing used for the contraction is not compatible with locality
(non-local gauge projectors); (BNA-F4) torus holonomies (flat but non-trivial V_k) are not in a small-field gauge.
**Not success.** Numerics in place of a proof; a constant depending on k or T; a contraction whose linear input is
assumed rather than proven, unless it is labelled as a reduction and the input is stated precisely.
**Acceptable partial outcome.** A reduction of B-NA to a precisely stated linear estimate, with every non-linear,
algebraic and gauge-fixing step proven with explicit constants, and the failure step named.

## 28. Session-14 target B: SU(N) versions of N2-E, N2-lin, N2-exp (pre-stated, same conditions as §27)
**Target.** As corollaries of §27 (or of separately proven SU(N) lemmas): E_NA ≤ C(1 + κ_+)·(curvature)² (N2-E), sup
bounds of r and f_0 by the coarse curvature (N2-lin), and exponential decay with a stated loss in the rate (N2-exp).
Each stated with its hypotheses; anything that rests on an unproven §27 input is labelled conditional.
**Not success.** Statements in terms of sup|B_k| presented as curvature statements.

## 29. Session-14 target C ((NA) for N4): gauge fixing on a small-field SU(N) background (pre-stated, same conditions)
**Setting.** PROOF L5 [S11]-[S13]: Lemma FP-ab and its soft-step application, Proposition PG, Lemma IT-line,
Proposition PG^{(k)}; L3g(a)-slice (NA).
**Target.** (a) The legitimate covariant fixing at an SU(N) background: the covariant slice functional h_U, the residual
group, the Faddeev-Popov identity with a background- and field-independent constant (what replaces FP-ab's linear
invariance); (b) the physical gap of the covariant fluctuation operator on the covariant Phys, as a perturbation of PG /
PG^{(k)}, with an explicit smallness condition on the background (uniform in n and T).
**Failure modes.** (NA-F1) the Gaussian part is not invariant under the linearised covariant gauge action (off
critical backgrounds); (NA-F2) the perturbation of PG's orbit decomposition is not uniform in n (line traces of the
S4' funnels, point capacities); (NA-F3) the covariant residual group is not admissible.
**Not success.** A gap with an n- or T-dependent constant; numerics.

## 30. Session-14 optional target D: a sharper m_* (pre-stated, same conditions)
**Target.** A proven strip width m_*' > m_* = 0.0111 (L = 3, κ ≡ 1), uniform in k, T, u, by sharper complex-strip
bounds on the explicit symbol (Lemma EXP-strip), keeping Theorem N2-exp's conclusion. State the new value at
κ = 0.25, 1, 4 and κ̂ = 1, 16, and the resulting N6 block-size requirement M ≳ 457/m_*'.
**Not success.** A numerically located rate; a bound shown only for fixed n.

## 31. Session-14 check c29 (criteria file first: checks/c29_criteria.md)
SU(2), d = 4, small torus, one soft step (c22 geometry): (C) the scaling of the non-abelian minimiser's deviation from
the linear solution (the contraction's second-order structure), and the decay of the non-abelian part of the response to
a localised data change against the linear part; (D) the covariant FP identities of target C at a critical background,
with a non-critical control. Optional (A) the identity behind any linear-source lemma; (B) target D's strip inequalities
at complex points. Memory peak < 1.5 GB; one job at a time.

## 32. Session-14 outcomes (ADDED AFTER the derivations; pointers only)
- §27 (B-NA): NOT met; the pre-stated acceptable partial outcome is met. Proposition B-NA-red (PROOF L5 [S14]) reduces
  B-NA to (G♯) (a multi-scale Schauder-type bound for the gauge-fixed linearised chain on general sources) and (R♯)
  (the remainder in the same norms), with explicit threshold ε_0. BNA-F1, F2 (scaling count, argued), F3 occur; F4 is
  handled by restricting to a global small-field gauge. Proven: NA-alg, NA-crit, NA-inv, NA-IFT, SRC-id.
- §28: conditional only (not counted); stated in the global-gauge D-norm, the curvature forms argued.
- §29 ((NA)): (a) met (Proposition NA-FP, every critical background, direct and composite slices; NA-F1 occurs off
  critical backgrounds, NA-F3 does not). (b) NOT met: NA-F2 occurs (the funnel-trace defect); routes recorded.
- §30 (m_*): met. m_*' = 0.0385 (κ ≡ 1), 0.0273 (0.25), 0.0307 (4); κ̂ = 16: 0.0141, 0.0227, 0.0217. M ≳ 1.2·10⁴.
- §31 (c29): A PASS, B PASS, C VALID (C1 FAIL as pre-registered on D(0.1) = 0.110 > 0.1, slope 1.04), D PASS.

## 33. Session-15 target A, (G♯)_0: the abelian multi-scale bound at the trivial background on general sources (pre-stated 2026-10-27 19:29 UTC, after applying REVIEW_S13_S14's fixes and after the lead's exploratory reasoning in this session, before any written session-15 derivation and before any session-15 check script)

**Setting.** Setting SC (PROOF L5 [S10]) with sources: d = 4, L ≥ 3 odd, n = L^k, κ_- ≤ κ_i ≤ κ_+, coarse torus side T,
levels i = 0, …, k in their own units, B_k given. The chain energy with sources is
  E_j(B) := ½||dB_0||² + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1}||² - Σ_{l=0}^{k-1}⟨j_l, B_l⟩,
with each j_l a co-closed, zero-mean level-l 1-form (the gauge-orthogonality condition for a level-l source; level 0 as
in SRC-id). Every co-closed zero-mean j_l is d*G_l for some level-l 2-form G_l (e.g. G_l = dΔ_l^{-1}j_l); the norms
below are taken in DIVERGENCE FORM, over representatives G_l (infimum over representatives).
**Units, distance, weights (all norms are defined here).**
- Coarse-unit values: a level-l 2-form H has coarse-unit value H^c := L^{2(k-l)}H; a level-(i+1) 1-form r has
  r^c := L^{k-1-i}r; the fine curvature in coarse units is f_0 := n²dB_0 (as before).
- Each lattice object z at level l (site, link, plaquette) has its coarse position L^{l-k}·(its base point); d(z, z') is
  the ℓ¹ torus distance between coarse positions.
- For m ≥ 0 and a coarse site X_0: w(z) := e^{m d(z, X_0)}, and for a level-l form v, ||v||_{∞,m} := sup_z w(z)|v^c(z)|
  (componentwise maximum; |·| the maximum over components).
- Level weights: ω_0 := 1, ω_l ≥ 1 (1 ≤ l ≤ k-1), Ω := Σ_{l=0}^{k-1}ω_l^{-1}. The intended choice is ω_l = L^{θ(k-l)} for
  l ≥ 1 (θ ∈ (0, 1]), so Ω ≤ 1 + 1/(L^θ - 1) uniformly in k.
- Campanato seminorm (level 0, coarse units, scales between the fine spacing and one coarse unit): for a fine 2-form
  H, [H]_{α,m} := sup_{x} sup_{1/n ≤ ρ ≤ 1} w(x)ρ^{-α}Osc_2(H^c; Q_ρ(x)), Osc_2 as in Lemma LES (in coarse units: the
  L²-average over the fine plaquettes in the box of coarse side ρ of |H^c - mean|²), 0 < α < 1.
- Source norm: **||G||_{Y} := max_l ω_l||G_l||_{∞,m}**, and the Hölder source norm ||G||_{Y,α} := ||G||_Y + [G_0]_{α,m}.
- Data norm: ||B_k||_{D,m} := ||B_k||_{∞,m} (gauge-variant, as in B-NA-red; the gauge-invariant outputs depend on B_k
  mod Closed only).
- Output norms (gauge-invariant):
  - soft: **||r||_{X_s} := max_{0≤i≤k-1}L^{k-1-i}||r_i||_{∞,m}** (the factor L^{k-1-i} records that the fine-level residuals
    are irrelevant, J-str (c));
  - fine: **||f_0||_{X_f,α} := ||f_0||_{∞,m} + [f_0]_{α,m}** (sup + Campanato).
  - configuration (for B-NA-red): ||B||_{X_c} := max_i (||B_i||_{∞,m} + ||dB_i||_{∞,m}) for a stated gauge-fixed
    representative (the abelian per-level slice h^{(i)} = 0 with Feynman terms); its Hölder version adds [f_0]_{α,m}.
**Targets.** With constants depending only on (L, κ_±, m, α), uniformly in k ≥ 1, T and X_0, for m < m_*' (some stated
loss):
- **(G♯_0-soft)** ||r||_{X_s} ≤ C_s(Ω||G||_Y + ||B_k||_{D,m}).
- **(G♯_0-fine)** ||f_0||_{X_f,α} ≤ C_f(||G||_{Y,α} + ||B_k||_{D,m}).
- **(G♯_0-field)** the configuration version in ||·||_{X_c} (needed by B-NA-red; pre-stated, attempted only if the first two
  are done).
Route: SRC-id generalised to sources at every level (exact effective datum), Green reciprocity with the proven
exponential B_k-kernels (Theorem N2-exp/N2-exp', Corollary N2-exp-b), J-str-type transport for the per-level residuals,
and a local lattice Schauder (Campanato) step for the fine level.
**Failure modes.** (G0-F1) a sum over levels that is not bounded without level weights (the marginal 4D count; then
state which ω are needed); (G0-F2) the fine-level Calderón-Zygmund singularity: no bound in sup norm alone for f_0
(expected; this is why the Hölder norm is used); (G0-F3) a long-range (non-exponential) tail of the f_0 response to fine
sources (screening fails at long range); (G0-F4) the bound needs a gauge-fixed field norm (then the gauge-invariant
statement is not available).
**Not success.** Numerics; constants depending on k or T; a bound with ω ≡ 1 claimed while the count is marginal; a
statement in non-divergence-form source norms presented as the divergence-form one, or conversely.
**Acceptable partial outcome.** (G♯_0-soft) proven and (G♯_0-fine) reduced to a precisely stated remaining input, with the
failing step named.

## 34. Session-15 parallel target B: is NA-F2 an artefact of the direct n = L^k step? (pre-stated, same conditions as §33)
**Question.** State which object N4's fluctuation operator is in the soft RG (the direct one-step kernel with n = L^k, or
one level with n = L whose "fine" energy is the effective chain energy E_k). Redo the NA-F2 defect computation of PROOF
L5 [S14] ((NA) gap) in the per-level setting (n = L at each level, level-i contours of length ≤ 2(L - 1)).
**Target.** Either (a) a bound of the linearised per-level defect by C(L)·(background size)·||A||² per block, with no
ε^{-1} = n trace loss, uniform in k and T, together with a precise statement of what the (NA) gap then reduces to; or
(b) the named step at which an n- or k-dependent loss reappears.
**Not success.** A bound that is uniform only for fixed k; numerics.

## 35. Session-15 optional target C: (R♯) in the §33 norms (pre-stated, same conditions)
**Target.** A precise statement of the remainder bound (R♯) of Proposition B-NA-red in the norms of §33 (source norm Y
and Y_α, configuration norm X_c), with the level weights ω the remainder actually has (from the scaling count of
BNA-F2); proven parts marked, the rest labelled.

## 36. Session-15 check c30 (criteria file first: checks/c30_criteria.md)
(A) the strip constants: the corrected (η, r_0) pairs of N2-exp (with the f_0 "≤ 0.15φ" condition in the definition of
η_*) and of N2-exp', in high precision; (B) the SRC-id f_0 identity at complex points (REVIEW_S13_S14 fix 9); (C) the
identities used by §33's proof (generalised source identity, reciprocity) against an LSMR chain with sources at every
level; (D) informational: the ratio of the measured soft-output norm to the proven bound. One job at a time; peak < 1.5 GB.

**[R1314-fix] Annotation to §32 (added in session 15; the §32 lines above are not edited).** REVIEW_S13_S14 found two
overclaims and one rounding:
- §27: read "acceptable partial outcome PARTIALLY met: the algebraic and fixed-point steps (NA-alg, NA-crit, NA-inv,
  NA-IFT) are proven; (G♯), (R♯) and the combined (FP♯') are hypotheses, and (G♯)'s norms were unfixed in session 14"
  (they are fixed in §33).
- §29(a): read "met EXCEPT the background independence of the constant, which fails (FP_U = FP_U(V); its locality and
  analyticity are OPEN)"; and the identity is at the Hessian (Gaussian) level.
- §30: read m_*' = 0.0384 (κ ≡ 1, r_0 = 0.70), 0.0273 (0.25, r_0 = 0.37), 0.0306 (4, r_0 = 0.90); κ̂ = 16: 0.0140, 0.0226,
  0.0216 (values rounded down so that they are valid at the stated r_0; c30 A).

## 37. Session-15 outcomes (ADDED AFTER the derivations; pointers only)
- §33 ((G♯)_0): the acceptable partial outcome is met. (G♯_0-soft) PROVEN (PROOF L5 [S15], Theorem G♯_0-soft, with
  Lemmas SRC-all, REC, KF), with G0-F1 occurring (level weights needed: Ω < ∞). (G♯_0-fine) reduced: Lemma LES-div PROVEN;
  for level-0 sources it reduces to (LED-src), OPEN; sources at levels ≥ 1 are a separate OPEN item (G♯_0-fine-up); G0-F2
  occurs, G0-F3 undecided. (G♯_0-field) not attempted. G0-F4 does not occur for the soft half.
- §34 (per-level NA): outcome (a). Proposition NA-lev: the per-level defect obeys ||Def||² ≤ 81(5L - 4)(e^{2η̄} - 1)²||A||², no
  n-loss; with Lemma E-low the per-level abelian gap holds; the (NA) gap reduces to (NA-H) (inside B-NA) and a per-block
  perturbation at n = L.
- §35 ((R♯)): stated as (R♯_ω) in the §33 norms; argued, not proven.
- §36 (c30): A PASS, B PASS, C PASS, D informational.

**[R15-fix] Annotation to §37 (added in session 16; the §37 lines above are not edited).** REVIEW_S15_CONVERGENCE fixes
2-4: read the §33 bullet as "the acceptable partial outcome is met FOR LEVEL-0 SOURCES; for sources at levels ≥ 1 the
remaining input (G♯_0-fine-up) was named but not stated precisely in session 15 (it is stated as a displayed inequality
in PROOF L5 [S15] from session 16 on)". Read the §34 bullet's "the (NA) gap reduces to (NA-H) …" as "the TOP-LEVEL
per-step defect has no n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA (E_i^{NA} is the Schur complement
over all i finer levels, whose Hessian contains a soft defect of the same type at every finer level)".

## 38. Session-16 targets: wind-down session 1 of 2 for the linear/abelian package (pre-stated 2026-10-27 20:26 UTC, after reading REVIEW_S15_CONVERGENCE and the lead's exploratory reasoning in this session, before any written session-16 derivation or check script)
Owner decision 2026-10-27 (as relayed by the session brief): finish and write up the linear/abelian package in ≤ 2
sessions, then one session costing the soft-vs-hard choice, then pause the lane. No new SU(N) obligations are opened.
- **A. REVIEW_S15_CONVERGENCE job-1 fixes 1-6**, tagged [R15-fix].
- **B. Lemma F-df_0** (PROOF L5 [S13], Corollary N2-exp-b), read as its parenthesis states it: an exponentially decaying
  kernel for the fine-curvature response f_0 = n²dB_0 as a function of the coarse curvature F on ALL coarse 2-forms
  (i.e. an extension of the map, defined on closed F, to all F), uniformly in k, T and the fine offset u, with an explicit
  rate and constant in terms of N2-exp'/N2-exp's strip (m, M). Route explored before this pre-statement (on paper): factor
  the analytic B_k-symbol of f_0 through ν∧ by an explicit analytic Koszul homotopy built from one-variable divided
  differences in the variables e^{ip_α} - 1. **Not success:** a local (near p = 0) representative only; constants depending
  on k, n, u or T; a representative that is correct only on a dense set. **Acceptable outcome if it does not fall:** the
  failing step named, F-df_0 listed OPEN in the write-up.
- **C. Check c31** (criteria file first: checks/c31_criteria.md): (E) Lemma E-low at symbol and chain level (REVIEW fix 5);
  (F) the algebraic identity of target B's representative on the actual f_0 B_k-symbol; (S) the arithmetic of the NA-lev
  smallness (η̄ ≲ 1.9·10⁻⁷) and of c_E. One job at a time; peak < 1 GB.
- **D. P/LINEAR_PACKAGE.md**: a self-contained write-up of what is proven for the linearised/abelian soft RG chain on 4D
  lattice gauge fields (setting; statements with exact hypotheses and constants; proofs or exact pointers; check inventory
  with pre-registered outcomes and failures; a "what this is not" section; open items marked paper-scale vs session-scale).

## 39. Session-16 outcomes (ADDED AFTER the derivations; pointers only)
- §38 A: fixes 1-6 applied, tagged [R15-fix] (PROOF session-16 header lists them); no status change.
- §38 B: met. Lemma F-df_0 PROVEN (PROOF L5 [S16]): explicit analytic Koszul factorisation of the f_0 B_k-symbol through
  ν∧, kernel ≤ (2M/(m_*' - m'))e^{-m'|X|_1} for every m' < m_*', uniform in k, T, u. Unreviewed.
- §38 C: c31 E PASS, F PASS (checks/c31_*.{md,py,out,time,txt}).
- §38 D: LINEAR_PACKAGE.md written (431 lines).

## 40. Session-18 target N5-triv (pre-stated 2026-10-27 22:11 UTC, after the RLARGE repair and the LINEAR_PACKAGE freeze, before any written N5 derivation)
REVIEW_S16_S17 (strategic verdict) recommends N5 at the trivial background. **Target.** For the per-level gauge-fixed soft
fluctuation operator at the trivial background (the level-i form of Proposition NA-lev (c), E_i(A) + (κ_i/2)||QA||², with
the gauge fixing δ(h)·e^{-½||P_resd*A||²} of FP-ab), an exponential bound on its covariance C_i (the inverse on the slice
H_0 = ker h), |C_i(b, b')| ≤ C_cov e^{-m_cov d(b, b')}, and the ℓ¹ bound sup_bΣ_{b'}|C_i(b, b')|e^{m''d(b,b')} ≤ C'_cov, with
C_cov, m_cov explicit in terms of the ledger's proven constants (c_E, c_1, M, m_*', κ_±, L), uniformly in i, k ≥ 1 and T.
Route explored before this pre-statement (on paper): a Combes-Thomas argument on the saddle-point operator
[[O_i, h^T], [h, 0]], with coercivity on H_0 from NA-lev (c) plus the orbit decomposition, an inf-sup bound for h, and the
exponential locality of Hess E_i from N2-exp'. **Not success:** constants depending on i, k or T; a bound for the
unconstrained operator only; a gap without decay. **Failure modes:** (N5-F1) coercivity on H_0 does not follow from the
Phys gap; (N5-F2) Hess E_i is not exponentially local in own units uniformly in i; (N5-F3) the slice constraint is not
uniformly inf-sup stable. Random-walk expansion and general backgrounds are out of scope (paper-scale, CMP 95/96/99).

## 41. Session-18 outcomes (ADDED AFTER the derivations; pointers only)
- §40: **met.** Theorem N5-triv (PROOF.md [S18], end of file; with Lemmas CT, N5-sl, N5-coer, N5-loc): exponential
  covariance and square-root bounds, N5's ℓ² and ℓ¹ bounds, constants explicit in (L, κ_±, c_E^-, c_1, M, m'), uniform in
  i, k, T. N5-F1, N5-F2 do not occur (Lemmas N5-coer, N5-loc); N5-F3 is avoided (hh^T = ||w||²·1, so the slice projector is
  block-local and no inf-sup argument is needed). Constants are tiny (γ_i ≈ 1.3·10⁻¹⁰ at κ ≡ 1, L = 3). Check c34 PASS.
  Unreviewed. Random-walk expansion and general backgrounds remain OPEN.

## 42. Session-19 targets: N5 at small-field backgrounds; the random-walk expansion; γ (pre-stated 2026-10-27 22:30 UTC, after reading PROOF.md [S18] N5-triv, NA-alg, NA-FP, NA-lev, B-NA-red, LOG session 18, REVIEW_S16_S17's strategic verdict and the lead's exploratory reasoning in this session, before any written session-19 derivation or check script)
- **Target A (N5 at a small-field background).** For the per-level gauge-fixed fluctuation operator at a background
  (U, V) (Hessian of the soft action in left-trivialised Lie coordinates, covariant slice h_U, residual Feynman term
  P_res^UD_U^*, NA-FP's notation), prove: exponential decay of C(U, V) and 𝒞 = C^{1/2} with a rate close to N5-triv's,
  N5's ℓ² and ℓ¹ bounds, and analyticity in the background on a complex neighbourhood (for RLF-5 / N10), for every
  background whose plaquette curvatures |log U_p| and soft fluctuations |ρ_c| are ≤ ε, with an explicitly stated ε
  threshold, uniformly in k and T (T ≥ a stated T_0). **Route chosen before derivation:** gauge covariance of C, local
  axial gauges on localisation boxes (curvature only), a Combes-Thomas bound for perturbed compressions (Neumann series
  around N5-triv's compressed operator), and a Dirichlet-compression random-walk expansion (target B) to glue the local
  gauges. **Expected scope (pre-registered):** the level-0 operator (top level of the fluctuation integral = Wilson
  action + one soft step), where every term is finite range and local in the background, can be done unconditionally; for
  levels i ≥ 1 the background Hessian of E_i^{NA} is (NA-H) ⊂ B-NA (OPEN), so the level-i statement will be an implication
  from a localised form of (NA-H), not counted. **Not success:** a global small-field gauge hypothesis only (it fails for
  curvature-small backgrounds on large tori); constants depending on k or T; no complex neighbourhood. **Failure modes:**
  (N5bg-F1) the slice projector Π_U is not block-local or not analytic; (N5bg-F2) compressions of the background operator
  lose the gap; (N5bg-F3) the gauge-covariance identity C_{gU} = R_gC_UR_g^{-1} fails for the soft term or the residual
  Feynman term.
- **Target B (random-walk expansion).** For an operator K with compressions K_□ (to localisation boxes Ω_□ ⊃ □) that
  obey a Combes-Thomas bound, prove K^{-1} = Σ_ω T_ω over walks ω = (□_0, …, □_n) of localised Dirichlet inverses,
  |T_ω| ≤ C ε_R^n e^{-m_1 d} with ε_R explicit and → 0 as the box size R → ∞; the same for (K + t)^{-1} uniformly in
  t ≥ 0 and for K^{-1/2}; a complex s-weakening K^{-1}(s) analytic for |s_□| < 1/ε_R, equal to K^{-1} at s ≡ 1 and
  decoupling (localised to one box) where s vanishes. Trivial background (every level i, using N5-triv) first; then the
  small-field background of target A. **Not success:** walk terms without exponential suppression in walk length; no
  square-root version. The cluster-expansion uses ((H-Mayer), (DF1)) are out of scope.
- **Target C (γ).** Look for a cheap sharper bound on γ_i (≈ 1.3·10⁻¹⁰); report proven vs measured (Bloch fibres of the
  trivial-background level-0 operator, and of the lower-bound operator 2c_E·d*d + κQ^TQ + dP_resd* that covers every i
  through Lemma E-low). A floating-point minimum over a momentum grid is a measurement, not a proof.
- **Checks (c35, criteria first):** A, SU(2) on (Z/6)⁴ (d = 4, L = 3, T = 2): gauge covariance of C, the gap and the decay
  profile of C(U) versus the background size, on a model level-0 operator (Wilson Hessian at U, κ|Q_UA|² with the
  covariant S4' linearisation Q_U in place of the full soft Hessian, the background slice and residual term), stated as a
  model in the criteria; B, random-walk truncation error versus walk length (abelian, small d, several R); C, the
  measured γ (target C). Memory peak < 1.2 GB.

## 43. Session-19 outcomes (ADDED AFTER the derivations; pointers only)
- §42 A: **met for level 0; implication for i ≥ 1.** Theorem N5-sf0 (PROOF.md [S19]; Lemmas N5-cov, AX, N5-an): curvature-only
  hypothesis, T ≥ T_0, gap/decay/ℓ²/ℓ¹/holomorphy; ε_* explicit up to the existence constants r_*, S_* (≈ 2·10⁻³²/C_Δ with
  N5-triv's constants, ≈ 2·10⁻²⁴/C_Δ with Lemma N5-w0). N5bg-F1-F3 do not occur. Levels i ≥ 1: Proposition N5-sf_i ⇐ (NA-H_loc),
  not counted. Not covered: T < T_0, explicit r_*, S_*, FP_U.
- §42 B: **met.** Theorem RW (with CT♯; Corollary RW-triv for every level at the trivial background): walks of localised
  Dirichlet inverses, ε_R^n suppression, square root, complex s-weakening with exact decoupling, locality.
- §42 C: **partly.** Rate sharpened rigorously at level 0 (Lemma N5-w0, computer-assisted: 1.9·10⁻¹⁰ vs 3.9·10⁻¹⁸); γ not
  improved rigorously; measured γ(Õ_0) = 0.0398, γ^LB = 8.14·10⁻³ = 2c_E (the loss sits in PG's c_1).
- c35 A, B, C PASS. Unreviewed.
- **[R1819-fix SF-3, W0-1; annotation added in session 20, the lines above are not edited]** §42 A reads "met for level 0,
  except that ε_* is an existence constant (r_*, S_* of Lemma N5-an not computed)": the pre-registered "explicitly stated ε
  threshold" is only partly met. The "computer-assisted" rate of §42 C was, in session 19, a double-precision numerical
  verification; c36 C (session 20) redid it in exact rational arithmetic, after which the label holds. The proven gap of
  §42 A was ≈ 7·10⁻⁸² (≈ 4·10⁻⁵¹ with N5-w0); Proposition RW-ℓ² (S20) gives ≥ γ'(1 - ε_R)/9.

## 44. Session-20 targets: localised (NA-H) at level 1 by the Schur complement; W0-1 in exact arithmetic; the ℓ² gap (pre-stated 2026-10-27 23:58 UTC, after reading REVIEW_S18_S19 (binding), PROOF.md [S18]/[S19], RTARGET §40-43, LOG session 19, LINEAR_PACKAGE.md and the lead's exploratory reasoning in this session, before any written session-20 derivation and before the c36 criteria)
- **Target A (REVIEW_S18_S19's recommended target).** For level-1 backgrounds (V, W) (V on level-1 links, W on level-2
  coarse links) whose level-1 plaquette curvatures and level-2 soft fluctuations are ≤ ε, prove: (1) a critical point
  U(V) of F(·, V) := S_W + κ_0Σ_cφ̂_c(V; M̄_c(·)) exists near an explicit lift of V, is locally unique modulo the
  fluctuation gauge, gauge covariant and holomorphic in V on a complex neighbourhood (one-level, local case of B-NA);
  (2) the Hessian of E_1^{br}(V) := F(U(V), V) is the Schur complement F_VV - F_VU C(U(V), V) F_UV with C the covariance of
  Theorem N5-sf0; (3) (NA-H_loc)_1 of Proposition N5-sf_i, with δ_H(α, m) → 0 stated through the ledger's constants and
  existence constants; (4) hence N5 at level 1. Then (5) compare the constants at level 0 and level 1 (trivial gap,
  rate, background threshold: does each shrink, and by what factor?) and (6) state the inductive form for level i with
  exactly what it needs. **Route chosen before derivation:** an exact gauge-covariant lift of V (block-interior links 1,
  boundary-crossing links = the coarse link), a contraction-mapping (Newton) step in sup norm with N5-sf0's covariance
  as the inverse, Lemma NA-crit with Lagrange multipliers to remove the fixing, implicit differentiation for the
  Schur complement, and a resolvent comparison localised by the decay of C for the background deviation.
  **Expected scope (pre-registered):** E_1^{br} is the critical-branch value; its identification with the global
  minimum E_1^{NA} (B-NA's uniqueness) is not expected; RW (v)'s finite-range locality of walk terms is not expected at
  level 1 (Hess E_1 is not finite range). **Not success:** constants depending on k or T; a hypothesis that presupposes
  (NA-H_loc)_1 itself. **Failure modes:** (NAH1-F1) the slice/residual bookkeeping (level-0 gauge modes against the level-1
  coarse gauge) is not uniformly inf-sup (REVIEW_S18_S19's pre-stated mode); (NAH1-F2) no global lift, or the Newton step
  is not uniform in T; (NAH1-F3) the Schur complement's background deviation is not local, so no δ_H → 0 uniform in T;
  (NAH1-F4) in the inductive form a threshold or constant shrinks by a fixed factor per level.
- **Target B (REVIEW_S18_S19 fix W0-1).** Redo c35 C2 (the 324 rows of Õ_0 at L = 3, κ = 1; N_0 and the first moment) in
  exact rational arithmetic on Z⁴, with the zero pattern exact; only if it confirms, relabel Lemma N5-w0's rate
  "computer-assisted (exact rational)".
- **Target C (from fix SF-2, idea noticed while reading the review, before writing).** An ℓ²-operator-norm form of Theorem
  RW (iii): under (RW1) plus the norm bound ||(K_{Ω_□} + t)^{-1}|| ≤ 1/(γ' + t), λ_min(K) ≥ γ'(1 - ε_R)/μ_𝒫^{1/2} with μ_𝒫
  the covering multiplicity of the Ω_□ (≤ 3⁴), replacing the coth⁴(m/2) loss in N5-sf0's gap.
- **Checks (c36, criteria first):** A, the exact lift (SU(2), d = 4): M̄(U^(0)(V)) = V and the plaquette pattern; B, the
  Schur-complement identity and the critical branch on a d = 2 SU(2) model (finite differences of the re-minimised
  energy against F_VV - F_VU C F_UV); C, Target B; D, measured level-1 trivial-background gap and decay of Õ_1 (exact
  H_1 by the Schur formula in Bloch form, validated against c31 E's per-mode minimum) against level 0. Memory < 1 GB.

## 45. Session-20 outcomes (ADDED AFTER the derivations; pointers only)
- §44 A: **met for level 1 (critical branch), with named gaps.** Theorem NAH1 + Corollary N5-sf1 (PROOF [S20]; Lemmas U0,
  FPq, N5-an♭, BR1, SC1, LOC). NAH1-F1, F2, F3 do not occur. Not covered: E_1^br = E_1^NA ((MIN_1)); finite-range locality
  of level-1 walk terms; explicit existence constants. (5): measured gap ×0.997, proven gap ×2c_E once, proven threshold
  ×≲10⁻⁴⁰. (6): Proposition NAH-ind; **NAH1-F4 occurs for the per-level induction** (threshold shrinks by 1 + 36p_L𝔠_∞ per
  level); uniformity needs (BG-unif).
- §44 B: **met.** c36 C PASS; Lemma N5-w0's rate is computer-assisted in exact rationals.
- §44 C: **met.** Proposition RW-ℓ² (μ_𝒫 ≤ 3⁴): gap ≥ γ'(1 - ε_R)/9.
- c36: A, C, D PASS; B FAIL as pre-registered (larger background). Unreviewed.

## 46. Session-21 targets: the one-level curvature lemma (pre-stated 2026-10-28 01:24 UTC, after reading REVIEW_S20 (binding), PROOF.md [S20], RTARGET §44-45, the c36 checks and the reviewer's kcurv diagnostic, before any written session-21 derivation and before the c37 criteria)
- **Step 1 (REVIEW_S20 binding fixes, tagged [R20-fix]):** fixes 1-8, 10-12 in PROOF.md (fix 9 is RLARGE: listed as
  "FOR RLARGE v2" in LOG session 21, RLARGE.md not edited); fix 13 optional items where cheap. Tally unchanged unless a fix
  changes it.
- **Target A (REVIEW_S20 repair route (R-a)).** Measure, then if possible prove, the per-level amplification of background
  curvature through one soft RG step. Definition (pre-registered): at the trivial background, the linearised critical
  branch maps the coarse curvature F_V (abelian, ⊗ 1 on su(N)) to the fine curvature F_1 = 𝒦F_V, 𝒦 := (1 - dC^0d^*)ι, and
  to the soft fluctuation ρ = 𝒦_ρF_V, 𝒦_ρ := -QC^0d^*ι (ι the corner embedding of Lemma U0 (ii), C^0 the trivial level-0
  covariance). K_p, K_ρ := the ℓ^∞ → ℓ^∞ (row-ℓ¹) norms of 𝒦, 𝒦_ρ; **K_curv := max(K_p, K_ρ)**. Upper bounds by row sums;
  the exact norm on exact inputs (Bianchi) by linear programming on a torus. d = 4, L = 3, κ ≡ 1 primary; SU(N) is the
  same number at linear level (⊗ 1).
  - (a) c37 (criteria first; criteria file stat'ed into LOG before the script; peak memory < 1 GB): pre-registered main
    criterion **"K_curv < 1"** at the largest torus run, with torus stability.
  - (b) If K_curv < 1: a one-level curvature lemma (curvature-to-curvature response with the non-linear remainder, in the
    sup norm the small-field classes use) replacing BR1 (iii)'s triangle inequality, and the per-level induction for
    N5-sf_i / (NA-H_loc)_i restated with a depth-independent threshold, with every remaining hypothesis named.
  - (c) If K_curv ≥ 1: (BG-unif) in REVIEW_S20's precise form via the composite contraction.
- **Expected (pre-registered guess, not a criterion):** K_p of order 1/L² to a few times that (the reviewer's d = 2 model
  gave 0.12); K_ρ of order 0.2-0.5. **Failure modes:** (CURV-F1) K_curv ≥ 1 (the row-sum bound or the exact torus norm);
  (CURV-F2) the non-linear remainder of the lemma carries a level-dependent constant, so the threshold is depth-independent
  only conditionally on uniform level-i Lipschitz constants (the C_♭^{(i)} recursion of NAH-ind); (CURV-F3) K_curv < 1
  measured but not certifiable with the proven constants (decay rate 10⁻¹⁰), so the lemma's use stays conditional on a
  certified ℓ¹ bound. **Not success:** a uniformity statement that hides the C_♭^{(i)} recursion; a measured constant
  quoted as proven.

## 47. Session-21 outcomes (ADDED AFTER the derivations; pointers only)
- Step 1: REVIEW_S20 fixes applied ([R20-fix], pointer list at the head of PROOF [S21]); fix 9 listed "FOR RLARGE v2" in
  LOG session 21 (RLARGE.md not edited). Tally unchanged, 72 / 2 / 7 / 24 + 1.
- §46 A (a): **c37 B FAIL (criterion pre-registered)**: plain row sums K_p ≈ 2.27, K_ρ ≈ 2.97 (T = 10) — CURV-F1 occurs for
  the row-sum bound. Informational: on exact inputs (Bianchi) the exact torus norms are K_p^♯ ≈ 0.06-0.08 (level 0) and
  0.10 (level 1) **[R21-fix S21-2: exact-input, small-torus lower bounds; closed-input (CURV1) value ≈ 0.11-0.13 at level 0, margin ≈ 8, not certified]**, K_ρ^♯ ≈ 2.1-2.6; attained ratios 0.015-0.084. A PASS (validation); C, D, E informational (E1 holds).
- §46 A (b): Lemma CURV1 proven with K_p(Z) in a Bianchi-adapted representative (Lemmas CURV-lin, E3; PROOF [S21]);
  Proposition NAH-unif states the depth-independent threshold ε_unif under (H-K) (measured, not certified) and (H-C)
  (level-uniform Lipschitz constants of Hess E_i^br). **CURV-F2 occurs:** (H-C) is not discharged — Lemma E3's
  absolute-value recursion compounds by Z_colZ_row² ≈ 1.3·10³ per level (c37 D2). **CURV-F3 occurs:** K_p^♯ is measured,
  not certified. §46 A (c) not attempted beyond the precise (BG-unif) statement of Step 1 (fix 12), which is where (H-C)
  now points.

## 48. Session-22 targets: (H-G) at level 1; c38 (the (H-C) artefact test); (BG-unif) by the composite route (pre-stated 2026-10-28 03:41 UTC, after reading REVIEW_S21 (binding), PROOF.md [S20]/[S21], RTARGET §46-47, LOG session 21 and SF.md lane F ((BG-unif), (N5-unif), (BG-loc)), before any written session-22 derivation and before the c38 criteria)
- **Step 1 (REVIEW_S21 binding fixes, tagged [R21-fix]):** S21-1 … S21-7 in PROOF.md (S21-7 concerns RLARGE/LOG: the stale
  LOG item is marked done; RLARGE.md is not edited, its items go to "FOR OTHER FILES" in LOG session 22). Tally 72/2/7/24 + 1
  unless a fix changes it.
- **Target A (c38, criteria first; criteria file stat'ed into LOG before the script; peak < 1 GB, jobs < 20 min).** At the
  trivial background, d = 4, L = 3, κ ≡ 1, SU(2): the cubic vertex of E_1^br(1) by Lemma E3 (tree level: the cubic part of
  the level-0 action, Wilson + soft, evaluated on the linear critical branch), as a signed translation-invariant trilinear
  kernel on coarse links, against the cubic vertex of S_W (D³S_W(1), the level-0 object in own units). Pre-registered
  quantity: the signed row norm N3 (max over one slot, ℓ¹ over the other two of the totally antisymmetric scalar kernel).
  **Prediction (pre-registered guess):** N3(E_1^br)/N3(S_W) of order 1 (not ≈ 10³), and the smooth-limit vertex ratio equal
  to the smooth-limit quadratic ratio (gauge invariance), both ≈ 1 (d = 4 classical scale invariance).
- **Target B ((H-G) at level 1).** Prove REVIEW_S21's (H-G) at level 1: at the level-1 lift of a curvature-small level-2
  field, ∇E_1^br = (the level-1 linear term in curvature form) + e_{g,1} with explicit bounds. Planned route: the envelope
  identity ∇E_1^br(V) = ∂_B F(U(V), V) (BR1 (ii): U(V) is critical without fixing) makes the gradient a local function of
  the level-0 soft fluctuation at the branch, which Lemma CURV1 (ρ part) controls; then CURV1 at level 1.
- **Target C ((BG-unif) by the composite route on a level-uniform complex polydisc).** State and prove what can be proven:
  the tower as one critical point of a composite local functional; the composite contraction; Cauchy estimates for (iv).
  Name the exact wall otherwise.
- **Failure modes.** (HG-F1) the envelope gradient carries a first-order error not controllable by box size; (HG-F2) CURV1
  at level 1 needs a level-1 LOC that NAH1 (b) does not supply; (C38-F1) the signed ratio is ≫ 1 (then (H-C) is not a norm
  artefact at level 1); (COMP-F1) the composite linear inverse is not uniformly bounded in the norm the nonlinear remainder
  needs (d = 4 marginality); (COMP-F2) per-level second-order constants still compound. **Not success:** a uniform statement
  that hides a level recursion; a measured constant quoted as proven.

## 49. Session-22 outcomes (ADDED AFTER the derivations; pointers only)
- Step 1: REVIEW_S21 fixes applied ([R21-fix], pointer list at the head of PROOF [S22]); S21-7's RLARGE items listed in
  "FOR OTHER FILES" (LOG session 22). Tally unchanged, 72 / 2 / 7 / 24 + 1.
- §48 A: **c38 B FAIL (criterion pre-registered: torus stability)**: R_3 = 1.127 (T = 4), 1.396 (T = 5), in [0.1, 10] but
  not torus-stable (post-hoc D: the ℓ¹ mass sits at coarse distance 2). C38-F1 does not occur on the accessible tori
  (signed ratio ≈ 1.1-1.4 against E3's 1267 and the absolute-leg 24-30). A PASS; C prediction met (c_3, c_2 → 1, c_3 - c_2
  = O(s²)). **[R22-fix S22-1/S22-2 (session 23): torus N3 is a periodised lower bound; R_3(ℤ⁴) ∈ [1.40, ≲ 60], ≥ 20 times
  below 1267, the signed ℤ⁴ value unmeasured (REVIEW_S22 L); C confirms the marginal direction only.]**
- §48 B: (H-G) at level 1 PROVEN (Lemmas ENV, HG1); CURV1 at level 1 (Corollary CURV1_1, with Lemma LOC_1); (H-G)_{i+1} ⇐
  CURV1_i (Lemma HG-ind). HG-F1 does not occur (the first-order error θ' is exponentially small in the box size); HG-F2
  does not occur (LOC_1 from NAH1 (b)-(c) with two changes). New: CURV-F2′ occurs (the per-level second-order constants
  compound; (H-C⁺)). **[R22-fix (session 23): HG1 needs a near/far split in CURV1_1 (S22-3b); (H-G) derived at each fixed
  level only; CURV-F2″ (θ-cascade) occurs; NAH-unif′ GAP as written (S22-5).]**
- §48 C: Lemma TOWER-VAR PROVEN; Proposition COMP an implication ((BG-unif) (i)-(ii) ⇐ (CL-0)-(CL-3)) **[R22-fix S22-6:
  GAP, (CL-4)]**; **COMP-F1 occurs** **[R22-fix S22-7: [inference]]**
  for sup-curvature norms ((CL-2): the Π_ex tail on non-closed non-linear sources); COMP-F2 = CURV-F2′ on the per-level
  route. Named: (W1), (W2), (CL-cl). (H-ℂ) OPEN (route ARGUED).
- Step 4 (optional (H-K) certification): not attempted.

## 50. Session-23 (consolidation; no new targets; pointers only)
- No derivation targets: an editing session (REVIEW_S22 binding fixes [R22-fix]; REVIEW_SF_S7-adjudicated SF edits
  [SF7-edit]; BR1 (v)'s radius [BR1v-fix]; the CROSS-LANE STATUS map). Pointer lists at the head of PROOF [S23].
- The named target is now **BFT** (REVIEW_S22 Part 5; PROOF [S23]): (BG-unif) → BFT-0, 1 (θ_w = 0), 2, 3, 4; (H-C⁺) and
  level-uniform (H-G) → BFT-4; (H-ℂ) → BFT-2; (CL-cl) → BFT-4; COMP's (CL-0)-(CL-4) → BFT-0..2's proof route in 𝔐.
- Status changes recorded (no count change): Proposition NAH-unif′ GAP as written (CURV-F2″); Proposition COMP GAP ((CL-4));
  level-0 constants on the session-23 class: 𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³, ε_* = 2.476·10⁻¹³/C_Δ (κ_0 = 1). Tally
  72 / 2 / 7 / 24 + 1.

## 51. Session-24 (lead: review discharge, integration audit, consolidation) — PRE-STATED
**Written 2026-10-28 12:15:32 UTC, before any session-24 derivation, consolidation edit or result of any session-24
worker. Statements only. Nothing here cites a session-24 result.** Session 24 is a lead session: it commissions work,
audits the target against its consumers, and consolidates. It proves no new mathematics of its own.

**Standing facts this session takes as given (recorded so that the pre-statement is checkable):** the tally entering the
session is 72 / 2 / 7 / 24 + 1; five sessions were unreviewed at handoff (HW S5, PLD S5, SQ S4, BFT A S8, FLOW S13);
REVIEW_BFT_B_S8 is written and binding; the named target is BFT-0..5.

**Lead decisions taken at the head of the session (before any worker reported), recorded as decisions, not results.**
- **D1 (one slice).** Both BFT lanes use the elliptic slice S_E. Lane A's root-funnel spikes in S_E are accepted as real
  (ARGUED via an exact identity, REVIEW_BFT_B_S8's adjudication), so (PW-i)/(GE-T) for Γ_E is false at large k and lane
  A's PW-E is empty for S_E. (NC-Γ) is to be restated for composite-co-closed sources plus a remainder bound. Lane B owns
  BFT-5. *This ratifies REVIEW_BFT_B_S8's recommendation; the decision was the lead's to make and is now made.*
- **D2 (the per-level route is closed).** Its level-uniform form is GAP (CURV-F2, CURV-F2′, CURV-F2″). The composite /
  BFT route is the single route. No further effort is to be spent repairing the per-level induction except through D3.
- **D3 (the constants are the target).** The measured one-level curvature contraction is K_p^♯ ≈ 0.11-0.13 ≈ 1/L²
  (a contraction) while the proven recursion compounds by Z_colZ_row² ≈ 1.27·10³ per level. Closing that gap, in the
  norm 𝔐 of REVIEW_S22 l.389-398 and subject to the anti-circularity constraint, is the highest-value open problem and
  is commissioned this session (NORMS.md).

**Targets (statements only; each is to be judged PASS / PARTIAL / FAIL in §52 after the fact).**
- **T51-A (review discharge).** The five outstanding hostile reviews are written by reviewers that did not write the
  sessions: REVIEW_HW_S5, REVIEW_PLD_S5, REVIEW_SQ_S4, REVIEW_BFT_A_S8, REVIEW_FLOW_S13. Each ends with binding fixes,
  an independent tally, and a verdict on its lane's headline claim. *Pre-stated expectation, to be scored honestly: at
  least two of the five will narrow, demote or refute a headline claim of the session they review.*
- **T51-B (integration audit).** INTEGRATION_AUDIT.md answers: if every clause of BFT were proven, would the chain close?
  The audit is to be scored FAIL if it finds no shortfall and PASS only if each shortfall it names is traced to a quoted
  consumer requirement and a quoted clause.
- **T51-C (the constants).** NORMS.md states a curvature-adapted norm, re-derives E3's recursion constant A in it, and
  reports the θ_w-range on which A < 1. *Pre-stated failure modes, each to be reported if it occurs:*
  - **NORM-F1:** the norm that kills Z_col is too weak for (H-C)'s consumers, so a conversion reintroduces L^{d-1}.
  - **NORM-F2:** the Bianchi restriction to closed inputs is not preserved by the blocking map, so the 2.27 → 0.12
    cancellation is unavailable at level i ≥ 1.
  - **NORM-F3:** the recursion is circular (it inverts the per-level covariances C^{(j)} as Newton inverses).
  - **NORM-F4:** A < 1 holds only at θ_w below what a consumer needs.
- **T51-D (node A).** PLD session 6 reports a status for (J-NS^cd) and for HW's (E2^𝔉), and states whether one lemma
  covers both. *Failure mode **NA-F1:** the level induction for (J-NS^cd) compounds, so the energy grading is not closed
  by induction alone.*
- **T51-E ((H-inv+)).** BFT_B session 9 reports a status for (Res-Hölder), (CO-0), (CO-up), the (NC-Γ) restatement under
  D1, and BFT-5. *Failure mode **HI-F1:** (Res-Hölder) fails in every norm pair tried, and the failure is the Π_ex tail
  already recorded as COMP-F1 rather than a new one.*
- **T51-F (honest distance).** The consolidation states the remaining work in the project's own measure
  (LINEAR_PACKAGE §10: paper-scale and session-scale tasks), not in the flat OPEN count, which REVIEW_S15_CONVERGENCE
  recorded as a counting artefact. No public text is drafted: the landing rule requires a complete and reviewed proof,
  and this session does not expect to produce one.

**Anti-inflation clause (pre-stated).** Session 24 adds no PROVEN-HERE item of its own. Any change to the tally comes
only from a review's adjudication of an earlier session, or from a worker's file, and is attributed there. If the
workers' net contribution to the main-path tally is zero, §52 says so plainly.

## 52. Session-24 outcomes against §51 (ADDED AFTER the workers reported; pointers only)
Scored honestly, including against the lead. Full detail in SESSION24_RESULTS.md; each item's mathematics is
in the owning file.

- **T51-A (review discharge): PASS.** All five reviews written by reviewers that did not write the sessions:
  REVIEW_HW_S5 (714 l.), REVIEW_PLD_S5 (561 l.), REVIEW_SQ_S4, REVIEW_BFT_A_S8 (586 l.), REVIEW_FLOW_S13
  (727 l.). The pre-stated expectation (≥ 2 of 5 narrow, demote or refute a headline) is **met**: no headline
  was refuted outright, three were narrowed, one session's reported verdicts were reversed three times, one
  session's framing was relabelled (a bestiary, not a cluster expansion), and REVIEW_BFT_A_S8 **supplied a
  proof its session lacked** (ψ_u computed exactly: φ₁ = -1/432, φ₂ = -17/104976, ratio 17/243, so (GE-T) is
  false by ≍ L^{3k} without the Coulomb stand-in). **Lead decision D1 is confirmed, on better grounds than
  the session claimed.**
- **T51-B (integration audit): PASS, and revised twice during the session.** INTEGRATION_AUDIT.md found four
  shortfalls; A1-A3 were withdrawn when REVIEW_SQ_S4 showed SQ proves θ_w = 2 natively and EPS-T + NREFL
  supply the free-boundary cone-box clause; **A1 was then reinstated on stronger grounds** by NORMS.md
  (with a single common θ_w there is no solution in (0, 2] **for anybody**, so BFT-1 needs a weight pair);
  A4 ((BB-mix), proposed as **BFT-6**) stands; **A5 ((CONST-T)) and A6 (PROOF.md's wrong Z_col diagnosis)
  were added.**
- **T51-C (the constants): PASS, with a sharper outcome than asked.** NORMS.md: the per-level route is a
  **no-go** (A ≥ 1 in every scale-covariant norm, because the d = 4 cubic vertex is marginal; the
  weight-invariance half **proven**) — so **N-F2 occurs for every per-level route** and decision D2 is
  upgraded from a judgement to a theorem. The composite route gives **A_soft = 1/L = 1/3**, uniformly in k.
  **NORM-F1, NORM-F2 (in §N6) and NORM-F3 do not occur**; NORM-F3 does not occur *by construction*.
- **T51-D (node A): PASS on reporting; 0 OPEN items closed, as the worker states plainly.** (J-NS^cd) stays
  OPEN; induction on levels does not close it. One lemma does cover both walls ((CEM^{COL})), with the
  worker's own correct label: **a consolidation, not a discharge**, since it is strictly stronger than the
  pair it replaces. **NA-F1 is half refuted: the conclusion holds, the lead's guessed mechanism (compounding)
  is wrong** — the worker *proved* the union-form excess line, so the obstruction is the **nesting** of the
  certificates. **Proposition PATCH** writes the allowance statement REVIEW_HW_S5 called "a differently-shaped
  statement nobody has written", and explains why nobody had: **NA-PRICE generates no allowance, it only
  transmits the hypothesis's.**
- **T51-E ((H-inv+)): PASS on four of five targets.** **HI-F1 does not occur.** (Res-Hölder) = EP-F4 is
  **closed at m = 0** by an identity (the forced cascade of Lemma RT-cc), not by a better estimate; (CO-0)
  and (CO-up) were **already discharged** by lane A reviews and the project's open list was stale, and (SB)
  is no longer an input; (NC-Γ) restated; BFT-5 has a statement, **(BFT-5_E)**, with clause (c) PROVEN.
  (Mult-Y) and (CovLift) not attempted. **Session 10 then proved (CO-fun) under (CC-0) and showed (GT-sup)
  is not a spike-support question**, completing **Theorem NCE: (NC-Γ) for Γ_E at every critical point of
  𝔉_k**, uniformly in k and T, for every gauge fixing.
- **T51-F (honest distance): PASS.** Stated in LINEAR_PACKAGE §10's measure, not the flat OPEN count. **No
  public text drafted**, per the landing rule.
- **Anti-inflation clause: HONOURED.** Session 24 adds no PROVEN-HERE item of its own, and the main-path
  tally is unchanged.

**Three corrections to the lead, recorded against me.**
1. **The θ_w relaxation I sent NORMS mid-run was backwards.** The composite route needs the **maximal**
   θ_w^c = 2 and does not get easier at small θ_w. The worker ignored the relaxation and was right to.
2. **Decision D3's framing conflated two problems.** The 1267-per-level factor is the origin of the
   **depth-dependence**, not of the **magnitudes**, which are dominated by 288·A_in·coth⁴(m₁/2)·ℓ_θ some
   **10³²** higher. So **g_K² is unchanged and g_0 still has to be lowered.** The uniformity problem is now
   solved at the trivial background; the magnitude problem is untouched by anything in this session.
3. **The (GT-sup) guidance I forwarded was moot.** I said the decisive question was whether the spikes sit
   where D(S) lives; lane B's own proven Lemma ΓT-op (d) bounds the transport function with an **absolute**
   constant, so (GT-sup) was never a spike-support question.

**Two cross-lane disagreements recorded and NOT adjudicated here** (for the next reviews):
(i) the price of node A's extra R-free ring — HW's **Lemma RING gives ×17** (with a proof and check w6 G6),
PLD gives **×82**; (ii) **TF-2** — HW recorded both positions and did not propagate; node A says PLD §17.2's
law already carries the finer spectators. HW session 6 agrees node A is right; the lead leaves it to review.

## 53. Session-24 follow-on wave (ADDED AFTER §52; pointers only)
After §52 was written the owner directed the session to run the reviews of session 24's own output and then
to press on the walls rather than report distance. Nineteen further worker sessions ran, for **27 in all**.
Nothing below is counted in PROOF's tally; the main-path tally is **unchanged at 72 / 2 / 7 / 24 + 1**.

**Reviews of session-24 output (4 of 8 files reviewed; 4 remain).** REVIEW_NORMS_S1, REVIEW_NQ_S1,
REVIEW_BFT_B_S9_S10, and TAUFLAT as an adjudication. **STILL UNREVIEWED: HW s6, PLD s6/s7, BFT_B s11,
CONST_T, STAR_CONST, EPSSTAR, NLOC, TENTQ, YSUP, EPS1_SWEEP, ARS_FIX, TGAUGE_PRICE, GREENT.**

**What closed, with honest labels.**
- **(N-Q) PROVEN** (NQ_CHECK, Theorem NQ-1; CONFIRMED by REVIEW_NQ_S1, which rebuilt it and added the
  argument that the identification is *forced by the consumer*).
- **(Res-Hölder) at m = 0 closed** (BFT_B §29, Theorem RHT-cc; CONFIRMED unconditional by review).
- **(CO-fun) PROVEN under (CC-0)** (BFT_B §35; the review confirmed (CC-0) is the right hypothesis, not a
  convenient one, and found no circularity).
- **The torus Hodge bound PROVEN** (NLOC, Lemma NL-1) and the **lattice Green's-function estimate PROVEN**
  with explicit R-uniform constants (GREENT), closing NL-8's hole.
- **A_cγ_c closed constant-free** (EPSSTAR, Theorem ES-1), making **C_T a number**: 5.288e12 at q = 12.
- **Σ_X Q_X = 0 with no hypothesis**, and the charge identified as a **collar flux** (TENTQ).
- **(Φ-conv) PROVEN for the |z|^{-3} profile class** (YSUP) — one flag after it was raised.

**What was REFUTED or struck, which is most of the value.**
- **The per-level no-go is NOT established** (REVIEW_NORMS_S1): its norm class is undefined and excludes
  𝔐's own Hölder leg, and **the check said to prove its weight-invariance half is a TAUTOLOGY**. The lead
  had carried it into HANDOFF as "do not relitigate"; withdrawn.
- **Theorem NCE (i) is NOT k-uniform** (REVIEW_BFT_B_S9_S10): Corollary COF-crit substitutes a per-level row
  bound for a weighted max, leaving ≈ 25(k-1). **The lead had banked the uniform form twice.**
- **(NEUT-box) is FALSE by exactly L^{2k} and struck** (TENTQ, Proposition QFALSE); route (ii)/GT-ell dies.
- **(CovLift)'s non-residual clause at θ > 0 is FALSE for every lift** (BFT_B §41, GZ-FALSE) — a currency
  mismatch; the search for a better lift is foreclosed.
- **(TENT-osc) is FALSE by exactly n²** (YSUP) and **the gauge escape is a NULL OPERATION** (TGAUGE_PRICE,
  Theorem TG-PRICE) — route (β) **CLOSED**, with the obstruction stated exactly: **the only μ that would
  work is the one Λ₀ excludes** (Proposition TG-EXCL).
- **Lever (b) on HW's ×6561 REFUTED** (HW §35, Proposition SH-neg) — the review's own suggestion, killed by
  proof, with its numerics diagnosed as an artefact of randomising position but not direction.
- **a_RS BINDS TODAY** and **RLARGE l.618 is FALSE** (EPS1_SWEEP, ARS_FIX).

**What consolidated — four items turned out to be fewer items.**
(i) **(GAP-Z) IS BFT-5's (G♯_0-field)**: the nontrivial background and BFT-5 are **one** obstruction.
(ii) **(CO-fun)'s residue is the (GE-T) refutation's functional** — not two items.
(iii) **(CEM-2) was never an ingredient** of the moment it was thought to gate (PLD §19, Theorem W-FREE).
(iv) The **HW/PLD interface** closed on one allowance form (Proposition PATCH).

**Three systemic defects, now the first thing a future session should act on.**
1. **SYMBOL COLLISIONS.** Four distinct ε_*, two θ_0, **five ε_1**, **three η_1** — and **two of the η_1 are
   different values of the same quantity in the same lemma**, flagged by a review **two cycles ago**. Three
   separate multi-decade errors today trace to this, including the 52-decade τ_♭ error.
2. **STALE MINIMA AND STALE QUANTIFIERS.** The τ_♭ defect was an item correct at the C_D it was written for,
   in a file that later made C_D an output. (E1)/(E2), (CO-0)/(CO-up)/(SB), and REVIEW_SQ_S2's θ_w
   insufficiency were all stale in the same way.
3. **CHECKS THAT CANNOT DECIDE.** Nine findings: a literal tautology; a gate built from its object's own
   primitives; an abelian model vacuous for nonabelian claims; a verdict that was the transpose of its own
   script's definition; a gate that passed on a buggy energy; clauses passing **vacuously**; and a gate
   **unsatisfiable by construction**. **"Could this check have failed, and could it have passed?" must be
   the first question of every criteria file.**

**Scoring the lead honestly: seven errors of mine were caught by my own workers**, each recorded where it
occurred — the θ_w relaxation (backwards); D3's conflation of depth-dependence with magnitude; the (GT-sup)
spike guidance (moot); the Combes-Thomas route for (N-loc) (wrong question); the "factor 2-10" and ε_* ≤ 1e-4
figures (relayed across a changed constant); banking Theorem NCE's k-uniformity twice; and repeating
"10²⁸ → ≈16" when the true price is 2.51e8. **A banked review is evidence, not a certificate** — that is the
session's main process lesson, and it applies to this file too.

---

## §54. Session 25 — pre-stated targets (written 2026-10-28T21:02:17Z, BEFORE any derivation this session)

**Owner instruction (2026-10-28):** execute, do not surface. The two items §52/§53 left as
owner decisions are hereby taken as instructed; this section records what is being attempted
and the named ways each attempt can fail, before anything is derived.

**The lead's reading of the two "decisions", stated so it can be refuted:** they are not a fork.
EPS1_SWEEP §5 calls **(C2)** *"the binding condition; everything else is bookkeeping"*, and (C2)
**is** the 82-decade adoption (ARS_FIX §4.1). So the chain is: discharge H1 → adopt KN-step' →
(C2) discharged → the ε_1 move carries only bookkeeping conditions. **If this reading is wrong the
session's whole ordering is wrong**; T55-A is spec'd to try to break it first.

### Pre-stated targets

- **T55-A (keystone).** Decide hypothesis **H1** of Lemma KN' (ARS_FIX §3.3): M̄_c must be a
  **mixture with nonnegative normalised weights**, where RLARGE l.996 says only *"M̄_c is a mean of
  the T^σ_y"*. Settle it from the **S4' definition itself**, not from the word "mean". Then, only if
  H1 holds, write the adoption patch for RLARGE §6 (η_1 := c_1ε_1, c_1 = 1/117 at d=4, L=3).
- **T55-B.** Execute the ε_1 move under (C1), (C3)-(C7); ε_1^cut ≤ 9.38495·10⁻⁴⁵, scoped to
  RLARGE §0's χ_Q threshold only.
- **T55-C.** Lane-wide **symbol audit and rename** (4 ε_*, 2 θ_0, 5 ε_1, 3 η_1). Named by §53 as a
  prerequisite for any further constant work.
- **T55-D/E.** **(N-bg)** — the structural wall — from two independent sides: its own, and BFT-5's
  (G♯_0-field), which [S24-flag] identifies as the *same* obstruction.
- **T55-F.** **T-uniformity.**
- **T55-G.** **Face (b)'s n²**: find the escape or prove none exists and price it.
- **T55-H.** Hostile review of **ARS_FIX.md** and **EPS1_SWEEP.md** — the two files being acted on.
  §53's own lesson: a banked review is evidence, not a certificate.

### Named failure modes (pre-stated, so a failure is recorded as a failure)

- **H1-F1** H1 is false, or true only for a *sub*-family of S4' contours → KN-step' is CONDITIONAL
  and the adoption does not land; the 82.141 decades are not available and (C2) must be discharged
  by its second horn (recording the 15.62/35.03-decade shortfall) instead.
- **H1-F2** H1 holds but the S4' average that makes it hold is **not** the average RLARGE §6 (R1)
  actually uses → the patch would be to a different object.
- **C2-F1** (C2) is *not* the binding condition and one of (C1), (C3)-(C7) is more than bookkeeping
  → §54's ordering above is wrong and T55-B must stop.
- **SYM-F1** A rename changes a *value* somewhere, not just a name → the audit has found a real
  defect and must stop and report it rather than rename through it.
- **NBG-F1** (N-bg) and BFT-5's (G♯_0-field) are **not** the same obstruction → [S24-flag]'s
  collapse is wrong and the obstruction count goes back up.
- **ARITH-F1** ARS_FIX's 82.141 is wrong → it was computed at today's ε_1 and 91.85 at the proposed
  one (ARS_FIX §8.6 item 2 corrects the ledger's "92"); a review must re-derive both, not re-read them.

### Anti-inflation clause (as §51, unchanged)

The lead claims **no new mathematics** this session. Every PROVEN this session is a worker's, named
with its file and section. The master tally moves only on a worker's proof, and a reversal of a
banked item is recorded against whoever banked it, the lead included.

---

## §55. Session 26 — owner decision and pre-stated targets (written 2026-10-28T22:25:45Z, BEFORE any Step 1/4/5 work)

**Lead: claude-opus-5-5.** Sessions 24-25 are PROVISIONAL (SESSION25_RESULTS.md §SWEEP55) pending the
Opus 5.5 + Codex gpt-6-astra/max review sweep now running.

**Owner decision (verbatim choice: "Fixed torus").** The target is **T_fin^OS** (PLAN_S26.md §6). T_OS on
R^4 is a labelled OPEN problem. The plan is PLAN_S26.md §4.

**Worker floor.** Claude Opus 5.5 at xhigh or max, set explicitly, model ID printed as line one and checked
by the lead; Codex gpt-6-astra at max, banner checked. Nothing banked as PROVEN without a cross-family check.

### Pre-stated targets

- **T56-1 (Step 1) — Balaban, read directly.** BALABAN_EXTRACT.md: the exact statements (norms, hypotheses,
  constants, what is uniform in k) of (a) the k-fold-constrained background field — existence, regularity,
  analyticity (CMP 102); (b) the background-field propagator bounds and their random-walk expansions
  (CMP 95, 96, 99); (c) how the induction keeps constants from compounding across steps. Read through
  legitimate open copies only; no PDF and no extracted full text enters the repository; brief quotations
  with page references only.
- **T56-4 (Step 4) — the level-count factor.** Determine from source text (not from session-24/25 summaries)
  what the ≈ 25(k−1) factor multiplies, at what field scale, and whether it is absorbed — by a
  level-dependent small-field threshold, by exponential level decay, or by asymptotic-freedom running.
- **T56-5 (Step 5) — the smallness DAG.** Every threshold and constant on the live route as a node, every
  constraint "A ≤ f(B, …)" as an edge, machine-checked for (i) cycles and (ii) dependence on K or on the
  coarse side T. Retires the decade ledgers.

### Named failure modes (pre-stated)

- **BAL-F1** a paper cannot be read legitimately for free → name it and stop; never Sci-Hub/LibGen, pay
  nothing. **BAL-F2** Balaban's k-uniformity depends on the hard constraint in a way the soft scheme cannot
  reproduce → evidence for Step 3 (decision 4), not a failure of Step 1. **BAL-F3** a load-bearing PROOF.md
  paraphrase of Balaban is wrong → list each.
- **KF-F1** the factor is not in the source text (an artefact of session-24/25 derivations) → say so and
  where it came from. **KF-F2** it multiplies a quantity of fixed size (a threshold like ε_1, not shrinking
  with k) → a genuine non-uniformity; name the minimal repair. **KF-F3** it multiplies a quantity ∝ g_k² →
  absorbed by AF only marginally (constant ∝ 1/log L): the d = 4 marginality again, to be named as such.
- **DAG-F1** a cycle exists → name every node on it. **DAG-F2** a node grows with K or T → name it.
  **DAG-F3** a node cannot be placed because its symbol names more than one object → list, do not guess.

### Anti-inflation clause (unchanged)
The lead proves no mathematics. Every PROVEN is a worker's, named with its file, and banked only after a
cross-family check.

### §55 CORRECTION (2026-10-28T22:27:10Z) — the owner's guidance is the FULL proof
The "Owner decision (verbatim choice: Fixed torus)" above is **withdrawn by the owner**: *"i choose fixed torus
only because you seem to think thats the best direction here, obtain consensus. my guidence here is for you to
get the full proof!"* **The target is T_OS on R^4.** T_fin^OS is milestone 1, not the target. T56-1, T56-4 and
T56-5 stand unchanged (every route needs them). Added:
- **T56-R4 — OS1 on R^4.** Find a route to E(4) invariance of an infinite-volume limit point that does not
  assume uniqueness or a mass gap, or establish precisely which IR input any route must supply.
  Failure modes: **R4-F1** every candidate route reduces to uniqueness of the infinite-volume state — then
  say exactly which estimate and whether it is weaker than a gap; **R4-F2** a route exists but loses RP or
  gauge invariance — name what it loses and whether it can be restored.
- **T56-C — consensus on the route.** Panellists P1-P5 (PLAN_S26.md §7), independent, both model families.
