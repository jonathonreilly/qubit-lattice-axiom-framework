# Assumptions And Imports

- The current audited row is conditional because P1/P2/P3/P4 and B-W were not
  retained one-hop authorities in the restricted packet.
- This PR does not make those packets retained. It names them as source-side
  candidate discharges for independent audit.
- The all-period site-license packet still assumes the site license and
  unitarity; it discharges the finite-period flat-or-saturating dichotomy.
- The tick-unitarity packet still has named C-reading and N-reading premises;
  it reduces bare unitarity/pairing rather than proving OS0 c_t/c_s.
- B-W remains open.
