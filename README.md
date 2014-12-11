## このリポジトリについて

QiitaのDjango入門の記事をベースに、Djangoにおけるテストの書き方について勉強しました．

## 参考リンク

* http://nwpct1.hatenablog.com/entry/how-to-write-unittest-on-django

    ブログ記事．テストの書き方についてまとめました．
    
* http://qiita.com/kaki_k/items/511611cadac1d0c69c54

    Django入門記事．こちらをベースにDjangoの勉強をしました．
    本当に分かりやすいチュートリアルです．感謝！


## Project Structure

```
$ tree .
.
├── README.md
├── cms
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   └── cms
│   │       ├── book_edit.html
│   │       ├── book_list.html
│   │       ├── impression_edit.html
│   │       └── impression_list.html
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_book_form.py
│   │   ├── test_book_model.py
│   │   ├── test_can_save_a_post_request.py
│   │   ├── test_impression_form.py
│   │   ├── test_impression_model.py
│   │   ├── test_redirect_correct_location.py
│   │   ├── test_return_correct_html.py
│   │   └── test_urls.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── mybook
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── bootstrap-theme.css
│   │   ├── bootstrap-theme.css.map
│   │   ├── bootstrap-theme.min.css
│   │   ├── bootstrap.css
│   │   ├── bootstrap.css.map
│   │   └── bootstrap.min.css
│   ├── fonts
│   │   ├── glyphicons-halflings-regular.eot
│   │   ├── glyphicons-halflings-regular.svg
│   │   ├── glyphicons-halflings-regular.ttf
│   │   └── glyphicons-halflings-regular.woff
│   └── js
│       ├── bootstrap.js
│       ├── bootstrap.min.js
│       └── jquery-1.11.1.min.js
└── templates
```