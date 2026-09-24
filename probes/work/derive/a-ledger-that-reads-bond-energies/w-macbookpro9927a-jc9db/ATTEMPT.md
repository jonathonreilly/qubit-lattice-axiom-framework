# a-ledger-that-reads-bond-energies, attempt a2: the moved clock's bond part is the missing field

Worker `w-macbookpro9927a-jc9db` (`claude-opus-5-5`), unit `J-derive-a-ledger-that-reads-bond-energies-a2`.

**Sources.** I read these notes as landed on origin/main `0e6ad8285096`:
- block 106 (PR #8939, landed as "Periodic momentum weights and exact bond-force identities");
- block 66 (#8597);
- block 64 (#8595);
- block 63 (#8593).

I also read block 106's PR head `b8a4e01b96` and block 66's `c4afb022c2`. The definitions used below are the landed ones, and they agree with the PR heads.

**Provenance and independence.**
- **No prior attempts.** No attempt at this problem was on ai/probes at claim time, so there was nothing to read first.
- **Origin of the plan.** The plan is my own: promote the clock to an operator, and take its bond part as the field. It starts from two remarks in block 66:
  - "on the lattice what [a relabelling] makes of a rate is not a rate: it is the hop `Λ_ξ`";
  - its N1.3: "whether some lattice ledger has T3's exact force density on its right-hand side is the named next step".
- **Block 106's T2 and T3.** These came from probes workers of this machine (`w-macbookpro90c72-j5c0d` and `-j152a`, Claude Opus 5.5), and a Grok model refereed them. I use only their landed statements, and I re-check T2 exactly (family Q).
- **Block 106 as landed.** Its T3 says the equal-data obstruction "does not exclude functionals of perturbed densities, additional bond variables, their derivatives or nonlocal information". This attempt builds such a ledger with an additional bond variable.
- **A related earlier unit of this worker.** `deferred-20260924-ledger` (#9060) asked which placements of the walk's momentum current can source block 62's member. It is a different question, and nothing from it is used here.

## 1. What is attempted

**Setting.** Everything here is supplied; nothing is adopted.
- **Lattice, state and clock.**
  - The torus is `Z_L³` with `L ≥ 3`, and `ψ` maps sites to `C²`.
  - `S_a = (T_a − T_a†)/(2i)` and `H = Σ_a σ_a S_a`.
  - The clock root is `φ > 0`, with `u = 2 log φ` and `H_w = φHφ`.
- **Densities.** Notation from blocks 66 and 106:
  - `χ = Hφψ`, `ρ_x = Re ψ_x†χ_x` and `𝔢 = φρ`;
  - `C_j[v]ψ(x) = (v(x)ψ(x+e_j) + v(x−e_j)ψ(x−e_j))/2` and `d_jφ(x) = φ(x+e_j) − φ(x)`;
  - `f_j(x) = Re[(C_j[d_jφ]ψ)†χ + ψ†C_j[d_jφ]χ](x)`;
  - `ε_(x,j) = ½Re[ψ(x+e_j)†χ(x) + ψ(x)†χ(x+e_j)]`.
- **Relabelling and strains.**
  - `G_ξ = ½Σ_j{ξ_j, S_j}` and `Λ_ξ = ½Σ_j{ξ_j, C_j[d_jφ]}` (block 66).
  - The bond current is `J_a^j[·]` (block 63).
  - `H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`, with the relabelling `B → B + dξ` and the curls `F_ab^j = d_aB_b^j − d_bB_a^j` (block 64).

**New supplied objects.**
- `h_b = C_j[δ_b]`, the symmetric hop on the bond `b = (x, j)`, with coin identity.
- A real bond field `κ_b` and the **clock operator** `Φ = φ + K`, where `K = Σ_b κ_b h_b`.
- The content's energy `E_c(B, Φ; ψ) = ⟨ψ|ΦH[B]Φ|ψ⟩`. At `B = 0`, `κ = 0` it is block 54's walk.
- The **moved bond part** `δκ*_(x,j)(ξ) = −½ d_jφ(x)(ξ_j(x) + ξ_j(x+e_j))`.
- The **relabelling of the ledger's fields** `T_ξ`: `B → B + dξ`, `u → u`, `κ → κ + δκ*(ξ)`.
- The content's responses are taken at `B = 0`, `κ = 0` (first order in the fields), as in blocks 66 and 106.

**Claims.**

- **(A) Every blind ledger demands the walk's law exactly.**
  - Let `F(B, u, κ)` be any differentiable function unchanged by `T_ξ` for every `ξ`.
  - Its static equations are `∂F/∂B = −J[φψ]` and `∂F/∂κ = −2ε`.
  - They demand `Σ_a[J_a^j(x) − J_a^j(x − e_a)] = −f_j(x)` at every site, which is block 66 T3(d)'s law. Equivalently, `d⟨G_ξ⟩/dt = 0` for every `ξ`.
  - This holds for every state and every positive rate field, at all orders in the rate gradient and at every wave number.
  - The demanded force density is exactly `f_j(x) = d_jφ(x)ε_(x,j) + d_jφ(x−e_j)ε_(x−e_j,j)`.
- **(B) A local member exists, and its static equations can be solved exactly when the law holds.**
  - The member is `F₂ = ½Σ_x w_x[Σ_{a<b,j} F_ab^j(x)² + Σ_{a,j} Ĩ_aj(x)²]`, with

    `Ĩ_aj(x) = −2[d_jφ(x)κ_(x+e_a,j) − d_jφ(x+e_a)κ_(x,j)] − d_jφ(x)d_jφ(x+e_a)[B_a^j(x) + B_a^j(x+e_j)]`.

  - It is unchanged by every finite relabelling `T_ξ`.
  - Suppose no bond is flat (`d_jφ ≠ 0` on every bond) and `L ≥ 3`. Then its static equations `∂F₂/∂B = −J[φψ]`, `∂F₂/∂κ = −2ε[ψ]` have a solution iff the law in (A) holds, and the solution is unique up to `T_ξ`.
- **(C) The transport is forced, and a bond field is needed** (`L ≥ 5`).
  - **Setting.** Let the fields be `(B, u, κ)`, with `B → B + dξ` and any transport `(δu[ξ], δκ[ξ])` linear in `ξ`.
  - **The criterion.** The static equations, including `∂F/∂u = −𝔢`, demand the force density `f` at every state iff `δΦ_ξ − δΦ*_ξ ∈ 𝒩(φ) = {δΦ : δΦHφ + φHδΦ = 0}` for every `ξ`. Here:
    - `δΦ_ξ = diag(φδu/2) + Σ_b δκ_b h_b`;
    - `δΦ*_ξ = −Λ_ξ`.
  - **The null space.**
    - The site part of `𝒩` is `span{Γφ}` for even `L` and `0` for odd `L`.
    - The bond part vanishes on every bond `(x, b)` that has a transverse direction `a` with `d_bu(x) + d_bu(x+e_a) ≠ 0`.
  - **Consequences.**
    - Under that rate condition the transport is forced: `δκ = δκ*` and `δu ∈ span{Γ}`.
    - Without a bond field, no transport of the rates demands `f` once one bond is not flat. A two-site state with zero energy density everywhere and a force is the witness.
- **(D) The continuum reading.** On smooth amplitudes the moved bond part acts as multiplication by `−hξ·∇φ + O(h³)`, the carried rate of block 66's T1.
- **(S) Side result: tori with every side even.**
  - `U_c = σ_cΓ_aΓ_b` (with `Γ_a = (−1)^{x_a}`) and `Θ = σ_2K` commute with `H_w` for every rate field.
  - Every level of `H_w` has even dimension.
  - Every eigenstate in a twofold level, and every eigenstate at `E = 0`, has `ε ≡ 0` and `J[φψ] ≡ 0`, so `f ≡ 0`.

## 2. Steps

0. **ASSUMED (supplied clauses).**
   - The walk, rates, strains and relabellings of blocks 54, 63, 64 and 66, as landed.
   - The new clause that the content is timed by a clock operator `Φ = φ + K` with a nearest-neighbour bond part.
   - Nothing is adopted.

1. **PROVED; CHECKED Q1 (the moved clock).**
   - For a site function `ξ`, `{ξ, h_b} = (ξ(x) + ξ(x+e_j))h_b`: `ξh_b` puts `ξ(x)` on `|x⟩⟨y|` and `ξ(y)` on `|y⟩⟨x|`, and `h_bξ` the reverse.
   - `C_j[v] = Σ_{b ∥ j} v_b h_b`, read off from its definition.
   - Hence `Λ_ξ = Σ_b ½d_jφ_b(ξ_j(x) + ξ_j(x+e_j))h_b = −Σ_b δκ*_b h_b`. This is a pure bond operator.
   - Block 66 T3(a),(b) gives `i[φ, G_ξ] = −Λ_ξ`.
     - The proof is its shift formula: `[φ, S_j]ψ(x) = (1/(2i))[(φ(x) − φ(x+e_j))ψ(x+e_j) − (φ(x) − φ(x−e_j))ψ(x−e_j)]`.
     - Summing, `i[φ, G_ξ] = ½Σ_j{ξ_j, i[φ, S_j]} = −Λ_ξ`.
   - So `e^{−iG_ξ}φe^{iG_ξ} = φ − i[G_ξ, φ] + O(ξ²) = φ + i[φ, G_ξ] + O(ξ²) = φ − Λ_ξ + O(ξ²)`.
     - The site part is unchanged at first order.
     - The bond part moves by `δκ*`.
   - Check Q1: the operator identity is exact on all 128 basis vectors of `4³`, for random rational `φ` and integer `ξ`; `Λ_ξ` has no diagonal entries.

2. **PROVED; CHECKED Q2 (the content's responses at `B = 0`, `κ = 0`).**
   - **The bond field.** `∂E_c/∂κ_b = ⟨ψ|h_bHφ + φHh_b|ψ⟩ = 2Re⟨h_bψ|χ⟩`. Since `(h_bψ)(x) = ½ψ(y)` and `(h_bψ)(y) = ½ψ(x)`, this is `Re[ψ(y)†χ(x) + ψ(x)†χ(y)] = 2ε_b`.
   - **The strain.** `∂E_c/∂B_a^j(x) = J_a^j[φψ](x)`. This is block 64 T1(b) for the state `φψ`; `⟨H[B]⟩` is linear in `B`.
   - **The rates.** `∂E_c/∂φ_x = 2ρ_x`, so `∂E_c/∂u_x = (φ_x/2)·2ρ_x = 𝔢_x`.
   - Check Q2: exact symmetric differences on `4³`. `E_c` is quadratic in `κ` and in `φ` and linear in `B`, so the differences equal the derivatives.

3. **PROVED; CHECKED Q3 (the content is unchanged by the joint move).** For every `ψ`, `φ` and `ξ`:

   `⟨ψ|i[G_ξ, H_w]|ψ⟩ + Σ_{x,a,j}(d_aξ_j)(x)J_a^j[φψ](x) + Σ_b 2ε_b δκ*_b(ξ) = 0.`

   - **The first term.** Block 66 T3(c) gives `⟨i[H_w, G_ξ]⟩ = Σ(dξ)J[φψ] − Σ_x ξ·f`.
   - **The force.** Block 106 T2's bond form `f_j(x) = d_jφ(x)ε_(x,j) + d_jφ(x−e_j)ε_(x−e_j,j)` gives, after collecting by bonds,

     `Σ_x ξ·f = Σ_b ε_b d_jφ_b(ξ_j(x) + ξ_j(x+e_j)) = −Σ_b 2ε_b δκ*_b`.

   - **Reading.** The content's energy is unchanged at first order when three things happen together: the state is relabelled by `e^{−iG_ξ}`, the strain moves by `dξ`, and the clock moves to `φ − Λ_ξ`.
   - Check Q3, on `4³` with a random Gaussian-rational state:
     - T2's bond form at all 192 site-directions;
     - T3(c);
     - the displayed sum, with `d⟨G_ξ⟩/dt ≈ −139.15` for that state.

4. **PROVED (claim A).**
   - **The identity.** Differentiate `F(T_ξ(B, u, κ)) = F(B, u, κ)` at `ξ = 0`:

     `Σ_{x,a,j}(d_aξ_j)(x)E_a^j(x) + Σ_b δκ*_b(ξ) K_b = 0`, with `E = ∂F/∂B` and `K = ∂F/∂κ`.

   - **Site form.** Summing by parts, for arbitrary `ξ`:

     `Σ_a[E_a^j(x) − E_a^j(x−e_a)] = −½[d_jφ(x)K_(x,j) + d_jφ(x−e_j)K_(x−e_j,j)]`.

   - **The demand.** Put in the static equations `E = −J[φψ]` and `K = −2ε`. The right side becomes `d_jφ(x)ε_(x,j) + d_jφ(x−e_j)ε_(x−e_j,j) = f_j(x)`, so the demand is `div J^j[φψ](x) = −f_j(x)`. By step 3 this is the same as `d⟨G_ξ⟩/dt = 0` for all `ξ`.
   - **No approximation.** Nothing is expanded in the rate gradient, and no wave number enters.
   - **The contrast with block 106.** Block 106 T3's two plane waves have equal `𝔢` and zero `J`, but bond energies along `e_1` of `0` and `2` (check E1). The requirement here reads that difference.
   - Checks:
     - I2: the site form for the member `F₂` at random fields on `3³` and `4³`, at every site-direction;
     - I3: with the static sources of a random state, the identity's residual `−div J − f`, paired with `ξ`, equals `d⟨G_ξ⟩/dt` exactly, and is nonzero for that non-stationary state.

5. **PROVED; CHECKED I1 (the member is unchanged by relabellings).**
   - **Curls.** They are unchanged because `d_ad_b = d_bd_a` (block 64 T1(a)).
   - **The bond invariants.** Under `T_ξ`:
     - the `κ`-terms of `Ĩ_aj(x)` move by `d_jφ(x)d_jφ(x+e_a)[(ξ_j(x+e_a) + ξ_j(x+e_a+e_j)) − (ξ_j(x) + ξ_j(x+e_j))]`;
     - the `B`-terms move by `−d_jφ(x)d_jφ(x+e_a)[(d_aξ_j)(x) + (d_aξ_j)(x+e_j)]`, which is the negative of that.
   - **Finite relabellings.** `T_ξ` is affine in `(B, κ)` at fixed `u`, so invariance holds for finite `ξ`. The rates enter only as the site weights `w_x` and through the fixed coefficients `d_jφ`.
   - **Block 64's blindness.** It is kept verbatim for the curl part.
   - Check I1: all `9N` curls and `9N` bond invariants are unchanged by a random finite `ξ` on `3³` and `4³`.

6. **PROVED for every `L ≥ 3`; CHECKED R1–R2 on `3³` and `4³` (the kernel).** Let `A` be the map `(B, κ) ↦ (curls, Ĩ)` and `V: ξ ↦ (dξ, δκ*(ξ))`. When no bond is flat, `ker A = span V`.
   - **(i) Curl-free strains.** For each `j`, a curl-free `B^j` is `dΞ_j + h^j`, with `h^j` constant.
     - Fourier on the torus: for `q ≠ 0` pick `a` with `D_a(q) = e^{iq_a} − 1 ≠ 0` and put `Ξ̂ = B̂_a/D_a`. Zero curl gives `D_aB̂_b = D_bB̂_a`, hence `B̂_b = D_bΞ̂` for every `b`. The choice of `a` does not matter, and `Ξ̂(−q) = conj Ξ̂(q)`.
     - `q = 0` gives the constants.
   - **(ii) The bond field.** With no flat bond, put `μ_b = −2κ_b/d_jφ_b` and `ν_b = μ_b − Ξ_j(x) − Ξ_j(x+e_j)`.
     - `Ĩ_aj(x) = d_jφ(x)d_jφ(x+e_a)[μ_(x+e_a,j) − μ_(x,j) − B_a^j(x) − B_a^j(x+e_j)]`, so `Ĩ = 0` reads `ν_(x+e_a,j) − ν_(x,j) = 2h_a^j`.
     - Summing around an `a`-cycle gives `2Lh_a^j = 0`.
     - So `ν_(·,j)` is a constant `c_j`, because the bonds along `j` are joined by the steps `e_a`.
   - **(iii) The gauge form.** Then `(B, κ) = V(ξ)` with `ξ_j = Ξ_j + c_j/2`. Conversely, `V(ξ) ∈ ker A` by step 5.
   - **(iv) `V` is injective** when each direction has a non-flat bond. `V(ξ) = 0` gives `dξ = 0`, so `ξ` is uniform; then `δκ* = −d_jφ ξ_j = 0` on a non-flat bond, so `ξ = 0`.
   - **Certificate** (R1–R2), on `3³` and `4³` with random rates having no flat bond:
     - `A·V(e_{y,j}) = 0` exactly on all `3N` gauge basis vectors;
     - rank `V = 3N` and rank `A = 9N` modulo `2³¹ − 1`. The rank modulo a prime is a lower bound for the rational rank, and it meets the upper bound `12N − 3N`.

7. **PROVED (claim B).**
   - **Kernel and range.** The Hessian of `F₂` is `M = AᵀWA` with `W = diag(w_x) > 0`. So `ker M = ker A = span V`, and `range M = (span V)^⊥`.
   - **When the equations can be solved.** The static equations `M(B, κ) = (−J[φψ], −2ε)` have a solution iff `(−J, −2ε) ⊥ V(ξ)` for all `ξ`. By step 3 that pairing is `−d⟨G_ξ⟩/dt`, so this is iff the law holds.
   - **Uniqueness.** Solutions differ by `ker M = span V`, that is, by relabellings.
   - **The uniform current.** Pairing with a uniform `ξ` gives only the total force, `ξ_j Σ_x f_j(x)`. So a nonzero uniform current does not obstruct these equations. In block 64's curl-only case it does, because there the harmonic strains are in the kernel.
   - **R4 (floating control, evidence only).** On `5³`, take the eigenstate of `H_w` with the largest bond energy (sources of norm 0.42). The member's static equations have relative residual `2.2×10⁻¹⁴` by least squares; for a random state the residual is 0.37. The control uses `5³` because of step 14: on `4³` every eigenstate has zero sources.

8. **PROVED (criterion of claim C).**
   - **The two demands.**
     - With the general transport, the identity and static equations give `Σ(dξ)J[φψ] = −(Σ_x 𝔢_x δu_x + Σ_b 2ε_b δκ_b) = −⟨ψ|Q(δΦ_ξ)|ψ⟩`. Here `Q(δΦ) = δΦHφ + φHδΦ`, which is the first variation of `⟨ψ|ΦHΦ|ψ⟩` (step 2).
     - The walk's law is `Σ(dξ)J = Σξ·f = −⟨ψ|Q(δΦ*_ξ)|ψ⟩` (step 3).
   - **When they coincide.** The demanded force density equals `f` for every state iff `⟨ψ|Q(δΦ_ξ − δΦ*_ξ)|ψ⟩ = 0` for all `ψ`. Since `Q` is hermitian (polarization), this holds iff `Q(δΦ_ξ − δΦ*_ξ) = 0`.

9. **PROVED; CHECKED N1 (block structure of `Q`).**
   - **Decomposition.** `Q = Σ_a σ_a ⊗ Q_a`, with `Q_a = δΦS_aφ + φS_aδΦ`. The `σ_a` are linearly independent, so `Q = 0` iff every `Q_a = 0`.
   - **The site part.** For `δΦ = D + K`, the site part `D` contributes only
     `Q_a(x, x+se_a) = −(is/2)(D_xφ_{x+se_a} + φ_xD_{x+se_a})`.
   - **The bond part.** The bond part contributes `Q_a(x,x) = 0` and
     `Q_a(x, x+se_a+te_b) = −(is/4)[κ(x,t,b)φ_{x+se_a+te_b} + φ_xκ(x+se_a,t,b)]` for `b ≠ a` or `t = s`.
     Here `κ(z,+1,b) = κ_(z,b)` and `κ(z,−1,b) = κ_(z−e_b,b)`.
   - **They separate.** For `L ≥ 5` the displacements `±e_a` and `0, ±2e_a, ±e_a±e_b` are all distinct, so `Q = 0` iff both parts vanish.
   - Check N1: every entry, on `5³`, for random `D`, `κ` and `φ`.

10. **PROVED (site part).**
    - The site part vanishes iff `D_x/φ_x = −D_{x+e_a}/φ_{x+e_a}` for all `x` and `a`.
    - Going once around an `a`-cycle multiplies by `(−1)^L`. So `D = cΓφ` for even `L` and `D = 0` for odd `L`.
    - Indeed `Q(Γφ) = φ{Γ, H}φ = 0`, so `Σ_x(−1)^{|x|}𝔢_x ≡ 0`.

11. **PROVED; CHECKED N3 (bond part).** Take a bond along `b` and a transverse direction `a ≠ b`.
    - The block `(s,t) = (+,+)` at `x` gives `κ_(x+e_a,b)φ_x = −κ_(x,b)φ_{x+e_a+e_b}`.
    - The block `(s,t) = (−,+)` at `x+e_a` gives `κ_(x+e_a,b)φ_{x+e_b} = −κ_(x,b)φ_{x+e_a}`.
    - Eliminating `κ_(x+e_a,b)`: `κ_(x,b)[φ_{x+e_a+e_b}φ_{x+e_b} − φ_xφ_{x+e_a}] = 0`.
    - The bracket vanishes iff `d_bu(x) + d_bu(x+e_a) = 0`.
    - Check N3, with ranks certified against the exact null vectors:
      - `dim 𝒩 = 0` on `5³` and `1` (`Γφ`) on `6³`, for random rates satisfying the condition at every bond;
      - `dim 𝒩 = 4` at uniform rates on `6³`: `Γφ` and `κ_(x,b) = (−1)^{|x|}` for each `b`.

12. **PROVED; CHECKED N2 (consequences of C).**
    - **(i)** Under the rate condition, steps 8–11 give `δκ = δκ*` and `φδu/2 ∈ span{Γφ}`.
    - **(ii) No bond field.** The two-site state `ψ(y) = (1,0)`, `ψ(y+2e_a) = (i,0)`, on `L ≥ 5` with `a = 3`, is the witness.
      - **Zero energy density.** No site of the support neighbours another, so `χ = Hφψ` vanishes on the support and `𝔢 ≡ 0`. Every transport of the rates alone therefore demands zero force for this state.
      - **The bond energies.** `χ(y+e_a) = σ_a(φ_{y+2e_a}ψ(y+2e_a) − φ_yψ(y))/(2i)`, so `ε_(y,a) = φ_{y+2e_a}/4` and `ε_(y−e_a,a) = 0`.
      - **The force.** `f_a(y) = d_aφ(y)φ_{y+2e_a}/4`, which is nonzero whenever the bond `(y, a)` is not flat.
    - Check N2: exact on `5³` (`f_3(y) = −11445/155236` for the rates drawn). This is block 106 T2's sublattice remark, made local.

13. **PROVED; CHECKED C1 (the continuum reading).**
    - For smooth `φ`, `ξ` and `ψ` along one axis with spacing `h`: `(Kψ)(x) = ½[δκ*_(x)ψ(x+h) + δκ*_(x−h)ψ(x−h)] = −hξφ'ψ + O(h³)`.
    - So the moved bond part acts as the moved clock `φ(x − hξ)`: the rate carried along, as in block 66's T1.
    - At the static point, and at leading order for smooth states (`ε ≈ ρ`), the right side of step 4's site form is `−½·2∂_jφ·(−2ρ) = 2ρ∂_jφ = 𝔢∂_ju`. This is block 66 T4's leading form of `f`.
    - Check C1: Taylor coefficients of `h⁰`, `h¹` and `h²` vanish, symbolically.

14. **PROVED for twofold levels; CHECKED S1 exactly; S2 floating evidence (side result S).**
    - **(i) The symmetries.** With every side even:
      - `Γ_aΓ_b` flips `S_a` and `S_b` and keeps `S_c`;
      - `σ_c` flips `σ_a` and `σ_b` and keeps `σ_c`;
      - so `U_c H U_c = H`, and `U_c` commutes with the diagonal `φ`.
      - `KS_aK = −S_a` and `σ_2σ_a*σ_2 = −σ_a`, so `ΘHΘ⁻¹ = H`.
      - `U_aU_b = iε_abc U_c`, `U_c² = 1`, and `ΘU_c = −U_cΘ`.
    - **(ii) Even dimension.** An eigenspace carries the anticommuting involutions `U_1`, `U_2`. Their algebra is `M_2(C)`, whose only irreducible module has dimension 2, so every eigenspace has even dimension.
    - **(iii) Twofold levels.**
      - In a twofold level `W` the `U_c` act as Pauli matrices.
      - `h_(x,j)` commutes with `U_j`, anticommutes with the other two, and is `Θ`-even.
      - So `X = P_W h_b P_W = βU_j` with `β` real.
      - `Θ`-evenness gives `ΘXΘ⁻¹ = X`, while `ΘU_jΘ⁻¹ = −U_j` gives `ΘXΘ⁻¹ = −X`. Hence `X = 0`, so `Re ψ(x)†ψ(y) = 0` on every bond.
      - For an eigenstate, `ε_b = ½E(1/φ_x + 1/φ_y)Re ψ(x)†ψ(y) = 0`.
      - Block 63's current operators `σ_a½{h_(x,a), S_j}` have the same pattern (commute with `U_j`, anticommute with `U_c` for `c ≠ j`, `Θ`-even), so `J[φψ] = 0`.
    - **(iv) `E = 0`.** Then `χ = 0`, so `ε = 0`. Also `φψ ∈ ker H`, which is spanned by the modes with `k ∈ {0, π}³`, on which `S_j = 0`; so `J = 0`.
    - **Check S1.** Exact on `4³` with random rates:
      - the commutations, the Pauli relations and `ΘU_c = −U_cΘ`;
      - the sign pattern and `Θ`-evenness of `h_(x,j)` and of the current operators, on every basis vector they reach.
    - **Check S2.** Floating evidence, max `|ε|` and `|J|` over all eigenstates:

      | torus | max `\|ε\|` | max `\|J\|` |
      |---|---|---|
      | `3³` | 3e-01 | 3e-01 |
      | `5³` | 9e-02 | 7e-02 |
      | `6×5×4` | 8e-02 | 5e-02 |
      | `4³` | 1e-14 | 1e-14 |
      | `4×4×6` | 6e-15 | 3e-15 |
      | `6³` | 3e-14 | 9e-15 |

      Every nonzero level is twofold on the even tori tested.
    - **Consequence for tests.** On tori with every side even, stationary states of the clocked walk in twofold levels feel no lattice force, so tests of the fall on stationary states need an odd side. Block 66's W3 used `6×5×4`, and its ring version was empty for the same kind of reason.

**Mutation census.** Each mutation fails only in its own families:
- flipping the sign of `δκ*` fails Q3, I1–I2 and R1–R2;
- dropping `B_a^j(x+e_j)` from `Ĩ` fails I1–I2 and R1–R2;
- doubling `ε` fails Q2, Q3, I3 and E1;
- `U_c` with one `Γ` fails S1;
- flipping the site-part sign fails N1;
- flipping the continuum sign fails C1.

## 3. Where the route stops (not claimed)

- **The rates' own equation.** `∂F/∂u = −𝔢` is not solved, and neither is any self-consistent coupled solution. For `F₂` that equation also carries the `u`-dependence of the coefficients of `Ĩ`.
- **Second order in the fields.** The content is taken at `B = 0` and `κ = 0`. The walk timed by `ΦH[B]Φ` with nonzero fields is not treated:
  - its `κ²` term;
  - block 63's second-neighbour remainder at nonzero `B`;
  - the exact conjugation `e^{−iG}Φe^{iG}` at `κ ≠ 0`, which leaves the nearest-neighbour class.
- **Flat bonds.** The identity (claim A) holds for every rate field. Existence (claim B) is shown only with no flat bond:
  - `½Σ_{flat b}κ_b²` keeps blindness and restores existence in the bond sector;
  - at uniform rates the bond sector decouples, and block 64's uniform-current obstruction returns.
- **Claim C at `L = 3, 4`**, where displacements collide, and for rates that violate step 11's condition (uniform rates have extra null bond fields).
- **Linearity in the rates** (block 60). `F₂` is not linear in `w`.
- **Side result S for levels of dimension 4 or more.** That generic rates give twofold levels is floating evidence only.
- **No adoption.** Nothing here is adopted, and nothing is said about gravity.

## 4. What would finish it

- **Solve the rates' equation together with the bond field's.** Does `∂F/∂u = −𝔢` together with `∂F/∂κ = −2ε` have solutions? Would a member linear in `w` (block 60) do?
- **Carry the joint move to second order in the fields,** with the content timed by `ΦH[B]Φ`. The question is whether a ledger can keep the exact conjugation `Φ → e^{−iG}Φe^{iG}`, which needs longer-reach bond fields.
- **Give flat bonds a member with existence that depends smoothly on `u`.**
- **Prove, or refute, that generic rates on even tori give only twofold levels.**

## Checks (`check.py`)

Exact unless marked. The run takes about 20 s.

| Family | What it verifies |
|---|---|
| Q1 | `i[φ, G_ξ] = −Λ_ξ` on all basis vectors of `4³`; `Λ_ξ = −Σδκ*_b h_b`, with no diagonal part |
| Q2 | The responses `2ε_b`, `J[φψ]` and `2ρ` (so `𝔢`), by exact symmetric differences |
| Q3 | Block 106 T2's bond form at every site-direction; block 66 T3(c); the joint-move identity of step 3 |
| I1–I2 (`3³`, `4³`) | Finite invariance of every curl and bond invariant; the member's identity in site form |
| I3 | The demand: the residual paired with `ξ` equals `d⟨G_ξ⟩/dt` |
| R1–R2 (`3³`, `4³`) | `AV = 0`; rank `V = 3N`, rank `A = 9N`: `ker A = span V` |
| R4 | Floating control on `5³` (evidence) |
| N1 (`5³`) | The block formulas of `Q` |
| N2 (`5³`) | The two-site witness |
| N3 (`5³`, `6³`) | Null dimensions 0, 1 and 4 |
| C1 | The continuum series |
| E1 (`4³`) | Block 106's two plane waves: equal `𝔢`, zero `J`, bond energies along `e_1` of `0` and `2` |
| S1 (`4³`) | The doubler algebra |
| S2 | Floating survey (evidence) |
