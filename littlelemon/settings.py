"""
Django settings for littlelemon project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)0zn411(r*jh1iwab0mjvzw*m(+kn3j@335+_cu^p*_)=-bbis"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "restaurant",
    "rest_framework", # API geliştirmek için. pip install djangorestframework
    "rest_framework.authtoken", # Token authtantication için. buraya ekledikten sonra migrate komutları çalıştırılmalı.
    "djoser",    
]

"""
Djoser, Django tabanlı projelerde kullanıcı yönetimi işlemlerini kolaylaştıran bir kütüphanedir ve kullanıcı kimlik doğrulama mekanizmalarını da içerir. Djoser, varsayılan olarak token tabanlı kimlik doğrulama mekanizmasını kullanır.
Bu durumda, Djoser'ı kullanıyorsanız ve Djoser'ın sağladığı kimlik doğrulama mekanizmasını kullanıyorsanız, ayrıca `rest_framework.authtoken` kütüphanesine ihtiyacınız olmayabilir. Djoser, kullanıcı kaydı, oturum yönetimi, token oluşturma ve doğrulama işlemlerini kendi içerisinde yönetir.
Ancak, duruma göre ihtiyaçlarınıza bağlı olarak `rest_framework.authtoken` kütüphanesini de kullanabilirsiniz. Örneğin, Djoser dışında farklı bir kimlik doğrulama yöntemi veya daha özelleştirilmiş bir kimlik doğrulama süreci uygulamak isterseniz, `rest_framework.authtoken` kütüphanesi size daha fazla esneklik sağlayabilir.
Bununla birlikte, Djoser'ın varsayılan kimlik doğrulama mekanizması genellikle ihtiyaçları karşılar ve `rest_framework.authtoken` kütüphanesine ek olarak kullanmanız gerekmez. Djoser, kullanıcı yönetimi ve token tabanlı kimlik doğrulama için kapsamlı bir çözüm sunar.
"""

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "littlelemon.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'], # Include 'templates' which is not a part of any app.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "littlelemon.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    },
    # 'mydb': {   
 
    #     'ENGINE': 'django.db.backends.mysql',   
    #     'NAME': 'my_database',   
    #     'USER': 'root',   
    #     'PASSWORD': 'your_password',   
    #     'HOST': '127.0.0.1',   
    #     'PORT': '3306',   
    #     'CONN_MAX_AGE': 300,  # Bağlantıların 300 saniye (5 dakika) açık kalmasını sağlar
    #     'OPTIONS': {   
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
    #     } 
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [ # looking for static directory which is not a part of any app.
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        #'rest_framework_xml.renderers.XMLRenderer', # pip install djangorestframework-xml
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication', # Token yöntemi ile ilerlicem.
    ),
    'DEFAULT_FILTER_BACKENDS': [ # https://www.django-rest-framework.org/api-guide/settings/#default_filter_backends
        # 'django_filters.rest_framework.DjangoFilterBackend', # Yorum satırını kaldırarak 'django_filters.rest_framework.DjangoFilterBackend' ayarını etkinleştirebilir ve filtreleme işlemlerini Django modelinizde tanımlı filtreleme özellikleriyle gerçekleştirebilirsiniz. Ancak, 'OrderingFilter' ve 'SearchFilter' ile birlikte kullanırken dikkatli olmanız ve çakışma veya yanlış sonuçlara neden olabilecek durumları kontrol etmeniz önemlidir.
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': # https://www.django-rest-framework.org/api-guide/pagination/#setting-the-pagination-style
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,
    
    'DEFAULT_THROTTLE_CLASSES': [ # https://www.django-rest-framework.org/api-guide/throttling/#setting-the-throttling-policy
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],

    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/minute',
        'user': '10/minute'
    }
}


"""
'DEFAULT_RENDERER_CLASSES':
Bu ayar, varsayılan olarak kullanılacak render sınıflarını belirtir. Render sınıfları, API yanıtlarının hangi formatlarda döndürüleceğini belirler. Bu örnekte, JSONRenderer ve BrowsableAPIRenderer sınıfları belirtilmiştir. JSONRenderer, yanıtların JSON formatında döndürülmesini sağlar ve BrowsableAPIRenderer, geliştiricilere API'yi tarayıcı üzerinde keşfetme ve test etme imkanı sağlar.

DEFAULT_AUTHENTICATION_CLASSES:
DEFAULT_AUTHENTICATION_CLASSES ayarına TokenAuthentication ve SessionAuthentication sınıflarını eklemek, Django REST Framework'ün token tabanlı kimlik doğrulama yanı sıra oturum tabanlı kimlik doğrulamayı da desteklemesini sağlar. Bu durumda, hem token tabanlı kimlik doğrulama hem de oturum tabanlı kimlik doğrulama mekanizmaları kullanılabilir.
Djoser da token tabanlı doğrulama yapıyor. DRF ile çakışır diye düşünülebilir ama djoser dokumanına göre 'rest_framework.authentication.TokenAuthentication' ifadesini yazmak gerekiyor. https://djoser.readthedocs.io/en/latest/authentication_backends.html

`DEFAULT_FILTER_BACKENDS`:
`DEFAULT_FILTER_BACKENDS` ayarı, Django REST Framework tarafından sağlanan filtreleme backend sınıflarını belirtir. Bu sınıflar, API isteklerinde filtreleme işlemlerini gerçekleştirmek için kullanılır. 
Filtreleme işlemi, API isteklerinin belirli kriterlere göre sonuçları filtrelemesini sağlar. Örneğin, bir `Order` modeline ait verileri fiyata göre sıralamak veya belirli bir kelimeyi içeren `Product` modellerini aramak gibi işlemler filtreleme ile gerçekleştirilebilir.
`DEFAULT_FILTER_BACKENDS` ayarına belirtilen filtreleme backend sınıfları, API görünümünün varsayılan olarak kullanacağı filtreleme yöntemlerini belirler. Bu örnekte, `OrderingFilter` ve `SearchFilter` sınıfları belirtilmiştir.

- `OrderingFilter`: Bu sınıf, sonuçları belirli bir sıralama kriterine göre sıralamak için kullanılır. API isteği içinde `ordering` parametresi kullanılarak sıralama kriteri belirtilebilir. Örneğin, `?ordering=price` ile sonuçları fiyata göre sıralamak mümkün olacaktır.
- `SearchFilter`: Bu sınıf, sonuçları belirli bir arama kriterine göre filtrelemek için kullanılır. API isteği içinde `search` parametresi kullanılarak arama kriteri belirtilebilir. Örneğin, `?search=keyword` ile sonuçları belirli bir kelimeyi içeren kayıtlarla sınırlamak mümkün olacaktır.

Bu yapılandırma ayarı, API görünümlerine varsayılan filtreleme yöntemlerini sağlar. Bu sayede, API isteklerine göre sonuçları sıralamak ve aramak gibi filtreleme işlemlerini kolayca gerçekleştirebilirsiniz.

'DEFAULT_PAGINATION_CLASS'`: 
Bu ayar, varsayılan sayfalandırma sınıfını belirtir. Sayfalandırma, API sonuçlarının birden fazla sayfaya bölünmesini ve kullanıcılara sayfalama bilgilerini sağlar. Bu örnekte, `PageNumberPagination` sınıfı belirtilmiştir. Bu sınıf, sonuçları sayfalara bölen ve kullanıcılara sayfalamayı kontrol etmelerini sağlayan sayfalandırma işlemlerini gerçekleştirir.
'PAGE_SIZE'`: Bu ayar, bir sayfada görüntülenecek öğe sayısını belirtir. `DEFAULT_PAGINATION_CLASS` ayarında belirtilen sayfalandırma sınıfı tarafından kullanılır. Bu örnekte, her sayfada 3 öğe görüntülenmesi için `PAGE_SIZE` değeri 3 olarak belirlenmiştir.

'DEFAULT_THROTTLE_CLASSES'`: 
Bu ayar, varsayılan throttling (hız sınırlama) sınıflarını belirtir. Throttling, API isteklerinin belirli bir hızda sınırlanmasını sağlar. Bu örnekte, `AnonRateThrottle` ve `UserRateThrottle` sınıfları belirtilmiştir. `AnonRateThrottle`, anonim kullanıcıları, `UserRateThrottle` ise kullanıcıları hız sınırlamaları için kullanır.
'DEFAULT_THROTTLE_RATES'`: Bu ayar, throttling hızlarını belirtir. Belirli throttling sınıflarına ait hız sınırlamaları tanımlanır. Bu örnekte, `anon` ve `user` isimli iki throttle hızı belirtilmiştir. `anon` hızı "1 dakikada 2 istek" olarak belirlenmiş ve anonim kullanıcıların bu hızda istek yapabileceği anlamına gelir. `user` hızı ise "1 dakikada 10 istek" olarak belirlenmiş ve kullanıcıların bu hızda istek yapabileceği anlamına gelir.

"""
DJOSER = {
    "USER_ID_FIELD": "username", # https://djoser.readthedocs.io/en/latest/settings.html
    'SERIALIZERS': { # User modeline dayanan özel bir serializer tanımladığım ve onu djoser a entegre etmek için bu kısmı yazdım.
        'user': 'restaurant.serializers.UserSerializer'
    }
}



"""
Bu örnekte, DJOSER değişkeni USER_ID_FIELD ayarını içerir. USER_ID_FIELD ayarı, Djoser tarafından kullanıcı kimlik doğrulama sürecinde kullanılacak olan kullanıcı kimlik alanını belirtir. Bu alan, kullanıcının benzersiz bir kimlik bilgisini temsil eder.
USER_ID_FIELD: Varsayılan olarak id alanını kullanır. Yani, kullanıcılar kimlik doğrulama için id alanını kullanır. Bu, kullanıcıların API isteklerinde kimlik doğrulaması yaparken id değerlerini kullanacakları anlamına gelir.
Bu örnekte USER_ID_FIELD ayarı username olarak belirlenmiştir, bu da kullanıcının username alanının kimlik doğrulama için kullanılacağı anlamına gelir. Yani, kullanıcıların giriş yaparken veya kimlik doğrulama işlemi gerçekleştirirken, kullanıcı adı (username) alanı kullanılır.
"""



"""
'django_filters.rest_framework.DjangoFilterBackend' konusuyla ilgili ilave açıklama:

"Modelinizde tanımlı filtreleme" terimi, Django modelinizde `django-filter` kütüphanesi kullanılarak belirli alanlara veya ilişkilere dayalı olarak yapılandırılmış filtreleme seçeneklerini ifade eder. Bu seçenekler, API isteklerini belirli kriterlere göre filtrelemek için kullanılabilir.

Örneğin, aşağıdaki gibi bir Django modeli düşünelim:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
```

Bu modelde, `Product` modeli ve `Category` modeli bulunmaktadır. `Product` modeli, bir ürünün adını, kategorisini, fiyatını ve kullanılabilirlik durumunu temsil ederken, `Category` modeli bir ürün kategorisini temsil eder.

`django-filter` kütüphanesi kullanılarak, `Product` modelindeki alanlara veya ilişkilere dayalı olarak filtreleme seçenekleri ekleyebiliriz. Örneğin, `Product` modelindeki ürünleri kategoriye, fiyata veya kullanılabilirlik durumuna göre filtrelemek isteyebiliriz.

```python
import django_filters

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name')
    price = django_filters.NumberFilter()
    is_available = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['category', 'price', 'is_available']
```

Yukarıdaki kodda, `ProductFilter` adında bir filtre sınıfı tanımlanmıştır. Bu sınıf, `Product` modeli üzerindeki filtreleme seçeneklerini belirtir. `CharFilter`, `NumberFilter` ve `BooleanFilter` gibi filtreleme seçenekleri kullanılarak farklı alanlara veya ilişkilere göre filtreleme yapılabilir.

Bu örnekte, `category` alanı kategorinin adına göre filtrelemek için kullanılırken, `price` alanı sayısal değerlere göre filtrelemek için kullanılır. `is_available` alanı ise boolean değere göre filtrelemek için kullanılır.

Daha sonra, `ProductFilter` sınıfını kullanarak API görünümünüzde filtreleme yapabilirsiniz. Django REST Framework ile entegre edildiğinde, `ProductFilter` sınıfını kullanarak API isteklerini belirli kriterlere göre filtreleyebilirsiniz.

```python
from rest_framework import generics

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
```

Yukarıdaki kodda, `ProductList` adında bir API görünümü sınıfı tanımlanmıştır. Bu sınıf, `Product` modelindeki verileri listeleyen bir API görünümüdür. `filterset_class` özelliği, `ProductFilter` sınıfını belirtir ve API isteklerini bu filtreleme seçenekleriyle filtreler.

Bu şekilde, modelinizde tanımlı filtreleme seçenekleriyle API isteklerini yapılandırabilir ve kullanıcılara belirli kriterlere göre filtrelenmiş sonuçlar döndürebilirsiniz.

"""