#This class will allow us prompt the user to take exercise breaks throughout the work day
class Exercise():
    import time
    import webbrowser
    def __init__(self, activity, url, time_counter):
        self.activity = activity
        self.url = url
        self.time_counter = time_counter
        
    def how_long_to_wait(self):
        time.sleep(self.time_counter)
        
    def open_break(self):
        webbrowser.open(self.url)
