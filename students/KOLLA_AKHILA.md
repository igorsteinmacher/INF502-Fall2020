## Elastic Coupled Co-clustering for Single-Cell Genomic Data

**Venue:** Department of Statistics, The Chinese University of Hong Kong, HK**

**Number Of Pages:** 18

**GitHub Link:** (github for datasets and code)[https://github.com/cuhklinlab/elasticC3]

### Research Outcomes:

In this paper, the author focuses on clustering the single-cell genomic data across different domains.
The author uses an unsupervised transfer learning framework, which utilizes knowledge learned
from the dataset in one domain to cluster another dataset from a different domain. It is assumed that
the primary dataset has a good feature representation which can better the clustering on the target
dataset.

a. The author has focused on improving the performance of clustering one dataset using the knowledge
obtained from another dataset. Also, the degree of information shared among the datasets may vary
and their distributions can be different as the datasets are from different domains.

b. This approach significantly increasing the clustering performance as we cluster both the auxiliary and
target datasets optimally. This model can elastically control the degree of knowledge transfer.

### Contributions:

1. **Theoretical:**

a. The author defines an objective function to minimize the loss of information among the cells
and features of the dataset after clustering. The objective function for the auxiliary dataset and target
dataset is different. The Target dataset makes use of hyperparameters α,β which control the knowledge
transfer among the datasets, these values tend to higher if the auxiliary data are similar to the target
data.

b. The objective function for the algorithm elasticC3 is monotonically decreasing and that is
demonstrated with a theoretical proof that shows LT(i) >= LT(i+1) where LT is the objective function
for target and i represents the iterations.

c. The search space for the algorithm is finite and the algorithm converges to a local minimum since
finding a global optimal is NP-hard. The computational complexity of the algorithm is linear. This is because first,
we find the clustering function for Auxiliary data which takes O(NA + K). dA and then the clustering
function for Target data takes O (NT + K). dT. Therefore, the algorithm computes in
O((NA + K) . dA + O(NT + K) . dT) where dA, dT are the cell-feature co-occurrences for auxiliary, target
datasets respectively and NA,NT,K cluster constants thereby reducing the complexity of elasticC3
to O(dA+dT).

2. **Algorithmic:**

a. The algorithm presented gives the optimal clustering functions for both auxiliary and target dataset
based on the objective function which is reformulated using KL divergence for optimal results.

b. Step 1 of the algorithm calculates the C(i)x, C(i)w iteratively updating the cluster assignment for the
cells and features of the auxiliary data IA times. The step2 of the algorithm calculates the C(i)y, C(i)z
iteratively updating the cluster assignment for the cells and features of the auxiliary data IT times.

c. The KL divergence value is calculated over the cells and cell clusters and features and feature clusters.
The algorithm doesn’t clearly show us about iterating over clusters of cells and features and calculating
KL divergence value. It’s stated to obtain a minimized KL divergence value it should be iteratively
updated over the clustering functions but didn’t mention why.

3. **Empirical:**
The author experimented with simulated datasets and real single-cell genomic datasets to evaluate the
performance of the algorithm.

a. The author compares the elasticC3 method with the classic unsupervised clustering methods like STC
and k-means clustering and evaluates the performance on four criteria NMI, ARI, RI, purity.

b. The author sets the number of cells and feature clusters and also assumes that only a subset of
features in auxiliary data has a correlation with the features in target data and keeps varying the
percentage of correlation and this uses a simulated data set. The results show that all three methods
give almost similar NMI, ARI, RI, purity values.

c. Classic unsupervised clustering methods
The clustering results for target datasets in the real datasets are not clear and uses more than
specified classic unsupervised methods to evaluate the data and the data settings.


**Link To Paper**: (Click here to access paper online)[https://arxiv.org/pdf/2003.12970.pdf]
