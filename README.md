# Hackerrank Questions


AngryAnimal:

There are n animals that need to be shipped to another location. Some of these animals are enemy to each other. So, they should not be kept within same cabin. Given number of animals and two set of pairs (in which second set are enemy of first set elementwise), we should determine number of groups of animals that can be formed.
There is a condition that each interval as the output e.g. (1,4) should contain first to last element e.g. 1,2,3,4

Example Input:

4 # number of animals
2 # number of elements in first array
1 # first element in first array
2 # second element in first array
2 # number of element in second array
3 # first element in second array
4 # second element in second array

We can form these groups of animals:
[(1, 2), (1,), (2,), (3,), (4,), (2, 3), (3, 4)]

Example Output: 7


Stock Open Close Price:

We need to make queries from following URL and retrive stock open and close prices between two input dates on the specified weekday.

URL: https://jsonmock.hackerrank.com/api/stocks
This URL has 5 pages and we can determine search key or page number to retrive data:
https://jsonmock.hackerrank.com/api/stocks/search?date=1-January-2000&page=2

The retrived json data has following fields:
"page"
"per_page"
"total"
"total_pages" 
"data":["date", "open", "high", "low", "close"]

Example Input:

1-January-2000
22-February-2000
Monday

Example Output:
17-January-2000 5617.7 5404.07
31-January-2000 5338.67 5205.29
7-February-2000 5431.55 5474.0
14-February-2000 6130.23 5924.31
21-February-2000 5874.25 5876.89


Non-Prime Generator:

Given a positive integer k, return first k positive non_prime integers by using generator function. 

Example Input: 10
Example Output:
1
4
6
8
9
10
12
14
15
16

Function with Reverse Arguments:

Given function with arguments, return output as the function result with reverse arguments. This code is tested with four functions.

Example input:
4 
pow 2 3
output:9
cmp 3 4
output:1
join_with you are here ,
output:here,are,you
capitalize_first_and_join first second third
output: THIRDsecondfirst

Rest of the question exist in HackeRank with the same name as the scipt. 



