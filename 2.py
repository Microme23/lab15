import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

file = 'data.csv'
fixed = pd.read_csv(file, sep=',', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True, index_col='Date')

с = fixed.select_dtypes(include='number')
md = с.resample('M').sum()
mp = md.sum(axis=1).idxmax().strftime('%B')

print(f"Найпопулярніший місяць в 2011: {mp}")

md.plot(kind='line')

plt.title('Залежність кількості велосипедистів від місяців у 2011 році')
plt.xlabel('Місяці')
plt.ylabel('Кількість велосипедистів')
plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
plt.show()