#查询工资
import money

def selectx():
    saved_monye = money.saved_monye
    if  money.have_money == True:
        print(f"我有存款:{saved_monye+1000}")
    else:
        print(f"我有存款:{saved_monye}")

print(1111)
