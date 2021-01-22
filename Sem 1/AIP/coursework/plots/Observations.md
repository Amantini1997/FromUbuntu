# FreeCell

With cg plans tend to be shorter but the states expanded (and inevitably also the evaluated) are way more:

<img src="freecell_8.png">
<img src="freecell_9.png">

This leads to longer time spent searching:

<img src="freecell_10.png">


# Blocks World

Same as for FreeCell, but notice the elbow that is made when x = search_time:

<img src="blocks20.png">

This happens in all the plots having search time on the X axis, indicating that at some point, the search time increases way more than anything else.

I assume that getting this problem longer would lead to a point where the time is spent mostly on searching.

Both the heuristics seem to be affected, but the cg is still way more expensive

One thing to notice is that the total time spent is mostly just searching time.

<img src="blocks_10.png">
<img src="blocks_11.png">


The plan cost is definitely higher in h_add but the search is less expensive.

<img src="blocks_13.png">
<img src="blocks_15.png">

This can be become an issue if there is a time constraint on the search as the difference becomes huge on larger problem:

<img src="blocks_19.png">




# Depot 

In this case, once again, cg is more complete, but the number of states expanded is not as bad as for blocks world:

<img src="depot_8.png">
<img src="depot_10.png">


# DriverLog

In the driver log, just like the Depot, h_cg finds cheaper solutions and it the search time is not that bigger:

<img src="driverlog_9.png">

Nonetheless, the states expanded are way more:
<img src="driverlog_18.png">


## About h$^{ADD}$
h<sup>add</sup> is notoriously inadmissible, but works pretty good in absence of local minima as it performs a sort of gradient descent.