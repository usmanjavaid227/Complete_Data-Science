courses={
    'php':{'fee':2000,'durations':'2 months'},
    'python':{'fee':2000,'durations':'2 months'},
    'js':{'fee':2000,'durations':'2 months'}
}
# courses.update({'php':{'fee':2000,'durations':'3 months'}})
courses['python']['fee']=4000

# print(courses)
# print(courses['php'])
# print(courses['python']['fee'])

for y,z in courses.items():
    print(y,z,z['fee'])