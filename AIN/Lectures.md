[TOC]

<style>
    img {
        border: solid;
        margin: 3px;
    }
        
    h1:not(:first-of-type)::before {
        content: "";
        height: 100px;
        padding: 100px;
        display: block;
    }

    .no-mt {
        margin-top: -16px;
    }

    .warning {
        background: rgba(255, 0, 0, .3); 
        padding: 5px; 
        padding-left: 10px;
        margin: 20px 0; 
        border-left: solid 3px rgb(220, 0, 0);
    }

    .warning::before {
        content: "WARNING: ";
        font-weight: bold;
        color: rgb(220, 0, 0);
    }

    .info {
        background: rgba(240, 240, 0, .3); 
        padding: 5px; 
        padding-left: 10px;
        margin: 20px 0; 
        border-left: solid 3px rgb(190, 190, 0);
    }

    .info::before {
        content: "INFO: ";
        font-weight: bold;
        color: rgb(190, 190, 0);
    }

    .definition {
        background: rgba(80, 80, 255, .2); 
        padding: 5px; 
        padding-left: 10px;
        margin: 20px 0; 
        border-left: solid 3px rgb(80, 80, 255);
    }

    .definition::before {
        content: "DEFINITION: ";
        font-weight: bold;
        color: rgb(80, 80, 255); 
}
</style>


# Week 1

An agent, normally receives inputs (images, audios, waves from object detectors, etc.) called percepts.
These percepts are elaborated, help generate new states which, in turn, help decide the next action

## Environment Characteristics
<img src="img/Agent_characteristics">
<br>
<br>
<br>
<br>
<br>
<br>
# Week 2

## Observability

- Full observability: Everything can be observed.
    
        Chess, Go etc.
- You may get more information going on, but, at least at the beginning, not everything belonging to the environment (and about other possible agents) is known.
        
        Poker (you don't know enemies cards), a maze, real world, self-driving cars etc.

### Partial observability causes
Partial observability may depend on different things:
- The agent may **lack of some sensors**, or they are not powerful enough (physic limitations like atoms);
- There may be **noise** interferring with the sensors;
- **Computational complexity**;
- **World structure**.

<br>

## Uncertainty
<img src="img/uncertainty.png">


### Handling Uncertainty
- Using **probability** (given the available evidences); probabilistic assertions summerise the effects of:
    - **laziness**: failing to enumerate exceptions, qualifications, etc.;
    - **ignorance**: lack of relevant facts, initial conditions etc. (we tend to ignore these).
    
    Nonetheless, probabilistic assumptions come with issues such as computational complexities, obtaining values, semantics etc.

> <img src="img/fuzzy_logic.png">
> **Fuzzy logic** might look like probabilistic, but it's completely deterministic

- Using **utility theory**, used to represent and infer preferences;
- Using **decision theory** (utility theory + probabilistic theory).


## Probabilistic basis

>**Notion** -> P(*h* | *e*) is the probability of the hypothesis *h* given the event *e*

**sample space** (denoted as Big-Omega) -> indicates all the possible outcomes
*small-omega belongs to Big-omega* is a simple point, atomic event (it can't be two of these events at the same time)

An **event** is a set of sample points

**Probability space** (or **model**) is a sample space with an assignment P(*w*) for every *w* *belongs to* *Big-omega* (which sum has to be 1)

**Proposition**: mathematical statements which are true or false like (Cavity = True)
    
    You can use Boolean logic operators (AND, OR ...) as well as mathematical (<, >, != ...)

P(a OR b) = P(a) + P(b) - P(a AND b) 
    
    (a AND b is basically already calculated in P(a), so P(b) calculates it again)

**Prior or unconditional probabilites** happens when two probabilities are not related to to each other. Like having a cavity (Carie) and a sunny weather.

**Posterior probabilities** happens when we have additional evidences affecting the probability fo something:

>e.g. P( cavity = true ) = 0.1  . . . . . P( cavity | toothache ) = 0.2

A nice to remember formula is:
> P(a | b) = P(a AND b) / P(b)
> (assuming p(b) > 0)


Probability distribution can be represented as a vector which has to be exhaustive (include all the possible outcomes), mutual exclusive (no option has to be repeated), and of course the sum has to be 1.
> eg. <0.72, 0.1, 0.08, 0.1>

A subtle notation to look at is P() which generates a number and **P()** (bold) which generates a vector.
In the case the formula is **P**(H | e), the resulting vector is <P(H | e), (¬H | e)>

When looking at the `given clause` (in P(a | b) b is the given clause), some components can be removed. For instance, if a: *Cavity = TRUE* and b: *Toothache & Cavity*, of course P(a | b) = 1, and the Tootache part can be removed as its contribution is less than the other or, like in other cases, meaningless (suppose rather than tootache I had *Curtains Blue = True*).
<ht</ht>
> P(a AND b) = P(a | b)`*`P(b) = p(b | a)`*`P(a)

Comma `,` is often used in place of `AND`, so `P(a,b) = P(a AND b)`

### Chain Rule
<img src="img/ChainRule.png">

> P(a,b) = P(a,b,c) + P(a,b,¬c)

> **P**(a | b) = *alpha*\***P**(a,b) 
where *alpha* = 1 / P(b)

### Independence
When you create a matrix of the possibilities say of **P**(Cavity, Weather), the two of them are not related, so **P**(Cavity, Weather) = **P**(Cavity)\***P**(Weather). Suppose both of them have 100 possible outcomes, the matrxi resulting would be 100 * 100, but being **independent**, you can store them as 100 + 100. Furthermore, as the sum of the events always adds up to 1, you can store them as 99 + 99.


### Conditional Independence
Absolute independence is amazing, but rare. It formulates like 
>A is **conditionally independent** of B *given* C
>**P**(a | b, c) = **P**(a | b)

**ADVICE:** in case you have P(a | b) which is very high, don't automatically expect P(b | a) to be high as well    


# Week 3

## Naive Bayes & Bayesian networks

**Naive Bayes** means that you naively assume there's no correlation between 2 events.
> <img src="img/Bayesian_Independency.png" style="border: solid 2px">
> 
> **Bayesian networks** are a xvay to represent these dependences

> **CPT** (conditional probability table) are boolean table showing probabilites
> <img src="./img/CPT.png">

<img src="img/Bayesian_networks.png" style="border: solid 2px">


I AM NOT SURE WHICH IS THE CORRECT ONE *****
--
- A further way to reduce the storage is that to scompose a random variable, and then remove one of them
> e.g. **North America** <=> **Mexico** V **USA** V **Canada** (one of them can go)

- If there is a boolean random variable which is implied by other variables, this one can be omited
> e.g. **North America** <=> **Mexico** V **USA** V **Canada**, North America is already specified by the others, hence, we can omit it

## Markov Blanket
A Markov Blanket of a node X is the set of:
- parents of X
- children of X
- parents of X's children

## Inference
> **Given some evidence and reasoning, what conclusions can we draw**

### Inference by ENUMERATION
Among all the inferences, this is the only one that is **deterministic** as opposed to the others which are **probabilistic**.

When sampling, you can just take whatever sample you get, you can **reject** your samples if they are not efficient, or, as opposed to the latter, you can **weight** your samples, so you don't have to throw them away.

### Importance Sampling
Like for sampling, you may want to calculate a probability P(h | s, t).
The difference with normal sampling is that, since you want to calculate h given **s** and **t**, you assume that **s** and **t** are both true.

However, this will make the final result (probability) falsish. To fix this, you weight the samples that are taken for granted in the $given$ clause.

Suppose you have this network:
<img src="./img/network_for_weighting_likelihood.png">

and you want to calculate $P(h|s, t)$, then, using random sampling you calculate $P(m), P(c | s, t), P(h | t)$, `but P(t | M) you assume it's true` as well as `P(s | M)` as they both are part of the given clause. 
> Look out, **M** is neither **m** nor **¬m** yet as it has to be calculated using sampling.

Say, using sampling, that **M = m (so m = True)**, in that case **s** is still True (as it's part of the given clause), but what is the $likelihood$ of it happening, aka. $P(s | m)$?
The value (in this case **weight**) is given in the CPT and it's `0.20`.
Then we do the same for **t**, and the weight for $P(t | m)$, which is `0.70`.

Now, whatever is the probability we obtain using sampling, we wight it taking into account the given clause events weights.
$<m, c, h, s, t* 0.20 * 0.70$ 

    [always keeping in mind that we don't sample s and t] 

<img src="./img/likelihood_weighting.png">
<img src="./img/likelihood_weighin.png">

# Week 4

## Expected Value
Suppose you play a game with different possible outcomes, some good and some bad ones.
The so called **Expected value**(**E[X]**) is the sum of the probabilities of each possible outcome. 
> e.g. you play a dice game and:
> - win **10\$** if the result is **6**, 
> - loose **2\$** if the result is **odd**,
> - loose **1\$** if anything else.
> 
> $P(winning 10\$) = 1/6, P(loosing 2\$) = 3/6, P(loosing 1\$) = 2/6$  
> E[X] = 1/6 \* 10 + 3/6 \* -2 + 2/6 \* -1 = 1/3
> as E[X] is positive, you should take the risk.

### Linearity of expectation formula
In the example, if you play 10 times, expected value doesn't change for each game, and the total is multiplied by 10. There's a rule called Linearity of expectation which is describes as:
> **E[a\*X + Y] &nbsp; = &nbsp; E[a*X] + E[Y] &nbsp; = &nbsp; aE[X] + E[Y]**

### a* Function
We want our agent to be rational, so, given:
- a set of states **S**;
- an action **a**, and **s<sub>a</sub>** is the new state after applying a;
- an **utility function $u()$**;
  
> **a\*** = argmax $u$(s<sub>a</sub>)

The problem is that in any realistic situation, the resulting state is probabilistic. Instead we have to calculate the **expected utility** of each action and make the choice on the basis of that.

In other words, for each action **a** with a set of outcomes **s<sub>a</sub>**, the agent should calculate the **E[$u($a$)$]** for every **a** and pick the best one.

But if the action we are dealing with is **stochastic**, and the outcome in unsure?
Say for instance that both actions a1 and a2 have multiple outcomes like this:
<img src="./img/a-outcomes.png">

###### video 2

Now, there are 2 approaches to this problem:
- you are optimistic, and you hope the result will be the best (**maximax**), so the output of a\* would be the max value among the best values for each s<sub>a</sub>;
    > in this case, argmax(5, 7);
- or, if the there is a risk in getting the lowest score action (to say, the agent risks its life, or something very bad is related to it), you the best score among the worst ones for each action (**maximin**)
    > in this case, argmax(4, 3); 

<br>

## Markov Decision Process (MDP)
It is a **Markov Chain** with the addition of **probability and reward**; also, the probability distributions do not change.

This greedy approach takes into account only the next state, but in real life, agents have to take a **series of decisions**.

We can write a transition model to describe these **stochastic actions** and the model looks like:

> $P(s'| s, a)$

where $a$ is the action that takes the agent from $s$ to $s'$.

The probability, in this case, depends only on the previous and the next state, there's no "memory", i.e. the agent doesn't care about the previous states. This **transition** is known as **first order Markovian**.
This leads to a process called **Markov Decision Process (or MDP)**:
<img src="./img/MDP.png">

### Policy
Denoted as $\pi$, a **policy is a solution**, that is, a choice of action for every state. 
In any state $s$, $\pi(s)$ identifies what action to take.
> e.g. **$\pi$**: $\pi(s$<sub>0</sub>$)$ = left, $\pi(s$<sub>1</sub>$)$ = left, $\pi(s$<sub>2</sub>$)$ = right, etc....

Naturally we’d prefer not just any policy but the **optimum** policy which we found comparing policies by the **reward** they generate.

The optimum policy **$\pi$<sup>*</sup>** (Pi star) is the policy with the highest expected value.
At every stage the agent should perform **$\pi$<sup>*</sup>$(s$<sub>0</sub>$)$**


###### video 3

## Utility Run
Previously we have defined the utility function for a state, although this can be useful sometimes, we tend to prefer the utility for a **sequence of actions** also called a **run**.
We denote this function as 
> **$U$<sub>r</sub>([s<sub>0</sub>, s<sub>1</sub>, s<sub>2</sub>, ...., s<sub>n</sub>])**

Different type of utilty functions can be distinguished:
- based on the **horizon: finite or infinite** (how many state you consider, I think);
- based on the **reward: stationary (fixed) or non-stationary(it can change)**;
- based on **how later the agent gets the reward: additive or discounted**
  >**Additive:** R(s0, s1, ..., sn) = R(s0) + R(s1) + ... + R(sn)
  >**Discounted:** R(s0, s1, ..., sn) = R(s0) + $\gamma$ R(s0) + ... + $\gamma$<sup>n</sup> R(sn) ***[0 <= $\gamma$ < 1]***
  > What this means for discounted utilities is that, since action far away from our current state may include random factors and noise, we diminish their values.

In a "world" where utilities functions are infinite and additive, the are nou bounds on the min/max score of the function, and the output may be useless. To solve this problem there are 3 solutions:

### Proper policies
Always end up in a terminal state, so a **finite** expected utilities. A PAC-MAN whose only aim is to stay alive does not operate a proper policies as the steps can be infinite.

### Average reward
Sum the rewards of each state in the function, and then divide by $n$, aka, calculate the average score of the states.

### Discounted rewards
Scale the the reward based on the number of steps required to reach a state. Even if you have infinite steps, after a threshold, the reward will be close to 0.

<img src="./img/Bellman-equation.png">

###### video 4

## Bellman Equation

The formula to calculate $U(s) = R(s) + \gamma*max \sum P(s' | s, a) U(s')$. 
What this formula means, is that given a state, to calculate its utility, when to know the reward you obtain from that state + a $\gamma$ factor times the best E[X] obtained from the following states reachable from the current state. 

In the pacman example, R(s) is the cost of the action (0.04), whereas the remaining component is taken from the utility score of each possible next state. 

In the problem where the agent goes 80% of the time in the direction you specify, and 10% it goes to either traversal direction, the Bellman formula would result in:
<img src="./img/Bellman-applied.png">

> As you can figure out, Bellman equation is not computable in linear space, as from a state you can reach n new states, which in turn can reach n new states ($n^n$)

To reduce the space complexity, it is possible to use parallelism. In this case by creating an independent thread for each possible action. 
This process is called **value iteration** and is described by this pseudo-code: 
<img src="./img/value-iteration.png">
> [LOOK AT THE .XLS FILE TO FIGURE OUT THE ALGORITHM]

Another thing to mention is the fact that a reward is not always positive. In the case of PACMAN, for example, making a move might have a good utility score, but if no food is eaten, the moves has a cost of .4, which is in fact the reward.

This is the updated formula of Bellman
<img src="./img/Bellman-w-reward.png">

###### video 5
 
## Policy Iteration


### Policy Evaluation 
 
### Policy Improvement
Just look at one step ahead and take the best policy according to the scores given by policy evaluation.

The policy iteration process $O(n^3)$ is way faster the value iteration one $O(n^n)$, especially when using an approximation.
However, it is not guaranteed to converge. For this reason, it may be a good idea to create a first schema using `Policy `Iteration, and then converge using `Value Iteration`


# Week 5 

###### video 1 Introduction to game theory and Payoff matrix

## Payoff matrix
Suppose you have **2 agents:** $i$ and $j$. Create a matrix: 
- For each move of $i$ create a row in the matrix. 
- For each move of $j$ create a column in the matrix. 
- In each cell, write the reward for each agent, given they operate the move in that combination (row, column)

This matrix should look like this:
<img src="./img/PayoffMatrix.png">

However, it can be decomposed and a individual matrix can be created for each agent, and contains only the cost of such agent.
<img src="./img/PayoffMatrix2.png">


###### video 2 Dominant strategy

<img src="./img/DominantStrategy.png">
<img src="./img/Strong&WeakDominations.png">

To reduce the size of the matrix, it is possible to remove columns and row when they are dominated by at least another column or row respectively.

Say you have: <img src="./img/ReduceableMatrix.png">

**R** is always a **dominated strategy**, so you can get rid of it.
As we have removed a column, we should now look at the rows (again if have already done it).
Nothing can be removed, so this is it.


###### video 3 Nesh Equilibrium

## Nesh Equilibrium (NE)

In Game Theory, it's called **Nash Equilibrium** a state in which, for each agent, if **ONLY** that agent makes a move, there's no improvement in the score.

> In general, we will say that two strategies **s1** and **s2** are in **Nash equilibrium (NE)** if:
> 1. under the assumption that agent $i$ plays $s1$, agent $j$ can do no better than play $s2$; and
> 2. under the assumption that agent $j$ plays $s2$, agent $i$ can do no better than play $s1$.


Not every interaction scenario has a pure strategy NE.
Some interaction scenarios **have more than one NE**.
The optimal pair of strategies might be as well in the NE.
<img src="./img/NE.png">

<div class="warning">When looking for a NE remember that, if you want to check whether a cell is a NE:
<ul>
<li><b>for the column player you can only move LEFT or RIGTH</b></li> vice versa <li><b>for the row player you can only move UP and DOWN</li></b>
</ul>
</div>

> Remember, in a NE, given one agent opts for a **pure strategy** (aka, its strategy is fixed), you have to look at the payoff of the other agent only. In the above example, say $i$ move is **C**, then $j$ can either play **D** or **C**, and the payoffs to look at are respectively **0** and **3** **ONLY**.

###### video 4 Pareto Optimality

## Pareto Optimality (or Efficiency)

A **Pareto Efficient** state is state in which no agent wants to move away from.
In other terms, you only move away from it if either 
- the payoff improves for both agents;
- one agents ends up having the same payoff, but the other one improves it (the agent not improving has to allow it tho)

> Differently from the Nash Equilibrium, the pareto efficiency allows both agents to make a move. In the previous table, **(C, C)** is not pareto optimal because if both agents move to **(D, D)**, $i$ payoff doesn't get worse whereas $j$'s one does.

## Social Welfare

Conversely to the Pareto Efficiency, **Social Welfare** aims to maximise the total payoff of both agent, regardless with the score of each individual agent. So a (9, 0) is preferable to a (4, 4)

###### video 4 Pareto Optimality

## Coordination Game

In a coordination game, given 2 agents $i$ and $j$,
> $u_i(a) = u_j(a)$ for all $a \in A_i$ X $A_j$. 

In other words, both agents have the same payoff for each combination of moves, but when the two agents both take the same action (A, A) or (B, B), **payoff $>$ 0**, whereas different moves like (A, B) or (B, A) have a **zero** payoff.

The opposite of this game is the misanthropes (un)coordination game wherein the reward is bigger than zero when the two agent take opposite moves.

## Constant Sum Games
In a constant sum game, the sum of the payoff is the same for each move
> $u_i(a) + u_j(a) = c$ for all $a \in A_i$ X $A_j$.

An example is the tossing a coin game, where you either win (+1) or lose (0), and the sum is always constant (1)

### Zero Game

This is a special type of constant game where the sum is always **0**
>$u_i(a) + u_j(a) = 0$ for all $a \in A_i$ X $A_j$.

The toss a coin game where the payoff is $\pm 1$ would result in a sum payoff of 0 all the times. Another example is rock, paper, scissor

# Week 6 
## PCA (video 1)
**PCA** (or **Principal Component Analysis**) is ***dimensionality reduction*** technique. **SVD** (or **Simple Value Decomposition**) share the same idea and you can often interchange them, however, SVD is preferred.

What you do in PCA is you want to reduce the number of dimensions so that you can use clustering to make easier to analyse and plot the data. The steps are:
- take 2 or 3 dimensions;
- (plot them if you want a graphical representation);
- find a regression function with the **highest variance** (the more spread are the reflections of the X on the line, the better); and
- use that regression as a new, single dimension.

Say you start with 5 dimensions, you can group them into 2 PCAs (PCA_1 and PCA_2) with 3 and 2 features and make a new graph.
The PCA represented on X axis is more important than the one on the Y axis, as such, when a cluster A is equally distant from 2 clusters B and C, the further away in the X axis is the more different.

<div class="info">
    When he operates the LSD (least square distance), the distance from the regression line is actually the minimum distance from the point to the line rather than the distance which is parallel to the Y-axis. 
    He is using the <b>perpendicular offset</b> rather than the <b>vertical offeset</b>
    <img src="./img/PCA_LSD.png">
</div>



**(video 2)**
When you have 3 dimensions, ideally you want to reduce them to 1 eventually to be able to plot them in the PCA graph, however, you can go from a 3D to a 2D plot and that is still fine, but you have to remember that your PCA graph will end up with 1 more dimension.

Generally, if you have a 3D plan of **x1, x2, x3** and you create a 2D plan out of it, the hyperplane you have just created has **z1** and **z2** as axis names

## Matrix multiplication (video 3)
In a matrix $m \times n$ like the following one a common mistake may be to consider the cols as the X-axis and the rows as the Y-axis, but to refer to a cell it is actually the opposite. 
As you can see by looking at the names, the position of $a_{32}$ uses the **row as the first index** (row 3) and the **column as the second index** (col 2)
<img src="./img/PCA_matrix.png">
Even the dimensions are indicated as **$rows \times cols$** that is **$(m \times n)$**

**How do you multiply 2 matrices**

When you multiply matrices the order matters, so the commutative property does not hold.
Say you have 2 matrices $M_1$ and $M_2$, then $M_1 \times M_2 \ne M_2 \times M_1$.
In a 2 matrices multiplication, say $M_1 \times M_2$, the resulting matrix $M_3$ will have:
- the number of columns of $M_1$ and
- the number of rows of $M_2$;

> e.g. $(M \times K) \cdot (K \times N) = (M \times N)$

<div class="warning">
    The <b>K</b> dimension from the previous example has to be the same in both matrices, otherwise the operation cannot performed.
</div>

> Look at this matrix multiplication 
<img src="./img/scalar_mul.png">
The first matrix is a <b>5 x 1</b> (5 rows and 1 col) whereas the second is <b>1 x 4</b> (1 row and 4 cols).
For what said before, the resulting matrix will have 5 rows and 4 cols, so it will be a <b>5 x 4</b> matrix.

Having said that, the way you calculate the value for each cell should be pretty intuitive:
<img src="./img/Matrix_Multiplication.png">

**Transposition**: it means you flip the matrix along the main axis, aka you invert the indices, so $a_{ij}$ becomes $a_{ji}$.


## Matrix transformation
Let's say we have a matrix $\begin{pmatrix}
x\\
y
\end{pmatrix}$ which represents a **2D image**.

Using Matrix multiplication, you can change the aspect of this image in many ways:

**Image Stretching**
<img src="./img/matrix_stretching.png">

**Image Rotation**
<img src="./img/matrix_rotation.png">

**Image Skewing (Shear mapping)**
<img src="./img/matrix_skewing.png">

## Eigenvector and Eigenvalue
If you look closely at the third image transformation you will notice that the **X vector** (the green arrow) did not change at all.

When a vector doesn't change its direction after a multiplication with a matrix, then it's an **eigenvector**.

Contrary, the white vector did the change its direction, so it is not an *eigenvector*.

In the first transformation, both the vectors are **eigenvectors** as they keep their direction, however, their length does change and that changing factor is called **eigenvalue**$\lambda$.

### Eigenvector formula
A vector **v** is an **eigenvector** of the matrix **M** if
> $M \times v = λv$.
> 
$λ$ is the corresponding eigenvalue.

So multiplying **M** by **v** would result in **v times an eigenvalue**.

> e.g. <img src="./img/eigen_example.png">

## Calculating PCA using SVD

1. Start with the matrix $\textbf X$ you are interested in **reducing the dimensionality** of;
   > $\textbf X$ dimensions are $n \times d$
2. For each feature (**so actually the columns**) calculate the **mean** $\overline{\textbf x}$ (**mean row vector**);
3. Using matrix multiplication, multiple $\overline{\textbf x}^T$ by a matrix full of **ones** to obtain a matrix of the same dimensions as $\textbf X$. We will call this matrix $\overline{\textbf X}$ (**mean row matrix**).
   > $\overline{\textbf X}$ dimensions are $n \times d$ (1 row for each entry and 1 col for each feature, or col, in $\textbf X$). The result should be something like:
   > $\begin{pmatrix}
        1 & 5 & 12 & 3,5\\
        1 & 5 & 12 & 3,5\\
        & & ... & \\
        1 & 5 & 12 & 3,5
        \end{pmatrix}$
    
4. Given you have the mean of each row, you can **shift an hypothetical graph** so that its mean is the origin of the plan. The way you do it is by subtracting the mean to each elements $\textbf B = X - \overline{X}$.
   > **Note**: we shift the values, but the distance from each point remains the same.
   
   > $\textbf B$ dimensions are $n \times d$
5. Given $B$ we want to calculate the **covariance matrix $\textbf C$** we just multiply the values of $B$ by themselves as $\textbf C = B^TB$;
   > $ \textbf C$ dimensions are $(n \times d)^T \times (n \times d) = (d \times n) \times (n \times d) = d \times d$
6. (Using a software) Compute the $k$ largest eigenvector $\textbf{v}_1, \textbf{v}_2, ... , \textbf{v}_k$ of $\textbf{C}$. 
   > Each eigenvector has dimension $1 \times d$.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>