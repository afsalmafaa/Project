global location
global movie
global screen
global theater
global slot

#this function is used to capture location
def get_location():
    global location
    print('Select the city from the below option by giving there index Eg: 1 : Mumbai then press 1')
    print('1 : Mumbai')
    print('2 : Pune')
    print('3 : PUducherry')
    print('4 : Delhi')
    print('5 : Bengaluru')

    while (True):
        try:
            loc = int(input('choose your options :'))
            if loc == 1:
                location = 'Mumbai'
            elif loc == 2:
                location = 'Pune'
            elif loc == 3:
                location = 'Puducherry'
            elif loc == 4:
                location = 'Delhi'
            elif loc == 5:
                location = 'Bengaluru'
            else:
                print('please input a correct value')
                continue
            break
        except:
            print('please input a correct value')
    get_movie()

def get_movie():
    print(f'you have selected location {location}')
    global movie
    print('Great!!!! which movie you are interseted in ???')
    print('1 : Jawan')
    print('2 : Iraivan')
    print('3 : Chithha')
    print('4 : Mark Antony')
    print('5 : back')
    
    while(True):
        try:
            m = int(input('Choose your options :'))
            if m == 1:
                movie = "Jawan"
            elif m == 2:
                movie = "Iraivan"
            elif m == 3:
                movie = "Chithha"
            elif m == 4:
                movie = "Mark Antony"
            elif m == 5:
                break
            else:
                print('please input a correct value')
                continue
            break
        except:
            print('please input a correct value')
    if m == 4:
        get_location()

    get_screen()

def get_screen():
    print(f'you have selected movie {movie}')
    global screen
    print('Great !!! which effect you are interested in ???')
    print('1 : 2D')
    print('2 : 3D')
    print('3 : 4K')
    print('4 : back')

    while(True):
        try:
            m = int(input('choose your options : '))
            if m == 1:
                screen = '2D'
            elif m == 2:
                screen = '3D'
            elif m == 3:
                screen = '4K'
            elif m == 4:
                break
            else:
                print('please input a correct value')
                continue
            break
        except:
            print('please input a correct value')
    if m == 4:
        get_movie()
    get_theater()

def get_theater():
    print(f'ypu have selected screen {screen}')
    global theater
    print('Great!!! which theater you are interested in???')
    print('1 : PVR')
    print('2 : INOX')
    print('3 : WAVE')
    print('4 : back')

    while (True):
        try:
            m = int(input('choose your options : '))
            if m == 1:
                theater = 'PVR'
            elif m == 2:
                theater = 'INOX'
            elif m == 3:
                theater = 'WAVE'
            elif m == 4:
                break
            else:
                print('please input a correct value')
                continue
            break
        except:
            print('please input a correct value')
    if m == 4:
        get_screen()
    get_slot()

def get_slot():
    print(f'you have selected theater {theater}')
    global slot
    print(f'when you are available to enjoy the {movie} ???')
    print('1 : 10:00 am to 12:30 pm')
    print('2 : 1:00 pm to 3:30 pm')
    print('3 : 5:00 pm to 7:30 pm')
    print('4 : 9:00 pm to 11:30 pm')
    print('5 : back')

    while (True):
        try:
            m = int(input('choose your options : '))
            if m == 1:
                slot = '10:00 am to 12:30 pm'
            elif m == 2:
                slot = '1:00 pm to 3:30 pm'
            elif m == 3:
                slot = '5:00 pm to 7:30 pm'
            elif m == 4:
                slot = '9:00 pm to 11:30 pm'
            elif m == 5:
                break
            else:
                print('please input a correct value')
                continue
            break
        except:
            print('please input a correct value')
    if m == 5:
        get_theater()

get_location()
print(f'great to have you in {location} watching {movie} in {screen} at awesome {theater} theater on {slot}')


