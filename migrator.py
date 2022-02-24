from postgres import Postgres
from sqlite import Sqlite

#create postgres instance for writing to 
postgres_db = Postgres()
sqlite = Sqlite("database.sqlite")

print(sqlite.read('league', ['id', 'name', 'country_id']))

data = {
    "country": ["id", "name"],
    "league": ["id", "country_id", "name"],
    "match": [
                "id",
                "country_id",
                "season",
                "stage",
                "date",
                "match_api_id",
                "home_team_api_id",
                "away_team_api_id",
                "home_team_goal",
                "away_team_goal",
            ],
    "team": [
        "id", 
        "team_api_id", 
        "team_fifa_api_id",
        "team_long_name",
        "team_short_name",
    ],

}
separator = "="*10
for table, columns  in zip(data.keys(), data.values()):
    print(f""" 
    {separator[:4]} {table} {separator[:4]}\n
    {sqlite.read(table, columns)}
    {separator}
    """)
