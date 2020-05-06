import operator
dictn={1:2,3:4,4:3,2:1,0:0}
sorted_dict=dict(sorted(dictn.items(),key=operator.itemgetter(1)))
print("Accending order by value:",sorted_dict)
sorted_dict=dict(sorted(dictn.items(),key=operator.itemgetter(1),reverse=True))
print("Descending order by value",sorted_dict)

