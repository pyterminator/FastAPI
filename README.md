<h1 align="center">🚀 PyTerminator - FastAPI Dərslərinin Yazılı Dokumentasiyası</h1>

<p align="center">
<a href="https://www.youtube.com/@PyTerminator" target="_blank">
<img src="https://img.shields.io/badge/YouTube-PyTerminator-red?logo=youtube&logoColor=white" />
</a>
<a href="https://fastapi.tiangolo.com/" target="_blank">
<img src="https://img.shields.io/badge/Powered%20by-FastAPI-009688?logo=fastapi" />
</a>
<a href="#">
<img src="https://img.shields.io/badge/Status-Aktiv%20Layihə-success" />
</a>
</p>

## 📘 Haqqında

Bu repozitoriya **YouTube kanalımda paylaşdığım FastAPI dərslərinin yazılı izahlarını**, kod nümunələrini və real layihə tətbiqlərini özündə cəmləşdirir. Məqsəd – yalnız videoya baxmaqla kifayətlənməyəsən, həm də **praktiki və strukturlaşdırılmış dokumentasiya ilə mövzunu dərindən mənimsəyəsən**.

## 🎯 Bu sənə nə verəcək?

✅ FastAPI-nin əsas və professional səviyyələrini addım-addım öyrənmək  
✅ REST API arxitekturası üzrə real dünya nümunələri  
✅ Backend development üçün lazımi konsepsiyaları başa düşmək  
✅ YouTube dərsləri ilə sinxron yazılı tədris materialı  

## 🔗 YouTube Playlist

📺 **Bütün dərsləri izləmək üçün:**
🎯 **[PyTerminator](https://youtube.com/playlist?list=PLvAB7yjjF8026sMZvGM-N5ZNhnnYsChJk&si=XndSX5z5tIkklRlC)**


## 🙌 Sənin dəstəyin mənim üçün vacibdir!

Bu dərslərin davam etməsini istəyirsənsə:

➡️ YouTube kanalım **PyTerminator**-a abunə ol  
➡️ Bu repositoriyaya ⭐ star verərək motivasiya olmağıma kömək et


<hr>

## 🎬 1-ci Video: [FastAPI Azərbaycanca: Yükləmə və Çalışdırma](https://youtu.be/CfEeCtr_0ac)

Bu videoda aşağıdakı mövzular izah olunur:

### ✅ Virtual mühitin (venv) yaradılması
```bash
python -m venv venv
```

### ✅ Visual Studio Code-da venv aktiv edilməsi

#### ➡ Terminalda aktiv etdikdən sonra paketləri quraşdırdıq:

```bash
pip install fastapi
pip install uvicorn
```
### ✅ Layihə faylının yaradılması (index.py)
#### Burda biz bir app yaratdıq
```bash
from fastapi import FastAPI

app = FastAPI()
```

### ✅ İlk GET endpoint yazdıq
#### Base URL-ə (http://127.0.0.1:8000) sorğu göndərildikdə aşağıdakı funksiya işə düşür:

```bash
@app.get("/")
def index():
    return {
        "name": "Mushvig",
        "age": 23
    }
```

### ✅ Url-ə daxil olduqda bizə json data qaytarır 

```bash
{"name":"Mushvig","age":23}
```

### 🎯 Nəticə: Bu dərsdə FastAPI üçün lazım olan mühit quraşdırıldı, ilk API tətbiqi yaradıldı və GET sorğusuna cavab verən funksiya yazıldı.

## 🎬 2-ci Video: [FastAPI Azərbaycanca: Path parametrləri](https://youtu.be/ZpE-Si60dak)

Bu videoda aşağıdakı mövzular izah olunur:

### ✅ Path parametrləri
```bash
@myapp.get('/{age}')
def index(age:int):
    return {
        "name": "Mushvig",
        "age": age + 9
    }
```

### ✅ uvicorn index:app --reload nə deməkdir ?

- `uvicorn` – istifadə etdiyimiz server
- `index` – kodları yazdığımız Python faylının adı
- `myapp` – `index.py` faylında yaratdığımız FastAPI `app` obyekti
- `--reload` – kodlarda dəyişiklik etdikdə server avtomatik yenidən işə düşür (development mod üçün)

### 🎯 Nəticə: Bu dərsdə biz path parametrlərindən istifadə etməyi, swagger və redoc interfeyslərini, və serveri çalışdırdıqda yazdığımız əmri izah etdim.