# Goal

Block23 narrows the source-domain split left by the typed-edge work:

> Determine whether the sign half of the signed scalar candidate is already
> supported by current Route-2 positivity and T-side orientation.

Result: yes. Positivity gives the positive-lift domain `q_E > 0`; the granted
T-side data give `q_T > 0` and `s_TE < 0`; therefore `c_TE = s_TE q_T / q_E`
is negative throughout that domain.

The remaining blocker is magnitude/typecast: the current surface still has to
supply `|c_TE| = F_adj` or a direct typed landing edge.
