# kernel-normalization-in-3plus1, attempt 1 (worker w-macbookpro90c72-jee37, model grok-4.6)

Different route from a3 (same problem, unrefeered mean-map identity `K=gφ`). This attempt treats the **vMF innovation variance** on the linear covariance, which is the remaining `O(1/β)` channel once the mean map is gain-one. Plan locked from `formation_levelplane.py` and the vMF second-moment tensor before reading a3’s writeup.

Setting: backward 3+1, `n=4`, `φ=(1+∑ e^{-ik_j})/4`, `σ²=A(nβ)/(nβ)`, `A=coth-1/κ`. Executed first look (this worktree): `β=6`, `L=32`, low-`k` ratio `0.9719<1`.

## (1) The statement attempted

**Statement (PARTIAL / sign no-go).** Truncate the vMF draw at large concentration, `A(κ)=1-1/κ` (error `2/(e^{2κ}-1)`). On the linear covariance `S_{\mathrm{lin}}=σ²/(1-|φ|²)` off zero, the lab-frame innovation of one transverse component has

```
⟨Var(s_x|S)⟩ / σ² = 1 + (3 - G_V)/(n β) + O(1/β²),
```

where `G_V=V^{-1}∑_{k≠0} 1/(1-|φ|²)` and the two contributions are (i) fluctuations of `|S|` in `A(β|S|)/(β|S|)` and (ii) the tilt projector `(1-3A/κ-A²)û_x²`. For `n=4`, `G_4=1913/1344<3`, and for the infinite-volume `G_3≈1.79<3`, the coefficient `(3-G)/n` is **positive**: the truncation predicts `R=1-a/β` with `a=(G-3)/n<0`, i.e. `R>1`. The executed infrared ratio is `<1`. The cubic-Gaussian **noise** sector cannot produce a positive `a` involving `G_3` of the size needed for the deficit.

## (2) Steps

**Step 1 — vMF tensor (PROVED; CHECKED N1).** `Z=4π sinhκ/κ`, `E[s]=A u`, `E[(s·u)²]=1-2A/κ`, `E[(s·e_⊥)²]=A/κ`. Hence `E[s_i s_j]=(A/κ)δ_{ij}+(1-3A/κ)u_i u_j` and
`Var(s_x|S)=A/κ+(1-3A/κ-A²)û_x²`.
With `A_0=1-1/κ`, the projector coefficient is `2/κ²-1/κ`. Exact `A=1-1/κ+2/(e^{2κ}-1)`.

**Step 2 — `|S|` fluctuations (PROVED; CHECKED N2, N3).** Write `|S|=n+δ`. On `S_{\mathrm{lin}}`, `C(0)-C_v=σ²(1-V^{-1})` because `|φ|²/(1-|φ|²)=1/(1-|φ|²)-1` (CHECKED on `L=4`: `G_4=1913/1344`, `C_0-C_v=63/64`). Then `⟨δ⟩=-nσ²(1-V^{-1})`, `⟨1/|S|⟩=n^{-1}(1+σ²(1-V^{-1})+O(σ⁴))`, and `⟨A/κ⟩/σ²=(1+σ²(1-V^{-1}))/A(nβ)+O(1/β²,e^{-2nβ})`. At `V=∞`, `n=4`, `A=1-1/(nβ)`, this is `1+1/(2β)+1/(16β²)`. At `β=6`: `599/552>1`.

**Step 3 — projector (PROVED; CHECKED N4).** `⟨û_x²⟩=C_v=σ²(G_V-1)` on `S_{\mathrm{lin}}`. Extra `/σ²=(G_V-1)(2/(n²β²)-1/(nβ))`, leading `-(G_V-1)/(nβ)`.

**Step 4 — combine (PROVED; CHECKED N5).** `|S|` piece `+2/(nβ)` plus projector `-(G-1)/(nβ)` gives `R=1+(3-G_V)/(nβ)+O(1/β²)`. `G_4=1913/1344<3`; the 3D return sum is finite and `G_3<2<3`. So `a=(G-3)/n<0`.

**Step 5 — clash with the executed deficit (CHECKED N2e, N5).** Simulator shell `|k|∈[0,0.3)` at `β=6`, `L=32` is `0.9719<1`. The truncation’s `O(1/β)` is positive.

## (3) First point of failure of the suggested route

The noise sector, closed on the linear covariance, produces the wrong sign for `a`. Combined with a3’s mean-map result `K=gφ` with `g=1+O(1/β²)` (unrefeered, not used as a hypothesis here: even a strictly gain-one mean map leaves this noise), cubic Wick closure **cannot** yield `R(k→0)=1-a/β` with `a>0` built from `G_3`.

ASSUMED: insertion of `S_{\mathrm{lin}}` (first iterate); `A=1-1/κ` power-law truncation; Gaussian `⟨δ²⟩` dropped as `O(σ⁴)`.

## (4) What would finish it

A mechanism with the right sign: (i) self-consistent `S=R S_{\mathrm{lin}}` in the projector (`C_v=Rσ²(G-1)`), still `(3-RG)` and `R≈1` keeps the sign; (ii) expansion about the magnetized saddle `|S|∼nm` rather than `n`; (iii) the lab-frame structure factor of the unit vector after a finite run, relative to the *initial* axis (block 35’s frame caveat). The candidate `R=m_{\mathrm{sw}}/A(nβ)=(1-σ²G)/A` does give `a=(G-1)/n>0` and `0.9707` vs `0.9719` at the executed point, but it is not this truncation.
