# Lit lens summary (agent report 2026-10-01; diagnostic orientation only, nothing imported)
- Population-control bias raises the energy (UNR 1993 via Toulouse-Assaraf-Umrigar arXiv:1508.02989; Calandra-Sorella PRB 57 11446).
- NOT 1/N_w in general: Boninsegni-Moroni PRE 86 056712 (arXiv:1209.1663): e(N_w) = e_inf + c N_w^-k, k = 0.34 (good guide) / 0.20 (poor),
  N_w needed grows enormously with size; last-K reweighting failed (error grew as large as bias). Brand et al. PRB 105 235144 (FCIQMC): N^p, p ~ -0.4.
- Nemec PRB 81 035119 (arXiv:0906.0501): N_eff = sigma^2_walker(E_L)/sigma^2_pop; inefficiency >= exp(sigma tau_corr/sqrt(2pi)); N_eff falls exponentially with size.
- Genealogy: Koskela et al. Ann. Stat. 48 560 (arXiv:1804.01811): pair-merger rate c_N = sum w^2 ~ 1/ESS per generation; reading lineages deeper
  than ~1/c_N generations is meaningless. Calandra-Sorella: reconfigure as rarely as possible.
- Guides: Inack et al. PRB 98 235145 (arXiv:1809.03562): better guide turns required N_w from exponential to polynomial. Sikora et al. PRB 84 115129
  (arXiv:1105.1322): quantum-ice guide exp[alpha N_f + beta m_R + sum gamma_ij tau_i tau_j] (pair-plaquette Jastrow, SR-optimised).
  No published Gaussian-photon (~1/|k| kernel) guide found.
- Hermele-Fisher-Balents PRB 69 064404: CUBIC model = ours; L=2 zero-flux sector 880 states, 864 connected (matches our 864); n_f(RK) ~ 0.260.
- Benton-Sikora-Shannon PRB 86 075154 (PYROCHLORE, not ours): mu=0 photon c = 0.6 +- 0.1 (pyrochlore cell units); single-mode bound on c
  "indistinguishable" from c within errors; Gaussian lattice theory fits S(k) within a few percent.
- No report of slow GFMC drift in these models found.
