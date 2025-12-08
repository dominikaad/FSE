text = ' Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())'
print(text)
while True:
    open_pos = text.find("(")
    if open_pos==0:
        break
    close_pos = text.find(")", open_pos)
    if close_pos ==-1:
        break
    tp_remove = text[open_pos:close_pos+1]
    text = text.replace(tp_remove, '', 1)
print(text)