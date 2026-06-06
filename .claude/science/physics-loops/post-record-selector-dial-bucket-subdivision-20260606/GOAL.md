# Goal

Split the large selector/dial audit bucket into sub-queues that can be attacked
without forcing a dial.

The useful split is:

- Koide/generation selector rows;
- stability/dynamics selector rows;
- measure/weight/normalization rows;
- generic selector-rule rows.
