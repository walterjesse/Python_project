#lists in python
myclassmate=["Antonia","James","Joan","Edith","Victor"]
mynos=[3,4,6,8,5,1]
mynos.sort()
print(type(myclassmate))
myclassmate[3]="Nadia"
myclassmate.append("Daniel")
myclassmate.insert(3,"Juma")
myclassmate.insert(2, "Christine")
myclassmate.sort()
print(mynos)
print(myclassmate)
print(myclassmate[1])
print("I like  " + myclassmate[0])


#tuple in python
myfavmovies=("GOT", "Pepeta", "Famous", "Breaking bad")
print(myfavmovies)
print(myfavmovies[0])

#sets datasctructure
cars={"Benz","BMW","Volkswagen","Mazda","Ferrari"}
cars.add("Escalade")
print(cars)


#dictionaries in python
magari={
    "Name":"Mazda",
    "Model":"Demio",
    "Year":"2002"
}
print(magari)
print(magari["Model"])