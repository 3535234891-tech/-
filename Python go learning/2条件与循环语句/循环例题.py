
sum = 10000
for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效分{num},不发工资，下一位")
    else:#此时员工绩效够了，根据账户余额去判断是否发工资
        if sum >= 1000:
           sum -= 1000
           print(f"员工{i},绩效分{num},发工资1000，还剩{sum}")
        else:
           print(f"账户余额不足，当前余额{sum}元,不足以发工资了")
           break
