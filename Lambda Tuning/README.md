
It is important to understand the impact of the proposed coherence measures on the final reported performance values in our experiments. 
To this end, we report the frequency of values chosen for λ (as a percentage of overall adopted λ values) based on 10-fold cross validation in Figure 1. 
The values for λ show how impactful λ is on the final interpolated performance predictor.


| ![space-1.jpg](https://github.com/Narabzad/QPP-Retrieval-Coherency/blob/main/Lambda%20Tuning/fig2.PNG) | 
|:-:| 
| *Figure 1. The frequency (in %) of the adopted interpolation coefficients (λ) in different corpora* |

In Clueweb09, a λ=0.5 was the most widely adopted interpolation coefficient, which means that the coherence measures and base QPP methods had the same impact on the final outcome. 
For Gov2, the most frequent value for λ is 0.6, which also shows a balanced contribution from our proposed coherence measures on the interpolation.
For Robust04, the most frequent λ is $0.9$, which shows lesser impact by our coherence measure; 
however, as observed in Table 5, the interpolation with a λ=0.9 does lead to statistically significant improvements. 

We note that in none of our experiments and based on 10-fold cross-validation, λ was never determined to be at 1, i.e., no impact by the coherence measures.
