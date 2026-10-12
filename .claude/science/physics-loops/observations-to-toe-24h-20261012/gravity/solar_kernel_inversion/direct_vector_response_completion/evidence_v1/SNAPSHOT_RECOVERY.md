# Exact historical snapshot recovery

The original independent-review snapshot `prior_DIRECT_DYNAMICS.md` contains
an extra blank EOF line. It was not edited or deleted. A fresh checkout can
recover it byte-for-byte by decoding `IMMUTABLE_PRIOR_SNAPSHOT.json` into its
recorded block-relative path and checking the recorded SHA256. Other reviewed
source snapshots are ordinary tracked files. This representation change has
no scientific effect and does not replace the original proof or failure.
