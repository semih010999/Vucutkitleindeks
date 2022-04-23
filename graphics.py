import matplotlib.pyplot as plt
import numpy as np


def grafik_cizgi():
    plt.title("Vücut Kitle İndeksi Genel Grafiği")
    plt.xlabel("KİLO(KG)")
    plt.ylabel("BOY(CM)")

    erkek_kilo = [50,55,63,71,80]
    erkek_boy = [150,160,170,180,190]

    kadin_kilo = [50,51,60,69,78]
    kadin_boy = [150,160,170,180,190]


    plt.plot(erkek_kilo,erkek_boy, marker=".")
    plt.plot(kadin_kilo,kadin_boy, marker=".")
    plt.legend("EK")
    plt.grid(True)
    plt.show()

def grafik_bar():
    plt.title("Vücut Kitle İndeksi Genel Grafiği")
    plt.xlabel("KİLO(KG)")
    plt.ylabel("BOY(CM)")


    erkek_kilo = [50,55,63,71,80]
    erkek_boy = [150,160,170,180,190]

    kadin_kilo = [49,51,60,69,78]
    kadin_boy = [150,160,170,180,190]


    plt.bar(erkek_kilo,erkek_boy)
    plt.bar(kadin_kilo,kadin_boy)
    plt.legend("EK")
    plt.show()

def grafik_nokta():
    plt.title("Vücut Kitle İndeksi Genel Grafiği")
    plt.xlabel("KİLO(KG)")
    plt.ylabel("BOY(CM)")


    erkek_kilo = [50,55,63,71,80]
    erkek_boy = [150,160,170,180,190]

    kadin_kilo = [49,51,60,69,78]
    kadin_boy = [150,160,170,180,190]


    plt.scatter(erkek_kilo,erkek_boy, marker=".")
    plt.scatter(kadin_kilo,kadin_boy, marker=".")
    plt.legend("EK")
    plt.grid(True)
    plt.show()

def grafik_cubuk():
    plt.title("Vücut Kitle İndeksi Genel Grafiği")
    plt.xlabel("BOY(CM)")
    plt.ylabel("KİLO(KG)")


    erkek_kilo = [50,55,63,71,80]
    erkek_boy = [150,160,170,180,190]

    kadin_kilo = [49,51,60,69,78]
    kadin_boy = [150,160,170,180,190]


    plt.barh(erkek_kilo,erkek_boy)
    plt.barh(kadin_kilo,kadin_boy)
    plt.legend("EK")
    plt.show()


