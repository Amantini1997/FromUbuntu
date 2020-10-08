[TOC]

<style>
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

.definition {
    background: rgba(80, 80, 255, .3); 
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

# WEEK 1 (Refresh of searching algorithms)


<div class="definition"><b>Closed World Assumption :</b> Any fact not listed as explicitly being true in the initial state can safely be assumed as false.</div>

In PLANNING 3 are the **pillars** to solve a problem:
 - The initial state (what is True at the beginning);
 - The goal (what has to be True at the end to consider the problem solved);
 - The executable actions define according to the DOMAIN

**Lifted Action:** when the :action contains :parameters

**PLANNER:** takes in an initial state and creates a plan to reach the goal state. It can be seen as an ordered list of actions
           telling what to do and when in order to reach the goal. To do this, it creates many plans and find the first or the
           most effective one.

---

## Searching Methods

When looking for the optimal plan, you can use different methods to find it:
 - **Depth First Search** (not very used as the path to the goal tends to be longer);
 - **Breadth First Search** (better than DFS, but not the best yet);
 - **Best First Search** which:
    - assigns a heuristic value h(S) to each new node;
    - puts all the not visited nodes into a sorted queue, sorted by the h(S) (in case two nodes have the same h(S), https://www.amazon.co.uk/contact-us
        the first one generated has higher priority);
    - removes the first node in queue and visits it.
 - **A\*** which is like Best First Search, but takes into account the distance g(S) from the star<b>WARNING</b> ting node as well (f(S) = h(S) + g(S)).

Of course, you choose between BestFS and A* based on what is most convenient for you: 
- A* -> shorter distance from the initial state (so optimal path) is guaranteed;
- BestFS -> less computations, but MIGHT result in a longer path g(S);

> ### Heuristic Cryteria 
><div class="no-mt">A good heuristic value should be:</div>
>
>- **ADMISSIBLE:** never overestimates the distance to a goal state;
>- **CONSISTENT** (Monotonic): at every state, the heuristic value must be less than or equal to the distance from that state to another state + the heuristic value of the other state     h(S) <= h(S') + d(S, S');
>- **ADDITIVE:** (not necessary, but good for heuristic) given 2 heuristic functions h1 & h2, their sum is **admissible** for each state s (i.e. h(s) = h1(s) + h2(s) ).

A* is very good, but also "expensive", a good trade off comes with WA* (Weighted A* Search), which finds a solution 
more quickly than the A*, but not necessarily the optimal solution. I lays between A* and BestFS:
- f(S) = g(S) + W*h(S)
- when W is 2, the h(S) counts twice as much as it did before, making it more relevant than g(S)
- when W tends to Inf., WA* behaves like A*
- the W is the factor than influence the worst possible solution, i.e., if W = 2, the worst solution
    we can (not necessarily the one we will) find, is at most twice as much the best solution


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
# WEEK 2

**Delete Relaxation:** Finding the a good heuristic can be tricky sometimes, **RPG** (or Relaxed Planning Graph) is very handy for that. It assumes that the actions only add and never delete predicates; in other words, **delete relaxations remove only the delete effects of actions**.


> i.e. an action that moves a box and outputs (on A B) (not (on A C)) would in fact only add (on A B), without deleting the other consequence. So doing, you create, step by step, the RPG, and going backward you create a possible solution. when you have al the table of facts, basically you look at the predicates, if it didn't exist in the previous state, you look at the action that generates it, and you consider it for the heuristic function

## EHC (Enforced Hill Climbing)
RPG only provides heuristic scores, it's not a search method itself. However, EHC uses it to find the optimal solution. The way EHC works is pretty simple:
1. look at h(s) of the generated states;
2. from s, find the state s' with the best h(s') which has to be better than h(s)(h of the parent node) and expand it;
3. keep doing it until no acceptable state can be found (this situation is called **tableau**);
4. use **Breadth First Search** on all the child states (even the ones with the worst heuristic) until a state that meets the criteria from rule **2** is found;

If HEC reaches a dead end, FF resorts and uses Best First Search to look for a plan.

**EHC** can find solutions pretty fast, but it is **incomplete**, that is, it is not guaranteed to find a solution.

**FF** on the other hand, is slower, but **complete**. It can be made more efficient by using the RPG and **pruning** some states; in particular, an action that leads to a goal in the first state is called **helpful**. In spite of making the algorithm faster, it also makes FF less complete.

In case EHC fails, and (as far as I got from the lecture) so did FF due to pruning, we can try one more time using the **helpful actions constraints**, and see if it can find a solution before rolling back to FF.

<div class="warning"> the operator counting heuristic (<b>counting the number of actions used to reach the goal) isn't always admissible</b> (but that's not to say it's never admissible), <b>but the layer counting heuristic always is admissible</b></div>

>The **execution order** is then the following:
    1. **EHC with helpful actions**
    2. **EHC**
    3. **FF with helpful actions**
    4. **FF**

## Landmarks: Constraints-based heuristic
An alternative to using RPG is to set constraints that encapsulate facets of every possible solution of a problem.

Some of these constraints can be denoted as **landmarks** of the solution. 
- Landmarks **must be true** at some point in every plan generated. 
- They can include both facts and actions that will appear at some point.
- Landmarks can be **ordered** to dictate the order in which they should be achieved

<br>

## Types of landmarks

- #### Fact Landmark:
    <div style="margin-top: -16px">A variable takes a particular value in at least one state.</div>
- #### Action Landmark:
    <div style="margin-top: -16px">An action must be applied in the solution.</div>
- #### Disjunction Action Landmarks:
    <div style="margin-top: -16px">One of a set of possible actions must be applied.</div>

>**PROBLEM:** Finding landmarks, however, can be demonstrated to be as hard a the problem itself, aka, **PSPACE complex**.


<br>

## Finding Landmarks
<div class="no-mt">There are many ways to do it:</div>

### Deletion relaxation with RPG
- Iterate through all the actions and remove one that adds a fact;
- Build the RPG;
- If the goal no longer appears in the RPG, then that action is a landmark.
>**PROBLEM:** Applying this process for all the possible actions is pretty slow.

<br>

### Backchaining
- Consider every goal(B) *[in the goal state, I guess]* as a landmark:
- Look at the actions required to achieve B and the preconditions needed;
- If many actions needed to achieve B require A, than A can be considered as a landmark itself;
- Also, we know that A has to be achieved before B, this gives us a hint about the order

This approach can be improved by checking whether is needed to achieve B for the first time .

<br>

### RPG propagation
Not sure how it works...

---
<br>

## Landmarks ordering
<div style="margin-top: -16px">Having landmarks is definitely useful, but if we know in which order they should appear, this can be of much help.</div>

### Sound Ordering

<div style="margin-top: -16px; margin-bottom: 16px;"> We know that A achieves be, but we don't know when exactly.</div>

- **Necessary Ordering** A →<sub>n</sub> B : A is always TRUE one step before B becomes TRUE;
- **Greedy Necessary Ordering** A →<sub>gn</sub> B : A is TRUE one step before B becomes TRUE for the first time, rather than every time;
- **Natural Ordering** A → B : A is TRUE some time before B becomes TRUE;

>***[My Guess]*** Both in Necessary and Greedy-Necessary Ordering A is a precondition for the action that achieves B. In Natural ordering A is used to achieve intermediate state that in turns are preconditions for actions that achieve B; hence, A is not required by the action the directly achieves B, but to reach its preconditions I need to achieve A at some point.

### Unsound Orderings
<div style="margin-top: -16px; margin-bottom: 16px;"> There are a special conditions on the ordering of landmarks.</div>

- **Reasonable Ordering** A →<sub>r</sub> B : If B was achieved before A, then the plan should **delete B** and re-achieve it after (or at the same time as A);

>There are cases in which achieving B before A is a waste of time as one has to delete B, re-achieve A, and then again achieve B. However, there are cases, like the *Hanoi Tower*, where achieving,deleting, and eventually re-achieve B is necessary before reaching A.

- **Obedient Reasonable Ordering** A →<sub>or</sub> B : If B was achieved before A, then the plan should **delete B** and re-achieve it after achieving A;

>e.g.: I need to deliver a parcel to a location. If B = *reaching the location*, and A = *collecting the parcel*, it makes no sense to achieve B before A.





- We say that there is a reasonable ordering between A and B, written A →r B, if for every plan π where B is added at time i and A is first added at time j with i < j [*A is added after B*], 
it holds that B is not true at some time m with m ∈ {i + 1, . . . , j} and B is true at some time k with j ≤ k.true at any time j ≤ i.
---
- We say that there is an obedient-reasonable ordering between A and B with regard to a set of orderings O, written A → <sub>or</sub> B, if for every plan π obeying O where B is added at time i and A is first added at time j with i < j, 
it holds that B is not true at some time m with m ∈ {i + 1, . . . , j} and B is true at some time k with j ≤ k.


---

- We say that a plan π obeys a set of orderings O, if for all orderings A →x B ∈ O, regardless of their type, it holds that A is first added at time i in π and B is not 
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

<span style="color: black; font-size: 1.3em; font-weight: bold">