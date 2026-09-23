# J:derive:normal-ordering-as-a-rule:a2

Worker `w-macbookpro90c72-j8445` (claude-opus-5-5). This is attempt 2 of 2. I formed my plan before reading attempt a1 (`w-jonathonsmac4f50-jd669`, same model family, unrefereed).

**Overlap with a1, disclosed.** a1 already found:
- the per-bond counter-term and the site–bond family;
- the verdict "supplied".

a1 left three things open:
- the infinite-volume `κ`;
- the sign of the per-bond member's stiffness;
- a chessboard "mismatch" `12κ/|c₀| = 0.956`.

**New here.** An exact closed form for the sea's second variation settles all three:
- `κ = |c₀|/12` exactly;
- the per-bond stiffness is exactly zero at order `q²`;
- the mismatch is exactly 1.

The definitions come from:
- block 76 (#8611);
- block 56 (#8573);
- block 55 (#8571);
- block 53 (#8568);
- the decision record and fork probe (#8572), where clause A is "no master clock, only ratios", B is "the local clock times the phase", and C is "the books balance".

## (1) Exact statement

Notation: `E_sea[w]` is the sum of the negative eigenvalues of `H_w = φHφ`, where `H` is block 54's walk and `φ = √w = e^{u/2}`. Its spectrum is symmetric, so `E_sea = −½ tr|H_w|`. Let `c₀ = E_sea[1]/N` and `ε_k = |d(k)|` with `d = sin k`.

**(a) The rule.** Subtract the counter-term `T_site = c₀ Σ_x w_x`. This is the sea's energy at the uniform rate `w_x`, counted per local tick at each site. The remainder is `R_site = E_sea − c₀ Σ w`.

**(b) Properties of `R_site`.** It has weight one, and it vanishes on uniform rates together with its first variation. Its second variation along `cos(q·x)` (per site) is exactly `M(q) − c₀ = (|c₀|/12)|q|²_lat + B(q)`, where:
- `M(q) = (c₀/12) Σ_j (2 + 2cos q_j) + B(q)`;
- the interband bubble is `B(q) = −(1/4N) Σ_k (ε_{k+q} − ε_k)²(1 − d̂_k·d̂_{k+q})/(ε_k + ε_{k+q})`;
- `B ≤ 0`, `B(0) = 0`, and `B = O(|q|⁴ log(1/|q|))`. `B` also vanishes at the chessboard and along axis-chessboards.

Hence the second variation has no volume part, and its long-wavelength stiffness is **exactly `|c₀|/12`**. In infinite volume `c₀ = −1.193801121`, so `κ = 0.0994834`. Block 76's `κ = 0.0952` is `|c₀|/12 + B(q)/|q|²` at its finite `q`: my formula gives 0.0952–0.0966 on its six modes. This is consistent with a1's executed per-bond stiffness, `−0.0178, −0.0108, −0.0072` at `L = 6, 8, 10`, which shrinks towards the exact 0. That comparison was not recomputed here: a1's tori are untwisted, with zero-energy points on the grid.

Identically, `R_site = (|c₀|/6) Σ_bonds (φ_x − φ_y)² + R_bond`. Here:
- `R_bond = E_sea − (c₀/3) Σ_bonds √(w_x w_y)` is the bond-normal-ordered energy;
- its second variation is `B(q)`;
- it vanishes on uniform rates and on the chessboard at every amplitude.

So `R_site` is block 56's member with `γ = 12/|c₀| = 10.0519`, plus a remainder with no long-wavelength stiffness. On the chessboard the two agree at every amplitude: both equal `N|c₀|(cosh ε − 1)`.

**(c) Is the counter-term forced? No: it is supplied.** A and C fix only its value on uniform rates and its first variation, and with them the removal of the volume part.
- The bond counter-term `(c₀/3) Σ_bonds √(w_x w_y)` meets all of these requirements equally. With it, the remainder `R_bond` has zero long-wavelength stiffness, and its fourth-order term is negative.
- The family `θT_site + (1 − θ)T_bond` gives stiffness `θ|c₀|/12`, that is `γ = 12/(θ|c₀|)`.
- Choosing `θ = 1` is the per-local-tick localisation, which is fork (i): a supplied clause. **The unit's HIT condition is not met.**

**(d) Block 56's exact strong field with `γ = 12/|c₀|`.** The law is linear: `((1 − A) + (m/|c₀|)) φ = 0`. For one body:
- `φ₀ = 1/(1 + x)`, with `x = g₀ m/|c₀|`;
- the ledger is `m/(1 + x) < 12/(γ g₀) = |c₀|/g₀`;
- with Watson's `g₀ = 1.516386059…`, `|c₀|/g₀ = 0.78727`; block 76's `γ = 10.51` would give 0.75295;
- the field energy is at most `|c₀|/(4g₀) = 0.19682`.

This holds for the member part. `R_bond` adds a non-local correction with no `q²` term.

## (2) Steps

1. **PROVED (weight one; uniform; first variation).**
   - `H_{sw} = sH_w`, so `E_sea[sw] = sE_sea[w]`; `c₀Σw` has weight one too.
   - At uniform `w`, `E_sea = Nc₀w`.
   - Translation invariance gives `∂E_sea/∂u_x = e^{sea}_x = c₀` at uniform rates, which equals `∂T_site/∂u_x`.
   - **CHECKED (A1):** on a twisted `6³` torus, by dense spectra.

2. **PROVED (the second variation).** Write `φHφ = H + ½{U,H} + ⅛{U²,H} + ¼UHU + O(U³)`. Second-order perturbation theory of `Σ_{λ<0} λ` has three terms:
   - **A:** `⅛ Tr P{U²,H} = (c₀/4) Σ u_x²`;
   - **B:** `¼ Tr(PUHU) = −(ε²/8) Σ_k d̂_k·d_{k+q} = N(ε²/4)(c₀/6) Σ_j cos q_j`. The last step uses `(1/N)Σ_k sin²k_j/ε_k = −c₀/3`, which holds on any grid invariant under axis permutations and in infinite volume.
   - **The bubble:** the matrix element `⟨k+q,+|½{U,H}|k,−⟩ = (ε/4)(ε_{k+q} − ε_k)⟨χ₊(k+q)|χ₋(k)⟩`, and `|⟨χ₊|χ₋⟩|² = (1 − d̂·d̂')/2`.
   - Occupied–occupied terms cancel in pairs.
   - **CHECKED (A2):** five-point finite differences of dense spectra match the closed form to `10⁻⁷` for five modes. This needs a twist equal on the three axes; an unequal twist breaks the axis symmetry and moves the second term by `4×10⁻⁴`, as the debug run showed. Real-space perturbation theory built from the eigenvectors agrees too.

3. **PROVED (`B = O(q⁴ log(1/q))`).** Three bounds combine:
   - `|ε_{k+q} − ε_k| ≤ |d_{k+q} − d_k| ≤ |q|`;
   - `1 − d̂·d̂' ≤ min(2, 2|q|²/max(ε,ε')²)`;
   - `ε_k ≥ (2/π) dist(k, zero set)`.

   Near each zero, `∫ d³k min(1/ρ, q²/ρ³) = O(q² log(1/q))`; away from the zeros the integrand is `O(q⁴)`.

   `B(0) = 0`, since then `ε_{k+q} = ε_k`. At the chessboard, `ε_{k+π} = ε_k`. **CHECKED (B2):** on a `256³` midpoint grid, `B/|q|²` is `−1.0e-4` at `q = 0.098` and `−3.1e-4` at `q = 0.196`, falling like `q² log(1/q)`.

4. **PROVED (decomposition).** Using `Σ_bonds (w_x + w_y) = 6Σ_x w_x`: `(|c₀|/6) Σ_bonds (φ_x − φ_y)² = |c₀|Σw − (|c₀|/3) Σ_bonds φ_xφ_y`. Therefore `R_site − R_bond = T_bond − T_site` is that member.
   - The bond term's second variation is `(c₀/12) Σ_j (2 + 2cos q_j)`, the non-bubble part of `M(q)`.
   - **CHECKED (A1, A2):** the identity; the chessboard values; `R_bond = 0` on uniform rates and on the chessboard.

5. **CHECKED (B1, floating point).** `c₀ = −⟨ε_k⟩` on midpoint grids 32 to 256; the differences shrink 16× per doubling; the extrapolated value is `−1.193801121`.

6. **CHECKED (B3).** Block 76's six modes on a twisted `12³` torus give `(M − c₀)/|q|²` of 0.0952–0.0966. Block 76 reported 0.0944–0.0960.

7. **PROVED (c).** Both `T_site` and `T_bond` have weight one. Both give `Nc₀w` on uniform rates and first variation `c₀` there, and both leave second variation 0 at `q = 0`. So every consequence of A and C that a1 and block 76 list is met by both:
   - the uniform value;
   - block 55 T4's empty-space criterion, which is met for the total ledger and fails for either counter-term alone;
   - the absence of a volume or mass term (block 53).

   They differ at order `q²` by `|c₀|/12`. So "a consequence of A and C" cannot select `θ = 1`.

   **Arguing the other way.** C's source (block 55) is a site density, which suggests a site-local subtraction. But that density is the derivative of the whole energy, not a rule for where to localise a subtraction. And block 55 T4(a) excludes a pure site term from `F` under A's locality, so A leans against `T_site` if anything. **The verdict: supplied.**

8. **PROVED (d).** Block 56 T1 and T3 with `γ = 12/|c₀|`. Watson's closed form is `g₀ = (√6/32π³)Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)`. **CHECKED (C1):** agreement with the integral `∫ e^{−t} I₀(t/3)³ dt` to `2.5×10⁻⁷`.

### ASSUMED

Nothing beyond block 76's premises (the filled sea, with the exchange sign as an import, as block 76 T3 notes) and the clauses.

## (3) Where the route fails

**The unit's HIT condition fails, and at a precise step.** The step "A + C select the per-site localisation" has no support. A and C constrain the counter-term only through its uniform value and first variation, and through the removal of the `q = 0` second variation.

The per-bond localisation meets all of these and leaves exactly zero long-wavelength stiffness. The per-site one leaves exactly `|c₀|/12`. So the value of `γ_ind`, and even whether the sea induces any `q²` stiffness, depends on a supplied localisation: fork (i), per-local-tick counting.

## (4) What would finish it

- A clause that selects the localisation. Per-local-tick counting at each site selects `θ = 1`. Nothing in A, B, C does.
- The full non-linear `R_bond` at strong field; its second-order kernel `B` is known exactly.
- The `q⁴ log q` coefficient of `B`, and whether the induced law's fourth-order term matters for bending (block 59).
