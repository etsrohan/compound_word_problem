Name: Rohan Srivastava
Applying for: Impledge Technologies
Program name: Word Composition Problem

Steps to execute code:
 1) Make sure all the files are in the same directory (word_composition_problem.py, Input_01.txt, Input_02.txt, ).
    If you have any other test (.txt) files you want to test make sure they are in the same directory as the word_composition_problem.py file.

 2) Use terminal to type 'python word_composition_problem.py' (I use the anaconda prompt) or how ever you execute the python file.
 
 3) The program will prompt you to select 1 (Input_01.txt), 2 (Input_02.txt) or "o" to enter your own file.txt name.
 
 4) Press enter to enter the names and the program should display the first and second longest words in the terminal and as an Output.txt file
    (If Output.txt doesn't exist in the directory it will create the same)

Overview of program:
 This program takes a .txt file with each word on a new line as input and loads that into a list which is then converted
into a set for lookup optimization (lookup on set is O(1) whereas on list is O(n)). Then for every word in the set of 'words'
it sends it to the split_n_check function. The split_n_check function first splits this word into a left and a right component.
This is based on the index of a for loop going from 1 to length of word. So for the word 'cat' it will split it into 'c' + 'at',
then 'ca' + 't'. It then checks if the left and right strings are both in the 'words' set, if so, then it is a compound word and
the function returns True. If not, it then checks if left is in 'words' and right is a compound word (recursively calling the 
split_n_check function on right), if so, then returns True, else it returns False. Finally, when the word is found to be a compound word the function
appends it to the 'answer' list. Then a .sort function is called to sort the list in decreasing order of length. This is where I found
that there might be multiple compound words with the same length. So, I just put them in a list of their own. The 'first' list and the
'second' list. I then send these lists and the time taken to execute the program to a function that outputs a formatted message to the terminal and a text
file called Output.txt.

Optimizations:
 The main logic of splitting the word into a left and right section was optimized using a dictionary containing key value pairs: keys were the strings of full words
that were deemed to be not compound and compound words we have visited before. The values were a boolean variable to indicate if we visited that word before
and if so, then its True, else, its False.

Complexity:
 Time:
  Here, n is the number of words in the input file and l is the average length of the words themselves and m is the number of root words of the compound word. The Time
complexity of this program comes from the split_n_check function. Since, the lookups for word in a set and dictionary are constant, O(1), the complexity comes from the iteration
along the set which is O(n) and the splitting and checking which is based on word length, l. Since we are iterating over l then recursively going into the same function with 
(l - index) length of 'right' word and so on the worst case complexity is O(n * l!). This is based on if the input contains all the letters of the alphabet on average it is 
O(n * l ^  (m-1)); the (m-1) is because there are one less splits for m root words. For the inputs given, since the max number of root words in any compound word is 4
the complexity comes out to be O(n * l^3).
 Space:
  The space complexity of this program is linear so its O(n). Even the memory dictionary follows a linear pattern as it will contain either compound words or root words. At
worst the list contains all compound words except one, hence, it will be (2n-1).