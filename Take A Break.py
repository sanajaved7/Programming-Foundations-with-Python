import time
import webbrowser
breaks = 3
counts = 0
while (counts < breaks):
    time.sleep()
    webbrowser.open("https://www.youtube.com/watch?v=cCkIYkaLBGs")
    counts = counts + 1