  Assignment 2 Map Reduce
 =========================
 
 ## How to run the code
 
The program can be run in terminal by entering the following **python3 ./map_reduce.py**. By default the parallel portion is run with 8 threads. In order to change the thread number you must manually change the number in line 63:

    with mp.Parallel(8) as p:
    
## Report

This assignment proved challenging in figuring out how to initialize a dictionary in a parallel segment. Finding which portion needed to be locked seemed aparent in this case, however, I did get alot of errors when the dictionary of words was both initialized and declared outside of the parallel segment. It was not until the dictionary was declared inside the parallel segment and initialized outside. I found that if the shared word dictionary was initialized inside of the parallel segment the list would contain 0's as the count of the words.

After testing the program with 1,2,4,8 threads, I found that as the program was given increased threads the execution time took longer.

- 1 threads : 0.5922 seconds
- 2 threads : 0.6212 seconds
- 4 threads : 0.7658 seconds
- 8 threads : 1.1340 seconds

>model name      : Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
      4         36         216
