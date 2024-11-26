# INFO-B210

## **variablesAndoperators.py**
  #### In this file, I was tasked with making a code that will identify how many of the columns in my dataset, contain string values.
    

## **conditionalExecution.py**
  #### The purpose of this purpose is to count the most common day for the shows to be scheduled.;
  ######  * This program will take in the data from the csv and read it. 
  ######  * To use this program, the user will need to download the csv file and the code file. The user will need to make sure that csv file and the code file are in the same folder. 

## **repeatedExecution**
  #### The purpose of this is to find which TV show has the most number of seasons and which show has the most number of episodes?

  
## **BuiltInFunction.py**
  #### The purpose of this is to ask the user for a network and then prints the titles of all the shows that are available on that network from this list.
  ######  * This will take that input and go through each individual row to see what show is with the inputed network
  ######  * Use the Tv_Show.csv as the CSV file

## **UserDefinedFunction.py**
  #### The purpose is to ask the user for a genre and print out most common Schedule(time) based upon genre inputed.
  ######  * Use the Tv_Show.csv as the CSV file
  ######  * This is suppose to take the csv file and read the data. Then it will know that column 6 is where the genre data is located, and column 12 is where the schedule(time) data is located. It will go throw those columns and put the genres into a dictionary, while keeping track of the schedule(times) to see which one was used the most for that said genre. This should print out all the genres with the corresponding common time. I know that is not what will get displayed. In the dataset, the summary column has an abundance amount of commas, so when the data is being split by the commas, it will include those commas as well ruining the columns. 

## **ObjectOrientedProgramming.py**
  #### The purpose of this program is to Create a show class, complete with initialization function.
  ###### * Use the Tv_Show.csv as the CSV file
  ###### * This will take the define a class, show, the initize the attribute of the show objects for the csv file. Then the code will open the CSV and read the file. It will identify the headers and then store the data into a list called data. Then the show object is created where the corresponding data is paired with the corresponding object. In this, I just ended up calling the Show Name, Genre, Rating, and Show time. So when this is ran, it will display this of all the shows.

## **ListAssignment.py** 
  #### The purpose of this program is to write of function that makes a list of TV show names that ended prior to a given date. This will import the new data into a CSV file. 
  ##### * Use the Tv_Show.csv as the CSV file
  ##### * This will be one big user define. Within this one there are a couple of nested user defined functions. At the start, the date that given will be converted in to an integer, this will allow it to be compared to the other dates, as you cannot compare strings. Then there is a function that takes the dates from the dataset and converts them into a integer. Then it will compare the given date to the dataset dates.Then it will take the dates that ended prior to the given date into a new CSV file. 

## **TupleNSets.py**
  #### The purpose of this program is to write a function that orders TV show names based on their run time (based on length of time between Premiere Date and End Date) and as a set to a new CSV file.
  #####  * Use the Tv_Show.csv as the CSV file
  #####  * This will calulate the runtime of each tv show in the days given for it premiere and end dates. NOTE.. in this dataset, the premiere and end dates column labels are switched. So, to counter this, I have switched them in my code. When indexing the premiere date, i have set the code to index for 'End Date' and vise versa. The CSV will be ran and the times will be calculated and out into a set. Then that set will be put into a new CSV file.

## **Dictionaries.py**
  #### Write a function that alphabetically sorts the names of the TV shows and then creates ordered sets with the name of the show, genres, language, and rating, and writes to a new CSV file. 
  #####  * Use the Tv_Show.csv as the CSV file
  #####  * This will create one big user defined function that will read the csv file and write a new CSV file with the shows in alphabetical order. Inside this function, the lines will be parsed from the CSV. Then the data will be extracted into a dictionary called tv_show. This will be then sorted in order by tv show name. Then the new CSV file will be created with the data and in alphabetical order. 
