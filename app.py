from flask import Flask,jsonify,request
import ipl
import jugaad

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to my home"
@app.route('/api/team_played')
def team_played(): # it gives the json data of all teams played in IPL
    team = ipl.teams_played()
    return jsonify(team)

@app.route('/api/teamvapi') # return the json data of two teams like matches played, won, lost between them 
def teamvapi():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    main = ipl.teamvteamApi(team1, team2) 
    return jsonify(main)

@app.route('/api/teaminfo')
def teaminfo():# returns the json data  of a team like matches played, won, lost, no result
    team = request.args.get('team') 
    response = jugaad.teamAPI(team)
    return response

@app.route('/api/allrecord')
def allrecord(): #returns the json data  of all records of a team like title, matches played 
    tema = request.args.get('team')
    response = jugaad.allRecord(tema)
    return jsonify(response)

@app.route('/api/batsmanrecord')
def batsman():
    batsman = request.args.get('batsman')
    response_batsman = jugaad.batsmanRecord(batsman, jugaad.batter_data)
    return response_batsman

    # aur bananan paadega jugaad file mein s

app.run(debug = True)