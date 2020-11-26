#发工资
import money
def sendd():
    have_money = money.have_money
    if have_money == True:
        print("发工资了")
    else:
        print("没有收到工资！")
