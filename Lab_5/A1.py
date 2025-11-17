text = ' Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())'
position_left = text.rfind('(')
position_right = text.rfind(')')
text = text.replace(text[position_left:position_right + 1], '')
print(text)
