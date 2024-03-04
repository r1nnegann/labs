from time import sleep
num = int(input())
milliseconds = int(input())
sleep(milliseconds*0.001)
print(f'Square root of {num} after {milliseconds} miliseconds is {num**0.5}')