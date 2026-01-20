# Posture
Kodu çalıştırın: python .\app.py
Tarayıcınızda http://localhost:5000 adresini açın
Kamera görüntüsü ve duruş analizi tarayıcıda görünecek!


Pitch:

Bel ve sırt ağrıları, dünya genelinde en yaygın görülen ve en fazla engelliliğe yol açan sağlık sorunları arasındadır.
World Spine Care verilerine göre, dünya nüfusunun yaklaşık %80’i yaşamı boyunca en az bir kez bel veya sırt ağrısı yaşamaktadır.

Bu ağrıların nedenleri çoğu zaman sanıldığı gibi karmaşık değildir. Yanlış duruş, duruş bozukluğunun farkında olmamak, düzenli esneme yapmamak ve vücudu yeterince tanımamak gibi önlenebilir faktörler başlıca sebepler arasında yer alır. İnsanlar genellikle bel ve sırt bölgelerini nasıl kullanmaları ve korumaları gerektiğini genç yaşlarda hiç düşünmez; çoğu zaman bu farkındalık ancak ağrı ortaya çıktığında oluşur. Ancak sorun başladıktan sonra bile neyin doğru, neyin yanlış olduğu tam olarak bilinmez. Bu platformda amacımız, insanları bel ve sırt sağlığı konusunda bilinçlendirmek ve doğru bilgiyi erişilebilir hale getirmektir.

Duruşunun farkında olduğunu düşünen kişiler bile, günlük yaşamda fark etmeden duruş bozukluklarıyla zaman geçirir. Çalışırken oturma şeklin, akşam televizyon karşısında dinlenirken aldığın pozisyon ya da uyku sırasında vücudunun durumu… Zihnin başka şeylerle meşgulken, zamanının büyük bir bölümünü aslında yanlış duruşlarla geçiriyor olabilirsin. Çoğu zaman neyin gerçekten bir duruş bozukluğu olduğunu ayırt etmek bile mümkün değildir. Bu platformda, medikal olmayan giyilebilir ürünümüz sayesinde duruş bozukluğu oluştuğu anda kullanıcıyı canlı olarak uyaracak ve duruş pozisyonlarını sürekli olarak kayıt altına alacağız.

Benzer şekilde, çoğu insan esneme ve hareket etmenin gerekli olduğunu bilir; ancak hangi hareketi nasıl yapması gerektiğini ve doğru yapıp yapmadığını bilemez. Platformumuz, giyilebilir ürünümüz aracılığıyla kişiye uygun esneme hareketleri önerecek, hareketleri canlı olarak takip edecek, geri bildirim ve tavsiyeler sunacak ve bu verileri düzenli olarak kaydedecektir.

Son olarak, bazen sırt ağrısının hareket bozukluğundan kaynaklandığı düşünülür; fizyoterapist dahil herkes bu yönde yorum yapabilir. Ancak kişi dikkat ediyor olsa bile, ağrının gerçekten basit bir hareket bozukluğundan mı yoksa daha farklı ve derin bir sebepten mi kaynaklandığından kimse tam olarak emin olamaz. Bel bölgesi vücudun geniş ve karmaşık bir alanıdır ve farklı sağlık sorunlarının da habercisi olabilir. Bu platform sayesinde, hareket verilerini düzenli ve doğru şekilde kayıt altına alarak, doktorların basit hareket bozukluğu ihtimalini daha hızlı elemesini ve altta yatan asıl nedenlere çok daha kısa sürede ulaşmasını mümkün hale getirmeyi hedefliyoruz.


Mimari:
3 asamada bu platform insa edilecek;
Asama 1: Herhangi bir giyilebilir donanim olmadan, sadece kameradan alinan goruntu ile posture geri bildirimi yapicaz. kisinin gercek goruntusunu degil, 3b model goruntusunu cikartip, o modelin hareketleri uzerinden geri bildirim yapicaz. 

Asama 2: Giyilebilir patchler ile canli olarak x dogrulukta posture geri bildirimleri verecegiz. Burada kullanilan donanim buyuk oranda off the shelf olacak. Platform neyin dogru neyin yanlis durus oldugunu bilecek, olcumler ile kisinin 3b modelini gosterecek ve bu durustaki bozuklugu da soyleyecek

Bu platformda, minimum seviyede 
