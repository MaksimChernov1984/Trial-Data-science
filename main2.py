import matplotlib.pyplot as plt


figure = plt.figure()

# график 1
ax1 = figure.add_subplot(1, 2, 1)

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
cpt = [120, 178, 205, 215, 301, 312, 215, 345, 350, 457, 420, 425]

ax1.plot(years, cpt, color='#002', linestyle='--', marker='o', label='Oпыты Сз', linewidth=1)
ax1.grid(color='#002', linewidth=0.5)
ax1 = plt.gca()
ax1.set_facecolor('#eff')  # цвет фона графика

ax1.set_xlim(2009, 2022)
ax1.set_ylim(0, 500)

ax1.set_title('График количества опытов \nстатического зондирования \nза 2010-2021 гг.')
ax1.set_xlabel('Годы')
ax1.set_ylabel('количество опытов')
ax1.legend(loc='lower right')


# график 2
ax2 = figure.add_subplot(1, 2, 2)
labels = ['Жилое', 'Промышленное', 'Общественное', 'Инфраструктурное']
percent = [33, 28, 21, 18]
ax2.pie(percent, labels=labels, shadow=True, autopct='%1.0f%%', startangle=10)
ax2.set_title('Виды строительства \nза 2010-2021 гг.')



plt.show()  # показ всех графиков
