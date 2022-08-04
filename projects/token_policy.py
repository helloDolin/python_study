

def calculate(sell_price_begin, sell_price_end, sell_count_total, sell_count_begin, plan_sell_counts):
    ''' 策略计算：范围开始价格、范围结束价格、token 总个数、开始价格个数、挂几单 '''
    price_range = sell_price_end - sell_price_begin
    print('价格区间:%s \n' % (price_range))

    price_step = price_range / plan_sell_counts
    print(f'价格步长：{price_step} \n')

    price_arr = []
    while sell_price_begin < sell_price_end:
        price_arr.append(sell_price_begin)
        sell_price_begin += price_step
    print(f'挂单：{price_arr} \n')

    # 等比数列的和
    count_x = 0
    for i in range(0, int(plan_sell_counts)):
        count_x += i
    print('预求 x 个数 : %s \n' % count_x)

    # 每次加的个数
    x = (sell_count_total - (sell_count_begin * plan_sell_counts)) / count_x
    print('每次加的个数 x 值为: %s \n' % x)

    final_arr = []
    for i, obj in enumerate(price_arr):
        dic = {
            'price': obj,
            'count': sell_count_begin + i * x
        }
        print(dic)
        final_arr.append(dic)

    sum_income = 0.0
    for item in final_arr:
        per_income = float(item['price']) * float(item['count'])
        sum_income += per_income

    print('\n')
    print('final 均价: %s' % (sum_income / sell_count_total))


def main():
    # 策略
    sell_price_begin = 60000  # 第一单的价格
    sell_price_end = 69000  # 最后一单的价格
    sell_count_total = 20  # token 总数
    sell_count_begin = 0.1  # 第一单的个数
    plan_sell_counts = 10  # 计划挂几单

    calculate(sell_price_begin, sell_price_end, sell_count_total,
              sell_count_begin, plan_sell_counts)


if __name__ == '__main__':
    main()
