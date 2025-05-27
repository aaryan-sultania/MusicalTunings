import math

edo = int(input("Enter EDO: "))

def convert_to_cents(i):
    return 1200*math.log2(i)
def step_size(d):
    return convert_to_cents(math.pow(2,1/d))
def steps_in_interval(d, i):
    c_f = convert_to_cents(i)
    step_c = step_size(d)
    return round(c_f/step_c)

def convert_note_name(n):
    letter_name = ""
    match n[0]:
        case 0:
            letter_name = "F"
        case 1:
            letter_name = "C"
        case 2:
            letter_name = "G"
        case 3:
            letter_name = "D"
        case 4:
            letter_name = "A"
        case 5:
            letter_name = "E"
        case 6:
            letter_name = "B"
    accidentals = ""
    match n[1]:
        case -7:
            accidentals = "bbbbbbb"
        case -6:
            accidentals = "bbbbbb"
        case -5:
            accidentals = "bbbbb"
        case -4:
            accidentals = "bbbb"
        case -3:
            accidentals = "bbb"
        case -2:
            accidentals = "bb"
        case -1:
            accidentals = "b"
        case 0:
            accidentals = ""
        case 1:
            accidentals = "#"
        case 2:
            accidentals = "##"
        case 3:
            accidentals = "###"
        case 4:
            accidentals = "####"
        case 5:
            accidentals = "#####"
        case 6:
            accidentals = "######"
        case 7:
            accidentals = "#######"
        
    return letter_name + accidentals
    
def name_fifth_down(prev):
    new_name = [prev[0], prev[1]]
    new_name[0] -= 1
    if new_name[0] < 0:
        new_name[0] = 6
        new_name[1] -= 1
    return new_name
def name_fifth_up(prev):
    new_name = [prev[0], prev[1]]
    new_name[0] += 1
    if new_name[0] > 6:
        new_name[0] = 0
        new_name[1] += 1
    return new_name

notes = []
for i in range(edo):
    notes.append([i, round(i*step_size(edo), 2), None, None])
print(len(notes[1]))

current_note = 0
last_name = None
while True:
    if notes[current_note][2]:
        break
    new_name = []
    if not last_name:
        new_name = [3, 0]
    else:
        new_name = name_fifth_up(last_name)
    notes[current_note][2] = new_name
    last_name = new_name
    current_note += steps_in_interval(edo, 3/2)
    current_note %= edo

current_note = 0
last_name = None
while True:
    if notes[current_note][3]:
        break
    new_name = []
    if not last_name:
        new_name = [3, 0]
    else:
        new_name = name_fifth_down(last_name)
    notes[current_note][3] = new_name
    last_name = new_name
    current_note -= steps_in_interval(edo, 3/2)
    current_note %= edo


notable_intervals = (9/8, 10/9, 8/7, 3/2, 5/4, 6/5, 7/4, 7/6, 9/7)
notable_intervals_strings = ("9/8 ", "10/9 ", "8/7 ", "3/2 ", "5/4 ", "6/5 ", "7/4 ", "7/6 ", "9/7 ")
for note in notes:
    notable_interval_string = ""
    for i, noteable_interval in enumerate(notable_intervals):
        if (note[0] == steps_in_interval(edo, noteable_interval)):
            notable_interval_string += notable_intervals_strings[i]
    print(note[0], note[1], convert_note_name(note[2]), convert_note_name(note[3]), notable_interval_string)