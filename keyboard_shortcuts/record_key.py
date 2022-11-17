import pynput.keyboard as KEY

escape_character = KEY.Key.esc
log_file_name = "log.txt"
ended_logging = False

def get_controller():
    return KEY.Controller()

def get_listener():
    return KEY.Listener(on_press=on_press, on_release=on_release)

def process_special_keys(sp_key):
    if sp_key == "Key.space":
        return " "
    elif sp_key == "Key.enter":
        return "\n"
    elif sp_key == "Key.backspace":
        return "\b"
    else:
        return None

def on_press(key):
    try:
        pressed = str(key.char)
    except AttributeError:
        pressed = process_special_keys(str(key))
        if pressed is None:
            return
    with open(log_file_name, "r", encoding="utf-8") as f:
        content = f.read().split("\n")
    content.insert(0, pressed)
    while len(content) > 15:
        del content[-1]
    with open(log_file_name, "w") as f:
        f.write("")
    with open(log_file_name, "a", encoding="utf-8") as f:
        f.writelines("\n".join(content))
        
def on_release(key):
    global ended_logging
    if key == escape_character:
        print("End Logging!")
        ended_logging = True
        return False
