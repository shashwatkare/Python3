def main():
    monthlySales = inputSales()
    countyTax = calcCounty(monthlySales)
    stateTax = calcState(monthlySales)
    totalTax = calcTotal(countyTax, stateTax)
    printInfo (countyTax, stateTax, monthlySales, totalTax)
def inputSales():
    monthlySales = float(input ("Enter sales for the month: "))
    return monthlySales
def calcCounty(monthlySales):
    countyTax = monthlySales * .025
    return countyTax
def calcState (monthlySales):
    stateTax = monthlySales * .05
    return stateTax
def calcTotal (countyTax, stateTax):
    totalTax = countyTax + stateTax
    return totalTax
def printInfo (countyTax, stateTax, monthlySales, totalTax):
    print ("There were $", monthlySales, "in sales")
    print ("The county tax is $", countyTax)
    print ("The state tax is $", stateTax)
    print ("The total tax is $", totalTax)
main()
