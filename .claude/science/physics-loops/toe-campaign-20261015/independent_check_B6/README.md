# Independent check: range three (B1 Theorem 4') and the spin-3/2 coin

A fresh agent context was given only the problem statements, not the notes,
the runners or the expected answers.

- **Range three, spin-1/2, {-3..3}^3: constant only.** The route differs from
  the note's.
  - It first classifies the D4-covariant 2D walks on {-3..3}^2 exactly: 172
    line cases, 171 linearly inconsistent, and the last closed by a Singular
    radical computation.
  - So U = 1 on all six planes k_j in {0, pi}.
  - A divisibility and positivity argument follows: g = s1 s2 s3 h and
    1 - f = s1^2 s2^2 s3^2 p, so p(2 - S p) = |h|^2. Point conditions at
    {0, pi}^3 then force p = 0, and this step is machine-checked.
  - Scripts: `plane_*`, `q1_*`, `lines.py`, `polysys.py`, `realbasis.py`.
- **Spin-3/2 coin on the cell: constant only.** It uses the model
  E_{1/2} (x) E with a rational conjugation action. On the lines (t,0,0) and
  (t,pi,pi) the line lemma applies via the C4 eigenvalues.
  - 10 of 19 single-line patterns are excluded exactly over Q(i).
  - The 81 two-line cases are settled over F_32009 and F_40009 (unit ideal
    except the constant case), and 6 of them by modStd over Q.
  - This stage is modular evidence, not a certificate over Q. The note's own
    computation (`exact_extensions/`) is exact over Q(sqrt 3).
  - Scripts: `q2_*`; mod-p logs in `q2fp/`.

The generated Singular case files were not archived, to save space; the
scripts regenerate them. Limit of independence: the checker is the same model
family in a new context.
