#118p 혼자
#star 함수 정의
def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        str = (mark*repeat)
        for j in range(2, repeat):
            str += (space * space_repeat) + (mark*repeat)
        print(str)

star("※", 3, "_", 2, 4)
print("=-=-=-=-=-=-=-=-=")
star(mark = "*", repeat = 2, space = "+", space_repeat = 3, line = 5)
print("=-=-=-=-=-=-=-=-=")

def star2(mark, repeat, space, space_repeat, line):
    string = mark*repeat + space*space_repeat + mark*repeat
    for n in range(line):
        print(string)

star2("＠", 3, "_", 2, 3)
print("=-=-=-=-=-=-=-=-=")
star2(mark="＠", repeat=3, space="_", space_repeat=2, line=3)