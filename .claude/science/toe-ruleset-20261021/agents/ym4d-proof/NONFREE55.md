Reviewer model: claude-opus-5-5

# NONFREE55 — what "not free" must mean for the 4D SU(N) YM limit, and a witness that works against every identification

## PRE-STATED (written 2026-10-29T04:24Z, before any derivation)

Worker: Opus 5.5 (claude-opus-5-5), task brief `scratchpad/queue/nonfree.md`; rules `scratchpad/REVIEW_BRIEF_55.md`.
Writes only this file and `checks/nf55_*`. No git.

Targets (statements only):

- **T1 (definition).** State an intrinsic property of the reconstructed OS data of the limit theory
  ("NOT FREE") that does not depend on which field anyone labels "basic"; give at least two versions
  (a strong one: no unitary/OS equivalence to any member of a named free class — generalized free fields,
  free Maxwell with N^2-1 colours, finite tensor products / mixtures of these; a weaker standard one:
  the Schwinger functions of the generating local gauge-invariant fields are not those of a quasi-free
  state), say which version the owner's target T_OS should carry and why, and compare with what the
  constructive literature states for phi^4_3 / Y_2 (cited from the open corpus where located, else [m]).
- **T2 (witness).** Test at least the three named candidates: (a) logarithmic violation of exact scaling
  for a fixed observable; (b) the trace anomaly / energy-momentum tensor; (c) an OS-intrinsic Gaussianity
  test independent of field labelling. For each: a proved free-side statement (vanishes / excluded on the
  whole free class, under every identification) or an explicit counterexample showing it is not; and the
  exact Yang-Mills-side inequality the RG must deliver, as named inputs with statuses.
- **T3 (algebra).** The witness must be built on the observable algebra on which OS0-OS3 are produced
  (clover energy density e_a, smeared / separated Schwinger distributions, per ASSEMBLY55 F1/F2a), and be a
  function of the reconstructed OS theory; or else the flowed algebra must be shown to be generated inside
  the OS theory.
- **T4 (large fields).** Say whether the witness's YM-side inputs need dilute-instanton-strength
  large-field control ((TS-up)/(LF-inst) in ASSEMBLY55); prefer one that does not.
- **T5 (no-go option).** If no finite-moment witness can exclude all identifications, prove that as a
  first-class result, with the exact class for which it holds.

What would count as a refutation of what this file will claim:
- of a free-side theorem: one explicit member of the stated free class (or of a theory built from it by
  composite fields / tensor products / mixtures / changes of field labelling) on which the witness is
  nonzero or the claimed exclusion fails;
- of a no-go: one explicit finite-moment witness that separates the stated YM-type data from the whole
  free class;
- of a YM-side reduction: an example of data satisfying the named inputs with |W| < c, or a hidden
  extra input the reduction uses;
- of any numeric gate in `checks/nf55_*`: a gate that could not have failed, or a PASS not reproduced.

---

## §0. Inputs read, labels, and the Codex verdicts used (appended from 2026-10-29T05:0xZ)

*Read before the derivations below (bounded ranges, located by string):* the task brief (queue/nonfree.md); REVIEW_BRIEF_55
(all); CODEX_REVIEW_HINT2 (all; complete — it ends with "Exactly what may be banked" items 1-4); HINT2_55 (all 596 lines);
PANEL_P1 (`Non-free dynamics`, item 4 `CONDITIONAL — H_int`, §4 `Non-Gaussian composite observables`); PANEL_P3 §5
(`a nonzero connected four-point function of a composite observable`); ASSEMBLY55 §3-§4 (N0, N1F, N5, N6), §7 (F1, F2a, F16,
F17), §8 (ML1, ML13), §9 (items 22-23 and "most dangerous"), §10; SRCCD55 §2.2-§2.3 (OS0 reading, Lemma V), §3.1-§3.3 (setting,
operator list, SRC-κ); ROTDEF §2.2 (`e_a(x) := (4a⁴)⁻¹`, `Guard against a vacuous pass`); CODEX_REVIEW_ASSEMBLY (R1, R4, R13,
"Corrected ordered OPEN work list" items 1-2 and 16, "Single most dangerous unverified item"; read at ≈04:55Z, complete);
OSLEAF55 (as on disk at ≈04:55Z: PRE-STATED only — no algebra is fixed there yet). Two arXiv abstracts (checked, §1.5).

*Labels.* **PROVEN-HERE** (complete argument written here); **IMPORTED-standard** (textbook fact, named, not re-derived);
**[m]** (literature from memory, not checked against an open text); **CONDITIONAL** (implication proven here, inputs named);
**ARGUED** (reason given, hole named); **OPEN**; **CONJECTURE**. Verdicts on inherited items: CONFIRMED / NOT-VERIFIED / REFUTED.

*Symbol pins (systemic defect 1), fixed now.* e_a := the clover density of ROTDEF §2.2 (no coupling factor; s(U) = 1 − N⁻¹Re tr U);
ê := e_a − ω(e_a) (SRCCD55 Prop. E's subtracted field); O_a(f) := Σ_x a⁴f(x)ê(x). In the limit, e denotes the reconstructed
scalar field whose separated Schwinger distributions S_n^e ∈ ^0𝒮′(R^{4n}) are the limits of those of ê (the produced object of
ASSEMBLY55 N2/F2a). f_λ(x) := λ⁻⁴f(x/λ) (dilation, ∫f_λ = ∫f). G_s(x) := (√s/(4π²|x|))K_1(√s|x|) for s > 0, G_0(x) := 1/(4π²|x|²)
(the Euclidean propagator 1/(p² + s)). u_k := 1/g_k² (FLOW's lane coupling, u = 2N/g_std²); λ_m := L^{−m} (physical units,
ℓ_ref = 1). γ, j, C below are the exponent / log-power / amplitude of a short-distance asymptotic, never the lane's γ (FLOW's γ
is not used in this file). 𝔉_can, 𝔉_GFF, (NF), (ENV), (AF-e), (TS-e) are defined in §1-§3. ρ denotes a Källén–Lehmann (KL)
measure only (not a density matrix, not PROOF's ρ_k).

*Codex verdicts used, and my position.*
| Codex verdict (file, locating string) | My position |
|---|---|
| HINT2 F1: "ID♮ is a contraction convention, not a reconstructed-observable identification"; "(q²)^♮=0 while (q^♮)²=q₂(A)²≠0" | **Agree** (re-derived: the second-order contraction of q² is the c⁴ term, so it vanishes at order c²). Nothing below uses (ID♮) |
| HINT2 F1: scalar obstruction t²M²E[(K_t∗φ)²] ≤ M²t/(32π²) → 0; "mapping the family to φ(t)·1 also realizes any prescribed nonnegative profile" | **Agree**; strengthened in §2 (NG1): no continuous function of finitely many separated two-point values can vanish on even the linear identifications of 𝔉_can without vanishing everywhere |
| HINT2 F3 (UV-D_∞, Fatou mixture argument), F8 (REP needs translation invariance) | **Agree**; the Fatou pattern is reused for mixtures in §3.4; separated-point data never see contact terms, which is REP's point |
| HINT2 F9: tightness ≠ functional identification (X_j = Z/j example) | **Agree**; the witness below needs no new limit coordinate: it is a fixed family of separated two-point values of the produced field |
| HINT2 F4 + ASSEMBLY R4: failure of the union-bound route does not make (LF-inst) necessary | **Agree** (the abstract O = 0 on LF example suffices); §6 claims no necessity in either direction |
| ASSEMBLY R13: a 4D-flowed quadratic one-point statistic need not be an OS invariant (white-noise shift c/(64π²)) | **Agree**; I re-did ‖K_t‖² = (4πt)⁻⁴·(2πt)² = 1/(64π²t²) by the Gaussian integral ∫exp(−|x|²/(2t))d⁴x = (2πt)². This is why route (ii) of the brief is not taken (§5) |
| ASSEMBLY R1: separated (^0𝒮) data do not supply the ordinary positivity forms of e(f)² | **Agree** (S_2 + cδ changes ‖e(f)Ω‖² by c∫|f|² only). The witness below uses separated values only and needs no collision data |
| ASSEMBLY work-list item 2: choose the comparator class and an observable witness that survives the OS quotient; an ID♮-relative target must be labelled as a different target | **Agree**; §1 fixes the class, §3 gives the witness on the produced field, §1.4 labels the ID♮-relative statement as a different target |

## §1. T1 — what "not free" must mean (definition, version for T_OS, literature)

### 1.1 What is fixed
The limit theory is available only through the separated Schwinger distributions S_n^e of the produced scalar field e (and of
whatever finite field family OSLEAF55 adds). OS reconstruction (OS I/II [m]; owned by OSLEAF55 T-REC) turns them into a Wightman
theory 𝒯_e = (H, Ω, U, e). **Every functional of {S_n^e} is automatically identification-free**: nobody's labelling enters it.
The identification problem lives entirely on the *free side*: a free-side theorem must hold for every way of realising e inside
a free theory. This is the logical shape used throughout: witness = a functional of {S_n^e}; free-side theorem = quantified over
all realisations χ in the class.

### 1.2 Two readings that do not work
- **(i) Equivalence of (H, Ω, U) without the field.** Meaningless as a non-freeness notion. Two generalised free fields whose KL
  measures are mutually absolutely continuous carry unitarily equivalent (H, Ω, U) (Fock spaces over equivalent direct integrals
  of mass-√s irreducibles, multiplicity one; spectral theorem, IMPORTED-standard), yet their Schwinger functions differ. The local
  structure — the field — must be part of the data.
- **(ii) "The generating gauge-invariant field's state is not quasi-free".** Vacuous for gauge-invariant generators. The free
  counterpart of e, the Maxwell composite Σ_a:F^a_{μν}F^a_{μν}:, is itself not quasi-free: its truncated three-point function is
  nonzero (exact value at an explicit Euclidean configuration: check nf55_a, gate A3; the general mechanism is PANEL_P3 §5's
  Y = X² − 1, κ₃(Y) = 8, κ₄(Y) = 48 for a standard Gaussian X — re-derived by hand: E[Y³] = 15 − 3·3 + 3·1 − 1 = 8 and
  E[Y⁴] − 3E[Y²]² = 60 − 12 = 48). So "some truncated S_n^e ≠ 0, n ≥ 3" holds for free gluons too and proves nothing.

### 1.3 Definitions (PROVEN-HERE as definitions; nothing assumed)
- **Canonical free theory.** F = Fock space of finitely many free fields Φ_1, …, Φ_k (masses m_i ≥ 0, finite spin), mutually
  independent, vacuum = Fock vacuum (quasi-free). Each Φ_i has Euclidean two-point function P_i(∂)G_{m_i}(x) with P_i a matrix-valued
  polynomial (scalar: 1; Dirac/Majorana: a first-order matrix polynomial; Proca: δ_{μν} − ∂_μ∂_ν/m²; Maxwell field strength: the
  second-order tensor of §7.1 applied to G_0; higher spins likewise). **𝔉_can** is the set of these. It contains free Maxwell with
  any colour number n (in particular n = N² − 1), and every finite tensor product of its members (= more species).
- **Identifications.** 𝒞(F) := Hermitian, Lorentz-scalar, Bose finite Wick polynomials χ in components of the Φ_i and finitely
  many of their derivatives ("local composite fields of the free theory"). [Borchers class, [m]: Borchers (1960), Epstein (1963) —
  every tempered scalar Wightman field relatively local to finitely many free fields is a Wick series, finite by temperedness. Only
  the polynomial class is used below, so no result here depends on this [m].]
- **(NF-can).** The e-theory is **𝔉_can-free** if there are F ∈ 𝔉_can and χ ∈ 𝒞(F) with S_n^e = S_n^χ on ^0𝒮(R^{4n}) for every
  n ≥ 2 (equivalently, by uniqueness in Wightman reconstruction [m], 𝒯_e is unitarily equivalent — vacuum and Poincaré
  covariantly — to the cyclic subtheory of F generated by χ: "YM is a subtheory of a free theory under some field assignment").
- **Mixtures with a UV envelope.** ω = ∫ω_α dν(α) (probability ν, measurable family), each ω_α 𝔉_can-free via χ_α, and
  **(ENV)**: there are B, J < ∞, r_0 ∈ (0, 1] with S_2^{α,T}(x) ≤ B|x|^{−γ_α}|log|x||^J for 0 < |x| ≤ r_0 and ν-a.e. α, γ_α the
  component's leading exponent from Theorem FS (§3). Every finite mixture satisfies (ENV) (take the maximum of finitely many
  constants; each component obeys its own bound by Theorem FS).
- **T_NF (the target property).** The e-theory is neither 𝔉_can-free nor an (ENV)-mixture of 𝔉_can-free theories.
- **The larger class 𝔉_GFF.** Replace "canonical free fields" by generalised free fields (arbitrary tempered KL measures), and/or
  allow mixtures without (ENV). (NF-GFF) := not free relative to this class.

### 1.4 Which version T_OS should carry, and why (ARGUED, with the proved inputs cited)
**Recommendation: T_OS's "is not a free theory" should be read as T_NF, with the class 𝔉_can, the identification class 𝒞, and
(ENV)-mixtures written into the statement.** Reasons:
1. T_NF is intrinsic: a property of {S_n^e}, quantified over every identification in the class (every local composite, every
   finite tensor product, every mass, every colour number).
2. It says exactly that pure Yang–Mills is not a subtheory of any finite collection of free particles — in particular not of
   N² − 1 free gluons — under any field assignment.
3. It is certifiable on the produced algebra by a witness whose Yang–Mills side is a two-sided asymptotic-freedom bound on the
   separated e two-point function (§3), i.e. by the object H_reg already produces.
4. (NF-GFF) cannot be certified by anything built from the two-point function (§2, NG2, exact), nor by asymptotic-freedom-type
   two-sided bounds on finitely many n-point functions (§2, NG3). It is a strictly stronger target with no route I know of; if
   the owner wants it, it must be stated as such and is OPEN without route.
5. Reading (ii) is vacuous (§1.2). HINT2's statement — non-membership of the 4D-flowed one-point profile in conv(𝔊^col_∞ ∪ 𝔖)
   *relative to (ID♮)*, on the joint Euclidean state — is a **different target, T_NF♮**; if kept it must carry that name
   (CODEX_REVIEW_ASSEMBLY work-list item 2).
*Limitation, stated now.* The witness of §3 is affine in the state, so it certifies ω ∉ (ENV)-conv(𝔉_can-free). It does not
certify that every extremal component of ω is non-free: ½ω_YM + ½ω_free obeys every bound that ω_YM obeys and has a free
component. Component-wise non-freeness needs component-wise bounds (clustering-type information), outside OS0–OS3. T_OS's literal
"is not a free theory" is met by T_NF; "no free phase is mixed in" is not claimed.

### 1.5 Comparison with the constructive literature
- **Φ⁴_3.** Gubinelli–Hofmanová, *A PDE construction of the Euclidean Φ⁴_3 quantum field theory*, arXiv:1810.01700 (abstract
  checked): "Every limit point is non-Gaussian" — a statement about the law of the elementary field φ, i.e. reading (ii) for a
  *labelled elementary* field. The classical constructions (Glimm–Jaffe; Feldman–Osterwalder 1976; Magnen–Sénéor 1976) [m] obtain
  non-triviality from a nonzero four-point Ursell function of φ at weak coupling [m].
- **Φ⁴_4 (the opposite result).** Aizenman–Duminil-Copin, arXiv:1912.07973 (abstract checked): the scaling limits "are Gaussian";
  the deviation of the correlation functions "from Wick's law" is what is controlled — again the law of the elementary field.
- **P(φ)_2.** S-matrix non-triviality (Osterwalder–Sénéor 1976 [m]) is identification-free (the Haag–Ruelle S-matrix depends only
  on the Borchers class [m]) but needs isolated mass shells, i.e. a gap — excluded from T_OS.
- **Y_2.** Constructions [m] (Glimm–Jaffe, Seiler–Simon, Magnen–Sénéor, Schrader); I have no checked statement of a non-triviality
  theorem for Y_2 and nothing here uses one.
*Comparison.* Where the measure is the law of an elementary field, "non-Gaussian" (reading (ii)) is meaningful. A gauge-invariant
algebra has no elementary field, so the φ⁴ notion has no gauge-invariant analogue, and T_NF is the natural replacement: stronger
than the φ⁴ notion (all identifications in the class are excluded), weaker than S-matrix non-triviality (no gap needed). Side
remark (PROVEN-HERE, elementary): for a *linearly identified* field, a strictly negative fourth cumulant of one smeared variable
excludes every mixture of centred Gaussian states, since a centred Gaussian scale mixture has κ₄ = 3Var_ν(σ_α²) ≥ 0 — the
mechanism behind φ⁴'s Lebowitz sign [m]; composites have no such sign.

## §2. T5 — three no-go results (first-class results; they shape the witness)

*Common import.* **(KL)** For a scalar OS theory (OS0–OS3 with OS II's growth condition [m]), the separated two-point function is
S_2^T(F) = ∫ρ(ds)φ_F(s), φ_F(s) := ∫∫F(x, y)G_s(x − y)dx dy, F ∈ ^0𝒮(R⁸), with ρ a positive tempered measure on [0, ∞) (Källén–Lehmann:
reconstruction + spectral theorem + Lorentz covariance; IMPORTED-standard [m]). Used only in NG1–NG3, never in the free-side
theorem of §3 (where everything is explicit).

### NG1 — no continuous finite-moment two-point witness exists against 𝔉_can. PROVEN-HERE (given (KL))
**Statement.** Let F_1, …, F_k ∈ ^0𝒮(R⁸) and W: R^k → R continuous. If W(S_2^χ(F_1), …, S_2^χ(F_k)) = 0 for every χ = Σ_{i≤r}c_iφ_i
(r < ∞; φ_i independent free scalars of masses m_i > 0 — a member of 𝒞(F), F ∈ 𝔉_can), then W(S_2(F_1), …, S_2(F_k)) = 0 for the
separated two-point function of every scalar OS theory.
*Proof.* (a) Put F̃(z) := ∫F(y + z, y)dy ∈ 𝒮(R⁴). F vanishes with all derivatives on {x = y}, so ∂^αF̃(0) = 0 for all α and
|F̃(z)| ≤ C_M|z|^M on |z| ≤ 1, every M. φ_F(s) = ∫F̃(z)G_s(z)dz. Since zK_1(z) decreases from 1, 0 < G_s ≤ G_0, and F̃G_0 ∈ L¹, so
φ_F is continuous on [0, ∞) (dominated convergence). Scaling G_s(z) = sG_1(√s z) gives ∫_{|z|≤1}|F̃|G_s ≤ C_M s^{−1−M/2}∫|w|^MG_1(w)dw,
and on |z| ≥ 1, G_s is exponentially small in √s; so |φ_F(s)| ≤ C_{F,M}(1 + s)^{−M} for every M.
(b) Let ∫(1 + s)^{−K₀}dρ < ∞. Given ε, pick S with ∫_{(S,∞)}|φ_{F_i}|dρ ≤ ε for all i (by (a)), partition [0, S] into intervals I_j
on which every φ_{F_i} oscillates by less than ε/(1 + ρ([0, S])) (uniform continuity), pick s_j ∈ I_j, s_j > 0, and set
ρ_ε := Σ_jρ(I_j)δ_{s_j}. Then |∫φ_{F_i}dρ − ∫φ_{F_i}dρ_ε| ≤ 2ε. ρ_ε is the KL measure of χ_ε := Σ_jρ(I_j)^{1/2}φ_j, φ_j independent free
scalars of mass √s_j, whose separated two-point function is Σ_jρ(I_j)G_{s_j} (free covariance). So S_2^{χ_ε}(F_i) → S_2(F_i), and by
continuity W(S_2(F_i)) = lim_ε W(S_2^{χ_ε}(F_i)) = 0. ∎
**Consequence for the contract.** PANEL_P1 item 4's "continuous finite-moment witness W [that] vanishes on the named class of free
physical theories" **cannot be built from two-point data for any class containing 𝔉_can**. Against 𝔉_can, two-point non-freeness is
certifiable only as an *asymptotic* property: a family of fixed-scale functionals W_λ (λ ↓ 0), each with cutoff- and
volume-uniform bounds (so each bound passes to every limit point — this is how CODEX_REVIEW_P4's "Non-freeness is not a closed
property" is respected), plus a free-side theorem excluding the asymptotic behaviour. HINT2's H-RED♮ already had this shape
("W_m ≥ c_W for all m ≥ m₁"). CODEX_REVIEW_P4's "fixed-scale … witness separated by a positive amount from its *calibrated* free
Yang–Mills comparator" is achievable only for a fixed identification, i.e. for a T_NF♮-type target (§1.4 item 5).
**CONJECTURE NG1′ (all orders; OPEN, nothing below uses it).** For finitely many separated tests of orders n ≤ n₀, the values
attained by χ ∈ 𝒞(F), F ∈ 𝔉_can, and finite mixtures are dense in those attained by scalar OS theories. If true, *no* continuous
finite-moment witness of any order separates T_NF, and asymptotic witnesses are the only kind. Evidence only: n = 2 is NG1; at
n = 3 linear identifications are not enough (on mean-zero tests every centred Gaussian mixture has vanishing odd moments), so
Wick-quadratic identifications would be needed, for which I have no density proof.

### NG2 — the two-point function cannot exclude 𝔉_GFF or envelope-free mixtures (exact). PROVEN-HERE (given (KL), Bochner–Minlos)
For the separated two-point function S_2 of any scalar OS theory, with KL measure ρ:
- **(a) A GFF with the same S_2.** Fix K ≥ K₀ and set Ŝ(u) := S_K(u) + A(1 + u)^K, S_K(u) := ∫ρ(ds)[1/(u + s) − Σ_{j<K}(1 − u)^j/(1 + s)^{j+1}]
  = (1 − u)^K∫ρ(ds)/((u + s)(1 + s)^K) (HINT2 A4.1, Codex F3 CONFIRMED). For u ∈ (0, 1), S_K(u) ≥ 0; for u ≥ 1, (1 + s)/(u + s) ≤ 1
  gives |S_K(u)| ≤ |1 − u|^K∫ρ/(1 + s)^{K+1} =: A|1 − u|^K ≤ A(1 + u)^K. So Ŝ ≥ 0 on (0, ∞); near p = 0, Ŝ(p²) ≤ C(1 + p⁻²), locally
  integrable in R⁴. Hence C(f, g) := ∫f̂(p)*Ŝ(p²)ĝ(p)d⁴p/(2π)⁴ is a continuous positive form on 𝒮(R⁴) and the centred Gaussian measure
  with covariance C exists (Bochner–Minlos, IMPORTED-standard). It is Euclidean invariant (Ŝ depends on p² only). Away from the
  diagonal the polynomial parts are contact terms, so C(x − y) = ∫ρ(ds)G_s(x − y) for x ≠ y (Fubini; G_s decays like e^{−√s|x−y|}).
  RP: for f supported in {x₀ > 0}, C(θf, f) evaluates only separated points, = ∫ρ(ds)⟨θf, G_s f⟩ ≥ 0 (each G_s is RP:
  IMPORTED-standard free-field RP), and Gaussian RP follows from covariance RP (PANEL_P3 §2's Wick-exponential argument). Its
  separated two-point function is S_2. ∎
- **(b) A mixture of single free scalars with the same S_2.** Let Z := ∫ρ(ds)(1 + s)^{−K₀}, ν(ds) := ρ(ds)(1 + s)^{−K₀}/Z (a probability
  measure), and let component s be the free scalar of mass √s with identification χ_s := (Z(1 + s)^{K₀})^{1/2}φ_s (𝔉_can-free). The
  mixture's separated two-point function is ∫ν(ds)Z(1 + s)^{K₀}G_s = ∫ρ(ds)G_s = S_2. ∎ Each component has leading exponent γ_s = 2
  and amplitude Z(1 + s)^{K₀}/(4π²); (ENV) fails whenever supp ρ is unbounded — exactly the case of interest.
**Consequence.** No witness depending only on S_2^e excludes 𝔉_GFF or envelope-free mixtures. ASSEMBLY55 F1's (W-e) ("the UV
behaviour of r⁸S_2^e(r)") can therefore exclude at most 𝔉_can and (ENV)-mixtures — which it does (§3) — never GFFs.

### NG3 — asymptotic-freedom-type bounds do not exclude 𝔉_GFF. PROVEN-HERE (explicit example)
*Example.* ψ a real scalar GFF with KL density h(s)ds, h(s) := 1/log(e + s) (positive, tempered; exists by NG2 (a)).
**Lemma (slowly varying Abelian estimate).** S_ψ(r) = (1 + o(1))·h(1/r²)/(π²r⁴) as r ↓ 0.
*Proof.* Substituting s = u²/r², G_s(r) = uK_1(u)/(4π²r²), so S_ψ(r) = (2π²r⁴)⁻¹∫_0^∞u²K_1(u)h(u²/r²)du, and ∫_0^∞u²K_1(u)du = 2 (Mellin:
∫u^μK_1 = 2^{μ−1}Γ(μ/2 + 1)Γ(μ/2), μ = 2; for h ≡ 1 this reproduces 16π²G_0² = 1/(π²r⁴), the two-particle check). On u ≥ √r:
h(u²/r²)/h(1/r²) ≤ h(1/r)/h(1/r²) ≤ 3 for small r (h decreasing; log(e + r⁻²)/log(e + r⁻¹) → 2) and → 1 pointwise; dominated
convergence with 3u²K_1(u) ∈ L¹. On (0, √r): the ratio is ≤ log(e + r⁻²) and ∫_0^{√r}u²K_1 ≤ r/2 (uK_1(u) ≤ 1); the product → 0. ∎
χ := :ψ²: is a Wightman field (its two-point function's Fourier transform is the two-particle convolution of ρ_ψ-weighted mass
shells, supported in the forward cone and tempered: IMPORTED-standard [m]); its separated Schwinger functions are Gaussian-chaos
sums (Wick): S_2^{χ,T}(x) = 2S_ψ(x)² = (2 + o(1))h(r⁻²)²/(π⁴r⁸) ~ 1/(2π⁴r⁸log²(1/r)), and
S_n^{χ,T}(x_1, …, x_n) = 2^{n−1}Σ_{cyclic orders}Π_iS_ψ(x_{σ(i)} − x_{σ(i+1)}). Hence for every fixed separated configuration and every
dilation, λ^{4n}S_n^{χ,T}(λx) = (1 + o(1))(π²log(λ⁻²))^{−n}2^{n−1}Σ_cycΠ|x_{σ(i)} − x_{σ(i+1)}|⁻⁴: the "running coupling to the power n
times a tree structure" behaviour expected of Yang–Mills' e at leading order [m: one-loop RG-improved perturbation theory]. In
particular χ satisfies (AF-e) of §3 with the Yang–Mills rate 1/log². The colour/tensor version — an (N² − 1)-colour antisymmetric
tensor GFF with spectral data T^I(p)⊗𝟙·h(s)ds (HINT2's 𝔊^col_∞ with one subtraction, since ∫h(s)ds/(1 + s) = ∞) and
χ = Σ_a:F^a_{μν}F^a_{μν}: — reproduces the tree-level Maxwell :F²: structure of every n-point function with one factor h per propagator,
any overall constant (rescale h).
**Consequence.** Any witness whose Yang–Mills side is a set of two-sided bounds c_n u(λ)^{−κ_n} ≤ |λ^{4n}S_n^{e,T}(F_λ)| ≤ C_n u(λ)^{−κ′_n}
(κ_n ≤ n ≤ κ′_n, finitely many n and tests) cannot exclude 𝔉_GFF: the example meets the same bounds. Excluding 𝔉_GFF needs
information beyond leading-order RG asymptotics; I can name no such information an RG route delivers (the GFF-composite class
is flexible enough to absorb any single asymptotic coefficient). **(NF-GFF): OPEN, no route.** [Remarks, [m]: GFFs with
continuous mass spectrum violate the time-slice axiom (Landau 1974; Garber 1975) and, for dense enough spectra, phase-space
(nuclearity) conditions (Buchholz–Wichmann 1986) — intrinsic properties that could separate, but no lane estimate approaches them.]

## §3. T2(a)/T3 — the witness: logarithmic violation of scaling in the produced e two-point function

### 3.1 Theorem FS (free side). PROVEN-HERE
*Imports (IMPORTED-standard):* Wick's theorem for the Euclidean Schwinger functions of Wick polynomials of free fields at separated
points (Gaussian integration; Grassmann integration for fermion components); the series of K_1 (Abramowitz–Stegun 9.6.11; its
log-structure is checked symbolically in nf55_c); reflection positivity of free fields.
**Statement.** Let F ∈ 𝔉_can, χ ∈ 𝒞(F), and S^T(x) := S_2^{χ,T}(x) (x ≠ 0) not identically zero. Then there are γ ∈ Z, j ∈ Z_{≥0} and
C > 0 with **S^T(x) = C|x|^{−γ}|log|x||^j (1 + o(1)) as x → 0.** Masses enter only subleading orders; the leading log-power is never
negative. (All fields massless ⇒ j = 0.)
*Proof.*
1. *Wick.* χ is a finite sum of Wick monomials; Wick ordering removes same-point pairings and monomials of different degree have no
   complete cross-pairing, so S^T(x) is a finite sum of finite products of entries of ∂^βP_i(∂)G_{m_i}(x) (with signs for fermions).
2. *One factor.* For m > 0, G_m(x) = (4π²r²)⁻¹[1 + A(m²r²)log(mr/2) + B(m²r²)], A, B entire with A(0) = B(0) = 0 (from
   zK_1(z) = 1 + zI_1(z)log(z/2) − (z/2)Σ_k(ψ(k+1) + ψ(k+2))(z/2)^{2k+1}/(k!(k+1)!)); G_0 = (4π²r²)⁻¹. With log(mr/2) = log r + log(m/2),
   and since ∂_μr^q = qx_μr^{q−2}, ∂_μlog r = x_μr^{−2}, every entry of ∂^βP(∂)G_m has an expansion Σ_{ℓ≥0}[h_{ℓ,0}(x) + h_{ℓ,1}(x)log r]
   with h_{ℓ,j} homogeneous of integer degree increasing with ℓ, absolutely convergent on 0 < r < ∞; derivatives never raise the
   power of log r.
3. *Products and sums.* A finite product is Σ_{ℓ≥0}Σ_{j≤J}H_{ℓ,j}(x)(log r)^j with H_{ℓ,j} homogeneous of degree −γ₀ + ℓ, J ≤ the number
   of factors, and |H_{ℓ,j}(x)| ≤ M_{ℓ,j}r^{−γ₀+ℓ}, Σ_{ℓ,j}M_{ℓ,j}r_1^ℓ < ∞ for some r_1 > 0 (Cauchy products of absolutely convergent
   series). Finite sums keep this form.
4. *Radial coefficients.* S^T is O(4)-invariant (χ scalar, F Euclidean invariant). Along a ray x = r x̂ the expansion is unique
   (if Σc_{ℓ,j}r^{a_ℓ}(log r)^j ≡ 0 on (0, r_1), divide by the lexicographically leading r^a(log r)^j and let r → 0; induct), so each
   H_{ℓ,j} is rotation invariant: H_{ℓ,j}(x) = c_{ℓ,j}r^{−γ₀+ℓ}.
5. *Leading term.* If every c_{ℓ,j} = 0, S^T vanishes near 0, hence everywhere (each factor is real-analytic on R⁴∖{0}) — excluded.
   Otherwise ℓ₀ := min{ℓ : ∃j c_{ℓ,j} ≠ 0}, j₀ := max{j : c_{ℓ₀,j} ≠ 0}, γ := γ₀ − ℓ₀ give
   S^T(r) = c_{ℓ₀,j₀}r^{−γ}(log r)^{j₀}[1 + O(|log r|⁻¹)] + O(r^{−γ+1}|log r|^J).
6. *Sign.* S^T ≥ 0 off the origin: for x ≠ 0 rotate x to 2t e₀ (t > 0) and apply RP of the centred field χ − ⟨χ⟩ to f_ε ≥ 0
   concentrating at t e₀ (θ(te₀) = −te₀); continuity of S^T at separated points gives S^T(2t e₀) ≥ 0. Hence c_{ℓ₀,j₀}(−1)^{j₀} > 0;
   put C := |c_{ℓ₀,j₀}|. ∎
*Remark (why massive theories are no loophole).* A massive free theory breaks scale invariance at finite r, but its masses only
multiply higher powers of r (with at most nonnegative powers of log r). The witness is the r → 0 behaviour, not the scale
dependence at finite r.

### 3.2 Corollary SEP-e (separation; exactly what the witness needs). PROVEN-HERE
Fix f, g ∈ C_c^∞(R⁴), f, g ≥ 0, f, g ≢ 0, with disjoint supports (|x − y| ∈ [d, D] on supp f × supp g, 0 < d ≤ D). Say a scalar
OS theory satisfies **(AF-e)** if, along some λ_m ↓ 0,
  **λ_m⁸ S_2^{e,T}(f_{λ_m}⊗g_{λ_m}) → 0  and, for every η > 0,  λ_m^{8−η} S_2^{e,T}(f_{λ_m}⊗g_{λ_m}) → +∞.**
**Then the theory satisfies T_NF** (it is neither 𝔉_can-free nor an (ENV)-mixture of 𝔉_can-free theories).
*Proof.* Pure case, S_2^e = S_2^χ: S_2^χ(f_λ⊗g_λ) = ∫∫f(x)g(y)S^T(λ(x − y))dxdy, and by FS, uniformly for |w| ∈ [d, D],
S^T(λw) = Cλ^{−γ}|w|^{−γ}|log λ + log|w||^j(1 + o(1)) with |log λ + log|w||^j/|log λ|^j → 1; so
λ^γ|log λ|^{−j}S_2^χ(f_λ⊗g_λ) → C I_γ, I_γ := ∫∫f g|x − y|^{−γ} > 0. If γ ≥ 8, λ⁸S_2 stays ≥ C I₈/2 (γ = 8) or → ∞ (γ > 8),
contradicting the first half. If γ ≤ 7 (γ ∈ Z), take η = ½: λ^{7.5}S_2 ~ C I_γλ^{7.5−γ}|log λ|^j → 0, contradicting the second half.
Mixture case, S_2^e = ∫S_2^αdν: each S_2^α(f_λ⊗g_λ) ≥ 0 (FS step 6, f, g ≥ 0). Fatou gives ∫liminf_m λ_m⁸S_2^α dν ≤ 0, so the
liminf vanishes ν-a.e., which by the pure case forces γ_α ≤ 7 ν-a.e. Then (ENV) with λ_m D ≤ r_0 ≤ 1 gives
S_2^α(f_λ⊗g_λ) ≤ B∫∫fg(λ|x − y|)^{−7}(|log λ| + |log d|)^J ≤ B′λ^{−7}(|log λ| + c)^J ν-a.e., hence
λ^{7.5}S_2^e(f_λ⊗g_λ) ≤ B′λ^{1/2}(|log λ| + c)^J → 0, contradicting the second half with η = ½. ∎
*Which half excludes what.* The **upper half** excludes every 𝔉_can member with γ ≥ 8 — in particular the free Maxwell composite
Σ_a:F^aF^a: of N² − 1 free gluons (γ = 8, j = 0; exact two-point coefficient in nf55_a A2) under every normalisation and every
admixture of lower-dimension composites. The **lower half** excludes γ ≤ 7 and trivial limits. Neither half alone suffices.

### 3.3 The witness on the produced algebra, and the Yang–Mills-side named inputs
*Witness family.* W_λ(ω) := λ⁸ S_2^{ê,T}(f_λ⊗g_λ); on the lattice, W_λ(ω_{K,R}) = λ⁸ ω^c_{K,R}(O_a(f_λ), O_a(g_λ)) (Riemann sums of the
separated two-point function of the subtracted clover density — the object SRCCD55 Prop. E produces). Each W_λ is a fixed separated
two-point value: a function of the reconstructed theory (OS-invariant), on the algebra of OS0–OS3, with no flow, no time-zero
restriction and no collision data.
*Inputs (λ_m := L^{−m}, a = L^{−K}, F-tune's trajectory at fixed renormalised g, tori R ≥ R₀; constants independent of K, R):*
- **(TS-e-up)** there are C₊ < ∞, κ > 0, d₀, m₀ with λ_m⁸|ω^c_{K,R}(O(f_{λ_m}), O(g_{λ_m}))| ≤ C₊ u_{K−m}^{−κ} for all m ≥ m₀, K ≥ m + d₀.
- **(TS-e-low)** there are c₋ > 0, κ′ < ∞ with λ_m⁸ω^c_{K,R}(O(f_{λ_m}), O(g_{λ_m})) ≥ c₋ u_{K−m}^{−κ′}, same quantifiers.
- Rate-free form, equivalent for the conclusion: **(TS-e°)** sup_{K,R}λ_m⁸|ω^c| → 0 and, ∀η > 0, inf_{K,R}λ_m^{8−η}ω^c → ∞ (m → ∞).
*Expected values [m: one-loop RG-improved perturbation theory, not used]:* κ = κ′ = 2, since e ≈ F^aF^a/(2u) at tree level
(§4.1) and the free Maxwell composite has ⟨:F^aF^a:(x):F^bF^b:(0)⟩ = 48(N² − 1)/(π⁴|x|⁸) (nf55_a A2), giving
W_λ ≈ (12(N² − 1)/π⁴)u(λ)^{−2}∫∫f g|x − y|^{−8}.
**Lemma TS.** (TS-e) + (F-tune) ⇒ (TS-e°). *Proof.* U₋(m) ≤ u_{K−m} ≤ U₊(m) = g⁻² + β₊m log L + R_F (FLOW F-tune; R_F per CODEX_REVIEW_HINT2
F9's collision repair). Upper: C₊U₋(m)^{−κ} → 0 as β₋ > 0. Lower: λ_m^{8−η}ω^c ≥ L^{ηm}c₋U₊(m)^{−κ′} → ∞. ∎ PROVEN-HERE.
**Theorem H-RED^e.** CONDITIONAL on (TS-e°) [⇐ (TS-e) + (F-tune)] and on H_reg's convergence of the separated two-point values on the
countable family {f_{λ_m}⊗g_{λ_m}}_m along the common subsequence. Then every limit point satisfies (AF-e) along λ_m, hence T_NF.
*Proof.* For fixed m the bounds are uniform in (K, R) and the values converge along the subsequence, so λ_m⁸|S_2^{e,T}(f_{λ_m}⊗g_{λ_m})|
≤ ε(m) → 0 and λ_m^{8−η}S_2^{e,T}(…) ≥ inf_{K,R}(…) → ∞ in the limit; apply SEP-e. ∎ PROVEN implication.
*What this removes from HINT2's list.* No (MOM-E) (the values are limits of finitely many separated moments, supplied by H_reg), no
Lemma INT/CONV (no continuous flow time), no (SRC)/(FLOW-BLK) for flowed observables, no (ID♮), no time-zero finiteness. *What it
adds.* A lower bound at **every** short scale (HINT2's (TS-low) was at one coarse scale).
*Statuses.* **(TS-e-up): OPEN.** Nearest producer: SRCCD55 SRC-κ (κ-1) at n = 2, whose weight w_e(δ)² = δ⁻⁸𝔤_e(δ)² allows 𝔤_e to *grow*
like a power of log(2 + ℓ_ref/δ) — the wrong direction; (TS-e-up) is (κ-1) at n = 2 sharpened to an asymptotic-freedom envelope
u(δ)^{−κ/2} (this is ASSEMBLY55 F1(b)'s "AF upper bound at n = 2"); SRC-κ itself is NOT-VERIFIED (CODEX_REVIEW_SRCCD). **(TS-e-low): OPEN**;
no lower bound on any e-correlator exists on disk. By-product: (TS-e-low) at one fixed m supplies ROTDEF §2.2's missing non-vacuity
guard ("strict positivity uniform in (a,R) is **not** supplied here") with Z_e ≡ 1. **(F-tune): CONDITIONAL** (FLOW Theorem F-tune with the
inputs HINT2_55 R2.3 lists: (UIR^♮_br) + (SF-g) + (RLF-δ) + (SF-cont) + (SF-∞)). **H_reg: OPEN** (ASSEMBLY55 N2).
*Is an input H_int restated?* No single input separates: (TS-e-low) is met by every free composite with γ = 8 (e.g. free gluons),
(TS-e-up) by every free composite with γ ≤ 7. The separation is Theorem FS + SEP-e, proved here. (These inputs are where the
asymptotic-freedom work lives, as for HINT2.)

## §4. T2(b), T2(c) — the other two candidate witnesses

### 4.1 (b) The trace anomaly: subsumed by (a); rejected as an independent witness
*Tree-level identification of the produced field (PROVEN-HERE as algebra, nf55_b B0–B2; the anomaly formula is [m]).* With
s(U) = 1 − N⁻¹Re tr U, U_p = exp(ia²gF^at^a), tr(t^at^b) = δ^{ab}/2, g = g_std and u = 2N/g² (FLOW's pinned convention):
s(U_p) = a⁴g²Σ_a(F^a_{μν})²/(4N) + O(a⁶), u·Σ_{μ<ν}s(U_p) = a⁴·¼Σ_{μν}(F^a_{μν})² (the canonical action; with u misread as 1/g² the
identity fails by the factor 2N — control B1-F), and e_a = (4a⁴)⁻¹Σ_{μ≠ν}Σ_{clover}s(U_p) = **F^aF^a/(2u)** + O(a²) (F^aF^a := Σ_{μν}F^a_{μν}F^a_{μν}).
With the trace anomaly Θ = (β(g)/(2g))F^aF^a, β = −b₀g³ + O(g⁵), b₀ = 11N/(48π²) [m: Collins–Duncan–Joglekar 1977, Nielsen 1977],
**Θ = −(11N²/(24π²))·e** at leading order (nf55_b B3; the overall sign is convention-dependent [m]). So, up to an additive
constant (identity mixing, removed by ê) and relative O(g²) corrections, **the produced field e is the trace of the
energy–momentum tensor** — the renormalisation-group-invariant combination, which is why Z_e ≡ 1 is the right normalisation
(SRCCD55 Prop. D(ii)). The upper half of (AF-e) is the statement that the anomaly's two-point amplitude vanishes like β(g)²/g² ~ u⁻²
(expected amplitude 12(N² − 1)/(π⁴u²), nf55_b B4 with nf55_a A2), and the lower half that it is not power-suppressed. **The
identification-free content of the trace-anomaly witness is therefore exactly witness (a) on e.**
*As a stand-alone witness ("Θ ≠ 0") it fails both requirements.* (1) It needs a local energy–momentum tensor T_{μν} of the
reconstructed theory (a field generating translations, with Ward identities) and the identification of e with its trace — not
produced (SRCCD55 §3.2: the existence of 𝒯_{μν} "is part of SRC-M", OPEN). (2) On the free side it is neither
identification-free nor class-wide: a free theory's T_{μν} is fixed only up to improvement terms, which change the trace; free
massive theories have nonzero trace and free massless ones admit traceless improvements [m]. So "Θ ≠ 0" could exclude at most
massless free theories, and only under an identification of T. Likewise "the theory is not scale invariant" does not exclude
massive free theories; what excludes them is their short-distance structure (Theorem FS), i.e. (a). **Verdict: (b) is
SUBSUMED by (a) and REJECTED as an independent witness.**

### 4.2 (c) OS-intrinsic Gaussianity tests: rejected for T_OS (their usable content reduces to (a))
- *(c1) Truncated functions of e.* Composites of free fields have nonzero truncated functions, so these do not discriminate. Exact
  instance (nf55_a): for the one-colour free Maxwell composite :F_{μν}F_{μν}:, the truncated **four**-point function at R1 is
  −106278912/285333125·(4π²)⁻⁴ ≠ 0 (brute-force matching enumeration = cycle formula, gate A4). Its truncated **three**-point
  function vanishes identically (gate A3, three configurations): Euclidean F·F continues to a multiple of B² − E², which is odd
  under the unitary electric–magnetic duality rotation of free Maxwell theory [m]. (Consequence for Yang–Mills: the tree-level
  part of ⟨eee⟩_c vanishes; a nonzero three-point function of e is an interaction effect. Not used below.)
- *(c2) "Is there a quasi-free field generating, or containing, the e-net?"* That is T_NF itself (with the class made explicit).
  It is not decidable from finitely many separated two-point values (NG1), and at higher orders its finite-moment form is
  CONJECTURE NG1′ (OPEN).
- *(c3) LSZ / Haag–Ruelle.* Identification-free (the S-matrix is an invariant of the Borchers class [m]), but it needs isolated mass
  shells — a gap or at least isolated one-particle hyperboloids — which T_OS explicitly does not provide; Buchholz's scattering
  theory for massless particles [m] needs structure (Huygens-type propagation of the massless particles) that the lane does not
  produce either. Not available.
- *(c4) Cumulant-sign tests.* A negative fourth cumulant excludes mixtures of centred Gaussian states only for a *linearly
  identified* field (§1.5); composites have no sign.
**Verdict: (c) REJECTED for T_OS.** What survives of (c) is that a free-side theorem must be quantified over all identifications —
which Theorem FS does for the two-point function.

## §5. T3 — the witness is on the produced OS algebra; route (ii) not taken; what is reused from HINT2

**5.1 Same algebra, OS-invariant (PROVEN-HERE by inspection of the definitions).** W_λ uses only the values S_2^{e,T}(f_λ⊗g_λ) for one
fixed pair f, g ≥ 0 with disjoint supports and the countable family λ_m = L^{−m}. These are separated tests in ^0𝒮(R⁸), i.e. values
of the very Schwinger distributions on which OS0–OS3 are produced (ASSEMBLY55 F2a). Consequently: no collision data are used
(CODEX_REVIEW_ASSEMBLY R1 does not bite); no positive-time support is needed (W_λ is a Schwinger-function value, not an OS-vector
norm); and W_λ(ω) = ∫∫f_λ(x)g_λ(y)S_2^{e,T}(x − y)dxdy is the Euclidean continuation of the reconstructed Wightman two-point function,
so unitarily equivalent reconstructions give equal W_λ (OS invariance). H_Euc is not an input of H-RED^e: Theorem FS uses the free
theories' Euclidean invariance, not Yang–Mills'.
**5.2 Requirement on OSLEAF55's algebra — (ALG-W).** The field family contains e (with Z_e ≡ 1 and the identity subtracted), and the
countable family {f_{λ_m}⊗g_{λ_m}}_m belongs to the determining family on which H_reg's convergence is proved (or follows from it via
the uniform extension estimate ML9). OSLEAF55 is at its PRE-STATED on disk (T-ALG: an OS test algebra over a finite field family
with ^0𝒮 Schwinger distributions); (ALG-W) is compatible with it as stated. If the family is enlarged (e.g. by 𝓑 or the
pseudoscalar density), T_NF should be restated for the enlarged family; the e-witness still suffices, because a family that
embeds in a free theory restricts to an e that does.
**5.3 Route (ii) of the brief (the flowed algebra 𝔈 generated inside the OS theory) is not taken.** (1) CODEX_REVIEW_ASSEMBLY R13:
independent contact noise shifts the t²-normalised 4D-flowed quadratic one-point statistic by c/(64π²) without changing the
reconstructed Gaussian theory, so such statistics are not functions of the reconstructed theory in general; making one a
function of it needs the flowed field as a controlled limit of OS-algebra elements. (2) 𝓔(t, x) is a nonlinear functional of the
gauge field; e is one gauge-invariant composite; there is no expression of 𝓔 through e-correlators, so route (ii) would need the
produced algebra to be the full gauge-invariant local algebra with the continuum flow inside it, uniformly — far more than (i)
needs. (3) Under T_NF's quantification over all identifications, one-point witnesses fail outright (HINT2 R1.10(i); CODEX_REVIEW_HINT2
F1); (W-T0)'s comparator value is computed under (ID♮), so it inherits the identification gap. Route (i) is taken.
**5.4 Reuse of HINT2_55 (brief item 3).** *Reused:* the Fatou mixture pattern of SEP^col (→ SEP-e, mixture case); Lemma REP's
lesson that separated data never see contact terms (built into W_λ); H-RED♮'s skeleton (cutoff-uniform bounds at each fixed scale →
limit points → free-side theorem), now without (MOM-E), INT and CONV; the scalar obstruction of CODEX_REVIEW_HINT2 F1 (generalised to
NG1); the subtracted-Stieltjes construction of 𝔊^col (A4.1; used in NG2 (a)). *Not reused:* (ID♮) (as the brief requires), Lemma
PAIR, UV-D_∞ (a dichotomy for flowed one-point functions — at separated points subtractions are invisible), Proposition T0, NOBS /
GC-ξ, Lemma INT / CONV, Proposition WN.

## §6. T4 — large fields: what the e-witness needs (ARGUED; no necessity claimed in either direction)

**6.1 Where HINT2's difficulty came from.** For the τ²-normalised flowed one-point function at τ ≍ ℓ_k², a flow-surviving concentration
of size ℓ_j contributes (ℓ_k/ℓ_j)⁴ = L^{4(k−j)}, and a polylogarithmic per-block probability e^{−cp(g_j)²} loses against it (HINT2 R2.4;
CODEX_REVIEW_HINT2 F4/F13: the union-bound route fails; CODEX_REVIEW_ASSEMBLY R4: that does not make (LF-inst) necessary — I agree).
**6.2 The e-witness has no flow-time amplification, but the naive route fails for another reason.** W_λ is a *connected* two-point value
of *lattice-local* observables at separation λ. Bounding the large-field part by |ê| ≤ Ca⁻⁴ on the event and Cauchy–Schwarz forms the
coincident variance Var(O_a(g_λ)) ≥ c g_0⁴a⁻⁴λ⁻⁴‖g‖₂² (SRCCD55 Lemma V), which diverges as a → 0. So the large-field part of W_λ must be
controlled inside an expansion that never forms coincident variances — the multiscale expansion of the e-source generating
functional (SRCCD55 SRC-poly / SRC-κ-LF), with separated insertions.
**6.3 Power count (ARGUED; dilute-gas/OPE intuition [m]).** A level-j large-field region (diameter ℓ_j ≪ λ) inside supp f_λ shifts O_a(f_λ)
by ≍ λ⁻⁴·(its e-integral, O(1) in e's g²F² normalisation); there are ≍ (λ/ℓ_j)⁴ positions, each with probability P_j. Its *connected*
effect on O_a(g_λ) at distance λ is through the coarse field: a localised disturbance of size ℓ_j couples to distant gauge-invariant
observables through dimension-4 operators, relative size ≍ (ℓ_j/λ)⁴ (classical analogue: a small instanton's field F ≍ ℓ²/r⁴). Net:
λ⁻⁸·(λ/ℓ_j)⁴·P_j·(ℓ_j/λ)⁴ = λ⁻⁸P_j per level — no amplification. Summed over the levels between the cutoff and λ, with
P_j ≤ e^{−cp(g_j)²}, p(g) = (log 1/g)^p and u_j growing linearly in the level distance, the sum is dominated by levels near λ and is
o(u(λ)^{−2}) iff 2p > 1 (or c > 2 at 2p = 1) — the comparison algebra CODEX_REVIEW_HINT2 F13 checked (E7). That would make large fields
negligible for both halves of (TS-e).
**6.4 The named input this reading needs.** **(LF-dec)** In the multiscale expansion of the e-source generating functional, polymers
containing a level-j large-field cube within distance ℓ_j of one insertion and reaching the other insertion at distance λ ≥ ℓ_j
contribute at most Cλ⁻⁸θ(ℓ_j/λ)e^{−cp(g_j)²} to the connected two-point function, with θ bounded on (0, 1] (no inverse power of ℓ_j/λ),
plus a Balaban-type factor with 2p > 1. *Status:* OPEN; mechanism ARGUED only. *The crux* is the decoupling exponent: if the influence
decays only like (ℓ_j/λ)^q with q < 4, an amplification (λ/ℓ_j)^{4−q} remains and a polylogarithmic probability does not beat it — the
HINT2 phenomenon in another guise. I do not claim (LF-dec) holds, nor that (LF-inst) is necessary or unnecessary for (TS-e).
**6.5 Preference.** On the brief's criterion ("prefer a witness that does not [need dilute-instanton-strength control]"), the e-witness
is preferred: its large-field requirement, in this reading, is an observable-weighted decoupling statement of the kind a polymer
expansion with decay in units of each scale is built to give (SRC-κ-LF's path sums are where it would live), not an
instanton-strength probability bound. This preference is ARGUED, not proved.

## §7. Checks (criteria before scripts; exact arithmetic only)

**7.1 The free Maxwell field-strength correlator (the "second-order tensor" of §1.3).** With ⟨A_α(x)A_β(y)⟩ = δ_{αβ}G_0(x − y) (Feynman
gauge; any covariant gauge gives the same F-correlator — gate A1),
  D_{μν,ρσ}(z) := ⟨F_{μν}(x)F_{ρσ}(y)⟩ = −[δ_{νσ}∂_μ∂_ρ − δ_{νρ}∂_μ∂_σ − δ_{μσ}∂_ν∂_ρ + δ_{μρ}∂_ν∂_σ]G_0(z),  z = x − y,
and Σ_{μνρσ}D(z)² = 24/(π⁴|z|⁸) (gate A2: |z|⁸ΣD̃² = 384 with D̃ = 4π²D). Hence ⟨:F^aF^a:(x):F^bF^b:(0)⟩ = 48(N² − 1)/(π⁴|x|⁸) — the
γ = 8, j = 0, C > 0 case of Theorem FS that the upper half of (AF-e) excludes ("not N² − 1 free gluons").

**7.2 Record.**
| id | files (UTC by `date -u`) | result | could it fail? |
|---|---|---|---|
| nf55_a | criteria 05:22:47Z; script written after; a first launch at 05:24:09Z did not start (`timeout` is not installed: shell error, no output, nothing kept); run 05:24:13Z, 7.1 s; `nf55_a_out.txt` | **PASS**: A1 (all 144 components unchanged by the pure-gauge term at 4 points; control A1-F fired: 40 components change for the symmetrised F); A2 (384 at all six points; control A2-F fired: 304); A3 (T3 = 0 exactly at Q1, Q2, Q3; control A3-F fired: scalar :φ²: gives 2/5 = 8G̃G̃G̃); A4 (T4 = −106278912/285333125 in units (4π²)⁻⁴ at R1, enumeration over 48 connected matchings = 16·Σ over 3 cycles; control A4-F fired: disconnected part 214287181703424/13731656640625 ≠ 0) | yes: each gate compares independently built objects (F built from A by differentiation; brute-force matchings vs cycle formula); each control fired |
| nf55_b | criteria 05:22:47Z; script written and run 05:24:49Z | **PASS**: B0 (1/4 = 1/4), B1 (difference 0; control B1-F fired: the factor-2N convention trap), B2, B3 (Θ/e = −11N²/(24π²)), B4 | B1 yes (control fired); B2–B4 are arithmetic of [m] inputs (they can fail only on an algebra slip) |
| nf55_c | criteria 05:22:47Z; script written and run 05:24:49Z | **PASS**: C1 (A&S series of K_1 satisfies the modified Bessel ODE through z^13; control C1-F fired: wrong ½ gives nonzero residuals at z^9, z^11, z^13), C2 (only log¹; constant 1; coefficient of z²log(z/2) is ½), C3 | C1 yes (control fired); C2 could fail on a series slip; C3 is a sanity check that cannot fail unless the series had a 1/log term (stated in its criteria) |
*Disclosure.* §1.2(ii) was written (≈05:15Z) before I noticed the duality argument and asserts a nonzero three-point function; the
nf55_a criteria (05:22:47Z) registered the corrected prediction T3 = 0, the run confirmed it, and erratum E1 corrects §1.2(ii).
*What the checks do not test.* Theorem FS's general argument (only its single analytic import, the K_1 series, is checked), NG1–NG3's
analytic steps, the [m] anomaly formula and duality statement (A3 tests the consequence at three configurations, not "identically"),
and every Yang–Mills estimate.

## §8. Errata to this file (append-only; each overrides the text it names)
- **E1 (§1.2(ii)).** "its truncated three-point function is nonzero (exact value at an explicit Euclidean configuration: check nf55_a,
  gate A3 …)" is **false**: the truncated three-point function of the free Maxwell composite vanishes (A3, three configurations;
  duality [m]). Read: "its truncated **four**-point function is nonzero (nf55_a, gate A4: −106278912/285333125·(4π²)⁻⁴ at R1)". The
  conclusion of §1.2(ii) — the labelled reading is vacuous for gauge-invariant generators — is unchanged.
- **E2 (§2 NG3, the sentence beginning "The colour/tensor version").** Withdrawn: no such GFF exists. **Lemma (PROVEN-HERE).** For an
  antisymmetric-tensor GFF with Bianchi spectral data T^I(p)Ŝ_s(p²), Ŝ_s = ∫ρ(ds)/(p² + s) up to contact terms, the magnetic correlator
  at Euclidean time separation t satisfies t⁴⟨Σ_{ij≤3}F_{ij}(te₀)F_{ij}(0)⟩ ≥ (6K_1(1)/π²)·ρ([0, t⁻²]), which is nondecreasing as t ↓ 0.
  *Proof.* Σ_{ij}T^I_{ij,ij}(p) = 4|p⃗|² (HINT2 A3.4) gives the separated correlator −4Δ_3S(te₀), S = ∫ρ(ds)G_s; for radial S(x) = s(|x|),
  Δ_3s at a point of the time axis is 3s′(t)/t, so the correlator is −12s′(t)/t. From (zK_1)′ = −zK_0, −∂_rG_s(r) = (z²K_0(z) + 2zK_1(z))/(4π²r³)
  ≥ 2K_1(1)/(4π²r³) for z = √s r ≤ 1 (zK_1 decreasing, K_0 > 0); integrate over s ≤ t⁻². ∎ So a field strength of dimension 2 cannot be
  damped by a vanishing factor (the unitarity-bound phenomenon); the most direct GFF imitation of Yang–Mills' leading tensor structure
  is impossible. Whether some other GFF composite reproduces Yang–Mills' leading n-point asymptotics *including tensor structure* is
  OPEN — the one place I see where a route to (NF-GFF) might exist; it would need the RG to deliver precise leading asymptotics
  (tensor structure and per-vertex damping), not two-sided bounds.
- **E3 (§2 NG3, "Consequence").** Scope corrected. The tree-level part of Yang–Mills' ⟨eee⟩_c vanishes (A3), so its true three-point
  exponent is plausibly > 3, and :ψ²: (three-point ≍ u⁻³) need not meet a Yang–Mills three-point *upper* bound. Use instead
  χ′ := :ψ₁ψ₂: with ψ₁, ψ₂ independent copies of ψ: every connected matching is one cycle whose edges alternate species, so all
  odd-point functions vanish; S_2^{χ′,T} = S_ψ² meets (AF-e); even-n functions scale as u(λ)^{−n} times alternating-cycle structures.
  Corrected consequence: (AF-e), and any finite set of two-sided bounds with exponents κ_n ≤ n ≤ κ′_n for even n and upper bounds
  only for odd n, are met by χ′, so they cannot exclude 𝔉_GFF. The general statement (all n, arbitrary exponents and shapes) is OPEN
  (see E2).
- **E4 (§0 heading time).** "appended from 2026-10-29T05:0xZ": that append ran at 05:12:39Z (`date -u`). No content depends on it.

## §9. Summary table, verdicts on inherited items, and what should change in PROOF.md / HANDOFF

**9.1 Claims of this file.**
| # | claim (locating string) | label |
|---|---|---|
| 1 | T_NF: not 𝔉_can-free and not an (ENV)-mixture of such; identifications = all local composites (§1.3) | DEFINITION |
| 2 | Reading (i) (equivalence of (H, Ω, U) without the field) is meaningless; reading (ii) (labelled quasi-freeness) is vacuous for gauge-invariant generators (§1.2, with E1: free-gluon composite has nonzero truncated 4-point, zero 3-point) | PROVEN-HERE (+ nf55_a A3, A4) |
| 3 | T_OS should carry T_NF; (NF-GFF) and T_NF♮ are different targets (§1.4) | ARGUED |
| 4 | Literature comparison (§1.5) | two abstracts checked (arXiv:1810.01700, 1912.07973); rest [m] |
| 5 | NG1: no continuous function of finitely many separated two-point values vanishes on 𝔉_can without vanishing on every OS theory | PROVEN-HERE (given (KL)) |
| 6 | NG1′: the same at all orders, with composites and finite mixtures | CONJECTURE (OPEN) |
| 7 | NG2: every OS two-point function is that of a GFF and of a (non-ENV) mixture of single free scalars | PROVEN-HERE (given (KL), Bochner–Minlos) |
| 8 | NG3 (scope per E3): (AF-e) and two-sided AF bounds (κ_n ≤ n ≤ κ′_n for even n, upper bounds for odd n) are met by :ψ₁ψ₂: of a log-damped GFF | PROVEN-HERE (Abelian lemma + Wick) |
| 9 | E2: no Bianchi antisymmetric-tensor GFF has a log-damped Maxwell propagator (t⁴·magnetic correlator ≥ (6K_1(1)/π²)ρ([0, t⁻²])) | PROVEN-HERE |
| 10 | Theorem FS: every composite of every canonical free theory has S_2^T = C|x|^{−γ}|log|x||^j(1 + o(1)), γ ∈ Z, j ≥ 0, C > 0 | PROVEN-HERE (imports: Wick; A&S series, checked nf55_c; free RP) |
| 11 | Corollary SEP-e: (AF-e) ⇒ T_NF (pure and (ENV)-mixture cases) | PROVEN-HERE |
| 12 | Lemma TS: (TS-e) + (F-tune) ⇒ (TS-e°) | PROVEN-HERE |
| 13 | Theorem H-RED^e: (TS-e°) + H_reg on {f_{λ_m}⊗g_{λ_m}} ⇒ every limit point satisfies T_NF | PROVEN implication; CONDITIONAL |
| 14 | (TS-e-up), (TS-e-low): two-sided AF bounds on the produced e two-point function at every short scale | OPEN (named inputs) |
| 15 | e = F^aF^a/(2u) + O(a²) at tree level; e = −(24π²/(11N²))Θ + const at leading order | PROVEN-HERE algebra (nf55_b); anomaly formula [m] |
| 16 | Free Maxwell composite: ΣD² = 24/(π⁴|x|⁸), two-point 48(N² − 1)/(π⁴|x|⁸), three-point 0, four-point ≠ 0 | CHECKED exact (nf55_a); "three-point ≡ 0" beyond the tested points rests on duality [m] |
| 17 | (b) trace anomaly: subsumed by (a), rejected as an independent witness | ARGUED |
| 18 | (c) Gaussianity / LSZ / cumulant-sign tests: rejected for T_OS | ARGUED |
| 19 | (ALG-W): the witness lives on the produced algebra; route (ii) not taken | statement + reasons (§5) |
| 20 | (LF-dec) is the large-field input of the e-witness in the §6 reading; no necessity claimed for (LF-dec) or (LF-inst) | ARGUED; (LF-dec) OPEN |
| 21 | Contract: PANEL_P1 item 4 must be restated as an asymptotic family with uniform fixed-scale bounds (from NG1) | PROVEN-HERE (the impossibility); restatement is a recommendation |

**9.2 Verdicts on inherited items examined.**
| item (file, locating string) | verdict |
|---|---|
| PANEL_P1 item 4 `A specified continuous finite-moment witness W vanishes on the named class of free physical theories` | **REFUTED as satisfiable** for any two-point witness against any class ⊇ 𝔉_can (NG1). *Correction:* "a family {W_λ} of fixed-scale finite-moment functionals with cutoff- and volume-uniform two-sided bounds, plus a free-side theorem excluding their joint asymptotics on the named class" (§3) |
| PANEL_P1 §4 / PANEL_P3 §5: Y = X² − 1 has fourth cumulant 48 | **CONFIRMED** (re-derived; also κ₃(Y) = 8) |
| ASSEMBLY55 F1 repair (b) (W-e): `the UV behaviour of r^8 S_2^e(r)`, needs `a new comparator theorem for :F²: two-point functions` and `an AF upper bound at n = 2` | **CONFIRMED as a route, with two corrections**: the comparator theorem needs no calibration and covers all of 𝔉_can under every identification (Theorem FS); and an AF **lower** bound at every short scale is also needed (TS-e-low). It cannot reach GFFs (NG2) |
| ASSEMBLY55 F17 / HINT2 R2.4: (TS-up) needs (LF-inst) | agree with CODEX_REVIEW_ASSEMBLY R4 (necessity not established); for the e-witness the large-field input is (LF-dec), ARGUED |
| HINT2 R1.10 (i): no one-point witness without a fixed identification | **CONFIRMED**, strengthened to two-point data (NG1) |
| ROTDEF §2.2 `Guard against a vacuous pass` (strict positivity not supplied) | unchanged as a gap; (TS-e-low) at one scale would supply it with Z_e ≡ 1 |
| SRCCD55 Z_e ≡ 1 for e | consistent with e ∝ Θ at leading order [m]; **NOT-VERIFIED** here as an RG statement |
| This file §1.2(ii) (three-point nonzero) | **REFUTED by nf55_a A3**; corrected in E1 |
*Codex verdicts used (agree/disagree):* CODEX_REVIEW_HINT2 F1, F3, F8, F9, F4/F13 (E7 algebra) — **agree**; CODEX_REVIEW_ASSEMBLY R1, R4,
R13, work-list item 2 — **agree**; CODEX_REVIEW_P4 §4.3 "Non-freeness is not a closed property" — **agree** (and its "fixed-scale …
calibrated comparator" request is achievable only for a fixed identification, i.e. for T_NF♮; §2 NG1).

**9.3 What should change in PROOF.md / HANDOFF (recommendations to the lead; this worker edits neither).**
1. **OWN-free.** State T_OS's "not free" as T_NF (class 𝔉_can, all local-composite identifications, finite tensor products,
   (ENV)-mixtures). Label (NF-GFF) as a different, stronger target (OPEN, no route) and HINT2's ID♮-relative statement as T_NF♮.
2. **H_int contract.** Replace PANEL_P1 item 4's single continuous witness by the asymptotic family of §3 (NG1 shows the literal
   version is impossible against 𝔉_can for two-point witnesses).
3. **H_int's Yang–Mills side** becomes (TS-e-up) + (TS-e-low) [+ (F-tune)] on the *produced* e two-point function. This removes
   ASSEMBLY55 F1's algebra mismatch for T_NF, gives ML13 a comparator-side producer (Theorem FS + SEP-e, PROVEN here), and replaces
   (TS-up), (TS-low), (MOM-E), (SRC)/(FLOW-BLK) for flowed observables and (ID♮). The YM side stays OPEN.
4. **Critical path.** (LF-inst) leaves the H_int path for the e-witness; its place is taken by (TS-e), which is SRC-κ (κ-1) at
   n = 2 sharpened to a two-sided asymptotic-freedom envelope — so H_int and H_reg now share one RG producer (the e-source generating
   functional, SRC-poly), and ASSEMBLY55's tier-5 leaf merges with the tier-3 SRC leaf plus that sharpening; its large-field part is
   (LF-dec) (ARGUED).
5. **Free-gluon facts for the ledger** (exact, nf55_a): the free composite Σ_a:F^aF^a: has two-point 48(N² − 1)/(π⁴|x|⁸), vanishing
   three-point function, nonzero four-point function.

**End of NONFREE55 (worker claude-opus-5-5; last append 2026-10-29T05:3xZ).**

## §10. Addendum — compatibility with OSLEAF55 as now on disk (read at 05:31Z: §1 formulation, §2 (H_int-sep), §4 Theorem ALG)
1. **The witness is of OSLEAF55's (H_int-sep) form.** For each fixed λ, W_λ(S) = λ⁸S_2(f_λ⊗g_λ) with f_λ⊗g_λ ∈ 𝒟_2 ⊂ 𝒜_𝒟 (compact
   support off the diagonal) and Φ = λ⁸·identity. OSLEAF55's (H_int-sep) passes each such value to the limit along the subsequence,
   and its Lemma DET makes it a function of the reconstructed Euclidean data (agrees with §5.1). The asymptotic family is a countable
   set of such witnesses, each passed separately, exactly as H-RED^e uses them.
2. **(ALG-W) is automatic there.** OSLEAF55 Theorem ALG (iii): a sequence obeying (H_reg-sep) and converging on its determining family
   D converges on all of 𝒜_𝒟. So the family {f_{λ_m}⊗g_{λ_m}} need not be added to D; (ALG-W) reduces to (H_reg-sep), which is OPEN.
3. **Normalisation.** OSLEAF55 D8 allows ê_a := Z(a)⁻¹(e_a − ω(e_a)) with an R-independent Z(a). (TS-e) is stated for Z ≡ 1 (the lane's
   SRC-κ normalisation, the one under which e is the trace anomaly at leading order, §4.1). For another Z, replace ω^c by Z(a)⁻²ω^c.
   T_NF is unchanged if Z(a) → Z_∞ ∈ (0, ∞) (the free class is closed under constant rescaling of the identification); a Z(a) tending
   to 0 or ∞ (e.g. Z = g_0², i.e. studying F² instead of g²F²) changes the limit field and (TS-e) would have to be re-derived for it.
4. **OSLEAF55 confirms independently** that "e(f)²" is not in 𝒜 and that 4D-flowed one-point functions are not on 𝒜 — consistent
   with §5.3.
5. **Symbol collision (systemic defect 1).** "FS" also names OSLEAF55's *Proposition FS* (the forced normalisation of the point-like
   clover field on tori) and BFT_A's *Proposition FS* (funnel spike). Cite this file's result as **NONFREE55 Theorem FS (free side)**.
- **E5 (§9 closing line).** "last append 2026-10-29T05:3xZ": the §9 append ran at 05:29:30Z; this §10 is the last append.

**End of NONFREE55 (claude-opus-5-5).**
- **E6 (§10 heading).** "read at 05:31Z" is wrong: OSLEAF55 was read between 05:29:30Z and 05:30:20Z (`date -u` stamps of the surrounding appends).
