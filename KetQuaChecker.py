import sys
import requests
from bs4 import BeautifulSoup

ses = requests.Session()
resp = ses.get("http://ketqua.net")
tree = BeautifulSoup(resp.text, features="html.parser")


def all_lottery():
    list_lottery = []
    id_rs = [
        "rs_0_0",
        "rs_1_0",
        "rs_2_0",
        "rs_3_0",
        "rs_3_1",
        "rs_3_2",
        "rs_3_3",
        "rs_3_4",
        "rs_3_5",
        "rs_4_0",
        "rs_4_1",
        "rs_4_2",
        "rs_4_3",
        "rs_5_0",
        "rs_5_1",
        "rs_5_1",
        "rs_5_2",
        "rs_5_3",
        "rs_5_4",
        "rs_5_5",
        "rs_6_0",
        "rs_6_1",
        "rs_6_2",
        "rs_7_0",
        "rs_7_1",
        "rs_7_2",
        "rs_7_3",
    ]
    for idx in id_rs:
        node = tree.find("td", attrs={"id": idx})
        list_lottery.append(node.text)
    return list_lottery


list_check = [i[-2:] for i in all_lottery()]


def check_lottery():
    for arg in sys.argv[1:]:
        if arg[-2:] in list_check:
            print("Chúc mừng! Số {} của bạn đã trúng lô! ".format(arg))
        else:
            print("Rất tiếc! Số {} của bạn đã không trúng lô ngày hôm nay!"
            .format(arg))
            print("Danh sách số lô ngày hôm nay là :{}".format(list_check))
    pass


def main():

    check_lottery(15)


if __name__ == "__main__":
    main()
