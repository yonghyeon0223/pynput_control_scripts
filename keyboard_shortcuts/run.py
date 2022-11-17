import record_key as record
import match_key as match
import time
import sys

def run():
    listener = record.get_listener()
    listener.start()
    look_for = match.get_keywords("./config/" + sys.argv[1] + ".txt")
    
    while not record.ended_logging:
        current_log = match.read_log()
        match.write_if_match(look_for, current_log)
        time.sleep(1)
        
        
        

if __name__ == "__main__":
    run()
    

# dfjldkhelloworld