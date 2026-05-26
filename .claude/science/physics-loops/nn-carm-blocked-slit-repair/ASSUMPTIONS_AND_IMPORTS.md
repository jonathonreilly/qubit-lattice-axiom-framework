# Assumptions And Imports

- Harness constants remain fixed at `BETA=0.8`, `K_PHYS=5.0`,
  `PHYS_L=40`, `FANOUT=3`, and slit plane `nl//3`.
- The primary runner now imports the actual field-free blocked-slit
  propagation function `measure_arm_distribution(...)` from
  `scripts/lattice_nn_rescaled_continuum_identification.py`.
- The historical `C_arm=2.7107` diagnostic fit is comparator-only and is not
  used as the premise of the direct blocked-slit check.
- The no-slit full-kernel L1/L2 comparison remains context-only; the
  load-bearing bridge is the direct blocked-slit sigma table.
