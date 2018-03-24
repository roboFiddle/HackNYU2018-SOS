from flask import Flask, request, jsonify
import flask_sqlalchemy

app = Flask(__name__)


@app.route('schema.sql', methods = ['GET'])
def api_poll():
    if request.method == "GET":
        # query the db and return all the polls as json
        all_polls = {}

        # get all the topics in the database
        #topics = Topics.query.all()
        for topic in topics:
            # for each topic get the all options that are associated with it
            all_polls[topic.title] = {'options': [poll.option.name for poll in Polls.query.filter_by(topic=topic)]}
        return jsonify(all_polls)

if __name__ == '__main__':
    app.run()