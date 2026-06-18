# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| empirical small `m_nu` | fixes Dirac Yukawa scale | observational comparator | I12 comparator bridge | yes | yes | derive small neutrino mass in neutrino lane | explicit conditioning input |
| one-Higgs `<H> = 174 GeV` convention | maps `m_nu` to `y_nu` | admitted convention / inherited EW bookkeeping | I12 parent | yes | yes | native EWSB vev bridge | unchanged |
| `Gamma ~ y_nu^2 T` scaling | thermalization rate scaling | standard thermal comparator | I12 comparator bridge | yes for scaling; exact prefactor no | yes | collision-operator derivation | prefactor robustness added |
| `H ~ T^2/M_Pl` scaling | radiation-era expansion comparator | standard cosmology comparator | I12 comparator bridge | yes for scaling; exact `1.66` no | yes | native cosmology bridge | prefactor robustness added |
| `g_* = 427/4` | threshold value | retained-bounded declared inventory arithmetic | `SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md` | yes | yes | no local change | unchanged |

## Retirement Movement

This block retires exact-prefactor sensitivity as a load-bearing concern inside
the comparator packet. It does not retire the empirical small-`m_nu` wall or
derive thermal/cosmology scalings from framework primitives.
