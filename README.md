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
<details>
<summary> Açıqlama </summary>
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
</details>

<hr />

## 🎬 2-ci Video: [FastAPI Azərbaycanca: Path parametrləri](https://youtu.be/ZpE-Si60dak)
<details>
<summary> Açıqlama </summary>

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
- `app` – `index.py` faylında yaratdığımız FastAPI `app` obyekti
- `--reload` – kodlarda dəyişiklik etdikdə server avtomatik yenidən işə düşür (development mod üçün)

### 🎯 Nəticə: Bu dərsdə biz path parametrlərindən istifadə etməyi, swagger və redoc interfeyslərini, və serveri çalışdırdıqda yazdığımız əmri izah etdim.
</details>

<hr/>

## 🎬 3-cü Video: [FastAPI Azərbaycanca: Query parametrləri](https://youtu.be/yHjIigX7MOA)
<details>
<summary> Açıqlama </summary>
Bu videoda aşağıdakı mövzular izah olunur:

### ✅ Query parametrləri 
Query parametrlər URL-də verilən əlavə məlumatlardır. Onlar sorğunu daha spesifik etmək və serverə istifadəçi tərəfindən göndərilən məlumatı çatdırmaq üçün istifadə olunur.

> Məsələn, URL belə görünə bilər:  
> `http://127.0.0.1:8000/users?id=1&age=23`

### Niyə istifadə olunur?
- Sorğunu filtr etmək üçün  
- Məlumatları sıralamaq üçün  
- Optional (istəyə bağlı) məlumat göndərmək üçün 

```python
from fastapi import FastAPI
from typing import Optional

@app.get('/users')
def users(id:Optional[int]=None, age:int|None=None):
    # burda gələn parametrlərə uygun olaraq userləri filterləyib return edə bilərik
    ...
```

💡 Qeydlər:
- Query parametrlər optional ola bilər, yəni istifadəçi bu məlumatları göndərməyə də bilər.
- FastAPI-də default dəyər təyin edərək optional parametrləri idarə etmək olar.

<hr>

</details>

## 🎬 4-cü Video: [FastAPI Azərbaycanca: Serveri fərqli portda run etmək](https://youtu.be/P2IXLx7qgzs)
<details>
<summary> Açıqlama </summary>

### Port nədir ?
Kompüterdə və ya serverdə müxtəlif tətbiqlərin bir-birindən asılı olmadan eyni anda işləməsini təmin edən “giriş nöqtəsidir”.
Sadə desək, IP adres binadırsa, port həmin binadakı mənzildir. Hər xidmət (məsələn, FastAPI, MySQL, Redis və s.) öz portunda işləyir.
Məsələn:
🔹 8000 — FastAPI-nin default portu
🔹 5432 — PostgreSQL
🔹 3306 — MySQL

### Niyə portu dəyişməyə ehtiyac duyuruq?
Bəzi hallarda eyni portu başqa proqram artıq istifadə edir. Bu zaman serveri həmin portda işə salmaq mümkün olmur.
Ona görə portu dəyişmək lazım olur. Məsələn:

🔹 Eyni komputerdə bir neçə FastAPI tətbiqi işləyirsə
🔹 Backend və frontend serverləri fərqli portlarda işləməlidirsə
        - Məsələn: React → 3000, FastAPI → 8000
🔹 Və ya sadəcə test mühitində fərqli konfiqurasiyalar sınaqdan keçirilirsə
        - Məsələn: development və production üçün fərqli portlar
#### Bu hallarda portu dəyişmək, tətbiqlərin toqquşmadan (conflict) işləməsinə imkan yaradır.

### ✅ Serveri fərqli portda run edirik

- `uvicorn main:app --port 8080` əmri ilə portu dəyişmək mümkündür. Və ya :


```python
if __name__ == "__main__":
    uvicorn.run(app="index:app", port=9000, reload=True, host="127.1.1.1")
```

Portu dəyişmək üçün yuxarıdakı kod blokunda gördüyünüz formada portu dəyişmək olar.
Bu halda proyekti run etmək üçün ``` python index.py ``` əmrini terminalda yazmaq lazımdır.

</details>