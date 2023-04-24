from graphics import *
import pandas as pd

SECONDS_PER_DAY = 60*60*24

#Adjust to the range of time you want to visualize
startTime = "15:00"
endTime = "18:00"


def timeToSeconds(time):
    """Takes a string in HH:MM format and converts to seconds"""
    h, m = time.split(":")
    seconds = int(h) * 60 * 60 + int(m) * 60
    return seconds

def drawIntersection(win):

    for i in range(2):
        line = Line(Point(250 + i * 100, 50), Point(250 + i * 100, 200))
        line.draw(win)

        center = Rectangle(Point(295, 50 + i * 100), Point(305, 100 + i * 100))
        center.setFill("yellow")
        center.draw(win)

    for i in range(2):
        line = Line(Point(250 + i * 100, 300), Point(250 + i * 100, 450))
        line.draw(win)

        center = Rectangle(Point(295, 300 + i * 100), Point(305, 350 + i * 100))
        center.setFill("yellow")
        center.draw(win)

    for i in range(2):
        line = Line(Point(50, 200 + i * 100), Point(250, 200 + i * 100))
        line.draw(win)

        center = Rectangle(Point(50 + i * 100, 245), Point(100 + i * 100, 255))
        center.setFill("yellow")
        center.draw(win)

    for i in range(2):
        line = Line(Point(350, 200 + i * 100), Point(550, 200 + i * 100))
        line.draw(win)

        center = Rectangle(Point(370 + i * 100, 245), Point(420 + i * 100, 255))
        center.setFill("yellow")
        center.draw(win)

def main():

    df = pd.read_csv("output.csv")
    win = GraphWin("Intersection Simulator", 600, 500)
    drawIntersection(win)

    eastQ = []
    westQ = []
    northQ = []
    southQ = []

    for i in range(5):
        car = Circle(Point(270, 180 - i * 30), 10)
        car.setFill('blue')
        southQ.append(car)

        car = Circle(Point(330, 320 + i * 30), 10)
        car.setFill('blue')
        northQ.append(car)

        car = Circle(Point(230 - i * 30, 280), 10)
        car.setFill('blue')
        eastQ.append(car)

        car = Circle(Point(370 + i * 30, 220), 10)
        car.setFill('blue')
        westQ.append(car)


    carCount = {'N': 0 ,'S': 0, 'E': 0,'W': 0} #N, S, E, W
    timeMessage = Text(Point(100, 10), "Time: ")
    timeMessage.draw(win)
    start = timeToSeconds(startTime)
    end = timeToSeconds(endTime) + 1
    for currentTime in range(start, end):
        timeText = "Time: %2d:%02d:%02d" %(currentTime//(60*60), (currentTime//60)%60, currentTime %60)
        timeMessage.setText(timeText)
        new_cars = df.loc[df['Arrive'] == currentTime]

        length = len(new_cars)
        for i in range(length):
            carCount[new_cars.iloc[i]['Direction']] += 1


        depart_cars = df.loc[df['Depart'] == currentTime]

        length = len(depart_cars)
        for i in range(length):
            carCount[depart_cars.iloc[i]['Direction']] -= 1

        if carCount['N'] > 5:
            northQ[4].setFill("red")
        else:
            northQ[4].setFill('blue')

        if carCount['S'] > 5:
            southQ[4].setFill("red")
        else:
            southQ[4].setFill('blue')

        if carCount['E'] > 5:
            eastQ[4].setFill("red")
        else:
            eastQ[4].setFill('blue')

        if carCount['W'] > 5:
            westQ[4].setFill("red")
        else:
            westQ[4].setFill('blue')

        for i in range(5):


            if i < carCount['N']:
                try:
                    northQ[i].draw(win)
                except:
                    ""
            else:
                northQ[i].undraw()

            if i < carCount['S']:
                try:
                    southQ[i].draw(win)
                except:
                    ""
            else:
                southQ[i].undraw()

            if i < carCount['E']:
                try:
                    eastQ[i].draw(win)
                except:
                    ""
            else:
                eastQ[i].undraw()

            if i < carCount['W']:
                try:
                    westQ[i].draw(win)
                except:
                    ""
            else:
                westQ[i].undraw()

        #print(carCount)

    win.getMouse()

if __name__ == '__main__':
    main()
