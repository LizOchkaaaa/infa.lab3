import re
text1 = "X-O):<|=-}O8-}PX-O)"
text2 = "8-P<{PX<\;-}|X<O:<{(8-(;<)=-O:<{|X-P=-/X-O=-):<{)X<{|"
text3 = "rtyfjfjfjijieieff80OX-))))////rthjhgdfgX-);.;<}.}<=+X-)X-}}"
text4 = "01;<)2X-O{8()(-)<_)-<+tsdtfghgjhsdds%(->==+X-OX-OX-OX-O)X-O)"
text5 = "1-2%=4;{]-{=|X-OPVX-)X-)+;B-)S-)X-O(X-(<}8X-)+6-)X-O)"
print(len(re.findall(r'X-O' , text1)))
print(len(re.findall(r'X-O' , text2)))
print(len(re.findall(r'X-O' , text3)))
print(len(re.findall(r'X-O' , text4)))
print(len(re.findall(r'X-O' , text5)))
def M(message):
    n = r'([А-Я][а-я]+)(?=\s*[А-Я]\.[А-Я]\.)'
    n1 = re.compile(n)
    n2 = n1.findall(message)
    S2 = sorted(n2)
    return S2
print(M("Студент Вася вспомнил, что на своей лекции Балакшин П.В."
        " упоминал про старшекурсников, которые будут ему помогать: Анищенко А.А. и Машина Е.А."))
print(M("У меня есть четыре подруги: Кисилева А.Н. , Грудкова П.К. , Краснокожина Р.У. и Дудкина Н.О."))
print(M("С помощью ближайших «птенцов гнезда Петра» могущественного вельможи Меншикова А.Д. , начальника Тайной"
        " канцелярии Толстого Л.Н. , генерал-адмирала Апраксина Ф.М. и канцлера Головкина Г.И. , которые заручились поддержкой гвардии,"
        " на престол была возведена «кухарка» Екатерина."))
print(M("Законным наследником Петра был его внук Пётр Алексеевич, сын несчастного царевича Алексея и его супруги"
        " Вольфенбюттельская С.А."))
print(M("До 20-х годов Ленин В.И. и Сталин И.В. открыто не конфликтовали – и Владимир Ильич, и Иосиф Виссарионович были достаточно"
        " скрытными людьми."))

a = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
b = re.compile(r'@\S+\.[A-Z|a-z]\w+')

def L(email):
    if re.fullmatch(a, email):
      print("Подходит" , b.findall(email))
    else:
      print("Это не email")
L("svrvliza14@gmail.com")
L("Arnold1234@opppaa.ru")
L("imformaticAAAAAA@gmail.com")
L("...........@gmail.com")
L("TYYRYRY..@kjdhghffjj.com")