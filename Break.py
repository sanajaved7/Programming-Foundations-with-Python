#This class will allow us prompt the user to take exercise breaks throughout the work day
class Exercise():
    
    def __init__(self, url, time_counter):
        self.url = url
        self.time_counter = time_counter
        
    def how_long_to_wait(self):
        import time
        time.sleep(self.time_counter)
        
    def open_break(self):
        import webbrowser
        webbrowser.open(self.url)
