import pynput.keyboard as KEY
import time
from threading import Thread


class sign_writer:
    def on_press(self, key, special=KEY.Key):
        try:
            pressed = key.char
        except AttributeError:
            pressed = key
            if pressed == special.backspace:
                pressed = ""
                if len(self.log) > 0:
                    self.log.pop()
            elif pressed == special.space:
                pressed = " "
            elif pressed == special.enter:
                pressed = "\n"
            elif pressed == special.shift:
                return
            else:
                return
                # pressed = str(pressed)

        self.log.append(pressed)
        # print("".join(self.log))
        if len(self.log) > self.max_log:
            del self.log[0:self.clean_log_degree]

    def on_release(self, key):
        if key == self.end_key:
            # Stop listener
            return False

    def __init__(self, max_log=100, end_key=KEY.Key.esc, clean_log_degree=10):
        self.control = KEY.Controller()
        self.listener = KEY.Listener(on_press=self.on_press, on_release=self.on_release)

        self.log = []
        self.max_log = max_log
        self.clean_log_degree = clean_log_degree

        self.special_chr_matcher = []

        self.end_key = end_key

    def add_special_chr(self, name, sign):
        self.special_chr_matcher.append((name.replace("\b", ""), sign))

    def check_special_chr(self):
        check_str = "".join(self.log).lower().replace("\b", "")
        match_outcomes = []
        for key, val in self.special_chr_matcher:
            if check_str.endswith(key):
                match_outcomes.append((key, val))

        if len(match_outcomes) > 0:
            names = [outcome[0] for outcome in match_outcomes]
            result = 0
            for i in range(1, len(names)):
                if len(names[i]) > len(names[result]):
                    result = i
            self.log.clear()
            return match_outcomes[result]
        return None

    def replace_special_chr(self, name, sign):
        length = len(name)
        self.control.type("\b" * length)
        self.control.type(sign)

    def init_special_chr_matcher(self):
        # add at the end of symbol names (eg. sigma_) just to make sure that
        # user is not frustrated about wanting to write "sigma" in english, but
        # the program keeps changing it to Σ.
        execute = "_"

        # formal language signs
        self.add_special_chr("sigma" + execute, "Σ")
        self.add_special_chr("alphabet" + execute, "Σ")
        self.add_special_chr("epsilon" + execute, "ε")
        self.add_special_chr("null" + execute, "∅")
        self.add_special_chr("delta" + execute, "δ")
        self.add_special_chr("transition_function", "δ")

        # operations
        self.add_special_chr("union" + execute, "∪")
        self.add_special_chr("concat" + execute, "⋂")
        # sets
        self.add_special_chr("element_of", "∈")
        self.add_special_chr("subset_of", "⊂")
        self.add_special_chr("equal_or_subset_of", "⊆")

        # stats
        self.add_special_chr("pop_sd", "σ")
        self.add_special_chr("pop_mean", "μ")
        self.add_special_chr("sample_mean", "X̄")

    def run(self):
        while True:
            match = self.check_special_chr()
            if match is not None:
                self.replace_special_chr(match[0], match[1])


if __name__ == "__main__":
    sw = sign_writer(max_log=30)
    sw.listener.start()
    sw.init_special_chr_matcher()

    run_thread = Thread(target=sw.run, daemon=True)
    run_thread.start()
    sw.listener.join()

