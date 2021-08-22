from openpyxl import Workbook
from openpyxl import load_workbook
import itertools
wb = load_workbook('stages.xlsx',)
print('sheets:',wb.sheetnames)


ws = wb['exportConvention']
names=ws['C']
firstnames = ws['D']
codes = ws['L']
sujets = ws['T']
entreprises = ws['BB']
www_entreprises = ws['BQ']

for n, fn, c, s, e,w in sorted(zip(names, firstnames, codes, sujets, entreprises,www_entreprises), key=lambda x: x[0].value):
    if c.value == 'MI6251':
       print(
           """
 - [[[{0}]]] {1} {2}, _{4}_, link:{5}[{3}], link:++{{attachmentsdir}}/{1}-{2}.pdf++[{1}-{2}.pdf],  link:++{{attachmentsdir}}/{1}-{2}-slides.pdf++[{1}-{2}-slides.pdf] 
""".format(n.value.title().replace(" ", ""), n.value.title(), fn.value.title(), e.value.title().strip(), s.value.capitalize().strip(), w.value.strip()))


