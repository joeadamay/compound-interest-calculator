# Compound Interest Calculator

Calculate the accumulated value on balance subject to compound interest and outside changes, e.g. a loan or bank account.

## How to Use
Run `python3 compound-interest-calculator.py`

Then, answer the queries:<br/>
`Principle:` The initial value on the account.<br/>
`Rate:` The rate of the interest added per cycle (as a percentage).<br/>
`Payments:` The ammount by which the balance is reduced every cycle (before interest is applied).  Use a negative value to increase the balance.<br/>
`Number of Cycles:` The number of cycles after which to calculate the accumulated sum.

## Additional Notes
See the document `A Formula for the Computation of Compound Interest With Payments.pdf` for the proof and derivation of this algorithm.
