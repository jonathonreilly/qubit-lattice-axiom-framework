# Exact cubic-source reference tail refinement

ROOT author candidate, distinct checking required. This changes only the scalar actual-tail allowance U in three_site_reference_time/PROPOSAL.md (d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f), not its other premises or errors.

On the exact isolated three-source reference, the checked density and determinant give

 rho3(delta)=8lambda^5 sqrt(1-delta²/(4j²))/(3pi|q3(delta)|²),
 |q3(delta)|²>=(1-3eta)(delta²+lambda²)^3,
 eta=lambda/j<=1/16.

Therefore for any positive Delta, integrating only the physical band and then extending the nonnegative upper envelope yields

 int_{|delta|>=Delta} rho3(delta) ddelta
 <=16lambda^5/[15pi(1-3eta)Delta^5].

This follows from rho3<=8lambda^5/[3pi(1-3eta)|delta|^6] and twice integral_Delta^infinity delta^-6 ddelta=2/(5Delta^5). It remains valid if Delta exceeds the physical band, when the left side is zero.

The slow connector flux is contractive. The monotone exact map delta(x)=2g sin(x/(2g)) on the retained interval maps the omitted |x|>D to |delta|>delta_D. Thus the raw transmitted comparator tail outside |x|<=D has norm at most

 Usharp = min{1,lambda/(sqrt3 delta_D),sqrt(mu6)/delta_D^3,
    sqrt[16/(15pi(1-3eta))]*(lambda/delta_D)^(5/2)}.

Replace U by Usharp in the reference-time error E(t); all other terms, exactphase, periodization, normalization, domain and actualincoming identification requirements remain unchanged. This is a comparison-measure tail, never a replacement of the ACTUAL installed omitted-state charge. No finite-time operating point or complete-device improvement follows by itself.

Source density/determinant: three_site_product_source a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823, distinctcheckc161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b; denominator inequality also in three_site_loaded_inverse7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672/check8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2. Root authored the last inverse and proposed this tail refinement with exposure to all sources. No numerical run, sweep, canonical/Git/PR/prompt/axiom/model edit.
