# Wikipedia Crawler

this crawler starts from the homepage and crawls all the links, saving the result in a rethinkdb database it then counts the number of word repeats. 

### How to run:
```bash 
python main.py --db 
python main.py --website
```

--db uses the database to count the number of repeats and --website first crawls and writes to the database and calculates the word count. 