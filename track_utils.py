import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Fxn
def create_page_visited_table():
	c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename,timeOfvisit):
	c.execute('INSERT INTO pageTrackTable(pagename,timeOfvisit) VALUES(?,?)',(pagename,timeOfvisit))
	conn.commit()

def view_all_page_visited_details():
	c.execute('SELECT * FROM pageTrackTable')
	data = c.fetchall()
	return data


# Fxn To Track Input & Prediction
def create_emotionclf_table():
	c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(raw_text TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')

def add_prediction_details(raw_text,prediction,probability,timeOfvisit):
	c.execute('INSERT INTO emotionclfTable(raw_text,prediction,probability,timeOfvisit) VALUES(?,?,?,?)',(raw_text,prediction,probability,timeOfvisit))
	conn.commit()

def view_all_prediction_details():
	c.execute('SELECT * FROM emotionclfTable')
	data = c.fetchall()
	return data