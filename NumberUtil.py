import pandas as pd
from numpy import random


class NumberUtil:

    def __init__(self, start, stop, limit):
        self.start = start
        self.stop = stop
        self.limit = limit
        self.series = [random.randint(self.start, stop) for number in range(limit)]

    def get_min(self):
        return min(self.series)

    def get_max(self):
        return max(self.series)

    def get_sum(self):
        return sum(self.series)

    def get_repeating_items_amount(self):
        counts = pd.Series(self.series).value_counts()
        an_iterator = filter(lambda number: number > 1, counts)
        filtered_numbers = list(an_iterator)
        return len(filtered_numbers)

    def get_data_frame(self):
        asc_list = sorted(self.series, reverse=False)
        desc_list = sorted(self.series, reverse=True)
        data = {'Ascended': asc_list,
                'Descended': desc_list}
        df = pd.DataFrame(data)
        return df

    def get_data_frame_for_hist(self):
        asc_list = sorted(self.series, reverse=False)
        asc_round_to_hundreds = [round(num, -2) for num in asc_list]
        desc_list = sorted(self.series, reverse=True)
        desc_round_to_hundreds = [round(num, -2) for num in desc_list]
        data = {'Ascended': asc_round_to_hundreds,
                'Descended': desc_round_to_hundreds}
        df = pd.DataFrame(data)
        return df
