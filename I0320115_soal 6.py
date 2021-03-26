# SOAL NO 6
a = 4
b = 11
c = 0
print('Nilai : ',a,' , binary :',format(a,'08b'))
print('Nilai : ',b,' , binary :',format(b,'08b'))

c = a | b;
print('Line 1 - Value of c is ',c,', binary :',format(c,'08b'))

c = 4 >> 11;
print('Line 2 - Value of c is ',c,', binary :',format(c,'08b'))

c = 4 ^ 11;
print('Line 3 - Value of c is ',c,', binary :',format(c,'08b'))

c = ~4;
print('Line 4 - Value of c is ',c,', binary :',format(c,'08b'))

c = 11 & 4;
print('Line 5 - Value of c is ',c,', binary :',format(c,'08b'))
