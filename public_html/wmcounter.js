
// These values are updated every 5 minutes
// using site_stats table from all wikis replicated in
// WMF Labs databases.
// Families updated include ["wikibooks", "wikipedia", "wiktionary", "wikimedia", "wikiquote", "wikisource", "wikinews", "wikiversity", "commons", "wikispecies", "wikidata", "wikivoyage"]
// More questions? emijrp AT gmail DOT com
    
var timenow = new Date().getTime();
var period = 20; // period update in miliseconds
var spliter = ",";
var spliter_r = new RegExp(/(^|\s)(\d+)(\d{3})/);

function init() {
    adjustSizes();

    var lang = "";
    var header = "";
    var donate = "";
    var f11 = "";
    var author = "";
    if (navigator.systemLanguage) {
        lang = navigator.systemLanguage;
    }else if (navigator.userLanguage) {
        lang = navigator.userLanguage;
    }else if(navigator.language) {
        lang = navigator.language;
    }else {
        lang = "en";
    }

    if (lang.length>2) { lang=lang.substring(0,2); }

    switch(lang){
        case "example":
            header='<a href="http://www.wikimedia.org"></a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia"></a>';
            f11='';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "af":
            header='Totale wysigings in alle <a href="http://www.wikimedia.org">Wikimedia-projekte</a>:';
            spliter='&nbsp;';
            donate="<a href='http://wikimediafoundation.org/wiki/Skenk'>Skenk 'n donasie aan die Wikimedia-stigting</a>"; //be careful with 'n
            f11='Druk op F11 vir volskerm';
            author='Ontwikkel deur <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (inspirasie deur <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "als":
            header='Gsamtaazahl Bearbeitige uff de <a href="http://www.wikimedia.org">Wikimedia-Brojäkt:</a>';
            spliter='&nbsp;';
            donate="<a href='http://wikimediafoundation.org/wiki/Finanzielli_Hilf'>Understütz d'Wikimedia Foundation</a>"; //be careful with d'
            f11='Vollbild: F11';
            author='Gschribe vum <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (uff Basis vu <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "an":
            header='Edicions totals en <a href="http://www.wikimedia.org">prochectos Wikimedia</a>:';
            spliter='.';
            donate="<a href='http://wikimediafoundation.org/wiki/Support_Wikipedia'>Fer una donación t'a Fundación Wikimedia</a>"; //be careful with t'
            f11='Pretar F11 ta veyer en pantalla completa';
            author='Desembolicau por <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirau por <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ar":
            header='مجموع التعديلات في <a href="http://www.wikimedia.org">مشاريع ويكيميديا</a>:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/جمع_تبرعات">تبرع لمؤسسة ويكيميديا</a>';
            f11='للشاشة الكاملة اضغط F11';
            author='من تطوير <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (ملهمة من <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "az":
            header='<a href="http://www.wikimedia.org">Wikimedia layihəsində </a> redaktələrin ümumi sayı:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Bağışlar">Wikimedia Foundation təşkilatına ianələrin göndərilməsi</a>';
            f11='Ekranın tam açılması üçün F11 düyməsini basın';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> tərəfindən (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> dəstəyi ilə) işlənmişdir';
            break;
        case "be":
            header='Агулам правак у <a href="http://www.wikimedia.org">праектах Фундацыі «Вікімэдыя»</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Ахвяруйце Фундацыі Вікімэдыя</a>';
            f11='Націсьніце F11 для поўнаэкраннага прагляду';
            author='Распрацаваў <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (ідэя <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "bg":
            header='Общ брой редакции в <a href="http://www.wikimedia.org">проектите на Уикимедия</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Подкрепете с дарение Фондация Уикимедия</a>';
            f11='Натиснете F11 за показване на голям екран';
            author='Разработено от <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (вдъхновено от <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "bn":
            header='<a href="http://www.wikimedia.org">উইকিমিডিয়ার বিভিন্ন প্রকল্পে</a> সর্বমোট সম্পাদনার সংখ্যা:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">উইকিমিডিয়া ফাউন্ডেশনে দান করুন</a>';
            f11='সম্পূর্ন স্ক্রিন জুড়ে দেখতে হলে F11 চাপুন';
            author='এই কাউন্টারটি তৈরী করেছেন <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> এর অনুপ্রেরণায়)';
            break;
        case "br":
            header='Niver hollek a gemmoù er <a href="http://www.wikimedia.org">raktresoù Wikimedia</a> :';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donezoniñ da Ziazezadur Wikimedia</a>';
            f11='Pouezit war F11 evit ar mod skramm leun';
            author='Diorroet gant <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Awenet gant <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "bs":
            header='Ukupne izmjene u svim <a href="http://www.wikimedia.org">Wikimedia projektima</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donirajte Wikimedia Fondaciji</a>';
            f11='Pritisnite F11 za prikaz preko cijelog ekrana';
            author='Razvio korisnik <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspiriran od strane <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ca":
            header='Edicions entre tots els <a href="http://www.wikimedia.org">projectes de Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Donatius">Dona a la Fundació Wikimedia</a>';
            f11='Pantalla completa pulsant F11';
            author='Desarrollat per <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirat en <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ceb":
            header='Mga tibuok kausaban sa <a href="http://www.wikimedia.org">mga proyekto sa Wikimedya</a>:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Idonar sa Wikimedia Foundation</a>';
            f11='Tuploka ang F11 aron mapuno sa tabil';
            author='Gipalambo ni <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Nadasig sa <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "cs":
            header='Celkový počet editací v <a href="http://www.wikimedia.org">projektech nadace Wikimedia</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Sponzorství">Podpořte Wikimedia Foundation</a>';
            f11='Stisknutím klávesy F11 zobrazíte stránku na celou obrazovku';
            author='Vyvinul <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (inspirováno stránkami <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "cy":
            header='Cyfanswm yr holl olygiadau ym <a href="http://www.wikimedia.org">mhrosiectau Wikimedia</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Cyfrannwch at Sefydliad Wikimedia</a>';
            f11='Gwasgwch F11 am sgrîn lawn';
            author='Datblygwyd gan <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Ysbrydolwyd gan <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "da":
            header='Samlet antal rettelser på tværs af alle <a href="http://www.wikimedia.org">Wikimedia-projekter</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Indsamling">Giv et bidrag til Wikimedia Foundation</a>';
            f11='Tryk F11 for fuldskærmsvisning';
            author='Udviklet af <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspireret af <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "de":
            header='Gesamtzahl der Bearbeitungen in <a href="http://www.wikimedia.org">den Wikimedia-Projekten</a>:';
            spliter='&#8239;';
            donate='<a href="http://wikimediafoundation.org/wiki/Spenden">Spende an die Wikimedia Foundation</a>';
            f11='Drücke F11 für die Vollbild-Anzeige';
            author='Entwickelt von <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspiriert durch <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "el":
            header='Συνολικές επεξεργασίες στα <a href="http://www.wikimedia.org">εγχειρήματα του Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Κάντε δωρεά στο Ίδρυμα Wikimedia</a>';
            f11='Πατήστε F11 για πλήρη οθόνη';
            author='Αναπτύχθηκε από τον <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Εμπνευσμένο από το <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "eo":
            header='Totala nombro de redaktoj en <a href="http://www.wikimedia.org">Vikimediaj projektoj</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Monkolektado">Donaci al Fondaĵo Vikimedio</a>';
            f11='Premu F11 por plenekrana modo';
            author='Kreita de <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirita de <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "es":
            header='Ediciones entre todos los <a href="http://www.wikimedia.org">proyectos Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Donaciones">Dona a la Fundación Wikimedia</a>';
            f11='Pantalla completa pulsando F11';
            author='Desarrollado por <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirado en <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "et":
            header='<a href="http://www.wikimedia.org">Wikimedia projektides</a> tehtud redigeerimiste koguarv:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Anneta Wikimedia sihtasutusele</a>';
            f11='Täisekraani jaoks vajuta F11';
            author='Kasutajalt <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> eeskujul)';
            break;
        case "eu":
            header='<a href="http://www.wikimedia.org">Wikimedia proiektuetan</a> egindako eguneraketak guztira:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Dohaintzak">Wikimedia Foundazioari dohaintza egin</a>';
            f11='F11 sakatu pantaila osoan erakusteko';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a>-ek garatua (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>-ek inspiratuta)';
            break;
        case "fa":
            header='مجموع ویرایش‏ها در <a href="http://www.wikimedia.org">پروژه ویکی‏مدیا</a>:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">کمک مالی به بنیاد ویکی‏مدیا</a>';
            f11='را برای نمایش تمام صفحه فشار دهید F11کلید';
            author='گسترش‌یافته بوسیله <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (با الهام از <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "fr":
            header="Nombre total d'éditions dans les <a href='http://www.wikimedia.org'>projets Wikimedia</a>:"; // be careful with d'éditions
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Faire_un_don">Donner à la Wikimedia Foundation</a>';
            f11='Appuyez sur F11 pour passer en plein écran';
            author='Développé par <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspiré par <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "gu":
            header='<a href="http://www.wikimedia.org">વિકિમીડિયા પરિયોજના </a> માં કુલ સંપાદનો';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">વિકિમીડિયા ફાઉન્ડેશનને દાન આપો</a>';
            f11='ફુલ સ્ક્રીન માટે F11 દબાવો';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp ધ્વારા વિકસિત </a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7 ધ્વરા પ્રેરિત </a>)';
            break;
        case "hi":
            header='<a href="http://www.wikimedia.org">विकिमीडिया परियोजना</a> में कुल संपादन:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Donate/hi">विकिमीडिया फ़ौंडेशन को दान करें। </a>';
            f11='पूर्ण स्क्रीन के लिए ऍफ़११ [F11] दबाएँ।';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">एमिजआरपी [emijrp]</a> द्वारा विकसित (<a href="http://www.7is7.com/software/firefox/partycounter.html">७इस७ [7is7]</a> द्वारा प्रेरित।)';
            break;
        case "hu":
            header='<a href="http://www.wikimedia.org">A Wikimédia projektek</a> együttes szerkesztésszáma:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia/hu">Támogasd a Wikimédia Alapítványt</a>';
            f11='Teljes képernyős mód: F11';
            author='Készítette: <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> ötlete alapján)';
            break;
        case "id":
            header='Jumlah suntingan di <a href="http://www.wikimedia.org">proyek Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Penggalangan_dana">Menyumbang untuk Yayasan Wikimedia</a>';
            f11='Tekan F11 untuk tampilan layar penuh';
            author='Dikembangkan oleh <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Terinspirasi dari <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "it":
            header='Modifiche totali nei <a href="http://www.wikimedia.org">progetti Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Donazioni">Fai una donazione a Wikimedia Foundation</a>';
            f11='Premi F11 per passare a schermo intero';
            author='Sviluppato da <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (ispirato da <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ja":
            header='<a href="http://www.wikimedia.org">ウィキメディア・プロジェクト</a>の総編集回数';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">ウィキメディア財団に寄付</a>';
            f11='F11キーでフルスクリーン表示';
            author='開発：<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (原案：<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "kl":
            header='Tamakkiisumik amerlassutsit aaqqissuussinerni <a href="http://www.wikimedia.org">Wikimedia suliniutaani</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Wikimedia suliniutaani tunissuteqarit</a>';
            f11='F11 tooruk tamaat saqqummissagukku';
            author='Siuarsaasuuvoq <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Peqatigalugu <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ko":
            header='<a href="http://www.wikimedia.org">위키미디어 재단에서 운영하는 프로젝트</a>의 총 편집 횟수:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">위키미디어 재단에 기부하기</a>';
            f11='F11 키를 누르면 전체 화면 모드로 전환합니다';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a>이 만듬 (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>에서 영감을 얻음)';
            break;
        case "nl":
            header='Totaal aantal bewerkingen in <a href="http://www.wikimedia.org">Wikimediaprojecten</a>:';
            //spliter='&nbsp;';
            //donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia"></a>';
            //f11='';
            //author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "oc":
            header='Edicions totalas dins <a href="http://www.wikimedia.org">los projèctes de Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Far una donacion a la fondacion Wikimedia</a>';
            f11="Quichar sus F11 per un afichatge sus tot l'ecran";
            author='Desvolopat per <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirat de <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "pl":
            header='Ogólna liczba edycji w <a href="http://www.wikimedia.org">projektach Wikimedia</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Dary_pieniężne">Wesprzyj Wikimedia Foundation</a>';
            f11='Naciśnij F11, aby włączyć tryb pełnoekranowy';
            author='Stworzony przez <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (zainspirowany przez <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "pt":
            header='Total de edições nos <a href="http://www.wikimedia.org">projetos Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Coleta_de_fundos">Doe para a Fundação Wikimedia</a>';
            f11='Pressione F11 para tela cheia';
            author='Desenvolvido por <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirado em <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ro":
            header='Numărul total de modificări în <a href="http://www.wikimedia.org">proiectele Wikimedia</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Donaţii">Donaţi pentru Wikimedia</a>';
            f11='Apăsați F11 pentru afișarea pe tot ecranul';
            author='Dezvoltat de <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (inspirat de la <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ru":
            header='Всего правок в <a href="http://www.wikimedia.org">проектах Викимедиа</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia/ru">Пожертвуйте «Фонду Викимедиа»</a>';
            f11='Нажмите F11 для показа на весь экран';
            author='Разработал <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Основано на <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "sv":
            header='Antal redigeringar i <a href="http://www.wikimedia.org">Wikimediaprojekten</a>:';
            spliter='&nbsp;';
            donate='<a href="http://wikimediafoundation.org/wiki/Insamling">Donera till Wikimedia Foundation</a>';
            f11='Tryck F11 för helskärm';
            author='Utvecklad av <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspirerad av <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "te":
            header='<a href="http://www.wikimedia.org">వికీమీడియా ప్రాజెక్టుల</a>లో మొత్తం దిద్దుబాట్లు:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">వికీమీడియా ఫౌండేషనుకి విరాళమివ్వండి</a>';
            f11='నిండుతెర కొరకు F11 నొక్కండి';
            author='రూపొందించినది <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (<a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a> ప్రేరణతో)';
            break;
        case "tr":
            header='<a href="http://www.wikimedia.org">Wikimedia projelerindeki</a> toplam düzenleme sayısı:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Wikimedia Vakfına bağışta bulunun</a>';
            f11='Tam ekran görüntülemek için F11 tuşuna basın';
            author='<a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> tarafından geliştirilmiştir (Esin kaynağı <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        case "ur":
            header=' جملہ ترامیم در <a href="http://www.wikimedia.org">ویکیمیڈیا منصوبہ جات</a>:';
            spliter='.';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">مؤسسہ ویکیمیڈیا کو عطیہ دیں</a>';
            f11='مکمل سکرین دیکھنے کے لیے کلک رکیں F11';
            author='ترقی دہندہ <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (متاثر از <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
            break;
        default:
            header='Total edits in <a href="http://www.wikimedia.org">Wikimedia projects</a>:';
            spliter=',';
            donate='<a href="http://wikimediafoundation.org/wiki/Support_Wikipedia">Donate to Wikimedia Foundation</a>';
            f11='Press F11 for fullscreen';
            author='Developed by <a href="https://en.wikipedia.org/wiki/User:Emijrp">emijrp</a> (Inspired by <a href="http://www.7is7.com/software/firefox/partycounter.html">7is7</a>)';
    }
    
    document.getElementById('header').innerHTML = header;
    document.getElementById('donate').innerHTML = donate;
    document.getElementById('f11').innerHTML = f11;
    document.getElementById('author').innerHTML = author;
    
    window.setTimeout(update, period);
}

function update() {
   timenow2 = new Date().getTime();
   if (Math.round(((timenow2-timenow)/1000)+1) % 300 == 0) { window.setTimeout(window.location.reload(), 1100); } //refresh page
   editnow = editinit + (timenow2-timeinit) * editrate;
   editnowtext = ""+Math.round(editnow);
   for(var i=3; i<editnowtext.length; i+=3) {
      editnowtext = editnowtext.replace(spliter_r,'$2'+spliter+'$3');
   }
   document.getElementById('counter').innerHTML = editnowtext;
   window.setTimeout(update, period);
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
    document.getElementById('header').style.fontSize=width/45+'pt';
    document.getElementById('footer').style.fontSize=width/45+'pt';
    document.getElementById('counter').style.fontSize=width/12+'pt';
}

window.onload = init;
window.onresize = adjustSizes;
