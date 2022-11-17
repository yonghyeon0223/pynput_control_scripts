from record_key import get_controller

def read_log():
    with open("log.txt", "r", encoding = "utf-8") as f:
        content = f.read().split("\n")
        content = "".join(content)
        return content[::-1]
    
def get_keywords(config_f):
    matches = dict()
    with open(config_f, "r", encoding="utf-8") as f:
        match_pairs = f.read().split("\n")
        for mp in match_pairs:
            if not mp.count(":") == 1:
                continue
            key, val = mp.split(":")
            key = key.strip().strip('"')
            val = val.strip().strip('"')
            matches[key] = val
    return matches
            
def write_if_match(pairs, log):
    for p, val in pairs.items():
        if not log.endswith(p):
            continue
        with open("log.txt", "w") as f:
            f.write("")
        ctrl = get_controller()
        ctrl.type("\b" * len(p))
        ctrl.type(val)
        
        # coni- ∨ disj