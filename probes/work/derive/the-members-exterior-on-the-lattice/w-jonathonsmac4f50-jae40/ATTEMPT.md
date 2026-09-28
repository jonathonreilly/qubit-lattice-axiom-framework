# The member's exterior on the cubic lattice and the first-order ray turn

Worker `w-jonathonsmac4f50-jae40` (Claude Opus 5.5), unit `J:derive:the-members-exterior-on-the-lattice:a2`.

**Provenance, disclosed.** Blocks 110 and 166 are derivations by the supervisor on this same machine, and they are in the same model family as this worker. This attempt is a new derivation on their open item (block 110 N1: "lattice corrections to the exterior"; block 166's `next_trace_action`). It is not a referee of either block. A worker of another family should referee it.

Block 110 was read as landed on main. Block 166 was read on its pushed branch (`843d923cb1`); it makes no lattice statement. Nothing here is adopted.

## 1. Statement attempted

**Setting.** Block 110 T1 (landed) gives the exterior χ = 1 + a/r, N = 1 − p/r in the continuum, and the long-wave rays of E = (w/ℓ)|k| see the index n = χ³/N. Replace the continuum unit-source potential 1/(4πr) by the lattice one: the Green function G of the nearest-neighbour Laplacian on Z³, with −ΔG = δ₀ and G → 0. Work at first order in the charges. Put the content at one site, or make it cubic-symmetric about a site; §2 step 10 covers other content.

**Claims.**

- **(i) The fields.**
  - The exterior is exactly χ − 1 = Q G(x) and 1 − N = P G(x) on the sites.
  - G = 1/(4πr) + (5Σxᵢ⁴ − 3r⁴)/(32πr⁷) + G₂ + G₃ + O(r⁻⁹), with G₂ and G₃ given exactly below.
  - The relative correction to both fields is (5Σxᵢ⁴/r⁴ − 3)/(8r²): +1/(4r²) along an axis, −1/(16r²) along a face diagonal and −1/(6r²) along a body diagonal.

- **(ii) The turn.** Let t be the ray's direction, b its impact parameter, β = b⃗/b and φ the azimuth of β about t.
  - The first-order turn is (3a + p)[2/b + 2f₁/b³ + 4f₂/b⁵ + …] toward the body.
  - It also has a sideways part (3a + p)[f₁′/b³ + f₂′/b⁵ + …] along φ̂ = t × β. This is out of the plane that holds the ray and the body.
  - f₁(t, β) = ¼Σtᵢ⁴ + Σtᵢ²βᵢ² + ⅔Σβᵢ⁴ − ¾.

- **(iii) By direction.** φ is measured from e₁ for the axis e₃, from e₃ for the face diagonal (1,1,0)/√2, and from (1,−1,0)/√2 for the body diagonal.

  | ray direction t | f₁ (order b⁻³) | f₂ (order b⁻⁵) |
  |---|---|---|
  | axis | cos 4φ/6 | (3/20) cos 4φ + (5/24) cos 8φ |
  | face diagonal | −cos 2φ/12 + cos 4φ/8 | (19/192) cos 4φ − (1/10) cos 6φ + (15/128) cos 8φ |
  | body diagonal | 0, identically | −(4/135) cos 6φ |

  So along an axis the turn toward the body is (3a + p)[2/b + cos 4φ/(3b³)] and the sideways part is −(2/3)(3a + p) sin 4φ/b³, up to O(b⁻⁵).

  Along a body diagonal nothing depends on direction at b⁻³. The first anisotropy is at b⁻⁵: −(16/135)(3a + p) cos 6φ/b⁵ toward the body and (8/45)(3a + p) sin 6φ/b⁵ sideways.

- **(iv) Structure.**
  - There are no b⁻² or b⁻⁴ terms.
  - Averaged over the azimuth φ, the turn equals the continuum's 2(3a + p)/b at every order of the expansion.
  - The first direction-dependent term is at b⁻³, with angular content f₁. It vanishes identically only for body-diagonal rays.

**HIT.** The first direction-dependent term of the turn, exactly: (iii) and (iv).

## 2. Steps

**Step 1 — the exterior at first order. PROVED.**
- Block 110 T2(a) gives the site equations (Δχ)_z = −e_z/(8Kw_zχ_z) and (ΔN)_z = (e_z + 2τ_z)/(8Kχ_z).
- At first order in the content, the right-hand sides are the sources e/(8K) and (e + 2τ)/(8K) at the content sites. The walls are held at 1 and are taken to infinity.
- So χ − 1 = Σ_y s_χ(y) G(x − y) and 1 − N = Σ_y s_N(y) G(x − y). Here s_χ = e/(8K) and s_N = (e + 2τ)/(8K), with totals Q and P.
- For one content site this is Q G(x) and P G(x) exactly at every site. Block 110 normalises a = Q/4π and p = P/4π.

**Step 2 — the index at first order. PROVED.** χ³/N = 1 + 3(χ − 1) + (1 − N) + O(charges²). So n − 1 = (3Q + P)G = (3a + p)·4πG.

**Step 3 — the lattice Green function's expansion.**
- **ASSUMED (standard import).** G has an asymptotic expansion in homogeneous terms, G = Σ_k G_k with G_k of degree −(2k+1). The terms are generated term by term from the expansion of the symbol σ(k) = 2Σ(1 − cos kᵢ) (Duffin 1953, *Discrete potential theory*; Maradudin et al. 1960; Martinsson and Rodin 2002). Remainder bounds are part of that import.
- **CHECKED (exact).**
  - A1: σ = k² − Σkᵢ⁴/12 + Σkᵢ⁶/360 − Σkᵢ⁸/20160 + …
  - A2: the lattice Laplacian's Taylor form.
  - A3: the kernels r, r³, r⁵, whose iterated Laplacians give δ.
  - A4 and A5: G₁ = (5Σxᵢ⁴ − 3r⁴)/(32πr⁷). G₂ is a degree-8 cubic polynomial over πr¹³ (A5 lists it). G₃ is a degree-12 polynomial over 512πr¹⁹.
  - A6 to A8: each term satisfies the lattice Laplace equation at its order (r⁻⁵, r⁻⁷, r⁻⁹).
  - A9: G₁ is unique. The only cubic-invariant quadratic form is a r², which is harmonic only for a = 0, so no degree −3 harmonic can be added.
  - A10 and A11: no Gₖ has an l = 0 part. G₃ has no l = 4 part either, while G₂ does.
- **CHECKED (floating point, mpmath at 40 digits).**
  - D1: G(0) from the Bessel integral G(x) = ∫₀^∞ e^{−6t} Πᵢ I_{xᵢ}(2t) dt equals Watson's closed form √6/(192π³) Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24) to 3 × 10⁻²⁴. This confirms the normalisation.
  - D2: along an axis, a face diagonal, a body diagonal and the generic direction (2,1,0), (G − G₀ − G₁ − G₂ − G₃)·r⁹ is bounded out to |x| = 24–54 (values 5.9, 1.56, −0.79, 2.79). So the coefficients of G₂ and G₃ are right: an error in either would leave an r⁻⁵ or r⁻⁷ residue.

**Step 4 — the fields' anisotropy. CHECKED (B1).** G₁/G₀ = (5Σxᵢ⁴/r⁴ − 3)/(8r²). It is the same for χ − 1 and 1 − N at first order.

**Step 5 — the first-order turn. PROVED.**
- The rays of H = c|k| with c = 1/n obey dk/dt = −|k|∇c and dx/dt = c k̂ (block 110 T1).
- With n = 1 + εν, the change of direction at first order is Θ = ∫∇_⊥ν ds along the unperturbed line, that is Θ = ∇_b ∫ν(b⃗ + s t) ds.
- For the continuum part, ∇_b ∫ds/r = −2β/b, which is block 110 T4's first-order term 2ν₁/b.
- **CHECKED (floating point, E1).** Rays integrated directly (DOP853, rtol 10⁻¹², ε = 10⁻⁶, b = 2.5, path ±400) agree with this formula to 3 × 10⁻⁷ relative. That covers the size and sign of the part toward the body and of the sideways part (−4.267 × 10⁻² for an axis ray at φ = π/8), and the absence of any sideways part on the body diagonal.

**Step 6 — the b⁻³ term for every direction. PROVED.**
- Write Σᵢ(bβᵢ + s tᵢ)⁴. The terms even in s are b⁴Σβᵢ⁴ + 6b²s²Σtᵢ²βᵢ² + s⁴Σtᵢ⁴.
- The line integrals are ∫ds/r⁷ = 16/(15b⁶), ∫s²ds/r⁷ = 4/(15b⁴), ∫s⁴ds/r⁷ = 2/(5b²) and ∫ds/r³ = 2/b².
- So ∫4πG₁ ds = (1/8)[5(16/15 Σβ⁴ + 8/5 Σt²β² + 2/5 Σt⁴) − 6]/b² = f₁/b².
- **CHECKED (C1, C4).** Exact line integrals agree with f₁ for the three symmetry directions (symbolic in φ) and for four generic orthonormal pairs.

**Step 7 — the components. PROVED from steps 5 and 6.**
- With Ψ = (3a + p)[−2 ln b + f₁/b² + f₂/b⁴ + …], the turn is ∇_bΨ.
- Its component toward the body is −∂_bΨ = (3a + p)[2/b + 2f₁/b³ + 4f₂/b⁵].
- Its sideways component is b⁻¹∂_φΨ = (3a + p)[f₁′/b³ + f₂′/b⁵].

**Step 8 — the three directions. CHECKED (C2, C3).** These are the Fourier coefficients in the table of claim (iii), computed exactly.
- The body diagonal's f₁ is zero because Σβᵢ⁴ = ½ and Σtᵢ²βᵢ² = ⅓ for every β ⊥ (1,1,1). So f₁ = 1/12 + 1/3 + 1/3 − 3/4 = 0.

**Step 9 — averages and orders. PROVED.**
- Every Gₖ has odd degree −(2k+1), so the turn has only odd powers of 1/b.
- **Azimuthal average of f₁, for every t (C5).** The circle moments are ⟨βᵢβⱼ⟩ = Pᵢⱼ/2 and ⟨βᵢ⁴⟩ = 3Pᵢᵢ²/8, with P = I − tt. They give ⟨f₁⟩ = ¼Σt⁴ + ½(1 − Σt⁴) + ¼(1 + Σt⁴) − ¾ = 0.
- **All orders.**
  - The k-th symbol term is homogeneous of degree 2k − 2. Its angular parts with l ≤ 2k − 2 are |k|^{2k−2−l}h_l(k), which are polynomials, so their transforms sit at the origin.
  - Hence Gₖ = Σ_{l ≥ 2k} Y_l(x̂) r^{−(2k+1)}. A10 and A11 check this for k ≤ 3.
  - Averaging Y_l over rotations about t gives Y_l(t)P_l(t·x̂).
  - The line integral of P_l(t·x̂) r^{−(2k+1)} is b^{−2k} ∫_{−1}^{1} P_l(u)(1 − u²)^{k−1} du. This vanishes for l ≥ 2k (C6).
  - So termwise every correction averages to zero over φ. The φ-averaged first-order turn is the continuum's 2(3a + p)/b at every order.

**Step 10 — other content. PROVED.**
- For content with the cubic point symmetry about a site, the dipole vanishes and the second moment is (I₂/3)δᵢⱼ. Its term (I₂/6)Δ_cont G is O(r⁻⁵), because ΔG₀ = 0 and ΔG₁ = −Σ∂ᵢ⁴G₀/12 (A6).
- So the b⁻³ term is universal: the same f₁ for every such body, whatever its size. Structure-dependent terms begin at b⁻⁵.
- For content without that symmetry, the dipole gives a b⁻² turn about a site, and a traceless quadrupole gives a continuum-like Y₂/r³ field and a b⁻³ turn. These compete with or dominate f₁.
- s_χ and s_N may have different moments. At first order the index source is 3s_χ + s_N.

**Step 11 — size against the second order. CHECKED (C7).**
- Take an axis ray at φ = 0 and a = p = M/2, in lattice units.
- The ratio of the lattice b⁻³ term to the continuum second-order term (15π/4)(M/b)² is 8/(45πMb).
- So the lattice anisotropy is the larger of the two only when Mb < 8/(45π) ≈ 0.0566 (floating point value).

## 3. Where a route fails

None failed. Two slips during development were caught and fixed before the final run. My first face-diagonal field value used the wrong normalisation (it is −1/(16r²)). I also misremembered Watson's constant past the 18th digit; D1 now uses the closed form.

## 4. What would finish or extend it

- **Finite wave number.** The walker's own lattice dispersion makes the ray speed depend on direction at order k². This is separate from the field anisotropy here, and is block 110 N1's second route.
- **Second order in the charges on the lattice.** The exterior of block 60's exact site equations is not Q²G² at second order; the nonlinear lattice field needs its own expansion.
- **Content without cubic symmetry**, where the body's quadrupole competes at b⁻³.
- **Remainder bounds** for the expansion. They are imported here, and checked only numerically out to |x| ≈ 50.

## Prior art

- The r⁻³ term of the simple-cubic lattice Green function is classical: Duffin 1953, with later expansions by Maradudin et al. and by Martinsson and Rodin. It is imported, and re-derived and checked here.
- No landed note on main contains it or any lattice turn correction. A grep of `origin/main:docs` for the expansion found nothing.
- The members of this machine's family found no earlier probes attempt on this problem. `probes/work/derive` has no directory for it, and the claim showed no prior attempts.

## Check

`python3 check.py` runs sections A–C exactly (sympy, rational) and sections D and E in floating point, each labelled. It takes about 5 minutes and prints `SUMMARY: PROVED …` and `HIT: …`.
