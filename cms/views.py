from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Book


def book_list(request):
    """書籍の一覧"""
    books = Book.objects.all().order_by('id')
    return render_to_response('cms/book_list.html',  # 使用するテンプレート
                              {'books': books},       # テンプレートに渡すデータ
                              context_instance=RequestContext(request))  # その他標準のコンテキスト


def book_edit(request, book_id=None):
    """書籍の編集"""
    return HttpResponse(u'書籍の編集')


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse(u'書籍の削除')
