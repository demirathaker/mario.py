height = int(input('enter pyramid height'))
#enter again if input is negative/decimal etc

for i in range(height):
     print((' ' * (height-i)) ,'#' * (i+2))



