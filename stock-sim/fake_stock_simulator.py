import math
import random

def run_steps(company_brand, initial_stock):
    stock_value = initial_stock
    volatility = random.gauss(0, 1000)
    step = 0

    # 15 years
    company_life = 60 * 24 * 365 * 15

    company_history = []

    #                                          123456
    while (stock_value >= 0 and stock_value < 1000000) and step < 10000:
        # Market volatility based on atmosphere
        volatility = volatility + random.gauss(0, math.e)

        # Adding economic balance
        abs_vol = abs(volatility) 
        economic_bonus = (volatility / abs_vol * math.log(abs_vol, 42))
        
        # Value change based on brand value
        stock_flux = random.gauss(company_brand, volatility) / 42

        # Value change and economic bonus
        step_change = stock_flux + economic_bonus

        step_change_ratio = step_change / stock_value
        step_change_percent = step_change_ratio * 100

        stock_value = stock_value + step_change

        # Visuals
        visual_count = int(round(step_change))
        if visual_count > 0:
            visual_icon = '+'
        else:
            visual_icon = '-'

        visual_spike = visual_icon * abs(visual_count)

        step = step + 1
        print 'step %8d: %14.2f C: %8.2f % 8.2f%% (v: %6d e: %6.2f c: %6.2f) %s' \
            % (step, stock_value, step_change, step_change_percent, 
                volatility, economic_bonus, stock_flux, visual_spike)

    print 'simulation ended after %s steps' % step
    print 'brand value   : %7.2f' % company_brand
    print 'initial stock : %7.2f' % initial_stock

companies = []

company_brand = random.expovariate(1) * 3
initial_stock = math.floor(random.expovariate(1) * 100)

run_steps(company_brand, initial_stock)
