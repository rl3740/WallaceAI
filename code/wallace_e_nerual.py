from time import sleep



def timer(duration):
    '''
    this is used for control the program for a specific time
    '''
    counter = 0
    while counter < duration:
        counter+=1
        sleep(1)
    return True