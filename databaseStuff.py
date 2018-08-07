import rethinkdb as r 


def createTables():
	r.connect( "localhost", 28015).repl()
	allTables = r.db('test').table_list().run()
	if not "wiki_text" in allTables:
		r.db("test").table_create("wiki_text").run()
	if not "wiki_links" in allTables:
		r.db("test").table_create("wiki_links").run()

def insert(data, tableName):
	r.db("test").table(tableName).insert(data).run()
	cursor = r.db("test").table(tableName).run()
	print(cursor)

def readTable(tableName):
	r.connect( "localhost", 28015).repl()
	cursor = r.db("test").table(tableName).run()
	return cursor