# Worker b10 analysis: block10 factorization-discharge object matching

Verification worker (Opus 4.8 max, workhorse substitution disclosed). Task: verify or
refute the supervisor's proposed chain discharging Note 4's Gaussian-factorization
hypothesis using the corner notes, with exact quotes for every load-bearing claim.

Files read (ONLY these four):
1. Note 1 = `docs/CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md`
2. Note 2 = `docs/CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md`
3. Note 3 = `docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`
4. Note 4 = `docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`

---

## (a) Note 1: T_hat^2 = Gamma(t) = B^dag B, t = exp(-2E), E = arcsinh(sqrt(m^2+sin^2 p))

**VERDICT: VERIFIED (exact display match).** The mode-set fork does NOT affect this
identification.

Exact display, Note 1 lines 52-57 (section "The supplied surface"):

> "The per-channel transfer engine is the cited free staggered `1+1d` two-step
> construction: for a positive mass `m`, the two-step one-particle kernel is
> `t(p) = exp(-2 E(m,p))`, with
> `E(m,p) = arcsinh(sqrt(m^2 + sin^2 p))`, and the many-body two-step transfer is
> `T_hat^2 = Gamma(t) = B^dag B`, positive Hermitian."

Conventions around it (all quoted / pinned):

- **What `Gamma` is DEFINED as here.** Note 1 gives no standalone definition of
  `Gamma`; it is characterized operationally by the trace correspondence, Note 1
  lines 89-91:
  > "Tr Gamma(t) = det(1 + t) = product_k det(1 + t_k)."
  The `det(1+t)` form (not a Pfaffian / `det(1+..)^{1/2}` form) fixes `Gamma` as the
  **number-conserving fermionic second quantization** (`Gamma(t) = ⊕_n Λ^n t`, so
  `Tr_Fock Gamma(t) = det(1+t)`) — the *multiplicative* second quantization, NOT the
  additive `dΓ`. This is the same `Gamma` Note 4 uses in `T_MB = C(U)·Γ(T_1)`. Load-
  bearing but not spelled out in Note 1; inferred from the `det(1+t)` trace identity.

- **One-step vs two-step.** The kernel `t(p) = exp(-2 E)` is the **two-step** one-
  particle kernel; the many-body object is `T_hat^2` (`T_hat` SQUARED = two-step). The
  identification is between the SQUARED (two-step) many-body transfer and `Gamma` of
  the two-step one-particle kernel. The factor `2` in `exp(-2E)` is the two-step
  doubling (no explicit `a_tau`; see (c)).

- **Which mode set / MODE SET FORK.** Note 1 lines 111-126:
  > "**Mode-set fork -- exhibited, not resolved.** The canonical construction counts
  > channel modes, so the doublet contributes two Fock factors. The registrable
  > readout class is additive over disjoint records and constant on K/CPT orbits, so
  > its registered content is a function of the unordered K-orbit content. Whether the
  > registered Fock occupancy of the doublet is per-channel or per-K-orbit is exactly
  > the orbit-occupancy premise, localized here as one explicit fork in the corner
  > transfer structure's mode bookkeeping."
  > "Both branches map through the runner-rechecked bookkeeping `rho = (pi/g)/Z_d`,
  > `r = 1/(2 rho)`: per-channel counting gives the two-slot cell `r = 1`, while
  > per-K-orbit counting gives the one-slot cell `r = 1/2`. The admissible fork set is
  > the full binary `{1, 1/2}`. The trace correspondence fixes the kernel
  > normalization inside each branch; it does not select between branches."

  **Precise meaning of the fork:** it is a REGISTERED-OCCUPANCY counting choice for the
  K/CPT doublet channels — count the two doublet channels as two Fock slots
  (per-channel → `r = 1`) or as one K-orbit slot (per-K-orbit → `r = 1/2`). It is a
  downstream registration/readout bookkeeping premise (the orbit-occupancy premise),
  NOT a property of the transfer operator.

  **Does it affect the T_hat^2 = Gamma(t) identification? NO.** The identification is
  per-channel (`T_k^2 = Gamma(t_k) = B_k^dag B_k`, Note 1 lines 70-73) and holds
  identically in both branches; the trace correspondence (Note 1, quoted above)
  "fixes the kernel normalization inside each branch; it does not select between
  branches." So the factorization object needed for the block10 discharge is
  fork-INDEPENDENT. The fork only bears on the r-value occupancy count downstream.

- **Per-channel vs full.** The base identity `T_hat^2 = Gamma(t) = B^dag B` is stated
  for a single positive-mass staggered channel (the cited engine). Each of the three
  circulant channels inherits it verbatim, Note 1 lines 70-73:
  > "T_k^2 = Gamma(t_k) = B_k^dag B_k,
  >  t_k(p) = exp(-2 E(lambda_k,p))."
  and the full corner object is the tensor product, Note 1 lines 78-80:
  > "T_corner^2 := tensor_k T_k^2."

---

## (b) Note 2: Tr Gamma(t[U]) = det(1+t[U]); lambda=1 forcing; what t[U] is; relation to Note 3's D[U]

**VERDICT: VERIFIED (both quotes exact).**

Trace-correspondence display, Note 2 lines 83-85 (item N3):

> "Tr Gamma(t[U]) = det(1 + t[U])."

The `lambda = 1` normalization-forcing sentence, Note 2 lines 87-92:

> "The canonical Berezin pair normalization is forced: multiplying each pair measure by
> a positive scalar `lambda` changes the Berezin side by `lambda^N`, so equality for
> arbitrary nonzero determinant requires `lambda = 1`."

**What object `t[U]` is in Note 2.** It is the per-(generation-)channel one-particle
**two-step** transfer kernel at a FIXED spatial gauge background, whose second
quantization is the config-by-config positive transfer. Note 2 lines 46-54:

> "The retained fixed-background engine gives the position-space two-step staggered
> transfer construction. At fixed `U`, the spatial hop is anti-Hermitian; each positive
> channel mass `lambda_k` therefore inherits config-by-config two-step positivity:
> `T_k^2[U] = B_k[U]^dag B_k[U] >= 0`."

Note 2 does NOT give `t[U]` a closed symbol form (Note 1 did: `t(p)=exp(-2E)`); it uses
`t[U]` as the one-particle kernel inside `Tr Gamma(t[U]) = det(1+t[U])` and gives the
per-channel positivity `T_k^2[U] = B_k[U]^dag B_k[U]`. The channels here are the three
GENERATION channels of the circulant internal triplet (Note 2 lines 30-45), each a
staggered 1+1d fermion at fixed spatial background.

**Relation to Note 3's `D[U]`.** Note 3's `D[U]` is the SPATIAL-position-space covariant
radicand, Note 3 lines 50-54 (eq. 1):

> "D[U]   = m^2 I + ( sum_{mu=1}^d s_mu[U] )^2 ."

and the reconstructed single-particle Hamiltonian, Note 3 lines 59-61 (eq. 2):

> "h[U] = arcsinh( sqrt( D[U] ) ),"

with eigenvalues (Note 3 lines 62-66) `E_j[U] = arcsinh(sqrt(m^2 + lambda_j(U)^2))`.
The bridge is `t[U] = exp(-2 a_tau h[U]) = exp(-2 a_tau·arcsinh(sqrt(D[U])))`, with the
scalar mass `m` of Note 3 playing the role of the channel mass `lambda_k` in the corner
setting (so per channel `t_k[U] = exp(-2 a_tau·arcsinh(sqrt(lambda_k^2 I + (sum_mu
s_mu[U])^2)))`). At `U = 1`, `sum_mu s_mu` has symbol `sin p`, so `E_j → arcsinh(sqrt(
m^2 + sin^2 p)) = E(m,p)`, recovering Note 1's `t(p) = exp(-2E)`. NOTE the decomposition
axis differs: Note 2's `t[U]` is indexed by GENERATION channel (circulant/internal),
Note 3's `D[U]` is a SPATIAL-lattice operator; they align only through the symbol
identity at `U=1` and through `m ↔ lambda_k` per channel — the exact operator
identity `T_k^2[U] = Gamma(t_k[U])` at fixed `U` is carried by the cited fixed-gauge
engine, not re-displayed in Note 2 (see (d), LIMITS).

---

## (c) Note 3: h[U] = -log(T_hat^2)/(2 a_tau) and h[U] = arcsinh(sqrt(D[U])); verify -log t[U] = 2 a_tau h[U]

**VERDICT: VERIFIED as an identity given the two definitions, BUT reconciliation with
Note 1/2 forces `a_tau = 1` (unstated there), and there is a `T_hat^2` notation clash to
flag.**

First definition, Note 3 lines 22-26 (Role), quoting the free anchor verbatim:

> "the reconstructed single-particle Hamiltonian `h = -log(T_hat^2)/(2 a_tau)` has a
> **sharp** exponential kernel rate `arcsinh(m)`, proved by a Fourier / Paley-Wiener
> torus contour shift."

Second definition, Note 3 lines 59-61 (eq. 2):

> "h[U] = arcsinh( sqrt( D[U] ) ),"

**Arithmetic check `-log t[U] = 2 a_tau h[U]`.** Rearranging the first display,
`h = -log(T_hat^2)/(2 a_tau)` ⟺ `-log(T_hat^2) = 2 a_tau h`. Identifying the ONE-PARTICLE
`T_hat^2` of this formula with `t[U]` (Note 2's one-particle two-step kernel) gives
`-log t[U] = 2 a_tau h[U]` — TRUE, but tautologically: it is just the rearrangement of the
definition `h = -log(t)/(2 a_tau)`. It carries content only once `h[U] = arcsinh(sqrt(
D[U]))` is substituted: `t[U] = exp(-2 a_tau·arcsinh(sqrt(D[U])))`.

**Factor tracking (every factor):**
- Coefficient `2`: two-step doubling. Present on BOTH sides consistently (`exp(-2...)`
  ↔ `-log = 2...`). OK.
- `a_tau`: **MISMATCH TO FLAG.** Note 3 carries an explicit `2 a_tau`. Note 1 writes
  `t(p) = exp(-2 E)` (line 55) with **no `a_tau`**, and Note 1's `E(m,p) =
  arcsinh(sqrt(m^2+sin^2 p))` is the SAME expression as Note 3's `h` eigenvalue
  `E_j = arcsinh(sqrt(m^2+lambda_j^2))` at `U=1`. Reconciling `-log t = 2E` (Note 1)
  with `-log t = 2 a_tau h = 2 a_tau E` (Note 3) requires `a_tau = 1`. So Note 1/2
  silently adopt the lattice temporal spacing `a_tau = 1`; Note 3 keeps it symbolic.
  The two are consistent ONLY at `a_tau = 1`. Standard lattice-unit convention, but
  never stated in Note 1/2 — supervisor must confirm the shared convention.
- per-channel vs position-space: Note 3's `D[U]`/`h[U]` are POSITION-SPACE (spatial
  covariant); Note 1/2's `t[U]`/`t_k` are per-GENERATION-channel with mass `lambda_k`.
  They agree at `U=1` via the symbol `sin^2 p` and under `m ↔ lambda_k` per channel.
  No numeric factor is dropped; only the indexing axis differs.

**Notation hazard (flag).** The symbol `T_hat^2` means the MANY-BODY two-step transfer
in Note 1 (`T_hat^2 = Gamma(t) = B^dag B`, line 56) but the ONE-PARTICLE two-step
transfer in Note 3's formula `h = -log(T_hat^2)/(2 a_tau)` (line 24) — because `h` there
is the "reconstructed single-particle Hamiltonian" with a per-site "kernel rate"
`<x|h[U]|y>`, which forces `T_hat^2` in that formula to be the one-particle object
(= Note 1/2's `t`). Same glyph, different object across notes. Load-bearing for reading
the chain correctly; not an error, but a trap.

---

## (d) Note 4 hypothesis T_MB[U] = C(U) Gamma(T_1[U]); does the discharge (T_MB=T_hat^2, T_1=t[U], C=1) match AS STATED?

**VERDICT: STRUCTURALLY VERIFIED — the discharge is the `C=1` instance of Note 4's
`C(U)>0` hypothesis, and `C=1` is stated verbatim in Note 1. One wording gap: at fixed
`U` the full operator identity is Note 1's free identity + cited engine, not a Note 2
display.**

Note 4's factorization hypothesis, lines 82-91 (Hypotheses):

> "a positive, number-conserving **Gaussian factorization** `T_MB[U] = C(U)·Γ(T_1[U])`
> with scalar `C(U) > 0` (then `−log T_MB = −log C(U)·1 + dΓ(−log T_1)`, and the scalar
> term is an identity shift that drops from every commutator — gated). A one-particle
> kernel alone does NOT imply the factorization (review counterexample:
> `Γ(e^{−h})·e^{−g n_1 n_2}` has the same one-particle restriction but a quartic log).
> Without the factorization hypothesis, only the bilinear theorem is claimed."

**Matching the proposed discharge (`T_MB = T_hat^2`, `T_1 = t[U]`, `C = 1`):**

- `T_MB[U] = T_hat^2` and `T_1[U] = t[U]`, `C(U) = 1` gives `T_hat^2 = 1·Γ(t[U]) =
  Γ(t[U])`. This is exactly Note 1's identity `T_hat^2 = Gamma(t)` (line 56, free) and
  its fixed-background extension via Note 2's `Tr Gamma(t[U]) = det(1+t[U])` (line 84)
  plus per-channel `T_k^2[U] = B_k[U]^dag B_k[U]` (line 52). So the corner-note identity
  is the `C(U)=1` special case of Note 4's factorization. **Matches as stated.**
- Qualifier "positive": corner notes give `T_hat^2 = B^dag B`, "positive Hermitian"
  (Note 1 line 56; Note 2 lines 52, 62). OK.
- Qualifier "number-conserving": the `det(1+t)` trace form (Note 1 line 89; Note 2
  line 84) is the number-conserving second quantization (`⊕_n Λ^n t`), so `Γ(t[U])` is
  number-conserving. OK.
- Scalar `C(U)`: corner notes assert `C = 1` (no prefactor on `T_hat^2 = Gamma(t)`).
  Even if the physical free-fermion two-step transfer carried a config-dependent vacuum
  scalar `C(U) ≠ 1`, Note 4 states the scalar "drops from every commutator" (line 85),
  so the LR conclusion is insensitive to it. The discharge is therefore robust to
  whether `C = 1` exactly or `C(U)` is a nontrivial scalar.

**Why the discharge is legitimate against Note 4's own counterexample.** Note 4's
counterexample (`Γ(e^{−h})e^{−g n_1 n_2}`, quartic log) shows the one-particle kernel
does NOT by itself force Gaussianity. The corner notes evade this precisely because
they work with the **free (quadratic) staggered fermion**, whose many-body two-step
transfer IS `Γ(one-particle kernel)` by construction — that is the content of
`T_hat^2 = Gamma(t) = B^dag B` (Note 1) — so on the corner surface the factorization is
an established identity, not an assumption. This is consistent with Note 4's own scope
note (claim_scope, line 4 / Non-Claims lines 283-286): the identification is claimed
only for the "free/quadratic class"; "for non-quadratic transfer operators the theorem
is an LR bound for the bilinear dynamics itself, with no identification claimed."

**Wording gap (the one thing that differs).** At FIXED background, Note 2 displays
(i) per-channel positivity `T_k^2[U] = B_k[U]^dag B_k[U] >= 0` (line 52) and (ii) the
trace correspondence `Tr Gamma(t[U]) = det(1+t[U])` (line 84) — it does NOT re-display
the operator identity `T_MB[U] = Γ(t[U])` (i.e. `T_k^2[U] = Γ(t_k[U])`) as a single line.
That operator identity is Note 1's free statement (`T_hat^2 = Gamma(t)`) plus the cited
fixed-gauge engine (`RP_P2_GAUGE_EXTENSION...`, Note 2 dependency line 157), inherited
not re-proved in Note 2. So the `C=1` discharge at fixed `U` rests partly on a cited
authority I was not permitted to open (see LIMITS).

---

## (e) POSITIVITY: is t (and t[U]) positive with spectrum in (0,1] or (0,inf)? (Needed for -log t)

**VERDICT: PARTIAL — spectrum is in `(0,1]`, NOT `(0,inf)`. But strict positivity (needed
for `-log t`) is EXPLICIT only via Note 1's `exp(-2E)` form; Note 2 states only `>= 0`
(positive SEMIdefinite), so strict lower-boundedness at fixed `U` leans on the `m>0`
mass gap supplied by Note 3.**

- **Note 1** gives the explicit symbol, line 55: `t(p) = exp(-2 E(m,p))` with `E(m,p) =
  arcsinh(sqrt(m^2 + sin^2 p))`. Since `E >= arcsinh(m) > 0` for `m>0`, this is manifestly
  `t(p) ∈ (0, e^{-2·arcsinh(m)}] ⊂ (0,1)` — **strictly positive and ≤ 1** (spectrum in
  `(0,1]`, bounded away from both 0 and 1). Note 1 does not write "spec(t) ⊂ (0,1]"
  explicitly; it follows from the quoted `exp(-2E)` formula. Note 1 states the many-body
  object is "positive Hermitian" (line 56).
- **Note 2** states only positive SEMIdefiniteness, line 52: `T_k^2[U] = B_k[U]^dag
  B_k[U] >= 0`, and "positive Hermitian config-by-config" (line 62). Literally, `B^dag B
  >= 0` admits a zero eigenvalue; it does NOT by itself give the strict lower bound
  `t[U] > 0` that `-log t[U]` and `dΓ(-log t[U])` require. Note 2 supplies no `exp(-2E)`
  form of its own.
- **Where strict positivity actually comes from at fixed `U`:** Note 3's uniform gap,
  lines 88-94 (G1):
  > "m^2 I  <=  D[U]  <=  (m^2 + d^2) I ,    i.e.  spec(D[U]) subset [m^2, m^2 + d^2],"
  with (line 93) "`dist(spec(D[U]), (-inf, 0]) = m^2 > 0`". Hence `h[U] = arcsinh(sqrt(
  D[U])) >= arcsinh(m) > 0`, so `t[U] = exp(-2 a_tau h[U]) ∈ (0, e^{-2 a_tau·arcsinh m}]
  ⊂ (0,1)`, strictly positive. So `-log t[U]` is well-defined, but the strict bound is
  carried by Note 3's `m>0` gap (equivalently Note 1's `exp(-2E)` form), NOT by Note 2's
  `>= 0`.

**Consequence for the chain:** `t, t[U] ∈ (0,1]` (bounded above by 1, so `h = -log t/(2
a_tau) >= 0` — a genuine positive Hamiltonian, consistent). The `(0,1]` bound, not
`(0,inf)`, is the correct one. The load-bearing STRICT positivity for `-log` is present,
but sourced from the mass gap `m>0` (Note 1 exp-form / Note 3 G1), not from Note 2's
semidefinite `B^dag B >= 0` alone.

---

## (f) SCOPE: what surface do the corner notes cover? The discharge inherits exactly that.

**VERDICT: corner notes cover FREE (U=1) and FIXED-gauge-background staggered `1+1d`
(one spatial dimension). MAJOR MISMATCH: Note 4's activity feed is on `Z^3` (d=3). The
Gaussian-factorization discharge sourced from the corner notes is a `d=1` statement and
does NOT, as stated, cover Note 4's `d=3` surface.**

**Note 1 scope (FREE, U=1, per-channel, 1+1d):**
- lines 18-19: "This note establishes the five items below on the free corner-axis
  surface over the supplied positivity domain only."
- lines 23-26: "The result is free (`U = 1`) and per-channel. It does not claim a gauge
  extension, a full-dynamics corner theorem, physical-time derivation, a positive-mass
  derivation, a selector for the registered doublet mode set, or a route resolution
  beyond the stated free construction."
- theorem, lines 61-64: "Take the free staggered `1+1d` action of the cited
  construction, with the internal generation triplet carried by the supplied circulant
  mass term `H(delta)` above, on the supplied positivity domain where all three channel
  masses are positive."

**Note 2 scope (FIXED background only, 1+1d, U(1) witness / general fixed SU(3)/U(1),
NOT U-integrated):**
- lines 15-19: "FIREWALL: fixed background only. This note proves (N1)--(N5) on the
  supplied corner-axis surface at a fixed spatial gauge background in temporal gauge.
  The computed witness class is arbitrary finite `U(1)` phase backgrounds at `L_s = 2`;
  the retained fixed-gauge engine supplies the general fixed-background `SU(3)`/`U(1)`
  authority. The note does **not** integrate over backgrounds, does **not** supply the
  gauge measure..."
- lines 30-32: "Work with the staggered `1+1d` action at a fixed spatial background
  `{U_i(x)}` in temporal gauge."
- Does NOT list, lines 144-153: "Does not integrate over gauge backgrounds. / Does not
  supply or select the gauge measure. ... Does not claim that the U-INTEGRATED level has
  been handled."

**The mismatch, made precise.** Note 4 is on `Z^3` (three SPATIAL dimensions):
- Note 4 lines 108-114: "On `Z^3`: `||z||_1 ≤ 3 ||z||_∞` ... the `l_∞` sphere ... has
  exactly `(2r+1)^3 − (2r−1)^3 = 24r^2 + 2` points" (the `Z^3` shell count), and
- claim_scope (line 4, F5): "the threshold `mu < gamma_CT/3` is the `d = 3` instance of
  the landed free-bilinear note's `d·mu < eta` pattern."

The one-particle kernel BOUND Note 4 feeds is fine at `d=3` — Note 3 (CT) is dimension-
general (`D[U] = m^2 I + (sum_{mu=1}^d s_mu)^2`, `B(2,d) = 5^{d-1}·6`, tested `d=1,2`).
But the GAUSSIAN FACTORIZATION `T_MB = C·Γ(T_1)` that the corner notes would discharge is
established by Note 1/2 only for staggered `1+1d` (d=1 spatial). Free-fermion many-body
transfer `= Γ(one-particle)` is generically dimension-independent in spirit, but the
corner notes AS WRITTEN prove it only at `1+1d`; they contain no 3+1d construction and
no general free-fermion second-quantization theorem. **Therefore the discharge inherits
`d=1`, and does not cover Note 4's `d=3` usage without a separate, unstated dimensional
extension.** This is the load-bearing scope finding.

---

## (g) LIMITS

1. **`a_tau = 1` is unstated.** Note 1/2 write `t = exp(-2E)` with no `a_tau`; Note 3
   carries explicit `2 a_tau`. They reconcile only at `a_tau = 1`. Standard lattice
   convention, but the supervisor must confirm the shared temporal-spacing convention
   before treating `-log t = 2 a_tau h` as more than a definitional rearrangement.

2. **Dimension gap (d=1 vs d=3) is the biggest issue.** The corner-note factorization
   discharge is a `1+1d` (d=1 spatial) statement; Note 4's theorem lives on `Z^3`
   (d=3). The corner notes do NOT establish `T_MB = C·Γ(T_1)` at `d=3`. To discharge
   Note 4's hypothesis at its actual surface, the supervisor needs either a separate
   3+1d free-fermion second-quantization argument, or must restrict the discharge claim
   to `d=1` (which is not where Note 4 applies it). Do not let the structural match in
   (d) paper over the surface mismatch in (f).

3. **Cited engines not read (spec restricted me to 4 files).** The exact fixed-`U`
   operator identity `T_k^2[U] = Γ(t_k[U])` and the strict-positivity/spectrum bound at
   fixed background live in `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_
   2026-05-28` (Note 1 dep) and `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_
   2026-05-28` (Note 2 dep). Note 2 displays only `B^dag B >= 0` and the trace
   correspondence, inheriting the operator identity from those engines. Supervisor must
   verify those engines actually carry (i) the `C=1` operator identity at fixed `U` and
   (ii) `t[U] ∈ (0,1]` config-by-config.

4. **`T_hat^2` glyph is overloaded.** Many-body in Note 1 (`= Gamma(t)`), one-particle
   in Note 3's `h = -log(T_hat^2)/(2 a_tau)`. Not an error but a reading trap; any write-
   up must disambiguate.

5. **Object identification `T_MB` (Note 4) = `T_hat^2` (corner) is only structural.**
   I confirmed it holds on the free/quadratic surface (where the factorization is an
   identity, evading Note 4's quartic-log counterexample). Whether the physical many-
   body log-transfer generator of the microcausality program is literally the corner
   notes' free staggered two-step transfer is an identification I could check only for
   consistency, not derive. The overall scalar `C(U)` is set to 1 by corner assertion;
   it drops from commutators regardless (Note 4 line 85), so this does not threaten the
   LR bound — but it does mean "`C=1` exactly" is an assertion, not a computed value.

6. **Decomposition-axis mismatch (generation vs spatial).** Note 1/2 decompose by
   GENERATION channel (circulant internal triplet, mass `lambda_k`); Note 3/4 work in
   SPATIAL position space (mass `m`). The bridge `m ↔ lambda_k` per channel and the
   symbol identity at `U=1` are coherent, but the full alignment (three generation
   channels × `Z^3` spatial lattice) is not written out in any of the four notes; it is
   assumed. Supervisor should confirm the intended total one-particle space.
