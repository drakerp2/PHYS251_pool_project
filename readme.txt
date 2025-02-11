Starting out, I went to take physical measurements to get a baseline to work with.
The results of these measurements can be seen in images/physical_measurements.jpg

I then started determining the formulas for the starting positions of the table.
These calculations were done on mathmatics1.jpg and mathmatics2.jpg, in conjunction
with checking against graphs in https://www.desmos.com/calculator/ju8wtzytd7

After this is set up the table.  I have the pool_table class in pool_table.py
and the pool_ball class in pool_bool.py.  There initial state can be graphed
by running driver.py.

I also did some online research to determine important other variables involved
in a pool simulation, from the materials, to the dimensions, and so on.  For 
this project I will use the formal table specification guidelines from the 
World Pool Association (WPA), the international governing body over the sport
of pool. (not to be confused World Confederation of Billiards Sports, an associat)
https://wpapool.com/wp-content/uploads/2024/01/RECOMMENDED-EQUIPMENT-SPECIFICATIONS.pdf

I also need the coeficients of friction.  While there is less of a standard for
this (and some tournaments will intentionally have tables with higher or lower
coeficients) I did find this source from Ohio state.
https://billiards.colostate.edu/faq/physics/physical-properties/
Will this is not a very official source, it serves as a starting off point and
narrows in the goal of the project:

How much do the margins for error permitted by the governing bodies of pool
effect how the balls play?

Hypothesis: while I think that none of the variables will make a significant
difference on there own, I believe that when combined together there will be a
noticible impact on the game.  

Process: to test this I will create a physics simulation for a pool table,
altering different constant variables relating to the table and comparing how a 
set of different shots play on different tables.
