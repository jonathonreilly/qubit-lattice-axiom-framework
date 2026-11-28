lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1071

# Check of row 1068 (gap-ir-first-astra.md), cross-provider, line by line

File under check: `library/gap-ir-first-astra.md` (written by gpt-6-astra max, row 1068).
Checker: anthropic/claude-opus-5-5, max effort, laptop subagent.

## Plan (at most eight steps)

1. Read row 1071 (and row 1068) in FINISH.md. Record the exact check brief.
2. Read the file under check in full. List its claims and its sources.
3. Read the sources it relies on inside this checkout.
4. Check the first block of claims line by line.
5. Check the second block of claims line by line.
6. Check the remaining claims; a small numeric guide only if one helps.
7. Verdict table: HOLDS / HOLDS AFTER CORRECTION / FAILS per claim.
8. RESULT line.

## Step log

(Each step appends its result below before the next step starts.)

### Step 1 result: the brief (row 1071, FINISH.md line 1152)

Checkout HEAD `aed98a99e`; the file under check was added in `ef5116c2b`
(616 lines, 39070 bytes). Its own header says it was written by Codex
gpt-6-astra max on source checkout `4fd11a783a`, and "checked by no one".

Items to check line by line (labels used below):

- K-A: the statement of V4, its identification and its consumer (its step 2).
- K-B: the unrestricted lifting (its step 3).
- K-C: Proposition 4.1 (reweighting by a bounded density h keeps every
  conditional refinement kernel), both product examples, and the
  fixed-coarse-law variant.
- K-D: the contraction uniqueness of 4.2 and its two counter-models
  (vanishing product; relevant coordinate R(x,t,r)).
- K-E: the implication 4.3 from (6) to an EXIT datum, and the CR branch.
- K-F: the controls of its step 5 (compact U(1), the 2D comparison,
  frozen groups).
- K-G: the scope of its step 6.

Judgments asked:

- J1: do the toy models refute row 1053 section 4.4 and row 1062 J4 as
  written, or only a weaker argument?
- J2: is the locality remark of 4.1 (-log h(B_{0,k}U) is nonlocal on order
  L^k fine cells) the real constraint, and does it restore the renaming once
  locality and the account's inductive hypotheses are imposed?
- J3: is "V4 plus (6) gives an EXIT datum" correct, and is (6) as hard as EXIT?

### Step 2 result: claims of the file under check, and its sources

Claims (line numbers of `gap-ir-first-astra.md`):

| Id | Lines | Claim | Mark in file |
|---|---|---|---|
| A1 | 98-99 | cited uniqueness results do not supply the V4 classification | ARGUED |
| A2 | 103-146 | V4 = (1) + IR + UV + transfer + identification; two readings of "trajectory" | definition |
| A3 | 148-155 | chain to a gap; consumer = local continuum-gap branch; HO/PHYS-SEED alternative | ARGUED |
| A4 | 157-169 | (2) on a dense set gives Spec(H) in {0} u [m,inf) | PROVED |
| A5 | 171-180 | covariance identity (3) | stated |
| A6 | 182-196 | naming g_k -> 0 is not an identification; tower (4); B Borel, discontinuous | FAILS (as identification) |
| A7 | 198-206 | normalized projectivity forgets Z(T); c(T) example | FAILS (as deduction of EXIT) |
| B1 | 215-226 | lift S_k with B_k S_k = id gives projective families for every mu_0 | PROVED |
| B2 | 228-235 | S_k checked against the three-rule B | stated |
| B3 | 237-240 | gauge-averaged lift | stated |
| B4 | 242-249 | lifted laws singular w.r.t. Wilson (interior plaquette) | FAILS (for these lifts) |
| B5 | 251-261 | face-intersection plaquette keeps coarse holonomy; no UV estimate | stated |
| B6 | 267-277 | missing constraint: mu_k in B_{k*}(D_{k+1}), compatibly | OPEN |
| C1 | 283-307 | Proposition 4.1: dmu_k = h(B_{0,k}U) dnu_k keeps the kernels | PROVED |
| C2 | 309-323 | product example (Y, Z_j uniform on [-g_j,g_j]) | example |
| C3 | 325-334 | fixed-coarse-law variant (first-layer density) | example |
| C4 | 336-351 | what the model refutes; locality remark | ARGUED |
| D1 | 355-366 | contraction on full laws + product -> 0 gives uniqueness | PROVED |
| D2 | 370-377 | strict contraction, positive product, distinct families | model |
| D3 | 378-392 | R(x,t,r): relevant t undetermined | model |
| D4 | 394-398 | Opus intuition correct under the full-law hypothesis | judgment |
| E1 | 402-415 | (6) + Wilson-tower limits give mu_k = nu_k | PROVED (implication) |
| E2 | 417-423 | (6) + unnormalised data giving E0-E4 makes an EXIT datum | implication |
| E3 | 425-430 | CR branch after identification + BDD-Delta | stated |
| E4 | 432-438 | disposition: renaming inference FAILS under reduced premises | FAILS/OPEN |
| F1 | 442-487 | free Maxwell control, (7), cos-covariance bound | PROVED (model) |
| F2 | 489-529 | O(4)/O(3) comparison | ARGUED inputs |
| F3 | 531-566 | kill-test table and four-test spec | stated |
| G1 | 568-616 | scope table and RESULT | scope |

Sources to read in step 3 (inside this checkout unless noted):
row 1053 `gap-wall-vectors-max.md` 3.5 and 4.4; row 1061
`gap-wall-vectors-check-astra.md` 4.4; row 1062 `gap-wall-vectors-check-opus.md`
J4; `parts/gap.md`; EXIT (`gap-handoff-opus.md:247-289`, row 838
`gap-assume-opus.md`); CR (`gap-compact-rigidity-max.md`,
`gap-compact-rigidity-check-astra.md:283-324`); the SA lift and map
(SA 7127, 7215-7234) and uniqueness (SA 6871, 6971-6977, 32104-32176) through
`library/sa-index/`; CA-I Theorem 4.3 (4136-4198); the kill-test sources of
its step-5 table.

### Step 3 result, part 1: sources read (row 1053, its two checks, the SA map)

Row 1053, `gap-wall-vectors-max.md` L144-146 (3.5) and L189-191 (4.4), as
written: "The coarse measure is not a free choice. The fine members must be
asymptotically free, and the irrelevant directions contract under blocking, so
the projective family is one orbit of the scale group (ARGUED; it is the
uniqueness of the account's limit along its trajectory). [...] FAILS (S0)."

Row 1062 J4, `gap-wall-vectors-check-opus.md` L128-130: the same argument,
with "they expand under refinement, so a coarse mu_0 refines to such a family
only if it lies on the renormalized trajectory", and the sentence "The argument
presumes the uniqueness of the trajectory's coarse members, which the file
states as ARGUED; nothing more is claimed."

Row 1061, `gap-wall-vectors-check-astra.md` L460-478: first unsupported line
L191 of row 1053; no theorem with those hypotheses and that conclusion is
stated or proved; SA 6871 and 32172-32176 restrict uniqueness to fixed tori.

The SA outline (Sussman and Alpoge, `YM4_sketch_500.tex` at `31a47c543775`,
32,992 lines, sha256 d7f77d4d...) and CA-I (166,711 lines, sha256 4cb5cb5e...)
were fetched by URL into the new empty folder `/tmp/opus-1071-sa.u750ao/`.
Read directly:

- SA 7127: the lift, (Q^{s*}_k V)(b) = V(c) when b_+- in B^k(c_+-); value 1 on
  every bond inside one block of order k.
- SA 7068-7073: the three rules of M. Rule 1 on Dom(c) = {varpi_c < c L^-2}:
  M(U)(c) = exp(L^-4 sum_x log W_x) U[c], W_x = U(c_-,x) U([x,x']) U(x',c_+) U[c]^-1;
  rule 2 (no Y_{x,Gamma,Gamma'} equal to -1): arithmetic mean of intrinsic logs;
  rule 3: M(U)(c) = U[c]. U[c] is the straight transport (SA 5637).
- SA 7215-7234, Proposition 1a.1.3: M is covariant, local, "Borel. Each of the
  three rules applies on a Borel set, and M is continuous on each of these sets
  but not across their boundaries", and "It is onto: M^k(Q^{s*}_k V) = V."
- SA 7129-7133: the block algebra is "a notion separate from Theorem 0 and
  Theorem 0', whose observables are the smeared curvature evaluated at the bare
  scale; neither theorem refers to A".

My own check of row 1068 L228-235 against these rules (order-1 lift S = Q^{s*}_1):
every contour path of G(y,x) stays in the block B(y), so U(y,x) = 1; a straight
segment [x,x'] has L bonds and exactly one crosses the common face, so
U([x,x']) = U[c] = V(c); hence W_x = 1 and every Y = 1. Every plaquette of the
double block is inside one block (holonomy 1) or straddles the face with its two
crossing bonds traversed in opposite senses (holonomy V(c) V(c)^-1 = 1). So
varpi_c(SV) = 0, rule 1 applies, and M(SV)(c) = V(c) for every V, whatever its
size. Rules 2 and 3 would also give V(c). Row 1068's verification HOLDS.

### Step 3 result, part 2: EXIT, CR and the consumers, as written in the lane

- EXIT, `gap-handoff-opus.md` 6.2 (L255-267): for every first-passage datum
  (K, beta_bare) with K >= K_0 and every torus T_l, l >= l_1: (E0) densities of
  block fields with integral exactly Z_bare(T_l); (E1) the last one a global Gibbs
  density (2.1) with no labels or characteristic functions; (E2) the data on T_l
  and T_(rho l) satisfy (TC) of 2.1 (small sets carry the same W_X and E_X on both
  tori); (E3) both data in a zone O_tau(alpha, m); (E4) constants independent of
  the datum. Theorem HO (L269-279) consumes (E0)-(E3) to bound the two-torus
  defect S_bare, which is built from unnormalised log Z (Identity PHI, L147-160;
  "every extensive constant cancels exactly", L162-163).
- Theorem CR, `gap-compact-rigidity-max.md` 3.6 (L241-249) and its corrected
  form, `gap-compact-rigidity-check-astra.md` item 16 (L283-324): fix one
  trajectory and one BDD-Delta bound; Omega is built from that trajectory's
  admissible torus data; PHYS-SEED iff Omega empty; empty Omega has no recurrent
  element. The objects are partition-function data Z on boxes (3.1, L131-140), not
  block measures.
- `parts/gap.md` L151 (rows 1052, 1054, 1055): the local target T_JW-lat
  (clustering of limit states, no flux clause) is weaker than (W) by the flux
  clause, "a matched local-gap target suffices given full continuum data". This is
  the consumer row 1068 L150-152 names. It HOLDS as a citation.
- `parts/gap.md` L155 (the lead's summary of row 1068) says: "PROVED as an
  implication: V4 plus full block-law identification (6) gives an EXIT datum
  (Theorem HO consumes it)". The file itself (L417-423) proves less: it needs (6)
  AND "matching unnormalised finite-cutoff data [that] additionally give the
  landing representation E0-E4". This difference is judged under J3 below.

### Step 3 result, part 3: SA uniqueness, CA-I Theorem 4.3, X-CONS

- SA 6971-6977, Theorem 0 (d) [uniqueness, g <= gamma_U]: for bare data near
  the tuned couplings, "whenever K_j -> infinity, |beta_j - beta^natural_Kj| <=
  rho/4 and x^natural_Kj(beta_j) -> x, it follows that x in I and
  S^T_{n;K_j,l,beta_j} -> S^(l,x)_n"; "On each torus, the renormalised coupling by
  itself determines the limit theory." The objects are Wilson runs and connected
  functions of the curvature observables O(f). SA 32172-32176: "It proves no
  infinite-volume uniqueness." Row 1068 L75-78 and L182-185 read this correctly.
- SA 31858-31869: the scalar action-density sector "alone [does not identify] a
  full Yang--Mills observable algebra". Row 1068 L125-127 reads this correctly.
- CA-I 4136-4198, Theorem 4.3 (Balaban's one-step small-field theorem, cited by
  statement, CMP 109 Theorem 3): for "any family of effective actions" with
  Balaban's inductive properties, the fluctuation integral "produces an effective
  action E^(k+1) with the same properties and the same constants". This is forward
  preservation of a class. It states no bound on the difference of two members and
  no inverse statement. Row 1068 L129-138 reads this correctly.
- PR 10114 (`f76f6c64`, present in this clone), `EXISTENCE.md` L345-396: X-CONS
  uses the continuous extension S4c; with the discontinuous rule, consistency of
  limit block laws can fail "exactly on nu_{*,m+1}(Disc A) > 0". Row 1068 L60 and
  L192-195 read this correctly.

### Step 4 result: K-A (its step 2) and K-B (its step 3), line by line

**A1, L98-99 (source scope).** HOLDS. SA Theorem 0 (d) quantifies over Wilson
runs near the tuned couplings and over curvature correlations (step 3, part 3).
No cited passage quantifies over arbitrary projective families.

**A2, L103-146 (V4 stated).** HOLDS AFTER CORRECTION (wording of the UV clause).
(1) and the four requirements are well posed. One reading needs a fix. Read with
"cluster expansion" in the sense of the lane's landing zones (strong coupling),
clause 1 and clause 2 cannot both hold with "all finer laws" meaning every
k >= 1. A law with Balaban's coupling ceiling at depth 1 has small plaquettes
with high probability; one averaging multiplies curvature by at most
L^2 varpi + C (L^2 varpi)^2 (SA Proposition 1a.1.4, L7237-7243); so mu_0 is a
small-field law, not a strong-coupling one. The account's run moves x by about
c_0 = (11 N^2/(12 pi^2)) log L per step (SA L6871), so many steps lie between
the two domains. ARGUED (it uses the plaquette mean of a zone law, not written
out here). Corrected text for L116: "2. **UV:** every law mu_k with k >= K_1,
for one fixed K_1, has [...]; the depths 1 <= k < K_1 carry no domain
condition." With the "mixing bound" reading, clause 1 is consistent as written,
but it is then itself a gap statement for the block law at a_0. The correction
changes no conclusion of row 1068: a uniqueness proof on the depths k >= K_1
fixes mu_0 by push-forward.
L129-138 (CA-I Theorem 4.3 is forward only; CA-I 49495-49511 separates
background admission from the operator theorem): HOLDS (read in step 3).
L140-146 (two readings of "the account's trajectory"): HOLDS. This is the key
logical point: if formation from the Wilson runs is part of the hypothesis, no
classification of other laws is being claimed.

**A3, L148-155 (chain and consumer).** HOLDS as a conditional chain. Note: its
first arrow is definitional, because requirement 3 already contains decay on a
dense set with a common exponent. The IR clause enters only through requirement
3, and the file says so (L168-169, L176-180). The consumer citation matches
`parts/gap.md` L151 (rows 1052-1055: "a matched local-gap target suffices given
full continuum data"). The seed-engine alternative matches `gap-handoff-opus.md`
6.3.

**A4, L157-169 (spectral implication).** HOLDS, PROVED. Check:
<v, e^(-tH) v> >= e^(-rt) ||1_[0,r](H) v||^2, so ||1_[0,r](H)v||^2 <=
C_v e^(-(m-r)t) -> 0; 1_[0,r](H) -> 1_[0,m)(H) strongly as r increases to m; a
bounded operator zero on a dense subset of the vacuum complement is zero there;
the complement is H-invariant since H Omega = 0. Uniqueness of the vacuum is not
even needed for the inclusion of the spectrum. Formalizable in measure and
spectral terms.

**A5, L171-180 (identity (3)).** HOLDS (law of total covariance).

**A6, L182-196.** HOLDS. SA 0(d) is about W_{N,T}(beta_N); (4) is projective in
k for each N (finite algebra); B is Borel and discontinuous across rule
boundaries (SA L7224); X-CONS uses S4c (step 3, part 3).

**A7, L198-206 (normalized laws forget Z(T)).** HOLDS. Theorem HO needs the
unnormalised defect (Identity PHI uses log Z on two tori; (TC) fixes the
constants E_X of small sets). Replacing Z(T) by c(T) Z(T) leaves (1) and every
normalized correlation unchanged and shifts the defect by
rho^4 log c(T_n) - log c(T_(rho n)). Wording: "the actual bare masses" (L204)
means the total masses Z_bare(T) of E0; there are no bare mass parameters in
pure SU(2).

**B1, L215-226 (unrestricted lifting).** HOLDS, PROVED. With S_k the order-one
lift, B_k S_k = id (SA L7226, "It is onto"); the displayed integral identity
gives (1); V -> (V, S_0 V, S_1 S_0 V, ...) is Borel into the countable product.
No compactness or selection is used. This is SA's configuration-level result
plus push-forwards, as the file says (L228, L574).

**B2, L228-235 (section against the three rules).** HOLDS; my independent check
is in step 3, part 1 (varpi_c(SV) = 0, so rule 1 applies and gives V(c)).

**B3, L237-240 (gauge-averaged lift).** HOLDS. With rho = average over fine gauge
u of (tau_u S_k)_* mu_k, covariance M(U^u) = M(U)^{u|coarse} (SA L7218)
gives B_* rho = average of (tau_{u|coarse})_* mu_k = mu_k when mu_k is gauge
invariant.

**B4, L242-249 (singularity of the lifts).** HOLDS. For L >= 3 (L is odd) a block
holds an elementary plaquette; its holonomy under S_k is 1, also after gauge
averaging (conjugation fixes 1). A Wilson law at finite beta is absolutely
continuous w.r.t. Haar, and {U_p = 1} is Haar-null (fix three links; the fourth
is then one point of SU(2)). So the lifted law is singular w.r.t. Wilson.

**B5, L251-261 (face-intersection plaquette).** HOLDS. A fine plaquette in the
(mu,nu) plane with its four corners in the four blocks around a coarse
plaquette has four crossing bonds carrying the four coarse links, so its
holonomy is V_p. Repeating the section keeps one such plaquette p_k at every
depth, with Pr(||U_(p_k) - 1|| > delta) = c. So no bound
sup_p Pr(||U_p - 1|| > eps_k) -> 0 with eps_k -> 0 holds for these lifts.
The scope sentence L263-265 is correct: this is about the explicit section only.

**B6, L267-277 (the missing constraint).** HOLDS. The question is membership of
mu_k in B_{k*}(D_(k+1)), compatibly at all depths. Nonempty finite-depth sets do
not give an infinite tower without closedness and continuity (an inverse limit
of nonempty compact sets under continuous maps is nonempty; without these it can
be empty). No such argument is claimed.

### Step 5 result: K-C (4.1 and the product examples) and K-D (4.2 and its models)

**C1, L283-307 (Proposition 4.1).** HOLDS, PROVED, on its stated premise (a
reference projective family nu is given; such families exist by B1).
Line checks:
- Normalisation: integral of h(B_{0,k}U) dnu_k = integral of h d(B_{0,k*}nu_k) =
  integral of h dnu_0 = 1.
- Projectivity: B_{0,k+1} = B_{0,k} o B_k, so the integrand of L292 is F(B_k U)
  with F(V) = f(V) h(B_{0,k}V), and projectivity of nu gives L293.
- Kernels: X_k = SU(2)^(finite) is compact metrizable, hence standard Borel, so
  a regular conditional law K_{j,k}(V,.) of nu_k given B_{j,k}U = V exists and
  can be taken carried by the fibre {B_{j,k}U = V}. On that fibre
  h(B_{0,k}U) = h(B_{0,j}V), which gives L299, i.e. mu_k = integral of mu_j(dV)
  K_{j,k}(V,.). Since c <= dmu_j/dnu_j <= C, "nu_j-a.e." and "mu_j-a.e." agree,
  so fibrewise bounds transfer exactly.
- c nu_k(A) <= mu_k(A) <= C nu_k(A): immediate.
- Gauge invariance: B_{0,k}(U^u) = (B_{0,k}U)^(u|coarse) (SA L7218), so a gauge
  invariant h gives a gauge invariant mu_k.

**C2, L309-323 (product example).** HOLDS, every line. E_mu Y = E[(1 + eps Y) Y]
= eps; the density lies in [1 - |eps|, 1 + |eps|]; the product over sites is
positive and normalised on each finite torus (not volume-uniform, as L322-323
says); both coarse laws are products, hence clustered; j g_j^2 = j/(H + c_0 j)
-> 1/c_0. The scope sentence L320-322 (a prescribed schedule, not a computed
beta function) is correct.

**C3, L325-334 (fixed coarse law).** HOLDS, every line. X_0 records Y alone, so
a change of the Z_1 law leaves mu_0 fixed. Integral of (1 + eps z/g_1)/(2 g_1)
over [-g_1, g_1] is 1 (the odd part integrates to 0); the density is at least
(1 - |eps|)/(2 g_1) > 0; E Z_1 = (eps/(2 g_1^2)) (2 g_1^3/3) = eps g_1/3.
|Z_1| <= g_1 still holds. Two values of eps give two projective families with
one coarse law.

**C4, L336-351 (what the models refute; locality).** HOLDS, with one precision.
The product model cannot see locality at all: its coarse variable Y is itself a
fine coordinate at every depth, so h(Y) is a one-site term at every depth. In
the SU(2) case B_{0,k}U depends on blocks of L^(4k) fine links, so
-log h(B_{0,k}U), written as given, is a sum of terms of diameter of order L^k
in level-k units. With an activity of size a on such a term and a weight
exp(kappa d), the norm is a exp(kappa L^k) up to constants, unbounded in k
(L346-348). The same holds for the SU(2) analogue of C3: a level-1 density w
with conditional mean 1 given level 0 becomes -log w(B_{1,k}U) at depth k, of
diameter of order L^(k-1). The file is right that this shows only that the
displayed representation fails; no proof that every local representation
fails is given or claimed (L348-350). See J2 below.

**D1, L355-366 (backward contraction).** HOLDS AFTER CORRECTION (one implicit
premise). The iteration d_k(mu_k,nu_k) <= (prod_{j=k}^{N-1} q_j) d_N(mu_N,nu_N)
uses the contraction at every step j = k, ..., N-1, so both families must lie
in D_j for every j >= k. Corrected text for L360: "For two projective families
with mu_j, nu_j in D_j for every j, suppose d_N(mu_N,nu_N) <= M_N and [...]".
With that, d_k(mu_k,nu_k) = 0 for every k, and uniform q_j <= q < 1 with
bounded M_N suffices. PROVED; formalizable.

**D2, L370-377 (strict contraction, positive product).** HOLDS, every line.
B_k x_{k+1} = exp(-2^(-k-1)) a exp(1 - 2^(-k-1)) = a exp(1 - 2^(-k)) = x_k;
|x_k| < e|a| <= delta; prod_{j=k}^{N-1} q_j = exp(-(2^(-k) - 2^(-N))) ->
exp(-2^(-k)) > 0; Dirac laws with distance |x - y| contract by q_k. Here
q_k -> 1, which no uniform irrelevant contraction does; the model shows only
that "strict at each step" is not the needed hypothesis.

**D3, L378-392 (relevant coordinate).** HOLDS, every line.
R(x_{k+1}, t_{k+1}, r_{k+1}) = (H + k, L^2 t_0 L^(-2k-2), 0) = (x_k, t_k, r_k);
bounded families force r = 0 (r_k = q^(N-k) r_N); t_0 in [0, delta] is free;
g_k = x_k^(-1/2) -> 0 for every t_0. The quantity t_0 L^(2H) is constant on a
scale orbit (H, t_0) -> (H + 1, t_0 L^(-2)), so distinct values give distinct
orbits: the model meets both premises named in row 1053 L191 and fails its
conclusion "one orbit". Note: in R every bounded family still lies on the
unstable manifold {r = 0}, which is two-dimensional. So R refutes "one orbit",
not "mu_0 must lie on the renormalized trajectory" when that trajectory is
read as the whole unstable manifold. The file's own scope (L388-392: gauge
invariance forbids a scalar mass term; the model does not refute a supplied
completeness theorem) is correct.

**D4, L394-398.** HOLDS. The backward-expansion argument is valid under D1's
full-law hypotheses; the cited passages state no such estimate.

### Step 6 result: K-E (4.3), K-F (its step 5), K-G (its step 6)

**E1, L402-415 ((6) gives block-law identification).** HOLDS, PROVED. By (1),
the first integral of (6) is mu_{k,T}(f) for every N >= k; so (6) says
nu_{N,k,T}(f) -> mu_{k,T}(f). The limit functional is positive and normalised,
hence a probability by Riesz; continuous functions separate probabilities on the
compact X_k(T); so mu_{k,T} = nu_{k,T}. No Borel map passes a weak limit: B
acts at finite N inside the integrals. Note: the first hypothesis (the Wilson
tower has limits) is implied by (6) itself, so it can be dropped. "SA CP9"
(L414) is SA L32124-32134, a comparison requirement the SA index marks "named
open"; the file's reading of it is correct.

**E2, L417-423 ((6) and an EXIT datum).** HOLDS as written, but it carries no
content beyond its added hypothesis. EXIT (step 3, part 2) is a statement about
the account's finite-cutoff data for every K >= K_0. Under (6) those data are
the Wilson tower's. So "(6) and matching unnormalised finite-cutoff data
additionally give the landing representation E0-E4" assumes E0-E4 for the
account's own data, which is EXIT. V4 plus (6) alone gives none of E0 (exact
mass Z_bare), E1 (a finite-cutoff global Gibbs density), E2 ((TC)) or E4
(uniformity in K): it gives a weak limit of normalised laws, and weak
convergence does not put finite-cutoff Gibbs data in an open zone of the
landing norm. The converse sentence (L421-423) HOLDS: EXIT gives finitely many
landed steps per cutoff, not a projective family.
Corrected text for L417-420: "V4 plus (6) identifies every block law with the
limit of the Wilson block laws. It does not supply E0, E1, E2 or E4. If the
account's finite-cutoff data satisfy E0-E4, that is EXIT itself, and Theorem HO
consumes it; the V4 datum adds nothing to that hypothesis."
The lead's summary in `parts/gap.md` L155 ("V4 plus full block-law
identification (6) gives an EXIT datum (Theorem HO consumes it)") FAILS as a
report of this file: it drops the E0-E4 clause. Corrected text: "PROVED as an
implication: V4 plus (6) identifies the family with the limit of the Wilson
block laws; an EXIT datum needs E0-E4 for the account's finite-cutoff data in
addition, and the converse is not proved."

**E3, L425-430 (CR branch).** HOLDS. The corrected Theorem CR fixes one
trajectory and one BDD-Delta bound; PHYS-SEED iff Omega empty; an empty Omega
has no recurrent element (`gap-compact-rigidity-check-astra.md` L283-311). A
local clustered state is not shown to give PHYS-SEED (`parts/gap.md` L151: the
local target is weaker than (W) by the flux clause). Scoped as "not
established", which is right.

**E4, L432-438 (disposition).** HOLDS. The negative is scoped to "the reduced
premises"; the full-UV classification is OPEN; no SU(2) family and no
impossibility are claimed.

**F1, L442-487 (compact U(1), free Maxwell control).** HOLDS, PROVED for the
free Gaussian model. My re-derivation: <F_12(x) F_12(0)> = -(d_1^2 + d_2^2) D(x),
D = 1/(4 pi^2 |x|^2); d_i^2 |x|^-2 = -2|x|^-4 + 8 x_i^2 |x|^-6, so at x = t e_4
the value is 4 t^-4/(4 pi^2) = 1/(pi^2 t^4), which is (7). Away from 0 the kernel
is pi^-2 (|x|^-4 - 2(x_1^2 + x_2^2)|x|^-6), with gradient O(|x|^-5), so
C(t) = pi^-2 t^-4 (integral phi)^2 + O(t^-5). For centred jointly Gaussian
X, Y with variance v and covariance C, E cos X cos Y = e^-v cosh C and
E cos X = e^(-v/2), so Cov = e^-v (cosh C - 1) >= e^-v C^2/2, at least c t^-8
for large t. Precision: the variance v is finite because the Fourier multiplier
(k_1^2 + k_2^2)/|k|^2 is bounded, not because the pointwise kernel is
absolutely integrable (it is not, at coincident points); the file states v
finite without this reason. The scope lines L479-487 (no claim that nonlinear B is its
linearization; Guth and Frohlich-Spencer as cited inputs; none of (1), (5) or
the lifts gives U(1) a gap, since they are group-blind) HOLD.

**F2, L489-529 (two-dimensional comparison).** HOLDS as a reading, with one
item not re-verified here. Credit: OpenAI, `openai/math` at `4eaee875`. The O(3)
statements (Proposition 8.1 with v/2 < chi < min(1, eta/(2 pi)), Proposition
8.3, Corollary 8.5, pp. 69-74) match the lane's Opus reading
`prior/gap-o3-continuum-rg-read-opus.md` L142-167. The O(4) statements
(Proposition 2.2: Delta(2n) <= 64 Delta(n)^2 from Delta <= 2^-10, gap at least
(log 2)/n; Theorem 3.1 at every beta with Xi(beta) = exp(pi beta + C sqrt((1 +
beta) log(2 + beta)))) match `prior/gap-o4-pinned-cell-read-opus.md` L28-33,
L76 and its table row 17. Not re-verified: the side condition "n >= 4 even" and
the claim that (2) is the argument at the end of Proposition 2.2 (the paper was
fetched to `/tmp/opus-1071-o4.z0Gsxu/`, sha256 e87f407d..., but no PDF renderer
is installed here). The architecture verdict (L515-519: an actual measure
supplies the seed at a reference depth; comparison carries it; the 2D proofs
do not choose a clustered law and identify its refinements) HOLDS against the
O(3) reading L61.

**F3, L531-566 (frozen groups and kill tests).** HOLDS. Every cited range holds
the named result: PT (`gap-crux-exercise3-max.md` L690), NP
(`gap-crux-exercise4-max.md` L383-413), D2 and its Fourier repair
(`gap-tiltproof-check-astra.md` L152-159: A^(-1/2) at the self-inverse
momenta), SHEET and its general-group repair (`gap-sepinput-check-astra.md`
L197-208), CEN+ (`gap-global-reform-max.md` L446-452), WN
(`gap-invent-selective-max.md` L136-142), the flat triples (1,1,1), (i,1,1)
(`gap-crux-exercise2-check-astra.md` L235), the five-dimensional test and K9
(`gap-invent-selective-max.md` L52-65). Wording: K9 records (S2) as "a rate";
the file's "S2, scale control" (L555-557) should read "S2, a rate: the product
condition of 4.2 or the comparison (6) is the rate; it is OPEN". No verdict
changes.

**G1, L568-616 (scope).** HOLDS. The three-way table separates what is proved
(lifting), what fails (the reduced-premise inferences, in models outside SU(2))
and what is open (full-UV classification or its negation). The stopping
condition met is a gap model for the classification argument, not a gauge
model; the file says so (L575, L610-614). Cosmetic: the file's first heading is
"# Repo search", not the row's name.

### Step 7 result: the three judgments and the verdict table

**J1. Do the models refute row 1053 4.4 and row 1062 J4 as written?**
They refute both texts as inferences from the premises those texts state, and
only because those premises leave out two hypotheses the intended RG argument
needs. They do not refute the intended argument.

- Row 1053 L191 names two premises (fine members asymptotically free; the
  irrelevant directions contract under blocking) and concludes "one orbit of
  the scale group". D3 meets both named premises and has a free parameter
  t_0 L^(2H) across orbits, so the written inference fails. D3 needs a relevant
  coordinate. The inductive class as cited in CA-I Theorem 4.3 carries one
  running coefficient, the coupling increment beta_j (fourth bullet), with the
  vacuum constants carried apart; that pure SU(2) has no other non-irrelevant
  local term is the standard power count (gauge invariance, hypercubic
  symmetry), RECALLED here, not checked. With that completeness added, D3 is not
  a counterexample (the file says so, L388-392).
- C2, C3 and Proposition 4.1 refute a weaker inference: fibrewise UV bounds, a
  vanishing running schedule and projectivity. Rows 1053 and 1062 spoke of
  contracting directions of effective actions, which presumes a local
  coordinate system; the reweighted SU(2) families sit outside it (C4). So
  these models refute a weaker argument than the one intended.
- D2 refutes "strict contraction at each step suffices"; neither row claimed it.
- Row 1062 J4 itself names the missing premise ("presumes the uniqueness of
  the trajectory's coarse members"). Its error is the verdict word: HOLDS was
  given to an inference whose key premise it marked as presumed. Row 1061's
  correction (renaming not established) stands. Row 1068's disposition
  ("FAILS under the reduced premises", L432-433) is correctly scoped. Reading it
  as "V4 is not a renaming" would be wrong; that is OPEN.

**J2. Is locality the real constraint, and does it restore the renaming?**
Locality is the real constraint on the record, in this sense: Proposition 4.1
keeps every fibrewise clause exactly and every event-probability clause up to
the factor C/c, and changes the fine effective action only by
-log h(B_{0,k}U), which as given is a term of diameter of order L^k in level-k
units. The account's inductive class has depth-independent constants (CA-I
Theorem 4.3: "the same properties and the same constants"), so that
representation leaves the class as k grows. Two qualifications: no proof is
given that no other representation is in the class (the file says so,
L348-350); and the other UV clauses (large-field histories, background
admission) are not checked for the reweighted family.
Imposing locality and the inductive hypotheses does **not** restore the
renaming on the record. That needs the full-UV classification the file leaves
OPEN (L433-436): a bound that contracts the difference of two members of the
inductive class in a metric on full laws, large fields included, with the
coupling calibration matched and the vacuum constant quotiented, as in D1.
CA-I Theorem 4.3 is forward preservation for one family and bounds no
difference. The comparisons read here (SA 0(d), SA L6871's side-by-side runs,
CP8-CP9 through the index) compare Wilson runs, not arbitrary class members. No
model of row 1068 lies in the inductive class, so none bears on that
classification. If it were proved, and the Wilson limit tower lay in the class
at depths k >= K_1 with the same calibration, every V4 family would be that
tower, and V4 would rename the trajectory's IR statement in limit-law form
(not literal EXIT; see J3). Verdict on the remark: HOLDS AFTER CORRECTION.
Corrected text for L341-342: "Relative to nu_k the new action is changed by
-log h(B_{0,k}U); in this representation it is nonlocal on order L^k fine
cells and leaves the account's inductive class. Locality in that class is the
constraint the conditional-kernel calculation does not see. Imposing it does
not by itself restore uniqueness: that needs a difference contraction on full
laws in the class, which is OPEN."

**J3. Does V4 plus (6) give an EXIT datum, and is (6) as hard as EXIT?**
- "V4 plus (6) gives an EXIT datum", as `parts/gap.md` L155 states it: FAILS.
  First failing clause: "gives an EXIT datum". V4 plus (6) gives block-law
  identification (E1) and nothing of E0, the finite-cutoff part of E1, E2 or
  E4 (step 6, E2; A7's c(T) example). As the file states it (with E0-E4 added
  for the finite-cutoff data): HOLDS but empty, since the added clause is EXIT
  for the account's data.
- (6) alone has no infrared content. It asks that the Wilson block laws
  converge at every fixed depth and torus to the family's members: a UV and
  identification statement, OPEN, with the discontinuity of B as an extra
  issue (X-CONS's S4c remark). It is not shown to be as hard as EXIT. But (6)
  removes the free choice of mu_0: by E1 the family is the Wilson limit tower.
  So V4 with matching defined by (6) is equivalent to: that tower exists, is
  projective and UV-admitted, its coarse member meets clause 1, and clause 3
  holds for it. On a fixed torus X_0(T) is finite-dimensional, so the coarse
  limit follows from a fine one wherever B_{0,k} is continuous almost surely;
  the uniformity in T sits in clause 1. Clause 1 is then the
  trajectory's own IR statement (a strong-coupling landing in limit-law form,
  or the block-law gap itself under the mixing reading). So with (6), V4 is a
  renaming of an open IR statement about the account's trajectory, plus the UV
  obligation (6). It is not literal EXIT.

**Verdict table** (file `library/gap-ir-first-astra.md`, row 1068):

| Item | Lines | Verdict |
|---|---|---|
| A1 source scope | 98-99 | HOLDS |
| A2 V4 stated | 103-146 | HOLDS AFTER CORRECTION (UV clause from a depth K_1; text in step 4) |
| A3 chain, consumer | 148-155 | HOLDS (conditional; first arrow definitional) |
| A4 spectral implication | 157-169 | HOLDS (PROVED) |
| A5 identity (3) | 171-180 | HOLDS |
| A6 not an identification | 182-196 | HOLDS |
| A7 normalisation | 198-206 | HOLDS (wording: "bare masses" = Z_bare) |
| B1 unrestricted lifting | 215-226 | HOLDS (PROVED) |
| B2 section vs three rules | 228-235 | HOLDS (re-derived) |
| B3 gauge-averaged lift | 237-240 | HOLDS |
| B4 lifts singular to Wilson | 242-249 | HOLDS |
| B5 face plaquette diagnostic | 251-261 | HOLDS |
| B6 missing constraint | 267-277 | HOLDS |
| C1 Proposition 4.1 | 283-307 | HOLDS (PROVED) |
| C2 product example | 309-323 | HOLDS |
| C3 fixed-coarse-law variant | 325-334 | HOLDS |
| C4 scope and locality remark | 336-351 | HOLDS AFTER CORRECTION (J2 text) |
| D1 backward contraction | 355-366 | HOLDS AFTER CORRECTION (both families in D_j; text in step 5) |
| D2 positive product model | 370-377 | HOLDS |
| D3 relevant-coordinate model | 378-392 | HOLDS (refutes "one orbit", not "on the unstable manifold") |
| D4 Opus intuition | 394-398 | HOLDS |
| E1 (6) gives identification | 402-415 | HOLDS (PROVED; first hypothesis redundant) |
| E2 EXIT datum | 417-423 | HOLDS AFTER CORRECTION (empty as written; text in step 6) |
| E3 CR branch | 425-430 | HOLDS |
| E4 disposition | 432-438 | HOLDS |
| F1 free Maxwell control | 442-487 | HOLDS (PROVED; v finite by the Fourier multiplier) |
| F2 2D comparison | 489-529 | HOLDS as a reading; "n >= 4 even" not re-verified |
| F3 kill tests, frozen groups | 531-566 | HOLDS (wording: S2 = a rate) |
| G1 scope | 568-616 | HOLDS |
| `parts/gap.md` L155 (lead summary) | - | FAILS at "gives an EXIT datum"; corrected text in step 6 |

No line of the file under check FAILS. No mass gap is claimed by it or here.

### Step 8 result: provenance, what was not covered, RESULT

Provenance. Written by Claude Opus 5.5 (max effort), a laptop subagent of the
lead session. The file under check is by gpt-6-astra max (another provider).
Re-derived here by a separate computation, not only read: the section against
SA's three rules (B2), the face-plaquette and interior-plaquette facts (B4,
B5), the integrals of C2 and C3, the algebra of D2 and D3, the free Maxwell
kernel and the cosine covariance (F1), and the spectral implication (A4).
Read only: the citations of the kill-test table, the 2D readings, CR and EXIT.
This is a research check, not an audit; no status is granted.

Not covered: the file's step-1 table beyond X-CONS (PR 10114 `SOFTHARD.md` and
`CODEX_REVIEW_SEAM.md` not read); CA-I L2828-2908 and L3249-3305 not re-read;
the O(4) paper's "n >= 4 even" and the end of its Proposition 2.2 not
re-verified (no PDF renderer); no Lean formalization by anyone. Downloads:
`/tmp/opus-1071-sa.u750ao/` (SA outline and CA-I) and `/tmp/opus-1071-o4.z0Gsxu/`
(the O(4) paper); none is committed.

Credit: Ethan Sussman and Levent Alpoge (the outline and the complete account,
written with Claude and Codex); Tadeusz Balaban (the renormalization methods,
CMP 109 Theorem 3 as cited in CA-I Theorem 4.3); OpenAI (the posted O(3) and
O(4) papers); Guth and Frohlich-Spencer (the U(1) Coulomb phase, cited).

RESULT: Row 1071 (Claude Opus 5.5 max, laptop subagent; cross-provider check of row 1068 by gpt-6-astra max; research check, not an audit): no line of `gap-ir-first-astra.md` FAILS; HOLDS: unrestricted lifting and its section (re-derived against SA's three rules), the singularity and face-plaquette diagnostics, Proposition 4.1 with both product examples and the fixed-coarse-law variant, the two contraction counter-models, the (6) identification, the CR branch, the free-Maxwell U(1) control (re-derived), the kill tests and the step-6 scope; HOLDS AFTER CORRECTION: V4's UV clause (from a depth K_1), the contraction lemma (both families admitted at every depth), the locality remark (it does not restore uniqueness by itself), and the EXIT implication (empty as written: its added E0-E4 clause is EXIT); J1: the models refute row 1053 L191 and row 1062 J4 only as written inferences, through omitted locality and coordinate-completeness premises, not the intended RG argument; J2: locality is the constraint the reweighted family visibly fails, and imposing it restores the renaming only given an OPEN difference contraction on full laws in the inductive class; J3: "V4 plus (6) gives an EXIT datum" in `parts/gap.md` L155 FAILS (no E0, finite-cutoff E1, E2 or E4); (6) has no infrared content, but under (6) V4 renames the trajectory's open infrared statement in limit-law form; no mass gap claimed.
