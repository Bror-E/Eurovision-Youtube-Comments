
# Eurovision-Youtube-Comments
As I was scrolling through the youtube comments of a Eurovision song, it hit me that there are a superb number of comments that look like the following: 

> Tweleve points from Greece!

> Definetly the best one, love from Ukrain.

> UK love this! 

And so on, and so on. This led me to the the idea that maybe it would be possible to predict the public votes solely off of the frequency of country names in comments sections of the participanting countries youtube videoes. This idea led me to the build this project. 

## Predicting the public vote of Eurovision countries
1) Collect all the comments from a number of videoes from a number of countries on the Eurovision Youtube Channel.
    * Use the Youtube DATA API V3. 
2) Count the frequency of a country's name (or names) in another countries videoes
3) Compare the frequency of a country's name (or names) in all participating countries videoes. 
4) Convert frequency to points for the countries with a highest frequency. 
5) Do 2 -> 4 for all participating countries vidoes, looking for the frequencies of all the countries that are allowed to vote. 
6) Tally all the points. 
7) Declare a winner. 
