# Ali Yekta CURA

import streamlit as st
import numpy as np
import pickle
from urllib.parse import urlparse
import requests
from datetime import datetime
import re
from requests.exceptions import SSLError, Timeout  # SSLError ve Timeout için bu import eklenmiştir
import ipaddress  # IP adresi doğrulamak için bu import eklenmiştir

# URL'den domain bilgisini alır
def get_domain(url):  
    domain = urlparse(url).netloc
    if re.match(r"^www.", domain):
        domain = domain.replace("www.", "")
    return domain

# URL'nin IP adresi içerip içermediğini kontrol eder
def having_ip(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip

# URL'nin içinde "@" işareti olup olmadığını kontrol eder
def have_at_sign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at

# URL'nin uzunluğunu kontrol eder
def get_length(url):
    if len(url) < 54:
        length = 0
    else:
        length = 1
    return length

# URL'nin derinliğini hesaplar
def get_depth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth + 1
    return depth

# URL'de yönlendirme olup olmadığını kontrol eder
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0

# URL'nin HTTPS kullanıp kullanmadığını kontrol eder
def http_domain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0

# URL'nin kısaltma hizmetlerini kullanıp kullanmadığını kontrol eder
def tiny_url(url):
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                          r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                          r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                          r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                          r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                          r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                          r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                          r"tr\.im|link\.zip\.net"
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0

# URL'nin ön ek veya sonek içerip içermediğini kontrol eder
def prefix_suffix(url):
    if '-' in urlparse(url).netloc:
        return 1
    else:
        return 0 

# URL'nin web trafiğini kontrol eder
def web_traffic(url):
    try:
        querystring = {"domain": url}
        headers = {
            "X-RapidAPI-Key": "cd4733fedbmsh6f2cfc21cf195f2p1d088djsn84e6c824c74e",
            "X-RapidAPI-Host": "similar-web.p.rapidapi.com"
        }
        response = requests.get("https://similar-web.p.rapidapi.com/get-analysis", headers=headers, params=querystring)
        data = response.json()
        rank = data['GlobalRank']['Rank']
        rank = int(rank)
    except (requests.exceptions.RequestException, ValueError, KeyError):
        rank = 1

    if rank < 100000:
        return 1
    else:
        return 0

# URL'nin içinde iframe etiketi olup olmadığını kontrol eder
def iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"[<iframe>|<frameBorder>]", response.text):
            return 0
        else:
            return 1

# URL'nin içinde mouseover etkinliği bulunup bulunmadığını kontrol eder
def mouse_over(response): 
    if response == "" :
        return 1
    else:
        if re.findall("<script>.+onmouseover.+</script>", response.text):
            return 1
        else:
            return 0

# URL'nin içinde sağ tıklamayı devre dışı bırakma kodu bulunup bulunmadığını kontrol eder
def right_click(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 0
        else:
            return 1

# URL'nin yönlendirmelerle ilgili olup olmadığını kontrol eder
def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1

# URL'ye HTTP yanıtını alır
def get_http_response(url):
    try:
        response = requests.get(url, timeout=5)  # 5 saniyelik bir zaman aşımı belirlendi
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

# URL'den özellikleri çıkarır
def extract_features(url):
    features = []
    
    # Adres çubuğu tabanlı özellikler
    features.append(having_ip(url))
    features.append(have_at_sign(url))
    features.append(get_length(url))
    features.append(get_depth(url))
    features.append(redirection(url))
    features.append(http_domain(url))
    features.append(tiny_url(url))
    features.append(prefix_suffix(url))

    # Alan tabanlı özellikler
    dns = 0
    dns_age = 0
    dns_end = 0
    features.append(dns)
    features.append(dns_age)
    features.append(dns_end)
    features.append(web_traffic(url))
    response = get_http_response(url)

    # HTML ve JavaScript tabanlı özellikler
    if response is not None:
        features.append(iframe(response))
        features.append(mouse_over(response))
        features.append(right_click(response))
        features.append(forwarding(response))
    else:
        # Eğer yanıt yoksa, bu özellikleri 0 veya None olarak ayarla
        features.extend([0, 0, 0, 0])

    return features

# Phishing tespiti yapar
def predict_phishing(features):
    # Modeli yükle
    with open('yekta-XGBoostClassifier.pickle.dat', 'rb') as file:
        loaded_model = pickle.load(file)

    # Tahmin yap
    new_data = np.array([features])
    prediction = loaded_model.predict(new_data)

    return prediction

def main():
    st.title('Phishing URL Detector')
    st.write("URL'nin bir phishing olup olmadığını kontrol etmek için URL girin.")

    # URL girişi
    url = st.text_input("URL'yi Girin:")

    if st.button("Kontrol Et"):
        # Özellikleri çıkar
        st.write("Özellikler çıkarılıyor...")
        features = extract_features(url)

        # Tahmin yap
        st.write("Tahmin yapılıyor...")
        prediction = predict_phishing(features)

        # Tahmini göster
        if prediction[0] == 0:
            st.write("Yapılan Tahmin:")
            st.error("Phishing Uyarısı! Bu URL phishing olarak sınıflandırılmıştır.")
        else:
            st.write("Yapılan Tahmin:")
            st.success("Phishing Tespit Edilmedi. Bu URL güvenli görünüyor.")

if __name__ == '__main__':
    main()

# Ali Yekta CURA