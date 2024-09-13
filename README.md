# MapReduce
MapReduce algorithm for min, max, count, and average for Kaggle data 

## Summary

### Mapper.py 
Mapper.py simply takes the input from the file years.txt line by line and passes the year on to reducer.py.

### Reducer.py 
Reducer.py first sets up the variables that I use to compare and store numbers during the reducing process. As it receives each year one at a time, it compares and assigns the min_year and then passes it on to the max_year variable. During that process, it also keeps track of a count to display at the end and sum so that at the end, we can also compute and display the average. 
