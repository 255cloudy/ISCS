This is supposed to be an sqlite tool for editing Sqlite databases and possibly generating migrations 
for laravel(blueprint classes) and or django(models)

##revision 
project to take the data and put it into the postgres db

this is a small python project to migrate my sqlite data to postgres  

# plan

-get user to load a sqlite file
- show all the rows and columns they want to keep 
- select the columns 
-check the connections and make sure all is good 
- copy the data to a new database of their choosing(postgres)
- generate laravel blueprints 

# Postgres Backend [ ]

This is a class which will read the ini file and allow you to excecute the following operations:

- create
- read

## Create [x]
Given a tablename it should be able to add one or more records to the database
function specification:
**create**
params:
1. tablename: name of the table to insert []
2. column names: list of strings of columns
3. values: list of values to be insrted in respective columns

## Read [ ]
it will provide functions to:
- get by id
- get where certain colums equal some value. limit to a column for now


# Migration Plan [ ]

Get the data that i need from the sqlite database and copy it over to the postgres database

## Tables
Columns that i will keep from each table

1. Country
    - id
    - name

2. League
    - id
    - country_id
    - name
3. Match
    - id
    - country_id
    - season
    - stage
    - date
    - match_api_id
    - home_team_api_id
    - away_team_api_id
    - home_team_goal
    - away_team_goal

4. Team
    - id 
    - team_api_id
    - team_fifa_api_id
    - team_long_name
    - team_short_name

The data below will be used later but just migrate.
4. Player 
    - id
    - player_api_id
    - player_name
    - player_fifa_api_id
    - birthday
    - height
    - weight

5. Player_Attributes
    - id
    - player_fifa_api_id
    - player_api_id
    - overall_rating

# Sqlite

this class will provide read and write operations for sqlite database

## read
**read**
Parameters:
    1. tablename
    2. columns (list values for the columns to read)
Returns a tuple containing tuples with the values 

**read_multiple**
Parameters:
    1.Data - a dictionary whose keys are the tablenames
             the values are the list containing the columns to be read from the table
 

