import unirest
import time

def songs(artist):
	"""https://market.mashape.com/deezerdevs/deezer-1"""
	artist = artist.replace(" ", "+")
	response = unirest.get("https://deezerdevs-deezer.p.mashape.com/search",
	  headers={
	    "X-Mashape-Key": "DgoyXd9bunmshI9yT2CZbaGMDhTPp1x6YvIjsnmUnx2XbEtDw4",
	    "Accept": "text/plain"
	  },
	  params = {"q":artist}
	)
	d = response.body
	songs = []
	for i in range(len(d['data'])):
		songs.append(d['data'][i]['title'])
	return songs

def artist_info(artist):
	"""https://www.mediawiki.org/w/api.php"""
	response = unirest.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + artist)
	f = open("D:\\Cloud.txt", 'w')
	try:
		pages = response.body['query']['pages'].keys()[0]
		for item in response.body['query']['pages'][pages]['extract']:
			f.write(item)
	except: 
		pass		
	f.close()

def get_emotions(d, line):
	"""http://www.alchemyapi.com/api/text-api-0"""
	response = unirest.get("http://gateway-a.watsonplatform.net/calls/text/TextGetEmotion?apikey=2b1df6cec16bba04eac124c83db20bc6622072f6",
				params = {
					"text":line,
				  	"outputMode":"json"})
	if 'docEmotions' in response.body:
		for item in response.body['docEmotions']:
			if not item in d:
				d[item] = response.body['docEmotions'][item]
			else:
				s = float(d.get(item)) + float(response.body['docEmotions'][item])
				d.update({item:s})
		print line
		time.sleep(2)
	return d


def get_lyrics(artist):
	"""https://market.mashape.com/musixmatch-com/musixmatch"""
	song_list = songs(artist)
	print song_
	list
	artist_info(artist)
	for song in song_list:
		d = {}
		song = song.replace(" ", "+")
		response = unirest.get("https://musixmatchcom-musixmatch.p.mashape.com/wsr/1.1/matcher.lyrics.get?",
		  headers={
		    "X-Mashape-Key": "DgoyXd9bunmshI9yT2CZbaGMDhTPp1x6YvIjsnmUnx2XbEtDw4",
		    "Accept": "application/json"
		  },
		  params = {
		  	"q_artist":artist,
		  	"q_track": song
		  }
		)
		song = song.replace("+", " ")
		print "			***"
		print song
		print "			***" 
		text = response.body['lyrics_body']
		if len(text) == 0:

			print "			No lyrics found"
		else:
			lines = text.split("\n")
			for line in lines:
				if len(line) > 1:
					d = get_emotions(d, line)
			for item in d:
				print item, d[item]


get_lyrics("AC/DC")
