How it works (simple explanation)

dp[i][j] answers the question:
“Does the substring s[i:] match the pattern p[j:]?”

We fill the table from the back to the front.

Two major cases:
1. Next char is *

Example: a*, .*, etc.

We can either:

ignore the x* (0 occurrences) → dp[i][j+2]

use 1 occurrence if it matches → dp[i+1][j]

2. Next char is normal or .

Then we must match this char and move forward.
