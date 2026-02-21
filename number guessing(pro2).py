import random
randomnum=random.randrange(1,4)
usernum=int(input('guess the number:'))

if usernum>randomnum:
    print(randomnum)
    print('the number is too high⬆️💀')

elif usernum<randomnum:
    
    print('the number is too low⬇️💀')
    

else:
    
    print('🎉Congratulation! 🎉you matched the number🥳')



