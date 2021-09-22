
# Improved-QPP
[Query Performance Prediction through Retrieval Coherency](https://link.springer.com/content/pdf/10.1007/978-3-030-72240-1_15.pdf)

The problem of Query Performance Prediction (QPP) addresses evaluating the quality of retrieved information in satisfying the information need behind the query. While most of the QPP methods focus on the query and retrieved documents’ similarity and score, in this work, we propose a host of post-retrieval QPP metrics based on documents’ associations. We empirically study the potential of commonly used QPP baselines to be improved using document association. 

- Post-retrieval QPP baselines include:
  1. WIG
  2. Clarity
  3. QF
  4. NQC
  5. σ<sub>k</sub> (known as SD)
  6. n(σ<sub>x%</sub>) (known as ISD)
  7. SMV 
- Document association metrics includes calculating the following features in Document Association Network:
  1. ACC : Average Clustering Coefficient
  2. ADC : Average Degree Connectivity
  3. AND : Average Neighbour Degree
  4. D :  Density
  5. WACC : Weighted Average Clustering Coefficient
  6. WADC : Weighted Average Degree Connectivity
  7. WAND : Weighted Average Neighbour Degree
  8. WD :  Weighted Density
  

 
Results can be found in results directory and can be reproduced as follows: 
```
evaluate.py [-h] [-c  corpus] [-b baseline] [-d density_metric]
```

 - choose corpus from ['rb04', 'gov2', 'cw09']
 - choose density_metric from ['ACC', 'WACC', 'ADC', 'WADC', 'AND', 'WAND', 'D', 'WD']:
 - choose QPP baseline from ['WIG', 'Clarity', 'NQC', 'QF', 'ISD', 'SD', 'SMV']

for example: 

```
python evaluate.py -c rb04 -b WIG -d WD
```

will have the following output:

```
Corpus=rb04
Baseline= WIG
Density=WD
Pearson rho= 0.568209855531196   Kendall tau 0.4222981366459627
```


 The Table below shows the Pearson Rho and kendall Tau correlation of baselines standalone and baselines linearlyinterpolated with our host of document association metrics, respectively. It is shown that considering the relationship between the retrieved documents can boost the QPP methods performance. 


<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-c3ow" colspan="3"><span style="font-weight:bold">Pearson Rho</span></th>
    <th class="tg-c3ow" colspan="3"><span style="font-weight:bold">Kendall Tau</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">QPP baselines</td>
    <td class="tg-0pky">Document Association</td>
    <td class="tg-0pky">Robust 04</td>
    <td class="tg-0pky">ClueWeb09</td>
    <td class="tg-0pky">GOV2</td>
    <td class="tg-0pky">Robust 04</td>
    <td class="tg-0pky">ClueWeb09</td>
    <td class="tg-0pky">GOV2</td>
  </tr>
    <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br><br>WIG<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.31</td>
    <td class="tg-0pky">0.51</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.23</td>
    <td class="tg-0pky">0.36</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.52</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.46</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.24</td>
    <td class="tg-4yk9">0.31</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.58</td>
    <td class="tg-0pky">0.34</td>
    <td class="tg-0pky">0.21</td>
    <td class="tg-0pky">0.39</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.52</td>
    <td class="tg-4yk9">0.33</td>
    <td class="tg-4yk9">0.54</td>
    <td class="tg-4yk9">0.39</td>
    <td class="tg-4yk9">0.22</td>
    <td class="tg-4yk9">0.46</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.52</td>
    <td class="tg-0pky">0.24</td>
    <td class="tg-0pky">0.59</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.16</td>
    <td class="tg-0pky">0.46</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-4yk9">0.37</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-4yk9">0.37</td>
    <td class="tg-w262">0.25</td>
    <td class="tg-4yk9">0.42</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.41</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.57</td>
    <td class="tg-0pky">0.41</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.42</td>
    <td class="tg-0pky">0.24</td>
    <td class="tg-0pky">0.42</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br><br>Clarity<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.30</td>
    <td class="tg-0pky">0.45</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.22</td>
    <td class="tg-0pky">0.32</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.53</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.46</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.19</td>
    <td class="tg-4yk9">0.33</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.51</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.44</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.27</td>
    <td class="tg-0pky">0.32</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.52</td>
    <td class="tg-4yk9">0.32</td>
    <td class="tg-4yk9">0.46</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.21</td>
    <td class="tg-4yk9">0.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.46</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.20</td>
    <td class="tg-0pky">0.29</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.54</td>
    <td class="tg-4yk9">0.33</td>
    <td class="tg-4yk9">0.45</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.17</td>
    <td class="tg-4yk9">0.28</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.52</td>
    <td class="tg-0pky">0.32</td>
    <td class="tg-0pky">0.45</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.25</td>
    <td class="tg-0pky">0.32</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.51</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.21</td>
    <td class="tg-0pky">0.34</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br><br>QF<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.23</td>
    <td class="tg-0pky">0.43</td>
    <td class="tg-0pky">0.32</td>
    <td class="tg-0pky">0.14</td>
    <td class="tg-0pky">0.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.43</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.21</td>
    <td class="tg-4yk9">0.27</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.43</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.17</td>
    <td class="tg-0pky">0.38</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.42</td>
    <td class="tg-4yk9">0.20</td>
    <td class="tg-4yk9">0.47</td>
    <td class="tg-4yk9">0.35</td>
    <td class="tg-4yk9">0.14</td>
    <td class="tg-4yk9">0.36</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.42</td>
    <td class="tg-0pky">0.25</td>
    <td class="tg-0pky">0.51</td>
    <td class="tg-0pky">0.32</td>
    <td class="tg-0pky">0.17</td>
    <td class="tg-0pky">0.37</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.41</td>
    <td class="tg-4yk9">0.28</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-4yk9">0.33</td>
    <td class="tg-4yk9">0.17</td>
    <td class="tg-4yk9">0.42</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.40</td>
    <td class="tg-0pky">0.28</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.31</td>
    <td class="tg-0pky">0.15</td>
    <td class="tg-0pky">0.36</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.42</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.47</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.24</td>
    <td class="tg-0pky">0.31</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br>NQC</td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.48</td>
    <td class="tg-0pky">0.21</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.17</td>
    <td class="tg-0pky">0.27</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-0pky">0.53</td>
    <td class="tg-0pky">0.32</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.25</td>
    <td class="tg-0pky">0.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.52</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.41</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.18</td>
    <td class="tg-0pky">0.29</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-0pky">0.47</td>
    <td class="tg-0pky">0.24</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.24</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.51</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.15</td>
    <td class="tg-0pky">0.36</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.47</td>
    <td class="tg-4yk9">0.21</td>
    <td class="tg-4yk9">0.43</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.15</td>
    <td class="tg-4yk9">0.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.24</td>
    <td class="tg-0pky">0.43</td>
    <td class="tg-0pky">0.36</td>
    <td class="tg-0pky">0.15</td>
    <td class="tg-0pky">0.27</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.36</td>
    <td class="tg-0pky">0.46</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.22</td>
    <td class="tg-0pky">0.39</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br>SD<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.18</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.34</td>
    <td class="tg-0pky">0.12</td>
    <td class="tg-0pky">0.28</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.48</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.16</td>
    <td class="tg-4yk9">0.27</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.25</td>
    <td class="tg-0pky">0.44</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.15</td>
    <td class="tg-0pky">0.34</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-4yk9">0.21</td>
    <td class="tg-4yk9">0.50</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.18</td>
    <td class="tg-4yk9">0.33</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.31</td>
    <td class="tg-0pky">0.48</td>
    <td class="tg-0pky">0.33</td>
    <td class="tg-0pky">0.23</td>
    <td class="tg-0pky">0.35</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.47</td>
    <td class="tg-4yk9">0.26</td>
    <td class="tg-4yk9">0.43</td>
    <td class="tg-4yk9">0.39</td>
    <td class="tg-4yk9">0.18</td>
    <td class="tg-4yk9">0.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.52</td>
    <td class="tg-0pky">0.30</td>
    <td class="tg-0pky">0.47</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.34</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.53</td>
    <td class="tg-0pky">0.33</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.41</td>
    <td class="tg-0pky">0.22</td>
    <td class="tg-0pky">0.36</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br>SMV</td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.31</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.22</td>
    <td class="tg-0pky">0.21</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.49</td>
    <td class="tg-4yk9">0.30</td>
    <td class="tg-4yk9">0.41</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-4yk9">0.17</td>
    <td class="tg-4yk9">0.29</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.52</td>
    <td class="tg-0pky">0.18</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.16</td>
    <td class="tg-0pky">0.34</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.53</td>
    <td class="tg-4yk9">0.30</td>
    <td class="tg-4yk9">0.45</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.22</td>
    <td class="tg-4yk9">0.37</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.47</td>
    <td class="tg-0pky">0.26</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.31</td>
    <td class="tg-0pky">0.13</td>
    <td class="tg-0pky">0.35</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-4yk9">0.50</td>
    <td class="tg-4yk9">0.22</td>
    <td class="tg-4yk9">0.49</td>
    <td class="tg-4yk9">0.38</td>
    <td class="tg-4yk9">0.13</td>
    <td class="tg-4yk9">0.39</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.50</td>
    <td class="tg-0pky">0.18</td>
    <td class="tg-0pky">0.49</td>
    <td class="tg-0pky">0.37</td>
    <td class="tg-0pky">0.13</td>
    <td class="tg-0pky">0.34</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.33</td>
    <td class="tg-0pky">0.55</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.29</td>
    <td class="tg-0pky">0.37</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="9"><br><br><br><br><br><br><br><br><br>ISD<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">ACC</td>
    <td class="tg-0pky">0.56</td>
    <td class="tg-0pky">0.25</td>
    <td class="tg-0pky">0.47</td>
    <td class="tg-0pky">0.41</td>
    <td class="tg-0pky">0.21</td>
    <td class="tg-0pky">0.33</td>
  </tr>
  <tr>
    <td class="tg-0pky">WACC</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-bhur">0.40</td>
    <td class="tg-4yk9">0.43</td>
    <td class="tg-4yk9">0.34</td>
    <td class="tg-bhur">0.25</td>
    <td class="tg-4yk9">0.33</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADC</td>
    <td class="tg-0pky">0.56</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.57</td>
    <td class="tg-0pky">0.39</td>
    <td class="tg-0pky">0.21</td>
    <td class="tg-0pky">0.38</td>
  </tr>
  <tr>
    <td class="tg-0pky">WADC</td>
    <td class="tg-4yk9">0.54</td>
    <td class="tg-4yk9">0.35</td>
    <td class="tg-4yk9">0.55</td>
    <td class="tg-4yk9">0.36</td>
    <td class="tg-4yk9">0.21</td>
    <td class="tg-4yk9">0.43</td>
  </tr>
  <tr>
    <td class="tg-0pky">AND</td>
    <td class="tg-0pky">0.57</td>
    <td class="tg-0pky">0.26</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.42</td>
  </tr>
  <tr>
    <td class="tg-0pky">WAND</td>
    <td class="tg-bhur">0.60</td>
    <td class="tg-4yk9">0.32</td>
    <td class="tg-bhur">0.62</td>
    <td class="tg-bhur">0.41</td>
    <td class="tg-4yk9">0.19</td>
    <td class="tg-bhur">0.47</td>
  </tr>
  <tr>
    <td class="tg-0pky">D</td>
    <td class="tg-0pky">0.54</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">0.59</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.19</td>
    <td class="tg-0pky">0.42</td>
  </tr>
  <tr>
    <td class="tg-0pky">WD</td>
    <td class="tg-0pky">0.57</td>
    <td class="tg-0pky">0.43</td>
    <td class="tg-0pky">0.58</td>
    <td class="tg-0pky">0.38</td>
    <td class="tg-0pky">0.27</td>
    <td class="tg-0pky">0.45</td>
  </tr>
</tbody>
</table>
