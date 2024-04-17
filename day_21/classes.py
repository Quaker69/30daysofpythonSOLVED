import statistics as stat


class Statistics:
    def __init__(self, ages):
        self.array = ages

    def getData(self):
        return self.array

    def count(self):
        return len(self.array)

    def sum(self):
        return sum(self.array)

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def range(self):
        return max(self.array) - min(self.array)

    def mean(self):
        return stat.mean(self.array)

    def median(self):
        return stat.median(self.array)

    def mode(self):
        mode_value = stat.mode(self.array)
        return {'mode': mode_value, 'count': self.array.count(mode_value)}

    def std(self):
        return stat.stdev(self.array)

    def var(self):
        return stat.variance(self.array)

    def freq_dist(self):
        return sorted([(self.array.count(i) * 4.0, i) for i in set(self.array)], reverse=True)

    def describe(self):
        return 'Count: %d\nSum: %d\nMin: %d\nMax: %d\nRange: %d\nMean: %d\nMedian: %d\nMode: %s\nStandard Deviation: ' \
               '%.2f\nVariance: %.2f\nFrequency Distribution: %s' % (
                   self.count(), self.sum(), self.min(), self.max(), self.range(), self.mean(), self.median(),
                   self.mode(),
                   self.std(), self.var(), self.freq_dist())


# data = Statistics(ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24,
# 33, 29, 26]) print(data.describe())

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return "%s %s is the person's name. Their income is %d and their expense is %d." % (
            self.firstname, self.lastname, self.total_income(), self.total_expense())

    def add_income(self, data):
        for k, v in data.items():
            self.incomes[k] = v
        return dict(sorted(self.incomes.items(), key=lambda x: x[1], reverse=True))

    def add_expense(self, data):
        for k, v in data.items():
            self.expenses[k] = v
        return dict(sorted(self.expenses.items(), key=lambda x: x[1], reverse=True))

    def account_balance(self):
        return self.total_income() - self.total_expense()


'''
me = PersonAccount('Rishabh', 'Agrawal', {'Salary': 150000, 'Bonus': 5500}, {'Rent': 20000, 'General': 4500})
print(me.total_income())
print(me.total_expense())
print(me.account_info())
print(me.add_income({'Diwali': 2500, 'Birthday': 5000}))
print(me.add_expense({'Tax': 2500, 'Fuel': 5000}))
print(me.account_balance())
'''