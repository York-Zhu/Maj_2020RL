import sys
import json
import random

if __name__ == '__main__':

    hand = []
    inputRAW = sys.stdin.readline()
    inputJSON = json.loads(inputRAW)
    turnID = len(inputJSON['responses'])

    request = inputJSON['requests']
    response = inputJSON['responses']
    request.append(inputJSON['requests'][turnID])

    if turnID < 2:
        response.append('PASS')
    else:
        itmp, myPlayerID, quan = request[0].split(' ')
        itmp, myPlayerID, quan = int(itmp), int(myPlayerID), int(quan)

        hand = request[1].split(' ')[5:]

        for i in range(2, turnID):
            req = request[i].split(' ')
            if int(req[0]) == 2:
                hand.append(req[1])
                hand.remove(response[i].split(' ')[1])

        itmp = int(request[turnID][0])
        if itmp == 2:
            random.shuffle(hand)
            response.append('PLAY ' + hand.pop())
        else:
            response.append('PASS')

    outputJSON = json.dumps({'response': response[turnID]})
    sys.stdout.write(outputJSON)



