1. Give an example of the following types of machine learning.
For each example, give the feature set, and explain the aim of the learning.
(a) Supervised learning
> classification (spam, cat vs dog, kNN etc.)
>   (SPAM): **features** are the words, their frequency and their combinations, the author, and possibly meta and HTML elements such as links. **task** is to predict whether or not an email is spam.
> regression (stock market predictions)
>   **features** are the season(LSTM), the day, the past shares values, (in more refined algorithms) other stocks trends, big news or world events etc. **task** is to predict the stock market value in a future time period.
(b) Unsupervised learning
> clustering (movie prediction)
>   **features** come from watched movies (genre, director, actors etc.) **task** is to identify similar movies to recommend.


2.  For each of the following machine learning tasks give the feature set, and explain the aim of the learning task
(a) Binary classification
> The app "is This an hot-dog":
>   **Input features**: being an image classifier, the image itself (The pixels) is the only feature.
>   **Aim**: learn to correctly identify hot dogs
(b) Multiclass classification
> 
>   **Input features**: 
>   **Aim**: 
(c) Clustering
> cluster different species of plants:
>   **Input features**: may include the region, the clime required to survive, the type of seeds (including weight, length, width and colour), the petal colour, width, height, smell intensity, etc.
>   **Aim**: identify patterns in the classified plants to identify a genealogical tree.
(d) Regression
> Job pay estimator:
>   **Input features**: nation, location, working hours, learning level (PhD, master etc.), company, economical period ( demand and supply)
>   **Aim**: Predict the salary for a given job.

3. 
(a) Explain how a k-nearest neighbour classifier is trained.
> The idea is to create many discriminant function which define areas in feature space. Each area is associated to a class. 
(b) Explain how a k-nearest neighbour classifier is used to classify a new example.
> An input is classified according to the area it falls in. 
(c) For a given set of data, what difference in performance would you expect to see between a 1-nearest neighbour classifier and a 5-nearest neighbour classifier?
> I would expect the 5-NN to be more probabilistic, yet to hold better results as it can deal with outliers better.

4. 
|           |   | Actual |   |
|-----------|---|--------|---|
|           |   | **T**      | **F** |
| **Predicted** | **T** | 8      | 2 |
|           | **F** | 3      | 7 |

A) Accuracy = 8 + 7 / 20 = 3/4 = 0.75
B) [Draw the mesh]
C) The diagonal is bigger than the other cells, so the predictor is doing nice.
D) Precision = 8 / 8 + 2 = 4/5 = 0.25
E) Recall = 8 / 8 + 3 = 8/11 = 0.727272...
F) F = 0.25 x 0.727272 / (0.25 + 0.727272...) = 0.18604 

5. Using the Manhattan distance, where does the samples belong to according to 3-NN?
   
A) (3, 1) => C~1~ 100%
B) (4, 5) => C~2~ 100%
C) (2, 3) => (1 C~1~ is at d=0, 3 C~1~ & 1 C~2~ have d=2)
As no explanation on what to choose is provided, I will assign a score of 1/N to all the points having distance = 2
So P(x = C~1~) = (1 + 2 $\cdot$ (3/4)) / 3 = 2.5 / 3 = 83.3% 
D) (4, 3) => C~2~ 66.7%