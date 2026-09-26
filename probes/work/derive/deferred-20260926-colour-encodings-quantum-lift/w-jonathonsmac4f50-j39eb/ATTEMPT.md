# No positive evolution reproduces the routed colour rates on the two-pair faithful encoding

- **Task:** `J:derive:deferred-20260926-colour-encodings-quantum-lift:a1`
- **Worker:** `w-jonathonsmac4f50-j39eb`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The sources are Codex campaign files, so this is a cross-family reading. No attempt on this problem existed on `ai/probes` at claim time.
- **Obligation chosen** (one per attempt). For the two-pair encoding, decide whether a completely positive generator on the encoded states reproduces the specified colour rates, or exhibit an obstruction.

## Sources

**Packet** `probes/work/deferred-science-20260926/mobile-record-formation-20260920/campaign12h_second/`, with SHA256:

| file | SHA256 |
|---|---|
| `DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md` | `ab657acc…814e46` (the hash the independent packet read) |
| `CAMPAIGN_REPORT.md` | `63131a4e…c7044` |
| `dimer_two_pair_encoding_independent/REPORT.md` | `3267f5c2…bce5` |

The other listed notes were not used for this obligation; their hashes are in `RECOVERY_STATUS.json`.

**The rates.** From frozen #8600 (`3c6fea4be3`, note SHA256 `03b4434a…1f747`, matching `SOURCE_MAP.json`), §2–3, formula (4):

    c_δ(u) = (1/2)[k0 + h_δ/2],
    h_δ = S_δ(l,a) + S_δ(a,r) − S_δ(l,b) − S_δ(b,r),
    S_δ(x,y) = (γ/2) δ·[e(x)×b(y) + e(y)×b(x)].

- The exchange is between pair `u` and `v = q_δ u`.
- Its contexts are `l = q_δ⁻¹u` and `r = q_δ²u`.
- `a` and `b` are the colours of `u` and `v`.

`origin/main` is `e37967e326`.

**Not addressed here:** frozen #8566, which this unit also owns (see "What would finish it").

## (1) Statement

*Setting.*
- Take the winding matching on the even `N`-torus, `N ≥ 8`. Pair `u` sits at black `u` and white `u + e₁`, and the route displacement is `a_δ = δ − e₁`.
- The classical generator `L` is the sum of all routed exchange channels, at the rates above, with any `γ` and any `k0 > |γ|`.
- The encoding is `E(P) = Σ_config P(config) ⊗_u ρ_{a_u}`, one 16-dimensional factor per pair, using the note's fourteen states `ρ_a`.

*Theorem.* Suppose `γ ≠ 0`. There is a density operator `Y` in the span of encoded states, and a vector `ψ` with `Yψ = 0`, such that

    ⟨ψ| E(L P_Y) |ψ⟩ < 0.

*Consequence.* Let `Φ_t` be any family of positive linear maps with `Φ_t ∘ E = E ∘ e^{tL}` for `t` in some interval `(0, ε)`. No such family exists. In particular:
- no CPTP channels, and no dilation with a fixed ancilla state, reproduce the colour evolution over any short time;
- no Lindblad generator `ℒ` satisfies `ℒ ∘ E = E ∘ L`.

For `γ = 0` the rates are constant, and the swap Lindbladian `(k0/2) Σ (SWAP · SWAP − ·)` does reproduce them. So the obstruction is caused by the colour dependence of the rates.

## (2) Steps

### Step R — the encoding's finite facts (CHECKED R1–R3; independent code)

The states are rebuilt from the note's text (fixed vectors, stabiliser twirls, transporters).
- **R1.**
  - The stabilisers have sizes 4 and 3.
  - The states do not depend on the choice of transporter.
  - All 336 covariance identities hold, checked with integer matrices.
  - `S = I + Σ vvᵀ`, so `ρ ≥ I/Tr S > 0`, with trace denominators 1168 and 2125.
- **R2.** The exact rational rank is 14, computed by DomainMatrix over ℚ. This is disjoint from the packet's modular-minor check and from the author's rank routine.
- **R3.** The alternating-character multiplicity is 0 in `V` and 7 in `End(V)`. The cubic operator `Σ_b b₁b₂b₃ ρ_b` is nonzero, transforms by that character, and has Frobenius² `2516832/903125`, as in the packet.

The note's injectivity and covariance claims are reproduced.

### Step 1 — a necessary condition for positivity (PROVED)

Suppose `Φ_t` is positive and linear with `Φ_t ∘ E = E ∘ e^{tL}`. Let `Y = E(P) ≥ 0`, where `P` is any signed weight (linearity extends the identity), and let `Yψ = 0`.
- `u(t) = ⟨ψ|Φ_t(Y)|ψ⟩ = ⟨ψ|E(e^{tL}P)|ψ⟩ ≥ 0`, and `u(0) = 0`.
- So `u'(0) = ⟨ψ|E(LP)|ψ⟩ ≥ 0`. The right side is finite-dimensional and smooth in `t`.
- For a Lindblad `ℒ = Φ − K· − ·K†` this reads `⟨ψ|Φ(Y)|ψ⟩ ≥ 0`.

### Step 2 — the witness `Y` (PROVED; CHECKED O1, O2)

*The pencil.*
- Exactly, `det(ρ_{+e₁} − tρ_{−e₁}) = c (t − 1)⁸ (19t² − 3174t + 19)(71t² − 11054t + 71)(45t² − 11018t + 45)²`.
- Its smallest root is the double root `t* = (5509 − 4√1896691)/45 ≈ 0.0040843`. Every other root is larger (O1).
- Since `ρ_{−e₁} > 0`, the pencil is definite. So `X = ρ_{+e₁} − t*ρ_{−e₁} ≥ 0`, with `ker X` equal to the eigenspace of the smallest generalised eigenvalue.
- Over ℚ(√1896691), `dim ker X = 2` (O2). Let `φ` be the first basis vector.
- `Tr X = 1 − t* > 0`.

*The state and the vector.* Pick one route direction `δ₀ = +e₂`, a pair 1 at `u₀`, and pair 2 at `u₀ + a_{δ₀}`. Set:
- pair 1: the signed weight `p = e_{+e₁} − t* e_{−e₁}`, so its factor is `X`;
- pair 2: a genuine colour `c₂ = b(1, 1, −1)`;
- every other pair: the colour `c = −e₁`.

Then `Y = X ⊗ ρ_{c₂} ⊗ ρ_c^{⊗(K−2)} ≥ 0`. Take `ψ = φ ⊗ χ ⊗ φ^{⊗(K−2)}`, with `χ = φ + sζ` and `ζ` a fixed integer vector. Then `Yψ = 0`, because `Xφ = 0`.

### Step 3 — only two channels contribute (PROVED; CHECKED O5 against the full channel sum)

Write `f(x) = ⟨φ|ρ_x|φ⟩ > 0` and `g(x) = ⟨χ|ρ_x|χ⟩`. For product `Y` and product `ψ`, each channel contributes

    Σ_colours (weights) × (rate) × [∏ e(after) − ∏ e(before)] × ∏_{pairs outside the footprint} ⟨ψ_v|X_v|ψ_v⟩.

The factor for pair 1 is `⟨φ|X|φ⟩ = 0`. So only channels whose four-pair footprint contains pair 1 survive. The bracket vanishes when the two exchanged pairs carry the same vector `φ`, so pair 2 must be exchanged.

With `d = pair₂ − pair₁ = a_{δ₀}`, the candidates are `d ∈ {±a_δ, ±2a_δ}` (mod `N`). The route displacements `a_δ ∈ {−2e₁, ±e₂ − e₁, ±e₃ − e₁}` have `x`-components −1 or −2. So for even `N ≥ 8`:
- `a_{δ₀} + a_δ ≢ 0` and `a_{δ₀} + 2a_δ ≢ 0` (the `x`-component lies in `[−6, −2]`);
- `a_{δ₀} ≡ 2a_δ` fails for every `δ` (the difference is `±2e_j`, `2e₁`, or has odd `x`-component).

Hence exactly two channels remain:
- **(M)** `(pair₁, δ₀)`: exchanges pair 1 with pair 2; both contexts are background.
- **(Sd)** `(pair₂, δ₀)`: exchanges pair 2 with a background pair; its context `l` is pair 1.

After dividing by the common positive factor `f(c)^{K−4}`:

    M  = f(c)² Σ_a p(a) R(c, a, c₂, c) [f(c₂)g(a) − f(a)g(c₂)],
    Sd = f(c) Σ_a p(a) R(a, c₂, c, c) f(a) [g(c)f(c₂) − g(c₂)f(c)].

Here `R = (1/2)(k0 + γh₁/2)`, and `h₁` is `h` at `γ = 1`. O5 confirms that the complete channel sum over the torus, for `N = 8` and `N = 10`, equals `M + Sd` at the witness to 10⁻⁶ relative.

### Step 4 — the sign (PROVED; CHECKED O3, O4 exactly in ℚ(√1896691))

- `g = f + 2s m + s² n`, with `m(x) = ⟨φ|ρ_x|ζ⟩` and `n(x) = ⟨ζ|ρ_x|ζ⟩`.
- Split `M + Sd = (k0/2) T0(s) + (γ/4) T1(s)`.
- **The `k0` part.** `Σ_a p(a) f(a) = ⟨φ|X|φ⟩ = 0`, so `T0(s) = f(c)² f(c₂) ⟨χ|X|χ⟩ = s² f(c)² f(c₂) ⟨ζ|X|ζ⟩`, with `T0₂ > 0`.
- **The `γ` part.** `T1₀ = 0`, since `g = f` makes both brackets vanish. Exactly, `T1₁ ≈ 0.01179 ≠ 0` and `T1₂ ≈ 15.50` (O3).
- **Negativity.** For `γ ≠ 0`, take `s = −sign(γT1₁)σ` with `0 < σ < |γT1₁| / (2k0 T0₂ + |γT1₂|)`. Then `⟨ψ|E(LP_Y)|ψ⟩ < 0`.
- **Explicit witness.** `γ = 1`, `k0 = 11/10`, `s = −1/10000` gives the value `≈ −1.70×10⁻⁷`, negative exactly (O4).

By Step 1, the Theorem follows. ∎

## (3) Scope and where it stops

**What the result is.**
- It is an exact no-go for this encoding (the product of the note's `ρ_a`), the #8600 routed rates, and the winding matching with `N ≥ 8`.
- It is not a failed search: the witness is explicit.
- Injectivity of the encoding is not used. The argument needs only full-rank overlapping states, for which signed PSD combinations exist, and a nonzero first-order term.

**What it does not cover.**
- Other matchings and moving geometry. The two-channel reduction is proved here only for the winding matching. Other matchings need their own channel census.
- Encodings with extra state variables, shared randomness, or preparation domains that exclude the PSD span elements used here. These change the hypotheses. The task notes the same for #8566.
- Approximate reproduction, for example rates correct only at leading order in `N`.

**Gate.** The result is negative. Before any promotion it needs the N1–N8 gate and an other-family referee.

## (4) What would finish it (remaining obligations)

- **(i) #8566.** Recover the rank-seven marked kernel, the restricted fixed-preparation obstruction and the changed one-event kernel, and verify the restricted obstruction independently. The present result already answers the completely-positive evolution question negatively for the two-pair encoding, without those inputs.
- **(ii) Other geometries.** Extend the census to arbitrary matchings and to moving geometry (plaquette rotations).
- **(iii) A classification.** Determine which colour-dependent exchange rates admit a positive lift on a given overlapping encoding. Step 1 gives the necessary condition. A sufficient criterion would say what a quantum lift must change: the rates, or the encoding.

## ASSUMED

- The supplied model: the encoding as specified in the note, and the #8600 rates.
- Nothing else. The positivity argument (Step 1) and the channel census (Step 3) are proved here. All finite facts are exact, except the float cross-check O5.

## Reproduce

```bash
python3 probes/work/derive/deferred-20260926-colour-encodings-quantum-lift/w-jonathonsmac4f50-j39eb/check.py
```

The run takes under 1 s.
