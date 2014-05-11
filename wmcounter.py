#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2010-2014 emijrp
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import MySQLdb
import os
import re
import sys
import time

path="/data/project/wmcounter/public_html"

if os.path.exists('%s/wpcounter.log' % path):
    f=open('%s/wpcounter.log' % path, 'r')
    raw=f.read().splitlines()[0]
    f.close()
    [timestamp_old, total_old] = [int(i) for i in raw.split(';')]
else:
    [timestamp_old, total_old] = [0, 0]

print "timestamp_old =", timestamp_old, "total_old =", total_old

timestamp=int('%d' % time.time())*1000
total=0.0

conn = MySQLdb.connect(host='s3.labsdb', db='meta_p', read_default_file='~/replica.my.cnf', use_unicode=True)
cursor = conn.cursor()
cursor.execute("SELECT lang, family, slice, dbname FROM wiki WHERE 1;")
result=cursor.fetchall()
checked=0
families=["wikibooks", "wikipedia", "wiktionary", "wikimedia", "wikiquote", "wikisource", "wikinews", "wikiversity", "commons", "wikispecies", "wikidata", "wikivoyage"]
for row in result:
    lang=row[0]
    family=row[1]
    if family not in families:
        continue
    dbserver=row[2]
    dbname=row[3]+'_p'
    
    try:
        conn2 = MySQLdb.connect(host=dbserver, db=dbname, read_default_file='~/replica.my.cnf', use_unicode=True)
        cursor2 = conn2.cursor()
        #print "OK:", dbserver, dbname
        cursor2.execute("select ss_total_edits from site_stats where 1")
        result2=cursor2.fetchall()
        for row2 in result2:
            edits=int(row2[0])
            total+=edits
            checked+=1
            if edits>1:
                print "%s;%s;%s" % (edits, dbname, dbserver)

        cursor2.close()
        conn2.close()
    
    except:
        print "Error in", dbserver, dbname


print "timestamp =", timestamp, "total =", total
editrate=(total-total_old)/(timestamp-timestamp_old) # per milisecond
print "editrate =", editrate
print families
print "databases =",checked

if editrate<=0:
    sys.exit() #wait to the next update

css = u"""<style type="text/css">
<!--
body {
    margin:0;border:0;padding:0;
    font-family:monospace;
    background: #fff;
    color: #000;
    text-align: center;
}
div#wrapper{
    display:table;
    width:100%;
}
div#content{
    display:table-cell;vertical-align:middle;
    background-image: url('wplogoreduced.png');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center center;
    height:100%;
    }
span#header {
    font-size:250%;
    font-weight:bold;
    }
span#counter {
    font-size:1000%;
    font-weight:bold;
    }
p#followus, p#translateit {
    position:absolute;
    margin:0;border:0;padding:0;
    top:10;
    text-align:left;
}
p#followus {
    left:10;
}
p#translateit{
    right:10;
}
p#donate, p#author, p#f11 {
    position:absolute;
    margin:0;border:0;padding:0;
    bottom:10;
    }
p#donate {
    left:10;
    }
p#author {
    right:10;
    }
p#f11 {
    left:50%;
    width:40em;
    margin-left:-20em;
    text-align:center;
    bottom:30;
    }
-->
</style>"""

switchtraslations = u"""switch(lang){
    case "example":
        header='<a href="http://www.wikimedia.org"></a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia"></a>';
        f11='';
        author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "af":
        header='Totale wysigings in alle <a href="http://www.wikimedia.org">Wikimedia-projekte</a>:';
        spliter='&nbsp;';
        donate="<a href='http://wikimediafoundation.org/wiki/Skenk'>Skenk 'n donasie aan die Wikimedia-stigting</a>"; //be careful with 'n
        f11='Druk op F11 vir volskerm';
        author='Ontwikkel deur <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (inspirasie deur <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "als":
        header='Gsamtaazahl Bearbeitige uff de <a href="http://www.wikimedia.org">Wikimedia-Brojäkt:</a>';
        spliter='&nbsp;';
        donate="<a href='http://wikimediafoundation.org/wiki/Finanzielli_Hilf'>Understütz d'Wikimedia Foundation</a>"; //be careful with d'
        f11='Vollbild: F11';
        author='Gschribe vum <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (uff Basis vu <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ar":
        header='مجموع التعديلات في <a href="http://www.wikimedia.org">مشاريع ويكيميديا</a>:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/جمع_تبرعات">تبرع لمؤسسة ويكيميديا</a>';
        f11='للشاشة الكاملة اضغط F11';
        author='من تطوير <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (ملهمة من <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "az":
        header='<a href="http://www.wikimedia.org">Wikimedia layihəsində </a> redaktələrin ümumi sayı:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Bağışlar">Wikimedia Foundation təşkilatına ianələrin göndərilməsi</a>';
        f11='Ekranın tam açılması üçün F11 düyməsini basın';
        author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> tərəfindən (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> dəstəyi ilə) işlənmişdir';
        break;
    case "be":
        header='Агулам правак у <a href="http://www.wikimedia.org">праектах Фундацыі «Вікімэдыя»</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Ахвяруйце Фундацыі Вікімэдыя</a>';
        f11='Націсьніце F11 для поўнаэкраннага прагляду';
        author='Распрацаваў <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (ідэя <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "bg":
        header='Общ брой редакции в <a href="http://www.wikimedia.org">проектите на Уикимедия</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Подкрепете с дарение Фондация Уикимедия</a>';
        f11='Натиснете F11 за показване на голям екран';
        author='Разработено от <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (вдъхновено от <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "bn":
        header='<a href="http://www.wikimedia.org">উইকিমিডিয়ার বিভিন্ন প্রকল্পে</a> সর্বমোট সম্পাদনার সংখ্যা:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">উইকিমিডিয়া ফাউন্ডেশনে দান করুন</a>';
        f11='সম্পূর্ন স্ক্রিন জুড়ে দেখতে হলে F11 চাপুন';
        author='এই কাউন্টারটি তৈরী করেছেন <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> এর অনুপ্রেরণায়)';
        break;
    case "br":
        header='Niver hollek a gemmoù er <a href="http://www.wikimedia.org">raktresoù Wikimedia</a> :';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donezoniñ da Ziazezadur Wikimedia</a>';
        f11='Pouezit war F11 evit ar mod skramm leun';
        author='Diorroet gant <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Awenet gant <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "bs":
        header='Ukupne izmjene u svim <a href="http://www.wikimedia.org">Wikimedia projektima</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donirajte Wikimedia Fondaciji</a>';
        f11='Pritisnite F11 za prikaz preko cijelog ekrana';
        author='Razvio korisnik <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspiriran od strane <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ca":
        header='Edicions entre tots els <a href="http://www.wikimedia.org">projectes de Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Donatius">Dona a la Fundació Wikimedia</a>';
        f11='Pantalla completa pulsant F11';
        author='Desarrollat per <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspirat en <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ceb":
        header='Mga tibuok kausaban sa <a href="http://www.wikimedia.org">mga proyekto sa Wikimedya</a>:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Idonar sa Wikimedia Foundation</a>';
        f11='Tuploka ang F11 aron mapuno sa tabil';
        author='Gipalambo ni <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Nadasig sa <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "cs":
        header='Celkový počet editací v <a href="http://www.wikimedia.org">projektech nadace Wikimedia</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Sponzorství">Podpořte Wikimedia Foundation</a>';
        f11='Stisknutím klávesy F11 zobrazíte stránku na celou obrazovku';
        author='Vyvinul <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (inspirováno stránkami <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "cy":
        header='Cyfanswm yr holl olygiadau ym <a href="http://www.wikimedia.org">mhrosiectau Wikimedia</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Cyfrannwch at Sefydliad Wikimedia</a>';
        f11='Gwasgwch F11 am sgrîn lawn';
        author='Datblygwyd gan <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Ysbrydolwyd gan <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "da":
        header='Samlet antal rettelser på tværs af alle <a href="http://www.wikimedia.org">Wikimedia-projekter</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Indsamling">Giv et bidrag til Wikimedia Foundation</a>';
        f11='Tryk F11 for fuldskærmsvisning';
        author='Udviklet af <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspireret af <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "de":
        header='Gesamtzahl der Bearbeitungen in <a href="http://www.wikimedia.org">den Wikimedia-Projekten</a>:';
        spliter='&#8239;';
        donate='<a href="http://wikimediafoundation.org/wiki/Spenden">Spende an die Wikimedia Foundation</a>';
        f11='Drücken Sie F11 für Vollbild-Anzeige';
        author='Entwickelt von <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspiriert durch <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "el":
        header='Συνολικές επεξεργασίες στα <a href="http://www.wikimedia.org">εγχειρήματα του Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Κάντε δωρεά στο Ίδρυμα Wikimedia</a>';
        f11='Πατήστε F11 για πλήρη οθόνη';
        author='Αναπτύχθηκε από τον <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Εμπνευσμένο από το <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "eo":
        header='Totala nombro de redaktoj en <a href="http://www.wikimedia.org">Vikimediaj projektoj</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Monkolektado">Donaci al Fondaĵo Vikimedio</a>';
        f11='Premu F11 por plenekrana modo';
        author='Kreita de <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspirita de <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "es":
        header='Ediciones entre todos los <a href="http://www.wikimedia.org">proyectos Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Donaciones">Dona a la Fundación Wikimedia</a>';
        f11='Pantalla completa pulsando F11';
        author='Desarrollado por <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspirado en <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "et":
        header='<a href="http://www.wikimedia.org">Wikimedia projektides</a> tehtud redigeerimiste koguarv:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Anneta Wikimedia sihtasutusele</a>';
        f11='Täisekraani jaoks vajuta F11';
        author='Kasutajalt <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> eeskujul)';
        break;
    case "eu":
        header='<a href="http://www.wikimedia.org">Wikimedia proiektuetan</a> egindako eguneraketak guztira:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Dohaintzak">Wikimedia Foundazioari dohaintza egin</a>';
        f11='F11 sakatu pantaila osoan erakusteko';
        author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a>-ek garatua (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>-ek inspiratuta)';
        break;
    case "fa":
        header='مجموع ویرایش‏ها در <a href="http://www.wikimedia.org">پروژه ویکی‏مدیا</a>:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">کمک مالی به بنیاد ویکی‏مدیا</a>';
        f11='را برای نمایش تمام صفحه فشار دهید F11کلید';
        author='گسترش‌یافته بوسیله <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (با الهام از <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "fr":
        header="Nombre total d'éditions dans les <a href='http://www.wikimedia.org'>projets Wikimedia</a>:"; // be careful with d'éditions
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Faire_un_don">Donner à la Wikimedia Foundation</a>';
        f11='Appuyez sur F11 pour passer en plein écran';
        author='Développé par <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspiré par <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "hi":
        header='<a href="http://www.wikimedia.org">विकिमीडिया परियोजना</a> में कुल संपादन:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Donate/hi">विकिमीडिया फ़ौंडेशन को दान करें। </a>';
        f11='पूर्ण स्क्रीन के लिए ऍफ़११ [F11] दबाएँ।';
        author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">एमिजआरपी [emijrp]</a> द्वारा विकसित (<a href="http://www.7is7.com/software/firefox/partycounter.html">७इस७ [7is7]</a> द्वारा प्रेरित।)';
        break;
    case "hu":
        header='<a href="http://www.wikimedia.org">A Wikimédia projektek</a> együttes szerkesztésszáma:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia/hu">Támogasd a Wikimédia Alapítványt</a>';
        f11='Teljes képernyős mód: F11';
        author='Készítette: <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> ötlete alapján)';
        break;
    case "id":
        header='Jumlah suntingan di <a href="http://www.wikimedia.org">proyek Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Penggalangan_dana">Menyumbang untuk Yayasan Wikimedia</a>';
        f11='Tekan F11 untuk tampilan layar penuh';
        author='Dikembangkan oleh <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Terinspirasi dari <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "it":
        header='Modifiche totali nei <a href="http://www.wikimedia.org">progetti Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Donazioni">Fai una donazione a Wikimedia Foundation</a>';
        f11='Premi F11 per passare a schermo intero';
        author='Sviluppato da <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (ispirato da <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ja":
        header='<a href="http://www.wikimedia.org">ウィキメディア・プロジェクト</a>の総編集回数';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">ウィキメディア財団に寄付</a>';
        f11='F11キーでフルスクリーン表示';
        author='開発：<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (原案：<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "kl":
        header='Tamakkiisumik amerlassutsit aaqqissuussinerni <a href="http://www.wikimedia.org">Wikimedia suliniutaani</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Wikimedia suliniutaani tunissuteqarit</a>';
        f11='F11 tooruk tamaat saqqummissagukku';
        author='Siuarsaasuuvoq <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Peqatigalugu <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ko":
        header='<a href="http://www.wikimedia.org">위키미디어 재단에서 운영하는 프로젝트</a>의 총 편집 횟수:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">위키미디어 재단에 기부하기</a>';
        f11='F11 키를 누르면 전체 화면 모드로 전환합니다';
        author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a>이 만듬 (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>에서 영감을 얻음)';
        break;
    case "nl":
        header='Totaal aantal bewerkingen in <a href="http://www.wikimedia.org">Wikimediaprojecten</a>:';
        //spliter='&nbsp;';
        //donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia"></a>';
        //f11='';
        //author='<a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "pl":
        header='Ogólna liczba edycji w <a href="http://www.wikimedia.org">projektach Wikimedia</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Dary_pieniężne">Wesprzyj Wikimedia Foundation</a>';
        f11='Naciśnij F11, aby włączyć tryb pełnoekranowy';
        author='Stworzony przez <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (zainspirowany przez <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "pt":
        header='Total de edições nos <a href="http://www.wikimedia.org">projetos Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Coleta_de_fundos">Doe para a Fundação Wikimedia</a>';
        f11='Pressione F11 para tela cheia';
        author='Desenvolvido por <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspirado em <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ro":
        header='Numărul total de modificări în <a href="http://www.wikimedia.org">proiectele Wikimedia</a>:';
        spliter='.';
        donate='<a href="http://wikimediafoundation.org/wiki/Donaţii">Donaţi pentru Wikimedia</a>';
        f11='Apăsați F11 pentru afișarea pe tot ecranul';
        author='Dezvoltat de <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (inspirat de la <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "ru":
        header='Всего правок в <a href="http://www.wikimedia.org">проектах Викимедиа</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia/ru">Пожертвуйте «Фонду Викимедиа»</a>';
        f11='Нажмите F11 для показа на весь экран';
        author='Разработал <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Основано на <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "sv":
        header='Antal redigeringar i <a href="http://www.wikimedia.org">Wikimediaprojekten</a>:';
        spliter='&nbsp;';
        donate='<a href="http://wikimediafoundation.org/wiki/Insamling">Donera till Wikimedia Foundation</a>';
        f11='Tryck F11 för helskärm';
        author='Utvecklad av <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspirerad av <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
        break;
    case "te":
        header='<a href="http://www.wikimedia.org">వికీమీడియా ప్రాజెక్టుల</a>లో మొత్తం దిద్దుబాట్లు:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">వికీమీడియా ఫౌండేషనుకి విరాళమివ్వండి</a>';
        f11='నిండుతెర కొరకు F11 నొక్కండి';
        author='రూపొందించినది <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> ప్రేరణతో)';
        break;
    default:
        header='Total edits in <a href="http://www.wikimedia.org">Wikimedia projects</a>:';
        spliter=',';
        donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donate to Wikimedia Foundation</a>';
        f11='Press F11 for fullscreen';
        author='Developed by <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspired by <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
}"""

output=u"""<html>
<head>
<title>Wikimedia projects edits counter</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
%s
</head>
<body>
<div id='wrapper'>
<div id='content'>

<p id="followus">
<!--
Join us on <a href="http://www.facebook.com/group.php?gid=287466429242">Facebook</a> and follow us on <a href="http://twitter.com/wmcounter">Twitter</a>!<br/>
Chat with us at <a href="http://webchat.freenode.net/?randomnick=1&channels=wikimediacounter">Freenode</a><br/>-->
1 Billionth edit <a href="onebillion.png">screenshot</a>!<br/>
</p>

<p id="translateit"><a href="http://en.wikipedia.org/wiki/User:Emijrp/Wikimedia_projects_edits_counter">Translate it</a>!</p>

<span id="header">Total edits in <a href="http://www.wikimedia.org">Wikimedia projects</a>:</span><br/>

<span id='counter'>&nbsp;</span><br/>

<span id="header"><a href="http://en.wikipedia.org/wiki/User:Emijrp/All_human_knowledge">All human knowledge</a> &ndash; <a href="http://en.wikipedia.org/wiki/Wikipedia:There_is_a_deadline">There is a deadline</a></span><br/>

<p id="donate"><a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donate to Wikimedia Foundation</a></p>
<p id="f11">Press F11 for fullscreen</p>
<p id="author">Developed by <a href="http://wikitech.wikimedia.org/wiki/User:Emijrp">emijrp</a> (Inspired by <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)</p>

</div>
</div>


<script type="text/javascript">

//language
var lang="";
var spliter=",";
var header="";
var donate="";
var f11="";
var author="";
if (navigator.systemLanguage){
    lang=navigator.systemLanguage
}else if (navigator.userLanguage){
    lang=navigator.userLanguage;
}else if(navigator.language){
    lang=navigator.language;
}else{
    lang="en";
}

if (lang.length>2) { lang=lang.substring(0,2); }

%s

document.getElementById('header').innerHTML=header;
document.getElementById('donate').innerHTML=donate;
document.getElementById('f11').innerHTML=f11;
document.getElementById('author').innerHTML=author;

// These values are updated every 5 minutes
// using site_stats table from all wikis replicated in
// WMF Labs databases.
// Families updated include ["wikibooks", "wikipedia", "wiktionary", "wikimedia", "wikiquote", "wikisource", "wikinews", "wikiversity", "commons", "wikispecies", "wikidata", "wikivoyage"]
// More questions? emijrp AT gmail DOT com

var editinit=%.0f;
var timeinit=%d;
var timenow=new Date().getTime();
var period=1000/10; // period update in miliseconds
var editrate=%.4f; //per milisecond
editrate=editrate*period;
var editnow=editinit+((timenow-timeinit)/period)*editrate;
id=window.setTimeout("update();",period);
a=document.getElementById('counter');
function update() {
   timenow2=new Date().getTime();
   if (Math.round(((timenow2-timenow)/1000)+1)%%600==0) { window.setTimeout("window.location.reload();", 1100); } //refresh
   editnow=editinit+((timenow2-timeinit)/period)*editrate; //editnow+=editrate;
   editnowtext=""+Math.round(editnow)
   for(var i=3; i<editnowtext.length; i+=3) {
      editnowtext=editnowtext.replace(/(^|\s)(\d+)(\d{3})/,'$2'+spliter+'$3');
   }
   a.innerHTML=editnowtext;
   id=window.setTimeout("update();",period);
}

function adjustSizes(){
    var width=800;
    var height=600;
    if (self.innerWidth) { 
        width=self.innerWidth;
        height=self.innerHeight;
    } else if (document.documentElement && document.documentElement.clientWidth) { 
        width=document.documentElement.clientWidth;
        height=document.documentElement.clientHeight;
    } else if (document.body) {
        width=document.body.clientWidth;
        height=document.body.clientHeight;
    }
    document.getElementById('wrapper').style.height=(height-10)+'px';
    document.getElementById('header').style.fontSize=width/60+'pt';
    document.getElementById('counter').style.fontSize=width/12+'pt';
}

window.onload=adjustSizes;
window.onresize=adjustSizes;
</script>
</body>
</html>
""" % (css, switchtraslations, total, timestamp, editrate)

if total>total_old:
    f=open("%s/index.php" % path, 'w')
    f.write(output.encode("utf-8"))
    f.close()
    
    f=open('%s/wpcounter.log' % path, 'w')
    f.write("%d;%.0f" % (timestamp, total))
    f.close()
    
cursor.close()
conn.close()
