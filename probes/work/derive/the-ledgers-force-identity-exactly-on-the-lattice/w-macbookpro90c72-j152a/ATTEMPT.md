# The ledger's force identity exactly on the lattice: derivation attempt 1 of 2

Worker `w-macbookpro90c72-j152a` (claude-opus-5-5), unit `J-derive-the-ledgers-force-identity-exactly-on-the-lattice-a1`.

**Sources, pinned.**

| Block | PR | Head | What it supplies |
|---|---|---|---|
| 62 | #8592 | `aada5794` | the kinetic term |
| 64 | #8595 | `e5688665` | strains, relabelling, curls |
| 66 | #8597 | `c4afb022` | T3, the force density, the corrigendum |
| 72 | #8605 | `a57dbbab` | the two-step force, the species maps |

`check.py` quotes their definitions verbatim (family Q). Every finite claim is checked there in exact Gaussian-rational arithmetic. It runs in about 14 s.

**Overlaps and prior work.**
- The claim tool listed no prior attempt on this problem.
- Related earlier units of mine, all on different tasks:
  - #8702, the fall from the ledger's consistency (a1): any local momentum commuting with `H` falls with weight `∂p̄/∂k_j`. The `cos k` below is that weight.
  - The couplings unit and the reach-three unit (no HIT): relabellings, reach two and reach three.
  - #8741: the eight species.
- The closest result is #8644, the other attempt at the fall problem (same model family, unrefereed):
  - curl ledgers forbid the fall;
  - the first-order formula `f = 𝔢(centred d_ju)cos k_j`;
  - a rank argument.

  It lists as not covered: a lattice member that transports the rates, ledgers that see other content quantities, and the reach-three analog. This attempt supplies all three.

## 1. The statement attempted

**Notation.**
- `H = Σ_aσ_aS_a` and `H_w = φHφ`, with `u = 2 log φ`.
- `χ = Hφψ`, `ρ = Re ψ†χ`, and the energy density `𝔢 = φρ`.
- Block 66's force density `f_j`, and block 72's `f^P_j` with `P_j = S_jC_j`.
- `Γ = (−1)^{x₁+x₂+x₃}`, which is block 70's `V_(111)`.

**(a) The exact lattice force (Theorem A).** For every state, positive rate field, direction `j` and site `x`:

```
f_j(x) = d_jφ(x) ε_j(x) + d_jφ(x − e_j) ε_j(x − e_j),    ε_j(x) = ½ Re[ψ(x+e_j)†χ(x) + ψ(x)†χ(x+e_j)].
```

- Here `ε` is the bond cross energy.
- Since `d_jφ = ½Λ_b·d_ju` exactly, with `Λ_b` the logarithmic mean of `φ` at the bond's ends, this is the exact local factorisation:

  ```
  f_j(x) = 𝔈_j(x)[u(x+e_j) − u(x)] + 𝔈_j(x−e_j)[u(x) − u(x−e_j)],   𝔈_b = ½Λ_b ε_b.
  ```

  It is a bond-placed energy times a difference of `u`.
- The bond energy is not the energy density:

  ```
  ε_b = ½(ρ_x + ρ_y) − ½Re[(d_jψ)_b†(d_jχ)_b].
  ```

  So `f_j = f_j^𝔢 + R_j`. The first part is built from the energy density: `f_j^𝔢(x) = Σ_b ¼Λ_b(𝔢_x/φ_x + 𝔢_y/φ_y)(d_ju)_b`. The exact remainder is `R_j(x) = −½Σ_b (d_jφ)_b Re[(d_jψ)_b†(d_jχ)_b]`.
- **No factorisation through the energy density exists.** A state on one sublattice has `𝔢 = 0` at every site and `f ≠ 0`.

**(b) The field's side (Theorem B).**
- **(i) Curl ledgers.** Take block 64's `F = Σ_x w_xD_x(curls)`. Carry the rates by any transport `u → u + T_ξu`, or by the walk's own action `W → W + i[G_ξ, W]`, which turns a rate into a hop. Either way the identity obeyed by the field equations is `Σ_a[E_a^j(x) − E_a^j(x − e_a)] = 0` exactly. It has no rate term, whatever the rates. The static equations then require `f = 0` at every order.
- **(ii) Any ledger that carries the rates.** Let `F(B, u)` be invariant at first order under `δB = dξ + M_ξ[u]`, `δu = T_ξ[u]`, with `M` and `T` linear in `ξ` and vanishing for uniform rates. Then:

  ```
  Σ_b E_b(dξ + M_ξ)_b + Σ_x U_x(T_ξu)_x = 0.
  ```

  With the static field equations (`E = −J[φψ]`, `U = −𝔢`, at first order in the content) the content must satisfy

  ```
  Σ_x ξ·f = −Σ_b J_b(M_ξ)_b − Σ_x 𝔢_x(T_ξu)_x.
  ```

  This requirement `f_req` is linear in `J` and `𝔢`, with coefficients from the fields.
- **(iii) Such ledgers exist.** The volume member `F = c₀Σ_xw_x det(1 − B(x))` carries the rates with the upwind transport `δu_x = −Σ_aξ_a(x)(1 − w(x − e_a)/w(x))`. At `B = 0` its identity holds exactly. It requires `f_a(x) = 𝔢_x(1 − e^{−(u_x − u_{x−e_a})})`.
- **(iv) Comparison with (a).**
  1. *Parity, exact, every order, reach two.* `Γ` anticommutes with `H_w`, `𝔢[Γψ] = −𝔢[ψ]` and `f[Γψ] = +f[ψ]` (block 72 T2, re-checked). So a requirement linear in `𝔢` alone (`M = 0`) fails for `ψ` or for `Γψ` whenever `f[ψ] ≠ 0`, and `Γ` maps stationary states to stationary states. This is block 72's reflected-species failure, now exact and for every ledger of the class.
  2. *First order in the rate gradient, reach two, every `M` and `T`.* Take `φ = 1 + εη`. Then `f_j = 𝔢 cos k_j (u(x+e_j) − u(x−e_j))/2` exactly for plane waves, and the requirement at first order depends on the state only through `(𝔢⁽⁰⁾, J⁽⁰⁾)`.
     - The plane waves `k = (π/2,0,0)` and `(0,π/2,0)` at energy 1 have the same `𝔢⁽⁰⁾ = 2` and zero current `J`.
     - Their forces along `e₁` are `0` and `𝔢(u(x+e₁) − u(x−e₁))/2`.
     - So no ledger of the class meets the content's law beyond long wavelength.

**(c) With a kinetic term for the strains (Theorem C).** Take block 62's kinetic term per local tick, `K = Σ_x w_x^{−1}[αḣ_ijḣ_ij + βḣ²]_x`, which depends on the strains only through `Ḃ`. Write `Π = ∂K/∂Ḃ` and `𝒦_x = −∂K/∂u_x` (the strains' kinetic energy density). The equations of motion are `Π̇ = −E − J`, and for the rates `U = −(𝔢 + 𝒦)`. For a potential part `F` invariant as in B(ii), with static `ξ`:

```
Σ_b(Π̇_b + J_b)(dξ + M_ξ)_b + Σ_x(𝔢_x + 𝒦_x)(T_ξu)_x = 0.
```

Together with block 66 T3(c) this gives, exactly,

```
d⟨G_ξ⟩/dt + Σ_bΠ̇_b(dξ + M_ξ)_b = −Σ_x ξ·(f − f_req),   Σ_xξ·f_req = −Σ_bJ_b(M_ξ)_b − Σ_x(𝔢_x + 𝒦_x)(T_ξu)_x.
```

- **Curl members** (`M = T = 0`): `d/dt[⟨G_ξ⟩ + Σ_bΠ_b(dξ)_b] = −Σξ·f`.
- **Rate-carrying members:** the strains' kinetic energy weighs too.
- At first order in the content `𝒦` is of second order, so the static comparison of (b) is unchanged.
- In motion, `f − f_req` is exactly the rate at which the combined momentum of content and strains fails to be conserved.

**(d) Reach three (Theorem D).**
- The exact two-step bond form is `f^P_j(x) = ½[d2_jφ(x)ε2_j(x) + d2_jφ(x − 2e_j)ε2_j(x − 2e_j)]`, with `ε2` on the bond `(x, x+2e_j)` and `ε2 = ½(ρ_x + ρ_y) − ½Re[(d2_jψ)†(d2_jχ)]`.
- `f^P` is odd under `Γ`, like `𝔢`, so the parity obstruction is absent. That is block 72's "all eight species".
- At first order, `f^P_j = 𝔢 cos 2k_j (u(x+2e_j) − u(x−2e_j))/4`. The same pair of plane waves has opposite forces along `e₁` at equal `(𝔢, J)`. So reach three also meets the ledger's requirement only at long wavelength.

## 2. Steps

**S1 (PROVED; CHECKED A0).** The content's exact balance.
- `d⟨G_ξ⟩/dt = ⟨i[H_w, G_ξ]⟩ = Σ(d_aξ_j)J_a^j[φψ] − Σξ_jf_j` (block 66 T3(c)).
- Checked for a random non-stationary state, rate field and displacement on the 4-torus. The left side is computed as `−2 Im⟨H_wψ|G_ξψ⟩`.

**S2 (PROVED; CHECKED A1).** The bond form. With `C_j[v]ψ(x) = ½(v(x)ψ(x+e) + v(x−e)ψ(x−e))`:

```
f_j(x) = ½v_x Re[ψ(x+e)†χ(x) + ψ(x)†χ(x+e)] + ½v_{x−e} Re[ψ(x−e)†χ(x) + ψ(x)†χ(x−e)]
       = v_xε_j(x) + v_{x−e}ε_j(x−e),     v = d_jφ.
```

Checked at every site and direction for random states and rates on the 4- and 5-tori.

**S3 (PROVED).** The factorisation onto `u`.
- With `u = 2 log φ` and `Λ(p, q) = (q − p)/(log q − log p)`, we have `d_jφ = ½Λ·d_ju` exactly.
- Hence `𝔈_b = ½Λ_bε_b` factorises `f_j` onto the two bond differences of `u` at `x`.

**S4 (PROVED; CHECKED A2).** Polarization. `Re[(dψ)†(dχ)] = ρ_x + ρ_y − 2ε_b`. Checked exactly.

**S5 (PROVED; CHECKED A3).** No factorisation through `𝔢`.
- If `ψ` lives on the even sublattice, `χ = Hφψ` lives on the odd one, so `ρ ≡ 0` and `𝔢 ≡ 0`.
- `ε_b = ½Re[ψ_x†χ_y]` is non-zero on bonds. On the 4-torus `f_1 ≠ 0` at all 64 sites.
- A factorisation `f = Φ(𝔢, u)` with `Φ(0, ·) = 0` is therefore impossible, and so is any `f` built from the energy density alone.

**S6 (PROVED; CHECKED B1).** Curl ledgers are rate-free.
- The curls are invariant under `B → B + dξ` (block 64 T1(a)), and `F` depends on `u` only through the site multipliers `w_x = e^{u_x}`.
- For every transport, `F(B + dξ, u + T) − F(B, u) = Σ_x w_x(e^{T_x} − 1)D_x`. The chain rule then leaves `Σ_bE_b(dξ)_b = 0`: the rate change enters both sides and cancels.
- The walk's own action on a rate, `i[G_ξ, W]`, has zero diagonal, because `G_ξ` has zero diagonal and `W` is diagonal. So `Tr(D·i[G_ξ, W]) = 0` and `F` is unchanged.
- Checked for a random member (linear and quadratic in the nine curls, random rates and strains, 4-torus). `E` is computed exactly by central differences, which are exact for a quadratic.

**S7 (PROVED).** The general identity (B(ii)).
- Invariance at first order gives the displayed identity.
- The strains' equation at `B = 0` is `E = −∂⟨H_w[B]⟩/∂B = −J[φψ]` (block 64 T1(b) applied to `φψ`). The rates' equation is `U = −𝔢` (block 66: `𝔢 = ∂⟨H_w⟩/∂u_x`).
- S1 with `d⟨G⟩/dt = 0` gives `Σ(dξ)J = Σξf`.

**S8 (PROVED; CHECKED B2).** The volume member carries the rates.
- At `B = 0`: `E_a^j = −c₀w_xδ_aj` and `U = c₀w_x`.
- `Σ_{x,a}−c₀w_x(ξ_a(x+e_a) − ξ_a(x)) + Σ_x c₀w_xδu_x = 0` telescopes exactly with the upwind `δu`.
- The requirement follows from S7.
- Scope: first order in the strains. At `B ≠ 0` a transport of `B` along `ξ` would be needed at order `ξB`. This member has `c₀ ≠ 0` and is not block 64's curvature member (which has `c₀ = 0`). It shows that the class of B(ii) is not empty.

**S9 (PROVED; CHECKED A4).** Parity.
- `Γ` anticommutes with every nearest-neighbour hop and commutes with `φ` and with the two-step hop.
- So `H_wΓ = −ΓH_w`, `𝔢[Γψ] = −𝔢[ψ]`, `f[Γψ] = f[ψ]` and `f^P[Γψ] = −f^P[ψ]`. Checked for a random state and rates on the 6-torus.
- B(iv)1 follows: `f[ψ] = L[𝔢[ψ]]` and `f[ψ] = f[Γψ] = L[−𝔢[ψ]]` force `f[ψ] = 0`.

**S10 (PROVED; CHECKED F1–F3).** First order in the rate gradient.
- `f` is already `O(ε)` through `d_jφ = ε d_jη`, so `f⁽¹⁾` uses `ψ⁽⁰⁾` and `χ⁽⁰⁾ = Eψ` only.
- For `ψ = a e^{ik·x}`: `f⁽¹⁾ = 𝔢⁽⁰⁾cos k_j(η(x+e_j) − η(x−e_j))` and `f^{P(1)} = ½𝔢⁽⁰⁾cos 2k_j(η(x+2e_j) − η(x−2e_j))`.
- Checked at every site of the 8-torus for all 48 plane waves of energy ±1: one component of `k` in `{π/2, 3π/2}`, the others in `{0, π}`, with rational spinor eigenvectors. For `(π/2,0,0)` and `(0,π/2,0)`, `𝔢⁽⁰⁾ = 2` everywhere and `J ≡ 0` (F3).
- If `M` and `T` vanish for uniform rates, the requirement at first order is `f_req⁽¹⁾ = −M⁽¹⁾†J⁽⁰⁾ − T⁽¹⁾†𝔢⁽⁰⁾`. It is identical for the two waves, while `f⁽¹⁾` differs: at the origin it is `0` against `2` for reach two, and `+5` against `−5` for reach three.
- **Caveat for a hostile reader.** At energy 1 the plane waves are degenerate. A stationary state of `H_w` at first order has as its zeroth-order limit a combination within that subspace, not necessarily one plane wave. The comparison in S10 is therefore one of functionals of the state, as in block 66 T4. S9's parity statement covers stationary states directly.

**S11 (PROVED).** The kinetic term (C).
- The total Lagrangian is `𝓛 = K(Ḃ, u) − F(B, u) − ⟨H_w[B]⟩`.
- The equations of motion: the strains' equation `d/dt ∂𝓛/∂Ḃ = ∂𝓛/∂B` is `Π̇ = −E − J`. The rates' equation is `∂K/∂u − U − 𝔢 = 0`, i.e. `U = −(𝔢 + 𝒦)`; the rates carry no kinetic term.
- Invariance of `F` under static `(δB, δu)` gives `Σ(−E)δB − ΣU T = 0`. Substituting the equations of motion gives the displayed identity.
- Adding S1 (`d⟨G⟩/dt = ΣJ(dξ) − Σξf`) gives the balance of combined momentum.
- For curl members, S6 gives `ΣE(dξ) = 0` directly. `K` is unchanged by a static `dξ`.
- Block 62's family qualifies. Its two numbers `α` and `β` enter only through `Π` and `𝒦`.

**S12 (PROVED; CHECKED D1, D2).** Reach three.
- `i[φ, P_j] = −½C2_j[d2_jφ]` (block 72 T1(a)).
- The two-step bond form and its polarization, as in S2 and S4 with bonds of two steps. Checked on the 5- and 6-tori (block 72 requires sides of at least five).

**ASSUMED.**
- The objects exactly as the pinned notes define them.
- In B(ii), invariance at first order in `ξ`. The field equations to first order in the content, at `B = 0` for the strains' source.

## 3. Where the route stands

No step fails. The answers to the task's questions:

- **(a)** An exact local factorisation exists with the bond cross energy. None exists with the energy density.
- **(b)** For the curl members the lattice identity has no rate term under every transport. For every member that carries the rates, the requirement is built from `𝔢` and `J`, and it meets the content's exact law only at long wavelength. Under reach two it also fails the sign for reflected species, and that failure is exact.
- **(c)** The kinetic term does not change the static comparison, and for rate-carrying members its own energy weighs too. It makes the mismatch a non-conservation of combined momentum.
- **(d)** Under reach three the sign is right for all species, and the agreement is again only at long wavelength (`cos 2k_j`).

The disagreement beyond long wavelength, and its exact form, go beyond what block 66 states. Block 66 states the `cos k` factor for a plane wave and agreement at leading order.

## 4. What would finish it, or go further

- A lattice curvature member (`c₀ = 0`) that carries the rates exactly at all orders in the strains. It would fall under B(ii), so the comparison above would not change.
- A ledger that sees the bond cross energy `ε_b` itself, i.e. a content-dependent field coupling. That is outside B(ii), and it is the only way left for a field identity to reproduce Theorem A exactly.
- The comparison on self-consistent stationary states beyond first order, resolving S10's degenerate subspace.
