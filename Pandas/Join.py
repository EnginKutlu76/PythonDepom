import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'Ad':["Engin", "Diyar", "Kutlu", "Pınar"],
            'Soyad':["Kutlu", "Kutlu", "Kutlu", "Derya"]
        }
data2 = {
            'id':[1,3,4,7],
            'Ad':["Ali", "Ahmet", "Mehmet","Fatma"],
            'Soyad':["Veli", "Yılmaz", "Kaya", "Ayşe"]
        }

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df, data2Df, on = 'id', how ='inner'))
print(pd.merge(data1Df, data2Df, on = 'id', how ='left'))