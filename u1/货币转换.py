F = input('')
if F[:3] in ['USD']:
    print('RMB{:.2f}'.format(eval(F[3:])*6.78))
else:
    print('USD{:.2f}'.format(eval(F[3:])/6.78))
    