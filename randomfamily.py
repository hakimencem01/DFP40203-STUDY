import random;
family = ["Ali","Abu","Angah","Anie","Anna","Alia"];
family.append("Amira");
family.append("Afzan");
del family[(len(family)-1)];
print(" Name : ");
for eachmember in family:
    print("     - "+eachmember);
luckymember = random.choice(family);
print("\n"+luckymember+" is my lucky person");
