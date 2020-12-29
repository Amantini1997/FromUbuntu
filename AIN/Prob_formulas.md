[TOC]

<style>
    img {
        border: solid 2px black;
        border-radius: 10px;
    }
</style>

### PRIOR Probability
    P(h)

### POSTERIOR Probability or CONDITIONAL Probability
<img src="img/conditional_probability.png">

viceversa
##### PRODUCT RULE
<img src="img/product_rule.png">


### CHAIN RULE
<img src="img/ChainRule.png">

Also

$P(h_1,h_2 | e) = P(h_1 | e)P(h_2|h_1,e)$

### Probability VECTOR
a = {sunny, windy, rainy}
[NOTE the **BOLD** notation which means it is a vector]
**P(a)** = <P(a = sunny), P(a = windy), P(a = rainy)>

> same as 
> <img src="img/prob_notation_vector.png" width="230px"> 

### JOINT Probabilities
When there is an **AND**, often denoted by a "**,**".
<img src="img/joint_probabilities.png">

### HIDDEN Variable
When a variable is hidden, but part of the probability, you compute the probability for all its values.
<img src="img/hidden_variable.png">

In a Bayesian network where $m$ is the root, aka independent variable, and you want to calculate it given its children or descendant:

<img src="img/post_condition_tut3.png">
<br>

> In this case, you have to compute the formula for the combinations of $t$ and $c$, so $(t, c), (t, ¬c), (¬t, c), (¬t, ¬c)$ 