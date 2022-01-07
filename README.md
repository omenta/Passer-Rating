# Passer-Rating
A method to calculate the NFL football passer rating.
-----------------------------------------------------

Passer Rating (also known as Quarterback Rating) is 
a measure of the performance of passers, 
primarily quarterbacks, in gridiron football.

This method is a simple implementation of the formula
used to calculate the Passer Rating. 

A few things to note: 

    * Passer rating scale is 0 - 153.5 
      (negative ratings are adjusted to 0, 
      and anything over 153.5 is adjusted to 153.5)

    * The NFL passer rating formula includes five variables: 
        - pass attempts, 
        - completions, 
        - passing yards, 
        - touchdown passes, and 
        - interceptions. 
      Each of those variables is scaled to a value 
      between 0 and 2.375, with 1.0 being statistically 
      average (based on current league data.
