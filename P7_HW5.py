##Користувач робить внесок в розмірі n гривень строком на years років під 10% річних
##(щороку розмір його внеску збільшується на 10%. Ці гроші додаються до суми вкладу,
## і на них в наступному році теж будуть відсотки).
##Написати функцію bank, яка приймає аргументи n і years, і повертає суму,
##яка буде на рахунку користувача.

def bank (n, years):
    sum_cash = 0
    for i in range (years):
        sum_cash = (n * 0.10) + n
        n = sum_cash
    return sum_cash


n = int (input ("Input the count of cash: "))
years = int (input ("Input the count of years: "))
print ("Your's sum of money is: %.2f" %bank (n, years))
