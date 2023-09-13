import csv
from collections import namedtuple

def read_file(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        table_name = next(reader)[0]
        fields = next(reader)
        Tuple = namedtuple(table_name, fields)
        data = {Tuple(*row) for row in reader}
    return data

suppliers = read_file('suppliers.txt')
parts = read_file('parts.txt')
projects = read_file('projects.txt')
spj = read_file('spj.txt')

bolt = {s.sname for s in suppliers for r in spj if r.sno == s.sno and 'Bolt' in (p.pname for p in parts if p.pno == r.pno)}
print(bolt)

blue  ={s.sname for s in suppliers for r in spj if r.sno == s.sno and 'Blue' in (p.color for p in parts if p.pno == r.pno)}
print(blue)

non_athens ={s.sname for s in suppliers if not any(r.jno==j.jno and j.city=='Athens'for j in projects  for r  in spj if s.sno==r.sno)}
print(non_athens)

non_oslo = {(p.pname, p.color) for p in parts if not any(r.jno == j.jno and j.city == 'Oslo' for j in projects for r in spj if r.pno == p.pno)}
print(non_oslo)

pairs_in_city = {(s1.sname, s2.sname) for s1 in suppliers for s2 in suppliers if (s1.city == s2.city and s1.sname != s2.sname)}
print(pairs_in_city)

supplier_by_city = {city: {supplier.sname for supplier in suppliers if supplier.city == city} for city in {supplier.city for supplier in suppliers}}
print(supplier_by_city)

with open("output.txt", "w") as o:
    o.write(f"{bolt}\n")
    o.write(f"{blue}\n")
    o.write(f"{non_athens}\n")
    o.write(f"{non_oslo}\n")
    o.write(f"{pairs_in_city}\n")
    o.write(f"{supplier_by_city}")