# encoding:utf8
year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
           print("{0} 二月 29 天".format(year)) # 整百年能被400整除的是闰年
        else:
            print("{0} 二月 28 天".format(year))
    else:
        print("{0} 二月 29 天".format(year)) # 非整百年能被4整除的为闰年
else:
   print("{0} 二月 28 天".format(year))