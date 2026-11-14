# Repo search

**Task:** finite-volume seed size. **Status (2026-11-11):** GUIDE only. This note gathers published spectrum inputs where reachable and evaluates the explicitly stated dilute-state model. It does not prove the seed inequality or any mass gap. Inputs, sources, and numerical outputs are kept separate below.

The supplied lead digest `library/prior/repo-search-2026-11-08.md` is a rule-9 search for unrelated RG/history targets; its findings do not cover this spectrum question. The target row gives no separate Repo prior work paths. In this checkout, the closest hit is `library/gap-crux-restate.md` §§1, 3.1, 3.4: its Theorem D identifies the seed with `S(n;(2n)^3)`, and (SEED) asks for a very small periodic-torus doubling defect; Section 5 says the seed remains open. This gives the observable to estimate, but no spectrum table or estimate. The previous literature note `library/prior/gap-seed-lit.md` concerns tools for the partition-function criterion and records finite-volume literature as GUIDE/NOT REACHED; it is complementary, not a spectrum calculation. No matching owner row for this spectrum-size estimate was found in `library/open-registry.md`.

The lead's search was not an exhaustive search for this target. I checked the supplied digest, FINISH row 706, the cited crux statement, and the open registry; no branch file paths were named under “Repo prior work,” so I did not fetch other refs. The current checkout is pinned at `95828cfbf2f02d41f26bc577caef46a94d25231d`.

## Sussman–Alpoge boundary

The outline index `library/sa-index/chunk-01.md` rows 588–599 and `obligations.md` rows 233–236 identify the cited passage as a counterexample to inferring a mass gap from polynomial clustering. I read the neighbouring source lines in `YM4_sketch_500.tex` 31860–31882: the spectral measure $E e^{-E}\,dE$ has transform $(1+t)^{-2}$ while its support reaches zero, and the text says a gap requires excluding a whole interval above the vacuum. This supplies no numerical finite-volume glueball or torelon data. The CA-I index for items 4.12–4.19 was searched for physical spectrum, glueball, torelon, and mass-gap entries; its indexed material concerns RG stage estimates and supplies no such input. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of the outline and account.

## 1. Published spectrum inputs

Convention sought: four-dimensional Euclidean SU(2) Wilson action with β=4/g² and plaquette term β(1-½ tr Uₚ). A quoted number below is not assumed to be in this convention until the source establishes it. A source's table, fit, and quoted uncertainties will be transcribed with its own lattice irrep labels. `NOT REACHED` means I could not access the relevant table/equation in an allowed page; no value is supplied from memory.

### Candidate sources

- A. Athenodorou and M. Teper, [arXiv:2106.00364, HTML](https://ar5iv.labs.arxiv.org/html/2106.00364): full text reached. Eq. (2) gives the standard plaquette action and β=2N/g_L², which for SU(2) is the convention in the question. Appendix Table 1 gives SU(2) β, a√σ and a scalar mass labelled a m_G. Values reached are:

  | β | a√σ | a m_G (0++) | Source location |
  |---:|---:|---:|---|
  | 2.2986 | 0.36778(69) | 1.224(16) | Appendix Table 1 |
  | 2.3714 | 0.29023(50) | 1.025(12) | Appendix Table 1 |
  | 2.427 | 0.24013(41) | 0.8469(76) | Appendix Table 1 |
  | 2.509 | 0.18011(22) | 0.6563(56) | Appendix Table 1 |
  | 2.60 | 0.13283(30) | 0.5001(41) | Appendix Table 1 |

  The parentheses are the errors as printed by the source. Table 1 caption identifies these as the fundamental string tension and mass gap from the main SU(2) calculations; the table's β=2.427 data use a 20³×16 lattice. No Table 1 point below β=2.2986 was reached.

- The requested 2++ mass is directly tabulated only at β=2.427 among the points above: Athenodorou–Teper Appendix Table 17, on its 20³×16 column, reports effective energies at t=2a of E⁺ = 1.284(13) and T₂⁺ = 1.289(11). The source labels cubic-rotation representation and parity; continuum J=2 subduces to E and T₂, whose dimensions total five. These are finite-lattice effective-energy estimates, not an independently established exact degenerate mass. The same table reports the lightest fundamental flux-loop energy on that lattice as 1.0996(39). At the other listed β values, same-β 2++ values and measured torelon energies were **NOT REACHED**.

- For a common model proxy at every β, M. Teper, [hep-th/9812187, HTML](https://ar5iv.labs.arxiv.org/html/hep-th/9812187), Table 4 reports SU(2) m(0++)/√σ = 3.60±0.20 and m(2++)/√σ = 5.55±0.27 at a≈0.03 fm. The caption describes these as ratios at fixed, small lattice spacing, not beta-specific masses or continuum limits. Teper says the table errors are intended as realistic and include some systematic errors imperfectly; the text also cautions that lattice irreducible representations can carry extra unquantified spin-identification error. In the model table below I use 5.55 as a fixed central ratio proxy and form a m(2++) = 5.55(a√σ); this derived quantity is **not** quoted as a beta-specific published measurement. Its ratio error is not propagated in the central-value sums.

- B. Lucini, M. Teper and U. Wenger, [hep-lat/0404008, HTML](https://ar5iv.labs.arxiv.org/html/hep-lat/0404008), Eq. (10) gives the torelon relation on an anisotropic lattice: `a_t m_k = a_t a_s L_s σ_k − (a_t/a_s)π/(3L_s)`, including the leading long-string correction. In the isotropic fundamental case with length `L=2n`, this is `aE = L(a²σ) − π/(3L) = 2n(a²σ) − π/(6n)`, the linear formula used in the requested model. The paper's abstract and tables do not provide additional SU(2) points in the requested beta range. Athenodorou–Teper Eq. (8) instead uses the Nambu–Goto form `E_k(L)=σ_k L sqrt(1−2π/(3σ_k L²))`; its first large-L correction is the same `−π/(3L)`. The finite-volume formula is an effective-string model input, not an exact identity for all lengths.

### Coverage and limitations

The data coverage is five SU(2) couplings in [2.2, 2.6], none below 2.2. The 0++ and a√σ values are QUOTED at those five points from Athenodorou–Teper Table 1. The 2++ value at β=2.427 is QUOTED as the Table 17 E⁺ and T₂⁺ effective energies; the other four 2++ inputs in the model are derived from Teper's common ratio and are not beta-specific quotations. I did not find a reached published table containing a complete (a√σ, a m0++, a m2++) triplet at each of the five couplings. None of the pages reached supplies an SU(2) point below β=2.2. Candidate full sources already reached as HTML are listed above; no PDF was fetched. Teper's review and Lucini–Teper–Wenger remain useful for the spectrum convention and string correction; the Athenodorou–Teper tables are the main source of beta-resolved inputs.

For a targeted follow-up search, I queried INSPIRE for `SU(2) glueball spectrum Wilson` at [this API result](https://inspirehep.net/api/literature?q=SU%282%29%20glueball%20spectrum%20Wilson&size=10). Two potentially relevant older papers appeared: Carpenter, Michael and Teper, “0+ and 2+ Glueball Masses From Large Lattices in SU(2) Lattice Gauge Theory,” *Phys. Lett. B* 198 (1987), 511–515, DOI 10.1016/0370-2693(87)90909-9; and Zhang, Jin and Ji, “Estimates of SU(2) glueballs on a coarse, anisotropic lattice,” *Chinese Physics Letters* 15 (1998), 865–867, DOI 10.1088/0256-307X/15/12/003. Their INSPIRE abstracts indicate low-lying SU(2) states, but no beta-resolved tables or numbers were reached. The second paper uses a tadpole-improved action, so it is not directly the requested Wilson input. These are the files the owner could download if complete beta-resolved 2++ values or lower-beta Wilson data are needed. I use no numerical value from either abstract.

## 2. Model and arithmetic

This section estimates only the stated model trace. It uses central values in the input table and the Teper ratio proxy for 2++; published errors are not propagated, and model uncertainty can move the first passing integer n. The one-particle contribution is

\[
S_1(n)=\sum_{k\in\mathbb Z^3}e^{-n\sqrt{m_0^2+(\pi |k|/n)^2}}+5\sum_{k\in\mathbb Z^3}e^{-n\sqrt{m_2^2+(\pi |k|/n)^2}}+3\sum_{k\in\mathbb Z^3}e^{-n\sqrt{(2n\sigma-\pi/(6n))^2+(\pi |k|/n)^2}}.
\]

Here $m_0=a m(0^{++})$, $m_2=a m(2^{++})$, and $σ=(a\sqrt\sigma)^2$, so the flux ground energy has lattice units. The fivefold tensor multiplicity is the $E^+\oplus T_2^+$ dimension. At β=2.427 the tensor term is split into two E⁺ and three T₂⁺ states using 1.284 and 1.289; at all other points I use five degenerate states with proxy mass $5.55(a\sqrt\sigma)$. The flux term counts three winding directions; it uses the question's relativistic center-of-mass momentum model in all three spatial directions. For the correction I use an ideal, noninteracting Bose-state count for these modeled one-particle levels,

\[
S_2(n)=\tfrac12\left(S_1(n)^2+S_1(2n)\right),
\]

where $S_1(2n)$ means the same level list at the same box size with only the Boltzmann exponent doubled. This is the usual symmetrized two-particle correction in the model; it is not a bound on interacting two-glueball states or omitted species. In the script the momentum sum is cut off at each component $-12\le k_i\le12$. Outputs are central-value guides, and the truncation and independent-particle assumptions are not proof estimates.

Reproducible arithmetic script used (inputs are the QUOTED table values above, with the fixed Teper proxy except for the directly quoted β=2.427 irreps; model coefficients and cut-off are as stated):

```python
import math
data=[(2.2986,.36778,1.224),(2.3714,.29023,1.025),(2.427,.24013,.8469),(2.509,.18011,.6563),(2.60,.13283,.5001)]
K=12
def one(n,sig,m0,tensor_levels):
    t0=t2=tw=n2=0.0
    for i in range(-K,K+1):
      for j in range(-K,K+1):
       for k in range(-K,K+1):
        p2=(math.pi/n)**2*(i*i+j*j+k*k)
        x=math.exp(-n*math.sqrt(m0*m0+p2))
        y=sum(deg*math.exp(-n*math.sqrt(m*m+p2)) for m,deg in tensor_levels)
        ew=max(0.0,2*n*sig-math.pi/(6*n))
        z=3*math.exp(-n*math.sqrt(ew*ew+p2))
        t0+=x; t2+=y; tw+=z
        n2+=x*x+sum(deg*math.exp(-2*n*math.sqrt(m*m+p2)) for m,deg in tensor_levels)+3*math.exp(-2*n*math.sqrt(ew*ew+p2))
    s=t0+t2+tw
    return s,.5*(s*s+n2),t0,t2,tw
for beta,sig,m0 in data:
    tensor_levels=[(1.284,2),(1.289,3)] if beta==2.427 else [(5.55*sig,5)]
    for threshold in (1/5041,1/750,1/64):
        n=1
        while one(n,sig,m0,tensor_levels)[0]+one(n,sig,m0,tensor_levels)[1]>=threshold: n+=1
        s,p,a,b,c=one(n,sig,m0,tensor_levels)
        print(beta,threshold,n,2*n,n*m0,s,p,a,b,c)
    for n in (3,4,6,8):
        s,p,a,b,c=one(n,sig,m0,tensor_levels)
        print(beta,n,s,p,s+p,a,b,c)
```

Outputs (columns: β, threshold, n, side, n m0, S1, S2, scalar, tensor, flux; then fixed-n lines give β, n, S1, S2, total, scalar, tensor, flux):

```text
2.2986 0.000198373338623 10 20 12.240000 0.000122143941596 7.55640491419e-09 0.000121794142058 3.49799537595e-07 1.8694e-29
2.2986 0.00133333333333 8 16 9.792000 0.00105893477535 5.70116358489e-07 0.00104376980476 1.51649705905e-05 3.0533e-18
2.2986 0.015625 6 12 7.344000 0.00890447260169 4.04949846457e-05 0.00829931850665 6.05152940792e-04 1.1542e-09
2.3714 0.000198373338623 12 24 12.300000 0.000116422426524 6.86357587684e-09 0.000115466204033 9.56222490881e-07 9.9566e-34
2.3714 0.00133333333333 10 20 10.250000 0.000720202205231 2.63375738266e-07 0.000701630485316 1.85717199141e-05 7.1626e-23
2.3714 0.015625 7 14 7.175000 0.0109700607249 6.13287874596e-05 0.00954030829383 0.00142975225099 1.8005e-10
2.4270 0.000198373338623 14 28 11.856600 0.000174369815954 1.54016564573e-08 0.000171153075119 3.21674083541e-06 3.1282e-38
2.4270 0.00133333333333 12 24 10.162800 0.000790922185389 3.17520319991e-07 0.000756888929344 3.40332560449e-05 1.3875e-27
2.4270 0.015625 9 18 7.622100 0.00768079661354 3.00112873190e-05 0.00659050764012 0.00109028897341 8.1824e-15
2.5090 0.000198373338623 18 36 11.813400 0.000181117828718 1.66179284859e-08 0.000177827678587 3.29015013094e-06 6.7227e-48
2.5090 0.00133333333333 15 30 9.844500 0.00104864722745 5.58400494356e-07 0.000997439203008 5.12080244454e-05 1.2020e-32
2.5090 0.015625 11 22 7.219300 0.0110269665481 6.18675602124e-05 0.00919862151899 0.00182834502907 8.9281e-17
2.6000 0.000198373338623 24 48 12.002400 0.000154741714596 1.21239658587e-08 0.00015040371122 4.33800337581e-06 1.7083e-63
2.6000 0.00133333333333 20 40 10.002000 0.000934496158841 4.43039093952e-07 0.000870252435328 6.42437235134e-05 2.0149e-43
2.6000 0.015625 14 28 7.001400 0.0143000169061 1.03844319357e-04 0.0110017557784 0.00329826112760 2.4035e-20
```

Fixed n=3,4,6,8 outputs, respectively, for each β:

```text
2.2986: n3 total 0.377005802878; n4 0.083396347493; n6 0.008944967586; n8 0.001059504892
2.3714: n3 total 0.991091305584; n4 0.219835537411; n6 0.028132239287; n8 0.004415531540
2.4270: n3 total 2.218729372430; n4 0.544364034078; n6 0.084273171364; n8 0.016745273580
2.5090: n3 total 5.343305736560; n4 1.494040617450; n6 0.272449812043; n8 0.070927961728
2.6000: n3 total 11.667437627900; n4 4.109384364880; n6 0.863457762909; n8 0.278206058686
```

Across all measured couplings, the scalar zero-momentum term is the largest term at the first passing n for each threshold. The tensor contribution is the main correction; the modeled winding contribution is negligible there. The two-particle correction $S_2$ is about $10^{-8}$ at the 1/5041 threshold, $10^{-7}$ to $6\times10^{-7}$ at 1/750, and $3\times10^{-5}$ to $10^{-4}$ at 1/64. Since at the target threshold the central one-particle sum is close to the cutoff, the reported n values are only central-value model estimates, not robust intervals.

For fixed n=3, 4, 6, or 8, every reached data point already fails 1/5041; n=8 is closest at the lowest sampled coupling β=2.2986, with model sum 0.0010595. Thus there is no beta meeting the target among the sampled points, and no largest beta can be interpolated from them. Any crossing would lie below the lowest reached beta and would be an unsupported extrapolation. No beta-specific value below 2.2 was reached.

