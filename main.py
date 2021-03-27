import NumberUtil
import matplotlib.pyplot as plt

Start = -10000
Stop = 10000
Limit = 1000

numbersUtil = NumberUtil.NumberUtil(Start, Stop, Limit)


def show_graph():
    df = numbersUtil.get_data_frame()
    plt.plot('Ascended', 'Descended', data=df, marker='o', markerfacecolor='red', markersize=1, color='red',
             linewidth=2)
    plt.plot('Ascended', 'Ascended', data=df, marker='o', markerfacecolor='blue', markersize=1, color='skyblue',
             linewidth=2)
    plt.legend()
    plt.show()


def show_hist():
    df = numbersUtil.get_data_frame_for_hist()
    plt.hist(df)
    plt.show()


print(f' Все элементы {numbersUtil.series}.')
print(f' Минимальное значение {numbersUtil.get_min()}.')
print(f' Максимальное значение {numbersUtil.get_max()}.')
print(f' Сумма значений {numbersUtil.get_sum()}.')
print(f' Повторяющиеся элементы {numbersUtil.get_repeating_items_amount()}.')
print(f' Data Frame  {numbersUtil.get_data_frame()}.')
if __name__ == "__main__":
    show_graph()
    show_hist()
