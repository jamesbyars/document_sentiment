from flask import Flask
from flask import request
from textblob import TextBlob

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def main():
    return "James"


@app.route("/get_date_time")
def getDateTime():
    return "dt"


@app.route("/sentiment/v1/upload_file/<filename>")
def upload_file(filename):
    return filename


@app.route("/sentiment", methods=['POST'])
def sentiment():
    # print '----------------'
    # print 'Printing Request'
    # print request.data
    myJson = request.get_json()
    runit(request.data)
    # print 'Returning'
    # print '----------------'
    return request.data


def runit(content):
    content = ""
    with open('textblob.txt', 'r') as file_content:
       tmp = [line.decode('utf-8').strip() for line in file_content.readlines()]
       content = ''.join(tmp)

    wiki = TextBlob(content)

    def readBlobIntoList(blob):
        print "readBlobIntoList()"
        return blob.sentences

    def getSentenceSubjectivity(sentence):
        print "getSentenceSubjectivity()"
        return sentence.subjectivity

    def getSentencePolarity(sentence):
        print "getSentencePolarity()"
        return sentence.polarity

    ## Driver ##
    print "Starting:\n"
    sentenceList = readBlobIntoList(wiki)

    print "Sentence count: " + str(len(sentenceList))

    polarity = []
    subjectivity = []

    subScore = 0
    polScore = 0

    for x in sentenceList:
        print x
        sub = getSentenceSubjectivity(x)
        print sub
        subjectivity.append(sub)
        subScore = subScore + sub
        pol = getSentencePolarity(x)
        print pol
        polarity.append(pol)
        polScore = polScore + pol
        print "----------------\n\n"

    print "\n\nFinal Subjectivity score: " + str(subScore)
    print "Final Polarity score: " + str(polScore)

    print "\nAverage Subjectivity score: " + str(subScore / len(sentenceList))
    print "Average Polarity score: " + str(polScore / len(sentenceList))
    print "----------------\n\n"

    print "Done."


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
