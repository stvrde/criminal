# criminal
topcoder https://community.topcoder.com/stat?c=problem_statement&pm=884


Problem Statement for Criminal


Problem Statement
    	You are working for the FBI and are trying to locate a particular criminal organization. Within the organization you know which members communicate with each other. The problem is that the members may go by aliases. Given both the information in the database about the organization, and the field data about a suspicious organization, you will determine whether they represent the same group. The two sets of data represent the same group if and only if they only differ by the names of the participants.
For example:
Database               Field Data 
FRANK ----- BOB        WILLARD ----- GEORGE
  |                       |
  |                       |
  |                       |
GEORGE                  GREG
The Database and Field Data represent the same organization even though the participants are using different names.
Renaming Scheme:
FRANK -> WILLARD           FRANK -> WILLARD         
BOB -> GEORGE       or     BOB -> GREG 
GEORGE -> GREG             GEORGE -> GEORGE
If the database data and the field data represent the same organization return how many of the members are going by aliases, otherwise return -1. If there is more than one naming scheme possible in mapping the database information to the field data, use the one that gives the greatest value for the number of aliases. So in the previous example we would use the first renaming scheme thus giving 3 instead of 2.



The database data will be given in a String[] database. Each element of database will be in the form "NAME1 NAME2" meaning that NAME1 and NAME2 communicate with each other. The field data will be given in a String[] fieldData that is formatted in the same way as database. In the above example, the input could have been formatted as:
database = {"FRANK BOB","FRANK GEORGE"}
fieldData = {"WILLARD GREG","GEORGE WILLARD"}
In any particular organization, no two people will have the same name or alias. In other words, no two different people in the database will have the same name in database. In addition, no two different people in the field data will have the same name in fieldData.
 
Definition
    	
Class:	Criminal
Method:	numPseudonyms
Parameters:	String[], String[]
Returns:	int
Method signature:	int numPseudonyms(String[] database, String[] fieldData)
(be sure your method is public)
    
 
Notes
-	Communication is symmetric. In other words, if FRANK and BOB communicate then BOB and FRANK communicate.
 
Constraints
-	database will contain between 1 and 28 elements inclusive
-	fieldData will contain between 1 and 28 elements inclusive
-	Each element of database will contain between 3 and 50 characters inclusive
-	Each element of fieldData will contain between 3 and 50 characters inclusive
-	Each element of database and fieldData will be of the form NAME1_NAME2

where '_' is a single space and NAME1 is different than NAME2

NAME1 and NAME2 will have at least 1 character, and will only contain uppercase letters ('A'-'Z')
-	Each element of database and fieldData will have NO leading or trailing whitespace
-	There will be between 2 and 8 unique names inclusive in database
-	There will be between 2 and 8 unique names inclusive in fieldData
-	database cannot contains any repeated elements. In other words, if database contains an element "A B", it cannot contain another element "A B" or "B A".
-	fieldData cannot contain any repeated elements. In other words, if fieldData contains an element "A B", it cannot contain another element "A B" or "B A".
 
Examples
0)	
    	
{"FRANK BOB","FRANK GEORGE"}
{"WILLARD GREG","GEORGE WILLARD"}
Returns: 3
The example from above.
1)	
    	
{"ADAM FRANK","BOB SUZY"}
{"BRETT GEORGE","BRETT TOM"}
Returns: -1
These can't both be describing the same organization. The fieldData contains 3 distinct people where as the database contains 4.
2)	
    	
{"HARRY LLOYD","GEORGE BILL"}
{"FRANK THOMAS","GEORGE WILL","WILL FRANK"}
Returns: -1
These can't both be describing the same organization. The number of pairs of communicating members differs.
3)	
    	
{"A B","A C","AA BB","AA CC","AA DD"}
{"A B","A C","AA BB","AA CC","AA DD"}
Returns: 5
4)	
    	
{"A B"}
{"A B"}
Returns: 2
5)	
    	
{"STEVE BRETT", "STEVE LARS", "STEVE JAMES"}
{"SCHVEIGUY ADMINBRETT", "ADMINBRETT LBACKSTROM", "LBACKSTROM STEVEVAI"}
Returns: -1
