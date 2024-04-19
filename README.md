FastAPI ile Firestore Kullanarak Todo Listesi Uygulaması
Bu proje, FastAPI kullanarak basit bir Todo listesi uygulaması geliştirir. Firebase Firestore veritabanını kullanarak Todo kayıtlarını depolar ve işler. Ayrıca, HTTP istekleriyle veri iletişimi sağlar.

Gereksinimler

Python 3.7 veya üstü
FastAPI ve Firestore için gerekli kütüphaneler (örneğin, firebase-admin, uvicorn, vb.)
Firebase Firestore hesabı ve proje oluşturulması

Kurulum

Bu depoyu klonlayın:
bash
Copy code
git clone https://github.com/sizin-kullanıcı-adınız/todo-list-app.git

Firebase Firestore projeniz için bir servis hesabı anahtar dosyasını indirin ve bu dosyayı credentials.json olarak adlandırıp projenin ana dizinine yerleştirin.

Gerekli Python kütüphanelerini yükleyin:

bash
Copy code
pip install -r requirements.txt

Kullanım
Sunucuyu başlatmak için terminalde aşağıdaki komutu çalıştırın:

bash
Copy code

uvicorn main:app --reload

Tarayıcınızda http://localhost:8000 adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

API Endpointleri

Ana Sayfa: / (GET)

Uygulamaya hoş geldiniz mesajı döner.

Tüm Todo Kayıtlarını Al: /todos/all (GET)

Tüm Todo kayıtlarını Firestore veritabanından alır.

Belirli Bir Todo Kaydını Al: /todos/{doc_id} (GET)

Belirli bir Todo kaydının ayrıntılarını alır.

Yeni Todo Kaydı Oluştur: /todos (POST)

Yeni bir Todo kaydı oluşturur.

Todo Kaydını Güncelle: /todos/{doc_id} (PUT)

Belirli bir Todo kaydını günceller.

Todo Kaydını Sil: /todos/{doc_id} (DELETE)

Belirli bir Todo kaydını siler.
Notlar
Firestore veritabanı bağlantısı için credentials.json dosyasının doğru konumda olduğundan emin olun.
Kod, JWT kullanarak kimlik doğrulaması sağlar. Gerçek bir uygulamada güvenlik ihtiyaçlarınıza göre bu kodu uygun şekilde güncellemelisiniz.
Bu açıklama dosyası, projenizin kurulumu ve kullanımı hakkında temel bilgiler sağlar. İhtiyacınıza göre açıklamayı özelleştirebilirsiniz.
