from pynput.mouse import Listener

_record = []
maximum_record_length = 0
_record_length = len(_record)


def _append_record(element):
    global _record, maximum_record_length, _record_length
    _record.append(element)
    _record_length += 1
    if _record_length > maximum_record_length:
        del _record[0]
        _record_length -= 1


def get_record():
    global _record
    return _record


def _on_move(x, y):
    _append_record((x, y))


def run():
    global maximum_record_length
    if maximum_record_length == 0:
        maximum_record_length = int(input("Enter the maximum length of list that logs mouse positions upon movement: "))
    while maximum_record_length <= 0:
        maximum_record_length = int(input("Maximum length of record should be at least 1. Please re-enter the value: "))
