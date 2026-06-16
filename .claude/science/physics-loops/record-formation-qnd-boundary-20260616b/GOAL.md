# Goal

Repair the audited-failed record-formation pointer row without changing audit
verdicts. The failed audit objected that the old surface could be read as
`[H_int, Pi_S]=0` being sufficient for record formation. This branch makes the
supported result explicit:

- QND is necessary and sufficient only for all-state pointer-population
  conservation.
- Record formation additionally needs a nonzero fragment-imprinting channel,
  a recording time, and fresh/idle/decoupled completed fragments.
- A conserved-charge transfer lies only in the pointer-conserving class; it
  does not by itself prove a physical record channel.
