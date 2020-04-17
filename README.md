# Movies-EDA
Looking at a data set containing meta data on 45,000 movies.

The data set can be found at: https://www.kaggle.com/rounakbanik/the-movies-dataset  

I could not upload all the files directly due to some being too big. I have included some of the smaller csvs in the repository for a sample of what the data looks like though.


# EDA

## Relation between Budget and Revenue
![image](Charts/Rel_Budget_Rev.png)
Pretty interesting to see that theres almost somewhat of a linear trend with Budget and Revenue

## Genres with the largest Budgets
![image](Charts/GenreBudget.png)
I was surprised see that Drama was second. I not much of a drama movie kind of guy I guess. 

## Relationship between Budget and Runtime
![image](Charts/BudgetRuntime.png)
It's interesting that budget doesn't really seem to affect the runtime of a movie that much. I would've thought that it would since a longer movie means more editing etc.

## Relationship between Revenue and Runtime
![image](Charts/RevenueRuntime.png)
A few things to note from this scatter plot:
- There is a movie runtime sweet-spot 0 to ~200 minutes. Makes sense because no one wants to watch a 900 minute movie
- Each movie genre almost has a tight clustering of revenue and runtime. Family movies are a good example of this
- Drama movies tend to be longer, which is interesting 