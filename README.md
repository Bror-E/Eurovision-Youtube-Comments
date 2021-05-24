# Eurovision-Youtube-Comments

As I was scrolling through the youtube comments of a Eurovision song, it hit me that there are a superb number of comments that look like the following:

> Tweleve points from Greece!

> Definetly the best one, love from Ukrain.

> UK love this!

And so on, and so on. This led me to the the idea that maybe it would be possible to predict the public votes solely off of the frequency of country names in comments sections of the participanting countries youtube videoes. This idea led me to the build this project.

## Predicting the public vote of Eurovision countries

1. Collect all the comments from a number of videoes from a number of countries on the Eurovision Youtube Channel.
   - Use the Youtube DATA API V3.
2. Count the frequency of a country's name (or names) in another countries videoes
3. Compare the frequency of a country's name (or names) in all participating countries videoes.
4. Convert frequency to points for the countries with a highest frequency.
5. Do 2 -> 4 for all participating countries vidoes, looking for the frequencies of all the countries that are allowed to vote.
6. Tally all the points.
7. Declare a winner.

## Results

I cannot really say that the predictions here were really a success. There were some countries that were quite spot on, like Finland was predicted to get 220, but they got 218, but it aslo makes massive mistakes in that Italy was predicted to get 180, but they actually got 318. And Azerbaijan that was predicted to get 291, but only got 33. I am, for now, not gonna delve deep down into why this is the case. But I think I can conclude that the current algorithm, that attempts to predict the public vote of Eurovision based on the frequencies of country names in official youtubevideoes of the participating countries, was not functional, and did not predict very well at all.

## After thoughts:

- I should have written the entire data sets that were retrieved to files, instead of just collecting the comments. This would have made it possible to, for instance, to add weights (in the form of likes) to the comments that do have a countries names mentioned in it. Say for instance that there is only one comment mentioning Greece on the Norwegian video, but it has 200 liked. But on the Serbian video it is 4 comments mentioning Greece, but all with 10 likes. Maybe the one comment with 200 likes should have weighd more on the result then the number of comments.
