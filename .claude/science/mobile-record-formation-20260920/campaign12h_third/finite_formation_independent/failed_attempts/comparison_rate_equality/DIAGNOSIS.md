The first post-comparison helper used Python/SymPy structural equality between
the independently simplified rational rate and the author's algebraically
equivalent unevaluated complex-factor expression. For example, 1183/545 was
compared with (-13+7i)(-15379/118810-8281i/118810). Their difference simplifies
exactly to zero. The preserved diagnostic checks all three models and records
every mismatch; the independent model rate and the analytic rate already
agreed in each case.

The repair uses exact simplify(lhs-rhs)==0 for each mathematical comparison.
No tolerance, parameter, physical model, primary source, or scientific target
changed. The original helper, streams and exit-one receipt remain preserved.
