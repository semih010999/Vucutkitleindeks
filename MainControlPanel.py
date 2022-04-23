import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,QMessageBox
from PyQt5.uic import loadUi
import graphics
import matplotlib.pyplot as plt

#------------giriş ve kayıt ekranı ilişkisi------------#
class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("LoginPage.ui",self)
        self.btngiris.clicked.connect(self.loginfunction)
        self.entry_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnkayt.clicked.connect(self.gotocreate)
        self.btngirisyapma.clicked.connect(self.gotoanaprogram)
        
    def loginfunction(self):
        con = sqlite3.connect("uyeler.db")
        cursor = con.cursor()
        usernamE=self.entry_kullanicadi.text()
        passworD=self.entry_sifre.text()
        cursor.execute("SELECT * FROM users where username = ? AND password = ?",(usernamE , passworD))
        row = cursor.fetchone()
        if row:
            cevap=QMessageBox.question(self,"GİRİŞ BAŞARILI","Giriş Başarılı!Ana menüye Devam etmek İster misiniz?",\
                    QMessageBox.Yes | QMessageBox.No)
            if cevap==QMessageBox.Yes:
                self.gotoanaprogram()
            else:
                self.show()
        else:
            QMessageBox.about(self,"GİRİŞ BAŞARISIZ","Giriş Başarısız ya da Böyle Bir Kayıt Yok!Lütfen Tekrar Deneyin.")
        cursor.connection.commit()
        
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoanaprogram(self):
        girisyapma = girisYapmadan()
        widget.addWidget(girisyapma)
        widget.setCurrentIndex(widget.currentIndex()+1)
              

class CreateAcc(QMainWindow):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("SignUpPage.ui",self)
        self.btn_kayit.clicked.connect(self.createaccfunction)
        self.entry_sifre_kayit.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        def tabloolustur():
            con = sqlite3.connect("uyeler.db")
            cursor = con.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT , username TEXT NOT NULL, password INT NOT NULL)")
        def kayitekle(self):
            con = sqlite3.connect("uyeler.db")
            cursor = con.cursor()
            userName = self.entry_kullanicadi_kayit.text()
            passWord = self.entry_sifre_kayit.text()
            dbText=f"insert into users(username,password) values('{userName}', {passWord})"
            cursor.execute(dbText)
            con.commit()
        tabloolustur()
        kayitekle(self)
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class girisYapmadan(QMainWindow):
    def __init__(self):
        super(girisYapmadan,self).__init__()
        loadUi("mainProgram.ui",self)
        self.btn_hesapla.clicked.connect(self.INDEKS)
        self.btn_cikis.clicked.connect(self.CIKIS)
        self.pushButton.clicked.connect(self.BOYKILOBILGI)
        self.btn_erkek.clicked.connect(self.ERKEKBILGI)
        self.btn_kadin.clicked.connect(self.KADINBILGI)
        self.btn_temizle.clicked.connect(self.TEMIZLE)
        self.btn_tavsiye.clicked.connect(self.TAVSIYE)
        #-----------Menübar----------#
        self.action_izgi_Grafi_i.triggered.connect(graphics.grafik_cizgi)
        self.action_ubuk_Grafi_i.triggered.connect(graphics.grafik_cubuk)
        self.actionBar_Grafi_i.triggered.connect(graphics.grafik_bar)
        self.actionNokta_Grafi_i.triggered.connect(graphics.grafik_nokta)
        self.action_izgi_Grafi_i_2.triggered.connect(self.grafik_cizgi_kisisel)
        self.action_ubuk_Grafi_i_2.triggered.connect(self.grafik_cubuk_kisisel)
        self.actionBar_Grafi_i_2.triggered.connect(self.grafik_bar_kisisel)
        self.actionNokta_Grafi_i_2.triggered.connect(self.grafik_nokta_kisisel)
        self.actionHakk_nda.triggered.connect(self.hakkindamsg)

#---------grafik kisisel------------#

    def grafik_cizgi_kisisel(self):
        plt.title("Vücut Kitle İndeksi Kişisel Grafiği")
        plt.xlabel("KİLO(KG)")
        plt.ylabel("BOY(M)")
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())

        kilo_genel = [50,55,63,71,80,89,100]
        boy_genel = [1.50,1.60,1.70,1.80,1.90,2.00,2.10]

        kilo_alma_veri = [kilo+5,kilo+13,kilo+20,kilo+29,kilo+38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_verme_veri = [kilo-5,kilo-13,kilo-20,kilo-29,kilo-38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_veri2 = [kilo,kilo,kilo,kilo,kilo]
        boy_uzama_veri = [boy,boy+0.10,boy+0.20,boy+0.30,boy+0.40]


        plt.plot(kilo_genel,boy_genel, marker=".")
        plt.plot(kilo_alma_veri,boy_veri, marker=".")
        plt.plot(kilo_verme_veri,boy_veri, marker=".")
        plt.plot(kilo_veri2,boy_uzama_veri, marker=".")
        plt.legend("OAVB",markerscale=4,title="""
-Olması gereken
-Kilo alınca
-Kilo verince
-Boy uzayınca""")
        plt.grid(True)
        plt.show()


    def grafik_bar_kisisel(self):
        plt.title("Vücut Kitle İndeksi Kişisel Grafiği")
        plt.xlabel("KİLO(KG)")
        plt.ylabel("BOY(M)")
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())

        kilo_genel = [50,55,63,71,80,89,100]
        boy_genel = [1.50,1.60,1.70,1.80,1.90,2.00,2.10]

        kilo_alma_veri = [kilo+5,kilo+13,kilo+20,kilo+29,kilo+38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_verme_veri = [kilo-5,kilo-13,kilo-20,kilo-29,kilo-38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_veri2 = [kilo,kilo,kilo,kilo,kilo]
        boy_uzama_veri = [boy,boy+0.10,boy+0.20,boy+0.30,boy+0.40]


        plt.bar(kilo_genel,boy_genel)
        plt.bar(kilo_alma_veri,boy_veri)
        plt.bar(kilo_verme_veri,boy_veri)
        plt.bar(kilo_veri2,boy_uzama_veri)
        plt.legend("OAVB",markerscale=4,title="""
-Olması gereken
-Kilo alınca
-Kilo verince
-Boy uzayınca""")
        plt.grid(True)
        plt.show()


    def grafik_nokta_kisisel(self):
        plt.title("Vücut Kitle İndeksi Kişisel Grafiği")
        plt.xlabel("KİLO(KG)")
        plt.ylabel("BOY(M)")
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())

        kilo_genel = [50,55,63,71,80,89,100]
        boy_genel = [1.50,1.60,1.70,1.80,1.90,2.00,2.10]

        kilo_alma_veri = [kilo+5,kilo+13,kilo+20,kilo+29,kilo+38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_verme_veri = [kilo-5,kilo-13,kilo-20,kilo-29,kilo-38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_veri2 = [kilo,kilo,kilo,kilo,kilo]
        boy_uzama_veri = [boy,boy+0.10,boy+0.20,boy+0.30,boy+0.40]


        plt.scatter(kilo_genel,boy_genel, marker=".")
        plt.scatter(kilo_alma_veri,boy_veri, marker=".")
        plt.scatter(kilo_verme_veri,boy_veri, marker=".")
        plt.scatter(kilo_veri2,boy_uzama_veri, marker=".")
        plt.legend("OAVB",markerscale=4,title="""
-Olması gereken
-Kilo alınca
-Kilo verince
-Boy uzayınca""")
        plt.grid(True)
        plt.show()   


    def grafik_cubuk_kisisel(self):
        plt.title("Vücut Kitle İndeksi Kişisel Grafiği")
        plt.xlabel("KİLO(KG)")
        plt.ylabel("BOY(M)")
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())

        kilo_genel = [50,55,63,71,80,89,100]
        boy_genel = [1.50,1.60,1.70,1.80,1.90,2.00,2.10]

        kilo_alma_veri = [kilo+5,kilo+13,kilo+20,kilo+29,kilo+38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_verme_veri = [kilo-5,kilo-13,kilo-20,kilo-29,kilo-38]
        boy_veri = [boy,boy,boy,boy,boy]

        kilo_veri2 = [kilo,kilo,kilo,kilo,kilo]
        boy_uzama_veri = [boy,boy+0.10,boy+0.20,boy+0.30,boy+0.40]


        plt.barh(kilo_genel,boy_genel)
        plt.barh(kilo_alma_veri,boy_veri)
        plt.barh(kilo_verme_veri,boy_veri)
        plt.barh(kilo_veri2,boy_uzama_veri)
        plt.legend("OAVB",markerscale=4,title="""
-Olması gereken
-Kilo alınca
-Kilo verince
-Boy uzayınca""")
        plt.grid(True)
        plt.show() 
          
#-----------İndeks Hesabı----------#
    def INDEKS(self):
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())
        self.sonuc = kilo/(boy*boy)
        self.label_bos_sonuc.setText(str(self.sonuc))
#-----------Çıkış----------#
    def CIKIS(self):
        cevap=QMessageBox.question(self,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                        QMessageBox.Yes | QMessageBox.No)
        if cevap==QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            self.show()  
#-----------Bilgiler----------#
    def ERKEKBILGI(self):
        self.label_bos_cinsiyet.setText("Erkek")
    def KADINBILGI(self):
        self.label_bos_cinsiyet.setText("Kadın")
    def BOYKILOBILGI(self):
        self.label_bos_boy.setText(self.line_boy.text())
        self.label_bos_kilo.setText(self.line_kilo.text())
#-----------Temizle----------#
    def TEMIZLE(self):
        self.line_boy.clear()
        self.line_kilo.clear()
        self.label_bos_boy.clear()
        self.label_bos_kilo.clear()
        self.label_bos_cinsiyet.clear()
        self.label_bos_sonuc.clear()
    
#-----------Tavsiye Mesajı----------#
    def TAVSIYE(self):
        boy = float(self.line_boy.text())
        kilo = float(self.line_kilo.text())
        self.sonuc = kilo/(boy*boy)
        self.label_bos_sonuc.setText(str(self.sonuc))

        if 0<self.sonuc<18.5:
            QMessageBox.about(self,"TAVSİYE","""Olması gerekenden zayıfsınız.Zayıflığın altında yatan nedenler arasında; az ve yetersiz beslenme,düzensiz yemek yeme yer alır.
Sağlıklı kilo almanın yolları:
-Harcadığınızdan daha fazla kalori tüketin.
-Kalori açısından yoğun ve besleyici yiyecekler tercih edin. Ceviz, fındık, badem gibi yağlı tohumlar, kuru meyveler, süt ve süt ürünleri, tahin, pekmez,
bal gibi besinleri ara öğünlerde tercih ederek günlük beslenmenizde sıklıkla yer verin.
-Öğünlerinizi düzenli bir şekilde planlayın ve en az 3 ana öğün ve 3 ara öğün yapın.
-Çabuk doygunluk hissi sağlamaması için yemeklerle beraber sıvı alımını azaltılın. Su ve diğer içecekler yemeklerden 30-45 dakika önce veya sonra
tüketilmeli,yemeklerin yanında çorba tercih edilmemeli.
-Düzenli spor yaparak kas kütlesi artırın. Bir uzman desteği alarak size uygun olan bir egzersiz programı uygulayın.
-İştahı kapatması ve metabolizmayı hızlandırıcı etkisi olması nedeniyle sigara kullanmayın.
-Düzenli ve kaliteli uyuyun.
-Karbonhidrat kaynağı olarak tam tahıllı ürünler, bulgur, kepekli makarna tercih edin.
-Kas kütlenizi de artırmak için et, balık, yumurta, süt ürünleri ve baklagil tüketin.
-Yüksek antioksidan ve enerji içeren portakal ve nar suyu gibi taze sıkılmış meyve sularını ara öğünlerde tüketin.
-Salatalarınızı zeytinyağı, zeytin, avokado gibi sağlıklı yağlarla zenginleştirin.
-İştah durumu psikolojik nedenlerden etkilenebildiği için yemek yediğiniz ortamın ferah ve keyifli olmasına özen gösterin."""
        )
        self.show()
        if 18.5<self.sonuc<24.9:
            QMessageBox.about(self,"TAVSİYE","""İdeal kilonuzdasınız.
Daha sağlıklı bir yaşam açin aşağıdaki önerilerden fayadalanın:
-Bol su için.
-Yeterli ve kaliteli uyku uyuduğunuzdan emin olun.
-Egzersiz yapın.
-Derin nefesler alın.
-Varsa bağımlılıklarınızı gözden geçirin(Yeni hobiler ile bu bağımlılıklardan kurtulabilirsiniz).
            """
        )
        self.show()
        if 25<self.sonuc<29.9:
            QMessageBox.about(self,"TAVSİYE", """Kişinin fazla kilolu olduğunu ifade eder. Diyetisyen eşliğinde sağlıklı bir şekilde kilo verilmesi tavsiye edilir.
-Erken uyuyup erken uyanırsanız; metabolizma hızınız daima hızlı olacaktır. 
-Bol su için, vücudu dinç tutar ve yağ yakımını başlatır. Ayrıca metabolizma hızını da artırır.
-Porsiyon ayarını yaparak yemek tüketirseniz kilo alımına engel olabilirsiniz.
-Sebze ve meyve vitamin kaynaklarıdır. Özellikle de C vitamini açısından zengin olan besinler zayıflamaya yardım eder.
-Ev içinde yapacağınız 45 dakikalık ev sporları sayesinde tartıdaki rakamları kolayca düşürebilirsiniz.
-Eğer gün içinde şekersiz kahve tüketirseniz kilo verme döneminde yağ yakımını daha uzun süre yaşayabilirsiniz.
-Öğünlerinizde karbonhidrat dağılımını yapmalısınız. Bakliyat bulunan bir öğünde ekmek tüketiminden uzak kalmalısınız.
-Gün içinde hücrelerin yenilenmesine destek olmak ve evde daha kolay kilo vermek için uykudan önce duş alın.    
            """
        )
        self.show()  
        if 30<self.sonuc<34.9:
            QMessageBox.about(self,"TAVSİYE", """Kişinin birinci derece obez kategorisinde yer aldığını gösterir.
-Erken uyuyup erken uyanırsanız; metabolizma hızınız daima hızlı olacaktır. 
-Bol su için, vücudu dinç tutar ve yağ yakımını başlatır. Ayrıca metabolizma hızını da artırır.
-Porsiyon ayarını yaparak yemek tüketirseniz kilo alımına engel olabilirsiniz.
-Sebze ve meyve vitamin kaynaklarıdır. Özellikle de C vitamini açısından zengin olan besinler zayıflamaya yardım eder.
-Ev içinde yapacağınız 45 dakikalık ev sporları sayesinde tartıdaki rakamları kolayca düşürebilirsiniz.
-Eğer gün içinde şekersiz kahve tüketirseniz kilo verme döneminde yağ yakımını daha uzun süre yaşayabilirsiniz.
-Öğünlerinizde karbonhidrat dağılımını yapmalısınız. Bakliyat bulunan bir öğünde ekmek tüketiminden uzak kalmalısınız.
-Gün içinde hücrelerin yenilenmesine destek olmak ve evde daha kolay kilo vermek için uykudan önce duş alın.    
            """
        )
        self.show()
        if 35<self.sonuc<39.9:
            QMessageBox.about(self,"TAVSİYE", """İkinci derece obez kategorisinde yer alan bu kişi; kalp ve damar hastalıklarına karşı savunmasızdır.
-Erken uyuyup erken uyanırsanız; metabolizma hızınız daima hızlı olacaktır. 
-Bol su için, vücudu dinç tutar ve yağ yakımını başlatır. Ayrıca metabolizma hızını da artırır.
-Porsiyon ayarını yaparak yemek tüketirseniz kilo alımına engel olabilirsiniz.
-Sebze ve meyve vitamin kaynaklarıdır. Özellikle de C vitamini açısından zengin olan besinler zayıflamaya yardım eder.
-Ev içinde yapacağınız 45 dakikalık ev sporları sayesinde tartıdaki rakamları kolayca düşürebilirsiniz.
-Eğer gün içinde şekersiz kahve tüketirseniz kilo verme döneminde yağ yakımını daha uzun süre yaşayabilirsiniz.
-Öğünlerinizde karbonhidrat dağılımını yapmalısınız. Bakliyat bulunan bir öğünde ekmek tüketiminden uzak kalmalısınız.
-Gün içinde hücrelerin yenilenmesine destek olmak ve evde daha kolay kilo vermek için uykudan önce duş alın.    
            """
        )
        self.show()
        if 40<self.sonuc<44.9:
            QMessageBox.about(self,"TAVSİYE","""Üçüncü derece obezdir. Üçüncü derece obez kategorisinde yer alan bu kişi; hızlı bir şekilde kilo vermediği takdirde kendisini birçok hastalığın pençesinde bulur.
-Şok diyetlerden uzak durun. Herkes 10 günde 10 kilo vermek ister ama her metabolizmanın bir kilo kaybı sınırı vardır.
Bu şok diyetler, hayatınızı tehlikeye atabilir.
-Öğün atlamayın. Ne yaparsanız yapın asla öğün atlamayın. Öğün kaçırırsanız yağ yakımı duracak ve kilo verimi yavaşlayacaktır.
-Erken uyuyup erken uyanırsanız; metabolizma hızınız daima hızlı olacaktır. 
-Bol su için, vücudu dinç tutar ve yağ yakımını başlatır. Ayrıca metabolizma hızını da artırır.
-Porsiyon ayarını yaparak yemek tüketirseniz kilo alımına engel olabilirsiniz.
-Sebze ve meyve vitamin kaynaklarıdır. Özellikle de C vitamini açısından zengin olan besinler zayıflamaya yardım eder.
-Ev içinde yapacağınız 45 dakikalık ev sporları sayesinde tartıdaki rakamları kolayca düşürebilirsiniz.
-Eğer gün içinde şekersiz kahve tüketirseniz kilo verme döneminde yağ yakımını daha uzun süre yaşayabilirsiniz.
-Öğünlerinizde karbonhidrat dağılımını yapmalısınız. Bakliyat bulunan bir öğünde ekmek tüketiminden uzak kalmalısınız.
-Gün içinde hücrelerin yenilenmesine destek olmak ve evde daha kolay kilo vermek için uykudan önce duş alın. 
            """
        )
        self.show()
        if 45<self.sonuc<100:
            QMessageBox.about(self,"TAVSİYE", """Süper obez olarak kabul edilir.Kişi hızlı ve sağlıklı bir şekilde kilo vermelidir.
-Şok diyetlerden uzak durun. Herkes 10 günde 10 kilo vermek ister ama her metabolizmanın bir kilo kaybı sınırı vardır.
Bu şok diyetler, hayatınızı tehlikeye atabilir.
-Öğün atlamayın. Ne yaparsanız yapın asla öğün atlamayın. Öğün kaçırırsanız yağ yakımı duracak ve kilo verimi yavaşlayacaktır. 
-Erken uyuyup erken uyanırsanız; metabolizma hızınız daima hızlı olacaktır. 
-Bol su için, vücudu dinç tutar ve yağ yakımını başlatır. Ayrıca metabolizma hızını da artırır.
-Porsiyon ayarını yaparak yemek tüketirseniz kilo alımına engel olabilirsiniz.
-Sebze ve meyve vitamin kaynaklarıdır. Özellikle de C vitamini açısından zengin olan besinler zayıflamaya yardım eder.
-Ev içinde yapacağınız 45 dakikalık ev sporları sayesinde tartıdaki rakamları kolayca düşürebilirsiniz.
-Eğer gün içinde şekersiz kahve tüketirseniz kilo verme döneminde yağ yakımını daha uzun süre yaşayabilirsiniz.
-Öğünlerinizde karbonhidrat dağılımını yapmalısınız. Bakliyat bulunan bir öğünde ekmek tüketiminden uzak kalmalısınız.
-Gün içinde hücrelerin yenilenmesine destek olmak ve evde daha kolay kilo vermek için uykudan önce duş alın.             
            """
        )
        self.show()


#-----------Hakkında Mesajı----------#
    def hakkindamsg(self):
        QMessageBox.about(self,"HAKKINDA","e posta:semih_eseroglu@hotmail.com")
           

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.show()
app.exec_()