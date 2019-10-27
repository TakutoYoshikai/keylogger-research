import pyxhook
import datetime

log_file = "log.txt"

def datetime_str(dt):
    return dt.strftime("%Y/%m/%d %H:%M:%S:%f")[:-3]
def kbevent(event):
    now = datetime.datetime.today()
    log = open(log_file, "a")
    if event.Ascii >= 65 and event.Ascii <= 90:
        log.write(datetime_str(now) + " <uppercase>\n")
    elif event.Ascii >= 97 and event.Ascii <= 122:
        log.write(datetime_str(now) + " <lowercase>\n")
    else:
        log.write(datetime_str(now) + " <" + event.Key + ">\n")

hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
